#!/usr/bin/env python3
"""Add the DS-21 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_21_system.yaml"

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
TIMESTAMP = "2026-09-28T22:17:01Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T22:17:02Z"

IDENTIFIER = "traitmech:000446"
PROPOSAL = "proposals/metpo_traitmech_v323"

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
    "| DS-21 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROWS = (
    "| DS-21__DS-21A                                    |"
    "                                                  | DS-21"
    "                  | Custom                  | 20     |\n"
    "| DS-21__DS-21B                                    |"
    "                                                  | DS-21"
    "                  | Custom                  | 250    |\n"
    "| DS-21__DS-21C                                    |"
    "                                                  | DS-21"
    "                  | Custom                  | 70     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-21 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records three DS-21 "
            "custom profiles: DS-21__DS-21A, DS-21__DS-21B, and "
            "DS-21__DS-21C."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "TOXO\tNZ_QOXJ01000032.1\tGCF_003334085.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t7805\t9963"
            "\thypothetical protein, hypothetical protein, hypothetical "
            "protein\tWP_001532221.1, WP_001557682.1, WP_021552536.1"
            "\t10.9763556055726\t2.883007179633958\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-21"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "TOXO to DS_name DS-21, marks the cloned transcriptional "
            "unit as defensive, and records NZ_QOXJ01000032.1 positions "
            "7805-9963 with three product accessions."
        ),
    }


def table_s7_bas1_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t3000000\tTOXO\t24-07-25"
            "\t24-07-25_PDX1_TMO1_VANC_TOXO.png\t2\t1\t\t100"
            "\t4.477121254719663\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a TOXO "
            "assay row with a Bas1 phage readout and a -log(EOP) value "
            "of 4.477."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "TOXO\tDS-21\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps TOXO to replicated display name DS-21."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "TOXO\t3.0\t211.0\tWP_001557682.1\tPDDEXK\tPF18742.6"
            "\tDpnII-MboI ; REase_DpnII-MboI\thhpred_4621019.hhr"
            "\t37.0\t160.0\t0.96\t2024-07-29 00:00:00\t121-123"
            "\t103.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a PDDEXK "
            "HHpred hit for WP_001557682.1 in TOXO."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-21 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "three-gene DefensePredictor-discovered system 21 locus cataloged "
        "as working transcriptional unit TOXO and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-21",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "TOXO",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-21__DS-21A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DS-21__DS-21B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DS-21__DS-21C",
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
        table_s8_display_evidence(),
        table_s8_pddexk_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_21_locus_reduces_phage_plaquing",
            "title": "DS-21 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the three-gene "
                "DS-21 locus to reduced bacteriophage plaquing without "
                "resolving DS-21 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-21 as the validated TOXO "
                "transcriptional unit with three product accessions, a "
                "PDDEXK HHpred-domain row, and three DefenseFinder DS-21 "
                "profile rows. It does not assert native host breadth, "
                "exact profile-to-protein correspondence, DS-21 molecular "
                "activity, trigger, substrate, complete phage breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_21_locus",
                    "label": "DS-21 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene DefensePredictor-discovered system "
                        "21 locus represented in the pinned DefenseFinder "
                        "HMM inventory by three DS-21 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying cloned TOXO."
                    ),
                },
                {
                    "node_id": "ds_21_system_trait",
                    "label": "DS-21 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": ("Possession of a genome-encoded DS-21 phage-defense system."),
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
                    "subject": "ds_21_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-21/TOXO locus contributes to reduced "
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
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_21_system_trait",
                    "description": (
                        "DS-21-mediated phage plaquing reduction realizes the DS-21 system trait."
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
                    "subject": "ds_21_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": ("DS-21 system possession is a phage-defense-system trait."),
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
            "discussion_id": "ds-21-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-21 native host breadth, exact "
                "profile-to-protein mapping, HHpred-domain interpretation, "
                "component chemistry, complete phage breadth, molecular "
                "output, and rule-level DefenseFinder criteria before "
                "minting narrower DS-21 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-21 as the defensive TOXO "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to three product accessions, a Bas1 phage "
                "readout, display name DS-21, and a PDDEXK HHpred row. "
                "The pinned DefenseFinder HMM inventory records three "
                "DS-21 custom profile rows. The pinned rules table has no "
                "DS-21 row, and the first-pass record does not resolve "
                "native host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, PDDEXK nuclease "
                "activity, molecular output, or endogenous DS-21 activity."
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
                table_s8_pddexk_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-21, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_21_locus_reduces_phage_plaquing"],
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
            "Minted DS-21 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at TOXO "
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
            "Reviewed DS-21 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned TOXO assays "
            "in E. coli MG1655 and DefenseFinder DS-21 models, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-21 activity. No paid "
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
