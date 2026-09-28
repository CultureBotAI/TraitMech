#!/usr/bin/env python3
"""Add the DS-16 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_16_system.yaml"

DEWEIRDT = "DOI:10.1126/science.adv7924"

PMC_S3_PREFIX = "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/"
TABLE_S6 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S6.xlsx"
TABLE_S7 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S7.xlsx"
TABLE_S8 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S8.xlsx"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-28T17:24:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T17:24:01Z"

IDENTIFIER = "traitmech:000439"
PROPOSAL = "proposals/metpo_traitmech_v316"

DS_VALIDATION_SNIPPET = (
    "To test for anti-phage defense, we placed each TU with its predicted "
    "native promoter region on a low-copy number plasmid in E. coli MG1655 "
    "and challenged these strains with a panel of 24 diverse E. coli phages "
    "(Fig. 3; fig. S2). In total, 42 (45% of 94) of the cloned TUs produced "
    "smaller plaque sizes or reduced the efficiency of plating (EOP) at "
    "least ten-fold relative to an empty vector control strain"
)
DS_NAMING_SNIPPET = (
    "We refer to these validated TUs as DefensePredictor discovered systems "
    "(DSs), with genes in multi-gene TUs denoted by an alphabetical suffix, "
    "e.g., DS-8A is the first gene of DS-8."
)
ARTICLE_ROW = (
    "| DS-16 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-16__DS-16A": (
        "| DS-16__DS-16A                                    |"
        "                                                  | DS-16"
        "                  | Custom                  | 500    |"
    ),
    "DS-16__DS-16B": (
        "| DS-16__DS-16B                                    |"
        "                                                  | DS-16"
        "                  | Custom                  | 50     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-16 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom DS-16 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "PLIK\tNZ_QOYD01000001.1\tGCF_003333765.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t281241\t284220"
            "\thypothetical protein, DUF3696 domain-containing protein"
            "\tWP_001676492.1, WP_001676491.1\t10.6830001978657"
            "\t5.517452896464706\tTrue\tTrue\tStructural defense homolog"
            "\tDS-16"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id PLIK "
            "to DS_name DS-16, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOYD01000001.1 positions "
            "281241-284220 with product accessions WP_001676492.1 and "
            "WP_001676491.1."
        ),
    }


def table_s7_bas26_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas26\t2.2\tpLAND\t24-03-12_EV.png\t2400000000"
            "\tPLIK\t24-03-21\t24-03-21_PLIK_REPB_2.png\t7\t31"
            "\tY\t310000000\t0.8888495478773333\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a PLIK assay "
            "row with a Bas26 phage readout and smaller plaques."
        ),
    }


def table_s7_t4_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T4\t2.1\tpLAND\t24-03-12_EV.png\t200000000\tPLIK"
            "\t24-03-21\t24-03-21_PLIK_REPB.png\t3\t100\t\t100000"
            "\t3.3010299956639813\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a PLIK assay "
            "row with a T4 phage readout and a -log(EOP) value of 3.301."
        ),
    }


def all_table_s7_evidence() -> list[dict[str, str]]:
    return [table_s7_bas26_evidence(), table_s7_t4_evidence()]


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "PLIK\tDS-16\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps PLIK to "
            "replicated display name DS-16."
        ),
    }


def table_s8_rele_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PLIK\t2.0\t341.0\tWP_001676492.1\tRelE\t4NRN_A"
            "\tmetal-bound toxin; Toxin;\thhpred_4269994.hhr\t239.0"
            "\t335.0\t0.8002\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a RelE HHpred "
            "hit for WP_001676492.1 in PLIK."
        ),
    }


def table_s8_abc_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PLIK\t1.0\t656.0\tWP_001676491.1\tABC ATPase\t6QJ0_A"
            "\tStructural maintenance of chromosomes protein,Structural "
            "maintenance of chromosomes protein; condensin SMC complex "
            "ATPase\thhpred_2524462.hhr\t1.0\t572.0\t0.997"
            "\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports an ABC ATPase "
            "HHpred hit for WP_001676491.1 in PLIK."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_rele_evidence(), table_s8_abc_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-16 system",
    "definition": (
        "A phage defense system in which an organism possesses the two-gene "
        "DefensePredictor-discovered system 16 locus cataloged as working "
        "transcriptional unit PLIK and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-16",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "PLIK",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_PROFILE_SNIPPETS
        ],
    ],
    "evidence": [
        {
            "reference": DEWEIRDT,
            "snippet": DS_VALIDATION_SNIPPET,
            "notes": (
                "DeWeirdt et al. experimentally validated 42 predicted "
                "transcriptional units as phage-defense systems in E. coli."
            ),
        },
        {
            "reference": DEWEIRDT,
            "snippet": DS_NAMING_SNIPPET,
            "notes": (
                "DeWeirdt et al. name validated transcriptional units as "
                "DefensePredictor discovered systems."
            ),
        },
        table_s6_evidence(),
        *all_table_s7_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_16_locus_reduces_phage_plaquing",
            "title": "DS-16 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-16 locus to reduced bacteriophage plaquing without "
                "resolving DS-16 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-16 as the validated PLIK "
                "transcriptional unit with two product accessions, RelE and "
                "ABC ATPase HHpred-domain rows, and two DefenseFinder DS-16 "
                "profile rows. It does not assert native host breadth, exact "
                "profile-to-protein correspondence, DS-16A or DS-16B "
                "molecular activity, trigger, substrate, phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_16_locus",
                    "label": "DS-16 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system 16 "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by DS-16A and DS-16B custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned PLIK."
                    ),
                },
                {
                    "node_id": "ds_16_system_trait",
                    "label": "DS-16 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-16 phage-defense "
                        "system."
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
                    "subject": "ds_16_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-16/PLIK locus contributes to reduced "
                        "bacteriophage plaquing in heterologous E. coli "
                        "MG1655 plasmid-expression assays."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_VALIDATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. describe the plasmid-based "
                                "phage challenge used to validate predicted "
                                "transcriptional units."
                            ),
                        },
                        table_s6_evidence(),
                        *all_table_s7_evidence(),
                        table_s8_display_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_16_system_trait",
                    "description": (
                        "DS-16-mediated phage plaquing reduction realizes "
                        "the DS-16 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        *all_table_s7_evidence(),
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "The DS nomenclature is used for "
                                "DefensePredictor discovered systems."
                            ),
                        },
                    ],
                },
                {
                    "subject": "ds_16_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-16 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name validated TUs as "
                                "DefensePredictor discovered systems."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ds-16-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-16 native host breadth, exact "
                "profile-to-protein mapping, DS-16A/DS-16B component "
                "activities, RelE and ABC ATPase chemistry, sensitive-phage "
                "breadth, molecular output, and rule-level DefenseFinder "
                "criteria before minting narrower DS-16 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-16 as the defensive PLIK "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to product accessions WP_001676492.1 and "
                "WP_001676491.1, Bas26 and T4 phage readouts, display name "
                "DS-16, and RelE/ABC ATPase HHpred rows. The pinned "
                "DefenseFinder HMM inventory records DS-16A and DS-16B "
                "custom profile rows. The pinned rules table has no DS-16 "
                "row, and the first-pass record does not resolve native "
                "host breadth, phage breadth, direct profile-to-protein "
                "correspondence, RelE nuclease or ABC ATPase activity, "
                "molecular output, or endogenous DS-16 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                *all_table_s7_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-16, DS-16A, or DS-16B, leaving complete "
                        "component coverage and rule-level detection "
                        "criteria unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_16_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-28",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted DS-16 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at PLIK "
            "transcriptional-unit level because RelE/ABC ATPase chemistry "
            f"and rule rows remain unresolved, and {PROPOSAL} reserves the "
            "replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-16 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned PLIK assays in "
            "E. coli MG1655 and DefenseFinder DS-16 models, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-16 activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"Wrote {rel}")
    else:
        import yaml

        print(yaml.safe_dump(record, sort_keys=False, allow_unicode=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
