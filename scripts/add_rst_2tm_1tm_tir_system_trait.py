#!/usr/bin/env python3
"""Add the Rst_2TM_1TM_TIR system genomics trait."""

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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "rst_2tm_1tm_tir_system.yaml"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/"
    "ee7647d8/content/3.defense-systems/rst_2tm_1tm_tir.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T02:40:20Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T02:40:21Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000400"
PROPOSAL = "proposals/metpo_traitmech_v277"
SLUG = "rst_2tm_1tm_tir"

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"

WIKI_DESCRIPTION_SNIPPET = (
    "The Rst_2TM_1TM_TIR system is carried by the P2-like phage AC1 "
    "and protects *Escherichia coli* C against lambda, LF82_P8 and P2 "
    "phages. This system is composed of three proteins, Rst_TIR_tm, "
    "which contains a TIR (Toll/interleukin-1 receptor) domain, "
    "Rst_1TM_TIR, which contains a transmembrane helix (TM) and "
    "Rst_2TM_TIR, that contains two TMs "
    ":ref{doi=10.1016/j.chom.2022.02.018}."
)
ROUSSET_VALIDATED_DEFENSES_SNIPPET = (
    "Phage resistance heatmaps of the validated defense systems show the "
    "median fold resistance of three independent replicates against a panel "
    "of eight phages"
)
WIKI_HYPOTHESIS_SNIPPET = (
    "Rousset et al. suggested that the TIR-containing protein could "
    "generate a nucleotide messenger that in turn could activate the "
    "associated transmembrane proteins."
)
WIKI_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_STRUCTURE_SNIPPET = (
    "The Rst_2TM_1TM_TIR is composed of 3 proteins: Rst_2TM_TIR, "
    "Rst_TIR_tm and Rst_1TM_TIR."
)
WIKI_REFSEQ_SNIPPET = (
    "The Rst_2TM_1TM_TIR system in *Escherichia coli* "
    "(GCF_004006575.1, NZ_CP034787) is composed of 3 proteins "
    "Rst_TIR_tm (WP_023140578.1) Rst_1TM_TIR (WP_001534953.1) "
    "Rst_2TM_TIR (WP_023140577.1)"
)
WIKI_VALIDATION_SNIPPET = (
    "Rousset_2022[<a href='https://doi.org/10.1016/"
    "j.chom.2022.02.018'>Rousset et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli C\n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_001534952.1'>"
    "WP_001534952.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_001534953.1'>WP_001534953.1</a>, "
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_001534955.1'>"
    "WP_001534955.1</a>] --> Expressed_0[Escherichia coli C]\n"
    "    Expressed_0[Escherichia coli C] ----> Lambda & LF82_P8 & P2 "
    "& SIAC10 & SID07 & DC1 & AC1"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        Lambda\n"
    "        LF82_P8\n"
    "        P2\n"
    "        SIAC10\n"
    "        SID07\n"
    "        DC1\n"
    "        AC1"
)
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_2TM_1TM_TIR | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_2TM_1TM_TIR\tRst_2TM_1TM_TIR\t3\t3\t"
    "Rst_2TM_1TM_TIR__Rst_1TM_TIR, "
    "Rst_2TM_1TM_TIR__Rst_2TM_TIR, "
    "Rst_2TM_1TM_TIR__Rst_TIR_tm\t\t\t"
)
HMM_PROFILES = (
    "Rst_2TM_1TM_TIR__Rst_1TM_TIR",
    "Rst_2TM_1TM_TIR__Rst_2TM_TIR",
    "Rst_2TM_1TM_TIR__Rst_TIR_tm",
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {profile:<49}| {'Rst_2TM_1TM_TIR':<23}| "
    f"{'Custom':<24}| {'20':<7}|"
    for profile in HMM_PROFILES
)


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names Rst_2TM_1TM_TIR "
            "as a three-protein system and links the AC1 locus to lambda, "
            "LF82_P8, and P2 protection in Escherichia coli C."
        ),
    }


def rousset_validated_defenses_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_VALIDATED_DEFENSES_SNIPPET,
        "notes": (
            "The Figure 5 legend frames the cloned Rst_2TM_1TM_TIR hit as "
            "one of the validated defense systems in a replicated "
            "phage-resistance heatmap."
        ),
    }


def wiki_hypothesis_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_HYPOTHESIS_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page records the unresolved "
            "Rousset et al. hypothesis that the TIR-containing protein "
            "could produce a nucleotide messenger that activates the "
            "transmembrane proteins."
        ),
    }


