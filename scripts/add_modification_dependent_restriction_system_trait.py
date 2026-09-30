#!/usr/bin/env python3
"""Add the type IV modification-dependent restriction system genomics trait."""

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
    / "type_iv_modification_dependent_restriction_system.yaml"
)

LOENEN = "DOI:10.1093/nar/gkt747"
BAIR = "DOI:10.1016/j.jmb.2006.11.051"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T16:21:47Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T16:21:48Z"
POSED_DATE = "2026-09-30"
IDENTIFIER = "traitmech:000496"
PROPOSAL = "proposals/metpo_traitmech_v373"
SLUG = "type_iv_modification_dependent_restriction"

TYPE_IV_CLASS_SNIPPET = (
    "The new class of modification-dependent restriction enzymes was named "
    "Type IV, as distinct from the familiar modification-blocked Types I–III."
)
TYPE_IV_MODIFIED_DNA_SNIPPET = (
    "Type IV enzymes recognize modified DNA with low sequence selectivity and "
    "have emerged many times independently during evolution."
)
TYPE_IV_MODIFICATION_PRESENT_SNIPPET = (
    "there are enzymes that attack DNA only when the modification is present"
)
GMRSD_TARGET_SNIPPET = (
    "The Escherichia coli CT596 prophage exclusion genes gmrS and gmrD were "
    "found to encode a novel type IV modification-dependent restriction "
    "nuclease that targets and digests glucosylated "
    "(glc)-hydroxymethylcytosine (HMC) DNAs."
)
GMRSD_ACTIVITY_SNIPPET = (
    "Overall activities of the purified GmrSD enzyme are in good agreement "
    "with the properties of the cloned gmr genes in vivo and suggest a "
    "restriction enzyme specific for sugar modified HMC DNAs."
)
ARTICLE_REGISTRY_SNIPPET = (
    "| Other_Type_IV | 10\\.1093/nar/gkac975 | REBASE: a database for DNA "
    "restriction and modification: enzymes, genes and genomes | "
)
RULES_SNIPPET = (
    "RM\tRM_Type_IV\t1\t1\tRM_Type_IV__Type_IV_REases\t\t\t"
)
HMM_PROFILES = (
    ("RM_Type_IV__FAM_0", "100"),
    ("RM_Type_IV__FAM_1", "100"),
    ("RM_Type_IV__FAM_2", "100"),
    ("RM_Type_IV__Type_IV_01", "100"),
    ("RM_Type_IV__Type_IV_03", "60"),
    ("RM_Type_IV__Type_IV_05", "70"),
    ("RM_Type_IV__Type_IV_21", "175"),
    ("RM_Type_IV__Type_IV_22", "150"),
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {'':<49}| {'RM_Type_IV':<23}| "
    f"{'Custom':<24}| {score:<7}|"
    for profile, score in HMM_PROFILES
)


def type_iv_class_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": TYPE_IV_CLASS_SNIPPET,
        "notes": (
            "Loenen and Raleigh define Type IV as "
            "modification-dependent restriction, distinct from "
            "modification-blocked Types I-III."
        ),
    }


def type_iv_modified_dna_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": TYPE_IV_MODIFIED_DNA_SNIPPET,
        "notes": (
            "Loenen and Raleigh support the broad Type IV class as enzymes "
            "that recognize modified DNA with limited sequence specificity."
        ),
    }


def type_iv_modification_present_evidence() -> dict[str, str]:
    return {
        "reference": LOENEN,
        "snippet": TYPE_IV_MODIFICATION_PRESENT_SNIPPET,
        "notes": (
            "Loenen and Raleigh contrast modification-dependent restriction "
            "with protective modification by describing enzymes that attack "
            "DNA only when a modification is present."
        ),
    }


def gmrsd_target_evidence() -> dict[str, str]:
    return {
        "reference": BAIR,
        "snippet": GMRSD_TARGET_SNIPPET,
        "notes": (
            "Bair and Black experimentally support GmrSD as a Type IV "
            "modification-dependent restriction nuclease targeting "
            "glucosylated hydroxymethylcytosine DNA."
        ),
    }


