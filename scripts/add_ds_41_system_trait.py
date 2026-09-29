#!/usr/bin/env python3
"""Add the DS-41 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_41_system.yaml"

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
TIMESTAMP = "2026-09-29T12:49:10Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T12:49:11Z"

IDENTIFIER = "traitmech:000463"
PROPOSAL = "proposals/metpo_traitmech_v340"

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
    "| DS-41 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-41__DS-41                                     |"
    "                                                  | DS-41"
    "                  | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-41 "
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
            "The pinned DefenseFinder HMM inventory records DS-41__DS-41 "
            "as a custom DS-41 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "AAA2\tNZ_QOYD01000024.1\tGCF_003333765.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t5322\t6830"
            "\thypothetical protein\tWP_033812887.1"
            "\t7.980074950371131\t4.119037174812478\tTrue\tTrue"
            "\tRemote defense homolog\tDS-41"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "AAA2 to DS_name DS-41, marks the cloned transcriptional unit "
            "as defensive, and records NZ_QOYD01000024.1 positions "
            "5322-6830 with product accession WP_033812887.1."
        ),
    }


def table_s7_bas1_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t3000000\tAAA2\t24-07-17"
            "\t24-07-17_AAA2_RMOR_NERD_NUCS.png\t1\t3\t\t30"
            "\t5\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports an AAA2 assay row with a Bas1 phage readout and a "
            "-log(EOP) value of 5."
        ),
    }


def table_s7_t4_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T4\t6.2\tpLAND\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tAAA2\t24-07-17"
            "\t24-07-17_AAA2_VPUS_VAME_EV.png\t1\t10\t\t100"
            "\t5.301029995663981\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports an AAA2 assay row with a T4 phage readout and a "
            "-log(EOP) value of 5.301."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "AAA2\tDS-41\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps AAA2 to "
            "replicated display name DS-41."
        ),
    }


def table_s8_aaa_atpase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "AAA2\t1.0\t502.0\tWP_033812887.1\tAAA+ ATPase\t2QBY_A"
            "\tCell division control protein 6 homolog 1; "
            "winged-helix domain, helix-turn-helix, AAA+ ATPase domain"
            "\thhpred_7261390.hhr\t8.0\t488.0\t0.996"
            "\t2024-07-29 00:00:00\t\t"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability AAA+ ATPase HHpred hit for WP_033812887.1 "
            "in AAA2."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-41 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 41 locus cataloged "
        "as working transcriptional unit AAA2 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-41",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "AAA2",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-41__DS-41",
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
        table_s7_bas1_evidence(),
        table_s7_t4_evidence(),
        table_s8_display_evidence(),
        table_s8_aaa_atpase_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_41_locus_reduces_phage_plaquing",
            "title": "DS-41 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-41 locus to reduced bacteriophage plaquing without "
                "resolving DS-41 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-41 as the validated AAA2 "
                "transcriptional unit with one product accession, one "
                "high-probability AAA+ ATPase HHpred row for "
                "WP_033812887.1, and one DefenseFinder DS-41 profile row. "
                "It does not assert exact profile-to-protein "
                "correspondence, AAA+ ATPase activity, native host breadth, "
                "DS-41 molecular output, complete phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_41_locus",
                    "label": "DS-41 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "41 locus represented in the pinned DefenseFinder "
                        "HMM inventory by one DS-41 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned AAA2."
                    ),
                },
                {
                    "node_id": "ds_41_system_trait",
                    "label": "DS-41 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-41 phage-defense "
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
                    "subject": "ds_41_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-41/AAA2 locus contributes to reduced "
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
                        table_s7_t4_evidence(),
                        table_s8_display_evidence(),
                        table_s8_aaa_atpase_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_41_system_trait",
                    "description": (
                        "DS-41-mediated phage plaquing reduction realizes "
                        "the DS-41 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas1_evidence(),
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
                    "subject": "ds_41_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-41 system possession is a phage-defense-system "
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
            "discussion_id": "ds-41-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-41 native host breadth, exact component "
                "activity, profile-to-protein mapping, AAA+ ATPase "
                "interpretation, complete phage breadth, molecular output, "
                "and rule-level DefenseFinder criteria before minting "
                "narrower DS-41 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-41 as the defensive AAA2 "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to one product accession, Bas1 and T4 phage "
                "readouts, display name DS-41, and a high-probability AAA+ "
                "ATPase HHpred row. The pinned DefenseFinder HMM inventory "
                "records one DS-41 custom profile row. The pinned rules "
                "table has no DS-41 row, and the first-pass record does "
                "not resolve native host breadth, complete phage breadth, "
                "direct profile-to-protein correspondence, AAA+ ATPase "
                "activity, molecular output, or endogenous DS-41 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas1_evidence(),
                table_s7_t4_evidence(),
                table_s8_display_evidence(),
                table_s8_aaa_atpase_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-41, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_41_locus_reduces_phage_plaquing"],
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
            "Minted DS-41 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at AAA2 "
            "transcriptional-unit level because AAA+ ATPase activity and "
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
            "Reviewed DS-41 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned AAA2 assays "
            "in E. coli MG1655 and a DefenseFinder DS-41 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-41 activity. No paid "
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
