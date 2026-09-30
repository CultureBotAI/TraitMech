#!/usr/bin/env python3
"""Add the Kongming system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "kongming_system.yaml"

ZENG = "DOI:10.1126/science.ads6055"
LI = "DOI:10.1038/s41467-026-74710-9"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T22:04:45Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T22:04:46Z"
IDENTIFIER = "traitmech:000501"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v378"

ARTICLE_ROW = (
    "| Kongming | 10\\.1126/science\\.ads6055 | Base-modified "
    "nucleotides mediate immune signaling in bacteria | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "Kongming system to the Zeng et al. Science paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "HMM inventory found no exact Kongming row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Kongming system row."
        ),
    }


def zeng_antiphage_evidence() -> dict[str, str]:
    return {
        "reference": ZENG,
        "snippet": (
            "In this study, we reveal a bacterial antiphage system that "
            "mediates immune signaling through nucleobase modification."
        ),
        "notes": (
            "Zeng et al. describe the Science Kongming paper's antiphage "
            "system as a nucleobase-modification immune-signaling pathway."
        ),
    }


def zeng_ditp_signal_evidence() -> dict[str, str]:
    return {
        "reference": ZENG,
        "snippet": (
            "Immunity is triggered by phage nucleotide kinases, which, "
            "combined with the system-encoded adenosine deaminase, produce "
            "deoxyinosine triphosphates (dITPs) as immune messengers."
        ),
        "notes": (
            "Zeng et al. connect phage-triggered Kongming immunity to "
            "system-dependent production of dITP immune messengers."
        ),
    }


def zeng_nad_depletion_evidence() -> dict[str, str]:
    return {
        "reference": ZENG,
        "snippet": (
            "The dITP signal activates a downstream effector to mediate "
            "depletion of cellular nicotinamide adenine dinucleotide "
            "(oxidized form), resulting in population-level defense "
            "through the death of infected cells."
        ),
        "notes": (
            "Zeng et al. place dITP upstream of an effector that depletes "
            "NAD and drives infected-cell death."
        ),
    }


def li_effector_evidence() -> dict[str, str]:
    return {
        "reference": LI,
        "snippet": (
            "One of them is the Kongming system, which includes an "
            "effector complex (KomBC), composed of a non-canonical purine "
            "NTP pyrophosphatase (KomB) and a SIR2 domain-containing "
            "protein (KomC)."
        ),
        "notes": (
            "Li et al. name the Kongming effector complex and its KomB "
            "and KomC components."
        ),
    }


def li_ditp_activation_evidence() -> dict[str, str]:
    return {
        "reference": LI,
        "snippet": (
            "The Kongming system is activated by an atypical signaling "
            "nucleotide, dITP, generated upon phage infection."
        ),
        "notes": (
            "Li et al. describe dITP as a phage-infection-generated "
            "Kongming activation signal."
        ),
    }


def li_nadase_activation_evidence() -> dict[str, str]:
    return {
        "reference": LI,
        "snippet": (
            "Binding of dITP to KomB initiates progressive conformational "
            "rearrangements within the filament, ultimately remodeling "
            "the filament into a distinct architecture in which KomC "
            "adopts an active conformation with NADase activity."
        ),
        "notes": (
            "Li et al. connect dITP-bound KomB to activation of KomC "
            "NADase activity within the Kongming KomBC effector complex."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Kongming system",
    "definition": (
        "A phage defense system in which an organism possesses a Kongming "
        "locus that uses phage-triggered deoxyinosine triphosphate "
        "signaling to activate a KomBC effector complex and mediate NAD "
        "depletion-linked death of infected cells."
    ),
    "definition_source": ZENG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "Kongming",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Kongming system",
            "synonym_type": "EXACT_SYNONYM",
            "source": LI,
        },
        {
            "synonym_text": "Kongming immune system",
            "synonym_type": "EXACT_SYNONYM",
            "source": LI,
        },
    ],
    "evidence": [
        zeng_antiphage_evidence(),
        zeng_ditp_signal_evidence(),
        zeng_nad_depletion_evidence(),
        li_effector_evidence(),
        li_ditp_activation_evidence(),
        li_nadase_activation_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "kongming_ditp_nadase_defense",
            "title": "Kongming loci activate dITP-linked NADase defense",
            "description": (
                "Conservative system-level sketch linking a Kongming locus "
                "to phage-triggered dITP signaling, KomBC activation, NAD "
                "depletion, infected-cell death, and Kongming system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Kongming as a named dITP-signaling "
                "phage-defense system while leaving exact locus breadth, "
                "natural host breadth, phage nucleotide-kinase inputs, "
                "profile-to-component mapping, and DefenseFinder HMM/rules "
                "detection criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "kongming_locus",
                    "label": "Kongming locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Kongming anti-phage locus encoding dITP "
                        "immune-signaling and KomBC effector functions."
                    ),
                },
                {
                    "node_id": "ditp_immune_signaling",
                    "label": "dITP immune signaling",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Production of deoxyinosine triphosphate immune "
                        "messengers after phage infection."
                    ),
                },
                {
                    "node_id": "komc_nadase_activation",
                    "label": "KomC NADase activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of KomC NADase activity in the KomBC "
                        "effector complex after dITP binding to KomB."
                    ),
                },
                {
                    "node_id": "nad_depletion_cell_death",
                    "label": "NAD depletion-linked infected-cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Depletion of cellular NAD followed by death of "
                        "infected cells during population-level defense."
                    ),
                },
                {
                    "node_id": "kongming_system_trait",
                    "label": "Kongming system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Kongming "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_SYSTEM,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "kongming_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ditp_immune_signaling",
                    "description": (
                        "Kongming loci mediate phage-triggered production "
                        "of dITP immune messengers."
                    ),
                    "evidence": [
                        zeng_antiphage_evidence(),
                        zeng_ditp_signal_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "ditp_immune_signaling",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "komc_nadase_activation",
                    "description": (
                        "dITP binding activates KomC NADase activity in "
                        "the Kongming KomBC effector complex."
                    ),
                    "evidence": [
                        li_ditp_activation_evidence(),
                        li_nadase_activation_evidence(),
                    ],
                },
                {
                    "subject": "komc_nadase_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "nad_depletion_cell_death",
                    "description": (
                        "KomBC effector activation mediates NAD depletion "
                        "that can kill phage-infected cells."
                    ),
                    "evidence": [
                        zeng_nad_depletion_evidence(),
                        li_effector_evidence(),
                        li_nadase_activation_evidence(),
                    ],
                },
                {
                    "subject": "nad_depletion_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "kongming_system_trait",
                    "description": (
                        "dITP-triggered NAD depletion and infected-cell "
                        "death realize the Kongming system trait."
                    ),
                    "evidence": [zeng_nad_depletion_evidence()],
                },
                {
                    "subject": "kongming_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Kongming system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        zeng_antiphage_evidence(),
                        li_ditp_activation_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "kongming-profile-host-and-component-gap",
            "prompt": (
                "Resolve Kongming natural host breadth, exact locus "
                "composition, phage nucleotide-kinase inputs, KomA/KomB/"
                "KomC profile boundaries, and DefenseFinder HMM/rule "
                "coverage before minting narrower Kongming mechanism or "
                "component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Zeng et al. support a bacterial antiphage system that "
                "uses system-encoded adenosine deaminase and phage "
                "nucleotide kinases to produce dITP messengers, and Li "
                "et al. connect the named Kongming system to dITP-driven "
                "activation of the KomBC NADase effector. The pinned "
                "DefenseFinder article registry maps the Kongming source "
                "key to the Zeng et al. Science paper, but the pinned HMM "
                "inventory and rules table have no exact Kongming rows. "
                "This first-pass record therefore does not resolve the "
                "complete locus model, direct HMM/profile mapping, or "
                "native host breadth."
            ),
            "evidence": [
                zeng_ditp_signal_evidence(),
                li_effector_evidence(),
                li_nadase_activation_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#kongming_ditp_nadase_defense"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
        }
    ],
}


def write_new_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Kongming system as a Science-, Nature-, and "
            "DefenseFinder-backed GENOMICS TraitRecord under phage "
            "defense system after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Kongming system canonical_examples and left them "
            "empty because public Science, Nature, and DefenseFinder "
            "evidence supports the named phage-defense system but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous Kongming activity. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_new_record(apply=args.apply)


if __name__ == "__main__":
    main()
