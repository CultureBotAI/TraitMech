#!/usr/bin/env python3
"""Add the HEC-03 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hec_03_system.yaml"

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
TIMESTAMP = "2026-09-27T21:21:54Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T21:21:55Z"
IDENTIFIER = "traitmech:000418"
PROPOSAL = "proposals/metpo_traitmech_v295"

HEC_IDENTITY_SNIPPET = (
    "The candidate systems encoded diverse protein families, including "
    "three ATPases associated with either a topoisomerase-primase (TOPRIM) "
    "(HEC-01), nuclease-related (NERD) (HEC-02), or PilT N-terminal (PIN) "
    "(HEC-03) domain-containing protein"
)
HEC_ACTIVITY_SNIPPET = (
    "A quantitative assessment of the remaining systems showed that these "
    "were able to reduce the EOP of at least two phages by several orders "
    "of magnitude compared to the control"
)
HEC_GENE_REQUIREMENT_SNIPPET = (
    "For the two-gene systems HEC-02 and HEC-03, both genes were required "
    "for defence"
)
ARTICLE_ROW = (
    "| HEC-03 | 10\\.1101/2024\\.01\\.29\\.577857 | New antiviral "
    "defences are genetically embedded within prokaryotic immune systems |"
)
HMM_PROFILE_SNIPPETS = {
    "HEC-03__HEC-03A": (
        "| HEC-03__HEC-03A                                  |"
        "                                                  | HEC-03"
        "                 | Custom                  | 50     |"
    ),
    "HEC-03__HEC-03B": (
        "| HEC-03__HEC-03B                                  |"
        "                                                  | HEC-03"
        "                 | Custom                  | 150    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the HEC-03 "
            "source key to the Payne et al. Hma-embedded-candidate "
            "preprint."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom HEC-03 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "HEC-03 system",
    "definition": (
        "A phage defense system in which an organism possesses the two-gene "
        "HEC-03 Hma-embedded candidate locus, encoding an ABC ATPase and an "
        "associated PilT N-terminal domain protein, that can reduce "
        "bacteriophage plaquing."
    ),
    "definition_source": PAYNE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "HEC-03",
            "synonym_type": "EXACT_SYNONYM",
            "source": PAYNE,
        }
    ],
    "evidence": [
        {
            "reference": PAYNE,
            "snippet": HEC_IDENTITY_SNIPPET,
            "notes": (
                "Payne et al. identify HEC-03 as a candidate two-gene "
                "Hma-embedded antiviral system pairing an ATPase with a "
                "PilT N-terminal-domain protein."
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
            "snippet": HEC_GENE_REQUIREMENT_SNIPPET,
            "notes": (
                "Payne et al. show that both genes in the two-gene HEC-03 "
                "candidate system were required for defense."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "hec_03_locus_reduces_phage_plaquing",
            "title": "HEC-03 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "HEC-03 locus to reduced bacteriophage plaquing and HEC-03 "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures HEC-03 at candidate locus and "
                "anti-phage-output level without asserting native host "
                "breadth, exact profile-to-component mapping, the direct "
                "viral trigger or substrate, exact molecular output, or a "
                "DefenseFinder detection rule absent from the pinned rules "
                "table."
            ),
            "nodes": [
                {
                    "node_id": "hec_03_locus",
                    "label": "HEC-03 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene Hma-embedded candidate locus represented "
                        "in the pinned DefenseFinder HMM inventory by "
                        "HEC-03A and HEC-03B custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophages "
                        "in cells carrying a complete HEC-03 candidate "
                        "system."
                    ),
                },
                {
                    "node_id": "hec_03_system_trait",
                    "label": "HEC-03 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded HEC-03 phage-defense "
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
                    "subject": "hec_03_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The two-gene HEC-03 locus contributes to reduced "
                        "bacteriophage plaquing when both HEC-03 genes are "
                        "present."
                    ),
                    "evidence": [
                        {
                            "reference": PAYNE,
                            "snippet": HEC_IDENTITY_SNIPPET,
                            "notes": (
                                "Payne et al. identify HEC-03 as pairing an "
                                "ATPase with a PilT N-terminal-domain "
                                "protein."
                            ),
                        },
                        {
                            "reference": PAYNE,
                            "snippet": HEC_GENE_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Payne et al. show that HEC-03 requires both "
                                "genes for defense."
                            ),
                        },
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hec_03_system_trait",
                    "description": (
                        "HEC-03-mediated plaquing reduction realizes the "
                        "HEC-03 system trait."
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
                            "snippet": HEC_GENE_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Payne et al. show that complete HEC-03 "
                                "requires both genes for defense."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hec_03_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "HEC-03 system possession is a phage-defense-system "
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
            "discussion_id": "hec-03-defensefinder-model-gap",
            "prompt": (
                "Resolve HEC-03 native host breadth, exact HEC-03A/HEC-03B "
                "component functions, sensitive-phage breadth, molecular "
                "output, and rule-level detection criteria before minting "
                "narrower HEC-03 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Payne et al. support HEC-03 as an Hma-embedded candidate "
                "anti-phage system whose two genes are both required for "
                "defense, and the pinned DefenseFinder HMM inventory "
                "records HEC-03A and HEC-03B profile rows. The pinned rules "
                "table has no HEC-03 row, and the first-pass record does "
                "not yet resolve natural host breadth, HEC-03 profile-to-"
                "component mapping, phage target breadth, or the direct "
                "molecular output."
            ),
            "evidence": [
                {
                    "reference": PAYNE,
                    "snippet": HEC_IDENTITY_SNIPPET,
                    "notes": (
                        "Payne et al. identify HEC-03 as one of the "
                        "ATPase-associated Hma-embedded candidate systems."
                    ),
                },
                {
                    "reference": PAYNE,
                    "snippet": HEC_GENE_REQUIREMENT_SNIPPET,
                    "notes": (
                        "Payne et al. support two-gene requirement for "
                        "HEC-03-mediated defense."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "HEC-03, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#hec_03_locus_reduces_phage_plaquing"],
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
            "Minted HEC-03 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "two-gene candidate-locus level because the pinned "
            "DefenseFinder HEC-03 HMM rows are not backed by pinned rules "
            f"rows; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed HEC-03 system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support heterologous efficiency-of-plaquing assays "
            "and DefenseFinder HEC-03 HMM rows, but not a direct named "
            "native microbial isolate exemplar with experimentally "
            "verified endogenous HEC-03 activity. No paid research was "
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
