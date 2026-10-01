#!/usr/bin/env python3
"""Add the MspJI system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mspji_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

MSPJI_2011 = "DOI:10.1073/pnas.1018448108"
MSPJI_2010 = "DOI:10.1093/nar/gkq327"
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
TIMESTAMP = "2026-10-01T08:04:00Z"
PARENT_TIMESTAMP = "2026-10-01T08:04:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T08:04:02Z"
IDENTIFIER = "traitmech:000510"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v387"

ARTICLE_ROW = (
    "| MspJI | 10\\.1073/pnas\\.1018448108 | The MspJI family of "
    "modification-dependent restriction endonucleases for epigenetic "
    "studies | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "MspJI, PvuRts1I, ScoMcrA, TagI, or VcaM4I families before minting "
    "narrower Type IV custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "PvuRts1I, ScoMcrA, TagI, or VcaM4I families before minting narrower "
    "Type IV custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, MspJI, PvuRts1I, ScoMcrA, TagI, and VcaM4I "
    "article-registry rows correspond to reusable organism-level traits "
    "below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, PvuRts1I, ScoMcrA, TagI, and VcaM4I article-registry "
    "rows correspond to reusable organism-level traits below this class."
)


def mspji_family_evidence() -> dict[str, str]:
    return {
        "reference": MSPJI_2011,
        "snippet": (
            "MspJI is a novel modification-dependent restriction "
            "endonuclease that cleaves at a fixed distance away from the "
            "modification site."
        ),
        "notes": (
            "Cohen-Karni et al. support MspJI as a "
            "modification-dependent restriction endonuclease with "
            "distance-defined cleavage relative to its modified target."
        ),
    }


def family_modified_cytosine_evidence() -> dict[str, str]:
    return {
        "reference": MSPJI_2011,
        "snippet": (
            "All of the enzymes specifically recognize cytosine C5 "
            "modification (methylation or hydroxymethylation) in DNA and "
            "cleave at a constant distance (N(12)/N(16)) away from the "
            "modified cytosine."
        ),
        "notes": (
            "Cohen-Karni et al. biochemically characterized MspJI homologs "
            "and support the MspJI family as C5-modified-cytosine-dependent "
            "restriction endonucleases."
        ),
    }


def mspji_hydroxymethylcytosine_evidence() -> dict[str, str]:
    return {
        "reference": MSPJI_2010,
        "snippet": (
            "Besides 5-methylcytosine, MspJI also recognizes "
            "5-hydroxymethylcytosine but is blocked by "
            "5-glucosylhydroxymethylcytosine."
        ),
        "notes": (
            "Zheng et al. support MspJI restriction of both methylcytosine- "
            "and hydroxymethylcytosine-containing DNA while leaving "
            "glucosylated hydroxymethylcytosine DNA uncleaved."
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
            "The pinned DefenseFinder article registry maps the MspJI "
            "source key to the Cohen-Karni et al. MspJI-family paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact MspJI row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact MspJI system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "MspJI system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses an MspJI-family Mrr-like locus encoding a "
        "restriction endonuclease that recognizes methylcytosine- or "
        "hydroxymethylcytosine-modified DNA and cleaves both strands at a "
        "fixed distance from the modified cytosine."
    ),
    "definition_source": MSPJI_2011,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "MspJI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        mspji_family_evidence(),
        family_modified_cytosine_evidence(),
        mspji_hydroxymethylcytosine_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "mspji_restricts_modified_cytosine_dna",
            "title": "MspJI restricts modified-cytosine DNA",
            "description": (
                "Conservative system-level sketch linking an MspJI-family "
                "locus to modified-cytosine DNA restriction and to the Type "
                "IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures MspJI as a named Mrr-like Type IV "
                "modification-dependent restriction family while leaving "
                "natural host breadth, exact sequence-context specificity "
                "across characterized homologs, accession-level protein "
                "examples, and DefenseFinder RM_Type_IV HMM/rules mapping "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "mspji_family_locus",
                    "label": "MspJI-family locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding an MspJI-family "
                        "modification-dependent restriction endonuclease."
                    ),
                },
                {
                    "node_id": "mspji_modified_cytosine_dna",
                    "label": "MspJI-targeted modified-cytosine DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing methylcytosine or "
                        "hydroxymethylcytosine in an MspJI-family "
                        "sequence context."
                    ),
                },
                {
                    "node_id": "mspji_modified_cytosine_restriction",
                    "label": "MspJI modified-cytosine restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "C5-modified-cytosine DNA by an MspJI-family "
                        "endonuclease."
                    ),
                },
                {
                    "node_id": "mspji_system_trait",
                    "label": "MspJI system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MspJI-family "
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
                    "subject": "mspji_family_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "mspji_modified_cytosine_restriction",
                    "description": (
                        "MspJI-family loci encode Mrr-like "
                        "modification-dependent restriction endonucleases."
                    ),
                    "evidence": [
                        mspji_family_evidence(),
                        family_modified_cytosine_evidence(),
                    ],
                },
                {
                    "subject": "mspji_modified_cytosine_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "mspji_modified_cytosine_dna",
                    "description": (
                        "MspJI-family restriction targets methylcytosine- "
                        "or hydroxymethylcytosine-containing DNA."
                    ),
                    "evidence": [
                        family_modified_cytosine_evidence(),
                        mspji_hydroxymethylcytosine_evidence(),
                    ],
                },
                {
                    "subject": "mspji_modified_cytosine_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "mspji_system_trait",
                    "description": (
                        "MspJI-family modified-cytosine restriction "
                        "realizes the organism-level MspJI system "
                        "possession trait."
                    ),
                    "evidence": [
                        mspji_hydroxymethylcytosine_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "mspji_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "MspJI system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        mspji_family_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mspji-defensefinder-model-gap",
            "prompt": (
                "Resolve MspJI-family breadth, methylcytosine and "
                "hydroxymethylcytosine sequence-context specificity across "
                "natural hosts, accession-level protein examples, and "
                "DefenseFinder RM_Type_IV HMM/rules mapping before minting "
                "narrower MspJI mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Zheng et al. support MspJI as a methylcytosine- and "
                "hydroxymethylcytosine-dependent restriction endonuclease, "
                "Cohen-Karni et al. support MspJI homologs as a family of "
                "C5-modified-cytosine-dependent restriction endonucleases, "
                "and the pinned DefenseFinder article registry maps MspJI "
                "to the Cohen-Karni et al. paper. The pinned HMM inventory "
                "and rules table have no exact MspJI rows. This first-pass "
                "record therefore does not resolve a reusable "
                "DefenseFinder profile model, exact accession-level "
                "protein examples, the breadth of MspJI-like systems "
                "across natural hosts, or the complete set of natural "
                "methylcytosine and hydroxymethylcytosine sequence "
                "contexts."
            ),
            "evidence": [
                mspji_family_evidence(),
                family_modified_cytosine_evidence(),
                mspji_hydroxymethylcytosine_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#mspji_restricts_modified_cytosine_dna"
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
            "Documented MspJI as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000510 for the MspJI "
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
            "Minted MspJI system as a DOI- and DefenseFinder-backed "
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
            "Reviewed MspJI system during initial curation and left "
            "canonical_examples empty because Zheng et al. and Cohen-Karni "
            "et al. support MspJI and MspJI-family enzymes, but not a "
            "single stable NCBITaxon strain exemplar or accession-level "
            "protein example for the organism-level MspJI system trait. "
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
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "MspJI system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