def wiki_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page leaves the "
            "Rst_2TM_1TM_TIR molecular mechanism unresolved."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes Rst_2TM_1TM_TIR "
            "as a three-component Rst_2TM_TIR/Rst_TIR_tm/Rst_1TM_TIR "
            "system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted three-protein "
            "Rst_2TM_1TM_TIR locus in RefSeq assembly GCF_004006575.1 on "
            "NZ_CP034787."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Rousset et al. to an Escherichia coli C source locus "
            "expressed in Escherichia coli C against seven phages."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            "lambda, LF82_P8, P2, SIAC10, SID07, DC1, and AC1 in the "
            "Rst_2TM_1TM_TIR protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Rst_2TM_1TM_TIR system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_2TM_1TM_TIR as a "
            "three-profile system requiring "
            "Rst_2TM_1TM_TIR__Rst_1TM_TIR, "
            "Rst_2TM_1TM_TIR__Rst_2TM_TIR, and "
            "Rst_2TM_1TM_TIR__Rst_TIR_tm."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records the Rst_1TM_TIR, "
            "Rst_2TM_TIR, and Rst_TIR_tm profiles under Rst_2TM_1TM_TIR."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_2TM_1TM_TIR system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "three-protein Rst_2TM_1TM_TIR locus represented by DefenseFinder "
        "as a three-profile model requiring "
        "Rst_2TM_1TM_TIR__Rst_1TM_TIR, "
        "Rst_2TM_1TM_TIR__Rst_2TM_TIR, and "
        "Rst_2TM_1TM_TIR__Rst_TIR_tm and experimentally linked to "
        "multi-phage protection when expressed in Escherichia coli C."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_2TM_1TM_TIR",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_PROFILES
        ],
    ],
    "evidence": [
        rousset_validated_defenses_evidence(),
        wiki_description_evidence(),
        wiki_hypothesis_evidence(),
        wiki_mechanism_evidence(),
        wiki_structure_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_2tm_1tm_tir_locus_restricts_phages",
            "title": "Rst_2TM_1TM_TIR loci restrict phages",
            "description": (
                "Conservative system-level sketch linking the named "
                "Rst_2TM_1TM_TIR three-gene locus model to multi-phage "
                "resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_2TM_1TM_TIR as a named "
                "DefenseFinder three-profile phage-defense system while "
                "leaving native host breadth, accession-level component "
                "grounding, the putative nucleotide messenger, and the "
                "mechanism of phage restriction unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_2tm_1tm_tir_locus",
                    "label": "Rst_2TM_1TM_TIR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene Rst_TIR_tm/Rst_1TM_TIR/"
                        "Rst_2TM_TIR phage-defense locus represented by "
                        "the custom DefenseFinder Rst_2TM_1TM_TIR "
                        "profiles."
                    ),
                },
                {
                    "node_id": "multi_phage_resistance",
                    "label": "multi-phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Resistance against multiple phages in a host "
                        "expressing an Rst_2TM_1TM_TIR locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_2TM_1TM_TIR system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded "
                        "Rst_2TM_1TM_TIR phage-defense system."
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
                    "subject": "rst_2tm_1tm_tir_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "multi_phage_resistance",
                    "description": (
                        "The pinned DefenseFinder wiki links AC1 "
                        "Rst_2TM_1TM_TIR to protection against multiple "
                        "phages, and DefenseFinder models "
                        "Rst_2TM_1TM_TIR as a three-profile system."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "multi_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Rst_2TM_1TM_TIR-linked multi-phage resistance "
                        "realizes the Rst_2TM_1TM_TIR system trait."
                    ),
                    "evidence": [
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst_2TM_1TM_TIR system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        rousset_validated_defenses_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-2tm-1tm-tir-mechanism-gap",
            "prompt": (
                "Resolve Rst_2TM_1TM_TIR native host breadth, "
                "accession-level components, the proposed "
                "TIR-derived nucleotide messenger, and the downstream "
                "transmembrane activation mechanism before minting "
                "narrower Rst_2TM_1TM_TIR mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The pinned DefenseFinder wiki supports a "
                "three-component AC1 Rst_2TM_1TM_TIR system that protects "
                "Escherichia coli C against multiple phages, and "
                "DefenseFinder represents Rst_2TM_1TM_TIR as a required "
                "three-profile model. Rousset et al. proposed that the "
                "TIR-containing protein could generate a nucleotide "
                "messenger to activate associated transmembrane proteins, "
                "but the wiki still records the molecular mechanism as "
                "unknown."
            ),
            "evidence": [
                wiki_hypothesis_evidence(),
                wiki_mechanism_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#rst_2tm_1tm_tir_locus_restricts_phages"
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Rst_2TM_1TM_TIR system as a stable-URL-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Rst_2TM_1TM_TIR during canonical-example issue "
            "444 enforcement and left canonical_examples empty because "
            "the sources support a cloned P2-like-phage AC1 locus "
            "assayed in Escherichia coli C and a DefenseFinder RefSeq "
            "model example, but not a direct native microbial host "
            "exemplar with experimental Rst_2TM_1TM_TIR activity. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
