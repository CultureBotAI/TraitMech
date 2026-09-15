#!/usr/bin/env python3
"""Add the organohalide respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "organohalide_respiration.yaml"
HUG = "DOI:10.1098/rstb.2012.0322"
MAYMO_GATELL = "DOI:10.1126/science.276.5318.1568"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T04:25:36Z"

RECORD = {
    "identifier": "traitmech:000204",
    "label": "organohalide respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses an organohalide "
        "as the terminal electron acceptor for energy conservation."
    ),
    "definition_source": HUG,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "evidence": [
        {
            "reference": HUG,
            "snippet": (
                "Organohalide respiration is an anaerobic bacterial "
                "respiratory process that uses halogenated hydrocarbons as "
                "terminal electron acceptors during electron transport-based "
                "energy conservation."
            ),
            "notes": (
                "Hug et al. define organohalide respiration as anaerobic "
                "electron-transport-based energy conservation with "
                "halogenated hydrocarbons as terminal electron acceptors."
            ),
        },
        {
            "reference": HUG,
            "snippet": (
                "Organohalide-respiring bacteria have been identified from "
                "multiple bacterial phyla"
            ),
            "notes": (
                "Hug et al. support the record as a reusable bacterial "
                "respiration phenotype rather than a single-strain label."
            ),
        },
        {
            "reference": MAYMO_GATELL,
            "snippet": (
                "Growth of strain 195 with H2 and tetrachloroethene as the "
                "electron donor and acceptor pair required extracts from "
                "mixed microbial cultures."
            ),
            "notes": (
                "Maymo-Gatell et al. support tetrachloroethene as a "
                "growth-coupled organohalide electron acceptor in "
                "Dehalococcoides mccartyi strain 195."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:243164",
            "taxon_label": "Dehalococcoides mccartyi 195",
            "note": (
                "Strain 195 grows by coupling H2 oxidation to "
                "tetrachloroethene reduction, establishing growth-coupled "
                "organohalide respiration."
            ),
            "reference": MAYMO_GATELL,
        },
    ],
    "discussions": [
        {
            "discussion_id": "organohalide-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "organism-level organohalide respiration before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only obsolete "
                "Halogenated compound respiration and Organohalide "
                "respiration classes. Candidate reductive dehalogenase "
                "protein-family and enzyme terms are narrower than the "
                "whole-organism anaerobic respiration phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
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
            "Minted organohalide respiration as a DOI-backed anaerobic "
            "respiration TraitRecord after a repository-wide duplicate review "
            "covering ignored and hidden files; the local METPO snapshot has "
            "only obsolete organohalide/halogenated-compound respiration "
            "classes and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v81."
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
