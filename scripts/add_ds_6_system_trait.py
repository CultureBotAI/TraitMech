#!/usr/bin/env python3
"""Add the DS-6 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_6_system.yaml"

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
TIMESTAMP = "2026-09-28T09:20:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T09:20:01Z"

IDENTIFIER = "traitmech:000430"
PROPOSAL = "proposals/metpo_traitmech_v307"

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
DS_HIPAD_SNIPPET = "We independently discovered DS-6 (renamed HipAD) recently"
DS_D139A_SNIPPET = (
    "When we mutated a key predicted catalytic residue in DS-6A, we observed "
    "a loss of defense, suggesting that kinase activity is essential for "
    "protection."
)
ARTICLE_ROW = (
    "| DS-6 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-6__DS-6A": (
        "| DS-6__DS-6A                                      |"
        "                                                  | DS-6"
        "                   | Custom                  | 100    |"
    ),
    "DS-6__DS-6B": (
        "| DS-6__DS-6B                                      |"
        "                                                  | DS-6"
        "                   | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-6 "
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
            "custom DS-6 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "HIPA\tNZ_QOWQ01000062.1\tGCF_003334335.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t1591\t3164"
            "\tDUF3037 domain-containing protein, hypothetical protein"
            "\tWP_000210934.1, WP_000389051.1\t6.427268761356274"
            "\t-2.428836967683248\tTrue\tFalse"
            "\tPredicted novel defense gene\tDS-6"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id HIPA "
            "to DS_name DS-6, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOWQ01000062.1 positions "
            "1591-3164 with product accessions WP_000210934.1 and "
            "WP_000389051.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t40000000\tHIPA\t24-03-08"
            "\t24-03-08_IMPD_DISA_2CM2_MAZF.png\t3\t5\tY\t5000"
            "\t3.9030899869919438\tTrue\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a HIPA assay "
            "row with a Bas1 phage readout, smaller plaques, and a "
            "-log(EOP) value of 3.903."
        ),
    }


def table_s7_d139a_panel_a_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\tA.1\tMG1655"
            "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
            "\t3000000\tHIPA\t\t24-07-12"
            "\t24-07-12_HIPA_HIPA-D139A_SVIR_SVIR-H52A_DISA_DISA-D433A.png"
            "\t1\t2\t\t20\t5.176091259\n"
            "Bas1\tA.1\tMG1655"
            "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
            "\t3000000\tHIPA\tD139A\t24-07-12"
            "\t24-07-12_HIPA_HIPA-D139A_SVIR_SVIR-H52A_DISA_DISA-D433A.png"
            "\t5\t4\t\t400000\t0.8750612634"
        ),
        "notes": (
            "The final Science supplementary Table S7 System Mutants sheet "
            "pairs wild-type HIPA and HIPA D139A in a Bas1 assay panel, with "
            "-log(EOP) shifting from 5.176 to 0.875 for the D139A catalytic "
            "mutant."
        ),
    }


def table_s7_d139a_panel_b_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\tB.1\tMG1655\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t3000000\tHIPA\t\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t2\t10\t\t1000\t3.477121255\n"
            "Bas1\tB.1\tMG1655\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t3000000\tHIPA\tD139A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t6\t4\t\t4000000\t-0.1249387366"
        ),
        "notes": (
            "The final Science supplementary Table S7 System Mutants sheet "
            "records a second HIPA versus HIPA D139A Bas1 panel, with "
            "-log(EOP) shifting from 3.477 to -0.125 for the D139A catalytic "
            "mutant."
        ),
    }


def all_d139a_evidence() -> list[dict[str, str]]:
    return [table_s7_d139a_panel_a_evidence(), table_s7_d139a_panel_b_evidence()]


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "HIPA\tDS-6\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps HIPA to "
            "replicated display name DS-6."
        ),
    }


def table_s8_hipa_kinase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "HIPA\t15.0\t248.0\tWP_000389051.1\tHIPA kinase"
            "\tPF20613.3\tHipA_2 ; HipA-like kinase\thhpred_9120093.hhr"
            "\t15.0\t248.0\t1.0\t2024-07-28 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a HipA-like "
            "kinase HHpred hit for WP_000389051.1 in HIPA."
        ),
    }


def table_s8_duf3037_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "HIPA\t2.0\t275.0\tWP_000210934.1\tDUF3037\tPF11236.12"
            "\tDUF3037\thhpred_4386604.hhr\t7.0\t125.0\t0.9987"
            "\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a DUF3037 "
            "HHpred hit for WP_000210934.1 in HIPA."
        ),
    }


def table_s8_duf1829_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "HIPA\t2.0\t275.0\tWP_000210934.1\tDUF1829\tPF08862.14"
            "\tDUF1829\thhpred_4386604.hhr\t163.0\t260.0\t0.7785"
            "\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a DUF1829 "
            "HHpred hit for WP_000210934.1 in HIPA."
        ),
    }


def all_domain_evidence() -> list[dict[str, str]]:
    return [
        table_s8_hipa_kinase_evidence(),
        table_s8_duf3037_evidence(),
        table_s8_duf1829_evidence(),
    ]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-6 system",
    "definition": (
        "A phage defense system in which an organism possesses the two-gene "
        "DefensePredictor-discovered system 6 locus cataloged with working_id "
        "HIPA and whose plasmid expression in E. coli MG1655 reduced "
        "bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-6",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "HipAD",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "HIPA",
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
        {
            "reference": DEWEIRDT,
            "snippet": DS_HIPAD_SNIPPET,
            "notes": "DeWeirdt et al. record HipAD as a name for DS-6.",
        },
        {
            "reference": DEWEIRDT,
            "snippet": DS_D139A_SNIPPET,
            "notes": (
                "DeWeirdt et al. report that mutating a predicted DS-6A "
                "catalytic residue eliminated defense."
            ),
        },
        table_s6_evidence(),
        table_s7_evidence(),
        *all_d139a_evidence(),
        table_s8_display_evidence(),
        *all_domain_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_6_locus_reduces_phage_plaquing",
            "title": "DS-6 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-6 locus to reduced bacteriophage plaquing without "
                "resolving DS-6 component functions or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-6 as the validated HIPA "
                "transcriptional unit with two product accessions and with "
                "DefenseFinder DS-6A and DS-6B profile rows. It does not "
                "assert native host breadth, exact profile-to-protein "
                "correspondence, the direct viral trigger or substrate, "
                "DUF3037 or DUF1829 activity, exact HipA-like kinase "
                "substrates, phage target breadth, or DefenseFinder "
                "rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_6_locus",
                    "label": "DS-6 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by DS-6A and DS-6B custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas1 in cells carrying cloned HIPA."
                    ),
                },
                {
                    "node_id": "ds_6_system_trait",
                    "label": "DS-6 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-6 phage-defense "
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
                    "subject": "ds_6_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-6/HIPA locus contributes to reduced "
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
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_D139A_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. report that DS-6A catalytic "
                                "residue mutagenesis caused loss of defense."
                            ),
                        },
                        *all_d139a_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_6_system_trait",
                    "description": (
                        "DS-6-mediated phage plaquing reduction realizes the "
                        "DS-6 system trait."
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
                    "subject": "ds_6_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-6 system possession is a phage-defense-system "
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
            "discussion_id": "ds-6-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-6 native host breadth, exact two-component "
                "activities, DS-6 profile-to-protein mapping, sensitive-"
                "phage breadth, DUF3037 and DUF1829 activity, HipA-like "
                "kinase substrates, and rule-level detection criteria before "
                "minting narrower DS-6 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-6 as the defensive HIPA "
                "transcriptional unit that reduced Bas1 plaquing when "
                "cloned in E. coli MG1655, and the pinned DefenseFinder HMM "
                "inventory records two DS-6 profile rows. The pinned rules "
                "table has no DS-6 row, and the first-pass record does not "
                "resolve native host breadth, exact profile-to-protein "
                "correspondence, DUF3037 or HipA-like kinase activity, "
                "phage target breadth, or endogenous DS-6 activity."
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
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_HIPAD_SNIPPET,
                    "notes": "DeWeirdt et al. record HipAD as a DS-6 name.",
                },
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_D139A_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. report loss of defense after "
                        "mutation of a predicted DS-6A catalytic residue."
                    ),
                },
                table_s6_evidence(),
                table_s7_evidence(),
                *all_d139a_evidence(),
                table_s8_display_evidence(),
                *all_domain_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-6, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_6_locus_reduces_phage_plaquing"],
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
            "Minted DS-6 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned HIPA "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-6 HMM rows are not backed by a rules row; "
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
            "Reviewed DS-6 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned HIPA plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-6 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-6 activity. No paid "
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
