#!/usr/bin/env python3
"""Enrich the seeded METPO colony morphology record with stable URL evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "colony_morphology.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T11:15:17Z"
ASM_PROTOCOL = (
    "https://asm.org/asm/media/protocol-images/colony-morphology-protocol.pdf"
)

UPDATES = {
    "definition_source": ASM_PROTOCOL,
    "evidence": [
        {
            "reference": ASM_PROTOCOL,
            "snippet": (
                "If well separated from other colonies, a colony will have a "
                "characteristic shape (both in elevation and margin), size, "
                "color, and consistency."
            ),
            "notes": (
                "Breakwell et al. describe shape, elevation, margin, size, color, "
                "and consistency as characteristic macroscopic features of a "
                "well-separated colony on solid medium."
            ),
        },
        {
            "reference": ASM_PROTOCOL,
            "snippet": (
                "Describe the form, elevation, and margin as indicated in Fig. 1. "
                "Also indicate whether the colonies are smooth (shiny glistening "
                "surface), rough (dull, bumpy, granular, or matte surface), or "
                "mucoid (slimy or gummy appearance)."
            ),
            "notes": (
                "The peer-reviewed ASM protocol explicitly treats colony form, "
                "elevation, margin, and surface texture as morphology descriptors."
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
    if record.get("identifier") != "METPO:1007062":
        raise ValueError(f"expected METPO:1007062, got {record.get('identifier')!r}")
    if record.get("label") != "colony morphology":
        raise ValueError(f"expected colony morphology, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO colony morphology phenotype with stable "
            "ASM protocol evidence after a repository-wide duplicate review "
            "covering ignored and hidden files."
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
