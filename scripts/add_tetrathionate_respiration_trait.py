#!/usr/bin/env python3
"""Add the tetrathionate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "tetrathionate_respiration.yaml"
HENSEL = "DOI:10.1046/j.1365-2958.1999.01345.x"
PRICE_CARTER = "DOI:10.1128/JB.183.8.2463-2475.2001"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T02:26:41Z"

RECORD = {
    "identifier": "traitmech:000200",
    "label": "tetrathionate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses tetrathionate "
        "as the terminal electron acceptor and reduces it to thiosulfate "
        "for energy conservation."
    ),
    "definition_source": HENSEL,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "evidence": [
        {
            "reference": HENSEL,
            "snippet": (
                "A range of bacteria are able to use tetrathionate as a "
                "terminal respiratory electron acceptor"
            ),
            "notes": (
                "Hensel et al. support tetrathionate as an organism-level "
                "terminal electron acceptor for anaerobic respiration."
            ),
        },
        {
            "reference": HENSEL,
            "snippet": (
                "ttrA, ttrB and ttrC are the tetrathionate reductase "
                "structural genes"
            ),
            "notes": (
                "Hensel et al. identify the TtrA/TtrB/TtrC structural "
                "genes for Salmonella tetrathionate reductase."
            ),
        },
        {
            "reference": PRICE_CARTER,
            "snippet": "Salmonella reduces tetrathionate to thiosulfate",
            "notes": (
                "Price-Carter et al. support thiosulfate as the reduction "
                "product of Salmonella tetrathionate respiration."
            ),
        },
        {
            "reference": PRICE_CARTER,
            "snippet": (
                "the electron acceptor tetrathionate, which allows "
                "Salmonella to grow anaerobically on ethanolamine or "
                "1,2-propanediol"
            ),
            "notes": (
                "Price-Carter et al. support tetrathionate-dependent "
                "anaerobic growth in Salmonella enterica serovar "
                "Typhimurium LT2."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:99287",
            "taxon_label": (
                "Salmonella enterica subsp. enterica serovar "
                "Typhimurium str. LT2"
            ),
            "note": (
                "Price-Carter et al. showed that the electron acceptor "
                "tetrathionate supports anaerobic growth of Salmonella "
                "enterica serovar Typhimurium LT2 on ethanolamine or "
                "1,2-propanediol."
            ),
            "reference": PRICE_CARTER,
        },
    ],
    "discussions": [
        {
            "discussion_id": "tetrathionate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "tetrathionate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot has no active organism-level "
                "class for tetrathionate respiration. Candidate EC, Rhea, "
                "and protein-family terms for tetrathionate reductase or "
                "the TtrA/TtrB/TtrC complex are narrower than the "
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
            "Minted tetrathionate respiration as a DOI-backed anaerobic "
            "respiration TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; the local METPO "
            "snapshot has no exact class and the replacement placeholder "
            "is reserved in proposals/metpo_traitmech_v77."
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
