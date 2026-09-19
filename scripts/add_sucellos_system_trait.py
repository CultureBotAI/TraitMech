#!/usr/bin/env python3
"""Add the Sucellos system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sucellos_system.yaml"

DARRACQ = "DOI:10.1126/science.ads0768"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)
DEFENSEFINDER_HMMS = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/Liste_hmm_system.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-19T05:32:39Z"

PROFILES = ("SclA_VCA0367", "SclB_VCA0368")
EMPTY_HMM_NAME = ""


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"Sucellos__{profile}"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {EMPTY_HMM_NAME:<48} | Sucellos",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{profile} in the Sucellos model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000266",
    "label": "Sucellos system",
    "definition": (
        "A phage defense system in which an organism possesses a Sucellos "
        "locus represented by SclA_VCA0367 and SclB_VCA0368 profiles that "
        "can protect bacteria from bacteriophage infection."
    ),
    "definition_source": DARRACQ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Sucellos",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "SclA_VCA0367",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SclB_VCA0368",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": DARRACQ,
            "snippet": (
                "nearly 10% of the integron cassettes in the pandemic "
                "Vibrio cholerae strain encode novel antiphage functions"
            ),
            "notes": (
                "Darracq et al. support treating the newly discovered "
                "Vibrio cholerae SCI antiphage cassettes as bacterial "
                "anti-phage systems."
            ),
        },
        {
            "reference": DARRACQ,
            "snippet": (
                "Most of these novel systems have little or no similarity to "
                "previously known ones, with several providing defense "
                "through cell lysis or growth arrest"
            ),
            "notes": (
                "Darracq et al. support a conservative system record that "
                "does not assert a resolved Sucellos trigger, effector "
                "output, or universal pathway."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Sucellos | 10\\.1126/science\\.ads0768 | Sedentary "
                "chromosomal integrons as biobanks of bacterial antiphage "
                "defense systems"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named Sucellos "
                "system to the Darracq et al. SCI antiphage-system paper."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "sucellos_locus_restricts_phage",
            "title": "Sucellos loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Sucellos locus to restricted bacteriophage propagation "
                "without asserting the unresolved phage trigger or molecular "
                "output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Sucellos as a named SCI-derived "
                "anti-phage system with SclA_VCA0367 and SclB_VCA0368 "
                "DefenseFinder profiles while leaving its phage trigger, "
                "molecular substrate, antiviral effector output, and subtype "
                "breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sucellos_locus",
                    "label": "Sucellos locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Sucellos anti-phage defense locus represented in "
                        "DefenseFinder by SclA_VCA0367 and SclB_VCA0368 "
                        "profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Sucellos system."
                    ),
                },
                {
                    "node_id": "sucellos_system_trait",
                    "label": "Sucellos system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000266",
                    "description": (
                        "Possession of a genome-encoded Sucellos "
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
                    "subject": "sucellos_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps Sucellos to an SCI "
                        "anti-phage-system discovery paper and represents "
                        "Sucellos loci through the SclA_VCA0367 and "
                        "SclB_VCA0368 component profiles."
                    ),
                    "evidence": [
                        {
                            "reference": DARRACQ,
                            "snippet": (
                                "nearly 10% of the integron cassettes in the "
                                "pandemic Vibrio cholerae strain encode novel "
                                "antiphage functions"
                            ),
                            "notes": (
                                "Darracq et al. describe the newly discovered "
                                "antiphage-system cohort that the "
                                "DefenseFinder Sucellos registry row maps to "
                                "the Sucellos system."
                            ),
                        },
                        {
                            **hmm_inventory_evidence("SclA_VCA0367"),
                            "notes": (
                                "The DefenseFinder HMM inventory supports "
                                "SclA_VCA0367 as one Sucellos component "
                                "profile."
                            ),
                        },
                        {
                            **hmm_inventory_evidence("SclB_VCA0368"),
                            "notes": (
                                "The DefenseFinder HMM inventory supports "
                                "SclB_VCA0368 as one Sucellos component "
                                "profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sucellos_system_trait",
                    "description": (
                        "Sucellos-mediated phage restriction realizes the "
                        "Sucellos system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DARRACQ,
                            "snippet": (
                                "Most of these novel systems have little or no "
                                "similarity to previously known ones"
                            ),
                            "notes": (
                                "Darracq et al. place the Sucellos discovery "
                                "cohort in a set of novel bacterial systems "
                                "that protect against phages."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sucellos_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Sucellos system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Sucellos | 10\\.1126/science\\.ads0768 | "
                                "Sedentary chromosomal integrons as biobanks "
                                "of bacterial antiphage defense systems"
                            ),
                            "notes": (
                                "DefenseFinder associates Sucellos with the "
                                "Darracq et al. bacterial antiphage-system "
                                "paper."
                            ),
                        },
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "sucellos-mechanism-gap",
            "prompt": (
                "Resolve Sucellos phage triggers and effector outputs before "
                "minting narrower Sucellos mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Darracq et al. and DefenseFinder support Sucellos as a named "
                "anti-phage system with SclA_VCA0367 and SclB_VCA0368 "
                "profiles, but the trigger, molecular substrate, antiviral "
                "effector output, and subtype-specific mechanism are not "
                "resolved enough here to assert a narrower mechanistic child "
                "trait."
            ),
            "attaches_to": ["causal_graphs#sucellos_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-19",
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
            "Minted Sucellos system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v143."
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
