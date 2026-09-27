#!/usr/bin/env python3
"""Add the Rst_HelicaseDUF2290 system genomics trait."""

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
    / "rst_helicaseduf2290_system.yaml"
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
    "223cf269/content/3.defense-systems/rst_helicaseduf2290.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T04:03:20Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T04:03:21Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000401"
PROPOSAL = "proposals/metpo_traitmech_v278"
SLUG = "rst_helicaseduf2290"

ROUSSET_T7_SNIPPET = (
    "two systems that specifically inhibit the growth of phage T7: an "
    "ATP-dependent helicase associated with a DUF2290 protein and a "
    "HAD-like hydrolase associated with a transmembrane protein"
)
ROUSSET_VALIDATED_DEFENSES_SNIPPET = (
    "Phage resistance heatmaps of the validated defense systems show the "
    "median fold resistance of three independent replicates against a panel "
    "of eight phages"
)
WIKI_DESCRIPTION_SNIPPET = (
    "The Rst_HelicaseDUF2290 system was discovered during a screen for "
    "defense systems targeted at hotspots of antiphage activity in phages "
    "and phage-satellites. It is composed of 2 proteins, a helicase and a "
    "protein with the domain DUF2290."
)
WIKI_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_STRUCTURE_SNIPPET = (
    "The Rst_HelicaseDUF2290 is composed of 2 proteins: Helicase and "
    "DUF2290."
)
WIKI_REFSEQ_SNIPPET = (
    "The Rst_HelicaseDUF2290 system in *Klebsiella quasipneumoniae* "
    "(GCF_003020825.1, NZ_CP023478) is composed of 2 proteins Helicase "
    "(WP_046623504.1) DUF2290_Pers (WP_046623503.1)"
)
WIKI_VALIDATION_SNIPPET = (
    "Rousset_2022[<a href='https://doi.org/10.1016/"
    "j.chom.2022.02.018'>Rousset et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Klebsiella pneumoniae P4 loci \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_046623503.1'>"
    "WP_046623503.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_046623504.1'>WP_046623504.1</a>] --> "
    "Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T7"
)
PROTECTS_SUBGRAPH_SNIPPET = "subgraph Title4[Protects against]\n        T7"
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_HelicaseDUF2290 | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_HelicaseDUF2290\tRst_HelicaseDUF2290\t2\t2\t"
    "Rst_HelicaseDUF2290__DUF2290, "
    "Rst_HelicaseDUF2290__Helicase\t\t\t"
)
HMM_PROFILES = (
    (
        "Rst_HelicaseDUF2290__DUF2290",
        "Rst_HelicaseDUF2290__DUF2290___DUF2290",
        "PF10053.11",
        "25",
    ),
    (
        "Rst_HelicaseDUF2290__DUF2290_Pers",
        "Rst_HelicaseDUF2290__DUF2290_Pers___DUF2290_Pers",
        "Custom",
        "20",
    ),
    (
        "Rst_HelicaseDUF2290__Helicase",
        "Rst_HelicaseDUF2290__Helicase___Helicase",
        "Custom",
        "20",
    ),
)
HMM_SNIPPET = "\n".join(
    f"| {gene_name:<49}| {hmm_name:<49}| "
    f"{'Rst_HelicaseDUF2290':<23}| {accession:<24}| {ga_cut:<7}|"
    for gene_name, hmm_name, accession, ga_cut in HMM_PROFILES
)


def rousset_t7_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_T7_SNIPPET,
        "notes": (
            "Rousset et al. experimentally linked an ATP-dependent "
            "helicase plus DUF2290 protein pair to specific inhibition of "
            "phage T7 growth."
        ),
    }


def rousset_validated_defenses_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_VALIDATED_DEFENSES_SNIPPET,
        "notes": (
            "The Figure 5 legend frames the cloned P4-hotspot hits, "
            "including the ATP-dependent helicase plus DUF2290 system, as "
            "validated defense systems in a replicated phage-resistance "
            "heatmap."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names "
            "Rst_HelicaseDUF2290 as a two-protein helicase/DUF2290 system "
            "found in antiviral hotspots of phages and phage satellites."
        ),
    }


