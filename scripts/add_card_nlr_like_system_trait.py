"""Add the CARD-NLR-like system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "card_nlr_like_system.yaml"
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
TIMESTAMP = "2026-10-03T00:02:50Z"
PARENT_TIMESTAMP = "2026-10-03T00:02:51Z"
CANONICAL_TIMESTAMP = "2026-10-03T00:02:52Z"
IDENTIFIER = "traitmech:000559"
CARD_NLR_PARENT_ID = "traitmech:000337"
PROPOSAL = "proposals/metpo_traitmech_v436"

WEIN_CARD_SNIPPET = (
    "Here we show that CARD-like domains are present in defense systems "
    "that protect bacteria against phage."
)
ARTICLE_ROW = (
    "| CARD_NLR | 10\\.1101/2023\\.05\\.28\\.542683 | CARD-like domains "
    "mediate anti-phage defense in bacterial gasdermin systems | "
)
ENDONUCLEASE_HMM_ROW = (
    "| CARD_NLR__Endonuclease                           |"
    " CARD_NLR__Endonuclease                           |"
    " CARD_NLR               | Custom                  | 500    |"
)
PHOSPHO_TRYPSIN_HMM_ROW = (
    "| CARD_NLR__Phospho_Trypsin                        |"
    " CARD_NLR__Phospho_Trypsin                        |"
    " CARD_NLR               | Custom                  | 1000   |"
)
TRYPSIN_PHOSPHO_HMM_ROW = (
    "| CARD_NLR__Trypsin_Phospho                        |"
    " CARD_NLR__Trypsin_Phospho                        |"
    " CARD_NLR               | Custom                  | 400    |"
)
RULE_ROW = (
    "CARD_NLR\tCARD_NLR_like\t2\t4\tCARD_NLR__Endonuclease, "
    "CARD_NLR__Phospho_Trypsin, CARD_NLR__Subtilase_long_new, "
    "CARD_NLR__Trypsin_Phospho\tCARD_NLR__CARD_Protease, "
    "CARD_NLR__NLR_new, CARD_NLR__Trypsin\t\t"
)
RULE_PROFILE_SPAN = (
    "CARD_NLR_like\t2\t4\tCARD_NLR__Endonuclease, "
    "CARD_NLR__Phospho_Trypsin, CARD_NLR__Subtilase_long_new, "
    "CARD_NLR__Trypsin_Phospho"
)
RULE_PARENT_SPAN = "CARD_NLR\tCARD_NLR_like\t2\t4"


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


def endonuclease_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ENDONUCLEASE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "CARD_NLR__Endonuclease custom profile listed among "
            "the candidate effector profiles by the CARD_NLR_like rule row."
        ),
    }


def phospho_trypsin_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": PHOSPHO_TRYPSIN_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "CARD_NLR__Phospho_Trypsin custom profile listed among "
            "the candidate effector profiles by the CARD_NLR_like rule row."
        ),
    }


def trypsin_phospho_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": TRYPSIN_PHOSPHO_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "CARD_NLR__Trypsin_Phospho custom profile listed among "
            "the candidate effector profiles by the CARD_NLR_like rule row."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models CARD_NLR_like as "
            "a CARD_NLR subsystem requiring two matches from a four-profile "
            "candidate effector set."
        ),
    }


def rules_profile_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_PROFILE_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table models CARD_NLR_like "
            "with two required matches from Endonuclease, Phospho_Trypsin, "
            "Subtilase_long_new, and Trypsin_Phospho candidate effector "
            "profiles."
        ),
    }


def rules_parent_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_PARENT_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table places the "
            "CARD_NLR_like subsystem under the CARD_NLR system key with "
            "two mandatory matches and four genes required."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CARD-NLR-like system",
    "definition": (
        "A CARD-NLR system in which an organism possesses a genome-encoded "
        "DefenseFinder CARD_NLR_like subtype locus represented by the "
        "CARD_NLR_like rule row requiring two matches from the "
        "CARD_NLR__Endonuclease, CARD_NLR__Phospho_Trypsin, "
        "CARD_NLR__Subtilase_long_new, and CARD_NLR__Trypsin_Phospho "
        "effector-profile set."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [CARD_NLR_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "CARD_NLR_like",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        }
    ],
    "evidence": [
        wein_card_evidence(),
        article_registry_evidence(),
        endonuclease_hmm_evidence(),
        phospho_trypsin_hmm_evidence(),
        trypsin_phospho_hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "card_nlr_like_locus_subtype_defense",
            "title": "CARD-NLR-like is a DefenseFinder CARD-NLR subtype",
            "description": (
                "Conservative subtype-level classification linking the "
                "DefenseFinder CARD_NLR_like rule-row definition to "
                "CARD-NLR-like system possession and its CARD-NLR parent."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures CARD_NLR_like as a DefenseFinder "
                "rule-row subtype of CARD-NLR system possession without "
                "asserting a CARD_NLR_like-specific antiphage process, "
                "expanding any profile names, selecting which two of the "
                "four candidate effector profiles realize activity, "
                "resolving the absent CARD_NLR__Subtilase_long_new HMM "
                "inventory row, or resolving exact phage triggers, native "
                "host breadth, CARD-to-effector activation sequence, "
                "cell-death output, or whether every DefenseFinder "
                "CARD_NLR_like prediction is a complete experimentally "
                "active locus."
            ),
            "nodes": [
                {
                    "node_id": "card_nlr_like_system_trait",
                    "label": "CARD-NLR-like system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CARD-NLR-like "
                        "phage-defense system."
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
                    "subject": "card_nlr_like_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "card_nlr_system_trait",
                    "description": (
                        "CARD-NLR-like system possession is a "
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
            "discussion_id": "card-nlr-like-activity-gap",
            "prompt": (
                "Resolve the CARD_NLR_like phage triggers, native hosts, "
                "four-profile effector-combination semantics, "
                "CARD_NLR__Subtilase_long_new HMM inventory gap, and "
                "profile-to-activity criteria before minting effector or "
                "trigger children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wein et al. support CARD-like anti-phage defense, and the "
                "pinned DefenseFinder HMM inventory and rules table "
                "support CARD_NLR_like as a CARD_NLR subsystem requiring "
                "two matches from a four-profile Endonuclease, "
                "Phospho_Trypsin, Subtilase_long_new, and "
                "Trypsin_Phospho candidate effector set. This first-pass "
                "record follows the rule row but leaves exact phage "
                "triggers, native hosts, how the two-of-four effector "
                "profile combinations map to activity, how "
                "CARD_NLR__Subtilase_long_new maps to the pinned HMM "
                "inventory, and whether every DefenseFinder CARD_NLR_like "
                "prediction is a complete experimentally active locus."
            ),
            "evidence": [
                wein_card_evidence(),
                endonuclease_hmm_evidence(),
                phospho_trypsin_hmm_evidence(),
                trypsin_phospho_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#card_nlr_like_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-03",
        }
    ],
}

OLD_CARD_NLR_DISCUSSION_RATIONALE = (
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

UPDATED_CARD_NLR_DISCUSSION_RATIONALE = (
    "Wein et al. support CARD-like domains in multiple anti-phage defense "
    "systems that activate cell-death effectors, and DefenseFinder models "
    "CARD_NLR subtypes with gasdermin, endonuclease, CARD_NLR_Phospho, "
    "CARD_NLR_Subtilase, and CARD_NLR_like rule profiles. CARD-NLR "
    "GasderMIN, endonuclease, phospho, subtilase, and CARD-NLR-like "
    "TraitRecords now capture the five DefenseFinder CARD_NLR rule-row "
    "subtypes, but exact phage triggers, CARD-to-effector activation "
    "sequence, accession-level natural-host components, "
    "CARD_NLR_Subtilase_long_new HMM inventory coverage, CARD_NLR_like "
    "multi-effector semantics, and standalone GasderMIN versus "
    "CARD_NLR_GasderMIN mechanism boundaries remain unresolved."
)

PARENT_EVENT_CHANGES = (
    "Documented CARD-NLR-like as split out in the open CARD-NLR subtype "
    "discussion after minting traitmech:000559 for the DefenseFinder-backed "
    "CARD_NLR_like child; exact two-of-four effector-profile semantics, "
    "CARD_NLR__Subtilase_long_new HMM inventory coverage, and finer CARD-NLR "
    "activation mechanisms remain open."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted CARD-NLR-like system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the CARD-NLR "
            "system parent after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record for the target local ID, placeholder METPO "
            "ID, proposal cohort, record slug, or human label; existing "
            "CARD_NLR_like mentions were scoped to the CARD-NLR parent, "
            "not an exact child TraitRecord, and the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed CARD-NLR-like system during initial curation and "
            "left canonical_examples empty because Wein et al. and the "
            "pinned DefenseFinder tables support CARD-like anti-phage "
            "systems and the CARD_NLR_like rule row but not an "
            "accession-backed native microbial taxon exemplar tied to "
            "CARD_NLR_like profiles and experimentally verified "
            "endogenous activity. No paid research was used."
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
    if discussion["rationale"] == OLD_CARD_NLR_DISCUSSION_RATIONALE:
        discussion["rationale"] = UPDATED_CARD_NLR_DISCUSSION_RATIONALE
    elif discussion["rationale"] != UPDATED_CARD_NLR_DISCUSSION_RATIONALE:
        raise SystemExit("unexpected CARD-NLR subtype discussion rationale")

    parent_event = next(
        (
            event
            for event in record.get("curation_history", [])
            if event.get("action") == "TRACK_NARROWER_RECORD"
            and event.get("timestamp") == PARENT_TIMESTAMP
        ),
        None,
    )
    if parent_event is not None:
        if parent_event.get("changes") != PARENT_EVENT_CHANGES:
            raise SystemExit("unexpected CARD-NLR-like parent curation event")
    else:
        record_curation_event(
            record,
            curator=CURATOR,
            action="TRACK_NARROWER_RECORD",
            changes=PARENT_EVENT_CHANGES,
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
            "CARD-NLR-like system trait and parent update validate; "
            f"rerun with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
