#!/usr/bin/env python3
"""Enrich the seeded METPO epibiont-phenotype record with URL evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "epibiont_phenotype.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T09:20:00Z"

BACDIVE_U95 = "https://bacdive.dsmz.de/strain/24523"

UPDATES = {
    "definition_source": "DOI:10.1099/ijs.0.042838-0",
    "evidence": [
        {
            "reference": "DOI:10.1099/ijs.0.042838-0",
            "snippet": "were isolated from the marine alga Ulva australis",
            "notes": (
                "Penesyan et al. describe Epibacterium ulvae strains U95 and "
                "U82 as bacteria associated with the marine green alga "
                "Ulva australis."
            ),
        },
        {
            "reference": BACDIVE_U95,
            "snippet": "isolated from surface of the marine green alga Ulva australis",
            "notes": (
                "BacDive records the E. ulvae type strain U95 as isolated from "
                "the external surface of the marine green alga Ulva australis."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1156985",
            "taxon_label": "Epibacterium ulvae",
            "note": (
                "Species represented by type strain U95 (= DSM 24752 = "
                "LMG 26464), which was isolated from the surface of the marine "
                "green alga Ulva australis."
            ),
            "reference": BACDIVE_U95,
        }
    ],
}

SEEDED_SYNONYMS = [
    {
        "synonym_text": "ectosymbiont",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "epibiont",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def enrich(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007093":
        raise ValueError(f"expected METPO:1007093, got {record.get('identifier')!r}")
    if record.get("label") != "epibiont phenotype":
        raise ValueError(f"expected epibiont phenotype, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1000059"]:
        raise ValueError(f"expected phenotype parent, got {record.get('parent_traits')!r}")
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO epibiont phenotype with DOI- and "
            "stable-URL-backed Epibacterium ulvae surface-association "
            "evidence after a repository-wide duplicate review covering "
            "ignored and hidden files."
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
