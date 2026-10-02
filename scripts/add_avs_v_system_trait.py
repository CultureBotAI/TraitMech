#!/usr/bin/env python3
"""Add the Avs V system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "avs_v_system.yaml"

GAO_2020 = "DOI:10.1126/science.aba0372"
MURALIDHARAN = "DOI:10.1016/j.molcel.2026.01.004"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T07:21:42Z"
CANONICAL_TIMESTAMP = "2026-10-02T07:21:43Z"
IDENTIFIER = "traitmech:000538"
AVAST_PARENT_ID = "traitmech:000239"
PROPOSAL = "proposals/metpo_traitmech_v415"

ARTICLE_ROW = (
    "| Avs | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "Avs\tAvs_V\t1\t1\tAvs_V__Avs5A\t\t\t"
HMM_ROWS = {
    "Avs_V__Avs5A": (
        "| Avs_V__Avs5A                                     |"
        " Avs_V__Avs5A                                     |"
        " Avs_V                  | Custom                  | 60     |"
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


def avs5_immunity_evidence() -> dict[str, str]:
    return {
        "reference": MURALIDHARAN,
        "snippet": (
            "AVAST type 5 (Avs5) systems, part of the signal transduction "
            "ATPases of numerous domains (STAND) superfamily, confer "
            "conserved immunity against jumbo phages"
        ),
        "notes": (
            "Muralidharan et al. support treating Avs5 systems as type V "
            "AVAST systems with conserved immunity against jumbo phages."
        ),
    }


def avs5_effector_evidence() -> dict[str, str]:
    return {
        "reference": MURALIDHARAN,
        "snippet": (
            "Recognition of phage infection triggers the Sir2-like "
            "effector domain of Avs5 across three Avs5 clades"
        ),
        "notes": (
            "Muralidharan et al. connect Avs5 phage recognition to "
            "Sir2-like effector activation."
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
            "under the Avs_V model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Avs_V as an Avs "
            "subsystem with an Avs5A profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Avs V system",
    "definition": (
        "An AVAST system in which an organism possesses a genome-encoded "
        "subtype V locus represented by DefenseFinder with an Avs5A "
        "profile."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [AVAST_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Avs_V",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Avs_V__Avs5A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        avast_discovery_evidence(),
        avs5_immunity_evidence(),
        avs5_effector_evidence(),
        article_registry_evidence(),
        hmm_evidence("Avs_V__Avs5A"),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "avs_v_locus_sir2_effector_activation",
            "title": "Avs V loci support Sir2-like effector activation",
            "description": (
                "Conservative system-level sketch linking an Avs_V locus "
                "to Avs5 Sir2-like effector activation and Avs V system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Avs_V at locus and Avs5 Sir2-like "
                "effector-activation level without asserting the exact "
                "Avs5A component role, JADA trigger-protein breadth, "
                "native host breadth, sensitive jumbo-phage breadth, or "
                "whether every DefenseFinder Avs_V prediction is a "
                "complete experimentally active Avs V locus."
            ),
            "nodes": [
                {
                    "node_id": "avs_v_locus",
                    "label": "Avs V locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AVAST subtype V locus represented in "
                        "DefenseFinder by an Avs5A profile."
                    ),
                },
                {
                    "node_id": "avs5_sir2_like_effector_activation",
                    "label": "Avs5 Sir2-like effector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of an Avs5 Sir2-like effector domain "
                        "after phage infection recognition."
                    ),
                },
                {
                    "node_id": "avs_v_system_trait",
                    "label": "Avs V system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Avs V "
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
                    "subject": "avs_v_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "avs5_sir2_like_effector_activation",
                    "description": (
                        "Avs V loci encode Avs5 components, and Avs5 "
                        "phage-infection recognition triggers a Sir2-like "
                        "effector domain."
                    ),
                    "evidence": [
                        avs5_effector_evidence(),
                        hmm_evidence("Avs_V__Avs5A"),
                    ],
                },
                {
                    "subject": "avs5_sir2_like_effector_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "avs_v_system_trait",
                    "description": (
                        "The first-pass Avs V system trait is realized by "
                        "Avs5 phage recognition, Sir2-like effector "
                        "activation, and conserved immunity against jumbo "
                        "phages."
                    ),
                    "evidence": [
                        avs5_immunity_evidence(),
                        avs5_effector_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "avs_v_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "avast_system_trait",
                    "description": (
                        "Avs V system possession is an AVAST-system trait."
                    ),
                    "evidence": [
                        avast_discovery_evidence(),
                        avs5_immunity_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "avs-v-component-and-host-gap",
            "prompt": (
                "Resolve the Avs5A component role, exact JADA trigger "
                "breadth, native host breadth, sensitive jumbo-phage "
                "breadth, and DefenseFinder profile-to-activity "
                "requirements before minting Avs V mechanism or "
                "component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Muralidharan et al. support Avs5 Sir2-like effector "
                "activation during jumbo-phage defense, and the pinned "
                "DefenseFinder HMM inventory and rules table support "
                "Avs_V as a subtype V model with an Avs5A profile. This "
                "first-pass record leaves the exact component role, JADA "
                "trigger breadth, native host breadth, sensitive jumbo-"
                "phage breadth, and profile-to-activity requirements "
                "unresolved."
            ),
            "evidence": [
                avs5_immunity_evidence(),
                avs5_effector_evidence(),
                hmm_evidence("Avs_V__Avs5A"),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#avs_v_locus_sir2_effector_activation"
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
            "Minted Avs V system as a DOI- and DefenseFinder-backed "
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
            "Reviewed Avs V system during initial curation and left "
            "canonical_examples empty because Muralidharan et al. and "
            "the pinned DefenseFinder tables support Avs5 type V AVAST "
            "immunity and the Avs_V model namespace but not an "
            "accession-backed native microbial taxon exemplar tied to "
            "Avs_V__Avs5A and experimentally verified endogenous Avs V "
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
            "Avs V system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
