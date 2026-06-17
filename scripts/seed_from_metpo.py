#!/usr/bin/env python3
"""Seed data/traits/<category>/<slug>.yaml from data/raw/metpo.owl.

Usage
-----
    python3 scripts/seed_from_metpo.py             # dry-run (default)
    python3 scripts/seed_from_metpo.py --apply     # write YAMLs
    python3 scripts/seed_from_metpo.py --apply --force   # also overwrite existing
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import (
    ValidationFailedError,
    validate_trait,
    write_validated_trait,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
OWL_PATH = REPO_ROOT / "data" / "raw" / "metpo.owl"
TRAITS_DIR = REPO_ROOT / "data" / "traits"
SCHEMA_PATH = REPO_ROOT / "src" / "traitmech" / "schema" / "traitmech.yaml"
TARGET_CLASS = "TraitRecord"


def validate_record(doc: dict[str, Any]) -> str | None:
    """Validate a built record. Returns first ERROR message, or None if clean."""
    errors = validate_trait(doc, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
    if errors:
        return errors[0].message
    return None

NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "obo": "http://purl.obolibrary.org/obo/",
    "oboInOwl": "http://www.geneontology.org/formats/oboInOwl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
}
RDF_RES = f"{{{NS['rdf']}}}resource"
RDF_ABT = f"{{{NS['rdf']}}}about"

METPO_IRI_PREFIX = "https://w3id.org/metpo/"


# -----------------------------------------------------------------
# Categorisation by ancestor walk
# -----------------------------------------------------------------

# Ancestor-CURIE → TraitCategoryEnum value. Order matters: the FIRST
# matching ancestor (closest to the class) wins, so put more specific
# anchors before broader ones.
CATEGORY_BY_ANCESTOR: list[tuple[str, str]] = [
    # GENOMICS
    ("METPO:1000127", "GENOMICS"),                   # GC content
    # MORPHOLOGY (phenotype subtree)
    ("METPO:1000881", "MORPHOLOGY"),                 # cell length
    ("METPO:1000666", "MORPHOLOGY"),                 # cell shape
    ("METPO:1000882", "MORPHOLOGY"),                 # cell width
    ("METPO:1000697", "MORPHOLOGY"),                 # gram stain
    ("METPO:1000701", "MORPHOLOGY"),                 # motility
    ("METPO:1000870", "MORPHOLOGY"),                 # sporulation
    ("METPO:1003021", "MORPHOLOGY"),                 # pigmentation
    # ENVIRONMENT — pH/temperature/salinity/oxygen tolerance/optima
    ("METPO:1000534", "ENVIRONMENT"),                # delta phenotype
    ("METPO:1000535", "ENVIRONMENT"),                # growth range phenotype
    ("METPO:1000536", "ENVIRONMENT"),                # optimum phenotype
    ("METPO:1000531", "ENVIRONMENT"),                # pH phenotype with numerical limits
    ("METPO:1000532", "ENVIRONMENT"),                # salinity phenotype
    ("METPO:1000533", "ENVIRONMENT"),                # temperature phenotype
    ("METPO:1000601", "ENVIRONMENT"),                # oxygen preference
    ("METPO:1000613", "ENVIRONMENT"),                # temperature preference
    ("METPO:1003000", "ENVIRONMENT"),                # pH growth preference
    ("METPO:1000629", "ENVIRONMENT"),                # halophily preference
    # ECOLOGY
    ("METPO:1004000", "ECOLOGY"),                    # pathogenic to host
    ("METPO:1001101", "ECOLOGY"),                    # biosafety level
    # PHYSIOLOGY
    ("METPO:1000631", "PHYSIOLOGY"),                 # trophic type
    # METABOLISM (whole metabolism + biological-process subtrees)
    ("METPO:1000060", "METABOLISM"),                 # metabolism
    ("METPO:1000630", "METABOLISM"),                 # biological process
    # OBSERVATION (the observation root)
    ("METPO:1001000", "OBSERVATION"),
]

# Upper-level classifiers. The first four are the rdfs:subClassOf-of-nothing
# roots; phenotype is technically a child of `quality` but functions as a
# top-level bucket for all the morphological/environmental traits.
UPPER_ROOTS = {
    "METPO:1000186",  # material entity
    "METPO:1000188",  # quality
    "METPO:1000630",  # biological process
    "METPO:1001000",  # observation
    "METPO:1000059",  # phenotype
}

# Material-entity subtree contains chemicals/microbes/enzymes — those
# are not microbial traits and should not be seeded as TraitRecord.
SKIP_ANCESTOR = "METPO:1000186"


# -----------------------------------------------------------------
# Parsing
# -----------------------------------------------------------------

def _local(iri: str) -> str:
    return iri.rsplit("/", 1)[-1] if iri else ""


def _curie(iri: str) -> str | None:
    if not iri.startswith(METPO_IRI_PREFIX):
        return None
    n = _local(iri)
    return f"METPO:{n}" if n else None


def _is_numeric_metpo(curie: str | None) -> bool:
    if not curie or not curie.startswith("METPO:"):
        return False
    return curie[len("METPO:"):].isdigit()


def _xref_curie_or_none(text: str) -> str | None:
    """Return text as a CURIE if it looks like one, else None."""
    if not text:
        return None
    t = text.strip()
    return t if re.match(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$", t) else None


def parse_owl(path: Path) -> dict[str, dict[str, Any]]:
    """Return {curie: {label, definition, parents, synonyms, xrefs,
    created_by, term_kind, definition_source, range_, domain}}.

    Walks owl:Class, owl:DatatypeProperty, owl:ObjectProperty entries.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    out: dict[str, dict[str, Any]] = {}

    def _ingest(el: ET.Element, term_kind: str) -> None:
        iri = el.get(RDF_ABT, "")
        curie = _curie(iri)
        if not _is_numeric_metpo(curie):
            return
        rec: dict[str, Any] = {
            "label": None,
            "definition": None,
            "definition_source": None,
            "parents": [],
            "synonyms": [],
            "xrefs": [],
            "created_by": None,
            "term_kind": term_kind,
            "domain": None,
            "range_": None,
        }
        for child in el:
            tag = child.tag.split("}", 1)[-1]
            text = (child.text or "").strip() if child.text else ""
            if tag == "label":
                rec["label"] = text or None
            elif tag == "subClassOf":
                pres = child.get(RDF_RES, "")
                pcurie = _curie(pres)
                if _is_numeric_metpo(pcurie):
                    rec["parents"].append(pcurie)
            elif tag == "subPropertyOf":
                pres = child.get(RDF_RES, "")
                pcurie = _curie(pres)
                if _is_numeric_metpo(pcurie):
                    rec["parents"].append(pcurie)
            elif tag == "domain":
                pres = child.get(RDF_RES, "") or text
                rec["domain"] = pres or None
            elif tag == "range":
                pres = child.get(RDF_RES, "") or text
                rec["range_"] = pres or None
            elif tag == "IAO_0000115":
                rec["definition"] = text or None
            elif tag == "IAO_0000119":
                rec["definition_source"] = text or None
            elif tag == "IAO_0000117":
                rec["created_by"] = text or None
            elif tag == "hasExactSynonym":
                if text:
                    rec["synonyms"].append({"text": text, "type": "EXACT_SYNONYM"})
            elif tag == "hasRelatedSynonym":
                if text:
                    rec["synonyms"].append({"text": text, "type": "RELATED_SYNONYM"})
            elif tag == "hasNarrowSynonym":
                if text:
                    rec["synonyms"].append({"text": text, "type": "NARROW_SYNONYM"})
            elif tag == "hasBroadSynonym":
                if text:
                    rec["synonyms"].append({"text": text, "type": "BROAD_SYNONYM"})
            elif tag == "hasDbXref":
                xc = _xref_curie_or_none(text)
                if xc:
                    rec["xrefs"].append(xc)
        out[curie] = rec

    for cls in root.findall("owl:Class", NS):
        _ingest(cls, "CLASS")
    for dp in root.findall("owl:DatatypeProperty", NS):
        _ingest(dp, "DATATYPE_PROPERTY")
    for op in root.findall("owl:ObjectProperty", NS):
        _ingest(op, "OBJECT_PROPERTY")
    for ap in root.findall("owl:AnnotationProperty", NS):
        _ingest(ap, "ANNOTATION_PROPERTY")
    return out


