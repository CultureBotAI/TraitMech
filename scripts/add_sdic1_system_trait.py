#!/usr/bin/env python3
"""Add the SDIC1 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sdic1_system.yaml"

BAYER = "DOI:10.1016/j.celrep.2024.115055"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T22:49:28Z"

IDENTIFIER = "traitmech:000420"
PROPOSAL = "proposals/metpo_traitmech_v297"

SDIC1_UBIQUITIN_SNIPPET = "SDIC1 combines TIR and ubiquitin ligase"
SDIC_COHORT_SNIPPET = "four newly identified anti-phage systems"
TIR_SYSTEM_SNIPPET = (
    "previously unreported Toll/interleukin (IL)-1 receptor (TIR)-domain-"
    "containing system with population-wide immunity"
)
ARTICLE_ROW = (
    "SDIC1 | 10\\.1016/j\\.celrep\\.2024\\.115055 | Multi-conflict "
    "islands are a widespread trend within Serratia spp"
)
HMM_PROFILE_SNIPPETS = {
    "SDIC1__SDIC1A": (
        "| SDIC1__SDIC1A                                    |"
        "                                                  | SDIC1"
        "                  | Custom                  | 350    |"
    ),
    "SDIC1__SDIC1B": (
        "| SDIC1__SDIC1B                                    |"
        "                                                  | SDIC1"
        "                  | Custom                  | 130    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the SDIC1 source "
            "key to the Bayer et al. Serratia multi-conflict-island paper."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom SDIC1 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SDIC1 system",
    "definition": (
        "A phage defense system in which an organism possesses an SDIC1 locus "
        "encoding a TIR-domain SDIC1A component and a ubiquitin-ligase-like "
        "SDIC1B component that can provide population-wide immunity against "
        "bacteriophages."
    ),
    "definition_source": BAYER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SDIC1",
            "synonym_type": "EXACT_SYNONYM",
            "source": BAYER,
        },
        {
            "synonym_text": "SDIC1__SDIC1A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC1__SDIC1B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": BAYER,
            "snippet": SDIC_COHORT_SNIPPET,
            "notes": (
                "Bayer et al. identify SDIC1 in a cohort of Serratia "
                "defense-island candidate systems with anti-phage activity."
            ),
        },
        {
            "reference": BAYER,
            "snippet": TIR_SYSTEM_SNIPPET,
            "notes": (
                "Bayer et al. support SDIC1 as a TIR-domain-containing "
                "phage-defense system with a population-wide immunity "
                "phenotype."
            ),
        },
        {
            "reference": BAYER,
            "snippet": SDIC1_UBIQUITIN_SNIPPET,
            "notes": (
                "Bayer et al. connect the SDIC1 system with TIR and "
                "ubiquitin-ligase-like components."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "sdic1_locus_restricts_phage",
            "title": "SDIC1 loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking the SDIC1 locus "
                "to population-wide immunity against bacteriophages."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SDIC1 as a named anti-phage system with "
                "SDIC1A and SDIC1B DefenseFinder profiles while leaving "
                "natural host breadth, sensitive-phage breadth, the exact "
                "SDIC1A/SDIC1B profile-to-protein correspondence, the "
                "direct trigger, the ubiquitination substrate, and "
                "rule-level detection criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sdic1_locus",
                    "label": "SDIC1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An SDIC1 anti-phage defense locus represented in "
                        "the pinned DefenseFinder HMM inventory by SDIC1A "
                        "and SDIC1B custom profiles."
                    ),
                },
                {
                    "node_id": "population_wide_antiphage_immunity",
                    "label": "population-wide anti-phage immunity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection of a bacterial population against "
                        "bacteriophage infection by SDIC1 activity."
                    ),
                },
                {
                    "node_id": "sdic1_system_trait",
                    "label": "SDIC1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SDIC1 phage-defense "
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
                    "subject": "sdic1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "population_wide_antiphage_immunity",
                    "description": (
                        "The SDIC1 locus contributes to population-wide "
                        "immunity against bacteriophages."
                    ),
                    "evidence": [
                        {
                            "reference": BAYER,
                            "snippet": TIR_SYSTEM_SNIPPET,
                            "notes": (
                                "Bayer et al. report population-wide "
                                "immunity for the SDIC1 TIR-domain system."
                            ),
                        },
                        {
                            "reference": BAYER,
                            "snippet": SDIC1_UBIQUITIN_SNIPPET,
                            "notes": (
                                "Bayer et al. place TIR and "
                                "ubiquitin-ligase-like activities in the "
                                "SDIC1 system."
                            ),
                        },
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "population_wide_antiphage_immunity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sdic1_system_trait",
                    "description": (
                        "SDIC1-mediated anti-phage immunity realizes the "
                        "SDIC1 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BAYER,
                            "snippet": SDIC_COHORT_SNIPPET,
                            "notes": (
                                "Bayer et al. identify SDIC1 in the newly "
                                "reported anti-phage system cohort."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sdic1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SDIC1 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": BAYER,
                            "snippet": SDIC_COHORT_SNIPPET,
                            "notes": (
                                "Bayer et al. identify SDIC1 among anti-phage "
                                "systems."
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
            "discussion_id": "sdic1-defensefinder-model-gap",
            "prompt": (
                "Resolve SDIC1 natural host breadth, SDIC1A/SDIC1B "
                "component functions, phage triggers, ubiquitination "
                "substrates, population-immunity mechanism, and rule-level "
                "detection criteria before minting narrower SDIC1 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bayer et al. support SDIC1 as a TIR-domain-containing "
                "anti-phage system with a ubiquitin-ligase-like component, "
                "and the pinned DefenseFinder HMM inventory records SDIC1A "
                "and SDIC1B profile rows. The pinned rules table has no "
                "SDIC1 row, and the first-pass record does not resolve "
                "natural host breadth, sensitive-phage breadth, the exact "
                "profile-to-component mapping, phage triggers, the direct "
                "TIR-dependent output, or the ubiquitination substrate."
            ),
            "evidence": [
                {
                    "reference": BAYER,
                    "snippet": TIR_SYSTEM_SNIPPET,
                    "notes": (
                        "Bayer et al. support SDIC1 as a TIR-domain "
                        "anti-phage system with a population-level output."
                    ),
                },
                {
                    "reference": BAYER,
                    "snippet": SDIC1_UBIQUITIN_SNIPPET,
                    "notes": (
                        "Bayer et al. connect SDIC1 with a TIR domain and a "
                        "ubiquitin-ligase-like component."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "SDIC1, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#sdic1_locus_restricts_phage"],
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
            "Minted SDIC1 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "candidate-locus level because the pinned DefenseFinder SDIC1 "
            f"HMM rows are not backed by a rules row; {PROPOSAL} reserves "
            "the replacement placeholder."
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
