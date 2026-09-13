#!/usr/bin/env python3
"""Enrich the seeded METPO generalist record."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "generalist.yaml"

BELL_BACTERIAL_GENERALISM = "DOI:10.1093/femsec/fiaa240"
VON_MEIJENFELDT_NICHE_BREADTH = "DOI:10.1038/s41559-023-02027-7"

CURATOR = "codex"
TIMESTAMP = "2026-09-12T22:35:00Z"

UPDATES = {
    "definition_source": BELL_BACTERIAL_GENERALISM,
    "evidence": [
        {
            "reference": BELL_BACTERIAL_GENERALISM,
            "snippet": (
                "Organisms are often categorized as generalists or specialists, "
                "corresponding to broad or narrow niche requirements"
            ),
            "notes": (
                "Bell and Bell frame bacterial generalism by broad niche "
                "requirements across environmental axes such as temperature "
                "tolerance and resource use."
            ),
        },
        {
            "reference": VON_MEIJENFELDT_NICHE_BREADTH,
            "snippet": (
                "Generalists can survive in many environments, whereas "
                "specialists are restricted to a single environment."
            ),
            "notes": (
                "The social-niche-breadth study defines generalists and "
                "specialists while introducing a niche-breadth score for "
                "prokaryotic genomes across environments."
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


def enrich_record(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1005040":
        raise ValueError(f"expected METPO:1005040, got {record.get('identifier')!r}")
    if record.get("label") != "generalist":
        raise ValueError(f"expected generalist, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO generalist phenotype with DOI-backed "
            "bacterial and prokaryotic niche-breadth evidence after a "
            "repository-wide duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    record = enrich_record(load_record(TARGET))
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
