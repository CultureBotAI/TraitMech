#!/usr/bin/env python3
"""Add seeded METPO indole-test-negative with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "indole_test_negative.yaml"

DARKOH = "DOI:10.1128/AEM.02787-15"
ALVES = "DOI:10.1128/JCM.00940-06"

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T17:38:53Z"
TIMESTAMP = "2026-09-12T17:40:50Z"
REVIEW_TIMESTAMP = "2026-09-12T17:52:10Z"
EXTERNAL_REVIEW_TIMESTAMP = "2026-09-12T18:01:45Z"
DARKOH_REVIEW_TIMESTAMP = "2026-09-12T18:09:40Z"

SEED_RECORD = {
    "identifier": "METPO:1005012",
    "label": "indole test negative",
    "definition": (
        "A phenotype in which an organism tests negative in the indole test, "
        "indicating it does not produce indole from tryptophan."
    ),
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1005010"],
    "curation_history": [
        {
            "timestamp": SEED_TIMESTAMP,
            "curator": "seed_from_metpo",
            "action": "SEEDED_FROM_METPO",
            "changes": "imported from data/raw/metpo.owl (CLASS)",
        }
    ],
}

UPDATES = {
    "parent_traits": ["METPO:1000059"],
    "definition_source": DARKOH,
    "evidence": [
        {
            "reference": DARKOH,
            "snippet": "Indole, a bacterial product of tryptophan degradation",
            "notes": (
                "Darkoh et al. support indole as a microbial "
                "tryptophan-degradation product."
            ),
        },
        {
            "reference": ALVES,
            "snippet": (
                "most clinical isolates classified as Klebsiella spp. belong "
                "to the K. pneumoniae (indole-negative isolates)"
            ),
            "notes": (
                "Alves et al. describe Klebsiella pneumoniae as an "
                "indole-negative Klebsiella species in a clinical-isolate "
                "biochemical typing context."
            ),
        },
        {
            "reference": ALVES,
            "snippet": (
                "A total of 102 (84%) of the 122 isolates were negative for "
                "indole production"
            ),
            "notes": (
                "Alves et al. reported negative indole-production phenotypes "
                "among Klebsiella clinical isolates tested biochemically."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:573",
            "taxon_label": "Klebsiella pneumoniae",
            "note": (
                "Alves et al. describe K. pneumoniae as an indole-negative "
                "Klebsiella species in a clinical-isolate biochemical typing "
                "context."
            ),
            "reference": ALVES,
        }
    ],
    "discussions": [
        {
            "discussion_id": "indole-test-negative-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for negative indole-test "
                "phenotypes before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005010 is the seeded superclass of METPO:1005012, "
                "but METPO:1005010 defines an assay rather than a broader "
                "microbial trait class, so this record is temporarily "
                "parented directly to METPO:1000059 phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
        }
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO indole-test-negative phenotype with DOI-backed "
            "indole-test evidence after a repository-wide duplicate review "
            "covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Tightened Alves Klebsiella wording after local review issue #855 "
            "to avoid implying Klebsiella pneumoniae is the only "
            "indole-negative Klebsiella or Raoultella species."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Removed unquoted Klebsiella variicola wording after external "
            "review issue #856 while preserving the indole-negative "
            "Klebsiella pneumoniae interpretation."
        ),
        llm_assisted=True,
        timestamp=EXTERNAL_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Trimmed unsupported Darkoh indole-assay wording after external "
            "review issue #857."
        ),
        llm_assisted=True,
        timestamp=DARKOH_REVIEW_TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = build_record()
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
