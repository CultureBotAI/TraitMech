#!/usr/bin/env python3
"""Add the GmrSD system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gmrsd_system.yaml"
TYPE_IV_PARENT = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

BAIR = "DOI:10.1016/j.jmb.2006.11.051"
MACHNICKA = "DOI:10.1186/s12859-015-0773-z"
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
TIMESTAMP = "2026-10-01T04:21:00Z"
PARENT_TIMESTAMP = "2026-10-01T04:21:01Z"
CANONICAL_TIMESTAMP = "2026-10-01T04:21:02Z"
IDENTIFIER = "traitmech:000506"
TYPE_IV_PARENT_ID = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v383"

ARTICLE_ROW = (
    "| GmrSD_RM_Type_IV | 10\\.1016/j\\.jmb\\.2006\\.11\\.051 | A "
    "type IV modification dependent restriction nuclease that targets "
    "glucosylated hydroxymethyl cytosine modified DNAs | "
)
OLD_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder RM_Type_IV "
    "custom Type_IV_REases profiles and characterized McrA, GmrSD, MspJI, "
    "PvuRts1I, EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before minting "
    "narrower Type IV custom-profile traits."
)
NEW_PARENT_PROMPT = (
    "Resolve the accession-level relationships between DefenseFinder RM_Type_IV "
    "custom Type_IV_REases profiles and characterized McrA, MspJI, PvuRts1I, "
    "EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before minting narrower Type "
    "IV custom-profile traits."
)
OLD_PARENT_RATIONALE = (
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
NEW_PARENT_RATIONALE = (
    "Loenen and Raleigh support the broad Type IV modification-dependent "
    "restriction class, and the pinned DefenseFinder registries support an "
    "RM_Type_IV namespace with a broad Type_IV_REases custom profile group. "
    "The evidence does not yet map any of the eight pinned RM_Type_IV HMM rows "
    "to exact characterized families or resolve whether the Other_Type_IV, "
    "MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, TagI, and VcaM4I article-registry "
    "rows correspond to reusable organism-level traits below this class."
)


def gmrsd_target_evidence() -> dict[str, str]:
    return {
        "reference": BAIR,
        "snippet": (
            "The Escherichia coli CT596 prophage exclusion genes gmrS and "
            "gmrD were found to encode a novel type IV modification-dependent "
            "restriction nuclease that targets and digests glucosylated "
            "(glc)-hydroxymethylcytosine (HMC) DNAs."
        ),
        "notes": (
            "Bair and Black experimentally support split gmrS and gmrD genes "
            "as a GmrSD Type IV modification-dependent restriction nuclease "
            "targeting glucosylated hydroxymethylcytosine DNA."
        ),
    }


def gmrsd_component_evidence() -> dict[str, str]:
    return {
        "reference": BAIR,
        "snippet": (
            "Nuclease activity is dependent upon the presence of both the "
            "GmrS and the GmrD proteins."
        ),
        "notes": (
            "Bair and Black support both split GmrS and GmrD proteins as "
            "required for the characterized CT596 GmrSD restriction activity."
        ),
    }


def gmrsd_architecture_evidence() -> dict[str, str]:
    return {
        "reference": MACHNICKA,
        "snippet": (
            "GmrSD is a modification-dependent restriction endonuclease that "
            "specifically targets and cleaves glucosylated "
            "hydroxymethylcytosine (glc-HMC) modified DNA."
        ),
        "notes": (
            "Machnicka et al. support GmrSD as a "
            "glucosylated-hydroxymethylcytosine-targeting "
            "modification-dependent restriction endonuclease."
        ),
    }


def gmrsd_fusion_evidence() -> dict[str, str]:
    return {
        "reference": MACHNICKA,
        "snippet": (
            "It is encoded either as two separate single-domain GmrS and GmrD "
            "proteins or as a single protein carrying both domains."
        ),
        "notes": (
            "Machnicka et al. support treating split GmrS/GmrD loci and fused "
            "double-domain GmrSD homologs within the same first-pass system "
            "family."
        ),
    }


def gmrsd_fused_prevalence_evidence() -> dict[str, str]:
    return {
        "reference": MACHNICKA,
        "snippet": (
            "Moreover, we found that GmrSD systems exist predominantly as a "
            "fused, double-domain form rather than as a heterodimer and that "
            "their homologs are often encoded in regions enriched in defense "
            "and gene mobility-related elements."
        ),
        "notes": (
            "Machnicka et al. report that fused double-domain GmrSD systems "
            "are common and are often found near defense- and mobility-linked "
            "features."
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
            "The pinned DefenseFinder article registry maps the "
            "GmrSD_RM_Type_IV source key to Bair and Black."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact GmrSD or GmrSD_RM_Type_IV row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder rules "
            "table found no exact GmrSD or GmrSD_RM_Type_IV system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GmrSD system",
    "definition": (
        "A type IV modification-dependent restriction system in which an "
        "organism possesses a GmrSD locus encoding either separate GmrS and "
        "GmrD proteins or a fused double-domain GmrSD-family protein, "
        "that targets glucosylated hydroxymethylcytosine-containing DNA."
    ),
    "definition_source": BAIR,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [TYPE_IV_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "GmrSD",
            "synonym_type": "EXACT_SYNONYM",
            "source": BAIR,
        },
        {
            "synonym_text": "GmrSD_RM_Type_IV",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        gmrsd_target_evidence(),
        gmrsd_component_evidence(),
        gmrsd_architecture_evidence(),
        gmrsd_fusion_evidence(),
        gmrsd_fused_prevalence_evidence(),
        type_iv_class_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gmrsd_restricts_glucosylated_hmc_dna",
            "title": "GmrSD restricts glucosylated HMC DNA",
            "description": (
                "Conservative system-level sketch linking a GmrSD locus to "
                "modification-dependent restriction of glucosylated "
                "hydroxymethylcytosine DNA and to the Type IV restriction "
                "parent trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GmrSD as a named Type IV "
                "modification-dependent restriction system while leaving "
                "GmrS/GmrD domain activities, complete sugar-HMC substrate "
                "breadth, split-versus-fused host breadth, IPI inhibition, "
                "and DefenseFinder RM_Type_IV HMM/rules mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gmrsd_locus",
                    "label": "GmrSD locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding split GmrS and GmrD proteins or a "
                        "fused double-domain GmrSD-family protein."
                    ),
                },
                {
                    "node_id": "glucosylated_hmc_dna",
                    "label": "glucosylated HMC DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "DNA containing glucosylated hydroxymethylcytosine base modifications."
                    ),
                },
                {
                    "node_id": "gmrsd_dependent_type_iv_restriction",
                    "label": "GmrSD-dependent Type IV restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "glucosylated-hydroxymethylcytosine DNA by GmrSD."
                    ),
                },
                {
                    "node_id": "gmrsd_system_trait",
                    "label": "GmrSD system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GmrSD "
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
                    "subject": "gmrsd_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "gmrsd_dependent_type_iv_restriction",
                    "description": (
                        "The GmrSD locus encodes the proteins that cleave "
                        "glucosylated hydroxymethylcytosine DNA."
                    ),
                    "evidence": [
                        gmrsd_component_evidence(),
                        gmrsd_fusion_evidence(),
                    ],
                },
                {
                    "subject": "gmrsd_dependent_type_iv_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "glucosylated_hmc_dna",
                    "description": (
                        "GmrSD-dependent Type IV restriction targets "
                        "glucosylated hydroxymethylcytosine DNA."
                    ),
                    "evidence": [
                        gmrsd_target_evidence(),
                        gmrsd_architecture_evidence(),
                    ],
                },
                {
                    "subject": "gmrsd_dependent_type_iv_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "gmrsd_system_trait",
                    "description": (
                        "GmrSD-dependent Type IV restriction realizes the "
                        "organism-level GmrSD system possession trait."
                    ),
                    "evidence": [
                        gmrsd_architecture_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "gmrsd_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "type_iv_modification_dependent_restriction",
                    "description": (
                        "GmrSD system possession is a Type IV "
                        "modification-dependent restriction system trait."
                    ),
                    "evidence": [
                        gmrsd_target_evidence(),
                        type_iv_class_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gmrsd-defensefinder-model-gap",
            "prompt": (
                "Resolve exact GmrS/GmrD domain activities, complete "
                "sugar-modified HMC substrate breadth, split-versus-fused "
                "host breadth, phage IPI inhibition, and DefenseFinder "
                "RM_Type_IV HMM/rules mapping before minting narrower GmrSD "
                "mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bair and Black support split GmrS/GmrD as a Type IV "
                "modification-dependent restriction nuclease that targets "
                "glucosylated hydroxymethylcytosine DNA, Machnicka et al. "
                "support GmrSD homologs as either split or fused "
                "double-domain systems, and the pinned DefenseFinder article "
                "registry maps GmrSD_RM_Type_IV to Bair and Black. The "
                "pinned HMM inventory and rules table have no exact GmrSD "
                "or GmrSD_RM_Type_IV rows. This first-pass record therefore "
                "does not resolve a reusable DefenseFinder profile model, "
                "exact split-versus-fused prevalence across natural hosts, "
                "the complete set of sugar-modified HMC targets, the exact "
                "domain contributions of GmrS and GmrD, or the relationship "
                "between phage IPI inhibition and the organism-level GmrSD "
                "system trait."
            ),
            "evidence": [
                gmrsd_target_evidence(),
                gmrsd_component_evidence(),
                gmrsd_architecture_evidence(),
                gmrsd_fusion_evidence(),
                gmrsd_fused_prevalence_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#gmrsd_restricts_glucosylated_hmc_dna"],
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
            "Documented GmrSD as split out in the open Type IV "
            "modification-dependent restriction profile-interpretation "
            "discussion after minting traitmech:000506 for the GmrSD "
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
            "Minted GmrSD system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the type IV modification-dependent "
            "restriction system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed GmrSD system during initial curation and left "
            "canonical_examples empty because the Bair and Black and "
            "Machnicka et al. sources support the split CT596 GmrSD enzyme "
            "and broader split-or-fused GmrSD family, but not a single "
            "stable NCBITaxon strain exemplar for the organism-level GmrSD "
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
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, TYPE_IV_PARENT)
    else:
        print(
            "GmrSD system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{TYPE_IV_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
