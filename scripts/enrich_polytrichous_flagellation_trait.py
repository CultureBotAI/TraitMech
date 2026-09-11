#!/usr/bin/env python3
"""Enrich the seeded METPO polytrichous flagellation record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "polytrichous_flagellation.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T08:46:00Z"

UPDATES = {
    "definition_source": "DOI:10.1128/AEM.64.10.3576-3583.1998",
    "trait_category": "MORPHOLOGY",
    "parent_traits": ["traitmech:000056"],
    "evidence": [
        {
            "reference": "DOI:10.1128/AEM.64.10.3576-3583.1998",
            "snippet": (
                "In transmission electron micrographs, isolate OC 1/4 exhibited "
                "monopolar polytrichous flagellation, with up to three flagella "
                "per cell (Fig. 4)."
            ),
            "notes": (
                "Huber et al. directly observed multiple flagella at one pole "
                "of Thermocrinis ruber OC 1/4."
            ),
        },
        {
            "reference": "DOI:10.1128/AEM.68.12.6310-6320.2002",
            "snippet": (
                "The cells have bipolar polytrichous flagella and exhibit a "
                "unique swimming pattern, rotating and translating along their "
                "short axis."
            ),
            "notes": (
                "Thar and Kuhl describe a second bacterial polytrichous "
                "arrangement, with flagella present at both cell poles."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:75906",
            "taxon_label": "Thermocrinis ruber",
            "note": (
                "Huber et al. directly observed up to three monopolar flagella "
                "per cell in the Thermocrinis ruber isolate OC 1/4."
            ),
            "reference": "DOI:10.1128/AEM.64.10.3576-3583.1998",
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
    if record.get("identifier") != "METPO:1007006":
        raise ValueError(f"expected METPO:1007006, got {record.get('identifier')!r}")
    if record.get("label") != "polytrichous flagellation":
        raise ValueError(f"expected polytrichous flagellation, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") not in ("MORPHOLOGY", "OTHER"):
        raise ValueError(f"expected MORPHOLOGY/OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") not in (["METPO:1007005"], ["traitmech:000056"]):
        raise ValueError(
            f"expected flagellar-arrangement parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO polytrichous flagellation phenotype with "
            "DOI-backed polytrichous-flagella evidence after a repository-wide "
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
