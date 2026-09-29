#!/usr/bin/env python3
"""Add the HEC-05 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hec_05_system.yaml"

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
TIMESTAMP = "2026-09-29T16:05:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-29T16:05:01Z"
IDENTIFIER = "traitmech:000466"
PROPOSAL = "proposals/metpo_traitmech_v343"

HEC_IDENTITY_SNIPPET = "two GmrSD-like proteins (HEC-05 and HEC-06)"
HEC_BRXU_SNIPPET = "chosen HEC-05 homolog shares 99.2% amino acid identity"
HEC_ACTIVITY_SNIPPET = (
    "these were able to reduce the EOP of at least two phages"
)
ARTICLE_ROW = (
    "| HEC-05 | 10\\.1101/2024\\.01\\.29\\.577857 | New antiviral "
    "defences are genetically embedded within prokaryotic immune systems |"
)
HMM_PROFILE = "HEC-05__HEC-05"
HMM_PROFILE_SNIPPET = (
    "| HEC-05__HEC-05                                   |"
    "                                                  | HEC-05"
    "                 | Custom                  | 150    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the HEC-05 "
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
            f"{HMM_PROFILE} as a custom HEC-05 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "HEC-05 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene HEC-05 Hma-embedded candidate locus, encoding a "
        "GmrSD-like protein closely matching BrxU, that can reduce "
        "bacteriophage plaquing."
    ),
    "definition_source": PAYNE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "HEC-05",
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
                "Payne et al. identify HEC-05 as one of the "
                "Hma-embedded GmrSD-like candidate systems."
            ),
        },
        {
            "reference": PAYNE,
            "snippet": HEC_BRXU_SNIPPET,
            "notes": (
                "Payne et al. report that the selected HEC-05 homolog "
                "closely matches the independently characterized BrxU "
                "phage-defense protein."
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
            "graph_id": "hec_05_locus_reduces_phage_plaquing",
            "title": "HEC-05 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "HEC-05 locus to reduced bacteriophage plaquing and HEC-05 "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures HEC-05 at candidate locus and "
                "anti-phage-output level without asserting native host "
                "breadth, the direct viral trigger or substrate, exact "
                "GmrSD-like molecular output, or a DefenseFinder detection "
                "rule absent from the pinned rules table."
            ),
            "nodes": [
                {
                    "node_id": "hec_05_locus",
                    "label": "HEC-05 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene Hma-embedded candidate locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by a HEC-05 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophages "
                        "in cells carrying a complete HEC-05 candidate "
                        "system."
                    ),
                },
                {
                    "node_id": "hec_05_system_trait",
                    "label": "HEC-05 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded HEC-05 phage-defense "
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
                    "subject": "hec_05_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The HEC-05 locus contributes to reduced "
                        "bacteriophage plaquing as a GmrSD-like "
                        "Hma-embedded candidate."
                    ),
                    "evidence": [
                        {
                            "reference": PAYNE,
                            "snippet": HEC_IDENTITY_SNIPPET,
                            "notes": (
                                "Payne et al. identify HEC-05 among the "
                                "GmrSD-like Hma-embedded candidates."
                            ),
                        },
                        {
                            "reference": PAYNE,
                            "snippet": HEC_BRXU_SNIPPET,
                            "notes": (
                                "Payne et al. tie the selected HEC-05 "
                                "homolog to a close BrxU-like GmrSD-family "
                                "architecture."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hec_05_system_trait",
                    "description": (
                        "HEC-05-mediated plaquing reduction realizes the "
                        "HEC-05 system trait."
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
                    "subject": "hec_05_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "HEC-05 system possession is a phage-defense-system "
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
            "discussion_id": "hec-05-defensefinder-model-gap",
            "prompt": (
                "Resolve HEC-05 native host breadth, sensitive-phage "
                "breadth, BrxU synonymy, GmrSD-like molecular output, and "
                "rule-level detection criteria before minting narrower "
                "HEC-05 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Payne et al. support HEC-05 as a single-gene "
                "Hma-embedded candidate anti-phage system closely matching "
                "BrxU, and the pinned DefenseFinder HMM inventory records "
                "one HEC-05 profile row. The pinned rules table has no "
                "HEC-05 row, and the first-pass record does not yet "
                "resolve natural host breadth, phage target breadth, or "
                "the direct molecular output."
            ),
            "evidence": [
                {
                    "reference": PAYNE,
                    "snippet": HEC_IDENTITY_SNIPPET,
                    "notes": (
                        "Payne et al. identify HEC-05 as one of the "
                        "GmrSD-like Hma-embedded candidate systems."
                    ),
                },
                {
                    "reference": PAYNE,
                    "snippet": HEC_BRXU_SNIPPET,
                    "notes": (
                        "Payne et al. report that the selected HEC-05 "
                        "homolog closely matches BrxU."
                    ),
                },
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "HEC-05, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#hec_05_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-29",
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
            "Minted HEC-05 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "single-gene candidate-locus level because the pinned "
            "DefenseFinder HEC-05 HMM row is not backed by a pinned rules "
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
            "Reviewed HEC-05 system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support heterologous efficiency-of-plaquing assays "
            "and a DefenseFinder HEC-05 HMM row, but not a direct named "
            "native microbial isolate exemplar with experimentally "
            "verified endogenous HEC-05 activity. No paid research was "
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
