#!/usr/bin/env python3
"""Enrich the seeded METPO nitrification record with DOI-backed evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "nitrification.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T06:20:00Z"

UPDATES = {
    "definition_source": "DOI:10.3389/fmicb.2020.01900",
    "evidence": [
        {
            "reference": "DOI:10.3389/fmicb.2020.01900",
            "snippet": (
                "nitrification proceeds as a two-step process, involving the "
                "oxidation of ammonia to nitrite and the oxidation of nitrite "
                "to nitrate"
            ),
            "notes": (
                "Sedlacek et al. review the historical evidence that established "
                "nitrification as a microbially mediated, two-step ammonia- and "
                "nitrite-oxidation process."
            ),
        }
    ],
    "discussions": [
        {
            "discussion_id": "nitrification-component-go-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for the complete "
                "nitrification process before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO cites GO:0019329 ammonia oxidation and GO:0019332 "
                "nitrite oxidation as definition components, but each GO term "
                "covers only one half of the full two-step nitrification trait "
                "and is not exact enough for TraitRecord xrefs."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-11",
        }
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
    if record.get("identifier") != "METPO:1005001":
        raise ValueError(f"expected METPO:1005001, got {record.get('identifier')!r}")
    if record.get("label") != "nitrification":
        raise ValueError(f"expected nitrification, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "METABOLISM":
        raise ValueError(f"expected METABOLISM, got {record.get('trait_category')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the active METPO nitrification class with DOI-backed "
            "two-step ammonia- and nitrite-oxidation evidence after a "
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
