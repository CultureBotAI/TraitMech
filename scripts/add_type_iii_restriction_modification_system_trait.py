#!/usr/bin/env python3
"""Add the type III restriction-modification system genomics trait."""

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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iii_restriction_modification_system.yaml"
)

BUTTERER = "DOI:10.1093/nar/gku122"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T15:29:46Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T15:29:47Z"
POSED_DATE = "2026-09-30"
IDENTIFIER = "traitmech:000495"
PROPOSAL = "proposals/metpo_traitmech_v372"
SLUG = "type_iii_restriction_modification"

TYPE_III_ARCHITECTURE_SNIPPET = (
    "The Type III REs are hetero-oligomeric assemblies, comprising "
    "polypeptides encoded by the res (restriction) and mod (modification) "
    "genes (4)."
)
TYPE_III_STOICHIOMETRY_SNIPPET = (
    "In this study, we present a series of results obtained by native mass "
    "spectrometry and size exclusion chromatography with multi-angle light "
    "scattering consistent with a 1:2 ratio of Res to Mod subunits in the "
    "EcoP15I, EcoPI and PstII complexes as the main holoenzyme species and "
    "a 1:1 stoichiometry of specific DNA (sDNA) binding by EcoP15I and "
    "EcoPI."
)
ARTICLE_REGISTRY_SNIPPET = (
    "RM_Type_III | 10\\.1093/nar/gkac975 | REBASE: a database for DNA "
    "restriction and modification: enzymes, genes and genomes"
)
RULES_SNIPPET = (
    "RM\tRM_Type_III\t2\t2\tRM_Type_III__Type_III_MTases, "
    "RM_Type_III__Type_III_REases\t\t\t"
)
HMM_MTASE_SNIPPET = (
    f"| {'RM_Type_III__Type_III_MTases_FAM_0':<49}| {'':<49}| "
    f"{'RM_Type_III':<23}| {'Custom':<24}| 100    |\n"
    f"| {'RM_Type_III__Type_III_MTases_FAM_1':<49}| {'':<49}| "
    f"{'RM_Type_III':<23}| {'Custom':<24}| 100    |"
)
HMM_REASE_SNIPPET = (
    f"| {'RM_Type_III__Type_III_REases_FAM_0.einsi_trimmed':<49}| "
    f"{'':<49}| {'RM_Type_III':<23}| {'Custom':<24}| 22     |\n"
    f"| {'RM_Type_III__Type_III_REases_FAM_1.einsi_trimmed':<49}| "
    f"{'':<49}| {'RM_Type_III':<23}| {'Custom':<24}| 22     |"
)


def type_iii_architecture_evidence() -> dict[str, str]:
    return {
        "reference": BUTTERER,
        "snippet": TYPE_III_ARCHITECTURE_SNIPPET,
        "notes": (
            "Butterer et al. describe Type III restriction endonucleases as "
            "hetero-oligomeric assemblies encoded by res restriction and mod "
            "modification genes."
        ),
    }


def type_iii_stoichiometry_evidence() -> dict[str, str]:
    return {
        "reference": BUTTERER,
        "snippet": TYPE_III_STOICHIOMETRY_SNIPPET,
        "notes": (
            "Butterer et al. support a Type III R-M holoenzyme model with "
            "one Res subunit and two Mod subunits for characterized EcoP15I, "
            "EcoPI, and PstII complexes."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the RM_Type_III "
            "model namespace to the REBASE update."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RM_Type_III as an RM "
            "subsystem requiring Type_III_MTases and Type_III_REases profile "
            "groups."
        ),
    }


def mtase_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_MTASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom Type III "
            "methyltransferase profiles under the RM_Type_III system "
            "namespace."
        ),
    }


