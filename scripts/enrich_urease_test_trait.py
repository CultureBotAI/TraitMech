#!/usr/bin/env python3
"""Enrich the seeded METPO urease-test record with assay evidence."""
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

UREASE_TEST = REPO_ROOT / "data" / "traits" / "other" / "urease_test.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-11T14:53:47Z"

OMP_UREASE_TEST = "http://purl.obolibrary.org/obo/OMP_0000222"
HAFEZI_BIOCHEMICAL_TESTS = "DOI:10.5812/chbs-160199"

SEEDED_SYNONYMS = [
    {
        "synonym_text": "urea hydrolysis test",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "urease activity test",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]

UREASE_TEST_UPDATES = {
    "definition_source": OMP_UREASE_TEST,
    "evidence": [
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "Urea is classified as a diamide, and certain bacteria "
                "possessing the enzyme urease are capable of utilizing urea to "
                "generate ammonia, carbon dioxide, and water"
            ),
            "notes": (
                "Hafezi and Khamar describe the urease-test chemistry linking "
                "bacterial urease to urea conversion into alkaline products."
            ),
        },
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "Both types contain a phenol red reagent that changes color "
                "with pH variations"
            ),
            "notes": (
                "The review describes phenol red as the pH indicator for both "
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


def enrich_urease_test(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007082":
        raise ValueError(f"expected METPO:1007082, got {record.get('identifier')!r}")
    if record.get("label") != "urease test":
        raise ValueError(f"expected urease test, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(UREASE_TEST_UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO urease test with OMP definition "
            "provenance plus DOI-backed urea-hydrolysis and pH-indicator "
            "evidence after a repository-wide duplicate review covering "
            "ignored and hidden files."
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

    record = enrich_urease_test(load_record(UREASE_TEST))
    rel = UREASE_TEST.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, UREASE_TEST)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
