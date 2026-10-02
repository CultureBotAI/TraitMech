"""Add the CARD-NLR endonuclease system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "card_nlr_endonuclease_system.yaml"

WEIN_2023 = "DOI:10.1101/2023.05.28.542683"
WEIN_EUROPE_PMC = "https://europepmc.org/article/PPR/PPR668921"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T16:57:23Z"
CANONICAL_TIMESTAMP = "2026-10-02T16:57:24Z"
IDENTIFIER = "traitmech:000550"
CARD_NLR_PARENT_ID = "traitmech:000337"
PROPOSAL = "proposals/metpo_traitmech_v427"

WEIN_CARD_SNIPPET = (
    "Here we show that CARD-like domains are present in defense systems "
    "that protect bacteria against phage."
)
ARTICLE_ROW = (
    "| CARD_NLR | 10\\.1101/2023\\.05\\.28\\.542683 | CARD-like domains "
    "mediate anti-phage defense in bacterial gasdermin systems | "
)
RULE_ROW = (
    "CARD_NLR\tCARD_NLR_Endonuclease\t1\t3\tCARD_NLR__Endonuclease\t"
    "CARD_NLR__CARD_Protease, CARD_NLR__NLR_new, CARD_NLR__Trypsin\t"
    "CARD_NLR__Phospho, CARD_NLR__Phospho_Trypsin, "
    "CARD_NLR__Subtilase, CARD_NLR__Subtilase_long_new, "
    "CARD_NLR__Subtilase_small_new, CARD_NLR__Trypsin_Phospho, "
    "GasderMIN__bGSDM\t"
)
ENDONUCLEASE_HMM_ROW = (
    "| CARD_NLR__Endonuclease                           |"
    " CARD_NLR__Endonuclease                           |"
    " CARD_NLR               | Custom                  | 500    |"
)


def wein_card_evidence() -> dict[str, str]:
    return {
        "reference": WEIN_EUROPE_PMC,
        "snippet": WEIN_CARD_SNIPPET,
        "notes": (
            "Wein et al. support bacterial CARD-like domains as parts of "
            "anti-phage defense systems."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the CARD_NLR "
            "model namespace to the Wein et al. CARD-like-domain "
            "anti-phage defense preprint."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ENDONUCLEASE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "CARD_NLR__Endonuclease as a custom CARD_NLR profile."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models "
            "CARD_NLR_Endonuclease as a CARD_NLR subsystem requiring the "
            "CARD_NLR__Endonuclease profile with CARD_Protease, NLR_new, "
            "and Trypsin accessory profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CARD-NLR endonuclease system",
    "definition": (
        "A CARD-NLR system in which an organism possesses a genome-encoded "
        "DefenseFinder CARD_NLR_Endonuclease subtype locus represented by "
        "the CARD_NLR__Endonuclease mandatory rule profile."
    ),
    "definition_source": WEIN_2023,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [CARD_NLR_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "CARD_NLR_Endonuclease",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "CARD_NLR__Endonuclease",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "CARD_NLR__CARD_Protease",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "CARD_NLR__NLR_new",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "CARD_NLR__Trypsin",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        wein_card_evidence(),
        article_registry_evidence(),
        hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "card_nlr_endonuclease_locus_subtype_defense",
            "title": "CARD-NLR endonuclease loci mark a CARD-NLR antiphage subtype",
            "description": (
                "Conservative subtype-level sketch linking a DefenseFinder "
                "CARD_NLR_Endonuclease locus to CARD-like anti-phage "
                "defense and CARD-NLR endonuclease system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the CARD_NLR_Endonuclease subtype at "
                "DefenseFinder rule-row level without asserting the exact "
                "endonuclease effector substrate, phage trigger, native "
                "host breadth, CARD-to-effector activation sequence, or "
                "whether every DefenseFinder CARD_NLR_Endonuclease "
                "prediction is a complete experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "card_nlr_endonuclease_locus",
                    "label": "CARD-NLR endonuclease locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder CARD_NLR_Endonuclease subtype "
                        "locus represented by the mandatory "
                        "CARD_NLR__Endonuclease profile and generic "
                        "CARD_NLR accessory profiles."
                    ),
                },
                {
                    "node_id": "card_like_antiphage_defense",
                    "label": "CARD-like antiphage defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Anti-phage defense mediated by a bacterial "
                        "CARD-like defense system."
                    ),
                },
                {
                    "node_id": "card_nlr_endonuclease_system_trait",
                    "label": "CARD-NLR endonuclease system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CARD-NLR "
                        "endonuclease phage-defense system."
                    ),
                },
                {
                    "node_id": "card_nlr_system_trait",
                    "label": "CARD-NLR system",
                    "node_type": "TRAIT",
                    "grounding": CARD_NLR_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded CARD-NLR "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "card_nlr_endonuclease_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "card_like_antiphage_defense",
                    "description": (
                        "CARD_NLR_Endonuclease loci are represented in "
                        "DefenseFinder by a CARD_NLR__Endonuclease "
                        "mandatory profile plus CARD_NLR accessory profiles."
                    ),
                    "evidence": [
                        hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "card_like_antiphage_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "card_nlr_endonuclease_system_trait",
                    "description": (
                        "The first-pass CARD-NLR endonuclease system trait "
                        "is realized by a DefenseFinder "
                        "CARD_NLR_Endonuclease subtype locus."
                    ),
                    "evidence": [
                        wein_card_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "card_nlr_endonuclease_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "card_nlr_system_trait",
                    "description": (
                        "CARD-NLR endonuclease system possession is a "
                        "CARD-NLR-system trait."
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
            "discussion_id": "card-nlr-endonuclease-activity-gap",
            "prompt": (
                "Resolve the CARD_NLR_Endonuclease phage triggers, native "
                "hosts, endonuclease effector substrate, CARD-to-effector "
                "activation sequence, and profile-to-activity criteria "
                "before minting enzyme, trigger, or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wein et al. support CARD-like anti-phage defense systems, "
                "and the pinned DefenseFinder HMM inventory and rules table "
                "support CARD_NLR_Endonuclease as a subtype with a "
                "CARD_NLR__Endonuclease mandatory profile. This first-pass "
                "record leaves exact phage triggers, native hosts, "
                "accessory-profile requirements, nuclease substrate, and "
                "CARD-to-endonuclease activation unresolved."
            ),
            "evidence": [
                wein_card_evidence(),
                hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#card_nlr_endonuclease_locus_subtype_defense",
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
            "Minted CARD-NLR endonuclease system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the CARD-NLR "
            "system parent after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record for the target local ID, placeholder METPO "
            f"ID, proposal cohort, record slug, or human label; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed CARD-NLR endonuclease system during initial "
            "curation and left canonical_examples empty because Wein et "
            "al. and the pinned DefenseFinder tables support CARD-like "
            "anti-phage defense and the CARD_NLR_Endonuclease model "
            "namespace but not an accession-backed native microbial taxon "
            "exemplar tied to CARD_NLR_Endonuclease profiles and "
            "experimentally verified endogenous CARD-NLR endonuclease "
            "activity. No paid research was used."
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
            "CARD-NLR endonuclease system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