def gmrsd_activity_evidence() -> dict[str, str]:
    return {
        "reference": BAIR,
        "snippet": GMRSD_ACTIVITY_SNIPPET,
        "notes": (
            "Bair and Black verify purified GmrSD restriction activity "
            "against sugar-modified hydroxymethylcytosine DNA, one concrete "
            "activity within the Type IV branch."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the Other_Type_IV "
            "source key to the REBASE update, while RM_Type_IV itself is "
            "represented in the pinned rule and HMM registries."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The pinned DefenseFinder rules table models RM_Type_IV as an RM "
            "subsystem requiring the Type_IV_REases profile group."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory lists eight custom HMM "
            "rows under the RM_Type_IV system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "type IV modification-dependent restriction system",
    "definition": (
        "A phage defense system in which an organism possesses a Type IV "
        "modification-dependent restriction locus, including DefenseFinder "
        "RM_Type_IV loci, whose restriction-enzyme activity cleaves foreign "
        "DNA carrying recognized base or backbone modifications rather than "
        "the unmodified targets of canonical Type I-III "
        "restriction-modification systems."
    ),
    "definition_source": LOENEN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "RM_Type_IV",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "RM_Type_IV__Type_IV_REases",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Other_Type_IV",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        type_iv_class_evidence(),
        type_iv_modified_dna_evidence(),
        type_iv_modification_present_evidence(),
        gmrsd_target_evidence(),
        gmrsd_activity_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "type_iv_modification_dependent_restriction",
            "title": "Type IV restriction loci attack modified foreign DNA",
            "description": (
                "Conservative system-level sketch linking Type IV "
                "modification-dependent restriction loci to the broad "
                "phage-defense parent without resolving individual enzyme "
                "families or DefenseFinder profile rows."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the broad Type IV "
                "modification-dependent restriction class and the "
                "DefenseFinder RM_Type_IV custom-profile namespace without "
                "asserting accession-level mappings between HMM rows and "
                "McrA, McrBC, GmrSD, MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, "
                "TagI, or VcaM4I subfamilies."
            ),
            "nodes": [
                {
                    "node_id": "type_iv_rease_locus",
                    "label": "type IV restriction-enzyme locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding one or more Type IV "
                        "modification-dependent restriction enzymes."
                    ),
                },
                {
                    "node_id": "modified_foreign_dna",
                    "label": "modified foreign DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "Incoming bacteriophage or other foreign DNA bearing "
                        "modified bases or phosphorothioated backbone "
                        "positions."
                    ),
                },
                {
                    "node_id": "modification_dependent_restriction",
                    "label": "modification-dependent DNA restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction activity that cleaves DNA only when "
                        "the target DNA carries a recognized modification."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "type IV modification-dependent restriction system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Type IV "
                        "modification-dependent restriction system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "type_iv_rease_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "modification_dependent_restriction",
                    "description": (
                        "Type IV restriction loci encode restriction enzymes "
                        "that recognize and cleave modified DNA."
                    ),
                    "evidence": [
                        type_iv_modified_dna_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "modification_dependent_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "modified_foreign_dna",
                    "description": (
                        "Modification-dependent restriction attacks DNA only "
                        "when a recognized DNA modification is present."
                    ),
                    "evidence": [
                        type_iv_modification_present_evidence(),
                        type_iv_modified_dna_evidence(),
                        gmrsd_target_evidence(),
                    ],
                },
                {
                    "subject": "modification_dependent_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Type IV modification-dependent restriction realizes "
                        "the organism-level Type IV system-possession trait."
                    ),
                    "evidence": [
                        gmrsd_activity_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Type IV modification-dependent restriction system "
                        "possession is curated as a genome-encoded "
                        "phage-defense trait."
                    ),
                    "evidence": [
                        type_iv_modification_present_evidence(),
                        gmrsd_target_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "type-iv-rm-profile-interpretation-gap",
            "prompt": (
                "Resolve the accession-level relationships between "
                "DefenseFinder RM_Type_IV custom Type_IV_REases profiles "
                "and characterized McrA, McrBC, GmrSD, MspJI, PvuRts1I, "
                "EcoKMcrA, ScoMcrA, TagI, or VcaM4I families before minting "
                "narrower Type IV custom-profile traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Loenen and Raleigh support the broad Type IV "
                "modification-dependent restriction class, Bair and Black "
                "support GmrSD as one glucosylated-HMC-targeting Type IV "
                "enzyme, and the pinned DefenseFinder registries support an "
                "RM_Type_IV namespace with a broad Type_IV_REases custom "
                "profile group. The evidence does not yet map any of the "
                "eight pinned RM_Type_IV HMM rows to exact characterized "
                "families or resolve whether the Other_Type_IV, McrBC, "
                "GmrSD_RM_Type_IV, MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, "
                "TagI, and VcaM4I article-registry rows correspond to "
                "reusable organism-level traits below this class."
            ),
            "evidence": [
                type_iv_class_evidence(),
                type_iv_modified_dna_evidence(),
                gmrsd_target_evidence(),
                article_registry_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#type_iv_modification_dependent_restriction"
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
            "Minted type IV modification-dependent restriction system as a "
            "DOI-backed GENOMICS TraitRecord under phage defense system "
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
            "Reviewed type IV modification-dependent restriction system "
            "during initial curation and left canonical_examples empty "
            "because the sources support a broad Type IV "
            "modification-dependent restriction class, a GmrSD enzyme "
            "example, and a DefenseFinder system model, but not a single "
            "stable NCBITaxon strain exemplar for the whole broad Type IV "
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
