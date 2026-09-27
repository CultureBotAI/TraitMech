#!/usr/bin/env python3
"""Add the NLR-like bNACHT system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "nlr_like_bnacht_system.yaml"

OFIR = "DOI:10.1016/j.cell.2023.04.015"
OFIR_PMID = "PMID:37160116"
OFIR_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T12:41:08Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T12:41:09Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000408"
PROPOSAL = "proposals/metpo_traitmech_v285"
SLUG = "nlr_like_bnacht"

NACHT_ABSTRACT_SNIPPET = (
    "Here we show that proteins containing a NACHT module, the central "
    "feature of the animal nucleotide-binding domain and leucine-rich "
    "repeat-containing gene family (NLRs), are found in bacteria and "
    "defend against phages."
)
BNACHT01_NAMING_SNIPPET = (
    "We named this gene bacterial NACHT module-containing protein 1 "
    "(bNACHT01), and it did not appear to be in an operon with any other "
    "genes."
)
BNACHT01_PROTECTION_SNIPPET = (
    "bNACHT01 conferred over a 100-fold increase in protection against "
    "phage T4 and over a 1000-fold increase in protection against phages "
    "T5 and T6"
)
PHAGE_PRODUCTION_SNIPPET = (
    "bacteria expressing bNACHT01 restricted phage virion production and "
    "continued growing"
)
WALKER_MUTATION_SNIPPET = (
    "Mutation of R214 to alanine maintained expression of the protein but "
    "abrogated phage defense"
)
BNACHT_BREADTH_SNIPPET = (
    "Diverse bacterial NACHT proteins from different clades exhibited robust "
    "antiphage activity across a wide range of phages"
)

ARTICLE_REGISTRY_SNIPPET = (
    "NLR | 10\\.1101/2022\\.07\\.19\\.500537 | Bacterial NLR-related "
    "proteins protect against phage"
)
RULES_SNIPPETS = [
    (
        "NLR\tNLR_like_bNACHT01\t1\t1\t"
        "NLR_like_bNACHT01__NLR_like_bNACHT01\t\t\t"
    ),
    (
        "NLR\tNLR_like_bNACHT09\t1\t1\t"
        "NLR_like_bNACHT09__NLR_like_bNACHT09\t\t\t"
    ),
]
HMM_SNIPPETS = [
    (
        "| NLR_like_bNACHT01__NLR_like_bNACHT01             | "
        "NLR_like_bNACHT01__NLR_like_bNACHT01             | "
        "NLR_like_bNACHT01      | Custom                  | 250    |"
    ),
    (
        "| NLR_like_bNACHT09__NLR_like_bNACHT09             | "
        "NLR_like_bNACHT09__NLR_like_bNACHT09             | "
        "NLR_like_bNACHT09      | Custom                  | 400    |"
    ),
]


def abstract_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": NACHT_ABSTRACT_SNIPPET,
        "notes": (
            "Ofir et al. support NACHT-module proteins as bacterial "
            "NLR-related proteins that defend against phages."
        ),
    }


def bnacht01_naming_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": BNACHT01_NAMING_SNIPPET,
        "notes": (
            "Ofir et al. named the tested Klebsiella pneumoniae MGH 35 "
            "NACHT-module protein bNACHT01."
        ),
    }


def bnacht01_protection_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": BNACHT01_PROTECTION_SNIPPET,
        "notes": (
            "bNACHT01 protected against phages T4, T5, and T6 in the "
            "E. coli heterologous assay."
        ),
    }


def phage_production_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": PHAGE_PRODUCTION_SNIPPET,
        "notes": (
            "Ofir et al. observed restricted phage virion production in "
            "bacteria expressing bNACHT01."
        ),
    }


def walker_mutation_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": WALKER_MUTATION_SNIPPET,
        "notes": (
            "An R214A NACHT-module mutation preserved bNACHT01 expression "
            "but abrogated defense, supporting a NACHT-dependent output."
        ),
    }


def bnacht_breadth_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_PMC,
        "snippet": BNACHT_BREADTH_SNIPPET,
        "notes": (
            "Ofir et al. observed antiphage activity across diverse "
            "bacterial NACHT proteins."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the NLR family key to "
            "the Ofir et al. bNACHT preprint."
        ),
    }


def rules_evidence(index: int) -> dict[str, str]:
    subtype = "NLR_like_bNACHT01" if index == 0 else "NLR_like_bNACHT09"
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPETS[index],
        "notes": (
            "The DefenseFinder rules table models "
            f"{subtype} as a one-profile NLR-family subsystem."
        ),
    }


def hmm_evidence(index: int) -> dict[str, str]:
    subtype = "NLR_like_bNACHT01" if index == 0 else "NLR_like_bNACHT09"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPETS[index],
        "notes": (
            "The DefenseFinder HMM inventory records the "
            f"{subtype} profile under the same-named model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "NLR-like bNACHT system",
    "definition": (
        "A phage defense system in which an organism possesses an "
        "NLR-related bacterial NACHT locus represented by DefenseFinder as "
        "an NLR_like_bNACHT01 or NLR_like_bNACHT09 single-profile model, "
        "encoding a NACHT-module STAND-family protein that can restrict "
        "bacteriophage production."
    ),
    "definition_source": OFIR,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "NLR",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "bNACHT",
            "synonym_type": "RELATED_SYNONYM",
            "source": OFIR,
        },
        {
            "synonym_text": "NLR_like_bNACHT01",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "NLR_like_bNACHT09",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        abstract_evidence(),
        bnacht01_naming_evidence(),
        bnacht01_protection_evidence(),
        phage_production_evidence(),
        walker_mutation_evidence(),
        bnacht_breadth_evidence(),
        article_registry_evidence(),
        rules_evidence(0),
        rules_evidence(1),
        hmm_evidence(0),
        hmm_evidence(1),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:573",
            "taxon_label": "Klebsiella pneumoniae",
            "note": (
                "Ofir et al. identified the bNACHT01 locus in Klebsiella "
                "pneumoniae MGH 35 and found that bNACHT01 expressed from "
                "its endogenous promoter in Escherichia coli protected "
                "against phages T4, T5, and T6."
            ),
            "reference": OFIR,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "nlr_like_bnacht_loci_restrict_phage",
            "title": "NLR-like bNACHT loci restrict phage production",
            "description": (
                "Conservative system-level sketch linking NLR-like bNACHT "
                "loci to bacteriophage restriction while leaving subtype "
                "triggers and effector outputs unresolved."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DefenseFinder NLR_like_bNACHT01 and "
                "NLR_like_bNACHT09 as named bNACHT phage-defense models "
                "supported by Ofir et al. bacterial NLR-related protein "
                "experiments while leaving natural host breadth, phage "
                "triggers, the exact profile-to-bNACHT01 or "
                "profile-to-bNACHT09 correspondences, and subtype-specific "
                "effector mechanisms unresolved."
            ),
            "nodes": [
                {
                    "node_id": "nlr_like_bnacht_locus",
                    "label": "NLR-like bNACHT locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacterial NLR-related phage-defense locus "
                        "cataloged in DefenseFinder with a bNACHT profile."
                    ),
                },
                {
                    "node_id": "bnacht_phage_restriction",
                    "label": "bNACHT phage restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of phage production by a bacterial "
                        "NACHT-module antiviral protein."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "NLR-like bNACHT system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded NLR-like bNACHT "
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
                    "subject": "nlr_like_bnacht_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "bnacht_phage_restriction",
                    "description": (
                        "Ofir et al. showed that bacterial NACHT proteins "
                        "can restrict bacteriophages, and DefenseFinder "
                        "models two NLR_like_bNACHT subtypes."
                    ),
                    "evidence": [
                        abstract_evidence(),
                        bnacht01_protection_evidence(),
                        phage_production_evidence(),
                        rules_evidence(0),
                        rules_evidence(1),
                        hmm_evidence(0),
                        hmm_evidence(1),
                    ],
                },
                {
                    "subject": "bnacht_phage_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "NACHT-module-dependent phage restriction realizes "
                        "the NLR-like bNACHT system trait."
                    ),
                    "evidence": [
                        phage_production_evidence(),
                        walker_mutation_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "NLR-like bNACHT system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        abstract_evidence(),
                        bnacht_breadth_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "nlr-like-bnacht-mechanism-gap",
            "prompt": (
                "Resolve the exact mapping between DefenseFinder "
                "NLR_like_bNACHT01 and NLR_like_bNACHT09 profiles and the "
                "experimentally tested bNACHT proteins, natural host "
                "breadth, phage triggers, and bNACHT effector mechanisms "
                "before minting narrower bNACHT subtype traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Ofir et al. support bacterial NACHT proteins as "
                "NLR-related phage-defense proteins and DefenseFinder "
                "models NLR_like_bNACHT01 and NLR_like_bNACHT09 as "
                "single-profile NLR-family subsystems. This first "
                "system-level record leaves profile-to-assayed-protein "
                "correspondence and subtype-specific trigger and effector "
                "mechanisms unresolved."
            ),
            "evidence": [
                abstract_evidence(),
                bnacht01_protection_evidence(),
                rules_evidence(0),
                rules_evidence(1),
                hmm_evidence(0),
                hmm_evidence(1),
            ],
            "attaches_to": ["causal_graphs#nlr_like_bnacht_loci_restrict_phage"],
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
            "Minted NLR-like bNACHT system as a DOI-, PMID-, and "
            "stable-URL-backed GENOMICS TraitRecord under phage defense "
            "system after an ignored-and-hidden duplicate review found no "
            "exact live TraitMech, METPO, history, or prior proposal "
            f"record; the replacement placeholder is reserved in {PROPOSAL}."
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
            "Reviewed NLR-like bNACHT system canonical-example evidence and "
            "kept the example at the Klebsiella pneumoniae species level "
            "because Ofir et al. identified the tested bNACHT01 locus from "
            "K. pneumoniae MGH 35 but assayed the endogenous-promoter "
            "construct heterologously in Escherichia coli. No paid "
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
