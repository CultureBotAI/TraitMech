#!/usr/bin/env python3
"""Enrich the seeded METPO subpolar flagellation record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "subpolar_flagellation.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T08:30:00Z"

UPDATES = {
    "definition_source": "DOI:10.1128/JB.01405-06",
    "parent_traits": ["traitmech:000056"],
    "evidence": [
        {
            "reference": "DOI:10.1128/JB.01405-06",
            "snippet": (
                "The cell has two sets of flagellar systems, one thick "
                "flagellum and a few thin flagella, uniquely growing at "
                "subpolar positions."
            ),
            "notes": (
                "Kanbe et al. describe two morphologically distinct "
                "Bradyrhizobium flagellar systems that both emerge from "
                "subpolar positions."
            ),
        },
        {
            "reference": "DOI:10.3390/biom10050774",
            "snippet": (
                "Under the growth conditions commonly used in the laboratory, "
                "a single subpolar flagellum that traverses the cell membrane, "
                "is assembled on the surface."
            ),
            "notes": (
                "Camarena and Dreyfus review the Rhodobacter sphaeroides Fla1 "
                "system as a second bacterial example of subpolar flagellation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:224911",
            "taxon_label": "Bradyrhizobium diazoefficiens USDA 110",
            "note": (
                "Kanbe et al. directly observed subpolar thick and thin "
                "flagella in Bradyrhizobium japonicum 110spc4, a derivative "
                "of USDA 110 now assigned by NCBI to B. diazoefficiens."
            ),
            "reference": "DOI:10.1128/JB.01405-06",
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
    if record.get("identifier") != "METPO:1005037":
        raise ValueError(f"expected METPO:1005037, got {record.get('identifier')!r}")
    if record.get("label") != "subpolar flagellation":
        raise ValueError(f"expected subpolar flagellation, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "MORPHOLOGY":
        raise ValueError(f"expected MORPHOLOGY, got {record.get('trait_category')!r}")
    if record.get("parent_traits") not in (["METPO:1000704"], ["traitmech:000056"]):
        raise ValueError(
            f"expected flagellated/arrangement parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO subpolar flagellation phenotype with "
            "DOI-backed subpolar-flagella evidence after a repository-wide "
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
