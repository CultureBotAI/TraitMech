#!/usr/bin/env python3
"""Add the type IIG restriction-modification system genomics trait."""

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
    / "type_iig_restriction_modification_system.yaml"
)

SHEN = "DOI:10.1093/nar/gkr543"
ZHU = "DOI:10.1038/srep03838"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-26T08:04:20Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T08:14:20Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000375"
PROPOSAL = "proposals/metpo_traitmech_v252"
SLUG = "type_iig_restriction_modification"

BPU_IIG_ARCHITECTURE_SNIPPET = (
    "Type IIG R–M systems also follow this general strategy for target "
    "recognition, but instead of encoding separate REase, MTase and specificity "
    "subunits, they have evolved to combine them within a single uninterrupted "
    "protein chain."
)
BPU_SYSTEM_COMPONENTS_SNIPPET = (
    "The entire BpuSI R–M system consists of two MTase genes (M1 and M2) and "
    "the R–M fusion gene."
)
TTH_CLASS_SNIPPET = (
    "Type IIG (symmetric or asymmetric target sites; endonuclease activity "
    "affected by AdoMet (SAM))"
)
TTH_DOMAINS_SNIPPET = (
    "Tth111II contains both endonuclease (R) and methylase (M) domains and a "
    "shared specificity domain (S)."
)
TTH_RESTRICTION_SNIPPET = (
    "The biological function of restriction-modification systems is to "
    "restrict/cleave foreign invading DNA"
)
ARTICLE_REGISTRY_SNIPPET = (
    "RM_Type_IIG | 10\\.1093/nar/gkac975 | REBASE: a database for DNA "
    "restriction and modification: enzymes, genes and genomes"
)
RULES_SNIPPET = (
    "RM\tRM_Type_IIG\t1\t1\tRM_Type_IIG__Type_IIG\t\t"
    "BREX__pglZB, DISARM__drmB\t"
)
HMM_PROFILES = (
    "RM_Type_IIG__Type_IIG_1",
    "RM_Type_IIG__Type_IIG_2",
    "RM_Type_IIG__Type_IIG_3",
    "RM_Type_IIG__Type_IIG_4",
    "RM_Type_IIG__Type_IIG_5",
    "RM_Type_IIG__Type_IIG_FAM_0.einsi_trimmed",
    "RM_Type_IIG__Type_IIG_FAM_1.einsi_trimmed",
    "RM_Type_IIG__Type_IIG_FAM_2.einsi_trimmed",
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {'':<49}| {'RM_Type_IIG':<23}| "
    f"{'Custom':<24}| {'300':<7}|"
    for profile in HMM_PROFILES
)


def bpusi_architecture_evidence() -> dict[str, str]:
    return {
        "reference": SHEN,
        "snippet": BPU_IIG_ARCHITECTURE_SNIPPET,
        "notes": (
            "Shen et al. define Type IIG restriction-modification systems "
            "as systems that combine restriction, methyltransferase, and "
            "specificity subunits in one uninterrupted protein chain."
        ),
    }


def bpusi_components_evidence() -> dict[str, str]:
    return {
        "reference": SHEN,
        "snippet": BPU_SYSTEM_COMPONENTS_SNIPPET,
        "notes": (
            "The characterized BpuSI Type IIG example carries two companion "
            "methyltransferase genes and an R-M fusion gene, supporting a "
            "locus-level system trait rather than a single protein trait."
        ),
    }


def tth_class_evidence() -> dict[str, str]:
    return {
        "reference": ZHU,
        "snippet": TTH_CLASS_SNIPPET,
        "notes": (
            "Zhu et al. place Type IIG in the Type II restriction enzyme "
            "classification and describe variable target symmetry plus "
            "AdoMet/SAM-sensitive endonuclease activity."
        ),
    }


def tth_domains_evidence() -> dict[str, str]:
    return {
        "reference": ZHU,
        "snippet": TTH_DOMAINS_SNIPPET,
        "notes": (
            "The cloned Tth111II Type IIGS enzyme has endonuclease, "
            "methylase, and specificity domains in one polypeptide."
        ),
    }


