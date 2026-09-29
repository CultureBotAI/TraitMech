#!/usr/bin/env python3
"""Add the DS-32 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    emit_trait_yaml,
    write_validated_trait,
)

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_32_system.yaml"

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
TIMESTAMP = "2026-09-29T07:25:23Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T07:25:24Z"

IDENTIFIER = "traitmech:000455"
PROPOSAL = "proposals/metpo_traitmech_v332"

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
    "| DS-32 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROWS = {
    "DS-32__DS-32A": (
        "| DS-32__DS-32A                                    |"
        "                                                  | DS-32"
        "                  | Custom                  | 150    |"
    ),
    "DS-32__DS-32B": (
        "| DS-32__DS-32B                                    |"
        "                                                  | DS-32"
        "                  | Custom                  | 210    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-32 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            f"{profile} as a custom DS-32 profile."
        ),
    }


def all_hmm_inventory_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_ROWS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "NADR\tNZ_QOXQ01000027.1\tGCF_003333945.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t48629\t50261"
            "\thypothetical protein, NADAR family protein"
            "\tWP_000097610.1, WP_032260665.1\t9.822610074734904"
            "\t6.906754778648663\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-32"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id NADR "
            "to DS_name DS-32, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOXQ01000027.1 positions "
            "48629-50261 with product accessions WP_000097610.1 and "
            "WP_032260665.1."
        ),
    }


def table_s7_bas26_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas26\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t500000000\tNADR\t24-03-12"
            "\t24-03-12_SVIR_PIN8_NTTI_NADR.png\t4\t10\tY\t100000"
            "\t3.6989700043360187\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a NADR "
            "assay row with a Bas26 phage readout and a -log(EOP) value "
            "of 3.699."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "NADR\tDS-32\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps NADR to "
            "replicated display name DS-32."
        ),
    }


def table_s8_recr_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "NADR\t1.0\t343.0\tWP_000097610.1\tRecR\t8K3F_A"
            "\tRecombination protein RecR; Recombination mediator protein"
            "\thhpred_1157231.hhr\t1.0\t65.0\t0.6827"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "lower-probability RecR HHpred hit for WP_000097610.1 in "
            "NADR."
        ),
    }


def table_s8_prtase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "NADR\t1.0\t343.0\tWP_000097610.1\tPRTase\t3DMP_D"
            "\tUracil phosphoribosyltransferase\thhpred_1157231.hhr"
            "\t129.0\t196.0\t0.942\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability PRTase HHpred hit for WP_000097610.1 in "
            "NADR."
        ),
    }


def table_s8_nadar_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "NADR\t2.0\t203.0\tWP_032260665.1\tNADAR\tPF08719.15"
            "\tNADAR ; NADAR domain\thhpred_3126143.hhr\t13.0\t159.0"
            "\t0.9992\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability NADAR HHpred hit for WP_032260665.1 in "
            "NADR."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [
        table_s8_recr_evidence(),
        table_s8_prtase_evidence(),
        table_s8_nadar_evidence(),
    ]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-32 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DefensePredictor-discovered system 32 locus cataloged "
        "as working transcriptional unit NADR and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-32",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "NADR",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
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
        table_s7_bas26_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_32_locus_reduces_phage_plaquing",
            "title": "DS-32 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-32 locus to reduced bacteriophage plaquing without "
                "resolving DS-32 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-32 as the validated NADR "
                "transcriptional unit with two product accessions, "
                "lower-probability RecR and high-probability PRTase "
                "HHpred rows for WP_000097610.1, a high-probability NADAR "
                "HHpred row for WP_032260665.1, and two DefenseFinder "
                "DS-32 profile rows. It does not assert native host "
                "breadth, exact profile-to-protein correspondence, DS-32 "
                "molecular activity, trigger, substrate, complete phage "
                "breadth, RecR, PRTase, or NADAR HHpred-domain "
                "interpretation, or DefenseFinder rule-level detection "
                "criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_32_locus",
                    "label": "DS-32 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system "
                        "32 locus represented in the pinned DefenseFinder "
                        "HMM inventory by two DS-32 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned NADR."
                    ),
                },
                {
                    "node_id": "ds_32_system_trait",
                    "label": "DS-32 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-32 phage-defense "
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
                    "subject": "ds_32_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-32/NADR locus contributes to reduced "
                        "bacteriophage plaquing in heterologous E. coli "
                        "MG1655 plasmid-expression assays."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_VALIDATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. describe the "
                                "plasmid-based phage challenge used to "
                                "validate predicted transcriptional units."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_bas26_evidence(),
                        table_s8_display_evidence(),
                        *all_hhpred_evidence(),
                        *all_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_32_system_trait",
                    "description": (
                        "DS-32-mediated phage plaquing reduction realizes "
                        "the DS-32 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas26_evidence(),
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
                    "subject": "ds_32_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-32 system possession is a phage-defense-system "
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
            "discussion_id": "ds-32-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-32 native host breadth, exact component "
                "activities, profile-to-protein mapping, RecR, PRTase, and "
                "NADAR HHpred-domain interpretation, complete phage "
                "breadth, molecular output, and rule-level DefenseFinder "
                "criteria before minting narrower DS-32 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-32 as the defensive NADR "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to two product accessions, a Bas26 phage readout, "
                "display name DS-32, and three HHpred rows. The pinned "
                "DefenseFinder HMM inventory records two DS-32 custom "
                "profile rows. The pinned rules table has no DS-32 row, "
                "and the first-pass record does not resolve native host "
                "breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, component activities, "
                "molecular output, or endogenous DS-32 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas26_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-32, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_32_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-29",
        }
    ],
}


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


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
            "Minted DS-32 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at NADR "
            "transcriptional-unit level because RecR, PRTase, NADAR "
            "activity and rule rows remain unresolved, and "
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
            "Reviewed DS-32 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned NADR assays "
            "in E. coli MG1655 and a DefenseFinder DS-32 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-32 activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    validate_output(record)

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"Wrote {rel}")
    else:
        sys.stdout.write(emit_trait_yaml(record))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
