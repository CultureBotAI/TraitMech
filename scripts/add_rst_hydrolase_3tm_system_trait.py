#!/usr/bin/env python3
"""Add the Rst_Hydrolase-3Tm system genomics trait."""

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
    / "rst_hydrolase_3tm_system.yaml"
)

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/"
    "223cf269/content/3.defense-systems/rst_hydrolase-3tm.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T05:04:25Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T05:04:26Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000402"
PROPOSAL = "proposals/metpo_traitmech_v279"
SLUG = "rst_hydrolase_3tm"

ROUSSET_T7_SNIPPET = (
    "two systems that specifically inhibit the growth of phage T7: an "
    "ATP-dependent helicase associated with a DUF2290 protein and a "
    "HAD-like hydrolase associated with a transmembrane protein"
)
ROUSSET_VALIDATED_DEFENSES_SNIPPET = (
    "Phage resistance heatmap of the validated defense systems shows the "
    "mean fold resistance of three independent replicates against a panel "
    "of eight phages"
)
WIKI_STRUCTURE_SNIPPET = (
    "The Rst_Hydrolase-3Tm is composed of 2 proteins: Hydrolase and "
    "Hydrolase-Tm."
)
WIKI_REFSEQ_SNIPPET = (
    "The Rst_Hydrolase-Tm system in *Pectobacterium versatile* "
    "(GCF_003031305.1, NZ_CP024842) is composed of 2 proteins Hydrolase "
    "(WP_107333258.1) Hydrolase-Tm (WP_107333259.1)"
)
WIKI_VALIDATION_SNIPPET = (
    "Rousset_2022[<a href='https://doi.org/10.1016/"
    "j.chom.2022.02.018'>Rousset et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli P4 loci \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_000754434.1'>"
    "WP_000754434.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_001401335.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T7"
)
PROTECTS_SUBGRAPH_SNIPPET = "subgraph Title4[Protects against]\n        T7"
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_Hydrolase-3Tm | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_Hydrolase-3Tm\tRst_Hydrolase-Tm\t2\t2\t"
    "Rst_Hydrolase-Tm__Hydrolase, "
    "Rst_Hydrolase-Tm__Hydrolase-Tm\t\t\t"
)
HMM_PROFILES = (
    "Rst_Hydrolase-Tm__Hydrolase",
    "Rst_Hydrolase-Tm__Hydrolase-Tm",
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {profile:<49}| {'Rst_Hydrolase-Tm':<23}| "
    f"{'Custom':<24}| {'20':<7}|"
    for profile in HMM_PROFILES
)


def rousset_t7_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_T7_SNIPPET,
        "notes": (
            "Rousset et al. experimentally linked a HAD-like hydrolase "
            "plus transmembrane-protein pair to specific inhibition of "
            "phage T7 growth."
        ),
    }


