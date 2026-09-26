#!/usr/bin/env python3
"""Add the Rst TIR-NLR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rst_tir_nlr_system.yaml"

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-26T09:17:05Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T09:17:06Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000377"
PROPOSAL = "proposals/metpo_traitmech_v254"
SLUG = "rst_tir_nlr"

HOTSPOT_SNIPPET = (
    "Here, we show that hotspots of genetic diversity within the P2-like "
    "phage and P4-like satellite families constitute large reservoirs of "
    "anti-phage systems."
)
TIR_DOMAIN_SNIPPET = (
    "Validated systems also include a single-gene system with a TIR "
    "(toll/interleukin-1-receptor-like) domain protein."
)
P2_PROTECTION_SNIPPET = (
    "Out of the 18 tested systems, only the TIR-NLR system provided "
    "protection"
)
BROAD_PROTECTION_SNIPPET = (
    "This shows that while the TIR-NLR system protects against a broad "
    "range of virulent phages, this comes at the cost of limiting the "
    "transduction of P4 by P2."
)
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_TIR-NLR | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_TIR-NLR\tRst_TIR-NLR\t1\t1\tRst_TIR-NLR__TIR\t\t\t"
)
HMM_PROFILE = "Rst_TIR-NLR__TIR"
HMM_SNIPPET = (
    f"| {HMM_PROFILE:<49}| {HMM_PROFILE:<49}| {'Rst_TIR-NLR':<23}| "
    f"{'Custom':<24}| {'70':<7}|"
)


def hotspot_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": HOTSPOT_SNIPPET,
        "notes": (
            "Rousset et al. establish that P2-like phage and P4-like "
            "satellite hotspots are large reservoirs of anti-phage systems."
        ),
    }


def tir_domain_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": TIR_DOMAIN_SNIPPET,
        "notes": (
            "Rousset et al. describe one validated P4 hotspot system as a "
            "single-gene TIR-domain system."
        ),
    }


def p2_protection_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": P2_PROTECTION_SNIPPET,
        "notes": (
            "Rousset et al. report that TIR-NLR was the only P4 system in "
            "their tested cohort that protected against P2-like phages."
        ),
    }


def broad_protection_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": BROAD_PROTECTION_SNIPPET,
        "notes": (
            "Rousset et al. summarize broad virulent-phage protection by "
            "the TIR-NLR system in the context of P4 transduction costs."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Rst_TIR-NLR "
            "system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_TIR-NLR as a "
            "single-profile system requiring the Rst_TIR-NLR__TIR profile."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records Rst_TIR-NLR__TIR "
            "under the Rst_TIR-NLR system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst TIR-NLR system",
    "definition": (
        "A phage defense system in which an organism possesses a P4-like "
        "TIR-NLR locus represented by DefenseFinder as the Rst_TIR-NLR "
        "single-profile model and experimentally linked to broad "
        "virulent-phage and P2-like phage restriction."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "TIR-NLR system",
            "synonym_type": "RELATED_SYNONYM",
            "source": ROUSSET,
        },
        {
            "synonym_text": "Rst_TIR-NLR",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Rst_TIR-NLR__TIR",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        hotspot_evidence(),
        tir_domain_evidence(),
        p2_protection_evidence(),
        broad_protection_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_tir_nlr_locus_restricts_phages",
            "title": "Rst TIR-NLR loci restrict virulent and P2-like phages",
            "description": (
                "Conservative system-level sketch linking a P4-like "
                "Rst TIR-NLR locus to phage restriction."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_TIR-NLR as a named DefenseFinder "
                "single-profile phage-defense system while leaving source "
                "locus breadth, the phage trigger, TIR/STAND activation, "
                "and exact Rst_TIR-NLR__TIR profile-to-gene correspondence "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_tir_nlr_locus",
                    "label": "Rst TIR-NLR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A P4-like TIR-NLR phage-defense locus represented "
                        "by the Rst_TIR-NLR DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "virulent_and_p2_like_phage_restriction",
                    "label": "virulent and P2-like phage restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of broad virulent phages and P2-like "
                        "phages by the TIR-NLR locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst TIR-NLR system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded TIR-NLR "
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
                    "subject": "rst_tir_nlr_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "virulent_and_p2_like_phage_restriction",
                    "description": (
                        "Rousset et al. linked the TIR-NLR system to "
                        "virulent and P2-like phage protection, and "
                        "DefenseFinder models Rst_TIR-NLR as a "
                        "single-profile system."
                    ),
                    "evidence": [
                        tir_domain_evidence(),
                        p2_protection_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "virulent_and_p2_like_phage_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Restriction of virulent and P2-like phages "
                        "realizes the Rst TIR-NLR system trait."
                    ),
                    "evidence": [
                        broad_protection_evidence(),
                        p2_protection_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst TIR-NLR system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        hotspot_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-tir-nlr-mechanism-gap",
            "prompt": (
                "Resolve Rst_TIR-NLR natural host breadth, exact profile-to-gene "
                "correspondence, direct phage trigger, and TIR/STAND activation "
                "before minting narrower Rst TIR-NLR mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a P4-like TIR-NLR system that "
                "protects against virulent and P2-like phages, and "
                "DefenseFinder represents Rst_TIR-NLR as a single-profile "
                "model. This first system-level record leaves natural host "
                "breadth, profile-to-gene mapping, the direct phage trigger, "
                "and TIR/STAND effector logic unresolved."
            ),
            "evidence": [
                tir_domain_evidence(),
                p2_protection_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#rst_tir_nlr_locus_restricts_phages"],
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
            "Minted Rst TIR-NLR system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
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
            "Reviewed Rst TIR-NLR system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support cloned P4-like TIR-NLR system assays and a "
            "DefenseFinder system model, but not a direct native microbial "
            "isolate exemplar with experimentally verified Rst_TIR-NLR "
            "activity. No paid research was used."
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
