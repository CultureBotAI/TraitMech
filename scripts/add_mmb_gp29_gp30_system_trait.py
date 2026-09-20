#!/usr/bin/env python3
"""Add the MMB gp29-gp30 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mmb_gp29_gp30_system.yaml"

DEDRICK = "DOI:10.1038/nmicrobiol.2016.251"
DEDRICK_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5508108/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T00:13:48Z"

IDENTIFIER = "traitmech:000297"
SYSTEM = "MMB gp29-gp30"
DEFENSEFINDER_SYSTEM = "MMB_gp29_gp30"
SLUG = "mmb_gp29_gp30"
GP29_PROFILE = "MMB_gp29_gp30__gp29"
GP30_PROFILE = "MMB_gp29_gp30__gp30"
RULES_SNIPPET = (
    "MMB_gp29_gp30\tMMB_gp29_gp30\t2\t2\t"
    "MMB_gp29_gp30__gp29, MMB_gp29_gp30__gp30"
)
PROPOSAL = "proposals/metpo_traitmech_v174"


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{profile:<48} | {profile:<48} | {DEFENSEFINDER_SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records an MMB gp29-gp30 "
            f"profile for {profile} in the MMB_gp29_gp30 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models MMB_gp29_gp30 as a "
            "two-component system requiring gp29 and gp30 profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": f"{SYSTEM} system",
    "definition": (
        f"A phage defense system in which an organism possesses an {SYSTEM} "
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
            "reference": DEDRICK_PMC,
            "snippet": (
                "at least five distinct prophage-expressed viral defense "
                "systems that interfere with infection"
            ),
            "notes": (
                "Dedrick et al. place the Cluster N MMB gp29-gp30 system in "
                "a cohort of prophage-expressed defenses against lytic and "
                "temperate mycobacteriophages."
            ),
        },
        {
            "reference": DEDRICK_PMC,
            "snippet": "Tweety (F1) is targeted by Xerxes, MMB, Phrann and Panchino",
            "notes": (
                "Dedrick et al. identify Tweety as one phage targeted by the "
                "MichelleMyBell prophage defense profile."
            ),
        },
        {
            "reference": DEDRICK_PMC,
            "snippet": (
                "Phages MMB, Xerxes, and Pipsqueaks are closely-related in "
                "the lysis-immunity region (Fig. 4a) and MMB and Xerxes "
                "have almost identical patterns of defense against eleven "
                "individual phages"
            ),
            "notes": (
                "Dedrick et al. connect the MichelleMyBell and Xerxes "
                "defense spectra to their shared lysis-immunity-region "
                "context."
            ),
        },
        {
            "reference": DEDRICK_PMC,
            "snippet": (
                "we constructed a MMB mutant in which genes 29 and 30 are "
                "removed (deletions of individual genes appear to generate "
                "non-viable mutants; Supplementary Table 3) and showed that "
                "prophage-mediated defense is lost"
            ),
            "notes": (
                "Dedrick et al. deleted the MMB 29-30 interval when testing "
                "whether gp29 and gp30 contribute to MMB defense."
            ),
        },
        {
            "reference": DEDRICK_PMC,
            "snippet": (
                "expressing MMB 29 and 30 confers the same pattern of "
                "defense as the MMB lysogen"
            ),
            "notes": (
                "Dedrick et al. show that recombinant MMB genes 29 and 30 "
                "reproduce the MMB prophage-mediated defense pattern."
            ),
        },
        {
            "reference": DEDRICK_PMC,
            "snippet": (
                "MMB 29-30 and Phrann 29-30 also confer survival to infection "
                "by a lytic Tweety derivative"
            ),
            "notes": (
                "Dedrick et al. show that the MMB gp29-gp30 system can "
                "protect bacteria from a lytic Tweety derivative in addition "
                "to wild-type Tweety."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "MMB_gp29_gp30 | 10\\.1038/nmicrobiol\\.2016\\.251 | "
                "Prophage-mediated defence against viral attack and viral "
                "counter-defence"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "MMB_gp29_gp30 system to the Dedrick et al. "
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
            "title": "MMB gp29-gp30 loci confer heterotypic phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "MMB gp29-gp30 locus to restricted bacteriophage propagation "
                "without asserting the unresolved lytic trigger, gp29-gp30 "
                "interaction, or downstream arrest mechanism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures MMB gp29-gp30 as a named anti-phage "
                "system with DefenseFinder gp29 and gp30 profiles while "
                "leaving the direct lytic trigger, MMB gp30 regulatory role, "
                "MMB gp29 biochemical activity, and exact downstream arrest "
                "mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "MMB gp29-gp30 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An MMB gp29-gp30 anti-phage defense locus cataloged "
                        "in DefenseFinder with gp29 and gp30 HMM profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the MMB gp29-gp30 system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "MMB gp29-gp30 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MMB gp29-gp30 "
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
                        "Dedrick et al. show that MMB genes 29 and 30 are "
                        "necessary and sufficient for the tested MMB defense "
                        "profile, and DefenseFinder catalogs gp29 and gp30 "
                        "profiles in the MMB_gp29_gp30 model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK_PMC,
                            "snippet": (
                                "we constructed a MMB mutant in which genes "
                                "29 and 30 are removed (deletions of "
                                "individual genes appear to generate "
                                "non-viable mutants; Supplementary Table 3) "
                                "and showed that prophage-mediated defense "
                                "is lost"
                            ),
                            "notes": (
                                "Dedrick et al. show that deleting the MMB "
                                "29-30 interval abolishes MMB "
                                "prophage-mediated defense."
                            ),
                        },
                        {
                            "reference": DEDRICK_PMC,
                            "snippet": (
                                "expressing MMB 29 and 30 confers the same "
                                "pattern of defense as the MMB lysogen"
                            ),
                            "notes": (
                                "Dedrick et al. show that MMB genes 29 and "
                                "30 are sufficient to reproduce the MMB "
                                "defense pattern."
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
                        "MMB-gp29-gp30-mediated restriction of phage "
                        "propagation realizes the MMB gp29-gp30 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK_PMC,
                            "snippet": (
                                "expressing MMB 29 and 30 confers the same "
                                "pattern of defense as the MMB lysogen"
                            ),
                            "notes": (
                                "Dedrick et al. show that MMB genes 29 and "
                                "30 reproduce the MMB defense pattern."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "MMB_gp29_gp30 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence"
                            ),
                            "notes": (
                                "DefenseFinder records MMB_gp29_gp30 as a "
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
                        "MMB gp29-gp30 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| MMB_gp29_gp30 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence |"
                            ),
                            "notes": (
                                "DefenseFinder associates MMB_gp29_gp30 with "
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
                "Resolve the MMB gp29 biochemical activity, MMB gp30 "
                "regulatory role, lytic trigger, gp29-gp30 interaction, "
                "counter-defense specificity, and homolog breadth before "
                "minting narrower MMB gp29-gp30 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dedrick et al. and DefenseFinder support MMB gp29-gp30 as a "
                "named anti-phage system with gp29 and gp30 profiles, but the "
                "MMB gp29 biochemical activity, direct gp29-gp30 interaction, "
                "triggering Tweety early lytic gene or genes, MMB-specific "
                "counter-defense tuning, and relationship to Squirty "
                "homologs are not resolved enough here to assert a narrower "
                "mechanistic child trait."
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
            "Minted MMB gp29-gp30 system as a DOI-backed GENOMICS "
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
