#!/usr/bin/env python3
"""Add the DISARM1 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "disarm1_system.yaml"

OFIR_2018 = "DOI:10.1038/s41564-017-0051-0"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T15:17:43Z"
CANONICAL_TIMESTAMP = "2026-10-02T15:17:44Z"
IDENTIFIER = "traitmech:000548"
DISARM_PARENT_ID = "traitmech:000211"
PROPOSAL = "proposals/metpo_traitmech_v425"

ARTICLE_ROW = (
    "| DISARM | 10\\.1038/s41564-017-0051-0 | DISARM is a "
    "widespread bacterial defence system with broad anti-phage "
    "activities | "
)
RULE_ROW = (
    "DISARM\tDISARM_1\t4\t4\tDISARM_1__drmD, DISARM_1__drmMI, "
    "DISARM__drmA, DISARM__drmB, DISARM__drmC\t\t\t"
)
HMM_ROWS = (
    "| DISARM__drmA                                     |"
    " DISARM__drmA                                     |"
    " DISARM                 | Custom                  | 90     |\n"
    "| DISARM__drmB                                     |"
    " DISARM__drmB                                     |"
    " DISARM                 | Custom                  | 90     |\n"
    "| DISARM__drmC                                     |"
    " DISARM__drmC                                     |"
    " DISARM                 | Custom                  | 40     |\n"
    "| DISARM_1__drmD                                   |"
    " DISARM_1__drmD                                   |"
    " DISARM_1               | Custom                  | 500    |\n"
    "| DISARM_1__drmMI                                  |"
    " DISARM_1__drmMI                                  |"
    " DISARM_1               | Custom                  | 90     |"
)


def disarm_defense_evidence() -> dict[str, str]:
    return {
        "reference": OFIR_2018,
        "snippet": (
            "Our results establish DISARM as a new defence system, "
            "providing protection against diverse phages"
        ),
        "notes": (
            "Ofir et al. experimentally established DISARM as a "
            "broad-spectrum phage defense system."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DISARM "
            "source key to Ofir et al.'s DISARM phage-defense paper."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the shared "
            "DISARM drmA, drmB, and drmC profiles and the DISARM_1 "
            "drmD and drmMI profiles."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models DISARM_1 as a "
            "DISARM subsystem requiring four profiles from DISARM_1__drmD, "
            "DISARM_1__drmMI, DISARM__drmA, DISARM__drmB, and "
            "DISARM__drmC."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DISARM1 system",
    "definition": (
        "A DISARM system in which an organism possesses a genome-encoded "
        "DefenseFinder DISARM_1 subtype locus represented by DISARM_1__drmD, "
        "DISARM_1__drmMI, DISARM__drmA, DISARM__drmB, and DISARM__drmC "
        "rule profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DISARM_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DISARM_1",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "DISARM_1__drmD",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DISARM_1__drmMI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DISARM__drmA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DISARM__drmB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DISARM__drmC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        disarm_defense_evidence(),
        article_registry_evidence(),
        hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "disarm1_locus_subtype_defense",
            "title": "DISARM1 loci support DISARM antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DISARM_1 locus "
                "to DISARM methyltransferase-associated phage defense and "
                "DISARM1 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DISARM1 at DefenseFinder subtype-locus "
                "level without asserting the exact DISARM1 effector "
                "chemistry, native host breadth, sensitive-phage breadth, "
                "whether every DefenseFinder DISARM_1 prediction is a "
                "complete experimentally active locus, or how the shared "
                "DISARM drmA, drmB, and drmC profiles combine with the "
                "DISARM_1 drmD and drmMI profiles."
            ),
            "nodes": [
                {
                    "node_id": "disarm1_locus",
                    "label": "DISARM1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Defense Island System Associated with "
                        "Restriction-Modification subtype I locus "
                        "represented in DefenseFinder by DISARM_1 and "
                        "shared DISARM rule profiles."
                    ),
                },
                {
                    "node_id": "disarm_methyltransferase_antiphage_defense",
                    "label": "DISARM methyltransferase-associated antiphage defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Methyltransferase-associated DISARM phage defense "
                        "carried by a genome-encoded DISARM locus."
                    ),
                },
                {
                    "node_id": "disarm1_system_trait",
                    "label": "DISARM1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DISARM1 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "disarm_system_trait",
                    "label": "DISARM system",
                    "node_type": "TRAIT",
                    "grounding": DISARM_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded DISARM "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "disarm1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "disarm_methyltransferase_antiphage_defense",
                    "description": (
                        "DISARM1 loci are represented in DefenseFinder by "
                        "shared DISARM drmA, drmB, and drmC profiles plus "
                        "DISARM_1-specific drmD and drmMI profiles."
                    ),
                    "evidence": [
                        hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "disarm_methyltransferase_antiphage_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "disarm1_system_trait",
                    "description": (
                        "The first-pass DISARM1 system trait is realized by "
                        "a DefenseFinder DISARM_1 subtype locus within the "
                        "methyltransferase-associated DISARM family."
                    ),
                    "evidence": [
                        disarm_defense_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "disarm1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "disarm_system_trait",
                    "description": (
                        "DISARM1 system possession is a DISARM-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "disarm1-profile-activity-gap",
            "prompt": (
                "Resolve DISARM1 effector chemistry, exact native hosts, "
                "sensitive-phage breadth, shared-core component roles, "
                "and DISARM_1 profile-to-activity criteria before minting "
                "DISARM1 mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Ofir et al. support DISARM as a broad antiphage-system "
                "family, and the pinned DefenseFinder HMM inventory and "
                "rules table support DISARM_1 as a subtype with drmD, "
                "drmMI, drmA, drmB, and drmC profiles. This first-pass "
                "record leaves exact DISARM1 effector chemistry, native "
                "host breadth, sensitive-phage breadth, shared-core "
                "component roles, and profile-to-activity requirements "
                "unresolved."
            ),
            "evidence": [
                disarm_defense_evidence(),
                hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#disarm1_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
        }
    ],
}


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted DISARM1 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the DISARM system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "DISARM1 TraitMech, METPO, history, or prior proposal record; "
            "the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DISARM1 system during initial curation and left "
            "canonical_examples empty because Ofir et al. and the pinned "
            "DefenseFinder tables support the DISARM family and the "
            "DISARM_1 model namespace but not an accession-backed native "
            "microbial taxon exemplar tied to DISARM_1 profiles and "
            "experimentally verified endogenous DISARM1 activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    validate_outputs(record)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
    else:
        print(
            "DISARM1 system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