def rousset_validated_defenses_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_VALIDATED_DEFENSES_SNIPPET,
        "notes": (
            "The Figure 5 legend frames the cloned P4-hotspot hits, "
            "including the hydrolase plus transmembrane-protein system, "
            "as validated defense systems in a replicated "
            "phage-resistance heatmap."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names Rst_Hydrolase-3Tm "
            "as a two-component Hydrolase/Hydrolase-Tm system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "Rst_Hydrolase-Tm locus in RefSeq assembly GCF_003031305.1 "
            "on NZ_CP024842."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Rousset et al. to an Escherichia coli P4-locus source "
            "expressed in Escherichia coli against T7."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists T7 in "
            "the Rst_Hydrolase-3Tm protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Rst_Hydrolase-3Tm system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table maps Rst_Hydrolase-3Tm to a "
            "two-profile Rst_Hydrolase-Tm model requiring Hydrolase and "
            "Hydrolase-Tm profiles."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records Hydrolase and "
            "Hydrolase-Tm profiles under the normalized Rst_Hydrolase-Tm "
            "system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_Hydrolase-3Tm system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-protein Rst_Hydrolase-3Tm locus represented by "
        "DefenseFinder as a two-profile Rst_Hydrolase-Tm model requiring "
        "Rst_Hydrolase-Tm__Hydrolase and "
        "Rst_Hydrolase-Tm__Hydrolase-Tm and experimentally linked to T7 "
        "protection when expressed in Escherichia coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_Hydrolase-3Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Rst_Hydrolase-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_PROFILES
        ],
        {
            "synonym_text": "Hydrolase-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
    ],
    "evidence": [
        rousset_t7_evidence(),
        rousset_validated_defenses_evidence(),
        wiki_structure_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_hydrolase_3tm_locus_restricts_t7",
            "title": "Rst_Hydrolase-3Tm loci restrict T7",
            "description": (
                "Conservative system-level sketch linking a named "
                "Rst_Hydrolase-3Tm two-gene locus model to T7 phage "
                "resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_Hydrolase-3Tm as a named "
                "DefenseFinder two-profile phage-defense system while "
                "leaving native host breadth, the exact "
                "Rst_Hydrolase-3Tm-to-Rst_Hydrolase-Tm naming "
                "relationship, Hydrolase and Hydrolase-Tm molecular roles, "
                "and the mechanism of T7 restriction unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_hydrolase_3tm_locus",
                    "label": "Rst_Hydrolase-3Tm locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene hydrolase/transmembrane "
                        "phage-defense locus represented by the "
                        "DefenseFinder Rst_Hydrolase-Tm profiles."
                    ),
                },
                {
                    "node_id": "t7_phage_resistance",
                    "label": "T7 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Resistance against phage T7 in a host expressing "
                        "an Rst_Hydrolase-3Tm locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_Hydrolase-3Tm system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded "
                        "Rst_Hydrolase-3Tm phage-defense system."
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
                    "subject": "rst_hydrolase_3tm_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t7_phage_resistance",
                    "description": (
                        "Rousset et al. linked a HAD-like hydrolase plus "
                        "transmembrane-protein locus to T7 restriction, "
                        "and DefenseFinder models Rst_Hydrolase-3Tm as a "
                        "two-profile Rst_Hydrolase-Tm system."
                    ),
                    "evidence": [
                        rousset_t7_evidence(),
                        wiki_structure_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "t7_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Rst_Hydrolase-3Tm-linked T7 resistance realizes "
                        "the Rst_Hydrolase-3Tm system trait."
                    ),
                    "evidence": [
                        rousset_t7_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst_Hydrolase-3Tm system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        rousset_validated_defenses_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-hydrolase-3tm-host-mechanism-gap",
            "prompt": (
                "Resolve Rst_Hydrolase-3Tm native host breadth, the "
                "Rst_Hydrolase-3Tm and Rst_Hydrolase-Tm namespace "
                "relationship, accession-level Hydrolase/Hydrolase-Tm "
                "roles, and the mechanism of T7 restriction before "
                "minting narrower Rst_Hydrolase-3Tm mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a two-gene HAD-like hydrolase plus "
                "transmembrane-protein P4-hotspot system that inhibits T7 "
                "growth, and DefenseFinder maps Rst_Hydrolase-3Tm to a "
                "required two-profile Rst_Hydrolase-Tm model. This first "
                "system-level record leaves native host breadth, "
                "profile-to-gene mapping, the model-namespace mismatch, "
                "the molecular activities of the Hydrolase and "
                "Hydrolase-Tm components, and the T7 restriction mechanism "
                "unresolved."
            ),
            "evidence": [
                rousset_t7_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#rst_hydrolase_3tm_locus_restricts_t7"
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
            "Minted Rst_Hydrolase-3Tm system as a DOI/stable-URL-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
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
            "Reviewed Rst_Hydrolase-3Tm during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support a cloned P4-hotspot Hydrolase/Hydrolase-Tm "
            "locus assayed in Escherichia coli and a DefenseFinder RefSeq "
            "model example, but not a direct native microbial host "
            "exemplar with experimentally verified Rst_Hydrolase-3Tm "
            "activity. No paid research was used."
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
