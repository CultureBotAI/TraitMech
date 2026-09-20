#!/usr/bin/env python3
"""Add the Butters gp30-gp31 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "butters_gp30_gp31_system.yaml"

MAGEENEY = "DOI:10.1128/mSystems.00534-20"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T01:32:52Z"

IDENTIFIER = "traitmech:000298"
SYSTEM = "Butters gp30-gp31"
DEFENSEFINDER_SYSTEM = "Butters_gp30_gp31"
SLUG = "butters_gp30_gp31"
GP30_PROFILE = "Butters_gp30_gp31__Butters_gp30"
GP31_PROFILE = "Butters_gp30_gp31__Butters_gp31"
RULES_SNIPPET = (
    "Butters_gp30_gp31\tButters_gp30_gp31\t2\t2\t"
    "Butters_gp30_gp31__Butters_gp30, "
    "Butters_gp30_gp31__Butters_gp31"
)
PROPOSAL = "proposals/metpo_traitmech_v175"


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{profile:<48} | {profile:<48} | {DEFENSEFINDER_SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records a Butters gp30-gp31 "
            f"profile for {profile} in the Butters_gp30_gp31 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Butters_gp30_gp31 as a "
            "two-component system requiring Butters_gp30 and Butters_gp31 "
            "profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": f"{SYSTEM} system",
    "definition": (
        f"A phage defense system in which an organism possesses a {SYSTEM} "
        "locus that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": MAGEENEY,
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
            "reference": MAGEENEY,
            "snippet": (
                "we unveil a novel defense mechanism in cluster N prophage "
                "Butters"
            ),
            "notes": (
                "Mageeney et al. identify the Butters prophage as encoding a "
                "new heterotypic phage-defense mechanism."
            ),
        },
        {
            "reference": MAGEENEY,
            "snippet": (
                "we show that Butters genes located in the central region of "
                "the genome play a key role in the defense against "
                "heterotypic viral attack"
            ),
            "notes": (
                "Mageeney et al. support central Butters genes as contributors "
                "to prophage-mediated antiviral defense."
            ),
        },
        {
            "reference": MAGEENEY,
            "snippet": (
                "Our study suggests that a two-component system, articulated "
                "by interactions between protein products of genes 30 and 31, "
                "confers defense against heterotypic phage infection by "
                "PurpleHaze (cluster A/subcluster A3) or Alma (cluster "
                "A/subcluster A9)"
            ),
            "notes": (
                "Mageeney et al. connect Butters genes 30 and 31 to a "
                "two-component system that defends against PurpleHaze and "
                "Alma phage infection."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Butters_gp30_gp31 | 10\\.1128/mSystems\\.00534-20 | "
                "Mycobacterium phage Butters-encoded proteins contribute to "
                "host defense against viral attack"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "Butters_gp30_gp31 system to the Mageeney et al. "
                "Butters-defense paper."
            ),
        },
        hmm_inventory_evidence(GP30_PROFILE),
        hmm_inventory_evidence(GP31_PROFILE),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Butters gp30-gp31 loci confer heterotypic phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Butters gp30-gp31 locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "gp31 modulatory role, or downstream arrest mechanism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Butters gp30-gp31 as a named anti-phage "
                "system with DefenseFinder Butters gp30 and gp31 profiles "
                "while leaving the direct phage trigger, the biochemical "
                "action of gp30, the modulatory role of gp31, and the "
                "Island3-targeting gp30-independent mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Butters gp30-gp31 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Butters gp30-gp31 anti-phage defense locus "
                        "cataloged in DefenseFinder with Butters gp30 and "
                        "gp31 HMM profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Butters gp30-gp31 system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Butters gp30-gp31 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Butters gp30-gp31 "
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
                        "Mageeney et al. show that Butters genes in the "
                        "central genome region contribute to defense against "
                        "heterotypic viral attack, and DefenseFinder catalogs "
                        "Butters_gp30 and Butters_gp31 profiles in the "
                        "Butters_gp30_gp31 model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": MAGEENEY,
                            "snippet": (
                                "we show that Butters genes located in the "
                                "central region of the genome play a key role "
                                "in the defense against heterotypic viral "
                                "attack"
                            ),
                            "notes": (
                                "Mageeney et al. support Butters central "
                                "genes as effectors of heterotypic viral "
                                "defense."
                            ),
                        },
                        hmm_inventory_evidence(GP30_PROFILE),
                        hmm_inventory_evidence(GP31_PROFILE),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Butters-gp30-gp31-associated restriction of phage "
                        "propagation realizes the Butters gp30-gp31 system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": MAGEENEY,
                            "snippet": (
                                "Our study suggests that a two-component "
                                "system, articulated by interactions between "
                                "protein products of genes 30 and 31, "
                                "confers defense against heterotypic phage "
                                "infection by PurpleHaze (cluster "
                                "A/subcluster A3) or Alma (cluster "
                                "A/subcluster A9)"
                            ),
                            "notes": (
                                "Mageeney et al. support Butters gp30 and "
                                "gp31 as a two-component system that can "
                                "defend against PurpleHaze or Alma infection."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Butters_gp30_gp31 | "
                                "10\\.1128/mSystems\\.00534-20 | "
                                "Mycobacterium phage Butters-encoded "
                                "proteins contribute to host defense against "
                                "viral attack"
                            ),
                            "notes": (
                                "DefenseFinder records Butters_gp30_gp31 as a "
                                "named system from the Mageeney et al. "
                                "Butters-defense paper."
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
                        "Butters gp30-gp31 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Butters_gp30_gp31 | "
                                "10\\.1128/mSystems\\.00534-20 | "
                                "Mycobacterium phage Butters-encoded "
                                "proteins contribute to host defense against "
                                "viral attack |"
                            ),
                            "notes": (
                                "DefenseFinder associates Butters_gp30_gp31 "
                                "with the Mageeney et al. Butters "
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
                "Resolve the Butters gp30 biochemical output, the gp31 "
                "modulatory role, the gp30-gp31 stoichiometry, the direct "
                "PurpleHaze or Alma trigger, the Island3 gp30-independent "
                "defense, and homolog breadth before minting narrower "
                "Butters gp30-gp31 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mageeney et al. and DefenseFinder support Butters "
                "gp30-gp31 as a named anti-phage system with Butters gp30 "
                "and gp31 profiles, but the direct phage trigger, gp30 "
                "biochemical output, gp31 modulatory activity, stoichiometry "
                "of the possible gp30-gp31 complex, gp30-independent "
                "Island3-targeting defense, and relationship to CarolAnn and "
                "Sbash homologous systems are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
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
            "Minted Butters gp30-gp31 system as a DOI-backed GENOMICS "
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
