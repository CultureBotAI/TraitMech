#!/usr/bin/env python3
"""Add the Brc76 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc76_system.yaml"

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
TIMESTAMP = "2026-10-01T16:17:37Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T16:17:38Z"
IDENTIFIER = "traitmech:000519"
PROPOSAL = "proposals/metpo_traitmech_v396"

BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
BRC76_LOW_MOI_PROFILE_SNIPPET = "brc76 L 79.5 92.4 89.1 83.1"
BRC76_HIGH_MOI_PROFILE_SNIPPET = "brc76 H 96.6"
BRC76_ATTC_SNIPPET = """brc113
brc217
brc76
brcWGS21
brc22
brc23"""
BRC76_ECOLI_CONSTRUCT_SNIPPET = "C933\npMBA brc76\nE. coli IJ1862"
BRC76_KPNEUMONIAE_CONSTRUCT_SNIPPET = "C939\npMBA brc76\nK. pneumoniae\n\nKP5"
ARTICLE_ROW = (
    "| gcu76 | 10\\.1126/science\\.ads0915 | Mobile integrons "
    "encode phage defense systems | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the gcu76 source "
            "key to the Kieffer et al. mobile-integron BRiC paper."
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


def brc76_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC76_ATTC_SNIPPET,
        "notes": (
            "Kieffer et al. include brc76 among identified BRiCs with "
            "predicted attC secondary structures."
        ),
    }


def brc76_low_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC76_LOW_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc76 low-MOI "
            "E. coli IJ1862 heatmap row; the visible cells show reduced "
            "inhibition, including 79.5% for MS2, 92.4% for F1, 89.1% "
            "for phi80, and 83.1% for F13."
        ),
    }


def brc76_high_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC76_HIGH_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc76 high-MOI "
            "E. coli IJ1862 heatmap row; the visible MS2 cell shows 96.6% "
            "inhibition."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc76 system",
    "definition": (
        "A phage defense system in which an organism possesses a gcu76/Brc76 "
        "bacteriophage-resistance integron cassette that supports growth "
        "during bacteriophage challenge."
    ),
    "definition_source": KIEFFER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "gcu76",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "brc76",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brc76_low_moi_profile_evidence(),
        brc76_high_moi_profile_evidence(),
        bric_panel_evidence(),
        brc76_attc_evidence(),
        {
            "reference": KIEFFER,
            "snippet": BRC76_ECOLI_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists pMBA "
                "brc76 in E. coli IJ1862 for high/low-MOI phage-panel "
                "testing."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRC76_KPNEUMONIAE_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pMBA brc76 plasmid introduced into Klebsiella pneumoniae "
                "KP5."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brc76_integron_cassette_confers_phage_resistance",
            "title": "Brc76 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a gcu76/Brc76 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc76 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc76 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, or a "
                "DefenseFinder HMM/rules profile absent from the pinned "
                "snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc76_integron_cassette",
                    "label": "Brc76 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette named by the gcu76 "
                        "source key and curated as Brc76."
                    ),
                },
                {
                    "node_id": "brc76_phage_resistance",
                    "label": "Brc76 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcu76/Brc76 integron cassette."
                    ),
                },
                {
                    "node_id": "brc76_system_trait",
                    "label": "Brc76 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc76 "
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
                    "subject": "brc76_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc76_phage_resistance",
                    "description": (
                        "The gcu76/Brc76 integron cassette contributes to "
                        "phage resistance during phage-panel assays."
                    ),
                    "evidence": [
                        brc76_low_moi_profile_evidence(),
                        brc76_high_moi_profile_evidence(),
                    ],
                },
                {
                    "subject": "brc76_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc76_system_trait",
                    "description": (
                        "Brc76-linked phage resistance realizes the "
                        "Brc76 system possession trait."
                    ),
                    "evidence": [
                        brc76_low_moi_profile_evidence(),
                        brc76_high_moi_profile_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brc76_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc76 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        brc76_attc_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc76-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc76 native host breadth, exact sensitive-phage "
                "breadth, molecular output, and DefenseFinder HMM/rules "
                "coverage before minting narrower Brc76 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brc76 as a "
                "bacteriophage-resistance integron cassette, and the pinned "
                "DefenseFinder article registry maps the gcu76 source key "
                "to the same Science article. The pinned HMM inventory and "
                "rules table have no exact gcu76 or Brc76 row, so the "
                "first-pass record leaves native-host breadth, profile "
                "boundaries, exact phage target breadth, and direct "
                "molecular output unresolved."
            ),
            "evidence": [
                brc76_low_moi_profile_evidence(),
                brc76_high_moi_profile_evidence(),
                bric_panel_evidence(),
                brc76_attc_evidence(),
                {
                    "reference": KIEFFER,
                    "snippet": BRC76_KPNEUMONIAE_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc76 in the heterologous "
                        "Klebsiella pneumoniae KP5 BRiC panel."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder HMM inventory found no exact gcu76, "
                        "brc76, or Brc76 row."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder rules table found no exact gcu76, "
                        "brc76, or Brc76 system row."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#brc76_integron_cassette_confers_phage_resistance"
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
            "Minted Brc76 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at BRiC integron-cassette level because the pinned "
            "DefenseFinder article registry names gcu76 but the pinned HMM "
            "inventory and rules table have no exact Brc76 row; the "
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
            "Reviewed Brc76 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcu76/Brc76 phage-resistance assays and a "
            "DefenseFinder gcu76 article row, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous Brc76 activity. No paid research was used."
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
