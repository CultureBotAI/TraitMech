#!/usr/bin/env python3
"""Add acid phosphatase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / (
    "acid_phosphatase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T16:21:00Z"

RECORD = {
    "identifier": "traitmech:000142",
    "label": "acid phosphatase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active acid phosphatase enzymes that dephosphorylate "
        "phosphate-containing compounds under acidic conditions."
    ),
    "definition_source": "DOI:10.1128/JB.182.23.6850-6853.2000",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1128/JB.182.23.6850-6853.2000",
            "snippet": (
                "the presence of acid phosphatase activity in the culture "
                "filtrate of M. tuberculosis was confirmed and a 28-kDa protein "
                "possessing this activity was purified and characterized"
            ),
            "notes": (
                "Saleh and Belisle confirmed Mycobacterium tuberculosis acid "
                "phosphatase activity and purified the SapM protein carrying "
                "that activity."
            ),
        },
        {
            "reference": "DOI:10.1155/2021/8888641",
            "snippet": (
                "According to the API ZYM assays, all three isolates were "
                "positive for alkaline phosphatase, leucine aryl amidase, acid "
                "phosphatase, and naphthol_AS_BI_phosphohydrolase."
            ),
            "notes": (
                "Mekonnen et al. treated acid phosphatase as an assayed "
                "bacterial exoenzyme phenotype in rapid urease-producing soil "
                "isolates."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1773",
            "taxon_label": "Mycobacterium tuberculosis",
            "note": (
                "Mycobacterium tuberculosis secretes SapM, a culture-filtrate "
                "enzyme purified through its acid phosphatase activity."
            ),
            "reference": "DOI:10.1128/JB.182.23.6850-6853.2000",
        }
    ],
    "discussions": [
        {
            "discussion_id": "acid-phosphatase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for acid phosphatase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0003993 carries the same acid phosphatase activity label "
                "but denotes the enzyme molecular function rather than the "
                "organism-level phenotype, so it is appropriate as a "
                "causal-node grounding rather than an equivalent TraitRecord "
                "xref."
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
            "Minted acid phosphatase activity as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact acid phosphatase activity class "
            "yet."
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
