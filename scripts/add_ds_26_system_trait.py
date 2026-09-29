#!/usr/bin/env python3
"""Add the DS-26 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_26_system.yaml"

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
TIMESTAMP = "2026-09-29T19:30:01Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T19:30:02Z"

IDENTIFIER = "traitmech:000472"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v349"

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
            "NERD\tNZ_QOXL01000006.1\tGCF_003334035.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t203139"
            "\t204737\thypothetical protein\tWP_054626965.1"
            "\t9.096479385650875\t4.498799058824351\tTrue\tTrue"
            "\tRemote defense homolog\tDS-26"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "NERD to DS_name DS-26, marks the cloned transcriptional unit "
            "as defensive, and records NZ_QOXL01000006.1 positions "
            "203139-204737 with product accession WP_054626965.1."
        ),
    }


def table_s7_bas25_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas25\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t50000000\tNERD\t24-07-17"
            "\t24-07-17_AAA2_RMOR_NERD_NUCS.png\t1\t3"
            "\t\t30\t6.221848749616356\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports a NERD assay row with a Bas25 phage readout and a "
            "-log(EOP) value of 6.222."
        ),
    }


def table_s7_bas19_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas19\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t2200000\tNERD\t24-07-17"
            "\t24-07-17_AAA2_RMOR_NERD_NUCS.png\t1\t2"
            "\t\t20\t5.041392685158225\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet "
            "reports a NERD assay row with a Bas19 phage readout and a "
            "-log(EOP) value of 5.041."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "NERD\tDS-26\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps NERD to "
            "replicated display name DS-26."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "NERD\t1.0\t532.0\tWP_054626965.1\tPDDEXK\tPF09254.16"
            "\tFokI_cleav_dom ; FokI, cleavage domain"
            "\thhpred_1843394.hhr\t282.0\t459.0\t0.95"
            "\t2024-07-29 00:00:00\t77-79\t63.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "PDDEXK/FokI cleavage-domain HHpred lead for WP_054626965.1 "
            "in NERD; this first-pass record records it as source context "
            "without resolving DS-26 molecular activity."
        ),
    }


def article_registry_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "notes": (
            "The pinned DefenseFinder article registry has no exact DS-26 "
            "or source-key NERD row."
        ),
    }


def hmm_inventory_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "The pinned DefenseFinder HMM inventory has no exact DS-26 or "
            "DS-26__DS-26 profile row; the NERD substring occurs only in "
            "an unrelated UG34__NERD_Helicase profile row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "The pinned DefenseFinder rules table has no exact DS-26 or "
            "source-key NERD model row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-26 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 26 locus cataloged "
        "as working transcriptional unit NERD and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "DS-26",
            "synonym_type": "EXACT_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "NERD",
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
        table_s7_bas25_evidence(),
        table_s7_bas19_evidence(),
        table_s8_display_evidence(),
        table_s8_pddexk_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_26_locus_reduces_phage_plaquing",
            "title": "DS-26 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-26 locus to reduced bacteriophage plaquing without "
                "resolving DS-26 nuclease chemistry, native activity, "
                "DefenseFinder model coverage, or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-26 as the validated NERD "
                "transcriptional unit with one product accession, two "
                "Table S7 phage-specific readouts, and one Table S8 "
                "PDDEXK/FokI cleavage-domain HHpred lead for "
                "WP_054626965.1. It does not assert exact domain "
                "interpretation, nuclease chemistry, native host breadth, "
                "complete phage breadth, DefenseFinder article/HMM/rules "
                "coverage, molecular output, or endogenous DS-26 activity."
            ),
            "nodes": [
                {
                    "node_id": "ds_26_locus",
                    "label": "DS-26 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DS-26 locus cataloged as working "
                        "transcriptional unit NERD in final Science "
                        "supplementary Table S6."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned NERD."
                    ),
                },
                {
                    "node_id": "ds_26_system_trait",
                    "label": "DS-26 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-26 phage-defense "
                        "system."
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
                    "subject": "ds_26_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-26/NERD locus contributes to reduced "
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
                        table_s7_bas25_evidence(),
                        table_s7_bas19_evidence(),
                        table_s8_display_evidence(),
                        table_s8_pddexk_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_26_system_trait",
                    "description": (
                        "DS-26-mediated phage plaquing reduction realizes "
                        "the DS-26 system trait."
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
                    "subject": "ds_26_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-26 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name validated TUs as DSs."
                            ),
                        },
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ds-26-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-26 native host breadth, exact component "
                "activity, PDDEXK/FokI HHpred-domain interpretation, "
                "nuclease chemistry, complete phage breadth, molecular "
                "output, and DefenseFinder model coverage before minting "
                "narrower DS-26 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-26 as the defensive NERD "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to one product accession, Bas25 and Bas19 phage "
                "readouts, display name DS-26, and a PDDEXK/FokI "
                "cleavage-domain HHpred row. A first-pass pinned "
                "DefenseFinder review found no exact DS-26 article, HMM, "
                "or rules row, and the first-pass record therefore does "
                "not resolve native host breadth, complete phage breadth, "
                "domain interpretation, nuclease chemistry, molecular "
                "output, or endogenous DS-26 activity."
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
                table_s8_pddexk_evidence(),
                article_registry_absence_evidence(),
                hmm_inventory_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#ds_26_locus_reduces_phage_plaquing"],
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
            "Minted DS-26 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at NERD "
            "transcriptional-unit level because native host breadth, exact "
            "component activity, complete phage breadth, DefenseFinder "
            "model coverage, nuclease chemistry, and molecular output "
            "remain unresolved, and "
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
            "Reviewed DS-26 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned NERD assays "
            "in E. coli MG1655, but not a direct named native microbial "
            "isolate exemplar with experimentally verified endogenous "
            "DS-26 activity. No paid research was used."
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
