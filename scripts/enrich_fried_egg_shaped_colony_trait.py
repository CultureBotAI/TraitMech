#!/usr/bin/env python3
"""Enrich the seeded METPO fried-egg-shaped colony record."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "fried_egg_shaped_colony.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T13:41:36Z"
BERTIN_2013 = "DOI:10.1371/journal.pone.0068373"
MICRO_FRIED_EGG_COLONY = "http://purl.obolibrary.org/obo/MICRO_0000349"

UPDATES = {
    "definition_source": MICRO_FRIED_EGG_COLONY,
    "evidence": [
        {
            "reference": BERTIN_2013,
            "snippet": (
                "TR colonies showed the typical \u201cfried egg\u201d appearance, "
                "with a small opaque center surrounded by a large translucent "
                "peripheral area."
            ),
            "notes": (
                "Bertin et al. describe the opaque-center, translucent-periphery "
                "colony appearance that underlies the MICRO-derived "
                "fried-egg colony definition."
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


def enrich(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007069":
        raise ValueError(f"expected METPO:1007069, got {record.get('identifier')!r}")
    if record.get("label") != "fried-egg-shaped colony":
        raise ValueError(
            f"expected fried-egg-shaped colony, got {record.get('label')!r}"
        )
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007063"]:
        raise ValueError(
            f"expected colony shape parent, got {record.get('parent_traits')!r}"
        )
    if record.get("synonyms") != [
        {
            "synonym_text": "fried-egg colony",
            "synonym_type": "EXACT_SYNONYM",
            "source": "metpo.owl",
        }
    ]:
        raise ValueError(f"expected METPO exact synonym, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO fried-egg-shaped colony phenotype with "
            "stable MICRO definition provenance and DOI-backed opaque-center, "
            "translucent-periphery evidence after a repository-wide duplicate "
            "review covering ignored and hidden files."
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
