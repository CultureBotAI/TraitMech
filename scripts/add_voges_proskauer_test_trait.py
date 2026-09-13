#!/usr/bin/env python3
"""Add seeded METPO Voges-Proskauer-test parent and resolve its child gap."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "voges_proskauer_test.yaml"
VOGES_PROSKAUER_POSITIVE = (
    REPO_ROOT / "data" / "traits" / "other" / "voges_proskauer_test_positive.yaml"
)

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T21:15:14Z"
TIMESTAMP = "2026-09-12T21:15:44Z"

SEED_RECORD = {
    "identifier": "METPO:1005016",
    "label": "Voges-Proskauer test",
    "definition": (
        "An assay that tests the ability of an organism to produce acetoin "
        "from glucose via the butanediol fermentation pathway."
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
                "Bacteria fermenting sugars via the butanediol pathway "
                "produce acetoin (i.e., acetyl methyl carbinol or "
                "3-hydroxybutanone) as an intermediate which can be further "
                "reduced to 2,3-butanediol."
            ),
            "notes": (
                "The ASM protocol links acetoin production directly to sugar "
                "fermentation through the butanediol pathway."
            ),
        },
        {
            "reference": ASM_MRVP,
            "snippet": (
                "In the presence of KOH the intermediate acetoin is oxidized "
                "to diacetyl, a reaction which is catalyzed by a-naphthol "
                "(2). Diacetyl reacts with the guanidine group associated "
                "with molecules contributed by peptone in the medium, to "
                "form a pinkish-red-colored product (Fig. 2A)."
            ),
            "notes": (
                "The same protocol explains that the Voges-Proskauer "
                "reaction detects acetoin via Barritt chemistry that forms a "
                "pinkish-red product."
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


def build_voges_proskauer_test() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO Voges-Proskauer-test assay parent with "
            "stable-URL butanediol-pathway and acetoin-readout evidence "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def resolve_positive_parent_gap(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1005017":
        raise ValueError(f"expected METPO:1005017, got {record.get('identifier')!r}")
    if record.get("label") != "Voges-Proskauer test positive":
        raise ValueError(
            f"expected Voges-Proskauer test positive, got {record.get('label')!r}"
        )
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")

    discussions = record.get("discussions")
    if not isinstance(discussions, list):
        raise ValueError("expected Voges-Proskauer positive to have discussions")
    matches = [
        discussion
        for discussion in discussions
        if discussion.get("discussion_id")
        == "voges-proskauer-test-positive-assay-parent-gap"
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one assay-parent discussion, got {len(matches)}")
    discussion = matches[0]
    if discussion.get("status") != "OPEN":
        raise ValueError(f"expected OPEN discussion, got {discussion.get('status')!r}")
    if "resolved_date" in discussion or "resolution_note" in discussion:
        raise ValueError("expected unresolved discussion without resolution fields")

    record["parent_traits"] = ["METPO:1005016"]
    discussion["status"] = "RESOLVED"
    discussion["resolved_date"] = "2026-09-12"
    discussion["resolution_note"] = (
        "METPO:1005016 is now represented as the seeded Voges-Proskauer-test "
        "assay parent, so this positive assay-outcome phenotype can use its "
        "exact source superclass instead of a temporary direct phenotype "
        "parent; this resolves the exact METPO assay-parent gap, not the "
        "broader non-assay parent question for assay-outcome phenotypes."
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVED_PARENT_GAP",
        changes=(
            "Reparented Voges-Proskauer test positive below the newly curated "
            "METPO:1005016 Voges-Proskauer test assay parent and marked the "
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

    updates = [
        (TARGET, build_voges_proskauer_test()),
        (
            VOGES_PROSKAUER_POSITIVE,
            resolve_positive_parent_gap(load_record(VOGES_PROSKAUER_POSITIVE)),
        ),
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
