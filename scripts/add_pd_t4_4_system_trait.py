#!/usr/bin/env python3
"""Add the PD-T4-4 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t4_4_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t4-4.md"
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
TIMESTAMP = "2026-09-26T16:51:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T16:51:01Z"
REVIEW_SCOPE_TIMESTAMP = "2026-09-26T17:24:43Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000389"
PROPOSAL = "proposals/metpo_traitmech_v266"
SLUG = "pd_t4_4"

PHAGE_LIST = "T2, T4, T6, and SECphi17"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_DESCRIPTION_SNIPPET = (
    "PD-T4-4 is a defense system composed of two proteins, a P-loop NTPase "
    "and a nuclease, that is most likely protecting the bacterial population "
    "through abortive infection. It was identified from an ICE in an "
    "*E. coli* genome."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-T4-4 is composed of 2 proteins: PD-T4-4_A and PD-T4-4_B."
)
THIOTHRIX_EXAMPLE_SNIPPET = (
    "The PD-T4-4 system in *Thiothrix subterranea* "
    "(GCF_016772315.1, NZ_CP053482) is composed of 2 proteins PD-T4-4_A "
    "(WP_202716711.1) PD-T4-4_B (WP_202716712.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RCO57999.1'>"
    "RCO57999.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "RCO57988.1'>RCO57988.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T2 & T4 & T6 & SECphi17"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        T2\n"
    "        T4\n"
    "        T6\n"
    "        SECphi17"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T4-4 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the landscape "
    "of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = (
    "PD-T4-4\tPD-T4-4\t2\t2\t"
    "PD-T4-4__PD-T4-4_A, PD-T4-4__PD-T4-4_B\t\t\t"
)
PROFILE_A = "PD-T4-4__PD-T4-4_A"
PROFILE_B = "PD-T4-4__PD-T4-4_B"
PROFILE_NAMES = f"{PROFILE_A} and {PROFILE_B}"
HMM_ROW_A = (
    "| PD-T4-4__PD-T4-4_A                               | "
    "PD-T4-4__PD-T4-4_A                               | "
    "PD-T4-4                | Custom                  | 75     |"
)
HMM_ROW_B = (
    "| PD-T4-4__PD-T4-4_B                               | "
    "PD-T4-4__PD-T4-4_B                               | "
    "PD-T4-4                | Custom                  | 25     |"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T4-4 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes PD-T4-4 as a two-protein "
            "system from an E. coli integrative and conjugative element."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-T4-4 as a two-protein system "
            "with PD-T4-4_A and PD-T4-4_B components."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": THIOTHRIX_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "PD-T4-4 locus in RefSeq assembly GCF_016772315.1 on NZ_CP053482."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T4-4 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T4-4 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-T4-4 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-T4-4 as a two-profile "
            f"system requiring {PROFILE_NAMES}."
        ),
    }


def hmm_a_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_A,
        "notes": (
            f"The DefenseFinder HMM inventory records {PROFILE_A} under the "
            "PD-T4-4 system namespace."
        ),
    }


def hmm_b_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_B,
        "notes": (
            f"The DefenseFinder HMM inventory records {PROFILE_B} under the "
            "PD-T4-4 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T4-4 system",
    "definition": (
        "A phage defense system in which an organism possesses a PD-T4-4 "
        "locus represented by DefenseFinder as a two-profile model "
        f"requiring {PROFILE_NAMES}, and experimentally linked to "
        f"{PHAGE_LIST} protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-T4-4",
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
        hmm_a_evidence(),
        hmm_b_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t4_4_locus_restricts_t2_t4_t6_and_secphi17",
            "title": f"PD-T4-4 loci restrict {PHAGE_LIST}",
            "description": (
                "Conservative system-level sketch linking possession of a "
                f"PD-T4-4 locus to protection against {PHAGE_LIST}."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T4-4 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, and the hinted "
                "abortive-infection effector mechanism unmodeled until "
                "direct mechanism evidence is available."
            ),
            "nodes": [
                {
                    "node_id": "pd_t4_4_locus",
                    "label": "PD-T4-4 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the two "
                        "PD-T4-4 DefenseFinder profiles."
                    ),
                },
                {
                    "node_id": "pd_t4_4_listed_phage_protection",
                    "label": f"{PHAGE_LIST} protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": f"Protection against {PHAGE_LIST} by PD-T4-4.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T4-4 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T4-4 "
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
                    "subject": "pd_t4_4_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t4_4_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T4-4 locus "
                        f"from Vassallo et al. to protection against {PHAGE_LIST}, "
                        "and DefenseFinder models PD-T4-4 through two "
                        "mandatory profiles."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_a_evidence(),
                        hmm_b_evidence(),
                    ],
                },
                {
                    "subject": "pd_t4_4_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        f"Protection against {PHAGE_LIST} realizes the "
                        "PD-T4-4 system trait."
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
                        "PD-T4-4 system possession is a phage-defense-system "
                        "trait."
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
            "discussion_id": "pd-t4-4-mechanism-gap",
            "prompt": (
                "Resolve PD-T4-4 natural host breadth, direct phage trigger, "
                "and effector mechanism before minting narrower PD-T4-4 "
                "mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T4-4 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to protection "
                f"against {PHAGE_LIST}, and DefenseFinder represents the "
                "system with two mandatory profiles. Natural host breadth, "
                "the direct phage trigger, and direct effector logic remain "
                "unresolved, so the likely abortive-infection hypothesis is "
                "left unmodeled."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_description_evidence(),
                wiki_composition_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_a_evidence(),
                hmm_b_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#pd_t4_4_locus_restricts_t2_t4_t6_and_secphi17"
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
            "Minted PD-T4-4 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-T4-4 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder system model, "
            "and a RefSeq Thiothrix subterranea example, but not a direct "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous PD-T4-4 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_SCOPE_NOTE_REVIEW",
        changes=(
            "Clarified after Claude Code Review issue 1288 that the "
            "DefenseFinder wiki names abortive infection as the likely "
            "PD-T4-4 population-level protection route, but the graph "
            "leaves that hypothesis unmodeled until direct mechanism "
            "evidence is available."
        ),
        llm_assisted=True,
        timestamp=REVIEW_SCOPE_TIMESTAMP,
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
