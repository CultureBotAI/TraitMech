#!/usr/bin/env python3
"""Add the Eleos system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "eleos_system.yaml"

MILLMAN = "DOI:10.1016/j.chom.2022.09.017"
MILLMAN_PREPRINT = "DOI:10.1101/2022.05.11.491447"

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
TIMESTAMP = "2026-09-18T20:38:41Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000250",
    "label": "Eleos system",
    "definition": (
        "A phage defense system in which an organism possesses an Eleos "
        "locus represented by LeoA, LeoB, LeoBC, and LeoC profiles that "
        "can protect bacteria from bacteriophage infection."
    ),
    "definition_source": MILLMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Eleos",
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
                "cohort that DefenseFinder cites for Eleos as a bacterial "
                "anti-phage system."
            ),
        },
        {
            "reference": MILLMAN_PREPRINT,
            "snippet": (
                "discovery of 21 new defense systems that protect bacteria "
                "from phages, based on computational genomic analyses and "
                "phage infection experiments"
            ),
            "notes": (
                "The bioRxiv version of Millman et al. independently carries "
                "the 21-system discovery claim linked from DefenseFinder's "
                "Eleos article registry."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Eleos | 10\\.1101/2022\\.05\\.11\\.491447 | An "
                "expanding arsenal of immune systems that protect bacteria "
                "from phages"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named Eleos "
                "system to the Millman et al. antiphage-system discovery "
                "preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": (
                "Eleos\tEleos\t2\t2\tEleos__LeoA, Eleos__LeoB, "
                "Eleos__LeoBC, Eleos__LeoC"
            ),
            "notes": (
                "The DefenseFinder rules table models Eleos as a two-gene "
                "system over LeoA, LeoB, LeoBC, and LeoC mandatory-profile "
                "choices."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "Eleos__LeoA                                      | "
                "Eleos__LeoA                                      | Eleos"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records LeoA as an Eleos "
                "profile."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "Eleos__LeoA2                                     | "
                "Eleos__LeoA2                                     | Eleos"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records an additional "
                "LeoA profile for Eleos."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "Eleos__LeoB                                      | "
                "Eleos__LeoB                                      | Eleos"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records LeoB as an Eleos "
                "profile."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "Eleos__LeoBC                                     | "
                "Eleos__LeoBC                                     | Eleos"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records LeoBC as an Eleos "
                "profile."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "Eleos__LeoC                                      | "
                "Eleos__LeoC                                      | Eleos"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records LeoC as an Eleos "
                "profile."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "eleos_locus_restricts_phage",
            "title": "Eleos loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "Eleos locus to restricted bacteriophage propagation without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Eleos as a named anti-phage system with "
                "DefenseFinder LeoA, LeoB, LeoBC, and LeoC profiles while "
                "leaving its phage trigger, molecular substrate, antiviral "
                "effector output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "eleos_locus",
                    "label": "Eleos locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An Eleos anti-phage defense locus satisfying a "
                        "two-profile DefenseFinder rule over LeoA, LeoB, "
                        "LeoBC, and LeoC profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Eleos system."
                    ),
                },
                {
                    "node_id": "eleos_system_trait",
                    "label": "Eleos system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000250",
                    "description": (
                        "Possession of a genome-encoded Eleos phage-defense "
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
                    "subject": "eleos_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps Eleos to a bacterial "
                        "anti-phage-system discovery preprint and represents "
                        "Eleos loci through LeoA, LeoB, LeoBC, and LeoC "
                        "component profiles."
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
                                "Eleos registry row maps to the Eleos "
                                "system."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Eleos | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "The DefenseFinder registry maps Eleos "
                                "itself to the Millman et al. bacterial "
                                "antiphage-system discovery preprint."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": (
                                "Eleos\tEleos\t2\t2\tEleos__LeoA, "
                                "Eleos__LeoB, Eleos__LeoBC, Eleos__LeoC"
                            ),
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "LeoA, LeoB, LeoBC, and LeoC as Eleos "
                                "system profile choices."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "eleos_system_trait",
                    "description": (
                        "Eleos-mediated phage restriction realizes the Eleos "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "discovery of 21 defense systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "Millman et al. place the Eleos discovery "
                                "cohort in the set of bacterial systems that "
                                "protect against phages."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Eleos | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder records Eleos as a named "
                                "system from the Millman et al. antiphage "
                                "discovery preprint."
                            ),
                        },
                    ],
                },
                {
                    "subject": "eleos_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Eleos system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "An expanding arsenal of immune systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder associates Eleos with the "
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
            "discussion_id": "eleos-mechanism-gap",
            "prompt": (
                "Resolve Eleos phage triggers and effector outputs before "
                "minting narrower Eleos mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Millman et al. and DefenseFinder support Eleos as a named "
                "anti-phage system with LeoA, LeoB, LeoBC, and LeoC "
                "profiles, but the trigger, molecular substrate, antiviral "
                "effector output, and subtype-specific mechanism are not "
                "resolved enough here to assert a narrower mechanistic "
                "child trait."
            ),
            "attaches_to": ["causal_graphs#eleos_locus_restricts_phage"],
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
            "Minted Eleos system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v127."
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
