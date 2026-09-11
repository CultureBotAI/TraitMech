#!/usr/bin/env python3
"""Enrich the seeded METPO coagulase negative record with evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "coagulase_negative.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T09:59:00Z"
NCBI_BOOKSHELF = "https://www.ncbi.nlm.nih.gov/books/NBK563240/"

UPDATES = {
    "definition_source": "DOI:10.3390/microorganisms9040830",
    "evidence": [
        {
            "reference": "DOI:10.3390/microorganisms9040830",
            "snippet": (
                "Coagulase-negative staphylococci (CoNS) form a large group "
                "of Gram-positive cocci united by their mutual lack of the "
                "virulence factor coagulase"
            ),
            "notes": (
                "Michels et al. define coagulase-negative staphylococci by "
                "absence of the coagulase virulence factor, supporting the "
                "negative assay-outcome phenotype."
            ),
        },
        {
            "reference": NCBI_BOOKSHELF,
            "snippet": (
                "Staphylococcus epidermidis is a coagulase-negative, "
                "gram-positive cocci bacteria that form clusters"
            ),
            "notes": (
                "Lee and Anjum identify S. epidermidis as coagulase-negative, "
                "providing a stable species-level example of a negative "
                "coagulase test outcome."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1282",
            "taxon_label": "Staphylococcus epidermidis",
            "note": (
                "Lee and Anjum describe S. epidermidis as a coagulase-negative "
                "Staphylococcus species."
            ),
            "reference": NCBI_BOOKSHELF,
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
    if record.get("identifier") != "METPO:1007091":
        raise ValueError(f"expected METPO:1007091, got {record.get('identifier')!r}")
    if record.get("label") != "coagulase negative":
        raise ValueError(f"expected coagulase negative, got {record.get('label')!r}")
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
            "Enriched the seeded METPO coagulase negative test-outcome "
            "phenotype with DOI- and NCBI-backed evidence after a "
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
