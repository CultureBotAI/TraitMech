#!/usr/bin/env python3
"""Add seeded METPO methyl-red-test parent and resolve child parent gaps."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "methyl_red_test.yaml"
METHYL_RED_POSITIVE = (
    REPO_ROOT / "data" / "traits" / "other" / "methyl_red_test_positive.yaml"
)
METHYL_RED_NEGATIVE = (
    REPO_ROOT / "data" / "traits" / "other" / "methyl_red_test_negative.yaml"
)

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T20:14:22Z"
TIMESTAMP = "2026-09-12T20:15:55Z"

SEED_RECORD = {
    "identifier": "METPO:1005013",
    "label": "methyl red test",
    "definition": (
        "An assay that tests the ability of an organism to produce and "
        "maintain stable acid end products from glucose fermentation."
    ),
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1000059"],
    "curation_history": [
        {
            "timestamp": SEED_TIMESTAMP,
            "curator": "seed_from_metpo",
            "action": "SEEDED_FROM_METPO",
            "changes": "imported from data/raw/metpo.owl (CLASS)",
        }
    ],
}

UPDATES = {
    "definition_source": ASM_MRVP,
    "evidence": [
        {
            "reference": ASM_MRVP,
            "snippet": (
                "When the culture medium turns red after addition of methyl "
                "red, because of a pH at or below 4.4 from the fermentation "
                "of glucose, the culture has a positive result for the MR "
                "test (Fig.1A)."
            ),
            "notes": (
                "The ASM protocol PDF defines the methyl-red-test positive "
                "readout as acidification to pH 4.4 or below after glucose "
                "fermentation."
            ),
        },
        {
            "reference": ASM_MRVP,
            "snippet": (
                "A negative MR test is indicated by a yellow color in the "
                "culture medium (Fig. 1B), which occurs when less acid is "
                "produced (pH is higher) from the fermentation of glucose."
            ),
            "notes": (
                "The same protocol defines the negative readout as a yellow "
                "culture reflecting less glucose-derived acid production."
            ),
        },
    ],
}

CHILDREN = [
    (
        METHYL_RED_POSITIVE,
        "METPO:1005014",
        "methyl red test positive",
        "methyl-red-test-positive-assay-parent-gap",
        "positive",
    ),
    (
        METHYL_RED_NEGATIVE,
        "METPO:1005015",
        "methyl red test negative",
        "methyl-red-test-negative-assay-parent-gap",
        "negative",
    ),
]


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def build_methyl_red_test() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO methyl-red-test assay parent with stable-URL "
            "methyl-red readout evidence after a repository-wide duplicate "
            "review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def resolve_child_parent_gap(
    record: dict,
    *,
    expected_identifier: str,
    expected_label: str,
    discussion_id: str,
    polarity: str,
) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != expected_identifier:
        raise ValueError(
            f"expected {expected_identifier}, got {record.get('identifier')!r}"
        )
    if record.get("label") != expected_label:
        raise ValueError(f"expected {expected_label}, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")

    discussions = record.get("discussions")
    if not isinstance(discussions, list):
        raise ValueError(f"expected {expected_label} to have discussions")
    matches = [
        discussion
        for discussion in discussions
        if discussion.get("discussion_id") == discussion_id
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one assay-parent discussion, got {len(matches)}")
    discussion = matches[0]
    if discussion.get("status") != "OPEN":
        raise ValueError(f"expected OPEN discussion, got {discussion.get('status')!r}")

    record["parent_traits"] = ["METPO:1005013"]
    discussion["status"] = "RESOLVED"
    discussion["rationale"] = (
        "METPO:1005013 is now represented as the seeded methyl-red-test "
        "assay parent, so this assay-outcome phenotype can use its source "
        "superclass rather than a temporary direct phenotype parent."
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVED_PARENT_GAP",
        changes=(
            f"Reparented methyl red test {polarity} below the newly curated "
            "METPO:1005013 methyl red test assay parent and marked the "
            "temporary assay-parent discussion resolved."
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

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    updates = [(TARGET, build_methyl_red_test())]
    updates.extend(
        (
            path,
            resolve_child_parent_gap(
                load_record(path),
                expected_identifier=expected_identifier,
                expected_label=expected_label,
                discussion_id=discussion_id,
                polarity=polarity,
            ),
        )
        for (
            path,
            expected_identifier,
            expected_label,
            discussion_id,
            polarity,
        ) in CHILDREN
    )

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
