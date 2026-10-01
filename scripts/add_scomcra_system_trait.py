#!/usr/bin/env python3
"""Add the ScoMcrA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "scomcra_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

SCOMCRA_2010 = "DOI:10.1371/journal.pgen.1001253"
SCOMCRA_2018 = "DOI:10.1038/s41467-018-07093-1"
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
TIMESTAMP = "2026-10-01T10:14:00Z"
PARENT_TIMESTAMP = "2026-10-01T10:14:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T10:14:02Z"
IDENTIFIER = "traitmech:000512"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v389"

ARTICLE_ROW = (
    "| ScoMcrA | 10\\.1038/s41467-018-07093-1 | Structural basis for "
    "the recognition of sulfur in phosphorothioated DNA | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "ScoMcrA, TagI, or VcaM4I families before minting narrower Type IV "
    "custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "TagI, or VcaM4I families before minting narrower Type IV "
    "custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, ScoMcrA, TagI, and VcaM4I article-registry rows "
    "correspond to reusable organism-level traits below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, TagI, and VcaM4I article-registry rows correspond to "
    "reusable organism-level traits below this class."
)


def scomcra_cleavage_evidence() -> dict[str, str]:
    return {
        "reference": SCOMCRA_2010,
        "snippet": (
            "A His-tagged derivative of ScoA3McrA cleaved S-modified DNA "
            "and also Dcm-methylated DNA in vitro near the respective "
            "modification sites."
        ),
        "notes": (
            "Liu et al. support ScoA3McrA cleavage of phosphorothioated "
            "DNA and Dcm-methylated DNA."
        ),
    }


def scomcra_double_strand_evidence() -> dict[str, str]:
    return {
        "reference": SCOMCRA_2010,
        "snippet": (
            "Double-strand cleavage occurred 16-28 nucleotides away from "
            "the phosphorothioate links."
        ),
        "notes": (
            "Liu et al. support double-strand ScoA3McrA cleavage near "
            "DNA phosphorothioate linkages."
        ),
    }


def scomcra_first_pt_cleavage_evidence() -> dict[str, str]:
    return {
        "reference": SCOMCRA_2010,
        "snippet": (
            "This is the first report of in vitro endonuclease activity "
            "of a McrA homologue and also the first demonstration of an "
            "enzyme that specifically cleaves S-modified DNA."
        ),
        "notes": (
            "Liu et al. frame ScoA3McrA as a McrA homolog with "
            "phosphorothioated-DNA-specific cleavage activity."
        ),
    }


def sbd_structure_evidence() -> dict[str, str]:
    return {
        "reference": SCOMCRA_2018,
        "snippet": (
            "Here we present the crystal structure of the sulfur-binding "
            "domain (SBD) from the DNA phosphorothioation "
            "(PT)-dependent restriction endonuclease ScoMcrA."
        ),
        "notes": (
            "Liu et al. support ScoMcrA as a phosphorothioated-DNA-"
            "dependent restriction endonuclease with a sulfur-binding "
            "domain."
        ),
    }


def sbd_family_evidence() -> dict[str, str]:
    return {
        "reference": SCOMCRA_2018,
        "snippet": (
            "We show that three of these homologs bind PT-DNA in vitro "
            "and restrict PT-DNA gene transfer in vivo."
        ),
        "notes": (
            "Liu et al. support SBD homologs as phosphorothioated-DNA "
            "readers with in vivo PT-DNA restriction activity."
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
            "The pinned DefenseFinder article registry maps the ScoMcrA "
            "source key to the Liu et al. sulfur-recognition paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact ScoMcrA row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact ScoMcrA system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ScoMcrA system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses a ScoMcrA-family locus encoding a "
        "sulfur-binding-domain phosphorothioated-DNA restriction "
        "endonuclease."
    ),
    "definition_source": SCOMCRA_2018,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "ScoMcrA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        scomcra_cleavage_evidence(),
        scomcra_double_strand_evidence(),
        scomcra_first_pt_cleavage_evidence(),
        sbd_structure_evidence(),
        sbd_family_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "scomcra_restricts_phosphorothioated_dna",
            "title": "ScoMcrA restricts phosphorothioated DNA",
            "description": (
                "Conservative system-level sketch linking a "
                "ScoMcrA-family locus to phosphorothioated-DNA "
                "restriction and to the Type IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ScoMcrA as a named Type IV "
                "modification-dependent restriction family while leaving "
                "natural host breadth, exact PT-DNA sequence-context "
                "specificity across characterized homologs, Dcm-methylated "
                "DNA target breadth, accession-level protein examples, and "
                "DefenseFinder RM_Type_IV HMM/rules mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "scomcra_family_locus",
                    "label": "ScoMcrA-family locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a ScoMcrA-family "
                        "phosphorothioated-DNA restriction endonuclease."
                    ),
                },
                {
                    "node_id": "scomcra_phosphorothioated_dna",
                    "label": "ScoMcrA-targeted phosphorothioated DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing phosphorothioate linkages in a "
                        "ScoMcrA-family recognition context."
                    ),
                },
                {
                    "node_id": "scomcra_phosphorothioated_dna_restriction",
                    "label": "ScoMcrA phosphorothioated-DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "phosphorothioated DNA by a ScoMcrA-family "
                        "endonuclease."
                    ),
                },
                {
                    "node_id": "scomcra_system_trait",
                    "label": "ScoMcrA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded ScoMcrA-family "
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
                    "subject": "scomcra_family_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "scomcra_phosphorothioated_dna_restriction",
                    "description": (
                        "ScoMcrA-family loci encode PT-DNA readers that "
                        "restrict phosphorothioated DNA."
                    ),
                    "evidence": [
                        scomcra_cleavage_evidence(),
                        sbd_structure_evidence(),
                        sbd_family_evidence(),
                    ],
                },
                {
                    "subject": "scomcra_phosphorothioated_dna_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "scomcra_phosphorothioated_dna",
                    "description": (
                        "ScoMcrA-family restriction targets "
                        "phosphorothioated DNA."
                    ),
                    "evidence": [
                        scomcra_cleavage_evidence(),
                        scomcra_double_strand_evidence(),
                        sbd_family_evidence(),
                    ],
                },
                {
                    "subject": "scomcra_phosphorothioated_dna_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "scomcra_system_trait",
                    "description": (
                        "ScoMcrA-family phosphorothioated-DNA restriction "
                        "realizes the organism-level ScoMcrA system "
                        "possession trait."
                    ),
                    "evidence": [
                        scomcra_first_pt_cleavage_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "scomcra_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "ScoMcrA system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        scomcra_first_pt_cleavage_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "scomcra-defensefinder-model-gap",
            "prompt": (
                "Resolve ScoMcrA-family breadth, phosphorothioated-DNA "
                "sequence-context specificity across natural hosts, "
                "methylated-DNA target breadth, accession-level protein "
                "examples, and DefenseFinder RM_Type_IV HMM/rules mapping "
                "before minting narrower ScoMcrA mechanism or component "
                "traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Liu et al. support ScoA3McrA as a Type IV McrA homolog "
                "that cleaves S-modified DNA in vitro and support ScoMcrA "
                "as a PT-dependent endonuclease with a sulfur-binding "
                "domain. The pinned DefenseFinder article registry maps "
                "ScoMcrA to the sulfur-recognition paper, but the pinned "
                "HMM inventory and rules table have no exact ScoMcrA rows. "
                "This first-pass record therefore does not resolve a "
                "reusable DefenseFinder profile model, exact "
                "accession-level protein examples, the breadth of "
                "ScoMcrA-like systems across natural hosts, the complete "
                "set of natural phosphorothioated-DNA contexts, or the "
                "breadth of methylated-DNA target contexts."
            ),
            "evidence": [
                scomcra_cleavage_evidence(),
                scomcra_double_strand_evidence(),
                scomcra_first_pt_cleavage_evidence(),
                sbd_structure_evidence(),
                sbd_family_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#scomcra_restricts_phosphorothioated_dna"
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
            "Documented ScoMcrA as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000512 for the ScoMcrA "
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
            "Minted ScoMcrA system as a DOI- and DefenseFinder-backed "
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
            "Reviewed ScoMcrA system during initial curation and left "
            "canonical_examples empty because Liu et al. support "
            "ScoA3McrA and sulfur-binding-domain homologs, but not a "
            "single stable NCBITaxon strain exemplar or accession-level "
            "protein example for the organism-level ScoMcrA system trait. "
            "No paid research was used."
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
            assert existing["label"] == "ScoMcrA system"
            assert existing["mapping_status"] == "PROPOSED"
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "ScoMcrA system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
