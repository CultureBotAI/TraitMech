#!/usr/bin/env python3
"""Add the Brc23 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc23_system.yaml"

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
TIMESTAMP = "2026-10-01T20:08:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T20:08:01Z"
IDENTIFIER = "traitmech:000524"
PROPOSAL = "proposals/metpo_traitmech_v401"

BRC23_PROFILE_SNIPPET = (
    "gcu23 had a broader defense profile, including high resistance levels "
    "against G4, MS2, F1, and T4"
)
BRC23_REDEFINED_SNIPPET = (
    "We therefore redefined both cassettes as BRiCs (brc22 and brc23)"
)
BRIC_ATTC_CAPTION_SNIPPET = (
    "Predicted secondary structures of attC sites in identified BRiCs"
)
BRC23_ATTC_SNIPPET = """brc113
brc217
brc76
brcWGS21
brc22
brc23"""
BRC23_ECOLI_CONSTRUCT_SNIPPET = "D279\npMBA PcW brc23\nE. coli IJ1862"
BRC23_KPNEUMONIAE_CONSTRUCT_SNIPPET = (
    "D284\npMBA PcW brc23\nK. pneumoniae\nKP5"
)


def bric_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRIC_ATTC_CAPTION_SNIPPET,
        "notes": (
            "Kieffer et al. identify BRiC bacteriophage-resistance integron "
            "cassettes and show their predicted attC secondary structures."
        ),
    }


def brc23_profile_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC23_PROFILE_SNIPPET,
        "notes": (
            "Kieffer et al. report that the former gcu23 cassette conferred "
            "a broader phage-defense profile with high G4, MS2, F1, and T4 "
            "resistance levels."
        ),
    }


def brc23_renaming_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC23_REDEFINED_SNIPPET,
        "notes": (
            "Kieffer et al. renamed gcu22 and gcu23 as Brc cassettes after "
            "phage-resistance testing."
        ),
    }


def brc23_attc_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRC23_ATTC_SNIPPET,
        "notes": (
            "Kieffer et al. include brc23 among identified BRiCs with "
            "predicted attC secondary structures."
        ),
    }


def brc23_ecoli_construct_evidence() -> dict[str, str]:
    return {
        "reference": SCIENCE_SUPPLEMENT,
        "snippet": BRC23_ECOLI_CONSTRUCT_SNIPPET,
        "notes": (
            "Kieffer et al.'s supplementary construct table lists pMBA PcW "
            "brc23 in E. coli IJ1862 under naturally occurring defense "
            "island constructs."
        ),
    }


def brc23_kpneumoniae_construct_evidence() -> dict[str, str]:
    return {
        "reference": SCIENCE_SUPPLEMENT,
        "snippet": BRC23_KPNEUMONIAE_CONSTRUCT_SNIPPET,
        "notes": (
            "Kieffer et al.'s supplementary construct table lists pMBA PcW "
            "brc23 in Klebsiella pneumoniae KP5 under naturally occurring "
            "defense island constructs."
        ),
    }


def defensefinder_article_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "article registry found no exact gcu23, brc23, or Brc23 row."
        ),
    }


def defensefinder_hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact gcu23, brc23, or Brc23 row."
        ),
    }


def defensefinder_rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact gcu23, brc23, or Brc23 system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc23 system",
    "definition": (
        "A phage defense system in which an organism possesses a gcu23/Brc23 "
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
            "synonym_text": "gcu23",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
        {
            "synonym_text": "brc23",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        brc23_profile_evidence(),
        brc23_renaming_evidence(),
        bric_attc_evidence(),
        brc23_attc_evidence(),
        brc23_ecoli_construct_evidence(),
        brc23_kpneumoniae_construct_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brc23_integron_cassette_confers_phage_resistance",
            "title": "Brc23 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a gcu23/Brc23 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc23 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc23 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, whether Brc22 "
                "and Brc23 are variants of one Tragantia family, or a "
                "DefenseFinder article/HMM/rules profile absent from the "
                "pinned snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc23_integron_cassette",
                    "label": "Brc23 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette curated here as "
                        "gcu23/Brc23."
                    ),
                },
                {
                    "node_id": "brc23_phage_resistance",
                    "label": "Brc23 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcu23/Brc23 integron cassette."
                    ),
                },
                {
                    "node_id": "brc23_system_trait",
                    "label": "Brc23 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc23 "
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
                    "subject": "brc23_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc23_phage_resistance",
                    "description": (
                        "The gcu23/Brc23 integron cassette contributes to "
                        "G4, MS2, F1, and T4 phage resistance during "
                        "phage-panel assays."
                    ),
                    "evidence": [
                        brc23_profile_evidence(),
                    ],
                },
                {
                    "subject": "brc23_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc23_system_trait",
                    "description": (
                        "Brc23-linked phage resistance realizes the Brc23 "
                        "system possession trait."
                    ),
                    "evidence": [
                        brc23_profile_evidence(),
                        brc23_renaming_evidence(),
                    ],
                },
                {
                    "subject": "brc23_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc23 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_attc_evidence(),
                        brc23_attc_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc23-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc23 native host breadth, exact sensitive-phage "
                "breadth, molecular output, Tragantia-family boundaries, "
                "and DefenseFinder article/HMM/rules coverage before "
                "minting narrower Brc23 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify brc23 as a bacteriophage-resistance "
                "integron cassette. The pinned DefenseFinder article "
                "registry, HMM inventory, and rules table have no exact "
                "gcu23 or Brc23 row, so the first-pass record leaves native-"
                "host breadth, profile boundaries, exact phage target "
                "breadth, direct molecular output, and Brc22/Brc23 "
                "Tragantia-family scope unresolved."
            ),
            "evidence": [
                brc23_profile_evidence(),
                brc23_renaming_evidence(),
                bric_attc_evidence(),
                brc23_attc_evidence(),
                brc23_ecoli_construct_evidence(),
                brc23_kpneumoniae_construct_evidence(),
                defensefinder_article_absence_evidence(),
                defensefinder_hmm_absence_evidence(),
                defensefinder_rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#brc23_integron_cassette_confers_phage_resistance"
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
            "Minted Brc23 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review ruled out same-scope live TraitMech, METPO, "
            "history, and prior proposal collisions after reviewing exact "
            "Brc23/brc23/gcu23 hits; kept the graph at BRiC integron-cassette "
            "level because the pinned DefenseFinder article registry, HMM "
            "inventory, and rules table have no exact Brc23 row; the "
            "replacement placeholder is reserved in "
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
            "Reviewed Brc23 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcu23/Brc23 phage-resistance assays but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous Brc23 activity. No paid "
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
