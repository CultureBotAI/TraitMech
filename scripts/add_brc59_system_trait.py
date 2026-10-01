#!/usr/bin/env python3
"""Add the Brc59 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc59_system.yaml"

KIEFFER = "DOI:10.1126/science.ads0915"
SCIENCE_SUPPLEMENT = (
    "https://www.science.org/doi/suppl/10.1126/science.ads0915/"
    "suppl_file/science.ads0915_sm.pdf"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T20:28:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T20:28:01Z"
IDENTIFIER = "traitmech:000525"
PROPOSAL = "proposals/metpo_traitmech_v402"

BRC_ATT_C_PANEL_SNIPPET = "brc59\nbrc128\nbrc135\nbrc142\nbrc167.2\nbrc167"
BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
BRC59_LOW_MOI_PROFILE_SNIPPET = "brc59 L 44.7 49.6 87.3 98.6 7.6"
BRC59_HIGH_MOI_PROFILE_SNIPPET = "brc59 H 12.8 75.8 80.3 60.9"
BRC59_ECOLI_CONSTRUCT_SNIPPET = "C800\npMBA brc59\nE. coli IJ1862"
BRC59_KPNEUMONIAE_CONSTRUCT_SNIPPET = (
    "C810\npMBA brc59\nK. pneumoniae\n\nKP5"
)


def brc_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC_ATT_C_PANEL_SNIPPET,
        "notes": (
            "Kieffer et al. include brc59 among identified BRiCs with "
            "predicted attC secondary structures."
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


def brc59_low_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC59_LOW_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc59 "
            "low-MOI E. coli IJ1862 heatmap row; the visible cells show "
            "reduced inhibition, including 44.7% for MS2, 49.6% for T4, "
            "87.3% for F1, 98.6% for T7, and 7.6% for F13."
        ),
    }


def brc59_high_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC59_HIGH_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc59 "
            "high-MOI E. coli IJ1862 heatmap row; the visible cells show "
            "reduced inhibition, including 12.8% for MS2, 75.8% for F1, "
            "80.3% for HK544, and 60.9% for F13."
        ),
    }


def brc59_ecoli_construct_evidence() -> dict[str, str]:
    return {
        "reference": SCIENCE_SUPPLEMENT,
        "snippet": BRC59_ECOLI_CONSTRUCT_SNIPPET,
        "notes": (
            "Kieffer et al.'s supplementary construct table lists pMBA "
            "brc59 in E. coli IJ1862 for high/low-MOI phage-panel testing."
        ),
    }


def brc59_kpneumoniae_construct_evidence() -> dict[str, str]:
    return {
        "reference": SCIENCE_SUPPLEMENT,
        "snippet": BRC59_KPNEUMONIAE_CONSTRUCT_SNIPPET,
        "notes": (
            "Kieffer et al.'s supplementary construct table lists the pMBA "
            "brc59 plasmid introduced into Klebsiella pneumoniae KP5."
        ),
    }


def defensefinder_article_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "article registry found no exact gcu59, brc59, or Brc59 row."
        ),
    }


def defensefinder_hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact gcu59, brc59, or Brc59 row."
        ),
    }


def defensefinder_rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact gcu59, brc59, or Brc59 system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc59 system",
    "definition": (
        "A phage defense system in which an organism possesses a Brc59 "
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
            "synonym_text": "brc59",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brc59_low_moi_profile_evidence(),
        brc59_high_moi_profile_evidence(),
        bric_panel_evidence(),
        brc_attc_evidence(),
        brc59_ecoli_construct_evidence(),
        brc59_kpneumoniae_construct_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brc59_integron_cassette_confers_phage_resistance",
            "title": "Brc59 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a Brc59 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc59 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc59 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, a normalized "
                "gcu59 source key, or a DefenseFinder article/HMM/rules "
                "profile absent from the pinned snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc59_integron_cassette",
                    "label": "Brc59 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette curated here as "
                        "Brc59."
                    ),
                },
                {
                    "node_id": "brc59_phage_resistance",
                    "label": "Brc59 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "Brc59 integron cassette."
                    ),
                },
                {
                    "node_id": "brc59_system_trait",
                    "label": "Brc59 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc59 "
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
                    "subject": "brc59_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc59_phage_resistance",
                    "description": (
                        "The Brc59 integron cassette contributes to phage "
                        "resistance during phage-panel assays."
                    ),
                    "evidence": [
                        brc59_low_moi_profile_evidence(),
                        brc59_high_moi_profile_evidence(),
                    ],
                },
                {
                    "subject": "brc59_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc59_system_trait",
                    "description": (
                        "Brc59-linked phage resistance realizes the Brc59 "
                        "system possession trait."
                    ),
                    "evidence": [
                        brc59_low_moi_profile_evidence(),
                        brc59_high_moi_profile_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brc59_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc59 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        brc_attc_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc59-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc59 native host breadth, exact sensitive-phage "
                "breadth, molecular output, normalized source-key naming, "
                "and DefenseFinder article/HMM/rules coverage before "
                "minting narrower Brc59 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brc59 as a bacteriophage-resistance "
                "integron cassette. The pinned DefenseFinder article "
                "registry, HMM inventory, and rules table have no exact "
                "gcu59 or Brc59 row, so the first-pass record leaves native-"
                "host breadth, profile boundaries, exact phage target "
                "breadth, direct molecular output, and normalized gcu59 "
                "source-key status unresolved."
            ),
            "evidence": [
                brc59_low_moi_profile_evidence(),
                brc59_high_moi_profile_evidence(),
                bric_panel_evidence(),
                brc_attc_evidence(),
                brc59_ecoli_construct_evidence(),
                brc59_kpneumoniae_construct_evidence(),
                defensefinder_article_absence_evidence(),
                defensefinder_hmm_absence_evidence(),
                defensefinder_rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#brc59_integron_cassette_confers_phage_resistance"
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
            "Minted Brc59 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review ruled out same-scope live TraitMech, METPO, history, and "
            "prior proposal collisions after reviewing exact "
            "Brc59/brc59/gcu59 hits; kept the graph at BRiC integron-cassette "
            "level because the pinned DefenseFinder article registry, HMM "
            "inventory, and rules table have no exact Brc59 row; the "
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
            "Reviewed Brc59 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous brc59 phage-resistance assays but not a direct "
            "named native microbial isolate exemplar with experimentally "
            "verified endogenous Brc59 activity. No paid research was used."
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
