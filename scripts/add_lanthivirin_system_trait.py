#!/usr/bin/env python3
"""Add the lanthivirin system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "lanthivirin_system.yaml"

SERRA = "DOI:10.1016/j.chom.2026.06.017"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T20:02:44Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T20:02:45Z"
IDENTIFIER = "traitmech:000416"
PROPOSAL = "proposals/metpo_traitmech_v293"

ANTI_PHAGE_SNIPPET = (
    "We demonstrate anti-phage activity both in a native Streptomyces "
    "context and through heterologous expression of six distinct "
    "lanthivirin systems."
)
MATURATION_SNIPPET = (
    "lanthivirin maturation is required for anti-phage activity"
)
PHAGE_DNA_REPLICATION_SNIPPET = (
    "phage-protein-dependent inhibition of phage DNA replication"
)
ARTICLE_ROW = (
    "| Lanthiphage | 10\\.1101/2024\\.06\\.26\\.600839 | A family of "
    "lanthipeptides with anti-phage function |"
)
HMM_PROFILE_SNIPPETS = {
    "Lanthiphage__LphA": "| Lanthiphage__LphA                                |",
    "Lanthiphage__LphB1": "| Lanthiphage__LphB1                               |",
}


def anti_phage_evidence() -> dict[str, str]:
    return {
        "reference": SERRA,
        "snippet": ANTI_PHAGE_SNIPPET,
        "notes": (
            "Serra et al. support native Streptomyces anti-phage activity "
            "and activity from multiple heterologously expressed "
            "lanthivirin systems."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Lanthiphage "
            "source key to the lanthipeptide anti-phage preprint."
        ),
    }


def maturation_evidence() -> dict[str, str]:
    return {
        "reference": SERRA,
        "snippet": MATURATION_SNIPPET,
        "notes": (
            "Serra et al. support the requirement for lanthivirin "
            "maturation in anti-phage activity."
        ),
    }


def phage_dna_replication_evidence() -> dict[str, str]:
    return {
        "reference": SERRA,
        "snippet": PHAGE_DNA_REPLICATION_SNIPPET,
        "notes": (
            "Serra et al. link lanthivirins to inhibition of phage DNA "
            "replication."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom Lanthiphage profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "lanthivirin system",
    "definition": (
        "A phage defense system in which an organism possesses a lanthivirin "
        "lanthipeptide biosynthetic gene cluster that can confer "
        "anti-phage activity in a native Streptomyces context and after "
        "heterologous expression of complete lanthivirin systems."
    ),
    "definition_source": SERRA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "lanthivirin BGC",
            "synonym_type": "RELATED_SYNONYM",
            "source": SERRA,
        },
        {
            "synonym_text": "Lanthiphage",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        anti_phage_evidence(),
        maturation_evidence(),
        phage_dna_replication_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "lanthivirin_bgc_inhibits_phage_dna_replication",
            "title": "Lanthivirin BGCs mediate anti-phage activity",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "lanthivirin biosynthetic gene cluster to anti-phage "
                "activity and lanthivirin system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures lanthivirins at the biosynthetic gene "
                "cluster and anti-phage-output level without asserting the "
                "full native host range, exact Lanthiphage "
                "profile-to-component model, complete phage target breadth, "
                "or a DefenseFinder detection rule absent from the pinned "
                "rules table."
            ),
            "nodes": [
                {
                    "node_id": "lanthivirin_bgc",
                    "label": "lanthivirin biosynthetic gene cluster",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A lanthivirin biosynthetic gene cluster represented "
                        "in the pinned DefenseFinder HMM inventory by "
                        "Lanthiphage custom profiles."
                    ),
                },
                {
                    "node_id": "lanthivirin_maturation",
                    "label": "lanthivirin maturation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Maturation of a lanthivirin lanthipeptide by its "
                        "biosynthetic gene cluster."
                    ),
                },
                {
                    "node_id": "phage_dna_replication",
                    "label": "phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Replication of infecting bacteriophage DNA.",
                },
                {
                    "node_id": "lanthivirin_system_trait",
                    "label": "lanthivirin system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded lanthivirin "
                        "anti-phage system."
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
                    "subject": "lanthivirin_bgc",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "lanthivirin_maturation",
                    "description": (
                        "A lanthivirin biosynthetic gene cluster encodes the "
                        "machinery required for lanthivirin maturation."
                    ),
                    "evidence": [
                        maturation_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "lanthivirin_maturation",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_dna_replication",
                    "description": (
                        "Mature lanthivirins are associated with a "
                        "phage-protein-dependent inhibition of phage DNA "
                        "replication."
                    ),
                    "evidence": [
                        phage_dna_replication_evidence(),
                    ],
                },
                {
                    "subject": "lanthivirin_maturation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "lanthivirin_system_trait",
                    "description": (
                        "Lanthivirin maturation realizes the anti-phage "
                        "activity of the lanthivirin system."
                    ),
                    "evidence": [
                        anti_phage_evidence(),
                    ],
                },
                {
                    "subject": "lanthivirin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Lanthivirin system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "lanthivirin-defensefinder-model-gap",
            "prompt": (
                "Resolve Lanthiphage HMM-to-component coverage, "
                "rule-level detection criteria, sensitive-phage breadth, "
                "and exact lanthivirin effector identity before minting "
                "narrower lanthivirin mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Serra et al. support lanthivirin biosynthetic gene clusters "
                "as anti-phage systems, and the pinned DefenseFinder HMM "
                "inventory records Lanthiphage profile rows. The pinned "
                "rules table has no Lanthiphage row, and the first-pass "
                "record does not yet resolve exact profile-to-component "
                "mapping, full native host breadth, phage target breadth, or "
                "the direct mature lanthivirin effector."
            ),
            "evidence": [
                anti_phage_evidence(),
                maturation_evidence(),
                phage_dna_replication_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "Lanthiphage, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#lanthivirin_bgc_inhibits_phage_dna_replication"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted lanthivirin system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at lanthipeptide biosynthetic-gene-cluster level "
            "because the pinned DefenseFinder HMM rows are not backed by "
            "pinned rules rows; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed lanthivirin system during canonical-example issue "
            "444 enforcement and left canonical_examples empty because the "
            "sources support Streptomyces-context and heterologous "
            "expression assays, plus DefenseFinder Lanthiphage HMM rows, "
            "but not a direct named native microbial isolate exemplar with "
            "experimentally verified endogenous lanthivirin activity. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
