#!/usr/bin/env python3
"""Enrich the seeded METPO coagulase positive record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "coagulase_positive.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T09:37:00Z"

UPDATES = {
    "definition_source": "DOI:10.1099/mic.0.000019",
    "evidence": [
        {
            "reference": "DOI:10.1099/mic.0.000019",
            "snippet": (
                "coagulase-positive S. aureus bacteria promoted clotting of "
                "plasma which was not seen when a coagulase-deficient mutant "
                "strain was used"
            ),
            "notes": (
                "Loof et al. show that coagulase-positive S. aureus clots plasma "
                "in a way lost from a coagulase-deficient mutant, directly "
                "supporting the positive test-outcome phenotype."
            ),
        },
        {
            "reference": "DOI:10.1371/journal.ppat.1001036",
            "snippet": (
                "Clinical isolates of the human pathogen Staphylococcus aureus "
                "secrete coagulase (Coa), a polypeptide that binds to and "
                "activates prothrombin"
            ),
            "notes": (
                "Cheng et al. connect S. aureus Coa secretion to prothrombin "
                "activation, the clotting activity detected by the coagulase "
                "test."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1280",
            "taxon_label": "Staphylococcus aureus",
            "note": (
                "Loof et al. use coagulase-positive S. aureus as a direct "
                "plasma-clotting example and contrast it with a "
                "coagulase-deficient mutant."
            ),
            "reference": "DOI:10.1099/mic.0.000019",
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
    if record.get("identifier") != "METPO:1007090":
        raise ValueError(f"expected METPO:1007090, got {record.get('identifier')!r}")
    if record.get("label") != "coagulase positive":
        raise ValueError(
            f"expected coagulase positive, got {record.get('label')!r}"
        )
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007089"]:
        raise ValueError(
            f"expected coagulase activity parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO coagulase positive test-outcome "
            "phenotype with DOI-backed plasma-clotting evidence after a "
            "repository-wide duplicate review covering ignored and hidden files."
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