# -----------------------------------------------------------------
# Categorisation
# -----------------------------------------------------------------

def ancestors(curie: str, parents: dict[str, list[str]]) -> set[str]:
    """Transitive parents (excluding self)."""
    seen: set[str] = set()
    stack = list(parents.get(curie, []))
    while stack:
        p = stack.pop()
        if p in seen:
            continue
        seen.add(p)
        stack.extend(parents.get(p, []))
    return seen


def categorize(curie: str, rec: dict[str, Any], parents: dict[str, list[str]]) -> str | None:
    """Return TraitCategoryEnum value or None to skip."""
    if rec["term_kind"] == "DATATYPE_PROPERTY":
        return "QUANTITATIVE_PROPERTY"
    if rec["term_kind"] == "OBJECT_PROPERTY":
        return "METABOLISM"
    if rec["term_kind"] == "ANNOTATION_PROPERTY":
        return None  # skip annotation properties

    anc = ancestors(curie, parents)
    if SKIP_ANCESTOR in anc:
        return None  # material entity → skip

    # Self-as-root
    if curie in UPPER_ROOTS:
        return "UPPER"

    # Closest matching ancestor wins. Walk from self upward via BFS so
    # the first hit is the most specific.
    ordered = _bfs_order(curie, parents)
    rules = dict(CATEGORY_BY_ANCESTOR)
    for c in ordered:
        if c in rules:
            return rules[c]
    return "OTHER"


