#!/usr/bin/env python3
"""Enrich the seeded METPO lateral flagellation record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "lateral_flagellation.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T08:09:00Z"

UPDATES = {
    "definition_source": "DOI:10.1111/j.1574-6968.2006.00403.x",
    "parent_traits": ["traitmech:000056"],
    "evidence": [
        {
            "reference": "DOI:10.1111/j.1574-6968.2006.00403.x",
            "snippet": (
                "These bacteria are able to express both a constitutive polar "
                "flagellum required for swimming motility and a separate lateral "
                "flagella system that is induced in viscous media or on surfaces "
                "and is essential for swarming motility."
            ),
            "notes": (
                "Merino et al. review lateral flagella as a distinct, inducible "
                "flagellar system in bacteria with dual polar and lateral systems."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.167.1.210-218.1986",
            "snippet": (
                "The polar flagellum is responsible for motility in a liquid "
                "environment (swimming), and the lateral flagella enable the "
                "bacteria to move over surfaces (swarming)."
            ),
            "notes": (
                "Belas et al. directly connect V. parahaemolyticus lateral "
                "flagella with surface swarming."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.185.15.4508-4518.2003",
            "snippet": (
                "Multiple proton-driven lateral flagella enable translocation "
                "over surfaces (i.e., swarming)."
            ),
            "notes": (
                "Stewart and McCarter describe the lateral flagella of "
                "V. parahaemolyticus as surface-translocation organelles."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.188.3.852-862.2006",
            "snippet": (
                "Mesophilic Aeromonas strains express a polar flagellum in all "
                "culture conditions, and certain strains produce lateral flagella "
                "on semisolid media or on surfaces."
            ),
            "notes": (
                "Canals et al. show that lateral flagella are an Aeromonas trait "
                "as well as a Vibrio parahaemolyticus trait."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:670",
            "taxon_label": "Vibrio parahaemolyticus",
            "note": (
                "Belas et al. describe V. parahaemolyticus as producing a polar "
                "swimming flagellum and lateral flagella that enable swarming on "
                "surfaces."
            ),
            "reference": "DOI:10.1128/jb.167.1.210-218.1986",
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
    if record.get("identifier") != "METPO:1005036":
        raise ValueError(f"expected METPO:1005036, got {record.get('identifier')!r}")
    if record.get("label") != "lateral flagellation":
        raise ValueError(f"expected lateral flagellation, got {record.get('label')!r}")
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
            "Enriched the seeded METPO lateral flagellation phenotype with "
            "DOI-backed lateral-flagella evidence after a repository-wide "
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
