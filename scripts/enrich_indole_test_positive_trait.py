#!/usr/bin/env python3
"""Enrich the seeded METPO indole-test-positive record with DOI evidence."""
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

TARGET = REPO_ROOT / "data" / "traits" / "other" / "indole_test_positive.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T07:00:00Z"

UPDATES = {
    "definition_source": "DOI:10.1128/AEM.02787-15",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1128/AEM.02787-15",
            "snippet": "Indole, a bacterial product of tryptophan degradation",
            "notes": (
                "Darkoh et al. support microbial indole production as a "
                "tryptophan-degradation phenotype and evaluate indole detection "
                "in bacterial cultures."
            ),
        },
        {
            "reference": "DOI:10.1128/AEM.02787-15",
            "snippet": (
                "enterotoxigenic Escherichia coli strain H10407 produces 3.3 "
                "± 0.22 mM indole during a 24-h period in the presence of "
                "5 mM tryptophan"
            ),
            "notes": (
                "Darkoh et al. measured indole production by the enterotoxigenic "
                "E. coli H10407 strain under tryptophan-supplemented culture "
                "conditions."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:316401",
            "taxon_label": "Escherichia coli ETEC H10407",
            "note": (
                "Enterotoxigenic E. coli H10407 produced millimolar indole after "
                "24 h of growth with tryptophan supplementation."
            ),
            "reference": "DOI:10.1128/AEM.02787-15",
        }
    ],
    "discussions": [
        {
            "discussion_id": "indole-test-positive-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for positive indole-test phenotypes "
                "before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005010 is the seeded superclass of METPO:1005011, but "
                "METPO:1005010 defines an assay rather than a broader microbial "
                "trait class, so this record is temporarily parented directly to "
                "METPO:1000059 phenotype."
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
    if record.get("identifier") != "METPO:1005011":
        raise ValueError(f"expected METPO:1005011, got {record.get('identifier')!r}")
    if record.get("label") != "indole test positive":
        raise ValueError(f"expected indole test positive, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1005010"]:
        raise ValueError(f"expected assay parent, got {record.get('parent_traits')!r}")

    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the active METPO indole-test-positive phenotype with "
            "DOI-backed indole production evidence after a repository-wide "
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
