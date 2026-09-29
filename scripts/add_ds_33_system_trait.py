#!/usr/bin/env python3
"""Add the DS-33 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_33_system.yaml"

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
TIMESTAMP = "2026-09-29T08:03:43Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T08:03:44Z"

IDENTIFIER = "traitmech:000456"
PROPOSAL = "proposals/metpo_traitmech_v333"

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
    "| DS-33 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-33__DS-33                                     |"
    "                                                  | DS-33"
    "                  | Custom                  | 220    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-33 "
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
            "The pinned DefenseFinder HMM inventory records DS-33__DS-33 "
            "as a custom DS-33 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "GNAT\tNZ_QOWT01000046.1\tGCF_003334765.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t6922\t8901"
            "\thypothetical protein, hypothetical protein"
            "\tWP_014639476.1, WP_000354965.1\t9.45173070144912"
            "\t3.204412762840645\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-33"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id GNAT "
            "to DS_name DS-33, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOWT01000046.1 positions "
            "6922-8901 with product accessions WP_014639476.1 and "
            "WP_000354965.1."
        ),
    }


def table_s7_bas26_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas26\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t500000000\tGNAT\t24-03-09"
            "\t24-03-09_GNAT_NADR_D390_DRAT.png\t2\t100\tY\t10000"
            "\t4.698970004336019\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a GNAT assay "
            "row with a Bas26 phage readout and a -log(EOP) value of 4.699."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "GNAT\tDS-33\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps GNAT to "
            "replicated display name DS-33."
        ),
    }


def table_s8_csa3_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "GNAT\t2.0\t333.0\tWP_000354965.1\tCsa3\t6W11_B"
            "\tCRISPR locus-related putative DNA-binding protein Csa3; "
            "CARF, CRISPR-Cas, cyclic oligoadenylate, cA4"
            "\thhpred_9793887.hhr\t25.0\t110.0\t0.5601"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "lower-probability Csa3 HHpred hit for WP_000354965.1 in "
            "GNAT."
        ),
    }


def table_s8_hepn_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "GNAT\t1.0\t320.0\tWP_014639476.1\tHEPN\tPF18737.5"
            "\tHEPN_MAE_28990 ; MAE_28990/MAE_18760-like HEPN"
            "\thhpred_9884029.hhr\t144.0\t306.0\t0.9842"
            "\t2024-04-15 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability HEPN HHpred hit for WP_014639476.1 in GNAT."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_csa3_evidence(), table_s8_hepn_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-33 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DefensePredictor-discovered system 33 locus cataloged "
        "as working transcriptional unit GNAT and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-33",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "GNAT",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-33__DS-33",
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
        table_s7_bas26_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_33_locus_reduces_phage_plaquing",
            "title": "DS-33 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-33 locus to reduced bacteriophage plaquing without "
                "resolving DS-33 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-33 as the validated GNAT "
                "transcriptional unit with two product accessions, a "
                "lower-probability Csa3 HHpred row for WP_000354965.1, a "
                "high-probability HEPN HHpred row for WP_014639476.1, and "
                "one DefenseFinder DS-33 profile row. It does not assert "
                "native host breadth, exact profile-to-protein "
                "correspondence, DS-33 molecular activity, trigger, "
                "substrate, complete phage breadth, Csa3 or HEPN "
                "HHpred-domain interpretation, or DefenseFinder rule-level "
                "detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_33_locus",
                    "label": "DS-33 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system 33 "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-33 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned GNAT."
                    ),
                },
                {
                    "node_id": "ds_33_system_trait",
                    "label": "DS-33 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-33 phage-defense "
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
                    "subject": "ds_33_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-33/GNAT locus contributes to reduced "
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
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_33_system_trait",
                    "description": (
                        "DS-33-mediated phage plaquing reduction realizes "
                        "the DS-33 system trait."
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
                    "subject": "ds_33_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-33 system possession is a phage-defense-system "
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
            "discussion_id": "ds-33-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-33 native host breadth, exact component "
                "activities, profile-to-protein mapping, Csa3 and HEPN "
                "HHpred-domain interpretation, complete phage breadth, "
                "molecular output, and rule-level DefenseFinder criteria "
                "before minting narrower DS-33 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-33 as the defensive GNAT "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to two product accessions, a Bas26 phage readout, "
                "display name DS-33, and two HHpred rows. The pinned "
                "DefenseFinder HMM inventory records one DS-33 custom "
                "profile row. The pinned rules table has no DS-33 row, "
                "and the first-pass record does not resolve native host "
                "breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, component activities, "
                "molecular output, or endogenous DS-33 activity."
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
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-33, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_33_locus_reduces_phage_plaquing"],
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
            "Minted DS-33 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at GNAT "
            "transcriptional-unit level because Csa3 and HEPN activity "
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
            "Reviewed DS-33 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned GNAT assays "
            "in E. coli MG1655 and a DefenseFinder DS-33 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-33 activity. No paid "
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
