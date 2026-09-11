#!/usr/bin/env python3
"""Enrich the seeded METPO catalase-test record with assay evidence."""
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

CATALASE_TEST = REPO_ROOT / "data" / "traits" / "other" / "catalase_test.yaml"
CATALASE_NEGATIVE = REPO_ROOT / "data" / "traits" / "other" / "catalase_negative.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-11T14:03:00Z"

OMP_CATALASE_TEST = "http://purl.obolibrary.org/obo/OMP_0000218"
ASM_CATALASE_PROTOCOL = "https://asm.org/protocols/catalase-test-protocol"
CATALASE_ASSAY_DOI = "DOI:10.1038/srep03081"

SEEDED_SYNONYMS = [
    {
        "synonym_text": "catalase activity test",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "catalase assay",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]

CATALASE_TEST_UPDATES = {
    "definition_source": OMP_CATALASE_TEST,
    "evidence": [
        {
            "reference": ASM_CATALASE_PROTOCOL,
            "snippet": "The catalase test facilitates the detection of this enzyme in bacteria",
            "notes": (
                "The American Society for Microbiology catalase-test protocol "
                "describes the bacterial assay context for detecting catalase."
            ),
        },
        {
            "reference": CATALASE_ASSAY_DOI,
            "snippet": (
                "The enzyme-generated oxygen bubbles trapped by Triton X-100 "
                "were visualized as foam"
            ),
            "notes": (
                "Iwase et al. support the visible oxygen-bubble readout produced "
                "by catalase-mediated hydrogen-peroxide decomposition."
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


def enrich_catalase_test(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007080":
        raise ValueError(f"expected METPO:1007080, got {record.get('identifier')!r}")
    if record.get("label") != "catalase test":
        raise ValueError(f"expected catalase test, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(CATALASE_TEST_UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO catalase test with OMP definition "
            "provenance plus stable-URL and DOI-backed assay evidence after a "
            "repository-wide duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return record


def reparent_catalase_negative(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007084":
        raise ValueError(f"expected METPO:1007084, got {record.get('identifier')!r}")
    if record.get("label") != "catalase negative":
        raise ValueError(f"expected catalase negative, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")

    discussions = record.get("discussions")
    if not isinstance(discussions, list):
        raise ValueError("expected catalase negative to have discussions")
    matches = [
        discussion
        for discussion in discussions
        if discussion.get("discussion_id") == "catalase-negative-assay-parent-gap"
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one assay-parent discussion, got {len(matches)}")
    discussion = matches[0]
    if discussion.get("status") != "OPEN":
        raise ValueError(f"expected OPEN discussion, got {discussion.get('status')!r}")

    record["parent_traits"] = ["METPO:1007080"]
    discussion["status"] = "RESOLVED"
    discussion["rationale"] = (
        "METPO:1007080 is now represented as the seeded catalase-test assay "
        "parent, so this negative assay-outcome phenotype can use its source "
        "superclass rather than a temporary direct phenotype parent."
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVED_PARENT_GAP",
        changes=(
            "Reparented catalase negative below the newly curated "
            "METPO:1007080 catalase test assay parent and marked the temporary "
            "assay-parent discussion resolved."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    updates = [
        (CATALASE_TEST, enrich_catalase_test(load_record(CATALASE_TEST))),
        (CATALASE_NEGATIVE, reparent_catalase_negative(load_record(CATALASE_NEGATIVE))),
    ]
    for path, record in updates:
        rel = path.relative_to(REPO_ROOT)
        if args.apply:
            write_validated_trait(record, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