def wiki_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page leaves the "
            "Rst_HelicaseDUF2290 molecular mechanism unresolved."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes "
            "Rst_HelicaseDUF2290 as a two-component Helicase/DUF2290 "
            "system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "Rst_HelicaseDUF2290 locus in RefSeq assembly GCF_003020825.1 "
            "on NZ_CP023478."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Rousset et al. to a Klebsiella pneumoniae P4-locus source "
            "expressed in Escherichia coli against T7."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists T7 in "
            "the Rst_HelicaseDUF2290 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Rst_HelicaseDUF2290 system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_HelicaseDUF2290 as a "
            "two-profile system requiring Rst_HelicaseDUF2290__DUF2290 "
            "and Rst_HelicaseDUF2290__Helicase."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records DUF2290, "
            "DUF2290_Pers, and Helicase profiles under "
            "Rst_HelicaseDUF2290."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_HelicaseDUF2290 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-protein Rst_HelicaseDUF2290 locus represented by "
        "DefenseFinder as a two-profile model requiring "
        "Rst_HelicaseDUF2290__DUF2290 and "
        "Rst_HelicaseDUF2290__Helicase and experimentally linked to T7 "
        "protection when expressed in Escherichia coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_HelicaseDUF2290",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        *[
            {
                "synonym_text": gene_name,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for gene_name, _hmm_name, _accession, _ga_cut in HMM_PROFILES
        ],
        {
            "synonym_text": "DUF2290_Pers",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
    ],
    "evidence": [
        rousset_t7_evidence(),
        rousset_validated_defenses_evidence(),
        wiki_description_evidence(),
        wiki_mechanism_evidence(),
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
            "graph_id": "rst_helicaseduf2290_locus_restricts_t7",
            "title": "Rst_HelicaseDUF2290 loci restrict T7",
            "description": (
                "Conservative system-level sketch linking the named "
                "Rst_HelicaseDUF2290 two-gene locus model to T7 phage "
                "resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_HelicaseDUF2290 as a named "
                "DefenseFinder two-profile phage-defense system while "
                "leaving native host breadth, accession-level DUF2290 and "
                "helicase roles, the extra DUF2290_Pers profile, and the "
                "mechanism of T7 restriction unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_helicaseduf2290_locus",
                    "label": "Rst_HelicaseDUF2290 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene helicase/DUF2290 phage-defense locus "
                        "represented by the DefenseFinder "
                        "Rst_HelicaseDUF2290 profiles."
                    ),
                },
                {
                    "node_id": "t7_phage_resistance",
                    "label": "T7 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Resistance against phage T7 in a host expressing "
                        "an Rst_HelicaseDUF2290 locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_HelicaseDUF2290 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded "
                        "Rst_HelicaseDUF2290 phage-defense system."
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
                    "subject": "rst_helicaseduf2290_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t7_phage_resistance",
                    "description": (
                        "Rousset et al. linked an ATP-dependent helicase "
                        "plus DUF2290 locus to T7 restriction, and "
                        "DefenseFinder models Rst_HelicaseDUF2290 as a "
                        "two-profile system."
                    ),
                    "evidence": [
                        rousset_t7_evidence(),
                        wiki_description_evidence(),
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
                        "Rst_HelicaseDUF2290-linked T7 resistance realizes "
                        "the Rst_HelicaseDUF2290 system trait."
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
                        "Rst_HelicaseDUF2290 system possession is a "
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
            "discussion_id": "rst-helicaseduf2290-host-mechanism-gap",
            "prompt": (
                "Resolve Rst_HelicaseDUF2290 native host breadth, "
                "accession-level DUF2290/helicase roles, the "
                "DUF2290_Pers profile relationship, and the mechanism of "
                "T7 restriction before minting narrower "
                "Rst_HelicaseDUF2290 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a two-gene ATP-dependent helicase "
                "plus DUF2290 P4-hotspot system that inhibits T7 growth, "
                "and DefenseFinder represents Rst_HelicaseDUF2290 as a "
                "required two-profile model. This first system-level "
                "record leaves native host breadth, profile-to-gene "
                "mapping, the role of the extra DUF2290_Pers HMM profile, "
                "the molecular activities of the DUF2290 and helicase "
                "components, and the T7 restriction mechanism unresolved."
            ),
            "evidence": [
                rousset_t7_evidence(),
                wiki_mechanism_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#rst_helicaseduf2290_locus_restricts_t7"
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
            "Minted Rst_HelicaseDUF2290 system as a DOI/stable-URL-backed "
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
            "Reviewed Rst_HelicaseDUF2290 during canonical-example issue "
            "444 enforcement and left canonical_examples empty because "
            "the sources support a cloned P4-hotspot helicase/DUF2290 "
            "locus assayed in Escherichia coli and a DefenseFinder "
            "RefSeq model example, but not a direct native microbial "
            "host exemplar with experimentally verified "
            "Rst_HelicaseDUF2290 activity. No paid research was used."
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
