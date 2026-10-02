#!/usr/bin/env python3
"""Add the Avs I system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "avs_i_system.yaml"

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
TIMESTAMP = "2026-10-02T04:42:00Z"
CANONICAL_TIMESTAMP = "2026-10-02T04:42:01Z"
IDENTIFIER = "traitmech:000534"
AVAST_PARENT_ID = "traitmech:000239"
PROPOSAL = "proposals/metpo_traitmech_v411"

ARTICLE_ROW = (
    "| Avs | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "Avs\tAvs_I\t2\t2\tAvs_I__Avs1A, Avs_I__Avs1B, Avs_I__Avs1C\t\t\t"
HMM_ROWS = {
    "Avs_I__Avs1A": (
        "| Avs_I__Avs1A                                     |"
        " Avs_I__Avs1A                                     |"
        " Avs_I                  | Custom                  | 20     |"
    ),
    "Avs_I__Avs1B": (
        "| Avs_I__Avs1B                                     |"
        " Avs_I__Avs1B                                     |"
        " Avs_I                  | Custom                  | 100    |"
    ),
    "Avs_I__Avs1C": (
        "| Avs_I__Avs1C                                     |"
        " Avs_I__Avs1C                                     |"
        " Avs_I                  | Custom                  | 20     |"
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


def avs1_recognition_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2022,
        "snippet": (
            "Avs1 to Avs3 recognize the large terminase subunit, and Avs4 "
            "recognizes the portal"
        ),
        "notes": (
            "Gao et al. support Avs1 as a phage-protein-sensing member of "
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
            "under the Avs_I model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Avs_I as an Avs "
            "subsystem with Avs1A, Avs1B, and Avs1C profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Avs I system",
    "definition": (
        "An AVAST system in which an organism possesses a genome-encoded "
        "subtype I locus represented by DefenseFinder with Avs1A, Avs1B, "
        "and Avs1C profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [AVAST_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Avs_I",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Avs_I__Avs1A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Avs_I__Avs1B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Avs_I__Avs1C",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        avast_discovery_evidence(),
        avs1_recognition_evidence(),
        avs_activation_evidence(),
        article_registry_evidence(),
        hmm_evidence("Avs_I__Avs1A"),
        hmm_evidence("Avs_I__Avs1B"),
        hmm_evidence("Avs_I__Avs1C"),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "avs_i_locus_phage_protein_recognition",
            "title": "Avs I loci support phage protein recognition",
            "description": (
                "Conservative system-level sketch linking an Avs_I locus "
                "to Avs1-mediated phage protein recognition and Avs I "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Avs_I at locus and Avs1 phage-protein "
                "recognition level without asserting the exact Avs1A, "
                "Avs1B, and Avs1C component roles, the direct effector "
                "activity, native host breadth, sensitive-phage breadth, "
                "or whether every DefenseFinder Avs_I prediction is a "
                "complete experimentally active Avs I locus."
            ),
            "nodes": [
                {
                    "node_id": "avs_i_locus",
                    "label": "Avs I locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AVAST subtype I locus represented in "
                        "DefenseFinder by Avs1A, Avs1B, and Avs1C "
                        "profiles."
                    ),
                },
                {
                    "node_id": "avs1_phage_protein_recognition",
                    "label": "Avs1 phage protein recognition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recognition of an infecting phage protein by an "
                        "Avs1 antiviral STAND-family receptor."
                    ),
                },
                {
                    "node_id": "avs_i_system_trait",
                    "label": "Avs I system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Avs I "
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
                    "subject": "avs_i_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "avs1_phage_protein_recognition",
                    "description": (
                        "Avs I loci encode Avs1 components, and Avs1 "
                        "belongs to the AVAST receptors that recognize "
                        "the phage large terminase subunit."
                    ),
                    "evidence": [
                        avs1_recognition_evidence(),
                        hmm_evidence("Avs_I__Avs1A"),
                        hmm_evidence("Avs_I__Avs1B"),
                        hmm_evidence("Avs_I__Avs1C"),
                    ],
                },
                {
                    "subject": "avs1_phage_protein_recognition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "avs_i_system_trait",
                    "description": (
                        "The first-pass Avs I system trait is realized by "
                        "Avs1 target recognition and downstream antiviral "
                        "activity."
                    ),
                    "evidence": [
                        avs1_recognition_evidence(),
                        avs_activation_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "avs_i_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "avast_system_trait",
                    "description": (
                        "Avs I system possession is an AVAST-system "
                        "trait."
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
            "discussion_id": "avs-i-component-and-effector-gap",
            "prompt": (
                "Resolve Avs1A, Avs1B, and Avs1C component roles, direct "
                "effector chemistry, exact phage-trigger mapping, native "
                "host breadth, and sensitive-phage breadth before minting "
                "Avs I mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support Avs1 phage-protein recognition and "
                "Avs activation during antiviral defense, and the pinned "
                "DefenseFinder HMM inventory and rules table support Avs_I "
                "as a subtype I model with Avs1A, Avs1B, and Avs1C "
                "profiles. This first-pass record leaves the exact "
                "component functions, downstream effector chemistry, "
                "native host breadth, sensitive-phage breadth, and "
                "profile-to-activity requirements unresolved."
            ),
            "evidence": [
                avs1_recognition_evidence(),
                avs_activation_evidence(),
                hmm_evidence("Avs_I__Avs1A"),
                hmm_evidence("Avs_I__Avs1B"),
                hmm_evidence("Avs_I__Avs1C"),
                rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#avs_i_locus_phage_protein_recognition"],
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
            "Minted Avs I system as a DOI- and DefenseFinder-backed "
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
            "Reviewed Avs I system during initial curation and left "
            "canonical_examples empty because Gao et al. and the pinned "
            "DefenseFinder tables support the Avs_I model namespace and "
            "Avs1 phage-protein-recognition activity but not an "
            "accession-backed native microbial taxon exemplar with "
            "experimentally verified endogenous Avs I activity. No paid "
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
            "Avs I system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
