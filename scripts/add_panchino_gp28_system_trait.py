#!/usr/bin/env python3
"""Add the Panchino gp28 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "panchino_gp28_system.yaml"

DEDRICK = "DOI:10.1038/nmicrobiol.2016.251"

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
TIMESTAMP = "2026-09-19T21:37:34Z"

IDENTIFIER = "traitmech:000294"
SYSTEM = "Panchino gp28"
DEFENSEFINDER_SYSTEM = "Panchino_gp28"
SLUG = "panchino_gp28"
PROFILE = "gp28"
PROPOSAL = "proposals/metpo_traitmech_v171"


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            "Panchino_gp28__gp28                              | "
            "Panchino_gp28__gp28                              | Panchino_gp28"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records gp28 in the "
            "Panchino_gp28 model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": f"{SYSTEM} system",
    "definition": (
        f"A phage defense system in which an organism possesses a {SYSTEM} "
        "locus that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": DEDRICK,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": DEFENSEFINDER_SYSTEM,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        {
            "reference": DEDRICK,
            "snippet": (
                "at least five distinct prophage-expressed viral defense "
                "systems that interfere with infection"
            ),
            "notes": (
                "Dedrick et al. place the Cluster N Panchino gp28 system in a "
                "cohort of prophage-expressed defenses against lytic and "
                "temperate mycobacteriophages."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "The Panchino restriction system (gp28) is a strong candidate "
                "for conferring this defense"
            ),
            "notes": (
                "Dedrick et al. identify Panchino gp28 as the candidate "
                "restriction system responsible for a heterotypic viral-defense "
                "phenotype."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Panchino_gp28 | 10\\.1038/nmicrobiol\\.2016\\.251 | "
                "Prophage-mediated defence against viral attack and viral "
                "counter-defence"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "Panchino_gp28 system to the Dedrick et al. prophage-mediated "
                "viral-defense paper."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Panchino gp28 loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Panchino gp28 locus to restricted bacteriophage propagation "
                "without asserting the unresolved restriction target, "
                "methylation context, or target-phage breadth."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Panchino gp28 as a named anti-phage "
                "system with a DefenseFinder gp28 profile while leaving its "
                "restriction target, methylation requirements, and "
                "target-phage breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Panchino gp28 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Panchino gp28 anti-phage defense locus cataloged in "
                        "DefenseFinder with a gp28 HMM profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Panchino gp28 system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Panchino gp28 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Panchino gp28 "
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
                    "subject": f"{SLUG}_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Dedrick et al. identify Panchino gp28 as a "
                        "prophage-expressed viral-defense candidate, and "
                        "DefenseFinder catalogs a gp28 profile in the "
                        "Panchino_gp28 model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "The Panchino restriction system (gp28) is a "
                                "strong candidate for conferring this defense"
                            ),
                            "notes": (
                                "Dedrick et al. support Panchino gp28 as the "
                                "candidate system that confers a Panchino "
                                "defense profile."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Panchino-gp28-mediated phage restriction realizes "
                        "the Panchino gp28 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "at least five distinct prophage-expressed "
                                "viral defense systems that interfere with "
                                "infection"
                            ),
                            "notes": (
                                "Dedrick et al. place Panchino gp28 among "
                                "Cluster N prophage systems that defend "
                                "against phage infection."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Panchino_gp28 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence"
                            ),
                            "notes": (
                                "DefenseFinder records Panchino_gp28 as a "
                                "named system from the Dedrick et al. "
                                "prophage-defense paper."
                            ),
                        },
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Panchino gp28 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Panchino_gp28 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence |"
                            ),
                            "notes": (
                                "DefenseFinder associates Panchino_gp28 with "
                                "the Dedrick et al. prophage-mediated "
                                "viral-defense paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": f"{SLUG}-mechanism-gap",
            "prompt": (
                "Resolve the Panchino gp28 restriction target, methylation "
                "requirements, and homolog breadth before minting narrower "
                "Panchino gp28 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dedrick et al. and DefenseFinder support Panchino gp28 as a "
                "named anti-phage system with a gp28 profile, but the "
                "restriction target, methylation context, and full "
                "target-phage breadth are not resolved enough here to assert "
                "a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
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
            "Minted Panchino gp28 system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
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
