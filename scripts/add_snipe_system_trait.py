#!/usr/bin/env python3
"""Add the SNIPE system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "snipe_system.yaml"

SAXTON = "DOI:10.1038/s41586-026-10207-1"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T18:23:52Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T18:23:53Z"
IDENTIFIER = "traitmech:000414"
PROPOSAL = "proposals/metpo_traitmech_v291"

ARTICLE_ROW = (
    "| SNIPE | 10\\.1038/s41586-026-10207-1 | A membrane-bound nuclease "
    "directly cleaves phage DNA during genome injection |"
)
MEMBRANE_SNIPPET = (
    "Here, we characterize SNIPE, an anti-bacteriophage defence system that "
    "constitutively localizes to the bacterial cell membrane in Escherichia coli"
)
DNA_CLEAVAGE_SNIPPET = (
    "Using radiolabelled phage DNA and time-lapse microscopy to track phage "
    "genomes, we demonstrate that SNIPE directly cleaves phage DNA during "
    "genome injection."
)
SIPHO_DEFENSE_SNIPPET = "SNIPE also defends against diverse siphoviruses"
SPATIAL_TARGETING_SNIPPET = (
    "Our findings establish SNIPE as a widespread bacterial defence system "
    "that exploits the spatial organization of phage genome injection to "
    "specifically target viral DNA"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named SNIPE "
            "system to the Saxton et al. phage-genome-injection cleavage "
            "paper. The pinned HMM inventory and rules table do not list "
            "SNIPE, so this row is name-to-paper evidence rather than "
            "model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SNIPE system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "SNIPE anti-bacteriophage system that localizes to the bacterial "
        "membrane, exploits the spatial organization of phage genome "
        "injection, and directly cleaves incoming phage DNA to block "
        "siphovirus infection."
    ),
    "definition_source": SAXTON,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SNIPE",
            "synonym_type": "EXACT_SYNONYM",
            "source": SAXTON,
        }
    ],
    "evidence": [
        {
            "reference": SAXTON,
            "snippet": MEMBRANE_SNIPPET,
            "notes": (
                "Saxton et al. define SNIPE as an anti-bacteriophage "
                "defence system and localize it to the bacterial cell "
                "membrane in Escherichia coli."
            ),
        },
        {
            "reference": SAXTON,
            "snippet": DNA_CLEAVAGE_SNIPPET,
            "notes": (
                "Saxton et al. show that SNIPE directly cleaves phage DNA "
                "while the phage genome is being injected."
            ),
        },
        {
            "reference": SAXTON,
            "snippet": SIPHO_DEFENSE_SNIPPET,
            "notes": (
                "Saxton et al. support SNIPE defence against diverse "
                "siphoviruses."
            ),
        },
        {
            "reference": SAXTON,
            "snippet": SPATIAL_TARGETING_SNIPPET,
            "notes": (
                "Saxton et al. frame SNIPE as a widespread defence system "
                "that exploits phage genome-injection geometry to target "
                "viral DNA."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "snipe_cleaves_injected_phage_dna",
            "title": "SNIPE cleaves phage DNA during genome injection",
            "description": (
                "Conservative system-level sketch linking a SNIPE locus to "
                "direct phage DNA cleavage during genome injection, "
                "inhibition of siphovirus infection, and SNIPE system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SNIPE at membrane-localized "
                "phage-genome-injection targeting level without asserting "
                "the exact direct viral sensor, the full host or phage "
                "range, or any DefenseFinder HMM-to-component mapping."
            ),
            "nodes": [
                {
                    "node_id": "snipe_locus",
                    "label": "SNIPE locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A SNIPE anti-bacteriophage locus encoding the "
                        "membrane-localized SNIPE defense activity."
                    ),
                },
                {
                    "node_id": "snipe_direct_phage_dna_cleavage",
                    "label": "SNIPE direct phage DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Direct cleavage of phage DNA by SNIPE as the viral "
                        "genome is injected."
                    ),
                },
                {
                    "node_id": "phage_genome_injection",
                    "label": "phage genome injection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Injection of a siphovirus genome into the bacterial "
                        "cell."
                    ),
                },
                {
                    "node_id": "siphovirus_infection",
                    "label": "siphovirus infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Productive infection by bacteriophages with "
                        "siphovirus morphology."
                    ),
                },
                {
                    "node_id": "snipe_system_trait",
                    "label": "SNIPE system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SNIPE phage-defense "
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
                    "subject": "snipe_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "snipe_direct_phage_dna_cleavage",
                    "description": (
                        "A SNIPE locus enables direct cleavage of phage DNA "
                        "during genome injection."
                    ),
                    "evidence": [
                        {
                            "reference": SAXTON,
                            "snippet": DNA_CLEAVAGE_SNIPPET,
                            "notes": (
                                "Saxton et al. directly connect SNIPE to "
                                "phage DNA cleavage during genome injection."
                            ),
                        },
                    ],
                },
                {
                    "subject": "snipe_direct_phage_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_genome_injection",
                    "description": (
                        "SNIPE targets viral DNA during the genome-injection "
                        "stage of phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": SAXTON,
                            "snippet": SPATIAL_TARGETING_SNIPPET,
                            "notes": (
                                "Saxton et al. frame SNIPE cleavage as "
                                "exploitation of the spatial organization of "
                                "phage genome injection."
                            ),
                        },
                    ],
                },
                {
                    "subject": "snipe_direct_phage_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "siphovirus_infection",
                    "description": (
                        "By targeting injected viral DNA, SNIPE restricts "
                        "siphovirus infection."
                    ),
                    "evidence": [
                        {
                            "reference": SAXTON,
                            "snippet": SIPHO_DEFENSE_SNIPPET,
                            "notes": (
                                "Saxton et al. support SNIPE-mediated "
                                "defence against diverse siphoviruses."
                            ),
                        },
                    ],
                },
                {
                    "subject": "snipe_direct_phage_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "snipe_system_trait",
                    "description": (
                        "Direct cleavage of injected phage DNA realizes the "
                        "SNIPE system trait."
                    ),
                    "evidence": [
                        {
                            "reference": SAXTON,
                            "snippet": DNA_CLEAVAGE_SNIPPET,
                            "notes": (
                                "Saxton et al. show the SNIPE phage-defense "
                                "output as direct phage DNA cleavage during "
                                "genome injection."
                            ),
                        },
                    ],
                },
                {
                    "subject": "snipe_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SNIPE system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": SAXTON,
                            "snippet": MEMBRANE_SNIPPET,
                            "notes": (
                                "Saxton et al. define SNIPE as an "
                                "anti-bacteriophage defence system."
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
            "discussion_id": "snipe-defensefinder-model-gap",
            "prompt": (
                "Resolve SNIPE host breadth, sensitive-phage breadth, direct "
                "tape-measure interaction specificity, and DefenseFinder "
                "HMM/rules coverage before minting narrower SNIPE mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Saxton et al. support SNIPE as a membrane-localized "
                "anti-bacteriophage system that directly cleaves phage DNA "
                "during genome injection, while the pinned DefenseFinder "
                "article registry names a SNIPE system. The pinned "
                "DefenseFinder HMM inventory and rules table have no SNIPE "
                "rows, and the evidence does not yet resolve full host "
                "breadth, full target-phage breadth, direct tape-measure "
                "protein specificity, or profile-to-activity modeling."
            ),
            "evidence": [
                {
                    "reference": SAXTON,
                    "snippet": SPATIAL_TARGETING_SNIPPET,
                    "notes": (
                        "Saxton et al. support SNIPE as a widespread "
                        "phage-defense system targeting viral DNA during "
                        "phage genome injection."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "The pinned DefenseFinder HMM inventory does not "
                        "list SNIPE, leaving profile-level components "
                        "unresolved."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "SNIPE, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#snipe_cleaves_injected_phage_dna"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted SNIPE system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "membrane-localized phage-genome-injection cleavage level "
            "because the pinned DefenseFinder article row is not backed by "
            "pinned HMM or rules rows; the replacement placeholder is "
            f"reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed SNIPE system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support E. coli expression and phage-challenge assays "
            "plus a DefenseFinder article-registry system name, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified SNIPE activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
