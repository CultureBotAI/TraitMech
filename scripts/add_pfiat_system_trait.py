#!/usr/bin/env python3
"""Add the PfiAT system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pfiat_system.yaml"

LI = "DOI:10.1111/1751-7915.13570"
LI_PMID = "PMID:32246813"
PFIAT_TA_PAIR_SNIPPET = (
    "we provided experimental evidence to demonstrate that PA0729 and the "
    "upstream ORF Rorf0727 near the right attachment site of Pf4 form a type "
    "II toxin/antitoxin (TA) pair."
)
PFIT_INHIBITION_SNIPPET = (
    "Importantly, we found that the deletion of the toxin gene PA0729 greatly "
    "increased Pf4 phage production."
)
PFIA_PFIT_RENAME_SNIPPET = (
    "We thus suggest the toxin PA0729 be named PfiT for Pf4 inhibition toxin "
    "and Rorf0727 be named PfiA for PfiT antitoxin."
)
PFIAT_REGULATION_SNIPPET = (
    "Therefore, this study reveals that the TA systems in Pf prophages can "
    "regulate phage production and phage immunity, providing new insights "
    "into the function of TAs in mobile genetic elements."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-22T12:25:36Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-22T12:25:37Z"
IDENTIFIER = "traitmech:000365"
PROPOSAL = "proposals/metpo_traitmech_v242"
SLUG = "pfiat"

ARTICLE_REGISTRY_SNIPPET = (
    "PfiAT | 10\\.1111/1751-7915\\.13570 | Prophage encoding "
    "toxin/antitoxin system PfiT/PfiA inhibits Pf4 production in "
    "Pseudomonas aeruginosa"
)
RULES_SNIPPET = "PfiAT\tPfiAT\t2\t2\tPfiAT__PfiA, PfiAT__PfiT\t\t\t"
HMM_ROWS = {
    "PfiAT__PfiA": (
        "| PfiAT__PfiA                                      | "
        "PfiAT__PfiA                                      | "
        "PfiAT                  | Custom                  | 20     |"
    ),
    "PfiAT__PfiT": (
        "| PfiAT__PfiT                                      | "
        "PfiAT__PfiT                                      | "
        "PfiAT                  | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PfiAT "
            "system to Li et al.'s Pf4 prophage PfiT/PfiA paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PfiAT as a two-profile "
            "system requiring the PfiAT__PfiA and PfiAT__PfiT profiles."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": f"The DefenseFinder HMM inventory records {profile} under PfiAT.",
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PfiAT system",
    "definition": (
        "A phage defense system in which an organism possesses a Pf4 "
        "prophage-encoded PfiAT toxin-antitoxin locus represented by "
        "DefenseFinder as a two-profile model requiring PfiAT__PfiA and "
        "PfiAT__PfiT."
    ),
    "definition_source": LI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PfiAT",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
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
        {
            "reference": LI_PMID,
            "snippet": PFIAT_TA_PAIR_SNIPPET,
            "notes": (
                "Li et al. experimentally identify PA0729 and Rorf0727 in "
                "the Pf4 prophage as a PfiT/PfiA type II toxin-antitoxin "
                "pair."
            ),
        },
        {
            "reference": LI_PMID,
            "snippet": PFIT_INHIBITION_SNIPPET,
            "notes": (
                "Li et al. show that deleting pfiT increases Pf4 phage "
                "production."
            ),
        },
        {
            "reference": LI_PMID,
            "snippet": PFIA_PFIT_RENAME_SNIPPET,
            "notes": (
                "Li et al. name PA0729 as PfiT and Rorf0727 as PfiA."
            ),
        },
        {
            "reference": LI_PMID,
            "snippet": PFIAT_REGULATION_SNIPPET,
            "notes": (
                "Li et al. frame Pf prophage toxin-antitoxin systems as "
                "regulators of phage production and phage immunity."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pfiat_locus_regulates_pf4_phage",
            "title": "PfiAT loci regulate Pf4 prophage production",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PfiAT locus to PfiT/PfiA-dependent regulation of Pf4 "
                "phage production and immunity without asserting the "
                "cellular PfiT toxin target or natural host breadth."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PfiAT as a named DefenseFinder "
                "two-profile Pf prophage system while leaving natural host "
                "breadth, the cellular target of PfiT in Pseudomonas, Pf4 "
                "phage-immunity coupling, and PfiAT profile-to-activity "
                "mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pfiat_locus",
                    "label": "PfiAT locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Pf prophage-encoded PfiAT toxin-antitoxin locus "
                        "represented by PfiAT__PfiA and PfiAT__PfiT "
                        "profiles."
                    ),
                },
                {
                    "node_id": "pf4_phage_production_regulation",
                    "label": "Pf4 phage production regulation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Regulation of Pf4 phage production and Pf4 phage "
                        "immunity by a prophage-encoded PfiT/PfiA "
                        "toxin-antitoxin pair."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PfiAT system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PfiAT "
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
                    "subject": "pfiat_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pf4_phage_production_regulation",
                    "description": (
                        "Li et al. identify the Pf4 PA0729 and Rorf0727 "
                        "locus as a PfiT/PfiA toxin-antitoxin pair whose "
                        "pfiT toxin gene inhibits Pf4 production, and "
                        "DefenseFinder models PfiAT as a two-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": LI_PMID,
                            "snippet": PFIAT_TA_PAIR_SNIPPET,
                            "notes": (
                                "Li et al. experimentally identify PA0729 "
                                "and Rorf0727 as a PfiT/PfiA "
                                "toxin-antitoxin pair near the right "
                                "attachment site of Pf4."
                            ),
                        },
                        {
                            "reference": LI_PMID,
                            "snippet": PFIT_INHIBITION_SNIPPET,
                            "notes": (
                                "Li et al. show that pfiT inhibits Pf4 "
                                "phage production."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "pf4_phage_production_regulation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "PfiT/PfiA-dependent regulation of Pf4 phage "
                        "production and immunity realizes the PfiAT system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": LI_PMID,
                            "snippet": PFIAT_REGULATION_SNIPPET,
                            "notes": (
                                "Li et al. support Pf prophage "
                                "toxin-antitoxin systems as regulators of "
                                "phage production and phage immunity."
                            ),
                        }
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "PfiAT system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pfiat-mechanism-gap",
            "prompt": (
                "Resolve natural PfiAT host breadth, the PfiT cellular "
                "target in Pseudomonas, Pf prophage production and "
                "immunity coupling, and PfiAT profile-to-activity mapping "
                "before minting narrower PfiAT mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Li et al. support PA0729/PfiT and Rorf0727/PfiA in the "
                "Pf4 prophage as a type II toxin-antitoxin pair that "
                "regulates Pf4 production and phage immunity, and "
                "DefenseFinder models PfiAT as a two-profile system with "
                "PfiAT__PfiA and PfiAT__PfiT markers. Natural host breadth, "
                "the cellular target of PfiT, Pf4 immunity coupling, and "
                "profile-to-activity mapping remain unresolved."
            ),
            "evidence": [
                {
                    "reference": LI_PMID,
                    "snippet": (
                        "Homologs of PfiT are also found in other "
                        "Pseudomonas strains, and the cellular target of "
                        "PfiT in Pseudomonas will be investigated in future "
                        "studies."
                    ),
                    "notes": (
                        "Li et al. explicitly leave the PfiT cellular "
                        "target unresolved."
                    ),
                }
            ],
            "attaches_to": ["causal_graphs#pfiat_locus_regulates_pf4_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-22",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted PfiAT system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
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
            "Reviewed the PfiAT canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports the "
            "Pf4 prophage PfiT/PfiA toxin-antitoxin pair, its control of "
            "Pf4 phage production and immunity, and the pinned DefenseFinder "
            "PfiAT profiles, but does not cite a directly observed natural "
            "microbial taxon with a source-backed PfiAT locus broad enough "
            "for a canonical example. No paid research was used."
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
