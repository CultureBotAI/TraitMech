#!/usr/bin/env python3
"""Add the DS-17 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_17_system.yaml"

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
TIMESTAMP = "2026-09-28T18:12:47Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T18:12:48Z"

IDENTIFIER = "traitmech:000440"
PROPOSAL = "proposals/metpo_traitmech_v317"

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
    "| DS-17 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-17__DS-17                                     |"
    "                                                  | DS-17"
    "                  | Custom                  | 300    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-17 "
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
            "The pinned DefenseFinder HMM inventory records DS-17__DS-17 "
            "as a custom DS-17 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "NUCS\tNZ_QOYO01000009.1\tGCF_003333605.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t23399\t24397"
            "\thypothetical protein\tWP_001240354.1\t13.60450880206783"
            "\t3.377690933986817\tTrue\tTrue\tPredicted novel defense gene"
            "\tDS-17"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id NUCS "
            "to DS_name DS-17, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOYO01000009.1 positions "
            "23399-24397 with product accession WP_001240354.1."
        ),
    }


def table_s7_t4_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T4\t6.2\tpLAND\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tNUCS\t24-07-17"
            "\t24-07-17_NERD_MVB1_RMOR_NUCS.png\t2\t10\t\t1000"
            "\t4.301029995663981\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a NUCS "
            "assay row with a T4 phage readout and a -log(EOP) value of "
            "4.301."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "NUCS\tDS-17\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps NUCS to "
            "replicated display name DS-17."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "NUCS\t1.0\t332.0\tWP_001240354.1\tPDDEXK\tPF01939.21"
            "\tNucS_C ; Endonuclease NucS C-terminal domain"
            "\thhpred_4156604.hhr\t25.0\t181.0\t0.993"
            "\t2024-07-27 00:00:00\t412-414\t398.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a PDDEXK "
            "HHpred hit for WP_001240354.1 in NUCS."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-17 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 17 locus cataloged "
        "as working transcriptional unit NUCS and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-17",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "NUCS",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-17__DS-17",
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
        table_s7_t4_evidence(),
        table_s8_display_evidence(),
        table_s8_pddexk_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_17_locus_reduces_phage_plaquing",
            "title": "DS-17 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-17 locus to reduced bacteriophage plaquing without "
                "resolving DS-17 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-17 as the validated NUCS "
                "transcriptional unit with one product accession, one "
                "PDDEXK HHpred-domain row, and one DefenseFinder DS-17 "
                "profile row. It does not assert native host breadth, "
                "exact profile-to-protein correspondence, DS-17 molecular "
                "activity, trigger, substrate, phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_17_locus",
                    "label": "DS-17 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "17 locus represented in the pinned DefenseFinder "
                        "HMM inventory by one DS-17 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned NUCS."
                    ),
                },
                {
                    "node_id": "ds_17_system_trait",
                    "label": "DS-17 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-17 phage-defense "
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
                    "subject": "ds_17_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-17/NUCS locus contributes to reduced "
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
                        table_s7_t4_evidence(),
                        table_s8_display_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_17_system_trait",
                    "description": (
                        "DS-17-mediated phage plaquing reduction realizes "
                        "the DS-17 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_t4_evidence(),
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
                    "subject": "ds_17_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-17 system possession is a phage-defense-system "
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
            "discussion_id": "ds-17-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-17 native host breadth, exact "
                "profile-to-protein mapping, component chemistry, "
                "sensitive-phage breadth, molecular output, and "
                "rule-level DefenseFinder criteria before minting narrower "
                "DS-17 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-17 as the defensive NUCS "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to product accession WP_001240354.1, a T4 phage "
                "readout, display name DS-17, and a PDDEXK HHpred row. "
                "The pinned DefenseFinder HMM inventory records one "
                "DS-17 custom profile row. The pinned rules table has no "
                "DS-17 row, and the first-pass record does not resolve "
                "native host breadth, phage breadth, direct "
                "profile-to-protein correspondence, PDDEXK nuclease "
                "activity, molecular output, or endogenous DS-17 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_t4_evidence(),
                table_s8_display_evidence(),
                table_s8_pddexk_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-17, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_17_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-28",
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
            "Minted DS-17 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at NUCS "
            "transcriptional-unit level because PDDEXK chemistry and rule "
            f"rows remain unresolved, and {PROPOSAL} reserves the "
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
            "Reviewed DS-17 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned NUCS assays in "
            "E. coli MG1655 and a DefenseFinder DS-17 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-17 activity. No paid "
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
