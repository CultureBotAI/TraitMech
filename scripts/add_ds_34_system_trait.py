#!/usr/bin/env python3
"""Add the DS-34 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_34_system.yaml"

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
TIMESTAMP = "2026-09-29T08:40:09Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T08:40:10Z"

IDENTIFIER = "traitmech:000457"
PROPOSAL = "proposals/metpo_traitmech_v334"

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
    "| DS-34 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROWS = {
    "DS-34__DS-34A": (
        "| DS-34__DS-34A                                    |"
        "                                                  | DS-34"
        "                  | Custom                  | 120    |"
    ),
    "DS-34__DS-34B": (
        "| DS-34__DS-34B                                    |"
        "                                                  | DS-34"
        "                  | Custom                  | 50     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-34 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            f"{profile} as a custom DS-34 profile."
        ),
    }


def all_hmm_inventory_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_ROWS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "CITO\tNZ_QOXN01000005.1\tGCF_003334015.1\t+\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t236284\t238194"
            "\tphage repressor protein CI, hypothetical protein"
            "\tWP_001589054.1, WP_000377448.1\t8.290091443457554"
            "\t3.623314765621056\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-34"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id CITO "
            "to DS_name DS-34, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOXN01000005.1 positions "
            "236284-238194 with product accessions WP_001589054.1 and "
            "WP_000377448.1."
        ),
    }


def table_s7_bas19_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas19\t3.1\tpLAND\t24-04-10_CITO_AAA3_FDRT_EV.png"
            "\t4000\tCITO\t24-04-10\t24-04-10_CITO_AAA3_FDRT_EV.png"
            "\t0\t1\t\t1\t3.6020599913279625\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a CITO "
            "assay row with a Bas19 phage readout and a -log(EOP) value "
            "of 3.602."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "CITO\tDS-34\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps CITO to "
            "replicated display name DS-34."
        ),
    }


def table_s8_repressor_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "CITO\t1.0\t308.0\tWP_001589054.1\tPhage repressor"
            "\t2FJR_A\tRepressor protein CI; genetic switch, regulation, "
            "repressor\thhpred_1741337.hhr\t125.0\t307.0\t0.9987"
            "\t2024-04-17 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability phage-repressor HHpred hit for "
            "WP_001589054.1 in CITO."
        ),
    }


def table_s8_hth_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "CITO\t1.0\t308.0\tWP_001589054.1\tHTH\tPF08667.14"
            "\tBetR ; BetR domain\thhpred_1741337.hhr\t20.0\t88.0"
            "\t0.9431\t2024-04-17 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability HTH HHpred hit for WP_001589054.1 in CITO."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_repressor_evidence(), table_s8_hth_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-34 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DefensePredictor-discovered system 34 locus cataloged "
        "as working transcriptional unit CITO and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-34",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "CITO",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
        ],
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
        *all_hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_34_locus_reduces_phage_plaquing",
            "title": "DS-34 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-34 locus to reduced bacteriophage plaquing without "
                "resolving DS-34 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-34 as the validated CITO "
                "transcriptional unit with two product accessions, "
                "high-probability phage-repressor and HTH HHpred rows for "
                "WP_001589054.1, and two DefenseFinder DS-34 profile rows. "
                "It does not assert native host breadth, exact "
                "profile-to-protein correspondence, DS-34 molecular "
                "activity, trigger, substrate, complete phage breadth, "
                "phage-repressor or HTH HHpred-domain interpretation, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_34_locus",
                    "label": "DS-34 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system 34 "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by two DS-34 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned CITO."
                    ),
                },
                {
                    "node_id": "ds_34_system_trait",
                    "label": "DS-34 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-34 phage-defense "
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
                    "subject": "ds_34_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-34/CITO locus contributes to reduced "
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
                        *all_hhpred_evidence(),
                        *all_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_34_system_trait",
                    "description": (
                        "DS-34-mediated phage plaquing reduction realizes "
                        "the DS-34 system trait."
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
                    "subject": "ds_34_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-34 system possession is a phage-defense-system "
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
            "discussion_id": "ds-34-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-34 native host breadth, exact component "
                "activities, profile-to-protein mapping, phage-repressor "
                "and HTH HHpred-domain interpretation, complete phage "
                "breadth, molecular output, and rule-level DefenseFinder "
                "criteria before minting narrower DS-34 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-34 as the defensive CITO "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to two product accessions, a Bas19 phage readout, "
                "display name DS-34, and two HHpred rows. The pinned "
                "DefenseFinder HMM inventory records two DS-34 custom "
                "profile rows. The pinned rules table has no DS-34 row, "
                "and the first-pass record does not resolve native host "
                "breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, component activities, "
                "molecular output, or endogenous DS-34 activity."
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
                *all_hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list DS-34, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_34_locus_reduces_phage_plaquing"],
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
            "Minted DS-34 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at CITO "
            "transcriptional-unit level because phage-repressor and HTH "
            "activity and rule rows remain unresolved, and "
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
            "Reviewed DS-34 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned CITO assays "
            "in E. coli MG1655 and a DefenseFinder DS-34 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-34 activity. No paid "
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
