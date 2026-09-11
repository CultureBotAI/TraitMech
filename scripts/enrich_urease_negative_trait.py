#!/usr/bin/env python3
"""Enrich the seeded METPO urease-negative record with assay evidence."""
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

UREASE_NEGATIVE = REPO_ROOT / "data" / "traits" / "other" / "urease_negative.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-11T15:41:02Z"

OMP_UREASE_NEGATIVE = "http://purl.obolibrary.org/obo/OMP_0006090"
HAFEZI_BIOCHEMICAL_TESTS = "DOI:10.5812/chbs-160199"

SEEDED_SYNONYMS = [
    {
        "synonym_text": "urease -",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "urease test negative",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]

UREASE_NEGATIVE_UPDATES = {
    "definition_source": OMP_UREASE_NEGATIVE,
    "evidence": [
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "A positive reaction is indicated by the entire liquid medium "
                "and the surface of the solid medium turning pink, whereas a "
                "negative reaction is characterized by the medium remaining "
                "yellow"
            ),
            "notes": (
                "Hafezi and Khamar review the urease-test polarity and "
                "interpret an unchanged yellow medium as a negative assay "
                "result."
            ),
        },
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "Both types contain a phenol red reagent that changes color "
                "with pH variations"
            ),
            "notes": (
                "The review describes the pH-indicator readout shared by "
                "liquid and solid urease-test media."
            ),
        },
    ],
}


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def enrich_urease_negative(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007088":
        raise ValueError(f"expected METPO:1007088, got {record.get('identifier')!r}")
    if record.get("label") != "urease negative":
        raise ValueError(f"expected urease negative, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007082"]:
        raise ValueError(
            f"expected urease-test parent, got {record.get('parent_traits')!r}"
        )
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(UREASE_NEGATIVE_UPDATES))
    record.pop("canonical_examples", None)
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO urease-negative test outcome with OMP "
            "definition provenance plus DOI-backed assay evidence after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files."
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

    record = enrich_urease_negative(load_record(UREASE_NEGATIVE))
    rel = UREASE_NEGATIVE.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, UREASE_NEGATIVE)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
