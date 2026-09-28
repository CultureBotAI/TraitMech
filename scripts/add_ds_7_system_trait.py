#!/usr/bin/env python3
"""Add the DS-7 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_7_system.yaml"

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
TIMESTAMP = "2026-09-28T09:58:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T09:58:01Z"

IDENTIFIER = "traitmech:000431"
PROPOSAL = "proposals/metpo_traitmech_v308"

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
    "| DS-7 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-7__DS-7": (
        "| DS-7__DS-7                                       |"
        "                                                  | DS-7"
        "                   | Custom                  | 200    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-7 "
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
            "custom DS-7 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "SVIR\tNZ_QOYF01000007.1\tGCF_003334585.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t310084\t311190"
            "\tDUF2634 domain-containing protein\tWP_225403053.1"
            "\t5.785481186679323\t3.623314765621056\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-7"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id SVIR "
            "to DS_name DS-7, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOYF01000007.1 positions "
            "310084-311190 with product accession WP_225403053.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas60\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t5000000\tSVIR\t24-03-12"
            "\t24-03-12_SVIR_PIN8_NTTI_NADR.png\t2\t100\t\t10000"
            "\t2.6989700043360187\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an SVIR assay "
            "row with a Bas60 phage readout and a -log(EOP) value of 2.699."
        ),
    }


def table_s7_h52a_panel_a_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas60\tA.1\tMG1655"
            "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
            "\t3000000\tSVIR\t\t24-07-12"
            "\t24-07-12_HIPA_HIPA-D139A_SVIR_SVIR-H52A_DISA_DISA-D433A.png"
            "\t4\t14\t\t140000\t1.330993219\n"
            "Bas60\tA.1\tMG1655"
            "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
            "\t3000000\tSVIR\tH52A\t24-07-12"
            "\t24-07-12_HIPA_HIPA-D139A_SVIR_SVIR-H52A_DISA_DISA-D433A.png"
            "\t5\t10\t\t1000000\t0.4771212547"
        ),
        "notes": (
            "The final Science supplementary Table S7 System Mutants sheet "
            "pairs wild-type SVIR and SVIR H52A in a Bas60 assay panel, with "
            "-log(EOP) shifting from 1.331 to 0.477 for the H52A mutant."
        ),
    }


def table_s7_h52a_panel_b_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas60\tB.1\tMG1655\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t400000\tSVIR\t\t24-07-18"
            "\t24-07-18_DISA-R468A_DISA_SVIR_DISA-D433A_SVIR-H52A.png"
            "\t0\t1\t\t1\t5.602059991\n"
            "Bas60\tB.1\tMG1655\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t400000\tSVIR\tH52A\t24-07-18"
            "\t24-07-18_DISA-R468A_DISA_SVIR_DISA-D433A_SVIR-H52A.png"
            "\t4\t22\t\t220000\t0.2596373105"
        ),
        "notes": (
            "The final Science supplementary Table S7 System Mutants sheet "
            "records a second SVIR versus SVIR H52A Bas60 panel, with "
            "-log(EOP) shifting from 5.602 to 0.260 for the H52A mutant."
        ),
    }


def all_h52a_evidence() -> list[dict[str, str]]:
    return [table_s7_h52a_panel_a_evidence(), table_s7_h52a_panel_b_evidence()]


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "SVIR\tDS-7\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps SVIR to "
            "replicated display name DS-7."
        ),
    }


def table_s8_hnh_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "SVIR\t1.0\t368.0\tWP_225403053.1\tHNH endonuclease"
            "\t7RWK_A\tSAVED domain-containing protein; DNA nuclease "
            "SAVED Sensor Effector\thhpred_1710432.hhr\t5.0\t122.0"
            "\t0.99\t2024-04-17 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports an HNH "
            "endonuclease HHpred hit for WP_225403053.1 in SVIR."
        ),
    }


def table_s8_phage_baseplate_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "SVIR\t1.0\t368.0\tWP_225403053.1\tPhage baseplate\t8ENV_M"
            "\tSheath initiator gp34; Pseudomonas, phage, baseplate"
            "\thhpred_1710432.hhr\t225.0\t350.0\t0.99"
            "\t2024-04-17 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "phage-baseplate-like HHpred hit for WP_225403053.1 in SVIR."
        ),
    }


def all_domain_evidence() -> list[dict[str, str]]:
    return [table_s8_hnh_evidence(), table_s8_phage_baseplate_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-7 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 7 locus cataloged "
        "with working_id SVIR and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-7",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "SVIR",
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
        *all_h52a_evidence(),
        table_s8_display_evidence(),
        *all_domain_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_7_locus_reduces_phage_plaquing",
            "title": "DS-7 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-7 locus to reduced bacteriophage plaquing without "
                "resolving DS-7 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-7 as the validated SVIR "
                "transcriptional unit with one product accession and with a "
                "DefenseFinder DS-7 profile row. It does not assert native "
                "host breadth, exact profile-to-protein correspondence, the "
                "direct viral trigger or substrate, the exact HNH "
                "endonuclease activity, phage-baseplate-like domain "
                "relevance, phage target breadth, or DefenseFinder "
                "rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_7_locus",
                    "label": "DS-7 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-7 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas60 in cells carrying cloned SVIR."
                    ),
                },
                {
                    "node_id": "ds_7_system_trait",
                    "label": "DS-7 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-7 phage-defense "
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
                    "subject": "ds_7_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-7/SVIR locus contributes to reduced "
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
                        *all_h52a_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_7_system_trait",
                    "description": (
                        "DS-7-mediated phage plaquing reduction realizes "
                        "the DS-7 system trait."
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
                    "subject": "ds_7_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-7 system possession is a phage-defense-system "
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
            "discussion_id": "ds-7-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-7 native host breadth, exact single-component "
                "activity, DS-7 profile-to-protein mapping, sensitive-phage "
                "breadth, HNH endonuclease activity, the role of the H52 "
                "residue, the phage-baseplate-like hit, and rule-level "
                "detection criteria before minting narrower DS-7 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-7 as the defensive SVIR "
                "transcriptional unit that reduced Bas60 plaquing when "
                "cloned in E. coli MG1655, and the pinned DefenseFinder HMM "
                "inventory records one DS-7 profile row. The pinned rules "
                "table has no DS-7 row, and the first-pass record does not "
                "resolve native host breadth, exact profile-to-protein "
                "correspondence, HNH endonuclease activity, the function of "
                "the H52 residue, phage target breadth, or endogenous DS-7 "
                "activity."
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
                *all_h52a_evidence(),
                table_s8_display_evidence(),
                *all_domain_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-7, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_7_locus_reduces_phage_plaquing"],
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
            "Minted DS-7 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned SVIR "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-7 HMM row is not backed by a rules row; "
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
            "Reviewed DS-7 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned SVIR plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-7 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-7 activity. No paid "
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
