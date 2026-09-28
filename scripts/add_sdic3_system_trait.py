#!/usr/bin/env python3
"""Add the SDIC3 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sdic3_system.yaml"

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
TIMESTAMP = "2026-09-28T01:42:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T01:42:01Z"

IDENTIFIER = "traitmech:000423"
PROPOSAL = "proposals/metpo_traitmech_v300"

SDIC_CANDIDATE_SNIPPET = (
    "Using this approach, we identified three candidate anti-phage "
    "systems/subtypes, which were renamed SDIC1–3"
)
SDIC3_ACTIVITY_SNIPPET = (
    "In E. coli, SDIC1, SDIC2, and SDIC3 confer strong protection against "
    "several phages (R1,000-fold), including those from the Durham collection"
)
SDIC_PLASMID_SNIPPET = (
    "The four candidates were cloned into a low-copy plasmid under the "
    "control of a constitutive promoter compatible with expression in E. "
    "coli and S. marcescens"
)
ARTICLE_ROW = (
    "| SDIC3 | 10\\.1016/j\\.celrep\\.2024\\.115055 | Multi-conflict "
    "islands are a widespread trend within Serratia spp |"
)
HMM_PROFILE_SNIPPETS = {
    "SDIC3__SDIC3B": (
        "| SDIC3__SDIC3B                                    |"
        "                                                  | SDIC3"
        "                  | Custom                  | 20     |"
    ),
    "SDIC3__SDIC3C": (
        "| SDIC3__SDIC3C                                    |"
        "                                                  | SDIC3"
        "                  | Custom                  | 220    |"
    ),
    "SDIC3__SDIC3D": (
        "| SDIC3__SDIC3D                                    |"
        "                                                  | SDIC3"
        "                  | Custom                  | 40     |"
    ),
    "SDIC3__SDIC3E": (
        "| SDIC3__SDIC3E                                    |"
        "                                                  | SDIC3"
        "                  | Custom                  | 80     |"
    ),
    "SDIC3__SDIC3F": (
        "| SDIC3__SDIC3F                                    |"
        "                                                  | SDIC3"
        "                  | Custom                  | 600    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the SDIC3 "
            "source key to the Cummins et al. Serratia multi-conflict-island "
            "paper."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom SDIC3 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SDIC3 system",
    "definition": (
        "A phage defense system in which an organism possesses an SDIC3 "
        "Serratia defense-island candidate locus that can confer strong "
        "protection against several bacteriophages when plasmid expressed."
    ),
    "definition_source": CUMMINS,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "SDIC3",
            "synonym_type": "EXACT_SYNONYM",
            "source": CUMMINS,
        },
        {
            "synonym_text": "SDIC3__SDIC3B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC3__SDIC3C",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC3__SDIC3D",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC3__SDIC3E",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "SDIC3__SDIC3F",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": CUMMINS,
            "snippet": SDIC_CANDIDATE_SNIPPET,
            "notes": (
                "Cummins et al. identify SDIC3 as one of three Serratia "
                "defense-island candidate anti-phage systems or subtypes."
            ),
        },
        {
            "reference": CUMMINS,
            "snippet": SDIC3_ACTIVITY_SNIPPET,
            "notes": (
                "Cummins et al. show that plasmid-expressed SDIC3 can "
                "strongly protect E. coli against several bacteriophages."
            ),
        },
        {
            "reference": CUMMINS,
            "snippet": SDIC_PLASMID_SNIPPET,
            "notes": (
                "Cummins et al. assayed the four SDIC candidates from "
                "low-copy plasmids under a constitutive promoter."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "sdic3_locus_restricts_phage",
            "title": "SDIC3 loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking an SDIC3 locus to "
                "reduced bacteriophage propagation without resolving exact "
                "SDIC3 components or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SDIC3 as a named anti-phage system with "
                "DefenseFinder SDIC3B, SDIC3C, SDIC3D, SDIC3E, and SDIC3F "
                "profile rows. It does not assert native host breadth, "
                "SDIC3A status, exact profile-to-protein correspondence, "
                "whether SDIC3 is a distinct ECOR61-system subtype, "
                "sensitive-phage breadth, the direct trigger, the molecular "
                "output, or DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "sdic3_locus",
                    "label": "SDIC3 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An SDIC3 candidate anti-phage locus represented in "
                        "the pinned DefenseFinder HMM inventory by custom "
                        "SDIC3B, SDIC3C, SDIC3D, SDIC3E, and SDIC3F "
                        "profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "a plasmid-expressed SDIC3 candidate anti-phage "
                        "system."
                    ),
                },
                {
                    "node_id": "sdic3_system_trait",
                    "label": "SDIC3 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SDIC3 phage-defense "
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
                    "subject": "sdic3_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The SDIC3 candidate locus contributes to strong "
                        "restriction of bacteriophage propagation when "
                        "plasmid expressed."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC_CANDIDATE_SNIPPET,
                            "notes": (
                                "Cummins et al. identify SDIC3 as an "
                                "anti-phage candidate found in Serratia "
                                "defense islands."
                            ),
                        },
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC3_ACTIVITY_SNIPPET,
                            "notes": (
                                "Cummins et al. report strong SDIC3-mediated "
                                "protection against multiple phages."
                            ),
                        },
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sdic3_system_trait",
                    "description": (
                        "SDIC3-mediated phage restriction realizes the SDIC3 "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC3_ACTIVITY_SNIPPET,
                            "notes": (
                                "Cummins et al. connect SDIC3 with strong "
                                "phage protection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sdic3_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SDIC3 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUMMINS,
                            "snippet": SDIC_CANDIDATE_SNIPPET,
                            "notes": (
                                "Cummins et al. identify SDIC3 as an "
                                "anti-phage candidate found in Serratia "
                                "defense islands."
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
            "discussion_id": "sdic3-defensefinder-model-gap",
            "prompt": (
                "Resolve SDIC3 natural host breadth, SDIC3A status, exact "
                "SDIC3B/SDIC3C/SDIC3D/SDIC3E/SDIC3F component functions, "
                "sensitive-phage breadth, ECOR61-system subtype scope, the "
                "direct trigger and molecular output, and rule-level "
                "detection criteria before minting narrower SDIC3 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cummins et al. support SDIC3 as a Serratia defense-island "
                "candidate anti-phage system that can strongly protect E. "
                "coli when plasmid expressed, and the pinned DefenseFinder "
                "HMM inventory records SDIC3B, SDIC3C, SDIC3D, SDIC3E, "
                "and SDIC3F profile rows. The pinned rules table has no "
                "SDIC3 row, and the first-pass record does not resolve "
                "natural host breadth, whether SDIC3A is part of the "
                "DefenseFinder-detectable system, phage target breadth, "
                "ECOR61 anti-phage-system boundaries, or the direct "
                "molecular output."
            ),
            "evidence": [
                {
                    "reference": CUMMINS,
                    "snippet": SDIC_CANDIDATE_SNIPPET,
                    "notes": (
                        "Cummins et al. identify SDIC3 as a Serratia "
                        "defense-island candidate."
                    ),
                },
                {
                    "reference": CUMMINS,
                    "snippet": SDIC3_ACTIVITY_SNIPPET,
                    "notes": (
                        "Cummins et al. report strong phage protection in "
                        "E. coli."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "SDIC3, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#sdic3_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-28",
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
            "Minted SDIC3 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at candidate-locus level "
            "because the pinned DefenseFinder SDIC3 HMM rows are not backed "
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
            "Reviewed SDIC3 system canonical_examples and left them empty "
            "because Cummins et al. support plasmid-expressed E. coli and "
            "S. marcescens phage-challenge assays plus a DefenseFinder "
            "SDIC3 system model, but not a direct native microbial isolate "
            "exemplar with experimentally verified endogenous SDIC3 "
            "activity. No paid research was used."
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
