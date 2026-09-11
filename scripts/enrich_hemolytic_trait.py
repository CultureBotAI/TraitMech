#!/usr/bin/env python3
"""Enrich the seeded METPO hemolytic record with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "hemolytic.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T09:02:00Z"

UPDATES = {
    "definition_source": "DOI:10.3390/toxins5061140",
    "evidence": [
        {
            "reference": "DOI:10.3390/toxins5061140",
            "snippet": (
                "hemolysis to toxigenic substances secreted by S. aureus"
            ),
            "notes": (
                "Berube and Bubeck Wardenburg review historical evidence that "
                "S. aureus secretes hemolytic toxins, supporting a "
                "hemolytic phenotype."
            ),
        }
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1280",
            "taxon_label": "Staphylococcus aureus",
            "note": (
                "Canonical hemolytic bacterium whose culture supernatants have "
                "long been assayed for rabbit red-blood-cell lysis."
            ),
            "reference": "DOI:10.3390/toxins5061140",
        }
    ],
}


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def enrich(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1005026":
        raise ValueError(f"expected METPO:1005026, got {record.get('identifier')!r}")
    if record.get("label") != "hemolytic":
        raise ValueError(f"expected hemolytic, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1005025"]:
        raise ValueError(f"expected hemolysis parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the active METPO hemolytic child class with DOI-backed "
            "Staphylococcus aureus hemolysis evidence after a repository-wide "
            "duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    record = enrich(load_record(TARGET))
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