def _bfs_order(start: str, parents: dict[str, list[str]]) -> list[str]:
    """BFS over parents starting from `start` (inclusive)."""
    order: list[str] = []
    seen: set[str] = set()
    queue: list[str] = [start]
    while queue:
        cur = queue.pop(0)
        if cur in seen:
            continue
        seen.add(cur)
        order.append(cur)
        queue.extend(parents.get(cur, []))
    return order


# -----------------------------------------------------------------
# YAML emission
# -----------------------------------------------------------------

CATEGORY_DIR = {
    "MORPHOLOGY": "morphology",
    "PHYSIOLOGY": "physiology",
    "ENVIRONMENT": "environment",
    "METABOLISM": "metabolism",
    "GENOMICS": "genomics",
    "ECOLOGY": "ecology",
    "DETECTION": "detection",
    "QUANTITATIVE_PROPERTY": "quantitative_property",
    "OBSERVATION": "observation",
    "UPPER": "upper",
    "OTHER": "other",
}


def slugify(label: str | None, fallback: str) -> str:
    if not label:
        return fallback
    s = label.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s or fallback


def to_record(curie: str, rec: dict[str, Any], category: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "identifier": curie,
        "label": rec["label"],
        "definition": rec["definition"],
        "definition_source": rec["definition_source"],
        "trait_category": category,
        "term_kind": rec["term_kind"],
        "mapping_status": "SEEDED",
    }
    if rec["parents"]:
        out["parent_traits"] = sorted(set(rec["parents"]))
    if rec["synonyms"]:
        # Drop synonyms that merely duplicate the label (case-insensitive) —
        # they carry no information beyond the label itself and are redundant
        # noise per OBO convention. De-dupe repeated synonym_texts too.
        _label_norm = (rec["label"] or "").strip().lower()
        _seen: set[str] = set()
        syn_out = []
        for s in rec["synonyms"]:
            txt = (s["text"] or "").strip()
            key = txt.lower()
            if not txt or key == _label_norm or key in _seen:
                continue
            _seen.add(key)
            syn_out.append({"synonym_text": txt, "synonym_type": s["type"], "source": "metpo.owl"})
        if syn_out:
            out["synonyms"] = syn_out
    if rec["xrefs"]:
        out["xrefs"] = sorted(set(rec["xrefs"]))
    if rec["domain"]:
        out["domain"] = rec["domain"]
    if rec["range_"]:
        out["range_"] = rec["range_"]
    if rec["created_by"]:
        out["created_by"] = rec["created_by"]
    # Drop None values for cleanliness
    cleaned = {k: v for k, v in out.items() if v not in (None, [], {})}
    record_curation_event(
        cleaned,
        curator="seed_from_metpo",
        action="SEEDED_FROM_METPO",
        changes=f"imported from data/raw/metpo.owl ({rec['term_kind']})",
    )
    return cleaned


