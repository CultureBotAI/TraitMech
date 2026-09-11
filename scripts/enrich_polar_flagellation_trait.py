#!/usr/bin/env python3
"""Enrich the seeded METPO polar flagellation record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "polar_flagellation.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T08:00:00Z"

UPDATES = {
    "definition_source": "DOI:10.1093/femsre/fuv034",
    "parent_traits": ["traitmech:000056"],
    "evidence": [
        {
            "reference": "DOI:10.1093/femsre/fuv034",
            "snippet": (
                "Bacteria differ in number and location of their flagella that "
                "appear in regular patterns at the cell surface (flagellation "
                "pattern)."
            ),
            "notes": (
                "Schuhmacher et al. support treating the number and cellular "
                "position of flagella as a flagellation-pattern morphology class."
            ),
        },
        {
            "reference": "DOI:10.3390/biom10040533",
            "snippet": (
                "Some bacterial species, such as the marine bacterium Vibrio "
                "alginolyticus, have a single polar flagellum that allows it "
                "to swim in liquid environments."
            ),
            "notes": (
                "Kojima et al. give Vibrio alginolyticus as a direct bacterial "
                "example whose flagellum is positioned at a cell pole."
            ),
        },
        {
            "reference": "DOI:10.3390/biom10040533",
            "snippet": (
                "Two regulators, FlhF and FlhG, function antagonistically to "
                "generate only one flagellum at the cell pole."
            ),
            "notes": (
                "Kojima et al. connect FlhF/FlhG regulation to generation of a "
                "polar flagellum, supporting polar placement as a microbial "
                "flagellation phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:663",
            "taxon_label": "Vibrio alginolyticus",
            "note": (
                "Kojima et al. describe V. alginolyticus as a marine bacterium "
                "with a single polar flagellum."
            ),
            "reference": "DOI:10.3390/biom10040533",
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
    if record.get("identifier") != "METPO:1005032":
        raise ValueError(f"expected METPO:1005032, got {record.get('identifier')!r}")
    if record.get("label") != "polar flagellation":
        raise ValueError(f"expected polar flagellation, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "MORPHOLOGY":
        raise ValueError(f"expected MORPHOLOGY, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000704"]:
        raise ValueError(f"expected flagellated parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO polar flagellation phenotype with "
            "DOI-backed flagellar-arrangement evidence after a repository-wide "
            "duplicate review covering ignored and hidden files."
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
