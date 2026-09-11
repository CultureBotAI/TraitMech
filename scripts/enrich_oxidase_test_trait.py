#!/usr/bin/env python3
"""Enrich the seeded METPO oxidase-test record with assay evidence."""
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

OXIDASE_TEST = REPO_ROOT / "data" / "traits" / "other" / "oxidase_test.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-11T14:32:00Z"

OMP_OXIDASE_TEST = "http://purl.obolibrary.org/obo/OMP_0000220"
ASM_OXIDASE_PROTOCOL = "https://asm.org/protocols/oxidase-test-protocol"
HAFEZI_BIOCHEMICAL_TESTS = "DOI:10.5812/chbs-160199"

SEEDED_SYNONYMS = [
    {
        "synonym_text": "cytochrome oxidase test",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "oxidase activity test",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]

OXIDASE_TEST_UPDATES = {
    "definition_source": OMP_OXIDASE_TEST,
    "evidence": [
        {
            "reference": ASM_OXIDASE_PROTOCOL,
            "snippet": (
                "The oxidase test is a biochemical reaction that assays for the "
                "presence of cytochrome oxidase"
            ),
            "notes": (
                "The American Society for Microbiology oxidase-test protocol "
                "describes the assay as a biochemical reaction that reads "
                "cytochrome oxidase."
            ),
        },
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "The ability of bacteria to produce the enzyme cytochrome "
                "oxidase can be determined by performing an oxidase test"
            ),
            "notes": (
                "Hafezi and Khamar review oxidase-test use for determining "
                "bacterial cytochrome oxidase production."
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


def enrich_oxidase_test(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007081":
        raise ValueError(f"expected METPO:1007081, got {record.get('identifier')!r}")
    if record.get("label") != "oxidase test":
        raise ValueError(f"expected oxidase test, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(OXIDASE_TEST_UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO oxidase test with OMP definition "
            "provenance plus stable-URL and DOI-backed assay evidence after a "
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

    record = enrich_oxidase_test(load_record(OXIDASE_TEST))
    rel = OXIDASE_TEST.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, OXIDASE_TEST)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
