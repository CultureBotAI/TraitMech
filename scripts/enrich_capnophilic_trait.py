#!/usr/bin/env python3
"""Enrich the seeded METPO capnophilic record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "environment" / "capnophilic.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T07:30:00Z"

UPDATES = {
    "definition_source": "DOI:10.1111/1462-2920.13092",
    "evidence": [
        {
            "reference": "DOI:10.1111/1462-2920.13092",
            "snippet": (
                "Campylobacter jejuni, the leading cause of human bacterial "
                "gastroenteritis, requires low environmental oxygen and high "
                "carbon dioxide for optimum growth"
            ),
            "notes": (
                "Al-Haideri et al. support elevated carbon dioxide as a growth "
                "condition required by capnophilic Campylobacter jejuni."
            ),
        },
        {
            "reference": "DOI:10.1111/1462-2920.13092",
            "snippet": (
                "Taken together, our data suggest CanB is a major contributor "
                "to the capnophilic growth phenotype of C. jejuni."
            ),
            "notes": (
                "Al-Haideri et al. describe the elevated-CO2 requirement as a "
                "capnophilic growth phenotype and identify CanB as a major "
                "contributor in C. jejuni NCTC 11168."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:192222",
            "taxon_label": "Campylobacter jejuni subsp. jejuni NCTC 11168 = ATCC 700819",
            "note": (
                "C. jejuni NCTC 11168 was the strain background for the CanB "
                "study of the C. jejuni capnophilic growth phenotype."
            ),
            "reference": "DOI:10.1111/1462-2920.13092",
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
    if record.get("identifier") != "METPO:1005021":
        raise ValueError(f"expected METPO:1005021, got {record.get('identifier')!r}")
    if record.get("label") != "capnophilic":
        raise ValueError(f"expected capnophilic, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "ENVIRONMENT":
        raise ValueError(f"expected ENVIRONMENT, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000601"]:
        raise ValueError(f"expected environmental phenotype parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO capnophilic phenotype with DOI-backed "
            "elevated-carbon-dioxide evidence after a repository-wide "
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
