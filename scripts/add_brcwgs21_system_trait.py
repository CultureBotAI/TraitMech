#!/usr/bin/env python3
"""Add the BrcWGS21 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brcwgs21_system.yaml"

KIEFFER = "DOI:10.1126/science.ads0915"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T17:12:42Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T17:12:43Z"
IDENTIFIER = "traitmech:000520"
PROPOSAL = "proposals/metpo_traitmech_v397"

BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
BRCWGS21_LOW_MOI_PROFILE_SNIPPET = (
    "brcWGS21 L 88.6 60.5 93.4 77.2 25.6 0 93.4"
)
BRCWGS21_HIGH_MOI_PROFILE_SNIPPET = (
    "brcWGS21 H 95.6 98.2 84.9 98.0 24.9 78.4"
)
BRCWGS21_ATTC_SNIPPET = """brc113
brc217
brc76
brcWGS21
brc22
brc23"""
BRCWGS21_ECOLI_CONSTRUCT_SNIPPET = (
    "C935\npMBA brcWGS21\nE. coli IJ1862"
)
BRCWGS21_KPNEUMONIAE_CONSTRUCT_SNIPPET = (
    "C941\npMBA brcWGS21\nK. pneumoniae\n\nKP5"
)
ARTICLE_ROW = (
    "| gcuWGS21 | 10\\.1126/science\\.ads0915 | Mobile integrons "
    "encode phage defense systems | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the gcuWGS21 "
            "source key to the Kieffer et al. mobile-integron BRiC paper."
        ),
    }


def bric_panel_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRIC_PROFILE_SNIPPET,
        "notes": (
            "Kieffer et al. classify positive integron cassettes as BRiCs and "
            "compare their defense profiles across a phage panel."
        ),
    }


def brcwgs21_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRCWGS21_ATTC_SNIPPET,
        "notes": (
            "Kieffer et al. include brcWGS21 among identified BRiCs with "
            "predicted attC secondary structures."
        ),
    }


def brcwgs21_low_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRCWGS21_LOW_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 BrcWGS21 "
            "low-MOI heatmap row; the visible cells show reduced inhibition, "
            "including 88.6% for MS2, 60.5% for T7, 93.4% for HK544, "
            "77.2% for F13, 25.6% for Vs1, 0% for Px4, and 93.4% for Px5."
        ),
    }


def brcwgs21_high_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRCWGS21_HIGH_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 BrcWGS21 "
            "high-MOI heatmap row; the visible cells show reduced inhibition, "
            "including 95.6% for MS2, 98.2% for phi80, 84.9% for HK544, "
            "98.0% for F13, 24.9% for Vs1, and 78.4% for Px4."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "BrcWGS21 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "gcuWGS21/BrcWGS21 bacteriophage-resistance integron cassette that "
        "supports growth during bacteriophage challenge."
    ),
    "definition_source": KIEFFER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "gcuWGS21",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "brcWGS21",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brcwgs21_low_moi_profile_evidence(),
        brcwgs21_high_moi_profile_evidence(),
        bric_panel_evidence(),
        brcwgs21_attc_evidence(),
        {
            "reference": KIEFFER,
            "snippet": BRCWGS21_ECOLI_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists pMBA "
                "brcWGS21 in E. coli IJ1862 for high/low-MOI phage-panel "
                "testing."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRCWGS21_KPNEUMONIAE_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pMBA brcWGS21 plasmid introduced into Klebsiella "
                "pneumoniae KP5."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": (
                "brcwgs21_integron_cassette_confers_phage_resistance"
            ),
            "title": "BrcWGS21 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a "
                "gcuWGS21/BrcWGS21 bacteriophage-resistance integron "
                "cassette to phage resistance and BrcWGS21 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures BrcWGS21 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, or a "
                "DefenseFinder HMM/rules profile absent from the pinned "
                "snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brcwgs21_integron_cassette",
                    "label": "BrcWGS21 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette named by the "
                        "gcuWGS21 source key and curated as BrcWGS21."
                    ),
                },
                {
                    "node_id": "brcwgs21_phage_resistance",
                    "label": "BrcWGS21 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcuWGS21/BrcWGS21 integron cassette."
                    ),
                },
                {
                    "node_id": "brcwgs21_system_trait",
                    "label": "BrcWGS21 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded BrcWGS21 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "brcwgs21_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brcwgs21_phage_resistance",
                    "description": (
                        "The gcuWGS21/BrcWGS21 integron cassette contributes "
                        "to phage resistance during phage-panel assays."
                    ),
                    "evidence": [
                        brcwgs21_low_moi_profile_evidence(),
                        brcwgs21_high_moi_profile_evidence(),
                    ],
                },
                {
                    "subject": "brcwgs21_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brcwgs21_system_trait",
                    "description": (
                        "BrcWGS21-linked phage resistance realizes the "
                        "BrcWGS21 system possession trait."
                    ),
                    "evidence": [
                        brcwgs21_low_moi_profile_evidence(),
                        brcwgs21_high_moi_profile_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brcwgs21_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "BrcWGS21 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        brcwgs21_attc_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brcwgs21-defensefinder-model-gap",
            "prompt": (
                "Resolve BrcWGS21 native host breadth, exact sensitive-phage "
                "breadth, molecular output, and DefenseFinder HMM/rules "
                "coverage before minting narrower BrcWGS21 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brcWGS21 as a "
                "bacteriophage-resistance integron cassette, and the pinned "
                "DefenseFinder article registry maps the gcuWGS21 source key "
                "to the same Science article. The pinned HMM inventory and "
                "rules table have no exact gcuWGS21 or BrcWGS21 row, so the "
                "first-pass record leaves native-host breadth, profile "
                "boundaries, exact phage target breadth, and direct molecular "
                "output unresolved."
            ),
            "evidence": [
                brcwgs21_low_moi_profile_evidence(),
                brcwgs21_high_moi_profile_evidence(),
                bric_panel_evidence(),
                brcwgs21_attc_evidence(),
                {
                    "reference": KIEFFER,
                    "snippet": BRCWGS21_KPNEUMONIAE_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brcWGS21 in the heterologous "
                        "Klebsiella pneumoniae KP5 BRiC panel."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder HMM inventory found no exact gcuWGS21, "
                        "brcWGS21, or BrcWGS21 row."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder rules table found no exact gcuWGS21, "
                        "brcWGS21, or BrcWGS21 system row."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#"
                "brcwgs21_integron_cassette_confers_phage_resistance"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted BrcWGS21 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at BRiC integron-cassette level because the pinned "
            "DefenseFinder article registry names gcuWGS21 but the pinned "
            "HMM inventory and rules table have no exact BrcWGS21 row; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed BrcWGS21 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcuWGS21/BrcWGS21 phage-resistance assays and a "
            "DefenseFinder gcuWGS21 article row, but not a direct named "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous BrcWGS21 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
