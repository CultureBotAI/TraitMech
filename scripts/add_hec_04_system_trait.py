#!/usr/bin/env python3
"""Add the HEC-04 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hec_04_system.yaml"

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
TIMESTAMP = "2026-09-29T14:17:47Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-29T14:17:48Z"
IDENTIFIER = "traitmech:000465"
PROPOSAL = "proposals/metpo_traitmech_v342"

HEC_IDENTITY_SNIPPET = (
    "an ATPase fused to a TOPRIM domain (HEC-04)"
)
HEC_ACTIVITY_SNIPPET = (
    "A quantitative assessment of the remaining systems showed that these "
    "were able to reduce the EOP of at least two phages by several orders "
    "of magnitude compared to the control"
)
HEC_DOMAIN_REQUIREMENT_SNIPPET = (
    "For HEC-04, mutation of key active site residues in either the ABC "
    "ATPase or nuclease domains demonstrated their essential roles in defence"
)
ARTICLE_ROW = (
    "| HEC-04 | 10\\.1101/2024\\.01\\.29\\.577857 | New antiviral "
    "defences are genetically embedded within prokaryotic immune systems |"
)
HMM_PROFILE = "HEC-04__HEC-04"
HMM_PROFILE_SNIPPET = (
    "| HEC-04__HEC-04                                   |"
    "                                                  | HEC-04"
    "                 | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the HEC-04 "
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
            f"{HMM_PROFILE} as a custom HEC-04 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "HEC-04 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene HEC-04 Hma-embedded candidate locus, encoding an ABC "
        "ATPase fused to a TOPRIM-family nuclease domain, that can reduce "
        "bacteriophage plaquing."
    ),
    "definition_source": PAYNE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "HEC-04",
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
                "Payne et al. identify HEC-04 as a Hma-embedded antiviral "
                "candidate encoding an ATPase fused to a TOPRIM domain."
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
        {
            "reference": PAYNE,
            "snippet": HEC_DOMAIN_REQUIREMENT_SNIPPET,
            "notes": (
                "Payne et al. show that HEC-04 defense requires intact ABC "
                "ATPase and nuclease active-site residues."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "hec_04_locus_reduces_phage_plaquing",
            "title": "HEC-04 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "HEC-04 locus to reduced bacteriophage plaquing and HEC-04 "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures HEC-04 at candidate locus and "
                "anti-phage-output level without asserting native host "
                "breadth, the direct viral trigger or substrate, exact "
                "molecular output, or a DefenseFinder detection rule absent "
                "from the pinned rules table."
            ),
            "nodes": [
                {
                    "node_id": "hec_04_locus",
                    "label": "HEC-04 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene Hma-embedded candidate locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by a HEC-04 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophages "
                        "in cells carrying a complete HEC-04 candidate "
                        "system."
                    ),
                },
                {
                    "node_id": "hec_04_system_trait",
                    "label": "HEC-04 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded HEC-04 phage-defense "
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
                    "subject": "hec_04_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The HEC-04 locus contributes to reduced "
                        "bacteriophage plaquing when ABC ATPase and nuclease "
                        "active-site residues are intact."
                    ),
                    "evidence": [
                        {
                            "reference": PAYNE,
                            "snippet": HEC_IDENTITY_SNIPPET,
                            "notes": (
                                "Payne et al. identify HEC-04 as encoding an "
                                "ATPase-TOPRIM fused protein."
                            ),
                        },
                        {
                            "reference": PAYNE,
                            "snippet": HEC_DOMAIN_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Payne et al. show that HEC-04 requires "
                                "intact ATPase and nuclease domains for "
                                "defense."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hec_04_system_trait",
                    "description": (
                        "HEC-04-mediated plaquing reduction realizes the "
                        "HEC-04 system trait."
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
                        {
                            "reference": PAYNE,
                            "snippet": HEC_DOMAIN_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Payne et al. support ABC ATPase and nuclease "
                                "active-site requirements for HEC-04-mediated "
                                "defense."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hec_04_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "HEC-04 system possession is a phage-defense-system "
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
            "discussion_id": "hec-04-defensefinder-model-gap",
            "prompt": (
                "Resolve HEC-04 native host breadth, sensitive-phage "
                "breadth, ATPase-TOPRIM molecular output, and rule-level "
                "detection criteria before minting narrower HEC-04 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Payne et al. support HEC-04 as a single-gene "
                "Hma-embedded candidate anti-phage system whose ABC ATPase "
                "and nuclease domains are both required for defense, and "
                "the pinned DefenseFinder HMM inventory records one HEC-04 "
                "profile row. The pinned rules table has no HEC-04 row, "
                "and the first-pass record does not yet resolve natural "
                "host breadth, phage target breadth, or the direct "
                "molecular output."
            ),
            "evidence": [
                {
                    "reference": PAYNE,
                    "snippet": HEC_IDENTITY_SNIPPET,
                    "notes": (
                        "Payne et al. identify HEC-04 as the "
                        "ATPase-TOPRIM Hma-embedded candidate system."
                    ),
                },
                {
                    "reference": PAYNE,
                    "snippet": HEC_DOMAIN_REQUIREMENT_SNIPPET,
                    "notes": (
                        "Payne et al. support HEC-04 domain requirements "
                        "for defense."
                    ),
                },
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "HEC-04, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#hec_04_locus_reduces_phage_plaquing"],
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
            "Minted HEC-04 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "single-gene candidate-locus level because the pinned "
            "DefenseFinder HEC-04 HMM row is not backed by a pinned rules "
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
            "Reviewed HEC-04 system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support heterologous efficiency-of-plaquing assays "
            "and a DefenseFinder HEC-04 HMM row, but not a direct named "
            "native microbial isolate exemplar with experimentally "
            "verified endogenous HEC-04 activity. No paid research was "
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
