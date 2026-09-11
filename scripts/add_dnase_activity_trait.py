#!/usr/bin/env python3
"""Add DNase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "dnase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "traitmech:000138",
    "label": "DNase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active DNase enzymes that hydrolyze DNA."
    ),
    "definition_source": "DOI:10.3389/fmicb.2019.00969",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "DNase production",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.22207/JPAM.14.1.44",
        }
    ],
    "evidence": [
        {
            "reference": "DOI:10.3389/fmicb.2019.00969",
            "snippet": (
                "unexpected and widespread presence of DNase secretion in bacteria "
                "in general and in MGP more specifically"
            ),
            "notes": (
                "Al-Wahaibi et al. assayed marine bacterial isolates for "
                "extracellular DNase secretion."
            ),
        },
        {
            "reference": "DOI:10.22207/JPAM.14.1.44",
            "snippet": (
                "screened for their capacity to produce DNA hydrolyzing activity "
                "on DNase test agar plate"
            ),
            "notes": (
                "Asha and Krishnaveni screened halophilic marine-sediment "
                "Bacillus-group isolates for DNA hydrolysis on DNase test agar."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2026187",
            "taxon_label": "Bacillus pacificus",
            "note": (
                "Bacillus pacificus KVCMST-8A-12 was reported as a "
                "DNase-producing marine-sediment isolate."
            ),
            "reference": "DOI:10.1128/MRA.01011-21",
        }
    ],
    "discussions": [
        {
            "discussion_id": "dnase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for DNase activity "
                "before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004536 denotes the DNA nuclease molecular function rather "
                "than the organism-level DNase production phenotype, so it is "
                "too scope-shifted for an equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-11",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted DNase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has no exact DNase activity class yet."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
