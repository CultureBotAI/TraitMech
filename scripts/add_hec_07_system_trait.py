#!/usr/bin/env python3
"""Add the HEC-07 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hec_07_system.yaml"

PAYNE = "DOI:10.1101/2024.01.29.577857"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T00:50:18Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T00:50:19Z"
IDENTIFIER = "traitmech:000478"
PROPOSAL = "proposals/metpo_traitmech_v355"

HEC_IDENTITY_SNIPPET = (
    "RelE (HEC-07), higher eukaryotes and prokaryotes nucleotide-binding "
    "(HEPN) (HEC-08) and Nedd4-BP1/YacP nuclease (NYN) (HEC-09) "
    "domain-containing proteins"
)
HEC_ACTIVITY_SNIPPET = (
    "these were able to reduce the EOP of at least two phages"
)
ARTICLE_ROW = (
    "| HEC-07 | 10\\.1101/2024\\.01\\.29\\.577857 | New antiviral "
    "defences are genetically embedded within prokaryotic immune systems |"
)
HMM_PROFILE = "HEC-07__HEC-07"
HMM_PROFILE_SNIPPET = (
    "| HEC-07__HEC-07                                   |"
    "                                                  | HEC-07"
    "                 | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the HEC-07 "
            "source key to the Payne et al. Hma-embedded-candidate "
            "preprint."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            f"{HMM_PROFILE} as a custom HEC-07 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "HEC-07 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene HEC-07 Hma-embedded candidate locus, encoding a "
        "RelE domain-containing protein, that can reduce bacteriophage "
        "plaquing."
    ),
    "definition_source": PAYNE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "HEC-07",
            "synonym_type": "EXACT_SYNONYM",
            "source": PAYNE,
        },
        {
            "synonym_text": HMM_PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": PAYNE,
            "snippet": HEC_IDENTITY_SNIPPET,
            "notes": (
                "Payne et al. identify HEC-07 as a RelE-domain "
                "Hma-embedded candidate system."
            ),
        },
        {
            "reference": PAYNE,
            "snippet": HEC_ACTIVITY_SNIPPET,
            "notes": (
                "Payne et al. support reduced plaquing for the active "
                "Hma-embedded candidate systems after excluding inactive "
                "HEC-01 and HEC-09 candidates."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "hec_07_locus_reduces_phage_plaquing",
            "title": "HEC-07 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "HEC-07 locus to reduced bacteriophage plaquing and HEC-07 "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures HEC-07 at candidate locus and "
                "anti-phage-output level without asserting native host "
                "breadth, the direct viral trigger or substrate, exact "
                "RelE-domain molecular output, or a DefenseFinder detection "
                "rule absent from the pinned rules table."
            ),
            "nodes": [
                {
                    "node_id": "hec_07_locus",
                    "label": "HEC-07 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene Hma-embedded candidate locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by a HEC-07 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophages "
                        "in cells carrying a complete HEC-07 candidate "
                        "system."
                    ),
                },
                {
                    "node_id": "hec_07_system_trait",
                    "label": "HEC-07 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded HEC-07 phage-defense "
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
                    "subject": "hec_07_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The HEC-07 locus contributes to reduced "
                        "bacteriophage plaquing as a RelE-domain "
                        "Hma-embedded candidate."
                    ),
                    "evidence": [
                        {
                            "reference": PAYNE,
                            "snippet": HEC_IDENTITY_SNIPPET,
                            "notes": (
                                "Payne et al. identify HEC-07 among the "
                                "RelE-domain Hma-embedded candidates."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hec_07_system_trait",
                    "description": (
                        "HEC-07-mediated plaquing reduction realizes the "
                        "HEC-07 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PAYNE,
                            "snippet": HEC_ACTIVITY_SNIPPET,
                            "notes": (
                                "Payne et al. support reduced efficiency of "
                                "plaquing for the active HEC systems."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hec_07_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "HEC-07 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "hec-07-defensefinder-model-gap",
            "prompt": (
                "Resolve HEC-07 native host breadth, sensitive-phage "
                "breadth, RelE-domain molecular output, and rule-level "
                "detection criteria before minting narrower HEC-07 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Payne et al. support HEC-07 as a single-gene "
                "Hma-embedded candidate anti-phage system encoding a "
                "RelE-domain protein, and the pinned DefenseFinder HMM "
                "inventory records one HEC-07 profile row. The pinned "
                "rules table has no HEC-07 row, and the first-pass record "
                "does not yet resolve natural host breadth, phage target "
                "breadth, or the direct molecular output."
            ),
            "evidence": [
                {
                    "reference": PAYNE,
                    "snippet": HEC_IDENTITY_SNIPPET,
                    "notes": (
                        "Payne et al. identify HEC-07 as a RelE-domain "
                        "Hma-embedded candidate system."
                    ),
                },
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "HEC-07, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#hec_07_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
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
            "Minted HEC-07 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "single-gene candidate-locus level because the pinned "
            "DefenseFinder HEC-07 HMM row is not backed by a pinned rules "
            f"row; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed HEC-07 system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support heterologous efficiency-of-plaquing assays "
            "and a DefenseFinder HEC-07 HMM row, but not a direct named "
            "native microbial isolate exemplar with experimentally "
            "verified endogenous HEC-07 activity. No paid research was "
            "used."
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
