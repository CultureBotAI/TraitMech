#!/usr/bin/env python3
"""Add the DS-46 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_46_system.yaml"

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
TIMESTAMP = "2026-09-29T18:46:02Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T18:46:03Z"

IDENTIFIER = "traitmech:000471"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v348"

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


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "RMRT\tNZ_RRVG01000021.1\tGCF_003886135.1\t+\tFalse"
            "\tFalse\tTrue\tTrue\tHHblits hits\t62985\t63495"
            "\tDUF3606 domain-containing protein, hypothetical protein"
            "\tWP_001406733.1, WP_000002748.1\t-4.513359272522268"
            "\t5.517452896464706\tFalse\tTrue\t\tDS-46"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id RMRT "
            "to DS_name DS-46, marks the cloned transcriptional unit as "
            "defensive, records an HHblits-hit screen, and places two "
            "product accessions in NZ_RRVG01000021.1 positions 62985-63495."
        ),
    }


def table_s7_absence_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "notes": (
            "A structured first-pass search of final Science supplementary "
            "Table S7 found no exact RMRT or DS-46 system row to connect "
            "DS-46 to a phage-specific readout."
        ),
    }


def table_s8_absence_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "notes": (
            "A structured first-pass search of final Science supplementary "
            "Table S8 found no exact RMRT or DS-46 display-name or "
            "HHpred-domain row."
        ),
    }


def article_registry_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "notes": (
            "The pinned DefenseFinder article registry has no exact DS-46 "
            "or RMRT row."
        ),
    }


def hmm_inventory_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "The pinned DefenseFinder HMM inventory has no exact DS-46 or "
            "RMRT profile row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "The pinned DefenseFinder rules table has no exact DS-46 or "
            "RMRT model row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-46 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DS-46 locus cataloged as working transcriptional unit "
        "RMRT and whose plasmid expression in E. coli MG1655 reduced "
        "bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "DS-46",
            "synonym_type": "EXACT_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "RMRT",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
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
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_46_locus_reduces_phage_plaquing",
            "title": "DS-46 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-46 locus to reduced bacteriophage plaquing without "
                "resolving DS-46 phage-specific readouts, domain "
                "annotations, DefenseFinder model coverage, or molecular "
                "output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-46 as the validated RMRT "
                "transcriptional unit with two Table S6 product accessions. "
                "It does not assert phage-specific Table S7 readouts, "
                "Table S8 display-name rows, Table S8 HHpred-domain rows, "
                "DefenseFinder article/HMM/rules rows, native host "
                "breadth, exact component activities, molecular output, "
                "complete phage breadth, or endogenous DS-46 activity."
            ),
            "nodes": [
                {
                    "node_id": "ds_46_locus",
                    "label": "DS-46 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DS-46 locus cataloged as working "
                        "transcriptional unit RMRT in final Science "
                        "supplementary Table S6."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned RMRT."
                    ),
                },
                {
                    "node_id": "ds_46_system_trait",
                    "label": "DS-46 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-46 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_SYSTEM,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "ds_46_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-46/RMRT locus contributes to reduced "
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
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_46_system_trait",
                    "description": (
                        "DS-46-mediated phage plaquing reduction realizes "
                        "the DS-46 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "The DS nomenclature is used for validated "
                                "phage-defense transcriptional units."
                            ),
                        },
                    ],
                },
                {
                    "subject": "ds_46_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-46 system possession is a "
                        "phage-defense-system trait."
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
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ds-46-model-coverage-gap",
            "prompt": (
                "Resolve DS-46 phage-specific readouts, display-name and "
                "domain rows, DefenseFinder model coverage, native host "
                "breadth, exact component activities, molecular output, "
                "complete phage breadth, and endogenous activity before "
                "minting narrower DS-46 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-46 as the defensive RMRT "
                "transcriptional unit and final Science Table S6 maps RMRT "
                "to two product accessions. A first-pass final Science "
                "Table S7/S8 review found no exact RMRT/DS-46 "
                "phage-specific readout, display-name row, or "
                "HHpred-domain row. The pinned DefenseFinder article, HMM, "
                "and rules registries also do not list DS-46 or RMRT, and "
                "the first-pass record therefore does not resolve native "
                "host breadth, complete phage breadth, exact component "
                "activities, molecular output, or endogenous DS-46 "
                "activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_absence_evidence(),
                table_s8_absence_evidence(),
                article_registry_absence_evidence(),
                hmm_inventory_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#ds_46_locus_reduces_phage_plaquing"],
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
            "Minted DS-46 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at RMRT "
            "transcriptional-unit level because phage-specific Table S7 "
            "readouts, Table S8 display and domain rows, DefenseFinder "
            "article/HMM/rules coverage, native host breadth, exact "
            "component activities, complete phage breadth, and molecular "
            "output remain unresolved, and "
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
            "Reviewed DS-46 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned RMRT assays in "
            "E. coli MG1655, but not a direct named native microbial "
            "isolate exemplar with experimentally verified endogenous "
            "DS-46 activity. No paid research was used."
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
