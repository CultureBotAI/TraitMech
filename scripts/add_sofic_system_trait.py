#!/usr/bin/env python3
"""Add the SoFIC system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sofic_system.yaml"

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
TIMESTAMP = "2026-09-19T02:18:00Z"

PROFILES = ("SoFic",)


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"SoFic__{profile}"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {hmm:<48} | SoFic",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{profile} in the SoFic model namespace for the SoFIC system."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000260",
    "label": "SoFIC system",
    "definition": (
        "A phage defense system in which an organism possesses a SoFIC "
        "locus represented by a SoFic profile that can protect bacteria "
        "from bacteriophage infection."
    ),
    "definition_source": MILLMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SoFIC",
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
                "cohort that DefenseFinder cites for SoFIC as a bacterial "
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
                "SoFIC article registry."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "SoFIC | 10\\.1101/2022\\.05\\.11\\.491447 | An "
                "expanding arsenal of immune systems that protect bacteria "
                "from phages"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named SoFIC "
                "system to the Millman et al. antiphage-system discovery "
                "preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "SoFIC\tSoFic\t1\t1\tSoFic__SoFic",
            "notes": (
                "The DefenseFinder rules table models SoFIC with a SoFic "
                "profile."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "sofic_locus_restricts_phage",
            "title": "SoFIC loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "SoFIC locus to restricted bacteriophage propagation without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SoFIC as a named anti-phage system with "
                "the required DefenseFinder SoFic profile while leaving its "
                "phage trigger, molecular substrate, antiviral effector "
                "output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sofic_locus",
                    "label": "SoFIC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A SoFIC anti-phage defense locus satisfying a "
                        "DefenseFinder rule over the SoFic profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the SoFIC system."
                    ),
                },
                {
                    "node_id": "sofic_system_trait",
                    "label": "SoFIC system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000260",
                    "description": (
                        "Possession of a genome-encoded SoFIC phage-defense "
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
                    "subject": "sofic_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps SoFIC to a bacterial "
                        "anti-phage-system discovery preprint and represents "
                        "SoFIC loci through the SoFic component profile."
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
                                "SoFIC registry row maps to the SoFIC system."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "SoFIC | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "The DefenseFinder registry maps SoFIC "
                                "itself to the Millman et al. bacterial "
                                "antiphage-system discovery preprint."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": "SoFIC\tSoFic\t1\t1\tSoFic__SoFic",
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "SoFic as the required SoFIC system profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sofic_system_trait",
                    "description": (
                        "SoFIC-mediated phage restriction realizes the "
                        "SoFIC system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "discovery of 21 defense systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "Millman et al. place the SoFIC discovery "
                                "cohort in the set of bacterial systems that "
                                "protect against phages."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "SoFIC | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder records SoFIC as a named "
                                "system from the Millman et al. antiphage "
                                "discovery preprint."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sofic_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SoFIC system possession is a phage-defense-system "
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
                                "DefenseFinder associates SoFIC with the "
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
            "discussion_id": "sofic-mechanism-gap",
            "prompt": (
                "Resolve SoFIC phage triggers and effector outputs before "
                "minting narrower SoFIC mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Millman et al. and DefenseFinder support SoFIC as a named "
                "anti-phage system with a SoFic profile, but the trigger, "
                "molecular substrate, antiviral effector output, and "
                "subtype-specific mechanism are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": ["causal_graphs#sofic_locus_restricts_phage"],
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
            "Minted SoFIC system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v137."
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
