#!/usr/bin/env python3
"""Add the SDIC4 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sdic4_system.yaml"

CUMMINS = "DOI:10.1016/j.celrep.2024.115055"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T23:47:56Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-27T23:47:57Z"

IDENTIFIER = "traitmech:000421"
PROPOSAL = "proposals/metpo_traitmech_v298"

SDIC4_COMPOSITION_SNIPPET = (
    "SDIC4 comprises SDIC4A, a protein of unknown function, and SDIC4B, "
    "harboring the VasI-like domain"
)
SDIC4_ACTIVITY_SNIPPET = (
    "SDIC4-mediated anti-phage activity is more modest (R10- to 200-fold) "
    "but still significant"
)
SDIC4_ADSORPTION_SNIPPET = (
    "In the presence of full-length SDIC4 or SDIC4B, we observed a "
    "decrease in the adsorption rate"
)
SDIC4_TYPE_SNIPPET = (
    "SDIC4 type I and type II elicit protection against phage infection by "
    "reducing the adsorption rate of invading phages"
)
ARTICLE_ROW = (
    "SDIC4 | 10\\.1016/j\\.celrep\\.2024\\.115055 | Multi-conflict "
    "islands are a widespread trend within Serratia spp"
)
HMM_PROFILE_SNIPPETS = {
    "SDIC4__SDIC4A": (
        "| SDIC4__SDIC4A                                    |"
        "                                                  | SDIC4"
        "                  | Custom                  | 100    |"
    ),
    "SDIC4__SDIC4B": (
        "| SDIC4__SDIC4B                                    |"
        "                                                  | SDIC4"
        "                  | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the SDIC4 source "
            "key to the Cummins et al. Serratia multi-conflict-island paper."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom SDIC4 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SDIC4 system",
    "definition": (
        "A phage defense system in which an organism possesses an SDIC4 "
        "locus encoding an SDIC4A component and a VasI-like SDIC4B "
        "component that can reduce adsorption of invading bacteriophages."
    ),
    "definition_source": CUMMINS,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SDIC4",
            "synonym_type": "EXACT_SYNONYM",
            "source": CUMMINS,
        },
        {
            "synonym_text": "SDIC4__SDIC4A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC4__SDIC4B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": CUMMINS,
            "snippet": SDIC4_COMPOSITION_SNIPPET,
            "notes": (
                "Cummins et al. describe the SDIC4 locus as encoding an "
                "SDIC4A component of unknown function and a VasI-like SDIC4B "
                "component."
            ),
        },
        {
            "reference": CUMMINS,
            "snippet": SDIC4_ACTIVITY_SNIPPET,
            "notes": (
                "Cummins et al. report significant SDIC4-mediated "
                "anti-phage activity when SDIC4 was expressed in E. coli."
            ),
        },
        {
            "reference": CUMMINS,
            "snippet": SDIC4_ADSORPTION_SNIPPET,
            "notes": (
                "Cummins et al. connect full-length SDIC4 and SDIC4B with a "
                "decreased bacteriophage adsorption rate."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "sdic4_locus_reduces_phage_adsorption",
            "title": "SDIC4 loci reduce bacterial phage adsorption",
            "description": (
                "Conservative system-level sketch linking the SDIC4 locus "
                "to reduced adsorption of invading bacteriophages."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SDIC4 as a named anti-phage system with "
                "SDIC4A and SDIC4B DefenseFinder profiles while leaving "
                "natural host breadth, sensitive-phage breadth, the SDIC4 "
                "type I versus type II boundary, the exact "
                "SDIC4A/SDIC4B profile-to-protein correspondence, the "
                "receptor or phage target, and rule-level detection "
                "criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sdic4_locus",
                    "label": "SDIC4 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An SDIC4 anti-phage defense locus represented in "
                        "the pinned DefenseFinder HMM inventory by SDIC4A "
                        "and SDIC4B custom profiles."
                    ),
                },
                {
                    "node_id": "phage_adsorption_reduction",
                    "label": "reduced phage adsorption rate",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduction of the rate at which invading "
                        "bacteriophages adsorb to bacterial cells."
                    ),
                },
                {
                    "node_id": "sdic4_system_trait",
                    "label": "SDIC4 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SDIC4 phage-defense "
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
                    "subject": "sdic4_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_adsorption_reduction",
                    "description": (
                        "The SDIC4 locus contributes to reduced adsorption "
                        "of invading bacteriophages."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC4_ADSORPTION_SNIPPET,
                            "notes": (
                                "Cummins et al. report decreased phage "
                                "adsorption for full-length SDIC4 and "
                                "SDIC4B."
                            ),
                        },
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC4_TYPE_SNIPPET,
                            "notes": (
                                "Cummins et al. connect both tested SDIC4 "
                                "subtypes with reduced phage adsorption."
                            ),
                        },
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "phage_adsorption_reduction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sdic4_system_trait",
                    "description": (
                        "Reduced phage adsorption realizes the SDIC4 system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC4_ACTIVITY_SNIPPET,
                            "notes": (
                                "Cummins et al. report significant "
                                "SDIC4-mediated anti-phage activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sdic4_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SDIC4 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC4_ACTIVITY_SNIPPET,
                            "notes": (
                                "Cummins et al. report SDIC4-mediated "
                                "anti-phage activity."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "sdic4-defensefinder-model-gap",
            "prompt": (
                "Resolve SDIC4 natural host breadth, sensitive-phage "
                "breadth, type I versus type II component scope, "
                "SDIC4A/SDIC4B component functions, receptor or phage "
                "target, and rule-level detection criteria before minting "
                "narrower SDIC4 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cummins et al. support SDIC4 as a VasI-like anti-phage "
                "system that reduces phage adsorption, and the pinned "
                "DefenseFinder HMM inventory records SDIC4A and SDIC4B "
                "profile rows. The pinned rules table has no SDIC4 row, "
                "and the first-pass record does not resolve natural host "
                "breadth, sensitive-phage breadth, type I versus type II "
                "system boundaries, the exact profile-to-component mapping, "
                "the SDIC4A/SDIC4B relationship, or the phage-adsorption "
                "target."
            ),
            "evidence": [
                {
                    "reference": CUMMINS,
                    "snippet": SDIC4_COMPOSITION_SNIPPET,
                    "notes": (
                        "Cummins et al. describe the initially named SDIC4 "
                        "candidate as an SDIC4A/SDIC4B system."
                    ),
                },
                {
                    "reference": CUMMINS,
                    "snippet": SDIC4_TYPE_SNIPPET,
                    "notes": (
                        "Cummins et al. later add a second SDIC4 subtype "
                        "and connect both tested types with reduced "
                        "adsorption."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "SDIC4, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#sdic4_locus_reduces_phage_adsorption"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
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
            "Minted SDIC4 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at candidate-locus level "
            "because the pinned DefenseFinder SDIC4 HMM rows are not backed "
            f"by a rules row; {PROPOSAL} reserves the replacement "
            "placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed SDIC4 system canonical_examples and left them empty "
            "because Cummins et al. support plasmid-expressed E. coli and "
            "S. marcescens phage-challenge and phage-adsorption assays plus "
            "a DefenseFinder SDIC4 system model, but not a direct native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous SDIC4 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
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
