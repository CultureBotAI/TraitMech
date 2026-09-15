#!/usr/bin/env python3
"""Add the trimethylamine N-oxide respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "metabolism"
    / "trimethylamine_n_oxide_respiration.yaml"
)
DENBY = "DOI:10.1111/1462-2920.12726"
QIU = "DOI:10.3389/fmicb.2024.1467153"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T02:00:15Z"

RECORD = {
    "identifier": "traitmech:000199",
    "label": "trimethylamine N-oxide respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses trimethylamine "
        "N-oxide as the terminal electron acceptor and reduces it to "
        "trimethylamine for energy conservation."
    ),
    "definition_source": DENBY,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "TMAO respiration",
            "synonym_type": "EXACT_SYNONYM",
            "source": QIU,
        },
    ],
    "evidence": [
        {
            "reference": DENBY,
            "snippet": (
                "anaerobic respiratory growth with trimethylamine-N-oxide "
                "(TMAO) as the terminal electron acceptor"
            ),
            "notes": (
                "Denby et al. support TMAO as the organism-level terminal "
                "electron acceptor for anaerobic respiratory growth."
            ),
        },
        {
            "reference": DENBY,
            "snippet": (
                "TMAO is reduced to TMA by the enzyme TMAO reductase, "
                "encoded by the torCAD operon"
            ),
            "notes": (
                "Denby et al. describe reduction of trimethylamine N-oxide "
                "to trimethylamine by the TorCAD-linked TMAO reductase."
            ),
        },
        {
            "reference": QIU,
            "snippet": (
                "switching from aerobic intracellular energy metabolism to "
                "trimethylamine N-oxide respiration"
            ),
            "notes": (
                "Qiu and Tang use the unabbreviated respiration label while "
                "linking high-pressure survival in Shewanella "
                "eurypsychrophilus YLB-09 to TMAO respiration."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "note": (
                "Denby et al. characterized E. coli K-12 MG1655 adaptation "
                "from anaerobic fermentative growth to a "
                "TMAO-respiratory/fermentative steady state after TMAO "
                "addition."
            ),
            "reference": DENBY,
        },
    ],
    "discussions": [
        {
            "discussion_id": "trimethylamine-n-oxide-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "trimethylamine N-oxide respiration before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot has no active organism-level "
                "class for trimethylamine N-oxide respiration. Candidate EC, "
                "Rhea, and protein-family terms for TorA or broader "
                "trimethylamine N-oxide reductases are narrower than the "
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
            "Minted trimethylamine N-oxide respiration as a DOI-backed "
            "anaerobic respiration TraitRecord with an exact TMAO "
            "respiration synonym after a repository-wide duplicate review "
            "covering ignored and hidden files; the local METPO snapshot "
            "has no exact class and the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v76."
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
