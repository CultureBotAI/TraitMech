#!/usr/bin/env python3
"""Add the DS-42 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_42_system.yaml"

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
TIMESTAMP = "2026-09-29T13:30:52Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T13:30:53Z"

IDENTIFIER = "traitmech:000464"
PROPOSAL = "proposals/metpo_traitmech_v341"

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
    "| DS-42 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROWS = {
    "DS-42__DS-42A": (
        "| DS-42__DS-42A                                    |"
        "                                                  | DS-42"
        "                  | Custom                  | 70     |"
    ),
    "DS-42__DS-42B": (
        "| DS-42__DS-42B                                    |"
        "                                                  | DS-42"
        "                  | Custom                  | 20     |"
    ),
    "DS-42__DS-42C": (
        "| DS-42__DS-42C                                    |"
        "                                                  | DS-42"
        "                  | Custom                  | 200    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-42 "
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
            f"{profile} as a custom DS-42 profile."
        ),
    }


def all_hmm_inventory_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_ROWS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "PRO1\tNZ_QOXO01000016.1\tGCF_003334005.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t661\t3061"
            "\tMBL fold metallo-hydrolase, hypothetical protein, "
            "hypothetical protein\tWP_001198055.1, WP_001024069.1, "
            "WP_249925928.1\t4.870544869418898\t6.906754778648663"
            "\tTrue\tTrue\tPredicted novel defense gene\tDS-42"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "PRO1 to DS_name DS-42, marks the cloned transcriptional unit "
            "as defensive, and records NZ_QOXO01000016.1 positions "
            "661-3061 with product accessions WP_001198055.1, "
            "WP_001024069.1, and WP_249925928.1."
        ),
    }


def table_s7_bas1_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t3.1\tpLAND\t24-04-10_CITO_AAA3_FDRT_EV.png"
            "\t5000000\tPRO1\t24-04-13"
            "\t24-04-13_PRO1_CBT2_AAA4_TMRA.png\t5\t4\tY\t400000"
            "\t1.0969100130080565\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports a PRO1 assay row with a Bas1 phage readout and a "
            "-log(EOP) value of 1.097."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "PRO1\tDS-42\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps PRO1 to "
            "replicated display name DS-42."
        ),
    }


def table_s8_mbl_hydrolase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PRO1\t3.0\t363.0\tWP_001198055.1\tMBL hydrolase\tcd07731"
            "\tComA-like_MBL-fold; Competence protein ComA, ComEC and "
            "related proteins\thhpred_9048500.hhr\t12.0\t251.0"
            "\t0.998\t2024-04-15 00:00:00\t\t"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability MBL hydrolase HHpred hit for "
            "WP_001198055.1 in PRO1."
        ),
    }


def table_s8_dimerization_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PRO1\t2.0\t190.0\tWP_001024069.1\tDimerization\tPF16892.9"
            "\tCHS5_N ; Chitin biosynthesis protein CHS5 N-terminus"
            "\thhpred_3514574.hhr\t108.0\t166.0\t0.7787"
            "\t2024-04-15 00:00:00\t\t"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "moderate-probability CHS5_N/Dimerization HHpred hit for "
            "WP_001024069.1 in PRO1."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-42 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "three-gene DefensePredictor-discovered system 42 locus cataloged "
        "as working transcriptional unit PRO1 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-42",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "PRO1",
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
        table_s7_bas1_evidence(),
        table_s8_display_evidence(),
        table_s8_mbl_hydrolase_evidence(),
        table_s8_dimerization_evidence(),
        article_registry_evidence(),
        *all_hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_42_locus_reduces_phage_plaquing",
            "title": "DS-42 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the three-gene "
                "DS-42 locus to reduced bacteriophage plaquing without "
                "resolving DS-42 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-42 as the validated PRO1 "
                "transcriptional unit with three product accessions, a "
                "high-probability MBL hydrolase HHpred row for "
                "WP_001198055.1, a moderate-probability CHS5_N/Dimerization "
                "HHpred row for WP_001024069.1, and three DefenseFinder "
                "DS-42 profile rows. It does not assert native host breadth, "
                "exact profile-to-protein correspondence, MBL hydrolase or "
                "CHS5_N interpretation, WP_249925928.1 function, DS-42 "
                "molecular activity, complete phage breadth, or DefenseFinder "
                "rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_42_locus",
                    "label": "DS-42 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene DefensePredictor-discovered system 42 "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by three DS-42 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned PRO1."
                    ),
                },
                {
                    "node_id": "ds_42_system_trait",
                    "label": "DS-42 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-42 phage-defense "
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
                    "subject": "ds_42_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-42/PRO1 locus contributes to reduced "
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
                        table_s7_bas1_evidence(),
                        table_s8_display_evidence(),
                        table_s8_mbl_hydrolase_evidence(),
                        table_s8_dimerization_evidence(),
                        *all_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_42_system_trait",
                    "description": (
                        "DS-42-mediated phage plaquing reduction realizes "
                        "the DS-42 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas1_evidence(),
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
                    "subject": "ds_42_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-42 system possession is a phage-defense-system "
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
            "discussion_id": "ds-42-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-42 native host breadth, exact component "
                "activity, profile-to-protein mapping, MBL hydrolase and "
                "CHS5_N interpretations, WP_249925928.1 function, complete "
                "phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-42 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-42 as the defensive PRO1 "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to three product accessions, a Bas1 phage readout, "
                "display name DS-42, a high-probability MBL hydrolase "
                "HHpred row, and a moderate-probability CHS5_N/Dimerization "
                "HHpred row. The pinned DefenseFinder HMM inventory records "
                "three DS-42 custom profile rows. The pinned rules table "
                "has no DS-42 row, and the first-pass record does not "
                "resolve native host breadth, complete phage breadth, "
                "direct profile-to-protein correspondence, component "
                "activities, molecular output, or endogenous DS-42 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas1_evidence(),
                table_s8_display_evidence(),
                table_s8_mbl_hydrolase_evidence(),
                table_s8_dimerization_evidence(),
                article_registry_evidence(),
                *all_hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-42, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_42_locus_reduces_phage_plaquing"],
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
            "Minted DS-42 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at PRO1 "
            "transcriptional-unit level because component activities and "
            "rule rows remain unresolved, and "
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
            "Reviewed DS-42 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned PRO1 assays "
            "in E. coli MG1655 and a DefenseFinder DS-42 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-42 activity. No paid "
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
