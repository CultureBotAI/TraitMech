#!/usr/bin/env python3
"""Add the PD-T4-7 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t4_7_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t4-7.md"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-26T19:13:36Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T19:13:37Z"
REVIEW_FIX_TIMESTAMP = "2026-09-26T19:42:30Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000392"
PROPOSAL = "proposals/metpo_traitmech_v269"
SLUG = "pd_t4_7"

PHAGE_LIST = "T2, T4, and T6"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_COMPOSITION_SNIPPET = "The PD-T4-7 is composed of 1 protein: PD-T4-7."
WIKI_ABORTIVE_INFECTION_SNIPPET = (
    "Vassalo et al. :ref{doi=10.1038/s41564-022-01219-4} state that "
    "PD-T4-7 functions through an abortive infection mechanism."
)
THALASSOSPIRA_EXAMPLE_SNIPPET = (
    "The PD-T4-7 system in *Thalassospira sp. B30-1* "
    "(GCF_015767575.1, NZ_CP065232) is composed of 1 protein: "
    "PD-T4-7 (WP_139190007.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RRN43039.1'>"
    "RRN43039.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T2 & T4 & T6"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        T2\n"
    "        T4\n"
    "        T6"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T4-7 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the landscape "
    "of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = "PD-T4-7\tPD-T4-7\t1\t1\tPD-T4-7__PD-T4-7\t\t\t"
PROFILE = "PD-T4-7__PD-T4-7"
HMM_ROW = (
    "| PD-T4-7__PD-T4-7                                 | "
    "PD-T4-7__PD-T4-7                                 | "
    "PD-T4-7                | Custom                  | 80     |"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T4-7 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": "The DefenseFinder wiki names PD-T4-7 as a single-protein system.",
    }


def wiki_abortive_infection_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_ABORTIVE_INFECTION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki reports an abortive-infection mechanism "
            "assignment for PD-T4-7 while leaving the direct substrate and "
            "effector logic unresolved."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": THALASSOSPIRA_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted PD-T4-7 locus "
            "in RefSeq assembly GCF_015767575.1 on NZ_CP065232."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T4-7 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T4-7 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-T4-7 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-T4-7 as a "
            f"single-profile system requiring {PROFILE}."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            f"The DefenseFinder HMM inventory records {PROFILE} under the "
            "PD-T4-7 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T4-7 system",
    "definition": (
        "An abortive infection system in which an organism possesses a PD-T4-7 "
        f"locus represented by DefenseFinder as a single-profile model, {PROFILE}, "
        f"and experimentally linked to {PHAGE_LIST} protection when expressed "
        "in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "PD-T4-7",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        vassallo_screen_evidence(),
        wiki_composition_evidence(),
        wiki_abortive_infection_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t4_7_locus_restricts_t2_t4_and_t6",
            "title": f"PD-T4-7 loci restrict {PHAGE_LIST}",
            "description": (
                "Conservative system-level sketch linking possession of a "
                f"PD-T4-7 locus to protection against {PHAGE_LIST}."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T4-7 as a named DefenseFinder "
                "abortive-infection system while leaving natural host breadth, "
                "the direct phage trigger, and the direct effector logic "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t4_7_locus",
                    "label": "PD-T4-7 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the PD-T4-7 "
                        "DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "pd_t4_7_listed_phage_protection",
                    "label": f"{PHAGE_LIST} protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": f"Protection against {PHAGE_LIST} by PD-T4-7.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T4-7 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T4-7 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "pd_t4_7_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t4_7_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T4-7 locus from "
                        "Vassallo et al. to protection against "
                        f"{PHAGE_LIST}, and DefenseFinder models PD-T4-7 "
                        "through one mandatory profile."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "pd_t4_7_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        f"Protection against {PHAGE_LIST} realizes the "
                        "PD-T4-7 system trait."
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
                    "object": "abortive_infection_system",
                    "description": (
                        "PD-T4-7 system possession is an abortive-infection-system "
                        "trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        wiki_abortive_infection_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-t4-7-mechanism-gap",
            "prompt": (
                "Resolve PD-T4-7 natural host breadth, direct phage trigger, "
                "and direct abortive-infection effector logic before "
                "minting narrower PD-T4-7 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T4-7 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to protection "
                f"against {PHAGE_LIST}, and DefenseFinder represents the "
                "system with one mandatory profile and an abortive-infection "
                "mechanism assignment. Natural host breadth, the direct phage "
                "trigger, and direct effector logic remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_composition_evidence(),
                wiki_abortive_infection_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#pd_t4_7_locus_restricts_t2_t4_and_t6"],
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
            "Minted PD-T4-7 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under abortive infection system after an "
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
            "Reviewed PD-T4-7 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder system model, "
            "and a RefSeq Thalassospira example, but not a direct native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous PD-T4-7 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_SCOPE_NOTE_REVIEW",
        changes=(
            "Addressed PR #1292 review issue #1293 by reparenting PD-T4-7 "
            "under abortive infection system, updating the subclass graph "
            "node, and naming the DefenseFinder abortive-infection assignment "
            "while leaving natural host breadth, the direct phage trigger, "
            "and direct effector logic unresolved."
        ),
        llm_assisted=True,
        timestamp=REVIEW_FIX_TIMESTAMP,
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
