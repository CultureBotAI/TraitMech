#!/usr/bin/env python3
"""Add the Brc233 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc233_system.yaml"

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
TIMESTAMP = "2026-10-01T15:36:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T15:36:01Z"
IDENTIFIER = "traitmech:000518"
PROPOSAL = "proposals/metpo_traitmech_v395"

BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
BRC233_LOW_MOI_PROFILE_SNIPPET = "brc233 L 27.7 51.8 37.3 62.6 95.7 12.8"
BRC233_HIGH_MOI_PROFILE_SNIPPET = "brc233 H 34.0 52.2 89.4 39.4 98.2 41.3"
BRC233_ECOLI_CONSTRUCT_SNIPPET = "C807\npMBA brc233\nE. coli IJ1862"
BRC233_KPNEUMONIAE_CONSTRUCT_SNIPPET = "C817\npMBA brc233\nK. pneumoniae"
ARTICLE_ROW = (
    "| gcu233 | 10\\.1126/science\\.ads0915 | Mobile integrons "
    "encode phage defense systems | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the gcu233 source "
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


def brc233_low_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC233_LOW_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc233 low-MOI "
            "E. coli IJ1862 heatmap row; the row shows reduced inhibition, "
            "including 27.7% for MS2, 51.8% for G4, 37.3% for T4, 62.6% "
            "for F1, and 12.8% for F13."
        ),
    }


def brc233_high_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC233_HIGH_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc233 high-MOI "
            "E. coli IJ1862 heatmap row; the row shows reduced inhibition, "
            "including 34.0% for MS2, 52.2% for G4, 39.4% for F1, and "
            "41.3% for F13."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc233 system",
    "definition": (
        "A phage defense system in which an organism possesses a gcu233/Brc233 "
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
            "synonym_text": "gcu233",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "brc233",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brc233_low_moi_profile_evidence(),
        brc233_high_moi_profile_evidence(),
        bric_panel_evidence(),
        {
            "reference": KIEFFER,
            "snippet": BRC233_ECOLI_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists pMBA "
                "brc233 in E. coli IJ1862 for high/low-MOI phage-panel "
                "testing."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRC233_KPNEUMONIAE_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pMBA brc233 plasmid introduced into Klebsiella pneumoniae "
                "KP5."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brc233_integron_cassette_confers_phage_resistance",
            "title": "Brc233 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a gcu233/Brc233 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc233 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc233 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, or a "
                "DefenseFinder HMM/rules profile absent from the pinned "
                "snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc233_integron_cassette",
                    "label": "Brc233 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette named by the gcu233 "
                        "source key and curated as Brc233."
                    ),
                },
                {
                    "node_id": "brc233_phage_resistance",
                    "label": "Brc233 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcu233/Brc233 integron cassette."
                    ),
                },
                {
                    "node_id": "brc233_system_trait",
                    "label": "Brc233 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc233 "
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
                    "subject": "brc233_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc233_phage_resistance",
                    "description": (
                        "The gcu233/Brc233 integron cassette contributes to "
                        "phage resistance during phage-panel assays."
                    ),
                    "evidence": [
                        brc233_low_moi_profile_evidence(),
                        brc233_high_moi_profile_evidence(),
                    ],
                },
                {
                    "subject": "brc233_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc233_system_trait",
                    "description": (
                        "Brc233-linked phage resistance realizes the "
                        "Brc233 system possession trait."
                    ),
                    "evidence": [
                        brc233_low_moi_profile_evidence(),
                        brc233_high_moi_profile_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brc233_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc233 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc233-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc233 native host breadth, exact sensitive-phage "
                "breadth, molecular output, and DefenseFinder HMM/rules "
                "coverage before minting narrower Brc233 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brc233 as a "
                "bacteriophage-resistance integron cassette, and the pinned "
                "DefenseFinder article registry maps the gcu233 source key "
                "to the same Science article. The pinned HMM inventory and "
                "rules table have no exact gcu233 or Brc233 row, so the "
                "first-pass record leaves native-host breadth, profile "
                "boundaries, exact phage target breadth, and direct "
                "molecular output unresolved."
            ),
            "evidence": [
                brc233_low_moi_profile_evidence(),
                brc233_high_moi_profile_evidence(),
                bric_panel_evidence(),
                {
                    "reference": KIEFFER,
                    "snippet": BRC233_KPNEUMONIAE_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc233 in the heterologous "
                        "Klebsiella pneumoniae KP5 BRiC panel."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder HMM inventory found no exact gcu233, "
                        "brc233, or Brc233 row."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder rules table found no exact gcu233, "
                        "brc233, or Brc233 system row."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#brc233_integron_cassette_confers_phage_resistance"
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
            "Minted Brc233 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at BRiC integron-cassette level because the pinned "
            "DefenseFinder article registry names gcu233 but the pinned HMM "
            "inventory and rules table have no exact Brc233 row; the "
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
            "Reviewed Brc233 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcu233/Brc233 phage-resistance assays and a "
            "DefenseFinder gcu233 article row, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous Brc233 activity. No paid research was used."
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
