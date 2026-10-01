#!/usr/bin/env python3
"""Add the TagI system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "tagi_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

TAGI_DOI = "DOI:10.1093/nar/gky781"
TAGI_PMID = "PMID:30202937"
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
TIMESTAMP = "2026-10-01T11:10:00Z"
PARENT_TIMESTAMP = "2026-10-01T11:10:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T11:10:02Z"
IDENTIFIER = "traitmech:000513"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v390"

ARTICLE_ROW = (
    "| TagI | 10\\.1093/nar/gky781 | Crystal structure of the "
    "modification-dependent SRA-HNH endonuclease TagI | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "TagI, or VcaM4I families before minting narrower Type IV "
    "custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA or "
    "VcaM4I families before minting narrower Type IV custom-profile "
    "traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, TagI, and VcaM4I article-registry rows correspond to "
    "reusable organism-level traits below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV and VcaM4I article-registry rows correspond to reusable "
    "organism-level traits below this class."
)


def tagi_family_evidence() -> dict[str, str]:
    return {
        "reference": TAGI_PMID,
        "snippet": (
            "TagI belongs to the recently characterized SRA-HNH family of "
            "modification-dependent restriction endonucleases (REases) "
            "that also includes ScoA3IV (Sco5333) and TbiR51I (Tbis1)."
        ),
        "notes": (
            "Kisiala et al. support TagI as a member of an SRA-HNH "
            "modification-dependent restriction endonuclease family."
        ),
    }


def tagi_structure_evidence() -> dict[str, str]:
    return {
        "reference": TAGI_PMID,
        "snippet": (
            "Here, we present a crystal structure of dimeric TagI, which "
            "exhibits a DNA binding site formed jointly by the nuclease "
            "domains, and separate binding sites for modified DNA bases in "
            "the two protomers."
        ),
        "notes": (
            "Kisiala et al. support dimeric TagI structure with nuclease "
            "and modified-base-binding sites."
        ),
    }


def tagi_modified_base_evidence() -> dict[str, str]:
    return {
        "reference": TAGI_PMID,
        "snippet": (
            "Their pockets for the flipped bases are spacious enough to "
            "accommodate 5-methylcytosine (5mC) or "
            "5-hydroxymethylcytosine (5hmC), but not "
            "glucosyl-5-hydroxymethylcytosine (g5hmC)."
        ),
        "notes": (
            "Kisiala et al. support TagI recognition of flipped 5mC and "
            "5hmC bases."
        ),
    }


def tagi_phage_restriction_evidence() -> dict[str, str]:
    return {
        "reference": TAGI_PMID,
        "snippet": (
            "Such preference is in agreement with the biochemical "
            "determination of the TagI modification dependence and the "
            "results of phage restriction assays."
        ),
        "notes": (
            "Kisiala et al. support TagI modification dependence and phage "
            "restriction activity."
        ),
    }


def tagi_sequence_context_evidence() -> dict[str, str]:
    return {
        "reference": TAGI_PMID,
        "snippet": (
            "The ability of TagI to digest plasmids methylated by Dcm "
            "(C5mCWGG), M.Fnu4HI (G5mCNGC) or M.HpyCH4IV (A5mCGT) "
            "suggests that the SRA domains of the enzyme are tolerant to "
            "different sequence contexts of the modified base."
        ),
        "notes": (
            "Kisiala et al. support TagI digestion of multiple "
            "5mC-modified plasmid sequence contexts."
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
            "The pinned DefenseFinder article registry maps the TagI "
            "source key to the Kisiala et al. structural paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact TagI row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact TagI system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "TagI system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses a TagI-family locus encoding an SRA-HNH "
        "restriction endonuclease that recognizes 5-methylcytosine- or "
        "5-hydroxymethylcytosine-modified DNA."
    ),
    "definition_source": TAGI_DOI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "TagI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        tagi_family_evidence(),
        tagi_structure_evidence(),
        tagi_modified_base_evidence(),
        tagi_phage_restriction_evidence(),
        tagi_sequence_context_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "tagi_restricts_modified_cytosine_dna",
            "title": "TagI restricts modified-cytosine DNA",
            "description": (
                "Conservative system-level sketch linking a TagI-family "
                "locus to 5mC/5hmC-dependent DNA restriction and to the "
                "Type IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures TagI as a named Type IV "
                "modification-dependent restriction family while leaving "
                "natural host breadth, exact modified-DNA sequence-context "
                "specificity across SRA-HNH homologs, accession-level "
                "protein examples, and DefenseFinder RM_Type_IV HMM/rules "
                "mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "tagi_family_locus",
                    "label": "TagI-family locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a TagI-family SRA-HNH "
                        "modification-dependent restriction endonuclease."
                    ),
                },
                {
                    "node_id": "tagi_modified_cytosine_dna",
                    "label": "TagI-targeted modified-cytosine DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing 5-methylcytosine or "
                        "5-hydroxymethylcytosine in a TagI-family "
                        "recognition context."
                    ),
                },
                {
                    "node_id": "tagi_modified_cytosine_restriction",
                    "label": "TagI modified-cytosine DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "5mC/5hmC-modified DNA by a TagI-family "
                        "endonuclease."
                    ),
                },
                {
                    "node_id": "tagi_system_trait",
                    "label": "TagI system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded TagI-family "
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
                    "subject": "tagi_family_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "tagi_modified_cytosine_restriction",
                    "description": (
                        "TagI-family loci encode SRA-HNH endonucleases "
                        "that restrict 5mC/5hmC-modified DNA."
                    ),
                    "evidence": [
                        tagi_structure_evidence(),
                        tagi_modified_base_evidence(),
                    ],
                },
                {
                    "subject": "tagi_modified_cytosine_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "tagi_modified_cytosine_dna",
                    "description": (
                        "TagI-family restriction targets 5mC- or "
                        "5hmC-modified DNA."
                    ),
                    "evidence": [
                        tagi_modified_base_evidence(),
                        tagi_phage_restriction_evidence(),
                        tagi_sequence_context_evidence(),
                    ],
                },
                {
                    "subject": "tagi_modified_cytosine_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "tagi_system_trait",
                    "description": (
                        "TagI-family modified-cytosine DNA restriction "
                        "realizes the organism-level TagI system "
                        "possession trait."
                    ),
                    "evidence": [
                        tagi_family_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "tagi_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "TagI system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        tagi_family_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "tagi-defensefinder-model-gap",
            "prompt": (
                "Resolve TagI-family breadth, modified-cytosine "
                "sequence-context specificity across natural hosts, "
                "accession-level protein examples, and DefenseFinder "
                "RM_Type_IV HMM/rules mapping before minting narrower "
                "TagI mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kisiala et al. support TagI as an SRA-HNH "
                "modification-dependent restriction endonuclease that "
                "recognizes 5mC/5hmC bases and restricts phage in assays. "
                "The pinned DefenseFinder article registry maps TagI to "
                "that paper, but the pinned HMM inventory and rules table "
                "have no exact TagI rows. This first-pass record therefore "
                "does not resolve a reusable DefenseFinder profile model, "
                "exact accession-level protein examples, the breadth of "
                "TagI-like systems across natural hosts, or the complete "
                "set of natural modified-cytosine sequence contexts."
            ),
            "evidence": [
                tagi_family_evidence(),
                tagi_structure_evidence(),
                tagi_modified_base_evidence(),
                tagi_phage_restriction_evidence(),
                tagi_sequence_context_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#tagi_restricts_modified_cytosine_dna"
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
            "Documented TagI as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000513 for the TagI "
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
            "Minted TagI system as a DOI/PMID- and DefenseFinder-backed "
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
            "Reviewed TagI system during initial curation and left "
            "canonical_examples empty because Kisiala et al. support the "
            "purified TagI enzyme, structure, and phage restriction "
            "assays, but not a single stable NCBITaxon strain exemplar or "
            "accession-level protein example for the organism-level TagI "
            "system trait. No paid research was used."
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
            assert existing["label"] == "TagI system"
            assert existing["mapping_status"] == "PROPOSED"
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "TagI system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
