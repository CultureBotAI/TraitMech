#!/usr/bin/env python3
"""Enrich the seeded METPO non-hemolytic record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "non_hemolytic.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T10:34:52Z"
PETJUL_DOI = "DOI:10.14202/vetworld.2025.3622-3630"

UPDATES = {
    "definition_source": PETJUL_DOI,
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": PETJUL_DOI,
            "snippet": (
                "Hemolysis testing revealed γ-hemolysis for all strains, "
                "confirming non-hemolytic and non-pathogenic properties."
            ),
            "notes": (
                "Petjul et al. examined hemolytic patterns on Columbia agar "
                "supplemented with 5% sheep blood and reported gamma hemolysis "
                "for all assayed Bacillus isolates, supporting non-hemolysis "
                "as absence of red-blood-cell lysis on blood agar."
            ),
        }
    ],
    "discussions": [
        {
            "discussion_id": "non-hemolytic-parent-gap",
            "prompt": (
                "Resolve a neutral parent axis for absence of hemolysis before "
                "narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005025 is the seeded superclass of METPO:1005027, but "
                "METPO:1005025 defines the ability to lyse red blood cells; "
                "this absence phenotype is temporarily parented directly to "
                "METPO:1000059 phenotype until METPO has a neutral hemolysis "
                "axis or another broader parent for hemolysis-test outcomes."
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
    if record.get("identifier") != "METPO:1005027":
        raise ValueError(f"expected METPO:1005027, got {record.get('identifier')!r}")
    if record.get("label") != "non-hemolytic":
        raise ValueError(f"expected non-hemolytic, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1005025"]:
        raise ValueError(
            f"expected hemolysis parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO non-hemolytic child class with "
            "DOI-backed gamma-hemolysis evidence after a repository-wide "
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
