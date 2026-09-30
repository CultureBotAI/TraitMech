#!/usr/bin/env python3
"""Add the Metis system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "metis_system.yaml"

OSTERMAN = "DOI:10.1126/science.aed6782"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T22:51:08Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T22:51:09Z"
IDENTIFIER = "traitmech:000502"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v379"

ARTICLE_ROW = (
    "| Metis | 10\\.1101/2025\\.11\\.05\\.686725 | Bacteria "
    "sense virus-induced genome degradation via methylated "
    "mononucleotides | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "Metis system to the Osterman et al. preprint."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "HMM inventory found no exact Metis row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Metis system row."
        ),
    }


def osterman_system_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "In this work, we describe Metis, a bacterial defense system "
            "that directly senses phage-mediated host genome degradation."
        ),
        "notes": (
            "Osterman et al. directly name Metis as a bacterial system "
            "sensing host-genome degradation during phage infection."
        ),
    }


def osterman_detection_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "Metis aborts phage infection once it detects the modified "
            "mononucleotide N6-methyl-deoxyadenosine monophosphate "
            "(m6dAMP)."
        ),
        "notes": (
            "Osterman et al. identify m6dAMP as the modified "
            "mononucleotide cue detected by Metis."
        ),
    }


def osterman_genome_degradation_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "As methylation of deoxyadenosines usually occurs on the DNA "
            "polymer, accumulation of m6dAMP signals that the host genome "
            "has been degraded."
        ),
        "notes": (
            "Osterman et al. explain why free m6dAMP reports host-genome "
            "degradation."
        ),
    }


def osterman_detection_and_degradation_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "Metis aborts phage infection once it detects the modified "
            "mononucleotide N6-methyl-deoxyadenosine monophosphate "
            "(m6dAMP). As methylation of deoxyadenosines usually occurs "
            "on the DNA polymer, accumulation of m6dAMP signals that the "
            "host genome has been degraded."
        ),
        "notes": (
            "Osterman et al. connect Metis detection of m6dAMP to the "
            "accumulation of that nucleotide after host-genome "
            "degradation."
        ),
    }


def osterman_effector_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "In type I Metis, sensing of m6dAMP activates a nicotinamide "
            "adenine dinucleotide (NAD+) diphosphatase, leading to NAD+ "
            "depletion and cessation of the infection process, whereas "
            "the effector in type II Metis is a membrane-spanning protein "
            "whose toxicity is triggered in response to the modified "
            "mononucleotide."
        ),
        "notes": (
            "Osterman et al. distinguish type I and type II Metis "
            "effectors without resolving a DefenseFinder rule-level model "
            "in the pinned registry."
        ),
    }


def osterman_escape_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "We further show that Metis defense depends on endogenous DNA "
            "methylases and that phages can escape Metis through "
            "mutations that inactivate host genome degradation."
        ),
        "notes": (
            "Osterman et al. link Metis immunity to endogenous DNA "
            "methylases and to phage genome-degradation activity."
        ),
    }


def osterman_parent_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "In this work, we describe Metis, a bacterial defense system "
            "that directly senses phage-mediated host genome degradation. "
            "Metis aborts phage infection once it detects the modified "
            "mononucleotide N6-methyl-deoxyadenosine monophosphate "
            "(m6dAMP)."
        ),
        "notes": (
            "Osterman et al. identify Metis as a bacterial defense system "
            "that aborts phage infection after sensing m6dAMP."
        ),
    }


def osterman_effector_abortion_evidence() -> dict[str, str]:
    return {
        "reference": OSTERMAN,
        "snippet": (
            "Metis aborts phage infection once it detects the modified "
            "mononucleotide N6-methyl-deoxyadenosine monophosphate "
            "(m6dAMP)."
        ),
        "notes": (
            "Osterman et al. connect m6dAMP sensing to type-specific "
            "effector toxicity and abortion of the phage infection process."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Metis system",
    "definition": (
        "A phage defense system in which an organism possesses a Metis "
        "locus that senses phage-mediated host-genome degradation through "
        "N6-methyl-deoxyadenosine monophosphate and activates a "
        "type-specific toxic effector."
    ),
    "definition_source": OSTERMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "Metis",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        osterman_system_evidence(),
        osterman_detection_evidence(),
        osterman_genome_degradation_evidence(),
        osterman_effector_evidence(),
        osterman_escape_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "metis_m6damp_toxic_effector_defense",
            "title": "Metis systems detect methylated mononucleotides",
            "description": (
                "Conservative system-level sketch linking a Metis locus "
                "to phage-mediated host-genome degradation, modified "
                "mononucleotide sensing, toxic effector activation, and "
                "Metis system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Metis as a named m6dAMP-sensing "
                "phage-defense system while leaving exact type I and type "
                "II locus composition, native host breadth, subtype "
                "distribution, effector biochemistry, and DefenseFinder "
                "HMM/rules detection criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "metis_locus",
                    "label": "Metis locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Metis anti-phage locus encoding m6dAMP "
                        "sensing and type-specific toxic effector "
                        "functions."
                    ),
                },
                {
                    "node_id": "phage_mediated_host_genome_degradation",
                    "label": "phage-mediated host genome degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Degradation of bacterial host genomic DNA to "
                        "individual nucleotides during phage infection."
                    ),
                },
                {
                    "node_id": "modified_mononucleotide_sensing",
                    "label": "modified mononucleotide sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Detection of the modified mononucleotide m6dAMP "
                        "as a signal of phage-mediated host-genome "
                        "degradation."
                    ),
                },
                {
                    "node_id": "type_specific_toxic_effector_activation",
                    "label": "type-specific toxic effector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of a Metis effector that depletes NAD "
                        "in type I systems or triggers membrane-linked "
                        "toxicity in type II systems."
                    ),
                },
                {
                    "node_id": "metis_system_trait",
                    "label": "Metis system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Metis phage-defense "
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
                    "subject": "metis_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "modified_mononucleotide_sensing",
                    "description": (
                        "Metis loci directly sense m6dAMP after "
                        "phage-mediated host-genome degradation."
                    ),
                    "evidence": [
                        osterman_system_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "phage_mediated_host_genome_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "modified_mononucleotide_sensing",
                    "description": (
                        "Accumulation of free m6dAMP after host-genome "
                        "degradation provides the modified mononucleotide "
                        "signal detected by Metis."
                    ),
                    "evidence": [
                        osterman_detection_and_degradation_evidence(),
                        osterman_escape_evidence(),
                    ],
                },
                {
                    "subject": "modified_mononucleotide_sensing",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "type_specific_toxic_effector_activation",
                    "description": (
                        "m6dAMP sensing activates a Metis type-specific "
                        "toxic effector."
                    ),
                    "evidence": [osterman_effector_evidence()],
                },
                {
                    "subject": "type_specific_toxic_effector_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "metis_system_trait",
                    "description": (
                        "Triggered Metis effector toxicity realizes the "
                        "Metis system trait by aborting phage infection."
                    ),
                    "evidence": [osterman_effector_abortion_evidence()],
                },
                {
                    "subject": "metis_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Metis system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        osterman_parent_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "metis-subtype-and-model-coverage-gap",
            "prompt": (
                "Resolve Metis type I and type II locus composition, "
                "native host breadth, profile-to-component mapping, "
                "subtype-specific effector biochemistry, and "
                "DefenseFinder HMM/rule coverage before minting narrower "
                "Metis mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Osterman et al. support Metis as a bacterial defense "
                "system that senses m6dAMP from phage-mediated host-genome "
                "degradation and activates type-specific toxic effectors. "
                "The pinned DefenseFinder article registry maps the Metis "
                "source key to the Osterman et al. preprint, but the pinned "
                "HMM inventory and rules table have no exact Metis rows. "
                "This first-pass record therefore does not resolve the "
                "complete locus model, subtype component boundaries, direct "
                "HMM/profile mapping, or native host breadth."
            ),
            "evidence": [
                osterman_system_evidence(),
                osterman_effector_evidence(),
                osterman_escape_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#metis_m6damp_toxic_effector_defense"],
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
            "Minted Metis system as a Science-, PubMed-, and "
            "DefenseFinder-backed GENOMICS TraitRecord under phage "
            "defense system after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, research, or "
            "prior proposal record; the replacement placeholder is "
            f"reserved in {PROPOSAL}."
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
            "Reviewed Metis system canonical_examples and left them empty "
            "because public PubMed and DefenseFinder evidence supports "
            "the named phage-defense system but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous Metis activity. No paid research was used."
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
