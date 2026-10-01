#!/usr/bin/env python3
"""Add the McrBC system genomics trait."""

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

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mcrbc_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

PANNE = "DOI:10.1093/emboj/20.12.3210"
LOENEN = "DOI:10.1093/nar/gkt747"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)
DEFENSEFINDER_HMMS = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/Liste_hmm_system.md"
)
DEFENSEFINDER_RULES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/DefenseFinder_rules.tsv"
)

CURATOR = "codex"
TIMESTAMP = "2026-10-01T03:37:00Z"
PARENT_TIMESTAMP = "2026-10-01T03:37:01Z"
IDENTIFIER = "traitmech:000505"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v382"

ARTICLE_ROW = (
    "| McrBC | 10\\.1093/emboj/20\\.12\\.3210 | The McrBC restriction "
    "endonuclease assembles into a ring structure in the presence of G "
    "nucleotides | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder RM_Type_IV "
    "custom Type_IV_REases profiles and characterized McrA, McrBC, GmrSD, "
    "MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before "
    "minting narrower Type IV custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder RM_Type_IV "
    "custom Type_IV_REases profiles and characterized McrA, GmrSD, MspJI, "
    "PvuRts1I, EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before minting "
    "narrower Type IV custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, Bair and Black support GmrSD as one "
    "glucosylated-HMC-targeting Type IV enzyme, and the pinned DefenseFinder "
    "registries support an RM_Type_IV namespace with a broad Type_IV_REases "
    "custom profile group. The evidence does not yet map any of the eight "
    "pinned RM_Type_IV HMM rows to exact characterized families or resolve "
    "whether the Other_Type_IV, McrBC, GmrSD_RM_Type_IV, MspJI, PvuRts1I, "
    "EcoKMcrA, ScoMcrA, TagI, and VcaM4I article-registry rows correspond to "
    "reusable organism-level traits below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, Bair and Black support GmrSD as one "
    "glucosylated-HMC-targeting Type IV enzyme, and the pinned DefenseFinder "
    "registries support an RM_Type_IV namespace with a broad Type_IV_REases "
    "custom profile group. The evidence does not yet map any of the eight "
    "pinned RM_Type_IV HMM rows to exact characterized families or resolve "
    "whether the Other_Type_IV, GmrSD_RM_Type_IV, MspJI, PvuRts1I, EcoKMcrA, "
    "ScoMcrA, TagI, and VcaM4I article-registry rows correspond to reusable "
    "organism-level traits below this class."
)


def mcrbc_restriction_evidence() -> dict[str, str]:
    return {
        "reference": PANNE,
        "snippet": (
            "McrBC from Escherichia coli K-12 is a restriction enzyme that "
            "belongs to the family of AAA(+) proteins and cuts DNA containing "
            "modified cytosines."
        ),
        "notes": (
            "Panne et al. identify McrBC from Escherichia coli K-12 as a "
            "restriction enzyme that attacks modified-cytosine DNA."
        ),
    }


def mcrb_binding_evidence() -> dict[str, str]:
    return {
        "reference": PANNE,
        "snippet": (
            "McrB(L) binds specifically to the methylated recognition site "
            "and is, therefore, the DNA-binding moiety of the McrBC "
            "endonuclease."
        ),
        "notes": (
            "Panne et al. support methylated-site DNA binding by McrB(L), "
            "one of the products of the E. coli K-12 mcrB gene."
        ),
    }


def mcrc_cleavage_evidence() -> dict[str, str]:
    return {
        "reference": PANNE,
        "snippet": (
            "In the presence of McrC, a subunit that is essential for DNA "
            "cleavage, the tetradecameric species was the major form of the "
            "endonuclease."
        ),
        "notes": (
            "Panne et al. support McrC as the cleavage-associated subunit of "
            "the McrBC endonuclease complex."
        ),
    }


def type_iv_name_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": (
            "The rgl genes were renamed mcrA and mcrBC (modified cytosine "
            "restriction)."
        ),
        "notes": (
            "Loenen and Raleigh place mcrBC in the modified-cytosine "
            "restriction branch that helped define Type IV restriction."
        ),
    }


