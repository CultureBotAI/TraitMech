#!/usr/bin/env python3
"""Add the Phrann gp29-gp30 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "phrann_gp29_gp30_system.yaml"

DEDRICK = "DOI:10.1038/nmicrobiol.2016.251"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T23:37:58Z"
REVIEW_TIMESTAMP = "2026-09-19T23:47:14Z"

IDENTIFIER = "traitmech:000296"
SYSTEM = "Phrann gp29-gp30"
DEFENSEFINDER_SYSTEM = "Phrann_gp29_gp30"
SLUG = "phrann_gp29_gp30"
GP29_PROFILE = "Phrann_gp29_gp30__gp29"
GP30_PROFILE = "Phrann_gp29_gp30__gp30"
RULES_SNIPPET = (
    "Phrann_gp29_gp30\tPhrann_gp29_gp30\t2\t2\t"
    "Phrann_gp29_gp30__gp29, Phrann_gp29_gp30__gp30"
)
PROPOSAL = "proposals/metpo_traitmech_v173"


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{profile:<48} | {profile:<48} | {DEFENSEFINDER_SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records a Phrann gp29-gp30 "
            f"profile for {profile} in the Phrann_gp29_gp30 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Phrann_gp29_gp30 as a "
            "two-component system requiring gp29 and gp30 profiles."
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
                "Dedrick et al. place the Cluster N Phrann gp29-gp30 system "
                "in a cohort of prophage-expressed defenses against lytic and "
                "temperate mycobacteriophages."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "Phrann genes 29 and/or 30 are involved in defense against "
                "Tweety and Gaia, as a mutant lysogen lacking Phrann 29 loses "
                "defense against these phages"
            ),
            "notes": (
                "Dedrick et al. localize part of the Phrann prophage-mediated "
                "heterotypic defense phenotype to genes 29 and 30."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "expressing Phrann genes 29 and 30 reproduce the Phrann "
                "defense against Tweety and Gaia"
            ),
            "notes": (
                "Dedrick et al. show that recombinant Phrann genes 29 and 30 "
                "are sufficient to reproduce Phrann defense against Tweety "
                "and Gaia."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "Phrann prophage-mediated defense is strictly heterotypic, "
                "and Phrann gp29/gp30 does not defend against Phrann or other "
                "Cluster N phages"
            ),
            "notes": (
                "Dedrick et al. delimit the Phrann gp29-gp30 defense profile "
                "as heterotypic rather than Cluster N superinfection "
                "exclusion."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "Prophage-mediated defense by (p)ppGpp synthetases is a new "
                "and intriguing system for defense against viral attack"
            ),
            "notes": (
                "Dedrick et al. interpret Phrann gp29 as a putative "
                "(p)ppGpp synthetase in a prophage-mediated viral-defense "
                "system."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Phrann_gp29_gp30 | 10\\.1038/nmicrobiol\\.2016\\.251 | "
                "Prophage-mediated defence against viral attack and viral "
                "counter-defence"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "Phrann_gp29_gp30 system to the Dedrick et al. "
                "prophage-mediated viral-defense paper."
            ),
        },
        hmm_inventory_evidence(GP29_PROFILE),
        hmm_inventory_evidence(GP30_PROFILE),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Phrann gp29-gp30 loci confer heterotypic phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Phrann gp29-gp30 locus to restricted bacteriophage "
                "propagation without asserting the unresolved lytic trigger, "
                "gp29-gp30 interaction, or downstream arrest mechanism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Phrann gp29-gp30 as a named anti-phage "
                "system with DefenseFinder gp29 and gp30 profiles while "
                "leaving the direct lytic trigger, Phrann gp30 regulatory "
                "role, and exact (p)ppGpp-linked arrest mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Phrann gp29-gp30 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Phrann gp29-gp30 anti-phage defense locus "
                        "cataloged in DefenseFinder with gp29 and gp30 HMM "
                        "profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Phrann gp29-gp30 system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Phrann gp29-gp30 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Phrann gp29-gp30 "
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
                        "Dedrick et al. support Phrann genes 29 and 30 in "
                        "heterotypic phage defense, and DefenseFinder "
                        "catalogs gp29 and gp30 profiles in the "
                        "Phrann_gp29_gp30 model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "Phrann genes 29 and/or 30 are involved in "
                                "defense against Tweety and Gaia, as a mutant "
                                "lysogen lacking Phrann 29 loses defense "
                                "against these phages"
                            ),
                            "notes": (
                                "Dedrick et al. connect Phrann genes 29 and "
                                "30 to Phrann defense against Tweety and Gaia."
                            ),
                        },
                        hmm_inventory_evidence(GP29_PROFILE),
                        hmm_inventory_evidence(GP30_PROFILE),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Phrann-gp29-gp30-mediated defense against Tweety and "
                        "Gaia realizes the Phrann gp29-gp30 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "expressing Phrann genes 29 and 30 reproduce "
                                "the Phrann defense against Tweety and Gaia"
                            ),
                            "notes": (
                                "Dedrick et al. show that genes 29 and 30 are "
                                "sufficient to reproduce Phrann defense "
                                "against Tweety and Gaia."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Phrann_gp29_gp30 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence"
                            ),
                            "notes": (
                                "DefenseFinder records Phrann_gp29_gp30 as a "
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
                        "Phrann gp29-gp30 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Phrann_gp29_gp30 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence |"
                            ),
                            "notes": (
                                "DefenseFinder associates Phrann_gp29_gp30 "
                                "with the Dedrick et al. prophage-mediated "
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
                "Resolve the Phrann gp29-gp30 contribution to TM4 defense, "
                "Phrann gp30 regulator role, lytic trigger, (p)ppGpp "
                "synthetase activity, and remaining target-phage breadth "
                "before minting narrower Phrann gp29-gp30 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dedrick et al. and DefenseFinder support Phrann gp29-gp30 as "
                "a named anti-phage system with gp29 and gp30 profiles, but "
                "the Phrann gp30 regulatory role, lytic-phage trigger, direct "
                "(p)ppGpp activation mechanism, relative contribution to TM4 "
                "defense, and remaining target breadth are not resolved enough "
                "here to assert a narrower mechanistic child trait."
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
            "Minted Phrann gp29-gp30 system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Resolved PR #1092 review issues #1093 and #1094 by replacing a "
            "restriction-implying Phrann gp29-gp30 edge description with "
            "generic defense wording and narrowing the breadth knowledge gap "
            "to the unresolved TM4 contribution and remaining target-phage "
            "breadth."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
