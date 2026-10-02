#!/usr/bin/env python3
"""Add the Avs IV system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "avs_iv_system.yaml"

GAO_2020 = "DOI:10.1126/science.aba0372"
GAO_2022 = "DOI:10.1126/science.abm4096"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T06:35:42Z"
CANONICAL_TIMESTAMP = "2026-10-02T06:35:43Z"
IDENTIFIER = "traitmech:000537"
AVAST_PARENT_ID = "traitmech:000239"
PROPOSAL = "proposals/metpo_traitmech_v414"

ARTICLE_ROW = (
    "| Avs | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "Avs\tAvs_IV\t1\t1\tAvs_IV__Avs4A\t\t\t"
HMM_ROWS = {
    "Avs_IV__Avs4A": (
        "| Avs_IV__Avs4A                                    |"
        " Avs_IV__Avs4A                                    |"
        " Avs_IV                 | Custom                  | 60     |"
    ),
}


def avast_discovery_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2020,
        "snippet": "AVAST, antiviral ATPase/NTPase of the STAND superfamily",
        "notes": (
            "Gao et al. coined AVAST as an antiviral STAND ATPase/NTPase "
            "defense-system family."
        ),
    }


def avs4_recognition_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2022,
        "snippet": (
            "Avs1 to Avs3 recognize the large terminase subunit, and Avs4 "
            "recognizes the portal"
        ),
        "notes": (
            "Gao et al. support Avs4 as a phage-portal-sensing member of "
            "the AVAST receptor family."
        ),
    }


def avs_activation_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2022,
        "snippet": (
            "In all four cases, target recognition led to Avs protein "
            "activation and antiviral activity"
        ),
        "notes": (
            "Gao et al. connect Avs1 through Avs4 target recognition to "
            "Avs activation and antiviral activity."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Avs source "
            "key to the Gao et al. pangenome-scale antiviral-immunity paper."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} "
            "under the Avs_IV model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Avs_IV as an Avs "
            "subsystem with an Avs4A profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Avs IV system",
    "definition": (
        "An AVAST system in which an organism possesses a genome-encoded "
        "subtype IV locus represented by DefenseFinder with an Avs4A "
        "profile."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [AVAST_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Avs_IV",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Avs_IV__Avs4A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        avast_discovery_evidence(),
        avs4_recognition_evidence(),
        avs_activation_evidence(),
        article_registry_evidence(),
        hmm_evidence("Avs_IV__Avs4A"),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "avs_iv_locus_phage_portal_recognition",
            "title": "Avs IV loci support phage portal recognition",
            "description": (
                "Conservative system-level sketch linking an Avs_IV locus "
                "to Avs4-mediated phage portal recognition and Avs IV "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Avs_IV at locus and Avs4 phage-portal "
                "recognition level without asserting the exact Avs4A "
                "component role, direct effector activity, native host "
                "breadth, sensitive-phage breadth, or whether every "
                "DefenseFinder Avs_IV prediction is a complete "
                "experimentally active Avs IV locus."
            ),
            "nodes": [
                {
                    "node_id": "avs_iv_locus",
                    "label": "Avs IV locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AVAST subtype IV locus represented in "
                        "DefenseFinder by an Avs4A profile."
                    ),
                },
                {
                    "node_id": "avs4_phage_portal_recognition",
                    "label": "Avs4 phage portal recognition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recognition of an infecting phage portal protein "
                        "by an Avs4 antiviral STAND-family receptor."
                    ),
                },
                {
                    "node_id": "avs_iv_system_trait",
                    "label": "Avs IV system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Avs IV "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "avast_system_trait",
                    "label": "AVAST system",
                    "node_type": "TRAIT",
                    "grounding": AVAST_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded AVAST "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "avs_iv_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "avs4_phage_portal_recognition",
                    "description": (
                        "Avs IV loci encode Avs4 components, and Avs4 "
                        "belongs to the AVAST receptors that recognize the "
                        "phage portal protein."
                    ),
                    "evidence": [
                        avs4_recognition_evidence(),
                        hmm_evidence("Avs_IV__Avs4A"),
                    ],
                },
                {
                    "subject": "avs4_phage_portal_recognition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "avs_iv_system_trait",
                    "description": (
                        "The first-pass Avs IV system trait is realized by "
                        "Avs4 target recognition and downstream antiviral "
                        "activity."
                    ),
                    "evidence": [
                        avs4_recognition_evidence(),
                        avs_activation_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "avs_iv_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "avast_system_trait",
                    "description": (
                        "Avs IV system possession is an AVAST-system trait."
                    ),
                    "evidence": [
                        avast_discovery_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "avs-iv-component-and-effector-gap",
            "prompt": (
                "Resolve the Avs4A component role, direct effector "
                "chemistry, exact phage-trigger mapping, native host "
                "breadth, and sensitive-phage breadth before minting Avs IV "
                "mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support Avs4 phage-portal recognition and "
                "Avs activation during antiviral defense, and the pinned "
                "DefenseFinder HMM inventory and rules table support Avs_IV "
                "as a subtype IV model with an Avs4A profile. This "
                "first-pass record leaves the exact component role, "
                "downstream effector chemistry, native host breadth, "
                "sensitive-phage breadth, and profile-to-activity "
                "requirements unresolved."
            ),
            "evidence": [
                avs4_recognition_evidence(),
                avs_activation_evidence(),
                hmm_evidence("Avs_IV__Avs4A"),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#avs_iv_locus_phage_portal_recognition"
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
            "Minted Avs IV system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the AVAST system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
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
            "Reviewed Avs IV system during initial curation and left "
            "canonical_examples empty because Gao et al. and the pinned "
            "DefenseFinder tables support the Avs_IV model namespace and "
            "Avs4 phage-portal-recognition activity but not an "
            "accession-backed native microbial taxon exemplar with "
            "experimentally verified endogenous Avs IV activity. No paid "
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
            "Avs IV system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
