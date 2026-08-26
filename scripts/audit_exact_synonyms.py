#!/usr/bin/env python3
"""Audit exact synonyms supplied by TraitRecord ontology groundings.

The review has two deliberately separate products:

* ``trait_exact_synonym_audit.tsv`` checks every primary identifier and xref
  against predicate-scoped ontology annotations.  Only the canonical label and
  ``hasExactSynonym``/``EXACT`` values count as exact evidence.
* ``trait_exact_match_candidates.tsv`` lists external ontology terms whose
  canonical label or declared exact synonym matches a TraitRecord label.  These
  are candidates, not mappings: identical strings do not prove identical
  meaning.

Direct OBO/OWL snapshots are authoritative for the report.  OAK is used as an
independent API cross-check for groundings already asserted by the corpus.  The
script is network-free; download snapshots separately (the review document
records the official URLs and checksums).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import rdflib
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
# Backward-compatible alias used by helpers and focused tests.
ROOT = REPO_ROOT
TRAITS_DIR = REPO_ROOT / "data" / "traits"
DEFAULT_AUDIT = REPO_ROOT / "reports" / "trait_exact_synonym_audit.tsv"
DEFAULT_CANDIDATES = REPO_ROOT / "reports" / "trait_exact_match_candidates.tsv"
DEFAULT_COLLISIONS = REPO_ROOT / "reports" / "exact_synonym_collisions.tsv"
DEFAULT_MANIFEST = REPO_ROOT / "reports" / "ontology_snapshot_manifest.tsv"
DEFAULT_CAUSAL = REPO_ROOT / "reports" / "causal_grounding_exactness.tsv"
DEFAULT_DECISIONS = REPO_ROOT / "mappings" / "trait_exact_match_review.tsv"
OIO = rdflib.Namespace("http://www.geneontology.org/formats/oboInOwl#")
RDFS = rdflib.RDFS
OWL = rdflib.OWL

# File names used by the direct-download review.  Missing files are reported,
# not silently replaced with an ontology search endpoint.
SNAPSHOT_FILES = {
    "METPO": "metpo.owl",
    "GO": "go.obo",
    "CHEBI": "chebi.obo",
    "ENVO": "envo.obo",
    "PATO": "pato.obo",
    "RO": "ro.obo",
}
SNAPSHOT_URLS = {
    "METPO": "https://w3id.org/metpo/metpo.owl",
    "GO": "https://purl.obolibrary.org/obo/go/go-basic.obo",
    "CHEBI": "https://purl.obolibrary.org/obo/chebi.obo",
    "ENVO": "https://purl.obolibrary.org/obo/envo.obo",
    "PATO": "https://purl.obolibrary.org/obo/pato.obo",
    "RO": "https://purl.obolibrary.org/obo/ro.obo",
}


@dataclass(frozen=True)
class Term:
    curie: str
    label: str
    exact_synonyms: tuple[str, ...]
    definition: str = ""
    obsolete: bool = False


@dataclass(frozen=True)
class Snapshot:
    prefix: str
    path: Path
    version: str
    sha256: str
    terms: dict[str, Term]


def normalize(text: str) -> str:
    """Minimal lexical normalization; do not erase semantic punctuation."""
    return " ".join(unicodedata.normalize("NFC", text).split()).casefold()


def _write_tsv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_obo(prefix: str, path: Path) -> Snapshot:
    version = ""
    terms: dict[str, Term] = {}
    synonym_re = re.compile(r'^synonym:\s+"((?:\\.|[^"\\])*)"\s+EXACT\b')
    definition_re = re.compile(r'^def:\s+"((?:\\.|[^"\\])*)"')
    curie = label = ""
    definition = ""
    exact: list[str] = []
    obsolete = False
    in_entity = False

    def unescape(value: str) -> str:
        return re.sub(r"\\(.)", lambda match: {"n": "\n", "t": "\t"}.get(match.group(1), match.group(1)), value)

    def flush() -> None:
        nonlocal curie, label, definition, exact, obsolete
        if curie.startswith(f"{prefix}:") and label:
            terms[curie] = Term(curie, label, tuple(dict.fromkeys(exact)), definition, obsolete)
        curie = label = definition = ""
        exact = []
        obsolete = False

    # A small streaming parser is intentional.  ENVO currently contains a
    # backslash-escaped comma in an xref that strict OBO parsers reject even
    # though labels and synonym clauses remain perfectly readable.
    with path.open(encoding="utf-8", errors="replace") as fh:
        for raw_line in fh:
            line = raw_line.rstrip("\r\n")
            if line.startswith("[") and line.endswith("]"):
                if in_entity:
                    flush()
                in_entity = line in {"[Term]", "[Typedef]", "[Instance]"}
                continue
            if not in_entity:
                if not version and line.startswith(("data-version:", "date:")):
                    version = line.split(":", 1)[1].strip()
                continue
            if line.startswith("id:"):
                curie = line.split(":", 1)[1].strip()
            elif line.startswith("name:"):
                label = unescape(line.split(":", 1)[1].strip())
            elif line == "is_obsolete: true":
                obsolete = True
            else:
                match = synonym_re.match(line)
                if match:
                    exact.append(unescape(match.group(1)))
                else:
                    match = definition_re.match(line)
                    if match:
                        definition = unescape(match.group(1))
    if in_entity:
        flush()
    return Snapshot(prefix, path, version, _sha256(path), terms)


def parse_metpo_owl(path: Path) -> Snapshot:
    graph = rdflib.Graph()
    graph.parse(path)
    version = ""
    ontology = next(graph.subjects(rdflib.RDF.type, OWL.Ontology), None)
    if ontology is not None:
        values = list(graph.objects(ontology, OWL.versionInfo)) or list(
            graph.objects(ontology, OWL.versionIRI)
        )
        if values:
            version = str(values[0])
    terms: dict[str, Term] = {}
    prefix = "https://w3id.org/metpo/"
    subjects = set(graph.subjects(RDFS.label, None))
    for subject in subjects:
        uri = str(subject)
        if not uri.startswith(prefix):
            continue
        local_id = uri[len(prefix) :]
        if not local_id.isdigit():
            continue
        labels = [str(value) for value in graph.objects(subject, RDFS.label)]
        if not labels:
            continue
        exact = tuple(dict.fromkeys(str(value) for value in graph.objects(subject, OIO.hasExactSynonym)))
        deprecated = any(str(value).casefold() == "true" for value in graph.objects(subject, OWL.deprecated))
        curie = f"METPO:{local_id}"
        definitions = [
            str(value)
            for value in graph.objects(subject, rdflib.URIRef("http://purl.obolibrary.org/obo/IAO_0000115"))
        ]
        terms[curie] = Term(curie, labels[0], exact, definitions[0] if definitions else "", deprecated)
    return Snapshot("METPO", path, version, _sha256(path), terms)


def load_snapshots(snapshot_dir: Path | None) -> tuple[dict[str, Snapshot], list[dict[str, str]]]:
    snapshots: dict[str, Snapshot] = {}
    manifest: list[dict[str, str]] = []
    for prefix, filename in SNAPSHOT_FILES.items():
        if snapshot_dir is None:
            path = REPO_ROOT / "data" / "raw" / "metpo.owl" if prefix == "METPO" else Path()
        else:
            path = snapshot_dir / filename
        if not path or not path.is_file():
            manifest.append({
                "ontology": prefix,
                "version": "",
                "bytes": "0",
                "sha256": "",
                "file": filename,
                "source_url": SNAPSHOT_URLS[prefix],
                "status": "MISSING",
            })
            continue
        snapshot = parse_metpo_owl(path) if prefix == "METPO" else parse_obo(prefix, path)
        snapshots[prefix] = snapshot
        manifest.append({
            "ontology": prefix,
            "version": snapshot.version,
            "bytes": str(path.stat().st_size),
            "sha256": snapshot.sha256,
            "file": filename,
            "source_url": SNAPSHOT_URLS[prefix],
            "status": "LOADED",
        })
    return snapshots, manifest


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(TRAITS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("identifier") and doc.get("label"):
            records.append((path, doc))
    return records


def record_exact_names(doc: dict[str, Any]) -> dict[str, list[str]]:
    names: dict[str, list[str]] = defaultdict(list)
    names[normalize(str(doc["label"]))].append("LABEL")
    for synonym in doc.get("synonyms") or []:
        if synonym.get("synonym_type") == "EXACT_SYNONYM":
            text = str(synonym.get("synonym_text") or "").strip()
            if text:
                names[normalize(text)].append("EXACT_SYNONYM")
    return names


class OakLookup:
    def __init__(self, oak_dir: Path | None):
        self.oak_dir = oak_dir
        self.adapters: dict[str, Any | None] = {}

    def get(self, prefix: str, curie: str) -> tuple[str | None, set[str]]:
        if self.oak_dir is None:
            return None, set()
        if prefix not in self.adapters:
            db = self.oak_dir / f"{prefix.lower()}.db"
            if not db.is_file() or db.stat().st_size == 0:
                self.adapters[prefix] = None
            else:
                try:
                    from oaklib import get_adapter

                    self.adapters[prefix] = get_adapter(f"sqlite:{db}")
                except Exception:
                    self.adapters[prefix] = None
        adapter = self.adapters[prefix]
        if adapter is None:
            return None, set()
        try:
            label = adapter.label(curie)
            exact = {
                value
                for predicate, value in adapter.alias_relationships(curie)
                if predicate == "oio:hasExactSynonym"
            }
            return label, exact
        except Exception:
            return None, set()


def audit_groundings(
    records: list[tuple[Path, dict[str, Any]]],
    snapshots: dict[str, Snapshot],
    oak: OakLookup,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path, doc in records:
        record_id = str(doc["identifier"])
        groundings = [("identifier", record_id)] + [("xref", str(x)) for x in doc.get("xrefs") or []]
        exact_names = record_exact_names(doc)
        for role, curie in groundings:
            prefix = curie.split(":", 1)[0] if ":" in curie else ""
            snapshot = snapshots.get(prefix)
            term = snapshot.terms.get(curie) if snapshot else None
            if term is None:
                status = "NO_DIRECT_SOURCE" if snapshot is None else "TERM_NOT_FOUND"
                rows.append({
                    "record_path": str(path.relative_to(ROOT)), "record_id": record_id,
                    "record_label": str(doc["label"]), "grounding_role": role,
                    "grounding_curie": curie, "ontology_label": "",
                    "record_label_match": "", "declared_exact_synonyms": "",
                    "missing_exact_synonyms": "", "status": status,
                    "oak_status": "NOT_CHECKED", "source_version": "",
                })
                continue
            label_norm = normalize(term.label)
            exact_norm = {normalize(value) for value in term.exact_synonyms}
            record_label_norm = normalize(str(doc["label"]))
            if record_label_norm == label_norm:
                label_match = "CANONICAL_LABEL"
            elif record_label_norm in exact_norm:
                label_match = "EXACT_SYNONYM"
            else:
                label_match = "NO_EXACT_LABEL_MATCH"
            missing = sorted(
                value for value in term.exact_synonyms
                if normalize(value) != record_label_norm and normalize(value) not in exact_names
            )
            if term.obsolete or doc.get("mapping_status") == "DEPRECATED":
                status = "DEPRECATED_TERM"
            elif label_match == "NO_EXACT_LABEL_MATCH":
                status = "GROUNDING_LABEL_MISMATCH"
            elif missing:
                status = "MISSING_EXACT_SYNONYM"
            else:
                status = "EXACT_COMPLETE"
            oak_label, oak_exact = oak.get(prefix, curie)
            if oak_label is None:
                oak_status = "NOT_RESOLVED"
            elif normalize(oak_label) == label_norm and {normalize(x) for x in oak_exact} == exact_norm:
                oak_status = "AGREES"
            else:
                oak_status = "DIFFERS"
            rows.append({
                "record_path": str(path.relative_to(ROOT)), "record_id": record_id,
                "record_label": str(doc["label"]), "grounding_role": role,
                "grounding_curie": curie, "ontology_label": term.label,
                "record_label_match": label_match,
                "declared_exact_synonyms": " | ".join(term.exact_synonyms),
                "missing_exact_synonyms": " | ".join(missing), "status": status,
                "oak_status": oak_status, "source_version": snapshot.version,
            })
    return rows


def label_match(label: str, term: Term) -> str:
    value = normalize(label)
    if value == normalize(term.label):
        return "CANONICAL_LABEL"
    if value in {normalize(synonym) for synonym in term.exact_synonyms}:
        return "EXACT_SYNONYM"
    return "NO_EXACT_LABEL_MATCH"


def causal_grounding_rows(
    records: list[tuple[Path, dict[str, Any]]], snapshots: dict[str, Snapshot]
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(
        *, surface: str, source: str, label: str, semantic_type: str,
        curie: str, target_label: str = "", asserted_predicate: str = "",
        occurrences: int = 1, record_paths: str = "",
    ) -> None:
        prefix = curie.split(":", 1)[0] if ":" in curie else ""
        snapshot = snapshots.get(prefix)
        term = snapshot.terms.get(curie) if snapshot else None
        if term is None:
            match = target_match = ""
            status = "NO_DIRECT_SOURCE" if snapshot is None else "TERM_NOT_FOUND"
            ontology_label = exact = ""
        else:
            match = label_match(label, term)
            target_match = label_match(target_label, term) if target_label else ""
            ontology_label = term.label
            exact = " | ".join(term.exact_synonyms)
            if term.obsolete:
                status = "DEPRECATED_TERM"
            elif target_label and target_match == "NO_EXACT_LABEL_MATCH":
                status = "TARGET_LABEL_MISMATCH"
            elif match in {"CANONICAL_LABEL", "EXACT_SYNONYM"}:
                status = "EXACT_LEXICAL"
            else:
                status = "SEMANTIC_NOT_LEXICAL"
        rows.append({
            "surface": surface, "source": source, "record_paths": record_paths,
            "occurrences": str(occurrences), "label": label,
            "semantic_type": semantic_type, "target_curie": curie,
            "ontology_label": ontology_label, "label_match": match,
            "target_label": target_label, "target_label_match": target_match,
            "declared_exact_synonyms": exact,
            "asserted_predicate": asserted_predicate, "status": status,
        })

    for filename in ("node_grounding.tsv", "predicate_grounding.tsv"):
        path = REPO_ROOT / "mappings" / filename
        with path.open(encoding="utf-8", newline="") as fh:
            for line_number, row in enumerate(csv.DictReader(fh, delimiter="\t"), 2):
                add(
                    surface="mapping", source=f"mappings/{filename}:{line_number}",
                    label=str(row.get("label") or ""),
                    semantic_type=str(row.get("node_type") or "PREDICATE"),
                    curie=str(row.get("target_curie") or ""),
                    target_label=str(row.get("target_label") or ""),
                    asserted_predicate=str(row.get("predicate_id") or ""),
                )

    node_occurrences: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    predicate_occurrences: dict[tuple[str, str], list[str]] = defaultdict(list)
    for path, doc in records:
        rel = str(path.relative_to(ROOT))
        for graph in doc.get("causal_graphs") or []:
            for node in graph.get("nodes") or []:
                grounding = str(node.get("grounding") or "").strip()
                if grounding:
                    key = (str(node.get("label") or ""), str(node.get("node_type") or ""), grounding)
                    node_occurrences[key].append(rel)
            for edge in graph.get("edges") or []:
                predicate_id = str(edge.get("predicate_id") or "").strip()
                if predicate_id:
                    key = (str(edge.get("predicate") or ""), predicate_id)
                    predicate_occurrences[key].append(rel)
    for (label, node_type, curie), paths in sorted(node_occurrences.items()):
        add(
            surface="causal_node", source="data/traits/**/*.yaml", label=label,
            semantic_type=node_type, curie=curie, occurrences=len(paths),
            record_paths=" | ".join(sorted(set(paths))),
        )
    for (label, curie), paths in sorted(predicate_occurrences.items()):
        add(
            surface="causal_predicate", source="data/traits/**/*.yaml", label=label,
            semantic_type="PREDICATE", curie=curie, occurrences=len(paths),
            record_paths=" | ".join(sorted(set(paths))),
        )
    return rows


def load_decisions(path: Path) -> dict[tuple[str, str], tuple[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return {
            (str(row["record_id"]), str(row["target_curie"])): (
                str(row["decision"]), str(row["rationale"])
            )
            for row in csv.DictReader(fh, delimiter="\t")
        }


def candidate_rows(
    records: list[tuple[Path, dict[str, Any]]], snapshots: dict[str, Snapshot],
    decisions: dict[tuple[str, str], tuple[str, str]],
) -> list[dict[str, str]]:
    index: dict[str, list[tuple[str, Term, str, str]]] = defaultdict(list)
    for prefix, snapshot in snapshots.items():
        if prefix == "METPO":
            continue
        for term in snapshot.terms.values():
            if term.obsolete:
                continue
            index[normalize(term.label)].append((prefix, term, "CANONICAL_LABEL", term.label))
            for synonym in term.exact_synonyms:
                index[normalize(synonym)].append((prefix, term, "EXACT_SYNONYM", synonym))
    rows: list[dict[str, str]] = []
    for path, doc in records:
        label = str(doc["label"])
        current = {str(doc["identifier"]), *(str(x) for x in doc.get("xrefs") or [])}
        matches = index.get(normalize(label), [])
        unique_curies = {item[1].curie for item in matches}
        for prefix, term, basis, matched in matches:
            decision, rationale = decisions.get(
                (str(doc["identifier"]), term.curie), ("UNREVIEWED", "")
            )
            rows.append({
                "record_path": str(path.relative_to(ROOT)),
                "record_id": str(doc["identifier"]), "record_label": label,
                "record_definition": str(doc.get("definition") or ""),
                "trait_category": str(doc.get("trait_category") or ""),
                "term_kind": str(doc.get("term_kind") or ""),
                "candidate_curie": term.curie, "candidate_label": term.label,
                "candidate_definition": term.definition,
                "ontology": prefix, "match_basis": basis, "matched_text": matched,
                "candidate_exact_synonyms": " | ".join(term.exact_synonyms),
                "candidate_count_for_label": str(len(unique_curies)),
                "already_grounded": "yes" if term.curie in current else "no",
                "review_status": decision, "review_rationale": rationale,
            })
    return sorted(rows, key=lambda row: (row["record_id"], row["candidate_curie"], row["match_basis"]))


def collision_rows(records: list[tuple[Path, dict[str, Any]]]) -> list[dict[str, str]]:
    owners: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)
    display: dict[str, str] = {}
    for path, doc in records:
        label = str(doc["label"])
        key = normalize(label)
        display.setdefault(key, label)
        owners[key].append((str(doc["identifier"]), "LABEL", label, str(path.relative_to(ROOT))))
        for synonym in doc.get("synonyms") or []:
            if synonym.get("synonym_type") != "EXACT_SYNONYM":
                continue
            text = str(synonym.get("synonym_text") or "").strip()
            if text:
                key = normalize(text)
                display.setdefault(key, text)
                owners[key].append((str(doc["identifier"]), "EXACT_SYNONYM", text, str(path.relative_to(ROOT))))
    rows = []
    for key, values in owners.items():
        record_ids = {value[0] for value in values}
        if len(record_ids) < 2:
            continue
        rows.append({
            "normalized_text": key, "display_text": display[key],
            "owner_count": str(len(record_ids)),
            "owners": " | ".join(f"{curie} ({role}: {text})" for curie, role, text, _ in values),
            "record_paths": " | ".join(sorted({value[3] for value in values})),
        })
    return sorted(rows, key=lambda row: (-int(row["owner_count"]), row["normalized_text"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, help="directory containing the files in SNAPSHOT_FILES")
    parser.add_argument("--oak-dir", type=Path, help="directory containing OAK <ontology>.db files")
    parser.add_argument("--audit-out", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--candidate-out", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--collision-out", type=Path, default=DEFAULT_COLLISIONS)
    parser.add_argument("--manifest-out", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--causal-out", type=Path, default=DEFAULT_CAUSAL)
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    parser.add_argument(
        "--collisions-only",
        action="store_true",
        help=(
            "generate only the corpus-local exact-synonym collision report; "
            "does not require ontology snapshots"
        ),
    )
    args = parser.parse_args(argv)

    records = load_records()
    collisions = collision_rows(records)
    if args.collisions_only:
        _write_tsv(args.collision_out, [
            "normalized_text", "display_text", "owner_count", "owners", "record_paths",
        ], collisions)
        print(f"records={len(records)} exact_synonym_collisions={len(collisions)}")
        return 0

    snapshots, manifest = load_snapshots(args.snapshot_dir)
    audit = audit_groundings(records, snapshots, OakLookup(args.oak_dir))
    decisions = load_decisions(args.decisions)
    candidates = candidate_rows(records, snapshots, decisions)
    causal = causal_grounding_rows(records, snapshots)
    _write_tsv(args.audit_out, list(audit[0]), audit)
    _write_tsv(args.candidate_out, [
        "record_path", "record_id", "record_label", "record_definition", "trait_category", "term_kind",
        "candidate_curie", "candidate_label", "candidate_definition", "ontology", "match_basis", "matched_text",
        "candidate_exact_synonyms", "candidate_count_for_label", "already_grounded",
        "review_status", "review_rationale",
    ], candidates)
    _write_tsv(args.collision_out, [
        "normalized_text", "display_text", "owner_count", "owners", "record_paths",
    ], collisions)
    _write_tsv(args.manifest_out, [
        "ontology", "version", "bytes", "sha256", "file", "source_url", "status",
    ], manifest)
    _write_tsv(args.causal_out, [
        "surface", "source", "record_paths", "occurrences", "label", "semantic_type",
        "target_curie", "ontology_label", "label_match", "target_label",
        "target_label_match", "declared_exact_synonyms", "asserted_predicate", "status",
    ], causal)
    counts: dict[str, int] = defaultdict(int)
    for row in audit:
        counts[row["status"]] += 1
    print(
        f"records={len(records)} grounding_rows={len(audit)} candidates={len(candidates)} "
        f"collisions={len(collisions)} causal_rows={len(causal)}"
    )
    print("audit_status=" + ", ".join(f"{key}:{counts[key]}" for key in sorted(counts)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
