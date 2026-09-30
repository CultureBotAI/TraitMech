#!/usr/bin/env python3
"""Add the Reve system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "reve_system.yaml"

DE_SOUSA = "DOI:10.1093/nar/gkag898"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T19:41:32Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T19:41:33Z"
IDENTIFIER = "traitmech:000499"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v376"

ARTICLE_ROW = (
    "| Reve | 10\\.64898/2026\\.02\\.27\\.708500 | Shuttling, "
    "swapping and mixing: the rapid modular evolution of antiviral "
    "repertoires in temperate phages and their satellites | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Reve "
            "source key to the de Sousa et al. P4/P2 antiviral-repertoire "
            "paper preprint."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "HMM inventory found no exact Reve row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Reve system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Reve system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "single-gene Reve antiviral locus that is encoded by P4-like "
        "phage satellites and can protect bacteria from bacteriophage "
        "infection."
    ),
    "definition_source": DE_SOUSA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "Reve",
            "synonym_type": "EXACT_SYNONYM",
            "source": DE_SOUSA,
        },
    ],
    "evidence": [
        {
            "reference": DE_SOUSA,
            "snippet": (
                "The Reve system is another single-gene system, with "
                "ATPase and KAP family P-loop domains"
            ),
            "notes": (
                "de Sousa et al. identify Reve as a single-gene P4 "
                "defense system with ATPase and KAP-family P-loop "
                "domain annotations."
            ),
        },
        {
            "reference": DE_SOUSA,
            "snippet": (
                "with most (e.g. Bandua, Aernus, Toga, and Reve) "
                "providing strong protection against phages of different "
                "families"
            ),
            "notes": (
                "de Sousa et al. identify Reve among the novel "
                "P4-associated systems that provided strong protection "
                "against phage challenge."
            ),
        },
        {
            "reference": DE_SOUSA,
            "snippet": (
                "Our experimental validation of anti-phage activity for "
                "13 novel systems encoded by P4 confirms"
            ),
            "notes": (
                "de Sousa et al. summarize the validated P4-encoded "
                "novel-system cohort in their discussion."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "reve_locus_restricts_phage",
            "title": "Reve loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of "
                "a Reve locus to restricted bacteriophage propagation "
                "without asserting the unresolved trigger or molecular "
                "output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Reve as a named single-gene P4 "
                "anti-phage system while leaving its phage trigger, "
                "molecular substrate, ATPase/P-loop role, antiviral "
                "effector output, source-locus breadth, and "
                "DefenseFinder HMM/rule model coverage unresolved."
            ),
            "nodes": [
                {
                    "node_id": "reve_locus",
                    "label": "Reve locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A P4-associated Reve anti-phage defense locus."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Reve system."
                    ),
                },
                {
                    "node_id": "reve_system_trait",
                    "label": "Reve system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Reve "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_SYSTEM,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "reve_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Reve loci are among the novel P4-encoded systems "
                        "that reduced bacteriophage infection."
                    ),
                    "evidence": [
                        {
                            "reference": DE_SOUSA,
                            "snippet": (
                                "with most (e.g. Bandua, Aernus, Toga, "
                                "and Reve) providing strong protection "
                                "against phages of different families"
                            ),
                            "notes": (
                                "de Sousa et al. name Reve among the "
                                "novel P4 systems with antiviral "
                                "phenotypes."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "reve_system_trait",
                    "description": (
                        "Reve-mediated phage protection realizes the Reve "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DE_SOUSA,
                            "snippet": (
                                "with most (e.g. Bandua, Aernus, Toga, "
                                "and Reve) providing strong protection "
                                "against phages of different families"
                            ),
                            "notes": (
                                "de Sousa et al. connect Reve to strong "
                                "protection in the novel-system "
                                "validation cohort."
                            ),
                        },
                    ],
                },
                {
                    "subject": "reve_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Reve system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DE_SOUSA,
                            "snippet": (
                                "13 novel systems encoded by P4 confirms "
                                "that the contribution of defence "
                                "functions to the pangenomes of P4 and P2"
                            ),
                            "notes": (
                                "de Sousa et al. frame Reve and its "
                                "cohort as newly validated P4-encoded "
                                "anti-phage defense functions."
                            ),
                        },
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "reve-mechanism-and-modelling-gap",
            "prompt": (
                "Resolve Reve locus breadth, exact phage triggers, "
                "ATPase/P-loop molecular roles, direct antiviral output, "
                "source-system table rows, and DefenseFinder HMM/rule "
                "coverage before minting narrower Reve mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "de Sousa et al. support Reve as one of the novel "
                "single-gene P4-encoded systems with experimental "
                "phage-protection activity, and the pinned DefenseFinder "
                "article registry maps the Reve source key to the "
                "corresponding preprint. The pinned HMM inventory and "
                "rules table have no exact Reve rows, and this first-pass "
                "record does not resolve the tested source locus, complete "
                "phage breadth, exact trigger, molecular output, or "
                "detection rule."
            ),
            "evidence": [
                {
                    "reference": DE_SOUSA,
                    "snippet": (
                        "The Reve system is another single-gene system, "
                        "with ATPase and KAP family P-loop domains"
                    ),
                    "notes": (
                        "de Sousa et al. support Reve as a named "
                        "single-gene defense system while leaving exact "
                        "mechanism for separate review."
                    ),
                },
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#reve_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
        }
    ],
}


def write_new_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Reve system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
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
            "Reviewed Reve system canonical_examples and left them empty "
            "because de Sousa et al. support P4-encoded Reve phage "
            "protection and a DefenseFinder article-registry row, but "
            "not a direct named native microbial isolate exemplar with "
            "experimentally verified endogenous Reve activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_new_record(apply=args.apply)


if __name__ == "__main__":
    main()
