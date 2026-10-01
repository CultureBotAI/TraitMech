#!/usr/bin/env python3
"""Add the EcoKMcrA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ecokmcra_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

CZAPINSKA = "DOI:10.1093/nar/gky731"
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
TIMESTAMP = "2026-10-01T07:10:00Z"
PARENT_TIMESTAMP = "2026-10-01T07:10:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T07:10:02Z"
IDENTIFIER = "traitmech:000509"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v386"

ARTICLE_ROW = (
    "| EcoKMcrA | 10\\.1093/nar/gky731 | Activity and structure of "
    "EcoKMcrA | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before "
    "minting narrower Type IV custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder "
    "RM_Type_IV custom Type_IV_REases profiles and characterized McrA, "
    "MspJI, PvuRts1I, ScoMcrA, TagI, or VcaM4I families before minting "
    "narrower Type IV custom-profile traits."
)
OLD_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, TagI, and VcaM4I "
    "article-registry rows correspond to reusable organism-level traits "
    "below this class."
)
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM "
    "rows to exact characterized families or resolve whether the "
    "Other_Type_IV, MspJI, PvuRts1I, ScoMcrA, TagI, and VcaM4I "
    "article-registry rows correspond to reusable organism-level traits "
    "below this class."
)


def modified_cytosine_evidence() -> dict[str, str]:
    return {
        "reference": CZAPINSKA,
        "snippet": (
            "Escherichia coli McrA (EcoKMcrA) acts as a methylcytosine "
            "and hydroxymethylcytosine dependent restriction endonuclease."
        ),
        "notes": (
            "Czapinska et al. support EcoKMcrA as an E. coli McrA "
            "modification-dependent restriction endonuclease that targets "
            "methylcytosine- and hydroxymethylcytosine-containing DNA."
        ),
    }


def modified_cytosine_context_evidence() -> dict[str, str]:
    return {
        "reference": CZAPINSKA,
        "snippet": (
            "Electrophoretic mobility shift assay (EMSA) and footprinting "
            "experiments suggest that the N-terminal domains can sense the "
            "presence and sequence context of modified cytosines."
        ),
        "notes": (
            "Czapinska et al. support EcoKMcrA sensing of the presence and "
            "sequence context of modified cytosines."
        ),
    }


def endonuclease_activity_evidence() -> dict[str, str]:
    return {
        "reference": CZAPINSKA,
        "snippet": (
            "We present a biochemical characterization of EcoKMcrA that "
            "includes the first demonstration of its endonuclease activity"
        ),
        "notes": (
            "Czapinska et al. experimentally demonstrated EcoKMcrA "
            "endonuclease activity in vitro."
        ),
    }


def cellular_restriction_evidence() -> dict[str, str]:
    return {
        "reference": CZAPINSKA,
        "snippet": (
            "In cells, EcoKMcrA specifically restricts DNA that is modified "
            "in the correct sequence context. This activity is impaired by "
            "mutations of the nuclease active site, unless the enzyme is "
            "highly overexpressed."
        ),
        "notes": (
            "Czapinska et al. support cellular modified-DNA restriction by "
            "EcoKMcrA and tie efficient restriction to the nuclease active "
            "site."
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
            "The pinned DefenseFinder article registry maps the EcoKMcrA "
            "source key to the Czapinska et al. Activity and structure of "
            "EcoKMcrA paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact EcoKMcrA row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact EcoKMcrA system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "EcoKMcrA system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses an EcoKMcrA mcrA locus encoding a "
        "methylcytosine- and hydroxymethylcytosine-dependent restriction "
        "endonuclease whose nuclease active site is required for efficient "
        "restriction of DNA modified in the correct sequence context."
    ),
    "definition_source": CZAPINSKA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "EcoKMcrA",
            "synonym_type": "RELATED_SYNONYM",
            "source": CZAPINSKA,
        }
    ],
    "evidence": [
        modified_cytosine_evidence(),
        endonuclease_activity_evidence(),
        cellular_restriction_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ecokmcra_restricts_modified_cytosine_dna",
            "title": "EcoKMcrA restricts modified-cytosine DNA",
            "description": (
                "Conservative system-level sketch linking an EcoKMcrA "
                "mcrA locus to modified-cytosine DNA restriction and to "
                "the Type IV restriction parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures EcoKMcrA as a named E. coli K-strain "
                "McrA Type IV modification-dependent restriction system "
                "while leaving EcoKMcrA-family breadth, sequence-context "
                "specificity across natural hosts, accession-level protein "
                "examples, and DefenseFinder RM_Type_IV HMM/rules mapping "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "ecokmcra_locus",
                    "label": "EcoKMcrA mcrA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding an EcoKMcrA "
                        "methylcytosine- and hydroxymethylcytosine-dependent "
                        "restriction endonuclease."
                    ),
                },
                {
                    "node_id": "modified_cytosine_dna",
                    "label": "modified-cytosine DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing methylcytosine or "
                        "hydroxymethylcytosine in a sequence context "
                        "recognized by EcoKMcrA."
                    ),
                },
                {
                    "node_id": "ecokmcra_modified_dna_restriction",
                    "label": "EcoKMcrA modified-DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Nuclease-active-site-dependent restriction of "
                        "modified DNA by EcoKMcrA."
                    ),
                },
                {
                    "node_id": "ecokmcra_system_trait",
                    "label": "EcoKMcrA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded EcoKMcrA "
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
                    "subject": "ecokmcra_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "ecokmcra_modified_dna_restriction",
                    "description": (
                        "The EcoKMcrA mcrA locus encodes a "
                        "modified-cytosine-dependent restriction "
                        "endonuclease."
                    ),
                    "evidence": [
                        modified_cytosine_evidence(),
                        endonuclease_activity_evidence(),
                    ],
                },
                {
                    "subject": "ecokmcra_modified_dna_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "modified_cytosine_dna",
                    "description": (
                        "EcoKMcrA-dependent Type IV restriction targets "
                        "DNA modified in the correct sequence context."
                    ),
                    "evidence": [
                        modified_cytosine_context_evidence(),
                        cellular_restriction_evidence(),
                    ],
                },
                {
                    "subject": "ecokmcra_modified_dna_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ecokmcra_system_trait",
                    "description": (
                        "EcoKMcrA-dependent Type IV restriction realizes "
                        "the organism-level EcoKMcrA system possession "
                        "trait."
                    ),
                    "evidence": [
                        cellular_restriction_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "ecokmcra_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "EcoKMcrA system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        modified_cytosine_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ecokmcra-defensefinder-model-gap",
            "prompt": (
                "Resolve EcoKMcrA-family breadth, methylcytosine and "
                "hydroxymethylcytosine sequence-context specificity across "
                "natural hosts, accession-level protein examples, and "
                "DefenseFinder RM_Type_IV HMM/rules mapping before minting "
                "narrower EcoKMcrA mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Czapinska et al. support E. coli EcoKMcrA as a "
                "methylcytosine- and hydroxymethylcytosine-dependent "
                "restriction endonuclease with cellular modified-DNA "
                "restriction activity tied to the nuclease active site, and "
                "the pinned DefenseFinder article registry maps EcoKMcrA to "
                "that paper. The pinned HMM inventory and rules table have "
                "no exact EcoKMcrA rows. This first-pass record therefore "
                "does not resolve a reusable DefenseFinder profile model, "
                "exact accession-level protein examples, the breadth of "
                "EcoKMcrA-like systems beyond E. coli K strains, or the "
                "complete set of natural methylcytosine and "
                "hydroxymethylcytosine sequence contexts."
            ),
            "evidence": [
                modified_cytosine_evidence(),
                cellular_restriction_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#ecokmcra_restricts_modified_cytosine_dna"
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
            "Documented EcoKMcrA as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000509 for the EcoKMcrA "
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
            "Minted EcoKMcrA system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the type IV "
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
            "Reviewed EcoKMcrA system during initial curation and left "
            "canonical_examples empty because Czapinska et al. support the "
            "E. coli K-strain EcoKMcrA enzyme and the DefenseFinder "
            "EcoKMcrA source key, but not a single stable NCBITaxon strain "
            "exemplar or accession-level protein example for the "
            "organism-level EcoKMcrA system trait. No paid research was "
            "used."
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
            "EcoKMcrA system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
