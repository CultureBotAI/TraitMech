#!/usr/bin/env python3
"""Add the PD-Lambda-1 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_lambda_1_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-lambda-1.md"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T07:17:46Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T07:17:47Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000404"
PROPOSAL = "proposals/metpo_traitmech_v281"
SLUG = "pd_lambda_1"
PROFILE = "PD-Lambda-1__PD-Lambda-1"
PHAGE_LIST = "LambdaVir"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_DESCRIPTION_SNIPPET = (
    "The PD-Lambda-1 system is composed of one protein, PD-Lambda-1, and "
    "confers resistance to LambdaVir :ref{doi=10.1038/s41564-022-01219-4}."
)
WIKI_MECHANISM_GAP_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-Lambda-1 is composed of 1 protein: PD-Lambda-1."
)
GEMMATA_EXAMPLE_SNIPPET = (
    "The PD-Lambda-1 system in *Gemmata massiliana* "
    "(GCF_901538265.1, NZ_LR593886) is composed of 1 protein: "
    "PD-Lambda-1 (WP_197909633.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RCP76574.1'>"
    "RCP76574.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> LambdaVir"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        LambdaVir"
)
RULES_SNIPPET = "PD-Lambda-1\tPD-Lambda-1\t1\t1\tPD-Lambda-1__PD-Lambda-1\t\t\t"
HMM_ROW = (
    "| PD-Lambda-1__PD-Lambda-1                         | "
    "PD-Lambda-1__PD-Lambda-1                         | "
    "PD-Lambda-1            | Custom                  | 200    |"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-Lambda-1 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes PD-Lambda-1 as a one-protein "
            "system that can confer LambdaVir resistance."
        ),
    }


def wiki_mechanism_gap_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_GAP_SNIPPET,
        "notes": (
            "The DefenseFinder wiki records the PD-Lambda-1 molecular "
            "mechanism as unresolved."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-Lambda-1 as a single-protein "
            "system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": GEMMATA_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted one-protein "
            "PD-Lambda-1 locus in RefSeq assembly GCF_901538265.1 on "
            "NZ_LR593886."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-Lambda-1 source locus "
            f"expressed in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-Lambda-1 protects-against subgraph."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-Lambda-1 as a "
            "single-profile system requiring PD-Lambda-1__PD-Lambda-1."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records "
            "PD-Lambda-1__PD-Lambda-1 under the PD-Lambda-1 system "
            "namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-Lambda-1 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "PD-Lambda-1 locus represented by DefenseFinder as a "
        "single-profile model, PD-Lambda-1__PD-Lambda-1, and "
        "experimentally linked to LambdaVir protection when expressed in "
        "E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-Lambda-1",
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
        wiki_description_evidence(),
        wiki_mechanism_gap_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_lambda_1_locus_restricts_lambda_vir",
            "title": "PD-Lambda-1 loci restrict LambdaVir",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-Lambda-1 locus to LambdaVir protection."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-Lambda-1 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, and the effector mechanism "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_lambda_1_locus",
                    "label": "PD-Lambda-1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the "
                        "PD-Lambda-1 DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "pd_lambda_1_listed_phage_protection",
                    "label": "LambdaVir protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Protection against LambdaVir by PD-Lambda-1.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-Lambda-1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-Lambda-1 "
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
                    "subject": "pd_lambda_1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_lambda_1_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-Lambda-1 locus "
                        "from Vassallo et al. to LambdaVir protection, and "
                        "DefenseFinder models PD-Lambda-1 through one "
                        "mandatory profile."
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
                    "subject": "pd_lambda_1_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against LambdaVir realizes the "
                        "PD-Lambda-1 system trait."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
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
                        "PD-Lambda-1 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        wiki_composition_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-lambda-1-mechanism-gap",
            "prompt": (
                "Resolve PD-Lambda-1 natural host breadth, direct phage "
                "trigger, and effector mechanism before minting narrower "
                "PD-Lambda-1 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-Lambda-1 as one of the "
                "conserved systems from an E. coli pangenome "
                "phage-defense selection, the DefenseFinder wiki maps the "
                "source locus to LambdaVir protection, and DefenseFinder "
                "represents the system with one profile. Natural host "
                "breadth, the direct phage trigger, and effector logic "
                "remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_description_evidence(),
                wiki_mechanism_gap_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#pd_lambda_1_locus_restricts_lambda_vir"
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
        {
            "discussion_id": "pd-lambda-1-defensefinder-article-registry-gap",
            "prompt": (
                "Recheck whether DefenseFinder adds a PD-Lambda-1 "
                "List_system_article.md row before using the article "
                "registry as direct PD-Lambda-1 model-to-paper evidence."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned DefenseFinder wiki, rules table, and HMM "
                "inventory all represent PD-Lambda-1, but the pinned "
                "List_system_article.md registry omits a PD-Lambda-1 row. "
                "The PD-Lambda-1 record therefore cites the pinned wiki plus "
                "the DOI-backed Vassallo et al. screen instead of "
                "inventing a missing article-registry entry."
            ),
            "evidence": [
                wiki_description_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
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
            "Minted PD-Lambda-1 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-Lambda-1 system canonical_examples and left them "
            "empty because the current sources support an E. coli "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Gemmata massiliana example, but not "
            "a direct native microbial isolate exemplar with experimentally "
            "verified endogenous PD-Lambda-1 activity. No paid research was "
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
