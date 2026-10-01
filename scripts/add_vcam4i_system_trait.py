#!/usr/bin/env python3
"""Add the VcaM4I system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "vcam4i_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

VCAM4I_DOI = "DOI:10.1093/nar/gkaa1218"
LOENEN = "DOI:10.1093/nar/gkt747"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T11:48:00Z"
PARENT_TIMESTAMP = "2026-10-01T11:48:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T11:48:02Z"
IDENTIFIER = "traitmech:000514"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v391"

ARTICLE_ROW = (
    "| VcaM4I | 10\\.1093/nar/gkaa1218 | Crystal structures of the "
    "EVE-HNH endonuclease VcaM4I in the presence and absence of DNA | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA or "
    "VcaM4I families before minting narrower Type IV custom-profile "
    "traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and the characterized "
    "McrA family before minting narrower Type IV custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV and VcaM4I article-registry rows correspond to reusable "
    "organism-level traits below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to the characterized McrA family or resolve whether the "
    "Other_Type_IV article-registry row corresponds to a reusable "
    "organism-level trait below this class."
)


def vcam4i_eve_hnh_evidence() -> dict[str, str]:
    return {
        "reference": VCAM4I_DOI,
        "snippet": (
            "EVE domains belong to the PUA superfamily, and are present "
            "in MDREs in combination with HNH nuclease domains."
        ),
        "notes": (
            "Mierzejewska et al. support the EVE-HNH architecture of "
            "VcaM4I-family modification-dependent restriction "
            "endonucleases."
        ),
    }


def vcam4i_structure_evidence() -> dict[str, str]:
    return {
        "reference": VCAM4I_DOI,
        "snippet": (
            "Here, we present a biochemical characterization of the "
            "EVE-HNH endonuclease VcaM4I and crystal structures of the "
            "protein alone, with EVE domain bound to either 5mC modified "
            "dsDNA or to 5mC/5hmC containing ssDNA."
        ),
        "notes": (
            "Mierzejewska et al. biochemically characterized VcaM4I and "
            "solved structures of apo and modified-DNA-bound enzyme."
        ),
    }


def vcam4i_modified_base_evidence() -> dict[str, str]:
    return {
        "reference": VCAM4I_DOI,
        "snippet": (
            "The EVE domain is moderately specific for 5mC/5hmC "
            "containing DNA according to EMSA experiments."
        ),
        "notes": (
            "Mierzejewska et al. support VcaM4I EVE-domain recognition "
            "of 5mC/5hmC-containing DNA."
        ),
    }


def vcam4i_autoinhibition_evidence() -> dict[str, str]:
    return {
        "reference": VCAM4I_DOI,
        "snippet": (
            "Removal of the EVE domain and inter-domain linker, but not "
            "of the EVE domain alone converts VcaM4I into a non-specific "
            "toxic nuclease."
        ),
        "notes": (
            "Mierzejewska et al. support VcaM4I as a nuclease whose "
            "domain organization modulates toxic DNA cleavage."
        ),
    }


def vcam4i_variant_evidence() -> dict[str, str]:
    return {
        "reference": VCAM4I_DOI,
        "snippet": (
            "The role of the key residues in the EVE and HNH domains of "
            "VcaM4I is confirmed by digestion and restriction assays with "
            "the enzyme variants that differ from the wild-type by "
            "changes to the base binding pocket or to the catalytic "
            "residues."
        ),
        "notes": (
            "Mierzejewska et al. support the VcaM4I EVE base-binding "
            "pocket and HNH catalytic residues by digestion and "
            "restriction assays."
        ),
    }


def type_iv_class_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": (
            "The new class of modification-dependent restriction enzymes "
            "was named Type IV, as distinct from the familiar "
            "modification-blocked Types I-III."
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
            "The pinned DefenseFinder article registry maps the VcaM4I "
            "source key to the Mierzejewska et al. structural paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "HMM inventory found no exact VcaM4I row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact VcaM4I system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "VcaM4I system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses a VcaM4I-family locus encoding an EVE-HNH "
        "restriction endonuclease that recognizes 5-methylcytosine- or "
        "5-hydroxymethylcytosine-modified DNA."
    ),
    "definition_source": VCAM4I_DOI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "VcaM4I",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        vcam4i_eve_hnh_evidence(),
        vcam4i_structure_evidence(),
        vcam4i_modified_base_evidence(),
        vcam4i_autoinhibition_evidence(),
        vcam4i_variant_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "vcam4i_restricts_modified_cytosine_dna",
            "title": "VcaM4I restricts modified-cytosine DNA",
            "description": (
                "Conservative system-level sketch linking a VcaM4I-family "
                "locus to EVE-HNH 5mC/5hmC-dependent DNA restriction and "
                "to the Type IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures VcaM4I as a named Type IV "
                "modification-dependent restriction family while leaving "
                "natural host breadth, exact modified-DNA sequence-context "
                "specificity across EVE-HNH homologs, accession-level "
                "protein examples, and DefenseFinder RM_Type_IV HMM/rules "
                "mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "vcam4i_family_locus",
                    "label": "VcaM4I-family locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a VcaM4I-family EVE-HNH "
                        "modification-dependent restriction endonuclease."
                    ),
                },
                {
                    "node_id": "vcam4i_modified_cytosine_dna",
                    "label": "VcaM4I-targeted modified-cytosine DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing 5-methylcytosine or "
                        "5-hydroxymethylcytosine in a VcaM4I-family "
                        "recognition context."
                    ),
                },
                {
                    "node_id": "vcam4i_eve_hnh_restriction",
                    "label": "VcaM4I EVE-HNH DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "5mC/5hmC-modified DNA by a VcaM4I-family "
                        "EVE-HNH endonuclease."
                    ),
                },
                {
                    "node_id": "vcam4i_system_trait",
                    "label": "VcaM4I system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded VcaM4I-family "
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
                    "subject": "vcam4i_family_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "vcam4i_eve_hnh_restriction",
                    "description": (
                        "VcaM4I-family loci encode EVE-HNH endonucleases "
                        "that restrict 5mC/5hmC-modified DNA."
                    ),
                    "evidence": [
                        vcam4i_eve_hnh_evidence(),
                        vcam4i_structure_evidence(),
                    ],
                },
                {
                    "subject": "vcam4i_eve_hnh_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "vcam4i_modified_cytosine_dna",
                    "description": (
                        "VcaM4I-family EVE-HNH restriction targets 5mC- "
                        "or 5hmC-modified DNA."
                    ),
                    "evidence": [
                        vcam4i_modified_base_evidence(),
                        vcam4i_variant_evidence(),
                    ],
                },
                {
                    "subject": "vcam4i_eve_hnh_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "vcam4i_system_trait",
                    "description": (
                        "VcaM4I-family EVE-HNH DNA restriction realizes "
                        "the organism-level VcaM4I system possession "
                        "trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "vcam4i_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "VcaM4I system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        vcam4i_autoinhibition_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "vcam4i-defensefinder-model-gap",
            "prompt": (
                "Resolve VcaM4I-family breadth, modified-cytosine "
                "sequence-context specificity across natural hosts, "
                "accession-level protein examples, and DefenseFinder "
                "RM_Type_IV HMM/rules mapping before minting narrower "
                "VcaM4I mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mierzejewska et al. support VcaM4I as an EVE-HNH "
                "modification-dependent restriction endonuclease that "
                "recognizes 5mC/5hmC DNA and validate EVE-domain "
                "modified-base binding plus HNH catalytic residues by "
                "digestion and restriction assays. The pinned "
                "DefenseFinder article registry maps VcaM4I to that "
                "paper, but the pinned HMM inventory and rules table "
                "have no exact VcaM4I rows. This first-pass record "
                "therefore does not resolve a reusable DefenseFinder "
                "profile model, exact accession-level protein examples, "
                "the breadth of VcaM4I-like systems across natural "
                "hosts, or the complete set of natural modified-cytosine "
                "sequence contexts."
            ),
            "evidence": [
                vcam4i_eve_hnh_evidence(),
                vcam4i_structure_evidence(),
                vcam4i_modified_base_evidence(),
                vcam4i_variant_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#vcam4i_restricts_modified_cytosine_dna"
            ],
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
            "Documented VcaM4I as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000514 for the VcaM4I "
            "system; McrA and Other_Type_IV remain open."
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
            "Minted VcaM4I system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the type IV "
            "modification-dependent restriction system parent after an "
            "ignored-and-hidden duplicate review found no exact "
            "same-scope live TraitMech, METPO, history, or prior proposal "
            f"record; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed VcaM4I system during initial curation and left "
            "canonical_examples empty because Mierzejewska et al. support "
            "the purified VcaM4I enzyme, structures, and restriction "
            "assays, but not a single stable NCBITaxon strain exemplar or "
            "accession-level protein example for the organism-level "
            "VcaM4I system trait. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
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
            existing = load_trait(TARGET)
            assert existing["identifier"] == IDENTIFIER
            assert existing["label"] == "VcaM4I system"
            assert existing["mapping_status"] == "PROPOSED"
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "VcaM4I system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
