#!/usr/bin/env python3
"""Add the PD-T4-10 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t4_10_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t4-10.md"
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
TIMESTAMP = "2026-09-26T20:56:41Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T20:56:42Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000394"
PROPOSAL = "proposals/metpo_traitmech_v271"
SLUG = "pd_t4_10"

PROFILE_A = "PD-T4-10__PD-T4-10_A"
PROFILE_B = "PD-T4-10__PD-T4-10_B"
PROFILE_PAIR = f"{PROFILE_A} and {PROFILE_B}"
PHAGE_LIST = "T2, T4, T6, T5, and SECphi27"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_DESCRIPTION_SNIPPET = (
    "The PD-T4-10 system is composed of 2 proteins: PD-T4-10_B and, "
    "PD-T4-10_A. These ORFs are overlapping and PD-T4-10_B is toxic while "
    "PD-T4-10_A neutralizes its toxicity, hinting at a toxin-antitoxin (TA) "
    "mechanism. It confers resitance to T2, T4, T6 and SECphi27 through an "
    "Abi defense mechanism :ref{doi=10.1038/s41564-022-01219-4}."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-T4-10 is composed of 2 proteins: PD-T4-10_A and PD-T4-10_B."
)
E_FERGUSONII_EXAMPLE_SNIPPET = (
    "The PD-T4-10 system in *Escherichia fergusonii* "
    "(GCF_019047545.1, NZ_CP077242) is composed of 2 proteins "
    "PD-T4-10_A (WP_032236482.1) PD-T4-10_B (WP_032236481.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RCO36089.1'>"
    "RCO36089.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "RCO36088.1'>RCO36088.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T2 & T4 & T6 & T5 & SECphi27"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        T2\n"
    "        T4\n"
    "        T6\n"
    "        T5\n"
    "        SECphi27"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T4-10 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the landscape "
    "of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = (
    "PD-T4-10\tPD-T4-10\t2\t2\t"
    "PD-T4-10__PD-T4-10_A, PD-T4-10__PD-T4-10_B\t\t\t"
)
HMM_ROWS = (
    "| PD-T4-10__PD-T4-10_A                             | "
    "PD-T4-10__PD-T4-10_A                             | "
    "PD-T4-10               | Custom                  | 20     |\n"
    "| PD-T4-10__PD-T4-10_B                             | "
    "PD-T4-10__PD-T4-10_B                             | "
    "PD-T4-10               | Custom                  | 20     |"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T4-10 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes PD-T4-10 as a two-protein "
            "Abi system whose overlapping ORFs include a toxic PD-T4-10_B "
            "and neutralizing PD-T4-10_A."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-T4-10_A and PD-T4-10_B as the "
            "two components of the PD-T4-10 system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": E_FERGUSONII_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted PD-T4-10 locus "
            "in RefSeq assembly GCF_019047545.1 on NZ_CP077242."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T4-10 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T4-10 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-T4-10 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-T4-10 as a two-profile "
            f"system requiring {PROFILE_PAIR}."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS,
        "notes": (
            f"The DefenseFinder HMM inventory records {PROFILE_A} and "
            f"{PROFILE_B} under the PD-T4-10 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T4-10 system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "PD-T4-10 locus represented by DefenseFinder as a two-profile "
        f"model, {PROFILE_PAIR}, and experimentally linked to {PHAGE_LIST} "
        "protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "PD-T4-10",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": PROFILE_A,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": PROFILE_B,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        vassallo_screen_evidence(),
        wiki_description_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t4_10_locus_restricts_t2_t4_t6_t5_and_secphi27",
            "title": f"PD-T4-10 loci restrict {PHAGE_LIST}",
            "description": (
                "Conservative system-level sketch linking possession of a "
                f"PD-T4-10 locus to protection against {PHAGE_LIST}."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T4-10 as a named DefenseFinder "
                "abortive-infection system while leaving natural host "
                "breadth, the direct phage trigger, the toxic PD-T4-10_B "
                "target, and the PD-T4-10_A neutralization logic unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t4_10_locus",
                    "label": "PD-T4-10 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-profile abortive-infection locus represented "
                        "by the DefenseFinder PD-T4-10_A and PD-T4-10_B "
                        "profiles."
                    ),
                },
                {
                    "node_id": "pd_t4_10_listed_phage_protection",
                    "label": f"{PHAGE_LIST} protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": f"Protection against {PHAGE_LIST} by PD-T4-10.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T4-10 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T4-10 "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "pd_t4_10_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t4_10_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T4-10 locus from "
                        "Vassallo et al. to protection against "
                        f"{PHAGE_LIST}, and DefenseFinder models PD-T4-10 "
                        "through two mandatory profiles."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "pd_t4_10_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        f"Protection against {PHAGE_LIST} realizes the "
                        "PD-T4-10 system trait."
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
                        "PD-T4-10 system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        wiki_description_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-t4-10-mechanism-gap",
            "prompt": (
                "Resolve PD-T4-10 natural host breadth, direct phage "
                "trigger, the toxic PD-T4-10_B target, and PD-T4-10_A "
                "neutralization logic before minting narrower PD-T4-10 "
                "mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T4-10 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to protection "
                f"against {PHAGE_LIST}, and DefenseFinder represents the "
                "system with two mandatory profiles and an abortive-infection "
                "mechanism assignment. Natural host breadth, the direct phage "
                "trigger, the toxic PD-T4-10_B target, and the PD-T4-10_A "
                "neutralization logic remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_description_evidence(),
                wiki_composition_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#pd_t4_10_locus_restricts_t2_t4_t6_t5_and_secphi27"
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
            "Minted PD-T4-10 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under abortive infection system after "
            "an ignored-and-hidden duplicate review found no exact live "
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
            "Reviewed PD-T4-10 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder two-profile "
            "system model, and a RefSeq Escherichia fergusonii example, but "
            "not a direct native microbial isolate exemplar with "
            "experimentally verified endogenous PD-T4-10 activity. No paid "
            "research was used."
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
