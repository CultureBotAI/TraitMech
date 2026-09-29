#!/usr/bin/env python3
"""Add the DS-28 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_28_system.yaml"

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
TIMESTAMP = "2026-09-29T04:57:13Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T04:57:14Z"

IDENTIFIER = "traitmech:000452"
PROPOSAL = "proposals/metpo_traitmech_v329"

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
    "| DS-28 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW_A = (
    "| DS-28__DS-28A                                    |"
    "                                                  | DS-28"
    "                  | Custom                  | 100    |"
)
HMM_ROW_B = (
    "| DS-28__DS-28B                                    |"
    "                                                  | DS-28"
    "                  | Custom                  | 100    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-28 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_a_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_A,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DS-28__DS-28A "
            "as a custom DS-28 profile."
        ),
    }


def hmm_inventory_b_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_B,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DS-28__DS-28B "
            "as a custom DS-28 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "ANEX\tNZ_RRWS01000106.1\tGCF_003892555.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t2434\t3695"
            "\thypothetical protein, HEPN family nuclease"
            "\tWP_000494510.1, WP_000528930.1"
            "\t7.693635438050782\t1.093286044385436\tTrue"
            "\tTrue\tPredicted novel defense gene\tDS-28"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id "
            "ANEX to DS_name DS-28, marks the cloned transcriptional "
            "unit as defensive, and records NZ_RRWS01000106.1 positions "
            "2434-3695 with product accessions WP_000494510.1 and "
            "WP_000528930.1."
        ),
    }


def table_s7_bas60_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas60\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t400000\tANEX\t24-07-24\t24-07-24_ANEX_NADH_APE1_NLRH.png"
            "\t1\t1\t\t10\t4.6020599913279625\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an ANEX "
            "assay row with a Bas60 phage readout and a -log(EOP) "
            "value of 4.602."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "ANEX\tDS-28\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps ANEX to "
            "replicated display name DS-28."
        ),
    }


def table_s8_hepn_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ANEX\t1.0\t163.0\tWP_000528930.1\tHEPN\tPF18736.6"
            "\tpEK499_p136 ; HEPN pEK499 p136\thhpred_5242066.hhr"
            "\t1.0\t153.0\t1.0\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability HEPN HHpred hit for WP_000528930.1 in "
            "ANEX."
        ),
    }


def table_s8_tf_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ANEX\t2.0\t252.0\tWP_000494510.1\tTF\t6J9E_J"
            "\tRNA polymerase, transcription termination, anti-termination, "
            "RNAP clamp, phage, transcription initiation, P7, NusA, "
            "Xanthomonos oryzae, Xp10, transcription"
            "\thhpred_1617000.hhr\t143.0\t178.0\t0.326"
            "\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "lower-probability TF HHpred hit for WP_000494510.1 in ANEX."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-28 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DefensePredictor-discovered system 28 locus cataloged "
        "as working transcriptional unit ANEX and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-28",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "ANEX",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-28__DS-28A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DS-28__DS-28B",
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
        table_s7_bas60_evidence(),
        table_s8_display_evidence(),
        table_s8_hepn_evidence(),
        table_s8_tf_evidence(),
        article_registry_evidence(),
        hmm_inventory_a_evidence(),
        hmm_inventory_b_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_28_locus_reduces_phage_plaquing",
            "title": "DS-28 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-28 locus to reduced bacteriophage plaquing without "
                "resolving DS-28 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-28 as the validated ANEX "
                "transcriptional unit with two product accessions, one "
                "high-probability HEPN HHpred-domain row, one "
                "lower-probability TF HHpred-domain row, and two "
                "DefenseFinder DS-28 profile rows. It does not assert "
                "native host breadth, exact profile-to-protein "
                "correspondence, DS-28 molecular activity, trigger, "
                "substrate, complete phage breadth, HEPN or "
                "transcription-factor HHpred-domain interpretation, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_28_locus",
                    "label": "DS-28 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system 28 "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by two DS-28 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned ANEX."
                    ),
                },
                {
                    "node_id": "ds_28_system_trait",
                    "label": "DS-28 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-28 phage-defense "
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
                    "subject": "ds_28_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-28/ANEX locus contributes to reduced "
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
                        table_s7_bas60_evidence(),
                        table_s8_display_evidence(),
                        table_s8_hepn_evidence(),
                        table_s8_tf_evidence(),
                        hmm_inventory_a_evidence(),
                        hmm_inventory_b_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_28_system_trait",
                    "description": (
                        "DS-28-mediated phage plaquing reduction realizes "
                        "the DS-28 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_bas60_evidence(),
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
                    "subject": "ds_28_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-28 system possession is a phage-defense-system "
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
            "discussion_id": "ds-28-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-28 native host breadth, exact component "
                "activities, profile-to-protein mappings, HEPN and "
                "transcription-factor HHpred-domain interpretations, "
                "complete phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-28 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-28 as the defensive ANEX "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to product accessions WP_000494510.1 and "
                "WP_000528930.1, a Bas60 phage readout, display name "
                "DS-28, a high-probability HEPN HHpred row, and a "
                "lower-probability TF HHpred row. The pinned DefenseFinder "
                "HMM inventory records two DS-28 custom profile rows. The "
                "pinned rules table has no DS-28 row, and the first-pass "
                "record does not resolve "
                "native host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, HEPN or "
                "transcription-factor activity, molecular output, or "
                "endogenous DS-28 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_bas60_evidence(),
                table_s8_display_evidence(),
                table_s8_hepn_evidence(),
                table_s8_tf_evidence(),
                article_registry_evidence(),
                hmm_inventory_a_evidence(),
                hmm_inventory_b_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-28, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_28_locus_reduces_phage_plaquing"],
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
            "Minted DS-28 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at ANEX "
            "transcriptional-unit level because HEPN and "
            "transcription-factor HHpred-domain interpretation and rule "
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
            "Reviewed DS-28 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned ANEX assays "
            "in E. coli MG1655 and a DefenseFinder DS-28 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-28 activity. No paid "
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
