#!/usr/bin/env python3
"""Add the Rst gop-beta-cII system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rst_gop_beta_cll_system.yaml"

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
TIMESTAMP = "2026-09-26T08:43:24Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T08:53:24Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000376"
PROPOSAL = "proposals/metpo_traitmech_v253"
SLUG = "rst_gop_beta_cll"

P4_LOCUS_SNIPPET = (
    "The well-characterized P4 satellite (NC_001609) carries at this "
    "position the non-essential genes gop, β, and cII, with gop and β "
    "likely acting as a toxin-antitoxin pair"
)
GOP_DEFENSE_SNIPPET = (
    "We report that gop-β-cII forms an anti-phage system that protects "
    "against λ and P1."
)
P4_HOTSPOT_SNIPPET = (
    "P2-like phages and their parasitic P4-like satellites carry hotspots "
    "of genetic variation containing reservoirs of anti-phage systems"
)
CLONED_SCREEN_SNIPPET = (
    "When compared with a control vector encoding a green fluorescent "
    "protein (GFP), seven systems provided robust and reproducible "
    "resistance to at least one phage"
)
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_gop_beta_cll | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_gop_beta_cll\tRst_gop_beta_cll\t3\t3\t"
    "Rst_gop_beta_cll__beta, Rst_gop_beta_cll__cll, "
    "Rst_gop_beta_cll__gop\t\t\t"
)
HMM_PROFILES = (
    "Rst_gop_beta_cll__beta",
    "Rst_gop_beta_cll__cll",
    "Rst_gop_beta_cll__gop",
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {profile:<49}| {'Rst_gop_beta_cll':<23}| "
    f"{'Custom':<24}| {'20':<7}|"
    for profile in HMM_PROFILES
)


def p4_locus_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": P4_LOCUS_SNIPPET,
        "notes": (
            "Rousset et al. describe the canonical P4 satellite gop, beta, "
            "and cII locus before testing it for anti-phage activity."
        ),
    }


def gop_defense_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": GOP_DEFENSE_SNIPPET,
        "notes": (
            "Rousset et al. directly identify gop-beta-cII as an anti-phage "
            "system that protects against lambda and P1."
        ),
    }


def p4_hotspot_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": P4_HOTSPOT_SNIPPET,
        "notes": (
            "Rousset et al. frame the P4-like satellite hotspot that "
            "contains gop-beta-cII as a reservoir of anti-phage systems."
        ),
    }


def cloned_screen_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": CLONED_SCREEN_SNIPPET,
        "notes": (
            "Rousset et al. cloned P4/P2 hotspot systems under native "
            "promoters and measured reproducible phage resistance against "
            "their coliphage panel."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Rst_gop_beta_cll system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_gop_beta_cll as a "
            "three-profile system requiring beta, cll, and gop profiles."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records custom beta, cll, and "
            "gop profiles under the Rst_gop_beta_cll system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst gop-beta-cII system",
    "definition": (
        "A phage defense system in which an organism possesses a P4-like "
        "gop-beta-cII locus represented by DefenseFinder as the "
        "Rst_gop_beta_cll model and experimentally linked to lambda and P1 "
        "phage restriction."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "gop-β-cII",
            "synonym_type": "EXACT_SYNONYM",
            "source": ROUSSET,
        },
        {
            "synonym_text": "Rst_gop_beta_cll",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        p4_locus_evidence(),
        gop_defense_evidence(),
        cloned_screen_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_gop_beta_cll_locus_restricts_lambda_p1",
            "title": "Rst gop-beta-cII loci restrict lambda and P1 phages",
            "description": (
                "Conservative system-level sketch linking a P4 gop-beta-cII "
                "locus to lambda and P1 phage restriction."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures gop-beta-cII as a named DefenseFinder "
                "three-profile phage-defense system while leaving natural "
                "host breadth, the direct phage trigger, the gop and beta "
                "toxin-antitoxin interpretation, cII activity, and "
                "profile-to-gene mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_gop_beta_cll_locus",
                    "label": "Rst gop-beta-cII locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A P4-like gop-beta-cII phage-defense locus "
                        "represented by beta, cll, and gop DefenseFinder "
                        "profiles."
                    ),
                },
                {
                    "node_id": "lambda_and_p1_phage_restriction",
                    "label": "lambda and P1 phage restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of bacteriophages lambda and P1 by the "
                        "gop-beta-cII locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst gop-beta-cII system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded gop-beta-cII "
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
                    "subject": "rst_gop_beta_cll_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "lambda_and_p1_phage_restriction",
                    "description": (
                        "Rousset et al. linked gop-beta-cII to lambda and P1 "
                        "phage protection, and DefenseFinder models "
                        "Rst_gop_beta_cll as a three-profile system."
                    ),
                    "evidence": [
                        p4_locus_evidence(),
                        cloned_screen_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "lambda_and_p1_phage_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Restriction of lambda and P1 phages realizes the "
                        "Rst gop-beta-cII system trait."
                    ),
                    "evidence": [
                        gop_defense_evidence(),
                        cloned_screen_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst gop-beta-cII system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        p4_hotspot_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-gop-beta-cll-mechanism-gap",
            "prompt": (
                "Resolve Rst_gop_beta_cll natural host breadth, exact beta "
                "and cll gene correspondence, direct phage trigger, and Gop "
                "or beta toxin-antitoxin activities before minting narrower "
                "P4 gop-beta-cII mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a canonical P4 gop-beta-cII system "
                "that protects against lambda and P1, and DefenseFinder "
                "represents Rst_gop_beta_cll as a required beta/cll/gop "
                "three-profile model. This first system-level record leaves "
                "natural host breadth, profile-to-gene mapping, the direct "
                "phage trigger, and the gop, beta, or cII effector logic "
                "unresolved."
            ),
            "evidence": [
                p4_locus_evidence(),
                gop_defense_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#rst_gop_beta_cll_locus_restricts_lambda_p1"
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
            "Minted Rst gop-beta-cII system as a DOI-backed GENOMICS "
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
            "Reviewed Rst gop-beta-cII system during canonical-example "
            "issue 444 enforcement and left canonical_examples empty "
            "because the sources support a cloned P4 gop-beta-cII locus "
            "tested in Escherichia coli and a DefenseFinder system model, "
            "but not a direct native microbial isolate exemplar with "
            "experimentally verified Rst_gop_beta_cll activity. No paid "
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
