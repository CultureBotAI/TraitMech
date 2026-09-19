#!/usr/bin/env python3
"""Add the SEFIR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sefir_system.yaml"

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
TIMESTAMP = "2026-09-19T01:51:02Z"

PROFILES = ("bSEFIR",)


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"SEFIR__{profile}"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {hmm:<48} | SEFIR",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{profile} as a SEFIR profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000259",
    "label": "SEFIR system",
    "definition": (
        "A phage defense system in which an organism possesses a SEFIR "
        "locus represented by a bSEFIR profile that can protect bacteria "
        "from bacteriophage infection."
    ),
    "definition_source": MILLMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SEFIR",
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
                "cohort that DefenseFinder cites for SEFIR as a bacterial "
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
                "SEFIR article registry."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "SEFIR | 10\\.1101/2022\\.05\\.11\\.491447 | An expanding "
                "arsenal of immune systems that protect bacteria from phages"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named SEFIR "
                "system to the Millman et al. antiphage-system discovery "
                "preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "SEFIR\tSEFIR\t1\t1\tSEFIR__bSEFIR",
            "notes": (
                "The DefenseFinder rules table models SEFIR with a bSEFIR "
                "profile."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "sefir_locus_restricts_phage",
            "title": "SEFIR loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "SEFIR locus to restricted bacteriophage propagation without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SEFIR as a named anti-phage system with "
                "the required DefenseFinder bSEFIR profile while leaving its "
                "phage trigger, molecular substrate, antiviral effector "
                "output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sefir_locus",
                    "label": "SEFIR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A SEFIR anti-phage defense locus satisfying a "
                        "DefenseFinder rule over the bSEFIR profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the SEFIR system."
                    ),
                },
                {
                    "node_id": "sefir_system_trait",
                    "label": "SEFIR system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000259",
                    "description": (
                        "Possession of a genome-encoded SEFIR phage-defense "
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
                    "subject": "sefir_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps SEFIR to a bacterial "
                        "anti-phage-system discovery preprint and represents "
                        "SEFIR loci through the bSEFIR component profile."
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
                                "SEFIR registry row maps to the SEFIR system."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "SEFIR | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "The DefenseFinder registry maps SEFIR "
                                "itself to the Millman et al. bacterial "
                                "antiphage-system discovery preprint."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": "SEFIR\tSEFIR\t1\t1\tSEFIR__bSEFIR",
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "bSEFIR as the required SEFIR system profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sefir_system_trait",
                    "description": (
                        "SEFIR-mediated phage restriction realizes the "
                        "SEFIR system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "discovery of 21 defense systems that "
                                "protect bacteria from phages"
                            ),
                            "notes": (
                                "Millman et al. place the SEFIR discovery "
                                "cohort in the set of bacterial systems that "
                                "protect against phages."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "SEFIR | 10\\.1101/2022\\.05\\.11\\.491447 "
                                "| An expanding arsenal of immune systems "
                                "that protect bacteria from phages"
                            ),
                            "notes": (
                                "DefenseFinder records SEFIR as a named "
                                "system from the Millman et al. antiphage "
                                "discovery preprint."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sefir_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SEFIR system possession is a phage-defense-system "
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
                                "DefenseFinder associates SEFIR with the "
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
            "discussion_id": "sefir-mechanism-gap",
            "prompt": (
                "Resolve SEFIR phage triggers and effector outputs before "
                "minting narrower SEFIR mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Millman et al. and DefenseFinder support SEFIR as a named "
                "anti-phage system with a bSEFIR profile, but the trigger, "
                "molecular substrate, antiviral effector output, and "
                "subtype-specific mechanism are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": ["causal_graphs#sefir_locus_restricts_phage"],
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
            "Minted SEFIR system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v136."
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
