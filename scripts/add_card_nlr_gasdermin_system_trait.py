"""Add the CARD-NLR GasderMIN system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402, RUF100
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402, RUF100

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "card_nlr_gasdermin_system.yaml"
)
CARD_NLR_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "card_nlr_system.yaml"

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
TIMESTAMP = "2026-10-02T21:05:00Z"
PARENT_TIMESTAMP = "2026-10-02T21:05:01Z"
CANONICAL_TIMESTAMP = "2026-10-02T21:05:02Z"
IDENTIFIER = "traitmech:000555"
CARD_NLR_PARENT_ID = "traitmech:000337"
PROPOSAL = "proposals/metpo_traitmech_v432"

WEIN_CARD_SNIPPET = (
    "Here we show that CARD-like domains are present in defense systems "
    "that protect bacteria against phage."
)
WEIN_GASDERMIN_SNIPPET = (
    "The bacterial CARD is essential for protease-mediated activation of "
    "certain bacterial gasdermins, which promote cell death once phage "
    "infection is recognized."
)
ARTICLE_ROW = (
    "| CARD_NLR | 10\\.1101/2023\\.05\\.28\\.542683 | CARD-like domains "
    "mediate anti-phage defense in bacterial gasdermin systems | "
)
GASDERMIN_HMM_ROW = (
    "| GasderMIN__bGSDM                                 |"
    " GasderMIN__bGSDM___bGSDM                         |"
    " GasderMIN              | Custom                  | 50     |"
)
RULE_ROW = (
    "CARD_NLR\tCARD_NLR_GasderMIN\t1\t3\tGasderMIN__bGSDM\t"
    "CARD_NLR__CARD_Protease, CARD_NLR__NLR_new, CARD_NLR__Trypsin\t"
    "CARD_NLR__Endonuclease, CARD_NLR__Endonuclease_new, "
    "CARD_NLR__Phospho, CARD_NLR__Phospho_Trypsin, CARD_NLR__Subtilase, "
    "CARD_NLR__Subtilase_long_new, CARD_NLR__Subtilase_small_new, "
    "CARD_NLR__Trypsin_Phospho, CARD_NLR__Trypsine_Endonuclease_new\t"
)
RULE_SUBTYPE_PROFILE_SPAN = (
    "CARD_NLR_GasderMIN\t1\t3\tGasderMIN__bGSDM\t"
    "CARD_NLR__CARD_Protease, CARD_NLR__NLR_new, CARD_NLR__Trypsin"
)
RULE_PARENT_SPAN = "CARD_NLR\tCARD_NLR_GasderMIN\t1\t3\tGasderMIN__bGSDM"


def wein_card_evidence() -> dict[str, str]:
    return {
        "reference": WEIN_EUROPE_PMC,
        "snippet": WEIN_CARD_SNIPPET,
        "notes": (
            "Wein et al. support bacterial CARD-like domains as parts of "
            "anti-phage defense systems."
        ),
    }


def wein_gasdermin_evidence() -> dict[str, str]:
    return {
        "reference": WEIN_EUROPE_PMC,
        "snippet": WEIN_GASDERMIN_SNIPPET,
        "notes": (
            "Wein et al. support bacterial CARD-dependent activation of "
            "phage-triggered gasdermin cell-death effectors."
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


def gasdermin_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": GASDERMIN_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "GasderMIN__bGSDM profile reused as mandatory by the "
            "CARD_NLR_GasderMIN rule row."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models "
            "CARD_NLR_GasderMIN as a CARD_NLR subsystem requiring "
            "GasderMIN__bGSDM with CARD_Protease, NLR_new, and Trypsin "
            "accessory profiles."
        ),
    }


def rules_subtype_profile_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_SUBTYPE_PROFILE_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table models "
            "CARD_NLR_GasderMIN as a CARD_NLR subsystem requiring "
            "GasderMIN__bGSDM with CARD_Protease, NLR_new, and Trypsin "
            "accessory profiles."
        ),
    }


def rules_parent_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_PARENT_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table places the "
            "CARD_NLR_GasderMIN subsystem under the CARD_NLR system key "
            "and requires GasderMIN__bGSDM."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CARD-NLR GasderMIN system",
    "definition": (
        "A CARD-NLR system in which an organism possesses a genome-encoded "
        "DefenseFinder CARD_NLR_GasderMIN subtype locus represented by "
        "the CARD_NLR_GasderMIN rule row requiring the GasderMIN__bGSDM "
        "profile."
    ),
    "definition_source": WEIN_2023,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [CARD_NLR_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "CARD_NLR_GasderMIN",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "GasderMIN__bGSDM",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
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
        wein_gasdermin_evidence(),
        article_registry_evidence(),
        gasdermin_hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "card_nlr_gasdermin_locus_subtype_defense",
            "title": "CARD-NLR GasderMIN loci mark a CARD-NLR antiphage subtype",
            "description": (
                "Conservative subtype-level sketch linking a DefenseFinder "
                "CARD_NLR_GasderMIN locus to CARD-like gasdermin "
                "anti-phage defense and CARD-NLR GasderMIN system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the CARD_NLR_GasderMIN subtype at "
                "DefenseFinder rule-row level without asserting the exact "
                "phage trigger, native host breadth, CARD-to-gasdermin "
                "activation sequence, bGSDM cleavage route, or whether "
                "every DefenseFinder CARD_NLR_GasderMIN prediction is a "
                "complete experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "card_nlr_gasdermin_locus",
                    "label": "CARD-NLR GasderMIN locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder CARD_NLR_GasderMIN subtype locus "
                        "represented by the GasderMIN__bGSDM mandatory "
                        "profile and generic CARD_NLR accessory profiles."
                    ),
                },
                {
                    "node_id": "card_like_gasdermin_antiphage_defense",
                    "label": "CARD-like gasdermin antiphage defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Anti-phage defense mediated by bacterial "
                        "CARD-like activation of a gasdermin cell-death "
                        "effector."
                    ),
                },
                {
                    "node_id": "card_nlr_gasdermin_system_trait",
                    "label": "CARD-NLR GasderMIN system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CARD-NLR "
                        "GasderMIN phage-defense system."
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
                    "subject": "card_nlr_gasdermin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "card_like_gasdermin_antiphage_defense",
                    "description": (
                        "CARD_NLR_GasderMIN loci are represented in "
                        "DefenseFinder by a GasderMIN__bGSDM mandatory "
                        "profile plus CARD_NLR accessory profiles."
                    ),
                    "evidence": [
                        gasdermin_hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "card_like_gasdermin_antiphage_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "card_nlr_gasdermin_system_trait",
                    "description": (
                        "The first-pass CARD-NLR GasderMIN system trait is "
                        "realized by a DefenseFinder CARD_NLR_GasderMIN "
                        "subtype locus."
                    ),
                    "evidence": [
                        wein_card_evidence(),
                        wein_gasdermin_evidence(),
                        rules_subtype_profile_evidence(),
                    ],
                },
                {
                    "subject": "card_nlr_gasdermin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "card_nlr_system_trait",
                    "description": (
                        "CARD-NLR GasderMIN system possession is a "
                        "CARD-NLR-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_parent_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "card-nlr-gasdermin-activity-gap",
            "prompt": (
                "Resolve the CARD_NLR_GasderMIN phage triggers, native "
                "hosts, gasdermin proteolysis route, CARD-to-gasdermin "
                "activation sequence, and profile-to-activity criteria "
                "before minting protease, trigger, or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wein et al. support CARD-like anti-phage gasdermin "
                "defense, the pinned DefenseFinder HMM inventory supports "
                "GasderMIN__bGSDM as a bGSDM profile, and the pinned "
                "DefenseFinder rules table supports CARD_NLR_GasderMIN as "
                "a rule-row subtype requiring GasderMIN__bGSDM. This "
                "first-pass record leaves exact phage triggers, native "
                "hosts, CARD-to-gasdermin activation, bGSDM proteolysis "
                "route, and profile-to-activity criteria unresolved."
            ),
            "evidence": [
                wein_gasdermin_evidence(),
                gasdermin_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#card_nlr_gasdermin_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
        }
    ],
}

UPDATED_CARD_NLR_DISCUSSION_RATIONALE = (
    "Wein et al. support CARD-like domains in multiple anti-phage defense "
    "systems that activate cell-death effectors, and DefenseFinder models "
    "CARD_NLR subtypes with gasdermin, endonuclease, CARD_NLR_Phospho, "
    "CARD_NLR_Subtilase, and CARD_NLR_like rule profiles. CARD-NLR "
    "GasderMIN, endonuclease, phospho, and subtilase TraitRecords now "
    "capture four rule-row subtypes, but exact phage triggers, "
    "CARD-to-effector activation sequence, accession-level natural-host "
    "components, CARD_NLR_Subtilase_long_new HMM inventory coverage, "
    "CARD_NLR_like boundaries, and standalone GasderMIN versus "
    "CARD_NLR_GasderMIN mechanism boundaries remain unresolved."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted CARD-NLR GasderMIN system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the CARD-NLR "
            "system parent after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record for the target local ID, placeholder METPO "
            "ID, proposal cohort, record slug, or human label; existing "
            "CARD_NLR_GasderMIN mentions were scoped to CARD-NLR parent "
            "or GasderMIN evidence, not an exact child TraitRecord, and "
            f"the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed CARD-NLR GasderMIN system during initial curation "
            "and left canonical_examples empty because Wein et al. and "
            "the pinned DefenseFinder tables support CARD-like "
            "anti-phage gasdermin defense and the CARD_NLR_GasderMIN "
            "rule row but not an accession-backed native microbial taxon "
            "exemplar tied to CARD_NLR_GasderMIN profiles and "
            "experimentally verified endogenous activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    return record


def build_parent() -> dict[str, Any]:
    record = yaml.safe_load(CARD_NLR_PARENT.read_text())
    assert record["identifier"] == CARD_NLR_PARENT_ID
    assert record["label"] == "CARD-NLR system"
    assert record["mapping_status"] == "PROPOSED"

    discussion = next(
        item
        for item in record["discussions"]
        if item["discussion_id"] == "card-nlr-subtype-mechanism-gap"
    )
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    if discussion["rationale"] != UPDATED_CARD_NLR_DISCUSSION_RATIONALE:
        assert "CARD_NLR_GasderMIN context remain unresolved" in discussion["rationale"]
        discussion["rationale"] = UPDATED_CARD_NLR_DISCUSSION_RATIONALE

    if not any(
        event["timestamp"] == PARENT_TIMESTAMP
        and event["action"] == "TRACK_NARROWER_RECORD"
        for event in record.get("curation_history", [])
    ):
        record_curation_event(
            record,
            curator=CURATOR,
            action="TRACK_NARROWER_RECORD",
            changes=(
                "Documented CARD-NLR GasderMIN as split out in the open "
                "CARD-NLR subtype discussion after minting traitmech:000555 "
                "for the DefenseFinder-backed CARD_NLR_GasderMIN child; "
                "CARD_NLR_like and finer CARD-NLR activation mechanisms "
                "remain open."
            ),
            llm_assisted=True,
            timestamp=PARENT_TIMESTAMP,
        )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / CARD_NLR_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = build_parent()
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            existing = yaml.safe_load(TARGET.read_text())
            if existing.get("identifier") != IDENTIFIER:
                raise SystemExit(f"{TARGET} already exists with another identifier")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, CARD_NLR_PARENT)
    else:
        print(
            "CARD-NLR GasderMIN system trait and parent update validate; "
            f"rerun with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
