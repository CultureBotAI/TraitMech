#!/usr/bin/env python3
"""Add the DS-23 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_23_system.yaml"

DEWEIRDT = "DOI:10.1126/science.adv7924"

PMC_S3_PREFIX = "https://pmc-oa-opendata.s3.amazonaws.com/PMC13092281.1/"
TABLE_S6 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S6.xlsx"
TABLE_S7 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S7.xlsx"
TABLE_S8 = f"{PMC_S3_PREFIX}NIHMS2163519-supplement-Table_S8.xlsx"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-29T00:59:43Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T00:59:44Z"

IDENTIFIER = "traitmech:000448"
PROPOSAL = "proposals/metpo_traitmech_v325"

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
    "| DS-23 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-23__DS-23                                     |"
    "                                                  | DS-23"
    "                  | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-23 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DS-23__DS-23 "
            "as a custom DS-23 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "E2DP\tNZ_RRVV01000032.1\tGCF_003886345.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t38754\t40913"
            "\tSEC-C metal-binding domain-containing protein"
            "\tWP_020231147.1\t11.17818080568115\t3.842009204807092"
            "\tTrue\tTrue\tPredicted novel defense gene\tDS-23"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id E2DP "
            "to DS_name DS-23, marks the cloned transcriptional unit as "
            "defensive, and records NZ_RRVV01000032.1 positions "
            "38754-40913 with product accession WP_020231147.1."
        ),
    }


def table_s7_bas19_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas19\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t2200000\tE2DP\t24-07-24"
            "\t24-07-24_ABIL_E2DP_COAT_DDML.png\t0\t1\t\t1"
            "\t6.342422680822207\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an E2DP "
            "assay row with a Bas19 phage readout and a -log(EOP) value "
            "of 6.342."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "E2DP\tDS-23\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps E2DP to "
            "replicated display name DS-23."
        ),
    }


def table_s8_zf_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "E2DP\t1.0\t719.0\tWP_020231147.1\tZF\t2I9W_A"
            "\tHypothetical protein; Cystatin-like fold, sec-c motif fold, "
            "structural genomics\thhpred_7846250.hhr\t693.0\t716.0"
            "\t0.98\t2024-07-30 00:00:00\t\t"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a ZF "
            "HHpred hit for WP_020231147.1 in E2DP."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "E2DP\t1.0\t719.0\tWP_020231147.1\tPDDEXK\tcd22364"
            "\tVC1899-like; putative nuclease domain found in Vibrio "
            "cholerae VC1899 and similar proteins. A putative nuclease "
            "domain found in Vibrio cholerae VC1899 and similar proteins "
            "belongs to a superfamily of PDDEXK nucleases"
            "\thhpred_7846250.hhr\t295.0\t457.0\t0.96"
            "\t2024-07-30 00:00:00\t110-112\t96.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a PDDEXK "
            "HHpred hit for WP_020231147.1 in E2DP."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_zf_evidence(), table_s8_pddexk_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-23 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 23 locus cataloged "
        "as working transcriptional unit E2DP and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-23",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "E2DP",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-23__DS-23",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
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
        table_s7_bas19_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_23_locus_reduces_phage_plaquing",
            "title": "DS-23 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-23 locus to reduced bacteriophage plaquing without "
                "resolving DS-23 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-23 as the validated E2DP "
                "transcriptional unit with one product accession, ZF and "
                "PDDEXK HHpred-domain rows, and one DefenseFinder DS-23 "
                "profile row. It does not assert native host breadth, "
                "exact profile-to-protein correspondence, DS-23 molecular "
                "activity, trigger, substrate, complete phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_23_locus",
                    "label": "DS-23 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "23 locus represented in the pinned DefenseFinder "
                        "HMM inventory by one DS-23 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned E2DP."
                    ),
                },
                {
                    "node_id": "ds_23_system_trait",
                    "label": "DS-23 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-23 phage-defense "
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
                    "subject": "ds_23_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-23/E2DP locus contributes to reduced "
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
                        table_s7_bas19_evidence(),
                        table_s8_display_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_23_system_trait",
                    "description": (
                        "DS-23-mediated phage plaquing reduction realizes "
                        "the DS-23 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas19_evidence(),
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
                    "subject": "ds_23_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-23 system possession is a phage-defense-system "
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
            "discussion_id": "ds-23-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-23 native host breadth, exact "
                "single-component activity, profile-to-protein mapping, "
                "ZF and PDDEXK HHpred-domain interpretation, complete "
                "phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-23 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-23 as the defensive E2DP "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to product accession WP_020231147.1, a Bas19 "
                "phage readout, display name DS-23, and ZF and PDDEXK "
                "HHpred rows. The pinned DefenseFinder HMM inventory "
                "records one DS-23 custom profile row. The pinned rules "
                "table has no DS-23 row, and the first-pass record does "
                "not resolve native host breadth, complete phage breadth, "
                "direct profile-to-protein correspondence, ZF or PDDEXK "
                "activity, molecular output, or endogenous DS-23 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas19_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-23, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_23_locus_reduces_phage_plaquing"],
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
            "Minted DS-23 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at E2DP "
            "transcriptional-unit level because ZF and PDDEXK chemistry "
            "and rule rows remain unresolved, and "
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
            "Reviewed DS-23 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned E2DP assays "
            "in E. coli MG1655 and a DefenseFinder DS-23 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-23 activity. No paid "
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
