#!/usr/bin/env python3
"""Add the Sirona system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sirona_system.yaml"

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
TIMESTAMP = "2026-09-19T04:27:15Z"

PROFILES = ("VCA0356",)
EMPTY_HMM_CUTOFF = ""


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"Sirona__{profile}"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {EMPTY_HMM_CUTOFF:<48} | Sirona",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{profile} in the Sirona model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000264",
    "label": "Sirona system",
    "definition": (
        "A phage defense system in which an organism possesses a Sirona "
        "locus represented by a VCA0356 profile that can protect bacteria "
        "from bacteriophage infection."
    ),
    "definition_source": DARRACQ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Sirona",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "VCA0356",
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
                "Darracq et al. support a nonmechanistic system record that "
                "does not assert a resolved Sirona trigger, effector output, "
                "or pathway."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Sirona | 10\\.1126/science\\.ads0768 | Sedentary "
                "chromosomal integrons as biobanks of bacterial antiphage "
                "defense systems"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named Sirona "
                "system to the Darracq et al. SCI antiphage-system paper."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "sirona_locus_restricts_phage",
            "title": "Sirona loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Sirona locus to restricted bacteriophage propagation without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Sirona as a named SCI-derived "
                "anti-phage system with a VCA0356 DefenseFinder profile while "
                "leaving its phage trigger, molecular substrate, antiviral "
                "effector output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sirona_locus",
                    "label": "Sirona locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Sirona anti-phage defense locus represented in "
                        "DefenseFinder by a VCA0356 profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Sirona system."
                    ),
                },
                {
                    "node_id": "sirona_system_trait",
                    "label": "Sirona system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000264",
                    "description": (
                        "Possession of a genome-encoded Sirona "
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
                    "subject": "sirona_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps Sirona to an SCI "
                        "anti-phage-system discovery paper and represents "
                        "Sirona loci through the VCA0356 component profile."
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
                                "DefenseFinder Sirona registry row maps to "
                                "the Sirona system."
                            ),
                        },
                        {
                            **hmm_inventory_evidence("VCA0356"),
                            "notes": (
                                "The DefenseFinder HMM inventory supports "
                                "VCA0356 as the Sirona component profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sirona_system_trait",
                    "description": (
                        "Sirona-mediated phage restriction realizes the "
                        "Sirona system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DARRACQ,
                            "snippet": (
                                "Most of these novel systems have little or no "
                                "similarity to previously known ones"
                            ),
                            "notes": (
                                "Darracq et al. place the Sirona discovery "
                                "cohort in a set of novel bacterial systems "
                                "that protect against phages."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sirona_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Sirona system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DARRACQ,
                            "snippet": (
                                "We also demonstrate that nearly 10% of the "
                                "integron cassettes in the pandemic Vibrio "
                                "cholerae strain encode novel antiphage "
                                "functions"
                            ),
                            "notes": (
                                "Darracq et al. support treating the Sirona "
                                "source cohort as novel bacterial "
                                "anti-phage systems."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Sirona | 10\\.1126/science\\.ads0768 | "
                                "Sedentary chromosomal integrons as biobanks "
                                "of bacterial antiphage defense systems"
                            ),
                            "notes": (
                                "DefenseFinder associates Sirona with the "
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
            "discussion_id": "sirona-mechanism-gap",
            "prompt": (
                "Resolve Sirona phage triggers and effector outputs before "
                "minting narrower Sirona mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Darracq et al. and DefenseFinder support Sirona as a named "
                "anti-phage system with a VCA0356 profile, but the trigger, "
                "molecular substrate, antiviral effector output, and "
                "subtype-specific mechanism are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": ["causal_graphs#sirona_locus_restricts_phage"],
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
            "Minted Sirona system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v141."
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
