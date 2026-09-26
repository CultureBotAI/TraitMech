#!/usr/bin/env python3
"""Add the PD-Lambda-6 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_lambda_6_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-lambda-6.md"
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
TIMESTAMP = "2026-09-26T13:07:26Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T13:07:27Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000383"
PROPOSAL = "proposals/metpo_traitmech_v260"
SLUG = "pd_lambda_6"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-Lambda-6 is composed of 1 protein: PD-Lambda-6."
)
ENTEROBACTER_EXAMPLE_SNIPPET = (
    "The PD-Lambda-6 system in *Enterobacter asburiae* "
    "(GCF_013782005.1, NZ_CP056126) is composed of 1 protein: "
    "PD-Lambda-6 (WP_181599444.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RRK48647.1'>"
    "RRK48647.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> LambdaVir & T5"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        LambdaVir\n"
    "        T5"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-Lambda-6 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the "
    "landscape of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = (
    "PD-Lambda-6\tPD-Lambda-6\t1\t1\tPD-Lambda-6__PD-Lambda-6\t\t\t"
)
PROFILE = "PD-Lambda-6__PD-Lambda-6"
HMM_ROW = (
    f"| {PROFILE:<49}| {PROFILE:<49}| {'PD-Lambda-6':<23}| "
    f"{'Custom':<24}| {'20':<7}|"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-Lambda-6 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-Lambda-6 as a single-protein "
            "system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": ENTEROBACTER_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted one-protein "
            "PD-Lambda-6 locus in RefSeq assembly GCF_013782005.1 on "
            "NZ_CP056126."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-Lambda-6 source locus "
            "expressed in E. coli against LambdaVir and T5."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            "LambdaVir and T5 in the PD-Lambda-6 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-Lambda-6 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-Lambda-6 as a "
            "single-profile system requiring PD-Lambda-6__PD-Lambda-6."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records "
            "PD-Lambda-6__PD-Lambda-6 under the PD-Lambda-6 system "
            "namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-Lambda-6 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "PD-Lambda-6 locus represented by DefenseFinder as a single-profile "
        "model, PD-Lambda-6__PD-Lambda-6, and experimentally linked to "
        "LambdaVir and T5 protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-Lambda-6",
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
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_lambda_6_locus_restricts_lambda_vir_and_t5",
            "title": "PD-Lambda-6 loci restrict LambdaVir and T5",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-Lambda-6 locus to protection against LambdaVir and T5."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-Lambda-6 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, and the effector mechanism "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_lambda_6_locus",
                    "label": "PD-Lambda-6 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the "
                        "PD-Lambda-6 DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "pd_lambda_6_listed_phage_protection",
                    "label": "LambdaVir and T5 protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Protection against LambdaVir and T5 by PD-Lambda-6.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-Lambda-6 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-Lambda-6 "
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
                    "subject": "pd_lambda_6_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_lambda_6_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-Lambda-6 locus "
                        "from Vassallo et al. to protection against "
                        "LambdaVir and T5, and DefenseFinder models "
                        "PD-Lambda-6 through one mandatory profile."
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
                    "subject": "pd_lambda_6_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against LambdaVir and T5 realizes the "
                        "PD-Lambda-6 system trait."
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
                        "PD-Lambda-6 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-lambda-6-mechanism-gap",
            "prompt": (
                "Resolve PD-Lambda-6 natural host breadth, direct phage "
                "trigger, and effector mechanism before minting narrower "
                "PD-Lambda-6 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-Lambda-6 as one of the "
                "conserved systems from an E. coli pangenome "
                "phage-defense selection, the DefenseFinder wiki maps the "
                "source locus to protection against LambdaVir and T5, and "
                "DefenseFinder represents the system with one profile. "
                "Natural host breadth, the direct phage trigger, and "
                "effector logic remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_composition_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#pd_lambda_6_locus_restricts_lambda_vir_and_t5"
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
            "Minted PD-Lambda-6 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-Lambda-6 system canonical_examples and left them "
            "empty because the current sources support an E. coli "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Enterobacter asburiae example, but "
            "not a direct native microbial isolate exemplar with "
            "experimentally verified endogenous PD-Lambda-6 activity. No "
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
