#!/usr/bin/env python3
"""Add the type I restriction-modification system genomics trait."""

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
    / "type_i_restriction_modification_system.yaml"
)

LOENEN = "DOI:10.1093/nar/gkt847"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T14:49:40Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T14:49:41Z"
POSED_DATE = "2026-09-30"
IDENTIFIER = "traitmech:000494"
PROPOSAL = "proposals/metpo_traitmech_v371"
SLUG = "type_i_restriction_modification"

TYPE_I_ARCHITECTURE_SNIPPET = (
    "Type I restriction enzymes (REases) are large pentameric proteins with "
    "separate restriction (R), methylation (M) and DNA sequence-recognition "
    "(S) subunits."
)
TYPE_I_ENZYME_ACTIVITY_SNIPPET = (
    "Type I R–M enzymes are pentameric proteins of composition 2R+2M+S."
)
ARTICLE_REGISTRY_SNIPPET = (
    "RM_Type_I | 10\\.1093/nar/gkac975 | REBASE: a database for DNA "
    "restriction and modification: enzymes, genes and genomes"
)
RULES_SNIPPET = (
    "RM\tRM_Type_I\t2\t2\tRM__Type_I_MTases, RM__Type_I_REases\t"
    "RM__Type_I_S\t\t"
)
HMM_MTASE_SNIPPET = (
    f"| {'RM__Type_I_MTases_FAM_0':<49}| {'':<49}| {'RM':<23}| "
    f"{'Custom':<24}| 150    |"
)
HMM_REASE_SNIPPET = (
    f"| {'RM__Type_I_REases_FAM_0.einsi_trimmed':<49}| {'':<49}| "
    f"{'RM':<23}| {'Custom':<24}| 34     |"
)
HMM_SPECIFICITY_SNIPPET = (
    f"| {'RM__Type_I_S_01':<49}| {'':<49}| {'RM':<23}| "
    f"{'Custom':<24}| 75     |"
)


def type_i_architecture_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": TYPE_I_ARCHITECTURE_SNIPPET,
        "notes": (
            "Loenen et al. define Type I restriction enzymes as pentameric "
            "systems with distinct restriction, methylation, and "
            "sequence-recognition subunits."
        ),
    }


def type_i_activity_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": TYPE_I_ENZYME_ACTIVITY_SNIPPET,
        "notes": (
            "Loenen et al. describe the Type I R-M enzyme complex as a "
            "2R+2M+S pentamer with both restriction-endonuclease and "
            "methyltransferase activities."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the RM_Type_I "
            "model namespace to the REBASE update."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RM_Type_I as an RM "
            "subsystem requiring Type_I_MTases and Type_I_REases profile "
            "groups with Type_I_S as an accessory specificity-subunit group."
        ),
    }


def mtase_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_MTASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom Type I "
            "methyltransferase profiles under the broad RM system namespace."
        ),
    }


def rease_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_REASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom Type I "
            "restriction-endonuclease profiles under the broad RM system "
            "namespace."
        ),
    }


def specificity_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SPECIFICITY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom Type I "
            "specificity-subunit profiles under the broad RM system "
            "namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "type I restriction-modification system",
    "definition": (
        "A restriction-modification system in which an organism possesses a "
        "Type I R-M locus encoding a pentameric enzyme with HsdR-like "
        "restriction, HsdM-like methylation, and HsdS-like DNA "
        "sequence-recognition subunits, including RM_Type_I loci "
        "represented by DefenseFinder."
    ),
    "definition_source": LOENEN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000095"],
    "synonyms": [
        {
            "synonym_text": "RM_Type_I",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "RM__Type_I_MTases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "RM__Type_I_REases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "RM__Type_I_S",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        type_i_architecture_evidence(),
        type_i_activity_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        mtase_hmm_evidence(),
        rease_hmm_evidence(),
        specificity_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "type_i_rm_locus_restricts_foreign_dna",
            "title": "Type I R-M loci mark self and restrict foreign DNA",
            "description": (
                "Conservative system-level sketch linking Type I "
                "restriction-modification loci to "
                "restriction-modification-mediated foreign DNA cleavage."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures a reusable Type I R-M locus "
                "architecture and the DefenseFinder RM_Type_I "
                "system namespace without asserting an accession-level "
                "mapping between any custom HMM row and characterized "
                "HsdR, HsdM, or HsdS families."
            ),
            "nodes": [
                {
                    "node_id": "type_i_rm_locus",
                    "label": "type I restriction-modification locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Type I R-M locus encoding restriction, "
                        "methylation, and sequence-recognition subunits."
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
                    "label": "type I restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded type I "
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
                    "subject": "type_i_rm_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "foreign_unmethylated_dna_cleavage",
                    "description": (
                        "Type I R-M loci encode the restriction, "
                        "methylation, and specificity functions needed to "
                        "recognize and cleave unprotected foreign DNA."
                    ),
                    "evidence": [
                        type_i_activity_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "foreign_unmethylated_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Type I restriction-modification activity realizes "
                        "the organism-level Type I R-M system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        mtase_hmm_evidence(),
                        rease_hmm_evidence(),
                        specificity_hmm_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "restriction_modification_system",
                    "description": (
                        "A Type I R-M system is a subtype of broader "
                        "restriction-modification system possession."
                    ),
                    "evidence": [
                        type_i_architecture_evidence(),
                        type_i_activity_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "type-i-rm-profile-interpretation-gap",
            "prompt": (
                "Resolve the accession-level relationships between "
                "DefenseFinder RM Type I custom methyltransferase, "
                "restriction-endonuclease, and specificity-subunit profiles "
                "and characterized HsdR, HsdM, and HsdS families before "
                "minting narrower Type I protein or custom-profile traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Loenen et al. support Type I R-M system architecture and "
                "restriction/modification activity, while the pinned "
                "DefenseFinder registry supports an RM_Type_I namespace "
                "with broad Type_I_MTases, Type_I_REases, and Type_I_S "
                "custom profile groups. The evidence does not yet map "
                "individual custom profile rows to exact characterized "
                "Hsd families or resolve whether each source-model boundary "
                "corresponds to a reusable organism-level trait below this "
                "class."
            ),
            "evidence": [
                type_i_architecture_evidence(),
                type_i_activity_evidence(),
                rules_evidence(),
                mtase_hmm_evidence(),
                rease_hmm_evidence(),
                specificity_hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#type_i_rm_locus_restricts_foreign_dna"
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
            "Minted type I restriction-modification system as a DOI-backed "
            "GENOMICS TraitRecord under restriction-modification system "
            "after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
            "Reviewed type I restriction-modification system during initial "
            "curation and left canonical_examples empty because the sources "
            "support a broad Type I R-M class, a DefenseFinder system model, "
            "and multiple biochemical enzyme examples, but not a single "
            "stable NCBITaxon strain exemplar for the whole broad Type I "
            "branch. No paid research was used."
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
