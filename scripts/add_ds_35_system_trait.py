#!/usr/bin/env python3
"""Add the DS-35 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_35_system.yaml"

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
TIMESTAMP = "2026-09-29T09:12:09Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T09:12:10Z"

IDENTIFIER = "traitmech:000458"
PROPOSAL = "proposals/metpo_traitmech_v335"

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
    "| DS-35 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-35__DS-35                                     |"
    "                                                  | DS-35"
    "                  | Custom                  | 100    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-35 "
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
            "The pinned DefenseFinder HMM inventory records DS-35__DS-35 "
            "as a custom DS-35 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "RED5\tNZ_QOXO01000016.1\tGCF_003334005.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t25863\t26705"
            "\thypothetical protein\tWP_087906371.1\t8.022232609988304"
            "\t2.666159259393051\tTrue\tTrue"
            "\tRemote defense homolog\tDS-35"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id RED5 "
            "to DS_name DS-35, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOXO01000016.1 positions "
            "25863-26705 with product accession WP_087906371.1."
        ),
    }


def table_s7_rb69_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "RB69\t2.1\tpLAND\t24-03-12_EV.png\t200000\tRED5"
            "\t24-03-14\t24-03-14_RED5_TNEC_6236_RED2.png"
            "\t0\t1\t\t1\t5.301029995663981\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a RED5 "
            "assay row with an RB69 phage readout and a -log(EOP) value "
            "of 5.301."
        ),
    }


def table_s7_t4_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T4\t2.1\tpLAND\t24-03-12_EV.png\t200000000\tRED5"
            "\t24-03-14\t24-03-14_RED5_TNEC_6236_RED2.png"
            "\t2\t10\t\t1000\t5.301029995663981\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a RED5 "
            "assay row with a T4 phage readout and a -log(EOP) value "
            "of 5.301."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "RED5\tDS-35\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps RED5 to "
            "replicated display name DS-35."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "RED5\t1.0\t280.0\tWP_087906371.1\tPDDEXK\tPF18742.5"
            "\tDpnII-MboI ; REase_DpnII-MboI\thhpred_9496458.hhr"
            "\t142.0\t278.0\t1.0\t2024-04-15 00:00:00"
            "\t346-348\t333.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability PDDEXK HHpred hit for WP_087906371.1 in "
            "RED5."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-35 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 35 locus cataloged "
        "as working transcriptional unit RED5 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-35",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "RED5",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-35__DS-35",
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
        table_s7_rb69_evidence(),
        table_s7_t4_evidence(),
        table_s8_display_evidence(),
        table_s8_pddexk_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_35_locus_reduces_phage_plaquing",
            "title": "DS-35 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-35 locus to reduced bacteriophage plaquing without "
                "resolving DS-35 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-35 as the validated RED5 "
                "transcriptional unit with one product accession, one "
                "high-probability PDDEXK HHpred row for WP_087906371.1 in "
                "Table S8, and one DefenseFinder DS-35 profile row. It "
                "does not assert exact profile-to-protein correspondence, "
                "PDDEXK domain interpretation, nuclease chemistry, native "
                "host breadth, DS-35 molecular output, complete phage "
                "breadth, or DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_35_locus",
                    "label": "DS-35 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "35 locus represented in the pinned DefenseFinder "
                        "HMM inventory by one DS-35 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned RED5."
                    ),
                },
                {
                    "node_id": "ds_35_system_trait",
                    "label": "DS-35 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-35 phage-defense "
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
                    "subject": "ds_35_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-35/RED5 locus contributes to reduced "
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
                        table_s7_rb69_evidence(),
                        table_s7_t4_evidence(),
                        table_s8_display_evidence(),
                        table_s8_pddexk_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_35_system_trait",
                    "description": (
                        "DS-35-mediated phage plaquing reduction realizes "
                        "the DS-35 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_rb69_evidence(),
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
                    "subject": "ds_35_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-35 system possession is a phage-defense-system "
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
            "discussion_id": "ds-35-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-35 native host breadth, exact component "
                "activity, profile-to-protein mapping, PDDEXK HHpred-domain "
                "interpretation, nuclease chemistry, complete phage breadth, "
                "molecular output, and rule-level DefenseFinder criteria "
                "before minting narrower DS-35 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-35 as the defensive RED5 "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to one product accession, RB69 and T4 phage "
                "readouts, display name DS-35, and one PDDEXK HHpred row. "
                "The pinned DefenseFinder HMM inventory records one DS-35 "
                "custom profile row. The pinned rules table has no DS-35 "
                "row, and the first-pass record does not resolve native "
                "host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, PDDEXK domain "
                "interpretation, nuclease chemistry, molecular output, or "
                "endogenous DS-35 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_rb69_evidence(),
                table_s7_t4_evidence(),
                table_s8_display_evidence(),
                table_s8_pddexk_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-35, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_35_locus_reduces_phage_plaquing"],
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
            "Minted DS-35 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at RED5 "
            "transcriptional-unit level because PDDEXK activity and rule "
            "rows remain unresolved, and "
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
            "Reviewed DS-35 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned RED5 assays "
            "in E. coli MG1655 and a DefenseFinder DS-35 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-35 activity. No paid "
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