def tth_restriction_evidence() -> dict[str, str]:
    return {
        "reference": ZHU,
        "snippet": TTH_RESTRICTION_SNIPPET,
        "notes": (
            "Zhu et al. frame the Type IIGS decision between cleaving and "
            "modifying unmodified DNA in the broader restriction-modification "
            "role of cleaving foreign invading DNA."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "RM_Type_IIG model to the REBASE update."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RM_Type_IIG as an RM "
            "subsystem that requires the RM_Type_IIG__Type_IIG profile group "
            "and excludes two non-RM profiles."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory lists eight custom profiles "
            "under the RM_Type_IIG system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "type IIG restriction-modification system",
    "definition": (
        "A restriction-modification system in which an organism possesses a "
        "Type IIG locus centered on a restriction-methyltransferase-specificity "
        "fusion gene represented by DefenseFinder as the RM_Type_IIG subsystem."
    ),
    "definition_source": SHEN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000095"],
    "synonyms": [
        {
            "synonym_text": "RM_Type_IIG",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "RM_Type_IIG__Type_IIG",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
    ],
    "evidence": [
        bpusi_architecture_evidence(),
        bpusi_components_evidence(),
        tth_class_evidence(),
        tth_domains_evidence(),
        tth_restriction_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "type_iig_rm_locus_restricts_foreign_dna",
            "title": "Type IIG R-M loci mark self and restrict foreign DNA",
            "description": (
                "Conservative system-level sketch linking Type IIG "
                "restriction-methyltransferase-specificity fusion loci to "
                "restriction-modification-mediated foreign DNA cleavage."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the reusable Type IIG locus architecture "
                "and the DefenseFinder RM_Type_IIG custom-profile namespace "
                "without asserting an accession-level mapping between each "
                "custom HMM, BpuSI, Tth111II, or companion methyltransferases."
            ),
            "nodes": [
                {
                    "node_id": "type_iig_rm_locus",
                    "label": "type IIG restriction-modification locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Type IIG R-M locus centered on a single "
                        "restriction-methyltransferase-specificity fusion gene "
                        "and, in some systems, one or more companion "
                        "methyltransferase genes."
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
                    "label": "type IIG restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded type IIG "
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
                    "subject": "type_iig_rm_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "foreign_unmethylated_dna_cleavage",
                    "description": (
                        "Type IIG loci encode the fusion architecture and "
                        "methyltransferase context needed to cleave "
                        "unprotected foreign DNA."
                    ),
                    "evidence": [
                        bpusi_architecture_evidence(),
                        bpusi_components_evidence(),
                        tth_domains_evidence(),
                    ],
                },
                {
                    "subject": "foreign_unmethylated_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Type IIG restriction-modification activity realizes "
                        "the organism-level Type IIG R-M system trait."
                    ),
                    "evidence": [
                        tth_class_evidence(),
                        tth_restriction_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "restriction_modification_system",
                    "description": (
                        "A Type IIG R-M system is a subtype of broader "
                        "restriction-modification system possession."
                    ),
                    "evidence": [
                        bpusi_architecture_evidence(),
                        article_registry_evidence(),
                        hmm_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "type-iig-rm-profile-interpretation-gap",
            "prompt": (
                "Resolve the accession-level relationships between "
                "DefenseFinder RM_Type_IIG custom profiles, characterized "
                "BpuSI- or Tth111II-like enzymes, and companion "
                "methyltransferases before minting narrower Type IIG "
                "protein or subfamily traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Shen et al. and Zhu et al. support Type IIG R-M system "
                "architecture and experimentally characterized BpuSI and "
                "Tth111II examples, while the pinned DefenseFinder registry "
                "supports an RM_Type_IIG system-level namespace with eight "
                "custom HMM rows. The evidence does not yet map each custom "
                "profile row to exact characterized enzyme families or "
                "resolve companion methyltransferase requirements."
            ),
            "evidence": [
                bpusi_architecture_evidence(),
                tth_domains_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#type_iig_rm_locus_restricts_foreign_dna"
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted type IIG restriction-modification system as a DOI-backed "
            "GENOMICS TraitRecord under restriction-modification system after "
            "an ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
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
            "Reviewed type IIG restriction-modification system during "
            "canonical-example issue 444 enforcement and left "
            "canonical_examples empty because the sources support "
            "biochemically characterized BpuSI and Tth111II natural isolates "
            "plus a DefenseFinder system model, but not a direct stable "
            "NCBITaxon strain exemplar with whole-system Type IIG activity. "
            "No paid research was used."
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

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
