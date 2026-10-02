#!/usr/bin/env python3
"""Add the Zorya type II system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "zorya_type_ii_system.yaml"
ZORYA_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "zorya_system.yaml"

MARIANO_2025 = "DOI:10.1038/s41467-025-57397-2"
DORON_2018 = "DOI:10.1126/science.aar4120"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T18:08:00Z"
PARENT_TIMESTAMP = "2026-10-02T18:08:01Z"
IDENTIFIER = "traitmech:000552"
ZORYA_PARENT_ID = "traitmech:000217"
PROPOSAL = "proposals/metpo_traitmech_v429"

ARTICLE_ROW = (
    "| Zorya | 10\\.1126/science\\.aar4120 | Systematic discovery of antiphage "
    "defense systems in the microbial pangenome |"
)
RULE_ROW = (
    "Zorya\tZorya_TypeII\t3\t3\tZorya_TypeII__ZorE, Zorya__ZorA2, "
    "Zorya__ZorB\t\t\t"
)
SHARED_HMM_ROWS = (
    "| Zorya__ZorA2                                     |"
    " Zorya__ZorA2                                     |"
    " Zorya                  | Custom                  | 20     |\n"
    "| Zorya__ZorB                                      |"
    " Zorya__ZorB                                      |"
    " Zorya                  | Custom                  | 20     |"
)
ZORE_HMM_ROW = (
    "| Zorya_TypeII__ZorE                               |"
    " Zorya_TypeII__ZorE                               |"
    " Zorya_TypeII           | Custom                  | 20     |"
)


def zorya_type_ii_effector_evidence() -> dict[str, str]:
    return {
        "reference": MARIANO_2025,
        "snippet": (
            "For Zorya II, anti-phage activity requires the presence of the "
            "ZorE effector, which we show is recruited by ZorAB"
        ),
        "notes": (
            "Mariano et al. support the dependence of Zorya type II phage "
            "defense on a ZorAB-recruited ZorE effector."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Zorya source "
            "key to the Doron et al. microbial-pangenome antiphage-system "
            "discovery paper."
        ),
    }


def shared_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": SHARED_HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the Zorya__ZorA2 "
            "and Zorya__ZorB custom profiles used by the Zorya_TypeII rule."
        ),
    }


def zore_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ZORE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "Zorya_TypeII__ZorE under the Zorya_TypeII model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Zorya_TypeII as a "
            "Zorya subsystem requiring Zorya_TypeII__ZorE plus shared "
            "Zorya__ZorA2 and Zorya__ZorB profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Zorya type II system",
    "definition": (
        "A Zorya system in which an organism possesses a genome-encoded "
        "DefenseFinder Zorya_TypeII subtype locus represented by "
        "Zorya_TypeII__ZorE, Zorya__ZorA2, and Zorya__ZorB rule profiles."
    ),
    "definition_source": MARIANO_2025,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [ZORYA_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Zorya_TypeII",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Zorya_TypeII__ZorE",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Zorya__ZorA2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Zorya__ZorB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        zorya_type_ii_effector_evidence(),
        article_registry_evidence(),
        shared_hmm_evidence(),
        zore_hmm_evidence(),
        rules_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Mariano et al. report that a Zorya II locus from E. coli "
                "ATCC 8739 protected E. coli MT56 against several tested "
                "coliphages."
            ),
            "reference": MARIANO_2025,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "zorya_type_ii_locus_subtype_defense",
            "title": "Zorya type II loci mark a ZorE-dependent Zorya subtype",
            "description": (
                "Conservative subtype-level sketch linking a DefenseFinder "
                "Zorya_TypeII locus to ZorE-dependent type II antiphage "
                "activity and Zorya type II system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the Zorya_TypeII subtype at "
                "DefenseFinder rule-row level without asserting the exact "
                "phage trigger, ion substrate, ZorE nuclease target, "
                "anti-defense escape breadth, or whether every "
                "DefenseFinder Zorya_TypeII prediction is a complete "
                "experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "zorya_type_ii_locus",
                    "label": "Zorya type II locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Zorya_TypeII subtype locus "
                        "represented by Zorya_TypeII__ZorE, Zorya__ZorA2, "
                        "and Zorya__ZorB profiles."
                    ),
                },
                {
                    "node_id": "zorya_type_ii_antiphage_activity",
                    "label": "Zorya type II antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Antiphage activity of a ZorE-dependent type II "
                        "Zorya locus."
                    ),
                },
                {
                    "node_id": "zorya_type_ii_system_trait",
                    "label": "Zorya type II system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Zorya type II "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "zorya_system_trait",
                    "label": "Zorya system",
                    "node_type": "TRAIT",
                    "grounding": ZORYA_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded Zorya "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "zorya_type_ii_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "zorya_type_ii_antiphage_activity",
                    "description": (
                        "Zorya_TypeII loci are represented in DefenseFinder "
                        "by Zorya_TypeII__ZorE, Zorya__ZorA2, and "
                        "Zorya__ZorB rule profiles and the characterized "
                        "Zorya II branch requires ZorE for anti-phage "
                        "activity."
                    ),
                    "evidence": [
                        zorya_type_ii_effector_evidence(),
                        shared_hmm_evidence(),
                        zore_hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "zorya_type_ii_antiphage_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "zorya_type_ii_system_trait",
                    "description": (
                        "The first-pass Zorya type II system trait is "
                        "realized by a DefenseFinder Zorya_TypeII subtype "
                        "locus."
                    ),
                    "evidence": [
                        zorya_type_ii_effector_evidence(),
                    ],
                },
                {
                    "subject": "zorya_type_ii_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "zorya_system_trait",
                    "description": (
                        "Zorya type II system possession is a "
                        "Zorya-system trait."
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
            "discussion_id": "zorya-type-ii-activity-gap",
            "prompt": (
                "Resolve Zorya_TypeII phage triggers, native host breadth, "
                "ZorE nuclease targets, ZorAB-to-ZorE activation, and "
                "profile-to-activity criteria before minting enzyme, "
                "trigger, or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mariano et al. support ZorE dependence for type II Zorya "
                "anti-phage activity, and the pinned DefenseFinder HMM "
                "inventory and rules table support Zorya_TypeII as a "
                "subtype with Zorya_TypeII__ZorE, Zorya__ZorA2, and "
                "Zorya__ZorB profiles. This first-pass record leaves exact "
                "phage triggers, native hosts, profile-to-component "
                "correspondence, ion usage, anti-defense escape, and "
                "ZorE nuclease outputs unresolved."
            ),
            "evidence": [
                zorya_type_ii_effector_evidence(),
                zore_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#zorya_type_ii_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
        }
    ],
}

UPDATED_ZORYA_DISCUSSION_RATIONALE = (
    "Hu et al. support Type I ZorAB activation and ZorC/ZorD-mediated "
    "phage-DNA degradation, and Mariano et al. support Type I/II ZorAB "
    "architecture plus a recruited Type II ZorE nickase. The Zorya type II "
    "TraitRecord now captures the DefenseFinder Zorya_TypeII subtype, but "
    "Zorya variants still need separate review before TraitMech asserts one "
    "universal ion substrate, effector composition, nuclease target, "
    "cell-death pathway, Type III mechanism, or anti-defense breadth."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Zorya type II system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the Zorya "
            "system parent after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record for the target local ID, placeholder METPO "
            "ID, proposal cohort, record slug, or human label; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def build_zorya_parent() -> dict[str, Any]:
    record = yaml.safe_load(ZORYA_PARENT.read_text())
    assert record["identifier"] == ZORYA_PARENT_ID
    assert record["label"] == "Zorya system"
    assert record["mapping_status"] == "PROPOSED"

    discussion = next(
        item
        for item in record["discussions"]
        if item["discussion_id"] == "zorya-subtype-effector-and-trigger-gap"
    )
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    if discussion["rationale"] != UPDATED_ZORYA_DISCUSSION_RATIONALE:
        assert "Zorya variants need separate review" in discussion["rationale"]
        discussion["rationale"] = UPDATED_ZORYA_DISCUSSION_RATIONALE

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
                "Documented Zorya type II as split out in the open Zorya "
                "subtype-effector discussion after minting traitmech:000552 "
                "for the DefenseFinder-backed Zorya_TypeII child; Type I, "
                "Type III, and finer Zorya subtype mechanisms remain open."
            ),
            llm_assisted=True,
            timestamp=PARENT_TIMESTAMP,
        )
    return record


def validate_outputs(new_record: dict[str, Any], parent_record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(new_record, tmp_path / TARGET.name)
        write_validated_trait(parent_record, tmp_path / ZORYA_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    zorya_parent = build_zorya_parent()
    validate_outputs(record, zorya_parent)

    if args.apply:
        if TARGET.exists():
            existing = yaml.safe_load(TARGET.read_text())
            if existing.get("identifier") != IDENTIFIER:
                raise SystemExit(f"{TARGET} already exists with another identifier")
        write_validated_trait(record, TARGET)
        write_validated_trait(zorya_parent, ZORYA_PARENT)
    else:
        print(
            "Zorya type II system trait and parent update validate; rerun "
            f"with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
