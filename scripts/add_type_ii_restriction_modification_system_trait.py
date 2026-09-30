#!/usr/bin/env python3
"""Add the type II restriction-modification system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_ii_restriction_modification_system.yaml"
)
TYPE_IIG_TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iig_restriction_modification_system.yaml"
)

KIRILLOV = "DOI:10.1093/nar/gkac1124"
PINGOUD = "DOI:10.1093/nar/gku447"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T13:40:53Z"
REPARENT_TIMESTAMP = "2026-09-30T13:40:54Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T13:40:55Z"
POSED_DATE = "2026-09-30"
IDENTIFIER = "traitmech:000493"
PROPOSAL = "proposals/metpo_traitmech_v370"
SLUG = "type_ii_restriction_modification"

TYPE_II_SYSTEM_SNIPPET = (
    "The action of Type II restriction-modification (RM) systems depends on "
    "restriction endonuclease (REase), which cleaves foreign DNA at specific "
    "sites, and methyltransferase (MTase), which protects host genome from "
    "restriction by methylating the same sites."
)
TYPE_II_REASE_SNIPPET = (
    "Type II REases are produced by prokaryotes to combat bacteriophages. "
    "With extreme accuracy, each recognizes a particular sequence in "
    "double-stranded DNA and cleaves at a fixed position within or nearby."
)
TYPE_II_SOURCE_SNIPPET = (
    "REBASE (rebase.neb.com/rebase/rebase.html), the definitive source for "
    "information on REases and their companion proteins"
)
TYPE_IIG_SUBTYPE_SNIPPET = (
    "Type IIG (symmetric or asymmetric target sites; endonuclease activity "
    "affected by AdoMet (SAM))"
)
ARTICLE_REGISTRY_SNIPPET = (
    "RM_Type_II | 10\\.1093/nar/gkac975 | REBASE: a database for DNA "
    "restriction and modification: enzymes, genes and genomes"
)
RULES_SNIPPET = (
    "RM\tRM_Type_II\t2\t2\tRM_Type_II__Type_II_MTases, "
    "RM_Type_II__Type_II_REases\t\t\t"
)
HMM_MTASE_SNIPPET = (
    "| RM_Type_II__Type_II_MTases_FAM_0                 |"
    "                                                  | RM_Type_II"
    "             | Custom                  | 20     |"
)
HMM_REASE_SNIPPET = (
    "| RM_Type_II__Type_II_REase01                      |"
    "                                                  | RM_Type_II"
    "             | Custom                  | 20     |"
)


def type_ii_system_evidence() -> dict[str, str]:
    return {
        "reference": KIRILLOV,
        "snippet": TYPE_II_SYSTEM_SNIPPET,
        "notes": (
            "Kirillov et al. describe Type II restriction-modification "
            "systems as requiring a restriction endonuclease that cleaves "
            "foreign DNA and a methyltransferase that protects host DNA by "
            "methylating the same sites."
        ),
    }


def type_ii_rease_evidence() -> dict[str, str]:
    return {
        "reference": PINGOUD,
        "snippet": TYPE_II_REASE_SNIPPET,
        "notes": (
            "Pingoud et al. review Type II restriction endonucleases as "
            "prokaryotic phage-defense enzymes that recognize specific "
            "double-stranded DNA sequences and cleave at fixed positions "
            "within or near those sequences."
        ),
    }


def rebase_context_evidence() -> dict[str, str]:
    return {
        "reference": PINGOUD,
        "snippet": TYPE_II_SOURCE_SNIPPET,
        "notes": (
            "Pingoud et al. point to REBASE as the source for restriction "
            "endonucleases and companion proteins; DefenseFinder links its "
            "RM_Type_II model namespace to the 2023 REBASE update."
        ),
    }


def type_iig_subtype_evidence() -> dict[str, str]:
    return {
        "reference": "DOI:10.1038/srep03838",
        "snippet": TYPE_IIG_SUBTYPE_SNIPPET,
        "notes": (
            "Zhu et al. place Type IIG enzymes in the Type II restriction "
            "enzyme classification, supporting the Type IIG child record's "
            "reparenting beneath this Type II R-M parent."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the RM_Type_II "
            "model namespace to the REBASE update."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RM_Type_II as an RM "
            "subsystem requiring Type_II_MTases and Type_II_REases profile "
            "groups."
        ),
    }


def mtase_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_MTASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom "
            "methyltransferase profiles under the RM_Type_II system "
            "namespace."
        ),
    }


def rease_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_REASE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists custom restriction "
            "endonuclease profiles under the RM_Type_II system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "type II restriction-modification system",
    "definition": (
        "A restriction-modification system in which an organism possesses a "
        "Type II restriction endonuclease activity paired with cognate "
        "methyltransferase self-protection, including conventional "
        "RM_Type_II loci represented by DefenseFinder."
    ),
    "definition_source": KIRILLOV,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000095"],
    "synonyms": [
        {
            "synonym_text": "RM_Type_II",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "RM_Type_II__Type_II_MTases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "RM_Type_II__Type_II_REases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        type_ii_system_evidence(),
        type_ii_rease_evidence(),
        rebase_context_evidence(),
        type_iig_subtype_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        mtase_hmm_evidence(),
        rease_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "type_ii_rm_locus_restricts_foreign_dna",
            "title": "Type II R-M loci mark self and restrict foreign DNA",
            "description": (
                "Conservative system-level sketch linking Type II "
                "restriction-modification loci to "
                "restriction-modification-mediated foreign DNA cleavage."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures a reusable Type II R-M locus "
                "architecture and the DefenseFinder RM_Type_II "
                "custom-profile namespace without asserting an "
                "accession-level mapping between any custom HMM row and "
                "characterized Type II restriction endonucleases or "
                "methyltransferases."
            ),
            "nodes": [
                {
                    "node_id": "type_ii_rm_locus",
                    "label": "type II restriction-modification locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Type II R-M locus encoding restriction "
                        "endonuclease activity and cognate DNA "
                        "methyltransferase activity."
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
                    "label": "type II restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded type II "
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
                    "subject": "type_ii_rm_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "foreign_unmethylated_dna_cleavage",
                    "description": (
                        "Type II R-M loci encode the paired restriction and "
                        "methylation functions needed to cleave unprotected "
                        "foreign DNA."
                    ),
                    "evidence": [
                        type_ii_rease_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "foreign_unmethylated_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Type II restriction-modification activity realizes "
                        "the organism-level Type II R-M system trait."
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
                        "A Type II R-M system is a subtype of broader "
                        "restriction-modification system possession."
                    ),
                    "evidence": [
                        type_ii_system_evidence(),
                        rebase_context_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "type-ii-rm-profile-interpretation-gap",
            "prompt": (
                "Resolve the accession-level relationships between "
                "DefenseFinder RM_Type_II custom methyltransferase and "
                "restriction-endonuclease profiles, characterized Type II "
                "enzyme families, and Type IIG subclass boundaries before "
                "minting narrower Type II protein or custom-profile traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kirillov et al. and Pingoud et al. support Type II R-M "
                "system architecture and Type II restriction-endonuclease "
                "activity, while the pinned DefenseFinder registry supports "
                "an RM_Type_II namespace with broad custom MTase and REase "
                "profile groups. The evidence does not yet map individual "
                "custom profile rows to exact characterized enzyme families "
                "or resolve whether each source-model boundary corresponds "
                "to a reusable organism-level trait below this class."
            ),
            "evidence": [
                type_ii_system_evidence(),
                type_ii_rease_evidence(),
                rules_evidence(),
                mtase_hmm_evidence(),
                rease_hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#type_ii_rm_locus_restricts_foreign_dna"
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
            "Minted type II restriction-modification system as a "
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
            "Reviewed type II restriction-modification system during "
            "initial curation and left canonical_examples empty because the "
            "sources support a broad Type II R-M class, a DefenseFinder "
            "system model, and many biochemical enzyme examples, but not a "
            "single stable NCBITaxon strain exemplar for the whole broad "
            "Type II branch. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def write_type_iig_reparent(*, apply: bool) -> None:
    record = yaml.safe_load(TYPE_IIG_TARGET.read_text(encoding="utf-8"))
    if record.get("identifier") != "traitmech:000375":
        raise ValueError("unexpected type IIG identifier")
    if record.get("label") != "type IIG restriction-modification system":
        raise ValueError("unexpected type IIG label")
    if record.get("parent_traits") != ["traitmech:000095"]:
        raise ValueError("type IIG parent already differs from the expected broad parent")

    record["parent_traits"] = [IDENTIFIER]
    record_curation_event(
        record,
        action="REPARENT_TO_TYPE_II_RM",
        changes=(
            "Reparented type IIG restriction-modification system from the "
            "broad restriction-modification system to the newly minted "
            "type II restriction-modification system parent, preserving "
            "Type IIG as a narrower Type II R-M architecture while keeping "
            "unresolved DefenseFinder profile interpretations in an open "
            "knowledge gap."
        ),
        curator=CURATOR,
        timestamp=REPARENT_TIMESTAMP,
        llm_assisted=True,
    )
    if apply:
        write_validated_trait(record, TYPE_IIG_TARGET)
    else:
        print(f"Would update {TYPE_IIG_TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_new_record(apply=args.apply)
    write_type_iig_reparent(apply=args.apply)


if __name__ == "__main__":
    main()
