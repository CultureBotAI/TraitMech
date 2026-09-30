#!/usr/bin/env python3
"""Add the Tha system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "tha_system.yaml"

ROSTOL = "DOI:10.1038/s41564-024-01661-6"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T17:20:02Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T17:20:03Z"
IDENTIFIER = "traitmech:000497"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v374"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "| Tha | 10\\.1038/s41564-024-01661-6 | Bacteriophages "
            "avoid autoimmunity from cognate immune systems as an "
            "intrinsic part of their life cycles | "
        ),
        "notes": (
            "The pinned DefenseFinder article registry maps the Tha "
            "source key to the primary Nat Microbiol Tha paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            "| Tha__Tha                                         |"
            "                                                  |"
            " Tha                    | Custom                  | 20     |"
        ),
        "notes": (
            "The pinned DefenseFinder HMM inventory lists one Tha__Tha "
            "custom HMM row under the Tha system namespace."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Tha system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Tha system",
    "definition": (
        "A phage defense system in which an organism possesses a Tha "
        "tail-activated HEPN anti-phage locus that can be activated by "
        "incoming-phage minor tail proteins to mediate nonspecific "
        "RNase-linked defense."
    ),
    "definition_source": ROSTOL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "Tha",
            "synonym_type": "EXACT_SYNONYM",
            "source": ROSTOL,
        },
        {
            "synonym_text": (
                "tail-activated, HEPN domain-containing anti-phage system"
            ),
            "synonym_type": "EXACT_SYNONYM",
            "source": ROSTOL,
        },
        {
            "synonym_text": "Tha__Tha",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": ROSTOL,
            "snippet": (
                "multiple Staphylococcus aureus prophages encode Tha "
                "(tail-activated, HEPN (higher eukaryotes and prokaryotes "
                "nucleotide-binding) domain-containing anti-phage system)"
            ),
            "notes": (
                "Rostol et al. define Tha as a tail-activated HEPN "
                "anti-phage system encoded by multiple S. aureus "
                "prophages."
            ),
        },
        {
            "reference": ROSTOL,
            "snippet": (
                "We demonstrate the function of two Tha systems, Tha-1 "
                "and Tha-2, activated by distinct tail proteins"
            ),
            "notes": (
                "Rostol et al. support multiple experimentally tested Tha "
                "variants that are activated by different phage tail "
                "proteins."
            ),
        },
        {
            "reference": ROSTOL,
            "snippet": (
                "Tha is a non-specific RNase that is activated by "
                "conserved minor tail proteins from temperate phages"
            ),
            "notes": (
                "Rostol et al. connect the Tha anti-phage system to "
                "minor-tail-protein activation and nonspecific RNase "
                "activity."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1280",
            "taxon_label": "Staphylococcus aureus",
            "note": (
                "Rostol et al. report that multiple Staphylococcus aureus "
                "prophages encode Tha and experimentally test Tha-1 and "
                "Tha-2 antiphage defense in S. aureus RN4220."
            ),
            "reference": ROSTOL,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "tha_tail_activated_hepn_rnase_defense",
            "title": "Tha systems activate HEPN RNase defense after tail cues",
            "description": (
                "Conservative system-level sketch linking a Tha locus to "
                "incoming-phage minor-tail-protein activation, Tha HEPN "
                "RNase activity, and phage-defense-system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the Tha system at family scope "
                "without asserting that all Tha variants sense the same "
                "minor tail protein, have the same cognate Ith inhibitor, "
                "block the same phages, share the same native prophage "
                "organization, or map to a DefenseFinder rules row."
            ),
            "nodes": [
                {
                    "node_id": "tha_locus",
                    "label": "Tha locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-encoded Tha locus encoding a "
                        "tail-activated HEPN anti-phage system."
                    ),
                },
                {
                    "node_id": "minor_tail_protein_activation",
                    "label": "minor-tail-protein activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of Tha by incoming-phage minor tail "
                        "proteins during bacteriophage infection."
                    ),
                },
                {
                    "node_id": "tha_hepn_rnase_activity",
                    "label": "Tha HEPN RNase activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Nonspecific RNase activity mediated by a Tha "
                        "HEPN domain after activation by a cognate "
                        "minor tail protein."
                    ),
                },
                {
                    "node_id": "tha_system_trait",
                    "label": "Tha system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Tha phage-defense "
                        "system."
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
                    "subject": "tha_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "minor_tail_protein_activation",
                    "description": (
                        "Tha loci encode HEPN anti-phage proteins that can "
                        "be activated by structural tail proteins of "
                        "incoming phages."
                    ),
                    "evidence": [
                        {
                            "reference": ROSTOL,
                            "snippet": (
                                "a defence system activated by structural "
                                "tail proteins of incoming phages"
                            ),
                            "notes": (
                                "Rostol et al. define Tha as a defense "
                                "system activated by incoming-phage "
                                "structural tail proteins."
                            ),
                        },
                        article_registry_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "minor_tail_protein_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "tha_hepn_rnase_activity",
                    "description": (
                        "Incoming-phage minor tail proteins activate Tha "
                        "HEPN-domain RNase activity."
                    ),
                    "evidence": [
                        {
                            "reference": ROSTOL,
                            "snippet": (
                                "Tha is a non-specific RNase that is "
                                "activated by conserved minor tail proteins "
                                "from temperate phages"
                            ),
                            "notes": (
                                "Rostol et al. connect conserved minor "
                                "tail proteins to Tha RNase activation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tha_hepn_rnase_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "tha_system_trait",
                    "description": (
                        "Tha-mediated nonspecific RNase activity realizes "
                        "the Tha system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ROSTOL,
                            "snippet": (
                                "confirming that Tha-1 is a non-specific "
                                "RNase"
                            ),
                            "notes": (
                                "Rostol et al. validate Tha-1 "
                                "nonspecific RNase activity."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tha_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Tha system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": ROSTOL,
                            "snippet": (
                                "Tha-1 is an anti-phage system that causes "
                                "autoimmunity when improperly regulated"
                            ),
                            "notes": (
                                "Rostol et al. experimentally tested the "
                                "anti-phage properties of Tha-1."
                            ),
                        },
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "tha-variant-profile-rule-gap",
            "prompt": (
                "Resolve Tha variant boundaries, exact minor-tail-protein "
                "triggers, Ith inhibitor relationships, native host "
                "breadth, and DefenseFinder rule/profile coverage before "
                "minting narrower Tha mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rostol et al. support Tha-1 and Tha-2 as S. aureus "
                "prophage-encoded Tha systems activated by distinct "
                "incoming-phage minor tail proteins. The pinned "
                "DefenseFinder registries map the Tha source key to the "
                "same primary paper and list one Tha__Tha custom HMM row, "
                "but no exact Tha system rule row was present in the "
                "pinned rules table. The first TraitRecord therefore "
                "stays at Tha-system scope until separate review resolves "
                "variant boundaries, exact activators, Ith inhibitor "
                "relationships, native host breadth, and model coverage."
            ),
            "evidence": [
                {
                    "reference": ROSTOL,
                    "snippet": (
                        "Tha systems can also block reproduction of the "
                        "induced tha-positive prophages"
                    ),
                    "notes": (
                        "Rostol et al. report Tha autoimmunity and "
                        "inhibition by cognate overlapping antisense Ith "
                        "proteins."
                    ),
                },
                article_registry_evidence(),
                hmm_inventory_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#tha_tail_activated_hepn_rnase_defense"
            ],
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
            "Minted Tha system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE",
        changes=(
            "Reviewed Tha system canonical_examples and kept "
            "Staphylococcus aureus because Rostol et al. report that "
            "multiple S. aureus prophages encode Tha and experimentally "
            "test plasmid-carried Tha-1 and Tha-2 in S. aureus RN4220 "
            "phage-challenge assays. No paid research was used."
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
