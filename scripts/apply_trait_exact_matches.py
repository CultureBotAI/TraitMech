#!/usr/bin/env python3
"""Apply curator-approved exact ontology matches and their exact synonyms.

The decision ledger is ``mappings/trait_exact_match_review.tsv``.  A lexical
match enters that ledger as a candidate, but is written only after its
definitions have been reviewed and the row is marked ``APPROVED``.  Exact
synonyms on already asserted TraitRecord identifiers/xrefs are also synchronized.

Default is a dry run.  Direct ontology snapshots are required so an approval
cannot be applied from a search-engine result alone.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    validate_trait,
    write_validated_trait,
)

AUDIT_PATH = ROOT / "scripts" / "audit_exact_synonyms.py"
spec = importlib.util.spec_from_file_location("audit_exact_synonyms", AUDIT_PATH)
assert spec and spec.loader
audit = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = audit
spec.loader.exec_module(audit)

DECISIONS = ROOT / "mappings" / "trait_exact_match_review.tsv"
SOURCE_BY_PREFIX = {
    "METPO": "https://w3id.org/metpo/releases/2026-06-12/metpo.owl",
    "GO": "http://purl.obolibrary.org/obo/go/releases/2026-07-26/go-basic.obo",
    "CHEBI": "https://purl.obolibrary.org/obo/chebi.obo#release-254",
    "ENVO": "http://purl.obolibrary.org/obo/envo/releases/2026-06-26/envo.obo",
    "PATO": "http://purl.obolibrary.org/obo/pato/releases/2025-05-14/pato.obo",
    "RO": "http://purl.obolibrary.org/obo/ro/releases/2025-12-17/ro.obo",
}
FIELD_ORDER = [
    "identifier", "label", "definition", "definition_source", "trait_category",
    "term_kind", "mapping_status", "parent_traits", "synonyms", "created_by",
    "domain", "range_", "xrefs", "evidence", "canonical_examples", "causal_graphs",
    "discussions", "datasets", "curation_history",
]


def ordered(doc: dict[str, Any]) -> dict[str, Any]:
    out = {key: doc[key] for key in FIELD_ORDER if key in doc}
    out.update({key: value for key, value in doc.items() if key not in out})
    return out


def synchronize_record(
    doc: dict[str, Any], snapshots: dict[str, Any], approved: dict[str, str]
) -> tuple[list[str], list[str], list[str]]:
    """Return (new xrefs, new synonyms, scope upgrades), mutating ``doc``."""
    record_id = str(doc["identifier"])
    xrefs = [str(value) for value in doc.get("xrefs") or []]
    new_xrefs: list[str] = []
    approved_curie = approved.get(record_id)
    if approved_curie and approved_curie not in xrefs:
        xrefs.append(approved_curie)
        new_xrefs.append(approved_curie)
    if xrefs:
        doc["xrefs"] = xrefs

    groundings = [record_id, *xrefs]
    synonyms = list(doc.get("synonyms") or [])
    by_name = {
        audit.normalize(str(item.get("synonym_text") or "")): item
        for item in synonyms if item.get("synonym_text")
    }
    primary = audit.normalize(str(doc["label"]))
    added: list[str] = []
    upgraded: list[str] = []
    for curie in groundings:
        prefix = curie.split(":", 1)[0]
        snapshot = snapshots.get(prefix)
        term = snapshot.terms.get(curie) if snapshot else None
        if term is None or term.obsolete:
            continue
        # Import scoped synonyms only when the grounding itself has exact label
        # evidence.  An xref accepted for some other mapping relation must not
        # silently donate aliases to this record.
        if audit.label_match(str(doc["label"]), term) == "NO_EXACT_LABEL_MATCH":
            continue
        source = SOURCE_BY_PREFIX[prefix]
        for text in term.exact_synonyms:
            key = audit.normalize(text)
            if not key or key == primary:
                continue
            existing = by_name.get(key)
            if existing is not None:
                if existing.get("synonym_type") != "EXACT_SYNONYM":
                    existing["synonym_type"] = "EXACT_SYNONYM"
                    existing["source"] = source
                    upgraded.append(text)
                continue
            entry = {
                "synonym_text": text,
                "synonym_type": "EXACT_SYNONYM",
                "source": source,
            }
            synonyms.append(entry)
            by_name[key] = entry
            added.append(text)
    if synonyms:
        doc["synonyms"] = synonyms
    return new_xrefs, added, upgraded


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, required=True)
    parser.add_argument("--decisions", type=Path, default=DECISIONS)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    snapshots, _manifest = audit.load_snapshots(args.snapshot_dir)
    decisions = audit.load_decisions(args.decisions)
    approved_by_record: dict[str, str] = {}
    for (record_id, curie), (decision, _rationale) in decisions.items():
        if decision != "APPROVED":
            continue
        if record_id in approved_by_record:
            raise ValueError(f"multiple approved exact matches for {record_id}")
        approved_by_record[record_id] = curie

    changed: list[tuple[str, list[str], list[str], list[str]]] = []
    errors: list[str] = []
    for path, original in audit.load_records():
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        new_xrefs, added, upgraded = synchronize_record(doc, snapshots, approved_by_record)
        if not (new_xrefs or added or upgraded):
            continue
        details = []
        if new_xrefs:
            details.append("approved exact xref(s): " + ", ".join(new_xrefs))
        if added:
            details.append("declared exact synonym(s): " + ", ".join(repr(x) for x in added))
        if upgraded:
            details.append("upgraded to exact scope: " + ", ".join(repr(x) for x in upgraded))
        record_curation_event(
            doc, curator="codex", action="ADD_EXACT_ONTOLOGY_MATCH",
            changes=(
                "Ontology exact-match review (2026-08-25): " + "; ".join(details)
                + ". Evidence is predicate-scoped in the versioned ontology snapshots; "
                "OAK cross-checked direct data, and OLS4 spot-checked release deltas "
                "and disputed hits."
            ),
            llm_assisted=True,
        )
        doc = ordered(doc)
        validation_errors = validate_trait(doc)
        if validation_errors:
            errors.append(f"{path}: {validation_errors[0]}")
            continue
        if args.apply:
            write_validated_trait(doc, path)
        changed.append((str(path.relative_to(ROOT)), new_xrefs, added, upgraded))

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"{mode}: {len(changed)} record(s)")
    for path, xrefs, added, upgraded in changed:
        print(f"  {path}: xrefs={len(xrefs)} synonyms={len(added)} upgrades={len(upgraded)}")
    if errors:
        print("ERRORS:", *errors, sep="\n  ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