def rease_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_REASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom Type III "
            "restriction-endonuclease profiles under the RM_Type_III system "
            "namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "type III restriction-modification system",
    "definition": (
        "A restriction-modification system in which an organism possesses a "
        "Type III R-M locus encoding Mod-like DNA methyltransferase and "
        "Res-like ATP-dependent restriction subunits, including RM_Type_III "
        "loci represented by DefenseFinder."
    ),
    "definition_source": BUTTERER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000095"],
    "synonyms": [
        {
            "synonym_text": "RM_Type_III",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "RM_Type_III__Type_III_MTases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "RM_Type_III__Type_III_REases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        type_iii_architecture_evidence(),
        type_iii_stoichiometry_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        mtase_hmm_evidence(),
        rease_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "type_iii_rm_locus_restricts_foreign_dna",
            "title": "Type III R-M loci mark self and restrict foreign DNA",
            "description": (
                "Conservative system-level sketch linking Type III "
                "restriction-modification loci to "
                "restriction-modification-mediated foreign DNA cleavage."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures a reusable Type III R-M locus "
                "architecture and the DefenseFinder RM_Type_III "
                "custom-profile namespace without asserting an "
                "accession-level mapping between any custom HMM row and "
                "characterized Res or Mod families."
            ),
            "nodes": [
                {
                    "node_id": "type_iii_rm_locus",
                    "label": "type III restriction-modification locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Type III R-M locus encoding Mod-like and "
                        "Res-like subunits."
                    ),
                },
                {
                    "node_id": "foreign_unmethylated_dna_cleavage",
                    "label": "foreign unmethylated DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of invading DNA that has not been "
                        "protected by cognate methylation."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "type III restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded type III "
                        "restriction-modification system."
                    ),
                },
                {
                    "node_id": "restriction_modification_system",
                    "label": "restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000095",
                    "description": (
                        "Possession of a methyltransferase and restriction "
                        "endonuclease system for self/non-self DNA "
                        "discrimination."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "type_iii_rm_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "foreign_unmethylated_dna_cleavage",
                    "description": (
                        "Type III R-M loci encode the Mod and Res functions "
                        "needed to recognize, methylate, and cleave DNA at "
                        "Type III recognition sites."
                    ),
                    "evidence": [
                        type_iii_architecture_evidence(),
                        type_iii_stoichiometry_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "foreign_unmethylated_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Type III restriction-modification activity "
                        "realizes the organism-level Type III R-M system "
                        "trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        mtase_hmm_evidence(),
                        rease_hmm_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "restriction_modification_system",
                    "description": (
                        "A Type III R-M system is a subtype of broader "
                        "restriction-modification system possession."
                    ),
                    "evidence": [
                        type_iii_architecture_evidence(),
                        type_iii_stoichiometry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "type-iii-rm-profile-interpretation-gap",
            "prompt": (
                "Resolve the accession-level relationships between "
                "DefenseFinder RM_Type_III custom methyltransferase and "
                "restriction-endonuclease profiles and characterized Mod "
                "and Res families before minting narrower Type III protein "
                "or custom-profile traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Butterer et al. support Type III R-M Res/Mod architecture, "
                "while the pinned DefenseFinder registry supports an "
                "RM_Type_III namespace with broad Type_III_MTases and "
                "Type_III_REases custom profile groups. The evidence does "
                "not yet map individual custom profile rows to exact "
                "characterized Res or Mod families or resolve whether each "
                "source-model boundary corresponds to a reusable "
                "organism-level trait below this class."
            ),
            "evidence": [
                type_iii_architecture_evidence(),
                type_iii_stoichiometry_evidence(),
                rules_evidence(),
                mtase_hmm_evidence(),
                rease_hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#type_iii_rm_locus_restricts_foreign_dna"
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
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
            "Minted type III restriction-modification system as a "
            "DOI-backed GENOMICS TraitRecord under "
            "restriction-modification system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
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
            "Reviewed type III restriction-modification system during "
            "initial curation and left canonical_examples empty because "
            "the sources support a broad Type III R-M class, a "
            "DefenseFinder system model, and multiple biochemical enzyme "
            "examples, but not a single stable NCBITaxon strain exemplar "
            "for the whole broad Type III branch. No paid research was "
            "used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
