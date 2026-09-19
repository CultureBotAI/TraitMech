#!/usr/bin/env python3
"""Add the Charlie gp32 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "charlie_gp32_system.yaml"

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
TIMESTAMP = "2026-09-19T22:40:37Z"
REVIEW_TIMESTAMP = "2026-09-19T23:02:19Z"

IDENTIFIER = "traitmech:000295"
SYSTEM = "Charlie gp32"
DEFENSEFINDER_SYSTEM = "Charlie_gp32"
SLUG = "charlie_gp32"
PROFILE_ROW = "Charlie_gp32__gp32"
PROPOSAL = "proposals/metpo_traitmech_v172"


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"{PROFILE_ROW:<48} | {PROFILE_ROW:<48} | {DEFENSEFINDER_SYSTEM}"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records gp32 in the "
            "Charlie_gp32 model namespace."
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
            "synonym_text": f"{SYSTEM} defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEDRICK,
        },
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
                "Dedrick et al. place the Cluster N Charlie gp32 system in a "
                "cohort of prophage-expressed defenses against lytic and "
                "temperate mycobacteriophages."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": (
                "The gene responsible is Charlie 32 (and presumably the "
                "analogous genes in Xeno and SkinnyPete), and a Charlie "
                "lysogen in which 32 is deleted loses defense against Che9c"
            ),
            "notes": (
                "Dedrick et al. localize a Cluster N prophage-mediated "
                "heterotypic defense to Charlie gene 32."
            ),
        },
        {
            "reference": DEDRICK,
            "snippet": "The Charlie gp32 defense system is notable",
            "notes": (
                "Dedrick et al. explicitly name the Charlie gp32 defense "
                "system as an exclusion-like viral-defense system."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Charlie_gp32 | 10\\.1038/nmicrobiol\\.2016\\.251 | "
                "Prophage-mediated defence against viral attack and viral "
                "counter-defence"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "Charlie_gp32 system to the Dedrick et al. prophage-mediated "
                "viral-defense paper."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_blocks_phage_entry",
            "title": "Charlie gp32 loci confer heterotypic phage exclusion",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Charlie gp32 locus to blocked Che9c DNA injection and "
                "restricted bacteriophage propagation."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Charlie gp32 as a named anti-phage system "
                "with a DefenseFinder gp32 profile and a proposed "
                "Che9c-exclusion output while leaving the direct gp32 target, "
                "the membrane-blocking mechanism, and homolog breadth "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Charlie gp32 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Charlie gp32 anti-phage defense locus cataloged in "
                        "DefenseFinder with a gp32 HMM profile."
                    ),
                },
                {
                    "node_id": "blocked_che9c_dna_injection",
                    "label": "blocked Che9c DNA injection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced Che9c bacteriophage DNA injection across the "
                        "cell envelope in cells carrying Charlie gp32."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Charlie gp32 system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Charlie gp32 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Charlie gp32 "
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
                    "object": "blocked_che9c_dna_injection",
                    "description": (
                        "Dedrick et al. identify Charlie 32 as the gene "
                        "responsible for Che9c defense, and DefenseFinder "
                        "catalogs a gp32 profile in the Charlie_gp32 model "
                        "namespace."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "The gene responsible is Charlie 32 (and "
                                "presumably the analogous genes in Xeno and "
                                "SkinnyPete), and a Charlie lysogen in which "
                                "32 is deleted loses defense against Che9c"
                            ),
                            "notes": (
                                "Dedrick et al. support Charlie gp32 as the "
                                "genetic determinant of the Che9c-exclusion "
                                "phenotype."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "blocked_che9c_dna_injection",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Charlie-gp32-mediated blockade of Che9c DNA injection "
                        "reduces productive phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "We propose that Charlie gp32 confers "
                                "heterotypic exclusion, blocking Che9c DNA "
                                "injection across the membrane"
                            ),
                            "notes": (
                                "Dedrick et al. interpret Charlie gp32 defense "
                                "as an exclusion-like block to Che9c DNA "
                                "injection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Charlie-gp32-mediated Che9c exclusion realizes the "
                        "Charlie gp32 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEDRICK,
                            "snippet": (
                                "Charlie gp32 confers survival to Che9c "
                                "infection, which also is a temperate phage"
                            ),
                            "notes": (
                                "Dedrick et al. show a cellular survival "
                                "outcome for Charlie-gp32-mediated Che9c "
                                "defense."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Charlie_gp32 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence"
                            ),
                            "notes": (
                                "DefenseFinder records Charlie_gp32 as a "
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
                        "Charlie gp32 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Charlie_gp32 | "
                                "10\\.1038/nmicrobiol\\.2016\\.251 | "
                                "Prophage-mediated defence against viral "
                                "attack and viral counter-defence |"
                            ),
                            "notes": (
                                "DefenseFinder associates Charlie_gp32 with "
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
                "Resolve the Charlie gp32 membrane target, Che9c specificity, "
                "and homolog breadth before minting narrower Charlie gp32 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dedrick et al. and DefenseFinder support Charlie gp32 as a "
                "named anti-phage system with a gp32 profile, but the direct "
                "membrane target, determinants of its Che9c specificity, and "
                "breadth of homologous loci are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_blocks_phage_entry"],
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
            "Minted Charlie gp32 system as a DOI-backed GENOMICS "
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
            "Resolved PR #1089 review issues #1090 and #1091 by dropping the "
            "proposed heterotypic-exclusion mechanism from the definition and "
            "tightening the Charlie gp32 exact-synonym evidence snippet after "
            "rechecking the Dedrick et al. full text and pinned DefenseFinder "
            "rows."
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
