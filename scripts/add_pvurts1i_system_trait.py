#!/usr/bin/env python3
"""Add the PvuRts1I system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pvurts1i_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

PVURTS1I_2011 = "DOI:10.1093/nar/gkr607"
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
TIMESTAMP = "2026-10-01T09:01:00Z"
PARENT_TIMESTAMP = "2026-10-01T09:01:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T09:01:02Z"
REVIEW_TIMESTAMP = "2026-10-01T09:28:12Z"
IDENTIFIER = "traitmech:000511"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v388"

ARTICLE_ROW = (
    "| PvuRts1I | 10\\.1093/nar/gkr607 | Comparative characterization "
    "of the PvuRts1I family of restriction enzymes and their application "
    "in mapping genomic 5-hydroxymethylcytosine | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "PvuRts1I, ScoMcrA, TagI, or VcaM4I families before minting narrower "
    "Type IV custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "ScoMcrA, TagI, or VcaM4I families before minting narrower Type IV "
    "custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, PvuRts1I, ScoMcrA, TagI, and VcaM4I article-registry "
    "rows correspond to reusable organism-level traits below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, ScoMcrA, TagI, and VcaM4I article-registry rows "
    "correspond to reusable organism-level traits below this class."
)


def pvurts1i_family_evidence() -> dict[str, str]:
    return {
        "reference": PVURTS1I_2011,
        "snippet": (
            "Using PvuRts1I as the founding member, we define a family of "
            "homologous proteins with similar DNA modification-dependent "
            "recognition properties."
        ),
        "notes": (
            "Wang et al. support PvuRts1I as the founding member of a "
            "family of modification-dependent restriction enzymes."
        ),
    }


def modified_hmc_recognition_evidence() -> dict[str, str]:
    return {
        "reference": PVURTS1I_2011,
        "snippet": (
            "PvuRts1I is a modification-dependent restriction "
            "endonuclease that recognizes 5-hydroxymethylcytosine "
            "(5hmC) as well as 5-glucosylhydroxymethylcytosine (5ghmC) "
            "in double-stranded DNA."
        ),
        "notes": (
            "Wang et al. support PvuRts1I recognition of 5hmC- and "
            "5ghmC-containing double-stranded DNA."
        ),
    }


def double_strand_cleavage_evidence() -> dict[str, str]:
    return {
        "reference": PVURTS1I_2011,
        "snippet": (
            "We show that these enzymes introduce a double-stranded "
            "cleavage at the 3'-side away from the recognized modified "
            "cytosine."
        ),
        "notes": (
            "Wang et al. support PvuRts1I-family enzymes as "
            "modification-dependent restriction endonucleases that cleave "
            "both DNA strands at a defined offset from the modified "
            "cytosine."
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
            "The pinned DefenseFinder article registry maps the PvuRts1I "
            "source key to the Wang et al. PvuRts1I-family paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact PvuRts1I row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact PvuRts1I system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PvuRts1I system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses a PvuRts1I-family locus encoding a "
        "restriction endonuclease that recognizes 5-hydroxymethylcytosine "
        "or 5-glucosylhydroxymethylcytosine in double-stranded DNA and "
        "cleaves both strands on the 3'-side away from the recognized "
        "modified cytosine."
    ),
    "definition_source": PVURTS1I_2011,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "PvuRts1I",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        pvurts1i_family_evidence(),
        modified_hmc_recognition_evidence(),
        double_strand_cleavage_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pvurts1i_restricts_modified_hmc_dna",
            "title": "PvuRts1I restricts modified-HMC DNA",
            "description": (
                "Conservative system-level sketch linking a "
                "PvuRts1I-family locus to modified-hydroxymethylcytosine "
                "DNA restriction and to the Type IV restriction parent "
                "trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PvuRts1I as a named Type IV "
                "modification-dependent restriction family while leaving "
                "natural host breadth, exact target selectivity across "
                "characterized homologs, accession-level protein examples, "
                "and DefenseFinder RM_Type_IV HMM/rules mapping "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pvurts1i_family_locus",
                    "label": "PvuRts1I-family locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a PvuRts1I-family "
                        "modification-dependent restriction endonuclease."
                    ),
                },
                {
                    "node_id": "pvurts1i_modified_hmc_dna",
                    "label": "PvuRts1I-targeted modified-HMC DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "Double-stranded DNA containing 5hmC or 5ghmC in a "
                        "PvuRts1I-family recognition context."
                    ),
                },
                {
                    "node_id": "pvurts1i_modified_hmc_restriction",
                    "label": "PvuRts1I modified-HMC restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of 5hmC- or "
                        "5ghmC-containing DNA by a PvuRts1I-family "
                        "endonuclease."
                    ),
                },
                {
                    "node_id": "pvurts1i_system_trait",
                    "label": "PvuRts1I system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PvuRts1I-family "
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
                    "subject": "pvurts1i_family_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "pvurts1i_modified_hmc_restriction",
                    "description": (
                        "PvuRts1I-family loci encode "
                        "modification-dependent restriction endonucleases."
                    ),
                    "evidence": [
                        pvurts1i_family_evidence(),
                        double_strand_cleavage_evidence(),
                    ],
                },
                {
                    "subject": "pvurts1i_modified_hmc_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "pvurts1i_modified_hmc_dna",
                    "description": (
                        "PvuRts1I-family restriction targets DNA with 5hmC "
                        "or 5ghmC modifications."
                    ),
                    "evidence": [
                        modified_hmc_recognition_evidence(),
                        double_strand_cleavage_evidence(),
                    ],
                },
                {
                    "subject": "pvurts1i_modified_hmc_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "pvurts1i_system_trait",
                    "description": (
                        "PvuRts1I-family modified-HMC restriction realizes "
                        "the organism-level PvuRts1I system possession "
                        "trait."
                    ),
                    "evidence": [
                        modified_hmc_recognition_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "pvurts1i_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "PvuRts1I system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        pvurts1i_family_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pvurts1i-defensefinder-model-gap",
            "prompt": (
                "Resolve PvuRts1I-family breadth, 5hmC and 5ghmC target "
                "selectivity across natural hosts, accession-level protein "
                "examples, and DefenseFinder RM_Type_IV HMM/rules mapping "
                "before minting narrower PvuRts1I mechanism or component "
                "traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wang et al. support PvuRts1I as the founding member of a "
                "family of 5hmC- and 5ghmC-recognizing "
                "modification-dependent restriction endonucleases, and the "
                "pinned DefenseFinder article registry maps PvuRts1I to the "
                "Wang et al. paper. The pinned HMM inventory and rules "
                "table have no exact PvuRts1I rows. This first-pass record "
                "therefore does not resolve a reusable DefenseFinder "
                "profile model, exact accession-level protein examples, "
                "the breadth of PvuRts1I-like systems across natural "
                "hosts, or the complete set of natural 5hmC and 5ghmC "
                "target contexts."
            ),
            "evidence": [
                pvurts1i_family_evidence(),
                modified_hmc_recognition_evidence(),
                double_strand_cleavage_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#pvurts1i_restricts_modified_hmc_dna"
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
            "Documented PvuRts1I as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000511 for the PvuRts1I "
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
            "Minted PvuRts1I system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the type IV "
            "modification-dependent restriction system parent after an "
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
            "Reviewed PvuRts1I system during initial curation and left "
            "canonical_examples empty because Wang et al. support "
            "PvuRts1I and PvuRts1I-family enzymes, but not a single "
            "stable NCBITaxon strain exemplar or accession-level protein "
            "example for the organism-level PvuRts1I system trait. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADVERSARIAL_REVIEW_REPAIR",
        changes=(
            "Addressed PR #1514 adversarial review issue #1515 by "
            "tightening the PvuRts1I system definition to match the "
            "Wang et al. 3'-side cleavage evidence without claiming a "
            "fixed cleavage distance."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
            "PvuRts1I system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
