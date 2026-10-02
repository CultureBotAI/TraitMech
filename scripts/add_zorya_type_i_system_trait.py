#!/usr/bin/env python3
"""Add the Zorya type I system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "zorya_type_i_system.yaml"
ZORYA_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "zorya_system.yaml"

HU_2024 = "DOI:10.1038/s41586-024-08493-8"
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
TIMESTAMP = "2026-10-02T20:10:33Z"
PARENT_TIMESTAMP = "2026-10-02T20:10:34Z"
IDENTIFIER = "traitmech:000554"
ZORYA_PARENT_ID = "traitmech:000217"
PROPOSAL = "proposals/metpo_traitmech_v431"

ARTICLE_ROW = (
    "| Zorya | 10\\.1126/science\\.aar4120 | Systematic discovery of antiphage "
    "defense systems in the microbial pangenome |"
)
RULE_ROW = (
    "Zorya\tZorya_TypeI\t3\t3\tZorya_TypeI__ZorC, "
    "Zorya_TypeI__ZorD, Zorya__ZorA, Zorya__ZorB\t\t\t"
)
ZORA_HMM_ROW = (
    "| Zorya__ZorA                                      |"
    " Zorya__ZorA                                      |"
    " Zorya                  | Custom                  | 20     |"
)
ZORB_HMM_ROW = (
    "| Zorya__ZorB                                      |"
    " Zorya__ZorB                                      |"
    " Zorya                  | Custom                  | 20     |"
)
ZORCD_HMM_ROWS = (
    "| Zorya_TypeI__ZorC                                |"
    " Zorya_TypeI__ZorC                                |"
    " Zorya_TypeI            | Custom                  | 20     |\n"
    "| Zorya_TypeI__ZorD                                |"
    " Zorya_TypeI__ZorD                                |"
    " Zorya_TypeI            | Custom                  | 20     |"
)


def zorya_type_i_effector_evidence() -> dict[str, str]:
    return {
        "reference": HU_2024,
        "snippet": (
            "ZorAB transfers the phage invasion signal through the ZorA "
            "cytoplasmic tail to recruit and activate the soluble ZorC and "
            "ZorD effectors"
        ),
        "notes": (
            "Hu et al. support ZorAB-mediated recruitment and activation of "
            "the soluble ZorC and ZorD Type I effectors."
        ),
    }


def zorya_type_i_phage_dna_evidence() -> dict[str, str]:
    return {
        "reference": HU_2024,
        "snippet": (
            "soluble ZorC and ZorD effectors, which facilitate the "
            "degradation of the phage DNA"
        ),
        "notes": (
            "Hu et al. support Type I ZorC/ZorD effectors as phage-DNA "
            "degradation outputs."
        ),
    }


def native_locus_evidence() -> dict[str, str]:
    return {
        "reference": MARIANO_2025,
        "snippet": (
            "We observed that homologs of Zorya I from Serratia marcescens "
            "ATCC 274 and Zorya II from E. coli ATCC 8739 provide "
            "protection against several phages from the Durham collection"
        ),
        "notes": (
            "Mariano et al. support experimentally validated phage "
            "protection by a Zorya I homolog set from Serratia marcescens "
            "ATCC 274."
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


def zora_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ZORA_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the Zorya__ZorA "
            "custom profile listed by the Zorya_TypeI rule."
        ),
    }


def zorb_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ZORB_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the Zorya__ZorB "
            "custom profile listed by the Zorya_TypeI rule."
        ),
    }


def zorcd_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ZORCD_HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "Zorya_TypeI__ZorC and Zorya_TypeI__ZorD under the "
            "Zorya_TypeI model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Zorya_TypeI as a "
            "Zorya subsystem with Zorya_TypeI__ZorC, Zorya_TypeI__ZorD, "
            "Zorya__ZorA, and Zorya__ZorB in its mandatory profile set and "
            "3 mandatory matches / 3 genes required."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Zorya type I system",
    "definition": (
        "A Zorya system in which an organism possesses a genome-encoded "
        "DefenseFinder Zorya_TypeI subtype locus whose rule row lists "
        "Zorya_TypeI__ZorC, Zorya_TypeI__ZorD, Zorya__ZorA, and "
        "Zorya__ZorB in its mandatory profile set with 3 mandatory matches "
        "and 3 genes required."
    ),
    "definition_source": HU_2024,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [ZORYA_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Zorya_TypeI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Zorya_TypeI__ZorC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Zorya_TypeI__ZorD",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Zorya__ZorA",
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
        zorya_type_i_effector_evidence(),
        zorya_type_i_phage_dna_evidence(),
        native_locus_evidence(),
        article_registry_evidence(),
        zora_hmm_evidence(),
        zorb_hmm_evidence(),
        zorcd_hmm_evidence(),
        rules_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:615",
            "taxon_label": "Serratia marcescens",
            "note": (
                "Mariano et al. report that a Zorya I homolog set from "
                "Serratia marcescens ATCC 274 protected against several "
                "tested Durham-collection phages."
            ),
            "reference": MARIANO_2025,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "zorya_type_i_locus_subtype_defense",
            "title": "Zorya type I loci mark a ZorC/ZorD-dependent Zorya subtype",
            "description": (
                "Conservative subtype-level sketch linking a DefenseFinder "
                "Zorya_TypeI locus to ZorC/ZorD-dependent type I antiphage "
                "activity and Zorya type I system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the Zorya_TypeI subtype at "
                "DefenseFinder rule-row level without asserting the exact "
                "phage trigger, ion substrate, ZorC/ZorD nuclease target, "
                "anti-defense escape breadth, or whether every "
                "DefenseFinder Zorya_TypeI prediction is a complete "
                "experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "zorya_type_i_locus",
                    "label": "Zorya type I locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Zorya_TypeI subtype locus "
                        "whose rule row lists Zorya_TypeI__ZorC, "
                        "Zorya_TypeI__ZorD, Zorya__ZorA, and "
                        "Zorya__ZorB in its mandatory profile set with "
                        "3 mandatory matches and 3 genes required."
                    ),
                },
                {
                    "node_id": "zorya_type_i_antiphage_activity",
                    "label": "Zorya type I antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Antiphage activity of a ZorC/ZorD-dependent "
                        "type I Zorya locus."
                    ),
                },
                {
                    "node_id": "zorya_type_i_system_trait",
                    "label": "Zorya type I system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Zorya type I "
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
                    "subject": "zorya_type_i_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "zorya_type_i_antiphage_activity",
                    "description": (
                        "Zorya_TypeI loci are modeled in DefenseFinder by "
                        "a rule row listing Zorya_TypeI__ZorC, "
                        "Zorya_TypeI__ZorD, Zorya__ZorA, and Zorya__ZorB "
                        "in its mandatory profile set with 3 mandatory "
                        "matches and 3 genes required, and the "
                        "characterized Zorya type I branch recruits ZorC "
                        "and ZorD effectors."
                    ),
                    "evidence": [
                        zorya_type_i_effector_evidence(),
                        zora_hmm_evidence(),
                        zorb_hmm_evidence(),
                        zorcd_hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "zorya_type_i_antiphage_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "zorya_type_i_system_trait",
                    "description": (
                        "The first-pass Zorya type I system trait is "
                        "realized by a DefenseFinder Zorya_TypeI subtype "
                        "locus."
                    ),
                    "evidence": [
                        zorya_type_i_effector_evidence(),
                        zorya_type_i_phage_dna_evidence(),
                        native_locus_evidence(),
                    ],
                },
                {
                    "subject": "zorya_type_i_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "zorya_system_trait",
                    "description": (
                        "Zorya type I system possession is a "
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
            "discussion_id": "zorya-type-i-activity-gap",
            "prompt": (
                "Resolve Zorya_TypeI phage triggers, native host breadth, "
                "ZorC/ZorD nuclease targets, ZorAB-to-ZorC/ZorD "
                "activation, and profile-to-activity criteria before "
                "minting enzyme, trigger, or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Hu et al. support ZorAB activation and phage-DNA "
                "degradation by type I Zorya ZorC/ZorD effectors, "
                "Mariano et al. support Zorya I phage protection from a "
                "Serratia marcescens locus, and the pinned DefenseFinder "
                "HMM inventory and rules table support Zorya_TypeI as a "
                "subtype whose rule row lists Zorya_TypeI__ZorC, "
                "Zorya_TypeI__ZorD, Zorya__ZorA, and Zorya__ZorB with "
                "3 mandatory matches and 3 genes required. This first-pass "
                "record leaves exact phage triggers, native hosts, "
                "profile-to-component correspondence, ion usage, "
                "anti-defense escape, and ZorC/ZorD nuclease outputs "
                "unresolved."
            ),
            "evidence": [
                zorya_type_i_effector_evidence(),
                zorcd_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#zorya_type_i_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
        }
    ],
}

UPDATED_ZORYA_DISCUSSION_RATIONALE = (
    "Hu et al. support Type I ZorAB activation and ZorC/ZorD-mediated "
    "phage-DNA degradation, Mariano et al. support Type I/II ZorAB "
    "architecture plus a recruited Type II ZorE nickase, and the pinned "
    "DefenseFinder rules table supports distinct Zorya_TypeI and "
    "Zorya_TypeII subtype rows. Zorya type I and type II TraitRecords now "
    "capture those DefenseFinder subtypes, but Zorya variants still need "
    "separate review before TraitMech asserts one universal ion substrate, "
    "effector composition, nuclease target, cell-death pathway, Type III "
    "mechanism, or anti-defense breadth."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Zorya type I system as a DOI- and "
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
        assert "Zorya type II TraitRecord" in discussion["rationale"]
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
                "Documented Zorya type I as split out in the open Zorya "
                "subtype-effector discussion after minting traitmech:000554 "
                "for the DefenseFinder-backed Zorya_TypeI child; Type III "
                "and finer Zorya subtype mechanisms remain open."
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
            "Zorya type I system trait and parent update validate; rerun "
            f"with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
