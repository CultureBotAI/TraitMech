#!/usr/bin/env python3
"""Enrich the seeded METPO Voges-Proskauer-test-negative record."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "voges_proskauer_test_negative.yaml"

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-12T22:09:04Z"

UPDATES = {
    "definition_source": ASM_MRVP,
    "evidence": [
        {
            "reference": ASM_MRVP,
            "snippet": (
                "VP-positive E. areogenes (A) shows red coloration on top "
                "of the culture, whereas VP-negative E. coli (B) has a "
                "yellowish color."
            ),
            "notes": (
                "The ASM protocol figure caption identifies the yellow "
                "E. coli reaction after adding Barritt's reagents as the "
                "VP-negative comparison."
            ),
        }
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "ASM Figure 2 presents E. coli grown in MR-VP broth for 48 "
                "hours as the VP-negative control culture that remains "
                "yellowish after Barritt's reagents are added."
            ),
            "reference": ASM_MRVP,
        }
    ],
}


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def enrich_record(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1005018":
        raise ValueError(f"expected METPO:1005018, got {record.get('identifier')!r}")
    if record.get("label") != "Voges-Proskauer test negative":
        raise ValueError(
            f"expected Voges-Proskauer test negative, got {record.get('label')!r}"
        )
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1005016"]:
        raise ValueError(
            f"expected Voges-Proskauer parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO Voges-Proskauer-test-negative phenotype "
            "with stable-URL VP-negative interpretation evidence after a "
            "repository-wide duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    record = enrich_record(load_record(TARGET))
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