# -----------------------------------------------------------------
# Driver
# -----------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="write YAMLs (default: dry-run)")
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing files (default: skip existing)")
    ap.add_argument("--owl", type=Path, default=OWL_PATH)
    ap.add_argument("--out", type=Path, default=TRAITS_DIR)
    args = ap.parse_args()

    if not args.owl.exists():
        print(f"OWL not found: {args.owl}", file=sys.stderr)
        return 2

    parsed = parse_owl(args.owl)
    parents = {c: r["parents"] for c, r in parsed.items()}

    by_cat: Counter = Counter()
    skipped: Counter = Counter()
    written = 0
    skipped_existing = 0
    skipped_invalid: list[tuple[str, str]] = []

    # Build slug uniqueness map: prefer label-only slug; fall back to
    # label+localid when collisions occur.
    slug_for: dict[str, str] = {}
    label_seen: dict[str, list[str]] = {}
    for curie, rec in parsed.items():
        category = categorize(curie, rec, parents)
        if category is None:
            skipped[rec["term_kind"]] += 1
            continue
        local = curie.split(":", 1)[1]
        base = slugify(rec["label"], local)
        label_seen.setdefault(base, []).append(curie)

    # Resolve collisions (e.g. two classes share a label) by appending
    # localid.
    for base, curies in label_seen.items():
        if len(curies) == 1:
            slug_for[curies[0]] = base
        else:
            for c in curies:
                slug_for[c] = f"{base}__{c.split(':', 1)[1]}"

    for curie, rec in sorted(parsed.items()):
        category = categorize(curie, rec, parents)
        if category is None:
            continue
        slug = slug_for[curie]
        cat_dir = args.out / CATEGORY_DIR[category]
        path = cat_dir / f"{slug}.yaml"
        doc = to_record(curie, rec, category)
        try:
            display_path = str(path.relative_to(REPO_ROOT))
        except ValueError:
            display_path = str(path)

        # G03: validate before write — never commit an invalid record.
        # Don't abort the whole run on a single failure; the seed touches
        # hundreds of records.
        #
        # Single validation per mode: dry-run uses validate_record (no write);
        # --apply lets write_validated_trait do the only check. The path-exists
        # skip is checked first in apply mode so we don't waste a validation
        # pass on records we wouldn't write anyway.
        if args.apply:
            if path.exists() and not args.force:
                skipped_existing += 1
                continue
            try:
                write_validated_trait(doc, path, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
            except ValidationFailedError as exc:
                msg = exc.errors[0].message[:200] if exc.errors else str(exc)[:200]
                skipped_invalid.append((display_path, msg))
                print(f"  SKIP (invalid): {display_path}: {msg}", file=sys.stderr)
                continue
            written += 1
        else:
            err = validate_record(doc)
            if err is not None:
                skipped_invalid.append((display_path, err[:200]))
                print(f"  SKIP (invalid): {display_path}: {err[:200]}",
                      file=sys.stderr)
                continue
        by_cat[category] += 1

    print(f"OWL parsed:                 {args.owl}")
    print(f"Total terms found:          {len(parsed)}")
    print("Skipped (material entity / annotation property):")
    for k, v in skipped.most_common():
        print(f"  {k:<25} {v}")
    print()
    print("Per-category counts (would-emit):")
    for cat, n in sorted(by_cat.items()):
        print(f"  {cat:<25} {n:>4}")
    total = sum(by_cat.values())
    print(f"  {'TOTAL':<25} {total:>4}")
    print()
    if skipped_invalid:
        print(f"Skipped (invalid):          {len(skipped_invalid)}")
        for rel, msg in skipped_invalid[:10]:
            print(f"  {rel}: {msg}")
        if len(skipped_invalid) > 10:
            print(f"  ... and {len(skipped_invalid) - 10} more")
    if args.apply:
        print(f"Wrote:                      {written} files under {args.out}")
        if skipped_existing:
            print(f"Skipped (exists, no --force): {skipped_existing}")
    else:
        print("Mode:                       DRY-RUN (re-run with --apply to write)")
    return 1 if skipped_invalid else 0


if __name__ == "__main__":
    sys.exit(main())
