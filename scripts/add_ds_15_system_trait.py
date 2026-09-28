#!/usr/bin/env python3
"""Add the DS-15 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_15_system.yaml"

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
TIMESTAMP = "2026-09-28T16:50:13Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T16:50:14Z"

IDENTIFIER = "traitmech:000438"
PROPOSAL = "proposals/metpo_traitmech_v315"

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
    "| DS-15 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-15__DS-15A": (
        "| DS-15__DS-15A                                    |"
        "                                                  | DS-15"
        "                  | Custom                  | 300    |"
    ),
    "DS-15__DS-15B": (
        "| DS-15__DS-15B                                    |"
        "                                                  | DS-15"
        "                  | Custom                  | 20     |"
    ),
    "DS-15__DS-15C": (
        "| DS-15__DS-15C                                    |"
        "                                                  | DS-15"
        "                  | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-15 "
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
            "custom DS-15 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "AAA1\tNZ_QOXE01000046.1\tGCF_003334165.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t29629\t31530"
            "\thypothetical protein, hypothetical protein, AAA family ATPase"
            "\tWP_000957441.1, WP_060581740.1, WP_001619161.1"
            "\t11.46862191778244\t2.030866871531279\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-15"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id AAA1 "
            "to DS_name DS-15, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOXE01000046.1 positions "
            "29629-31530 with product accessions WP_000957441.1, "
            "WP_060581740.1, and WP_001619161.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t4.2\tpLAND\t24-05-17_EV_HHNH.png\t5000000"
            "\tAAA1\t24-05-17\t24-05-17_VAME_AAA1_PD3A_PDP7.png"
            "\t2\t100\t\t10000\t2.6989700043360187\t\tTrue"
            "\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an AAA1 "
            "assay row with a Bas1 phage readout and a -log(EOP) value "
            "of 2.699."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "AAA1\tDS-15\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps AAA1 to "
            "replicated display name DS-15."
        ),
    }


def table_s8_mind_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "AAA1\t1.0\t281.0\tWP_001619161.1\tMinD ATPase"
            "\tSCOP_d1hyqa_\tc.37.1.10 (A:) Cell division regulator "
            "MinD {Archaeoglobus fulgidus [TaxId: 2234]} | CLASS: "
            "Alpha and beta proteins (a/b), FOLD: P-loop containing "
            "nucleoside triphosphate hydrolases, SUPFAM: P-loop "
            "containing nucleoside triphosphate hydrolases, FAM: "
            "Nitrogenase iron protein-like\thhpred_6736485.hhr\t3.0"
            "\t268.0\t1.0\t2024-07-29 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a MinD "
            "ATPase HHpred hit for WP_001619161.1 in AAA1."
        ),
    }


def table_s8_duf6988_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "AAA1\t3.0\t221.0\tWP_000957441.1\tDUF6988\tPF22491.1"
            "\tDUF6988 ; Family of unknown function (DUF6988)"
            "\thhpred_7907160.hhr\t68.0\t144.0\t0.94"
            "\t2024-07-29 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a DUF6988 "
            "HHpred hit for WP_000957441.1 in AAA1."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_mind_evidence(), table_s8_duf6988_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-15 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "three-gene DefensePredictor-discovered system 15 locus cataloged "
        "as working transcriptional unit AAA1 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-15",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "AAA1",
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
        table_s7_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_15_locus_reduces_phage_plaquing",
            "title": "DS-15 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the three-gene "
                "DS-15 locus to reduced bacteriophage plaquing without "
                "resolving DS-15 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-15 as the validated AAA1 "
                "transcriptional unit with three product accessions, final "
                "Table S8 MinD ATPase and DUF6988 HHpred-domain rows, and "
                "three DefenseFinder DS-15 profile rows. It does not assert "
                "native host breadth, exact profile-to-protein "
                "correspondence, the direct viral trigger or substrate, "
                "exact AAA family ATPase or DUF6988 chemistry, phage target "
                "breadth, or DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_15_locus",
                    "label": "DS-15 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by DS-15A, DS-15B, and DS-15C custom "
                        "profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas1 in cells carrying cloned AAA1."
                    ),
                },
                {
                    "node_id": "ds_15_system_trait",
                    "label": "DS-15 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-15 phage-defense "
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
                    "subject": "ds_15_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-15/AAA1 locus contributes to reduced "
                        "bacteriophage plaquing when plasmid expressed."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_VALIDATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. experimentally validate "
                                "DefensePredictor-discovered systems by "
                                "assaying cloned transcriptional units "
                                "against E. coli phages."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_15_system_trait",
                    "description": (
                        "DS-15-mediated phage plaquing reduction realizes "
                        "the DS-15 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name each validated "
                                "transcriptional unit as a "
                                "DefensePredictor discovered system."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "ds_15_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-15 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_VALIDATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. validate DSs as "
                                "anti-phage systems."
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
            "discussion_id": "ds-15-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-15 native host breadth, exact "
                "profile-to-protein mapping, DS-15A/DS-15B/DS-15C "
                "component activities, sensitive-phage breadth, exact AAA "
                "family ATPase and DUF6988 chemistry, and rule-level "
                "DefenseFinder criteria before minting narrower DS-15 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-15 as the defensive AAA1 "
                "transcriptional unit that reduced Bas1 plaquing when "
                "cloned in E. coli MG1655, the final Table S8 HHpred sheet "
                "reports MinD ATPase and DUF6988 hits across two AAA1 "
                "products, and the pinned DefenseFinder HMM inventory "
                "records DS-15A, DS-15B, and DS-15C custom profile rows. "
                "The pinned rules table has no DS-15 row, and the "
                "first-pass record does not resolve native host breadth, "
                "exact profile-to-protein correspondence, direct ATPase or "
                "DUF6988 activity, phage target breadth, or endogenous "
                "DS-15 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_VALIDATION_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. validate predicted transcriptional "
                        "units by measuring plaquing relative to an empty "
                        "vector control strain."
                    ),
                },
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-15, DS-15A, DS-15B, or DS-15C, leaving "
                        "complete component coverage and rule-level "
                        "detection criteria unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_15_locus_reduces_phage_plaquing"],
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
            "Minted DS-15 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned AAA1 "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-15 HMM rows are not backed by a rules row; "
            f"{PROPOSAL} reserves the replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-15 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned AAA1 plaquing assays in "
            "E. coli MG1655 plus DefenseFinder DS-15 models, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-15 activity. No paid "
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
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
