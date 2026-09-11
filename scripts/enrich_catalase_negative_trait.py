#!/usr/bin/env python3
"""Enrich the seeded METPO catalase negative record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "catalase_negative.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T10:12:30Z"
CATALASE_ASSAY_DOI = "DOI:10.1038/srep03081"
E_FAECIUM_DOI = "DOI:10.1128/iai.72.8.4512-4520.2004"

UPDATES = {
    "definition_source": CATALASE_ASSAY_DOI,
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": CATALASE_ASSAY_DOI,
            "snippet": (
                "The enzyme-generated oxygen bubbles trapped by Triton X-100 "
                "were visualized as foam"
            ),
            "notes": (
                "Iwase et al. tie the catalase assay signal to oxygen bubbles "
                "from hydrogen-peroxide decomposition, supporting no visible "
                "bubbling as a negative test outcome."
            ),
        },
        {
            "reference": E_FAECIUM_DOI,
            "snippet": (
                "E. faecium is catalase negative, and the major mechanism to "
                "scavenge hydrogen peroxide is NADH peroxidase"
            ),
            "notes": (
                "Moy et al. identify E. faecium as catalase-negative and "
                "contrast its NADH-peroxidase scavenging with catalase-bearing "
                "E. faecalis under heme-supplemented conditions."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1352",
            "taxon_label": "Enterococcus faecium",
            "note": (
                "Moy et al. describe E. faecium as catalase-negative in the "
                "context of hydrogen-peroxide accumulation and scavenging."
            ),
            "reference": E_FAECIUM_DOI,
        }
    ],
    "discussions": [
        {
            "discussion_id": "catalase-negative-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for negative catalase-test "
                "phenotypes before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1007080 is the seeded superclass of METPO:1007084, but "
                "METPO:1007080 defines an assay rather than a broader "
                "microbial trait class, so this record is temporarily parented "
                "directly to METPO:1000059 phenotype."
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
    if record.get("identifier") != "METPO:1007084":
        raise ValueError(f"expected METPO:1007084, got {record.get('identifier')!r}")
    if record.get("label") != "catalase negative":
        raise ValueError(f"expected catalase negative, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007080"]:
        raise ValueError(
            f"expected catalase-test parent, got {record.get('parent_traits')!r}"
        )

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO catalase negative test-outcome "
            "phenotype with DOI-backed assay and Enterococcus faecium "
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
