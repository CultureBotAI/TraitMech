#!/usr/bin/env python3
"""Add the Brc113 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc113_system.yaml"

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
TIMESTAMP = "2026-10-01T18:33:44Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T18:33:45Z"
IDENTIFIER = "traitmech:000522"
PROPOSAL = "proposals/metpo_traitmech_v399"

BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
BRC113_LOW_MOI_PROFILE_SNIPPET = "brc113 L 95.1 70.8"
BRC113_ATTC_SNIPPET = """brc113
brc217
brc76
brcWGS21
brc22
brc23"""
BRC113_ECOLI_CONSTRUCT_SNIPPET = "C936\npMBA brc113\nE. coli IJ1862"
BRC113_KPNEUMONIAE_CONSTRUCT_SNIPPET = (
    "C942\npMBA brc113\nK. pneumoniae\n\nKP5"
)
BRC113_PSEUDOMONAS_CONSTRUCT_SNIPPET = (
    "C974\npBTZ PcW brc113\nP. aeruginosa\nPAO1"
)


def bric_panel_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRIC_PROFILE_SNIPPET,
        "notes": (
            "Kieffer et al. classify positive integron cassettes as BRiCs and "
            "compare their defense profiles across a phage panel."
        ),
    }


def brc113_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC113_ATTC_SNIPPET,
        "notes": (
            "Kieffer et al. include brc113 among identified BRiCs with "
            "predicted attC secondary structures."
        ),
    }


def brc113_low_moi_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC113_LOW_MOI_PROFILE_SNIPPET,
        "notes": (
            "Manual transcription of the Supplementary Fig. S2 Brc113 "
            "low-MOI E. coli IJ1862 heatmap row; the visible cells show "
            "reduced inhibition, including 95.1% for MS2 and 70.8% for F13."
        ),
    }


def defensefinder_article_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "article registry found no exact gcu113, brc113, or Brc113 row."
        ),
    }


def defensefinder_hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact gcu113, brc113, or Brc113 row."
        ),
    }


def defensefinder_rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact gcu113, brc113, or Brc113 system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc113 system",
    "definition": (
        "A phage defense system in which an organism possesses a gcu113/Brc113 "
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
            "synonym_text": "gcu113",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
        {
            "synonym_text": "brc113",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brc113_low_moi_profile_evidence(),
        bric_panel_evidence(),
        brc113_attc_evidence(),
        {
            "reference": SCIENCE_SUPPLEMENT,
            "snippet": BRC113_ECOLI_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists pMBA "
                "brc113 in E. coli IJ1862 for high/low-MOI phage-panel "
                "testing."
            ),
        },
        {
            "reference": SCIENCE_SUPPLEMENT,
            "snippet": BRC113_KPNEUMONIAE_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pMBA brc113 plasmid introduced into Klebsiella pneumoniae "
                "KP5."
            ),
        },
        {
            "reference": SCIENCE_SUPPLEMENT,
            "snippet": BRC113_PSEUDOMONAS_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pBTZ PcW brc113 plasmid introduced into Pseudomonas "
                "aeruginosa PAO1."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "brc113_integron_cassette_confers_phage_resistance",
            "title": "Brc113 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a gcu113/Brc113 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc113 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc113 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, or a "
                "DefenseFinder article/HMM/rules profile absent from the "
                "pinned snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc113_integron_cassette",
                    "label": "Brc113 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette curated here as "
                        "gcu113/Brc113."
                    ),
                },
                {
                    "node_id": "brc113_phage_resistance",
                    "label": "Brc113 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcu113/Brc113 integron cassette."
                    ),
                },
                {
                    "node_id": "brc113_system_trait",
                    "label": "Brc113 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc113 "
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
                    "subject": "brc113_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc113_phage_resistance",
                    "description": (
                        "The gcu113/Brc113 integron cassette contributes to "
                        "phage resistance during phage-panel assays."
                    ),
                    "evidence": [
                        brc113_low_moi_profile_evidence(),
                    ],
                },
                {
                    "subject": "brc113_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc113_system_trait",
                    "description": (
                        "Brc113-linked phage resistance realizes the "
                        "Brc113 system possession trait."
                    ),
                    "evidence": [
                        brc113_low_moi_profile_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brc113_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc113 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        brc113_attc_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc113-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc113 native host breadth, exact sensitive-phage "
                "breadth, molecular output, and DefenseFinder article/HMM/"
                "rules coverage before minting narrower Brc113 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brc113 as a "
                "bacteriophage-resistance integron cassette. The pinned "
                "DefenseFinder article registry, HMM inventory, and rules "
                "table have no exact gcu113 or Brc113 row, so the first-pass "
                "record leaves native-host breadth, profile boundaries, exact "
                "phage target breadth, and direct molecular output "
                "unresolved."
            ),
            "evidence": [
                brc113_low_moi_profile_evidence(),
                bric_panel_evidence(),
                brc113_attc_evidence(),
                {
                    "reference": SCIENCE_SUPPLEMENT,
                    "snippet": BRC113_KPNEUMONIAE_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc113 in the heterologous "
                        "Klebsiella pneumoniae KP5 BRiC panel."
                    ),
                },
                {
                    "reference": SCIENCE_SUPPLEMENT,
                    "snippet": BRC113_PSEUDOMONAS_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc113 in the heterologous "
                        "Pseudomonas aeruginosa PAO1 BRiC panel."
                    ),
                },
                defensefinder_article_absence_evidence(),
                defensefinder_hmm_absence_evidence(),
                defensefinder_rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#brc113_integron_cassette_confers_phage_resistance"
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
            "Minted Brc113 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at BRiC "
            "integron-cassette level because the pinned DefenseFinder "
            "article registry, HMM inventory, and rules table have no exact "
            "Brc113 row; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Brc113 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcu113/Brc113 phage-resistance assays but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous Brc113 activity. No paid "
            "research was used."
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
