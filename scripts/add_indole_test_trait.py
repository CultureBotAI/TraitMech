#!/usr/bin/env python3
"""Add seeded METPO indole-test parent and resolve child parent gaps."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "indole_test.yaml"
INDOLE_POSITIVE = REPO_ROOT / "data" / "traits" / "other" / "indole_test_positive.yaml"
INDOLE_NEGATIVE = REPO_ROOT / "data" / "traits" / "other" / "indole_test_negative.yaml"

ASM_INDOLE = "https://asm.org/protocols/indole-test-protocol"

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T21:35:36Z"
TIMESTAMP = "2026-09-12T21:38:12Z"
REVIEW_TIMESTAMP = "2026-09-12T21:50:37Z"

SEED_RECORD = {
    "identifier": "METPO:1005010",
    "label": "indole test",
    "definition": (
        "An assay that tests the ability of an organism to produce indole from "
        "tryptophan."
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
    "definition_source": ASM_INDOLE,
    "evidence": [
        {
            "reference": ASM_INDOLE,
            "snippet": (
                "The indole test screens for the ability of an organism to "
                "degrade the amino acid tryptophan and produce indole."
            ),
            "notes": (
                "The ASM protocol defines the indole test as an assay for "
                "organism-level tryptophan degradation to indole."
            ),
        },
        {
            "reference": ASM_INDOLE,
            "snippet": (
                "The chief requirement for culturing an organism prior to "
                "performing the indole test is that the medium contains a "
                "sufficient quantity of tryptophan (5)."
            ),
            "notes": (
                "The protocol explains that the indole-test medium needs "
                "tryptophan so production of indole can report tryptophan "
                "degradation."
            ),
        },
    ],
}

CHILDREN = [
    (
        INDOLE_POSITIVE,
        "METPO:1005011",
        "indole test positive",
        "indole-test-positive-assay-parent-gap",
        "positive",
    ),
    (
        INDOLE_NEGATIVE,
        "METPO:1005012",
        "indole test negative",
        "indole-test-negative-assay-parent-gap",
        "negative",
    ),
]


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def build_indole_test() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO indole-test assay parent with stable-URL "
            "tryptophan-to-indole assay evidence after a repository-wide "
            "duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Preserved the ASM source-local tryptophan citation marker after "
            "Claude Code Review issue #874 so the second evidence snippet is "
            "visibly a complete sentence."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
    if "resolved_date" in discussion or "resolution_note" in discussion:
        raise ValueError("expected unresolved discussion without resolution fields")

    record["parent_traits"] = ["METPO:1005010"]
    discussion["status"] = "RESOLVED"
    discussion["resolved_date"] = "2026-09-12"
    discussion["resolution_note"] = (
        "METPO:1005010 is now represented as the seeded indole-test assay "
        "parent, so this assay-outcome phenotype can use its exact source "
        "superclass instead of a temporary direct phenotype parent; this "
        "resolves the exact METPO assay-parent gap, not the broader non-assay "
        "parent question for assay-outcome phenotypes."
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVED_PARENT_GAP",
        changes=(
            f"Reparented indole test {polarity} below the newly curated "
            "METPO:1005010 indole test assay parent and marked the temporary "
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

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    updates = [(TARGET, build_indole_test())]
    updates.extend(
        (
            path,
            resolve_child_parent_gap(
                load_record(path),
                expected_identifier=identifier,
                expected_label=label,
                discussion_id=discussion_id,
                polarity=polarity,
            ),
        )
        for path, identifier, label, discussion_id, polarity in CHILDREN
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
