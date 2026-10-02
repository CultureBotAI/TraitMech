#!/usr/bin/env python3
"""Add the DISARM2 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402, RUF100
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402, RUF100

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "disarm2_system.yaml"

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
TIMESTAMP = "2026-10-02T15:56:12Z"
CANONICAL_TIMESTAMP = "2026-10-02T15:56:13Z"
IDENTIFIER = "traitmech:000549"
DISARM_PARENT_ID = "traitmech:000211"
PROPOSAL = "proposals/metpo_traitmech_v426"

ARTICLE_ROW = (
    "| DISARM | 10\\.1038/s41564-017-0051-0 | DISARM is a "
    "widespread bacterial defence system with broad anti-phage "
    "activities | "
)
RULE_ROW = (
    "DISARM\tDISARM_2\t4\t4\tDISARM_2__drmE, DISARM_2__drmMII, "
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
    "| DISARM_2__drmE                                   |"
    " DISARM_2__drmE                                   |"
    " DISARM_2               | Custom                  | 90     |\n"
    "| DISARM_2__drmMII                                 |"
    " DISARM_2__drmMII                                 |"
    " DISARM_2               | Custom                  | 90     |"
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
            "DISARM drmA, drmB, and drmC profiles and the DISARM_2 "
            "drmE and drmMII profiles."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models DISARM_2 as a "
            "DISARM subsystem requiring four profiles from DISARM_2__drmE, "
            "DISARM_2__drmMII, DISARM__drmA, DISARM__drmB, and "
            "DISARM__drmC."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DISARM2 system",
    "definition": (
        "A DISARM system in which an organism possesses a genome-encoded "
        "DefenseFinder DISARM_2 subtype locus represented by DISARM_2__drmE, "
        "DISARM_2__drmMII, DISARM__drmA, DISARM__drmB, and DISARM__drmC "
        "rule profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DISARM_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DISARM_2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "DISARM_2__drmE",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DISARM_2__drmMII",
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
            "graph_id": "disarm2_locus_subtype_defense",
            "title": "DISARM2 loci support DISARM antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DISARM_2 locus "
                "to DISARM methyltransferase-associated phage defense and "
                "DISARM2 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DISARM2 at DefenseFinder subtype-locus "
                "level without asserting the exact DISARM2 effector "
                "chemistry, native host breadth, sensitive-phage breadth, "
                "whether every DefenseFinder DISARM_2 prediction is a "
                "complete experimentally active locus, or how the shared "
                "DISARM drmA, drmB, and drmC profiles combine with the "
                "DISARM_2 drmE and drmMII profiles."
            ),
            "nodes": [
                {
                    "node_id": "disarm2_locus",
                    "label": "DISARM2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Defense Island System Associated with "
                        "Restriction-Modification subtype II locus "
                        "represented in DefenseFinder by DISARM_2 and "
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
                    "node_id": "disarm2_system_trait",
                    "label": "DISARM2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DISARM2 "
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
                    "subject": "disarm2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "disarm_methyltransferase_antiphage_defense",
                    "description": (
                        "DISARM2 loci are represented in DefenseFinder by "
                        "shared DISARM drmA, drmB, and drmC profiles plus "
                        "DISARM_2-specific drmE and drmMII profiles."
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
                    "object": "disarm2_system_trait",
                    "description": (
                        "The first-pass DISARM2 system trait is realized by "
                        "a DefenseFinder DISARM_2 subtype locus within the "
                        "methyltransferase-associated DISARM family."
                    ),
                    "evidence": [
                        disarm_defense_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "disarm2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "disarm_system_trait",
                    "description": (
                        "DISARM2 system possession is a DISARM-system trait."
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
            "discussion_id": "disarm2-profile-activity-gap",
            "prompt": (
                "Resolve DISARM2 effector chemistry, exact native hosts, "
                "sensitive-phage breadth, shared-core component roles, "
                "and DISARM_2 profile-to-activity criteria before minting "
                "DISARM2 mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Ofir et al. support DISARM as a broad antiphage-system "
                "family, and the pinned DefenseFinder HMM inventory and "
                "rules table support DISARM_2 as a subtype with drmE, "
                "drmMII, drmA, drmB, and drmC profiles. This first-pass "
                "record leaves exact DISARM2 effector chemistry, native "
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
                "causal_graphs#disarm2_locus_subtype_defense",
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
            "Minted DISARM2 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the DISARM system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "DISARM2 TraitMech, METPO, history, or prior proposal record; "
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
            "Reviewed DISARM2 system during initial curation and left "
            "canonical_examples empty because Ofir et al. and the pinned "
            "DefenseFinder tables support the DISARM family and the "
            "DISARM_2 model namespace but not an accession-backed native "
            "microbial taxon exemplar tied to DISARM_2 profiles and "
            "experimentally verified endogenous DISARM2 activity. No paid "
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
            "DISARM2 system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