def type_iv_class_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": (
            "The new class of modification-dependent restriction enzymes was "
            "named Type IV, as distinct from the familiar modification-blocked "
            "Types I-III."
        ),
        "notes": (
            "Loenen and Raleigh define the Type IV class as "
            "modification-dependent restriction enzymes."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the McrBC source "
            "key to Panne et al."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact McrBC row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder rules "
            "table found no exact McrBC system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "McrBC system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses an mcrBC locus encoding McrB DNA-binding and "
        "McrC cleavage-associated subunits that assemble into an McrBC "
        "restriction endonuclease complex targeting methylated "
        "cytosine-containing DNA."
    ),
    "definition_source": PANNE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "McrBC",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "McrBC restriction endonuclease",
            "synonym_type": "RELATED_SYNONYM",
            "source": PANNE,
        },
    ],
    "evidence": [
        mcrbc_restriction_evidence(),
        mcrb_binding_evidence(),
        mcrc_cleavage_evidence(),
        type_iv_name_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "note": (
                "Panne et al. characterized the McrBC endonuclease from "
                "Escherichia coli K-12."
            ),
            "reference": PANNE,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "mcrbc_restricts_methylated_cytosine_dna",
            "title": "McrBC restricts methylated-cytosine DNA",
            "description": (
                "Conservative system-level sketch linking an mcrBC locus to "
                "modification-dependent restriction of methylated-cytosine "
                "DNA and to the Type IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures McrBC as a named, E. coli K-12-derived "
                "Type IV modification-dependent restriction system while "
                "leaving exact McrB/McrC protein activities, complete "
                "modified-cytosine target breadth, natural host breadth, and "
                "DefenseFinder RM_Type_IV HMM/rules mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "mcrbc_locus",
                    "label": "mcrBC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding the McrB and McrC subunits of "
                        "the McrBC modification-dependent restriction "
                        "endonuclease."
                    ),
                },
                {
                    "node_id": "mcrbc_methylated_dna_restriction",
                    "label": "McrBC methylated-DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "McrBC endonuclease restriction of DNA containing "
                        "modified cytosines."
                    ),
                },
                {
                    "node_id": "mcrbc_system_trait",
                    "label": "McrBC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded McrBC "
                        "modification-dependent restriction system."
                    ),
                },
                {
                    "node_id": "type_iv_modification_dependent_restriction",
                    "label": "type IV modification-dependent restriction system",
                    "node_type": "TRAIT",
                    "grounding": TYPE_IV_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded Type IV "
                        "modification-dependent restriction system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "mcrbc_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mcrbc_methylated_dna_restriction",
                    "description": (
                        "The mcrBC locus encodes the McrBC endonuclease "
                        "subunits that bind and cleave modified-cytosine DNA."
                    ),
                    "evidence": [
                        mcrbc_restriction_evidence(),
                        mcrb_binding_evidence(),
                        mcrc_cleavage_evidence(),
                    ],
                },
                {
                    "subject": "mcrbc_methylated_dna_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "mcrbc_system_trait",
                    "description": (
                        "McrBC methylated-DNA restriction realizes the "
                        "organism-level McrBC system possession trait."
                    ),
                    "evidence": [
                        mcrbc_restriction_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "mcrbc_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "McrBC system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        type_iv_name_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mcrbc-defensefinder-model-gap",
            "prompt": (
                "Resolve exact McrB/McrC component activities, complete "
                "modified-cytosine target breadth, natural host breadth, and "
                "DefenseFinder RM_Type_IV HMM/rules mapping before minting "
                "narrower McrBC mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Panne et al. support McrBC from Escherichia coli K-12 as a "
                "restriction endonuclease complex that cuts DNA containing "
                "modified cytosines, and Loenen and Raleigh place mcrBC in "
                "the modified-cytosine restriction branch of Type IV "
                "modification-dependent restriction systems. The pinned "
                "DefenseFinder article registry maps the McrBC source key to "
                "Panne et al., but the pinned HMM inventory and rules table "
                "have no exact McrBC rows. This first-pass record therefore "
                "does not resolve a reusable DefenseFinder profile model, "
                "the exact relationship between individual McrB and McrC "
                "molecular functions and organism-level McrBC possession, "
                "the complete set of modified-cytosine targets, or the "
                "natural host breadth of McrBC systems."
            ),
            "evidence": [
                mcrbc_restriction_evidence(),
                mcrb_binding_evidence(),
                mcrc_cleavage_evidence(),
                type_iv_name_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#mcrbc_restricts_methylated_cytosine_dna"],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        }
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_type_iv_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == TYPE_IV_PARENT_ID
    assert record["label"] == "type IV modification-dependent restriction system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussion = next(
        item
        for item in record.get("discussions") or []
        if item.get("discussion_id") == "type-iv-rm-profile-interpretation-gap"
    )
    if (
        discussion["prompt"] == NEW_PARENT_PROMPT
        and discussion["rationale"] == NEW_PARENT_RATIONALE
    ):
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["prompt"] == OLD_PARENT_PROMPT
    assert discussion["status"] == "OPEN"
    assert discussion["rationale"] == OLD_PARENT_RATIONALE

    discussion["prompt"] = NEW_PARENT_PROMPT
    discussion["rationale"] = NEW_PARENT_RATIONALE
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=(
            "Documented McrBC as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000505 for the McrBC "
            "system; other RM_Type_IV custom HMM and article-registry "
            "families remain open."
        ),
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted McrBC system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the type IV modification-dependent "
            "restriction system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / TYPE_IV_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_type_iv_parent(load_trait(TYPE_IV_PARENT))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "McrBC system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
