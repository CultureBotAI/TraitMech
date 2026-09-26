#!/usr/bin/env python3
"""Add the PD-Lambda-3 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_lambda_3_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-lambda-3.md"
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
TIMESTAMP = "2026-09-26T12:32:10Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T12:32:11Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000382"
PROPOSAL = "proposals/metpo_traitmech_v259"
SLUG = "pd_lambda_3"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-Lambda-3 is composed of 2 proteins: PD-Lambda-3_A and "
    "PD-Lambda-3_B."
)
ENTEROBACTER_EXAMPLE_SNIPPET = (
    "The PD-Lambda-3 system in *Enterobacter sp. CRENT-193* "
    "(GCF_002787395.1, NZ_CP024812) is composed of 2 proteins "
    "PD-Lambda-3_A (WP_001542736.1) "
    "PD-Lambda-3_B (WP_039268887.1)"
)
WIKI_UNKNOWN_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RCP74640.1'>"
    "RCP74640.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "RCP74641.1'>RCP74641.1</a>,\n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RCP74642.1'>"
    "RCP74642.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> LambdaVir"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        LambdaVir"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-Lambda-3 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the "
    "landscape of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = (
    "PD-Lambda-3\tPD-Lambda-3\t2\t2\t"
    "PD-Lambda-3__PD-Lambda-3_A, PD-Lambda-3__PD-Lambda-3_B\t\t\t"
)
HMM_THRESHOLDS = {
    "PD-Lambda-3__PD-Lambda-3_A": "20",
    "PD-Lambda-3__PD-Lambda-3_B": "75",
}
HMM_ROWS = {
    profile: (
        f"| {profile:<49}| {profile:<49}| {'PD-Lambda-3':<23}| "
        f"{'Custom':<24}| {threshold:<7}|"
    )
    for profile, threshold in HMM_THRESHOLDS.items()
}


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-Lambda-3 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-Lambda-3 as a two-protein "
            "system with PD-Lambda-3_A and PD-Lambda-3_B."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": ENTEROBACTER_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "PD-Lambda-3 locus in RefSeq assembly GCF_002787395.1 on "
            "NZ_CP024812."
        ),
    }


def wiki_unknown_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_UNKNOWN_MECHANISM_SNIPPET,
        "notes": "The DefenseFinder wiki records the PD-Lambda-3 mechanism as unknown.",
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-Lambda-3 source locus "
            "expressed in E. coli against LambdaVir."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            "LambdaVir in the PD-Lambda-3 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-Lambda-3 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-Lambda-3 as a "
            "two-profile system requiring PD-Lambda-3__PD-Lambda-3_A and "
            "PD-Lambda-3__PD-Lambda-3_B."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under the "
            "PD-Lambda-3 system namespace."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-Lambda-3 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "PD-Lambda-3 locus represented by DefenseFinder as a two-profile "
        "model, PD-Lambda-3__PD-Lambda-3_A and "
        "PD-Lambda-3__PD-Lambda-3_B, and experimentally linked to "
        "LambdaVir protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-Lambda-3",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
        ],
    ],
    "evidence": [
        vassallo_screen_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_unknown_mechanism_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_lambda_3_locus_restricts_lambda_vir",
            "title": "PD-Lambda-3 loci restrict LambdaVir",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-Lambda-3 locus to protection against LambdaVir."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-Lambda-3 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, the effector mechanism, the "
                "third protein in the experimental source locus, and exact "
                "PD-Lambda-3 profile-to-protein correspondence unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_lambda_3_locus",
                    "label": "PD-Lambda-3 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the "
                        "PD-Lambda-3 DefenseFinder profiles."
                    ),
                },
                {
                    "node_id": "pd_lambda_3_listed_phage_protection",
                    "label": "LambdaVir protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Protection against LambdaVir by PD-Lambda-3.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-Lambda-3 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-Lambda-3 "
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
                    "subject": "pd_lambda_3_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_lambda_3_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-Lambda-3 locus "
                        "from Vassallo et al. to protection against "
                        "LambdaVir, and DefenseFinder models PD-Lambda-3 "
                        "through two mandatory profiles."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "pd_lambda_3_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against LambdaVir realizes the "
                        "PD-Lambda-3 system trait."
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
                        "PD-Lambda-3 system possession is a "
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
            "discussion_id": "pd-lambda-3-mechanism-gap",
            "prompt": (
                "Resolve PD-Lambda-3 natural host breadth, direct phage "
                "trigger, effector mechanism, the third protein in the "
                "experimental source locus, and exact profile-to-protein "
                "correspondence before minting narrower PD-Lambda-3 "
                "mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-Lambda-3 as one of the "
                "conserved systems from an E. coli pangenome "
                "phage-defense selection, the DefenseFinder wiki maps the "
                "source locus to protection against LambdaVir, and "
                "DefenseFinder represents the system with A and B profiles. "
                "Natural host breadth, the direct phage trigger, effector "
                "logic, the third protein in the experimental source locus, "
                "and exact profile-to-protein correspondence remain "
                "unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_composition_evidence(),
                wiki_unknown_mechanism_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                *all_hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#pd_lambda_3_locus_restricts_lambda_vir"],
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
            "Minted PD-Lambda-3 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-Lambda-3 system canonical_examples and left them "
            "empty because the current sources support an E. coli "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Enterobacter sp. example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified endogenous PD-Lambda-3 activity. No paid research was "
            "used."
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
