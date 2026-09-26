#!/usr/bin/env python3
"""Add the GAPS4 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps4_system.yaml"

MAHATA = "DOI:10.1038/s41564-024-01840-5"
MAHATA_PREPRINT = "DOI:10.1101/2023.03.28.534373"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/gaps4.md"
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
TIMESTAMP = "2026-09-26T10:47:13Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T10:47:14Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000379"
PROPOSAL = "proposals/metpo_traitmech_v256"
SLUG = "gaps4"

MAHATA_GMT_SYSTEMS_SNIPPET = (
    "We reveal four anti-phage defence systems encoded within GMT islands "
    "and further characterize one system, GAPS1, showing it is triggered "
    "by a phage capsid protein to induce cell dormancy"
)
WIKI_COMPOSITION_SNIPPET = (
    "GAPS4 is a two genes system (GAPS4a and GAPS4b). GAPS stands for "
    "GMT-encoded Anti-Phage System."
)
WIKI_ACTIVITY_SNIPPET = (
    "GAPS4 is present in both Gram-positive and Gram-negative GAPS4 activity "
    "was assessed in *E. coli* and was shown to be active against T4, P1-vir "
    "and lambda-vir and to reduce lysis plaque size of T7 "
    ":ref{doi=10.1101/2023.03.28.534373}."
)
WIKI_DNASE_SNIPPET = (
    "GAPS4a is a nuclease containing a domain from the PDDEXK clan (CL0236) "
    "suggesting that the GAPS4 defense system is acting via DNA degradation. "
    "Both genes are required for phage defense and were predicted to form a "
    "heterodimer. It was shown that the system causes host DNA degradation "
    "upon infection by lambda-vir only, which would suggest that GAPS4 is an "
    "abortive infection system :ref{doi=10.1101/2023.03.28.534373}."
)
WIKI_REFSEQ_SNIPPET = (
    "The GAPS4 system in *Hafnia alvei* (GCF_902387815.1, NZ_LR699008) is "
    "composed of 2 proteins GAPS4a (WP_111329122.1) GAPS4b (WP_111329123.1)"
)
WIKI_VALIDATION_GRAPH_SNIPPET = (
    "Mahata_2023[<a href='https://doi.org/10.1101/2023.03.28.534373'>"
    "Mahata et al., 2023</a>] --> Origin_0\n"
    "    Origin_0[Vibrio parahaemolyticus \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_055466293.1'>"
    "WP_055466293.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_055466294.1'>WP_055466294.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T7 & T4 & P1-vir & Lambda-vir"
)
WIKI_PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        T7\n"
    "        T4\n"
    "        P1-vir\n"
    "        Lambda-vir"
)
ARTICLE_REGISTRY_SNIPPET = (
    "GAPS4 | 10\\.1101/2023\\.03\\.28\\.534373 | Gamma-Mobile-Trio systems "
    "define a new class of mobile elements rich in bacterial defensive and "
    "offensive tools"
)
RULES_SNIPPET = "GAPS4\tGAPS4\t2\t2\tGAPS4__GAPS4a, GAPS4__GAPS4b\t\t\t"
HMM_THRESHOLDS = {
    "GAPS4__GAPS4a": "20",
    "GAPS4__GAPS4b": "20",
}
HMM_ROWS = {
    profile: (
        f"| {profile:<49}| {profile:<49}| {'GAPS4':<23}| "
        f"{'Custom':<24}| {threshold:<7}|"
    )
    for profile, threshold in HMM_THRESHOLDS.items()
}


def mahata_gmt_systems_evidence() -> dict[str, str]:
    return {
        "reference": MAHATA,
        "snippet": MAHATA_GMT_SYSTEMS_SNIPPET,
        "notes": (
            "Mahata et al. identify four anti-phage defense systems in "
            "Gamma-Mobile-Trio islands."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes GAPS4 as a two-gene "
            "GMT-encoded anti-phage system."
        ),
    }


def wiki_activity_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_ACTIVITY_SNIPPET,
        "notes": (
            "The DefenseFinder wiki summarizes GAPS4 activity against T4, "
            "P1-vir, lambda-vir, and T7 plaque lysis in an E. coli assay."
        ),
    }


def wiki_dnase_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DNASE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki summarizes evidence for PDDEXK-domain "
            "GAPS4a, dual-gene requirement, and lambda-vir-associated host "
            "DNA degradation."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "GAPS4 locus in RefSeq assembly GCF_902387815.1 on NZ_LR699008."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Mahata et al. to a Vibrio parahaemolyticus GAPS4 source locus "
            "expressed in E. coli against T7, T4, P1-vir, and Lambda-vir."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists T7, "
            "T4, P1-vir, and Lambda-vir in the GAPS4 protects-against "
            "subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named GAPS4 system "
            "to the Mahata et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models GAPS4 as a two-profile "
            "system requiring GAPS4__GAPS4a and GAPS4__GAPS4b."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under the "
            "GAPS4 system namespace."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GAPS4 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "GMT-encoded GAPS4 locus represented by DefenseFinder as a "
        "two-profile model, GAPS4__GAPS4a and GAPS4__GAPS4b, and "
        "experimentally linked to T7, T4, P1-vir, and lambda-vir "
        "protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "GAPS4",
            "synonym_type": "EXACT_SYNONYM",
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
        mahata_gmt_systems_evidence(),
        wiki_composition_evidence(),
        wiki_activity_evidence(),
        wiki_dnase_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gaps4_locus_restricts_phages",
            "title": "GAPS4 loci protect against T7, T4, P1-vir, and lambda-vir",
            "description": (
                "Conservative system-level sketch linking GAPS4 locus "
                "possession to protection against T7, T4, P1-vir, and "
                "lambda-vir."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GAPS4 as a named two-profile "
                "DefenseFinder phage-defense system while leaving natural "
                "host breadth, the lambda-vir trigger of host DNA "
                "degradation, the abortive-infection mechanism, and exact "
                "GAPS4a/GAPS4b profile-to-protein correspondence unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gaps4_locus",
                    "label": "GAPS4 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A GMT-encoded phage-defense locus represented by "
                        "the GAPS4a and GAPS4b DefenseFinder profiles."
                    ),
                },
                {
                    "node_id": "gaps4_listed_phage_protection",
                    "label": "T7, T4, P1-vir, and lambda-vir protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against T7, T4, P1-vir, and lambda-vir "
                        "by GAPS4."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "GAPS4 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GAPS4 phage-defense "
                        "system."
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
                    "subject": "gaps4_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gaps4_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a "
                        "Vibrio parahaemolyticus GAPS4 locus from Mahata "
                        "et al. to protection against T7, T4, P1-vir, and "
                        "lambda-vir, and DefenseFinder models GAPS4 through "
                        "GAPS4a and GAPS4b profiles."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_activity_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "gaps4_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against T7, T4, P1-vir, and lambda-vir "
                        "realizes the GAPS4 system trait."
                    ),
                    "evidence": [
                        wiki_activity_evidence(),
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
                        "GAPS4 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        mahata_gmt_systems_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gaps4-mechanism-gap",
            "prompt": (
                "Resolve GAPS4 natural host breadth, lambda-vir "
                "host-DNA-degradation triggers, abortive-infection "
                "mechanism, and exact GAPS4a/GAPS4b profile-to-protein "
                "correspondence before minting narrower GAPS4 mechanism "
                "traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mahata et al. support GAPS4 as a GMT-encoded anti-phage "
                "defense system that protects E. coli against T7, T4, "
                "P1-vir, and lambda-vir when expressed from a "
                "Vibrio parahaemolyticus locus, and DefenseFinder "
                "represents GAPS4 as a two-profile system. Natural host "
                "breadth, the lambda-vir-specific trigger of host DNA "
                "degradation, the abortive-infection mechanism, and exact "
                "profile-to-protein correspondence remain unresolved."
            ),
            "evidence": [
                wiki_activity_evidence(),
                wiki_dnase_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                *all_hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#gaps4_locus_restricts_phages"],
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
            "Minted GAPS4 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed GAPS4 system canonical_examples and left them empty "
            "because the current sources support a Vibrio parahaemolyticus "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Hafnia alvei example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified endogenous GAPS4 activity. No paid research was used."
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
