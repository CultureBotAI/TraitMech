#!/usr/bin/env python3
"""Add the DS-38 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_38_system.yaml"

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
TIMESTAMP = "2026-09-29T10:59:36Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T10:59:37Z"

IDENTIFIER = "traitmech:000460"
PROPOSAL = "proposals/metpo_traitmech_v337"

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
    "| DS-38 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-38__DS-38                                     |"
    "                                                  | DS-38"
    "                  | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-38 "
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
            "The pinned DefenseFinder HMM inventory records DS-38__DS-38 "
            "as a custom DS-38 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "HEP2\tNZ_QOYR01000034.1\tGCF_003333645.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t8089\t9189"
            "\thypothetical protein\tWP_001313577.1\t8.026493157403"
            "\t2.649821696202418\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-38"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "HEP2 to DS_name DS-38, marks the cloned transcriptional unit "
            "as defensive, and records NZ_QOYR01000034.1 positions "
            "8089-9189 with product accession WP_001313577.1."
        ),
    }


def table_s7_bas25_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas25\t2.2\tpLAND\t24-03-12_EV.png\t500000\tHEP2"
            "\t24-03-15\t24-03-15_GPEH_HEP2_PDO1_PDP6.png"
            "\t0\t1\t\t1\t5.698970004336019\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports an HEP2 assay row with a Bas25 phage readout and a "
            "-log(EOP) value of 5.699."
        ),
    }


def table_s7_bas19_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas19\t2.2\tpLAND\t24-03-12_EV.png\t15000\tHEP2"
            "\t24-03-15\t24-03-15_GPEH_HEP2_PDO1_PDP6.png"
            "\t0\t1\t\t1\t4.176091259055681\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports an HEP2 assay row with a Bas19 phage readout and a "
            "-log(EOP) value of 4.176."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "HEP2\tDS-38\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps HEP2 to "
            "replicated display name DS-38."
        ),
    }


def table_s8_zf_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "HEP2\t1.0\t366.0\tWP_001313577.1\tZF\t8SSU_A"
            "\tTranscriptional repressor CTCF,LIM domain-binding protein "
            "1; PROTEIN-DNA COMPLEX, DNA BINDING PROTEIN, transcription "
            "factor, zinc fingers, insulator/chromatin architecture, "
            "transcription-dna complex, TRANSCRIPTION"
            "\thhpred_7553560.hhr\t206.0\t364.0\t0.9902"
            "\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability zinc-finger HHpred hit for WP_001313577.1 "
            "in HEP2."
        ),
    }


def table_s8_hepn_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "HEP2\t1.0\t366.0\tWP_001313577.1\tHEPN\tPF05168.18"
            "\tHEPN ; HEPN domain\thhpred_7553560.hhr\t22.0\t153.0"
            "\t0.9662\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability HEPN HHpred hit for WP_001313577.1 in HEP2."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_zf_evidence(), table_s8_hepn_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-38 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 38 locus cataloged "
        "as working transcriptional unit HEP2 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-38",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "HEP2",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-38__DS-38",
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
        table_s7_bas25_evidence(),
        table_s7_bas19_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_38_locus_reduces_phage_plaquing",
            "title": "DS-38 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-38 locus to reduced bacteriophage plaquing without "
                "resolving DS-38 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-38 as the validated HEP2 "
                "transcriptional unit with one product accession, "
                "high-probability zinc-finger and HEPN HHpred rows for "
                "WP_001313577.1, and one DefenseFinder DS-38 profile row. "
                "It does not assert exact profile-to-protein "
                "correspondence, HEPN ribonuclease activity, zinc-finger "
                "DNA-binding activity, native host breadth, DS-38 "
                "molecular output, complete phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_38_locus",
                    "label": "DS-38 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "38 locus represented in the pinned DefenseFinder "
                        "HMM inventory by one DS-38 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned HEP2."
                    ),
                },
                {
                    "node_id": "ds_38_system_trait",
                    "label": "DS-38 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-38 phage-defense "
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
                    "subject": "ds_38_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-38/HEP2 locus contributes to reduced "
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
                        table_s7_bas25_evidence(),
                        table_s7_bas19_evidence(),
                        table_s8_display_evidence(),
                        *all_hhpred_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_38_system_trait",
                    "description": (
                        "DS-38-mediated phage plaquing reduction realizes "
                        "the DS-38 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas25_evidence(),
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
                    "subject": "ds_38_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-38 system possession is a phage-defense-system "
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
            "discussion_id": "ds-38-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-38 native host breadth, exact component "
                "activity, profile-to-protein mapping, HEPN ribonuclease "
                "interpretation, zinc-finger DNA-binding interpretation, "
                "complete phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-38 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-38 as the defensive HEP2 "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to one product accession, Bas25 and Bas19 phage "
                "readouts, display name DS-38, and high-probability HEPN "
                "and zinc-finger HHpred rows. The pinned DefenseFinder "
                "HMM inventory records one DS-38 custom profile row. The "
                "pinned rules table has no DS-38 row, and the first-pass "
                "record does not resolve native host breadth, complete "
                "phage breadth, direct profile-to-protein correspondence, "
                "HEPN ribonuclease activity, zinc-finger DNA-binding "
                "activity, molecular output, or endogenous DS-38 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas25_evidence(),
                table_s7_bas19_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-38, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_38_locus_reduces_phage_plaquing"],
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
            "Minted DS-38 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at HEP2 "
            "transcriptional-unit level because the HEPN and zinc-finger "
            "rows and rule rows remain unresolved, and "
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
            "Reviewed DS-38 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned HEP2 assays "
            "in E. coli MG1655 and a DefenseFinder DS-38 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-38 activity. No paid "
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
