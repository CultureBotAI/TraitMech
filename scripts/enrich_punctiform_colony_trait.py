#!/usr/bin/env python3
"""Enrich the seeded METPO punctiform colony record."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "punctiform_colony.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T13:19:39Z"
KANDI_2015 = "DOI:10.7759/cureus.374"
OMP_PUNCTIFORM_COLONY = "http://purl.obolibrary.org/obo/OMP_0000240"

UPDATES = {
    "definition_source": OMP_PUNCTIFORM_COLONY,
    "evidence": [
        {
            "reference": KANDI_2015,
            "snippet": (
                "Colony morphology is one among the various characters of "
                "bacteria, which is also unique to a particular genus of "
                "bacteria that could be instrumental in preliminary "
                "identification. Size (measured in millimetres - pinpoint "
                "(≤ 1 mm), small (2-3 mm), medium (4-5 mm), and large "
                "(> 5 mm) colonies), shape (circular, irregular, rhomboid, "
                "umbonate, umbonate, filamentous, or rhizoid)"
            ),
            "notes": (
                "Kandi lists pinpoint as the smallest bacterial colony-size "
                "descriptor, matching the size component of the OMP-derived "
                "punctiform colony definition."
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
    if record.get("identifier") != "METPO:1007067":
        raise ValueError(f"expected METPO:1007067, got {record.get('identifier')!r}")
    if record.get("label") != "punctiform colony":
        raise ValueError(f"expected punctiform colony, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007063"]:
        raise ValueError(
            f"expected colony shape parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO punctiform colony phenotype with stable "
            "OMP definition provenance and DOI-backed pinpoint-size evidence "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files."
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
