#!/usr/bin/env python3
"""Add the RosmerTA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rosmerta_system.yaml"

MILLMAN = "DOI:10.1016/j.chom.2022.09.017"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)
DEFENSEFINDER_RULES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/DefenseFinder_rules.tsv"
)
DEFENSEFINDER_HMMS = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/Liste_hmm_system.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-18T23:49:00Z"

PROFILES = ("RmrA_2585209417", "RmrT_2585209417")


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"RosmerTA__{profile}"
    short = profile.split("_", maxsplit=1)[0]
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<49} | {hmm:<49} | RosmerTA",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{short} as a RosmerTA profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000256",
    "label": "RosmerTA system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-component RosmerTA locus represented by RmrA and RmrT profiles "
        "that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": MILLMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "RosmerTA",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": MILLMAN,
            "snippet": (
                "discovery of 21 defense systems that protect bacteria from "
                "phages, based on computational genomic analyses and "
                "phage-infection experiments"
            ),
            "notes": (
                "Millman et al. report the computational and experimental "
                "cohort that DefenseFinder cites for RosmerTA as a bacterial "
                "anti-phage system."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "RosmerTA | 10\\.1016/j\\.chom\\.2022\\.09\\.017 | An "
                "expanded arsenal of immune systems that protect bacteria "
                "from phages"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named RosmerTA "
                "system to the Millman et al. antiphage-system discovery "
                "paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": (
                "RosmerTA\tRosmerTA\t2\t2\tRosmerTA__RmrA_2585209417, "
                "RosmerTA__RmrT_2585209417"
            ),
            "notes": (
                "The DefenseFinder rules table models RosmerTA with RmrA "
                "and RmrT profiles."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "rosmerta_locus_restricts_phage",
            "title": "RosmerTA loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "RosmerTA locus to restricted bacteriophage propagation "
                "without asserting the unresolved phage trigger or molecular "
                "output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures RosmerTA as a named anti-phage system "
                "with DefenseFinder RmrA and RmrT profile choices while "
                "leaving its phage trigger, molecular substrate, antiviral "
                "effector output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rosmerta_locus",
                    "label": "RosmerTA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A RosmerTA anti-phage defense locus satisfying a "
                        "DefenseFinder rule over RmrA and RmrT profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the RosmerTA system."
                    ),
                },
                {
                    "node_id": "rosmerta_system_trait",
                    "label": "RosmerTA system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000256",
                    "description": (
                        "Possession of a genome-encoded RosmerTA "
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
                    "subject": "rosmerta_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps RosmerTA to a bacterial "
                        "anti-phage-system discovery paper and represents "
                        "RosmerTA loci through RmrA and RmrT component "
                        "profiles."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "discovery of 21 defense systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "Millman et al. describe the anti-phage "
                                "discovery cohort that the DefenseFinder "
                                "RosmerTA registry row maps to the RosmerTA "
                                "system."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "RosmerTA | 10\\.1016/j\\.chom\\.2022\\.09\\.017 "
                                "| An expanded arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "The DefenseFinder registry maps RosmerTA "
                                "itself to the Millman et al. bacterial "
                                "antiphage-system discovery paper."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": (
                                "RosmerTA\tRosmerTA\t2\t2\t"
                                "RosmerTA__RmrA_2585209417, "
                                "RosmerTA__RmrT_2585209417"
                            ),
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "RmrA and RmrT as RosmerTA system profile "
                                "choices."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "rosmerta_system_trait",
                    "description": (
                        "RosmerTA-mediated phage restriction realizes the "
                        "RosmerTA system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "discovery of 21 defense systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "Millman et al. place the RosmerTA discovery "
                                "cohort in the set of bacterial systems that "
                                "protect against phages."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "RosmerTA | 10\\.1016/j\\.chom\\.2022\\.09\\.017 "
                                "| An expanded arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder records RosmerTA as a named "
                                "system from the Millman et al. antiphage "
                                "discovery paper."
                            ),
                        },
                    ],
                },
                {
                    "subject": "rosmerta_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "RosmerTA system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "An expanded arsenal of immune systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder associates RosmerTA with the "
                                "Millman et al. bacterial antiphage-system "
                                "discovery paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rosmerta-mechanism-gap",
            "prompt": (
                "Resolve RosmerTA phage triggers and effector outputs "
                "before minting narrower RosmerTA mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Millman et al. and DefenseFinder support RosmerTA as a "
                "named anti-phage system with RmrA and RmrT profile "
                "choices, but the trigger, molecular substrate, antiviral "
                "effector output, and subtype-specific mechanism are not "
                "resolved enough here to assert a narrower mechanistic child "
                "trait."
            ),
            "attaches_to": ["causal_graphs#rosmerta_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
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
            "Minted RosmerTA system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is reserved "
            "in proposals/metpo_traitmech_v133."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
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
