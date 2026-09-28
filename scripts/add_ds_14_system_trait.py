#!/usr/bin/env python3
"""Add the DS-14 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_14_system.yaml"

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
TIMESTAMP = "2026-09-28T08:11:18Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T08:11:19Z"

IDENTIFIER = "traitmech:000429"
PROPOSAL = "proposals/metpo_traitmech_v306"

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
    "| DS-14 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-14__DS-14": (
        "| DS-14__DS-14                                     |"
        "                                                  | DS-14"
        "                  | Custom                  | 500    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-14 "
            "source key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom DS-14 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "RMOR\tNZ_QOZC01000013.1\tGCF_003333475.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t106880\t109330"
            "\thypothetical protein\tWP_040091717.1\t14.71279098470142"
            "\t5.293304824724491\tTrue\tTrue\tRemote defense homolog\tDS-14"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id RMOR "
            "to DS_name DS-14, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOZC01000013.1 positions "
            "106880-109330 with product accession WP_040091717.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas50\t6.1\tpLAND\t24-07-17_MVB1_VPUS_VAME_EV.png"
            "\t500000000\tRMOR\t24-07-17"
            "\t24-07-17_AAA2_RMOR_NERD_NUCS.png\t3\t10\t\t10000"
            "\t4.698970004336019\t\t\tTrue\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an RMOR assay "
            "row with a Bas50 phage readout and a -log(EOP) value of 4.699."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "RMOR\tDS-14\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps RMOR to "
            "replicated display name DS-14."
        ),
    }


def table_s8_aaa_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "RMOR\t1.0\t816.0\tWP_040091717.1\tAAA+ ATPase\t7MCA_A"
            "\tOrigin recognition complex subunit 1; replication initiation, "
            "REPLICATION; HET: AGS; 3.6A {Saccharomyces cerevisiae}"
            "\thhpred_4983760.hhr\t270.0\t569.0\t0.99"
            "\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports an AAA+ ATPase "
            "HHpred hit for WP_040091717.1 in RMOR."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "RMOR\t1.0\t816.0\tWP_040091717.1\tPDDEXK\tPF15516.11"
            "\tBpuSI_N ; BpuSI N-terminal domain\thhpred_4983760.hhr"
            "\t27.0\t167.0\t0.99\t2024-07-30 00:00:00\t76-78\t65.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a PDDEXK "
            "HHpred hit for WP_040091717.1 in RMOR."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_aaa_evidence(), table_s8_pddexk_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-14 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 14 locus cataloged "
        "as working transcriptional unit RMOR and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-14",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "RMOR",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_PROFILE_SNIPPETS
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
        table_s7_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_14_locus_reduces_phage_plaquing",
            "title": "DS-14 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-14 locus to reduced bacteriophage plaquing without "
                "resolving DS-14 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-14 as the validated RMOR "
                "transcriptional unit with one product accession and with a "
                "DefenseFinder DS-14 profile row. It does not assert native "
                "host breadth, exact profile-to-protein correspondence, the "
                "direct viral trigger or substrate, exact AAA+ ATPase or "
                "PDDEXK nuclease chemistry, phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_14_locus",
                    "label": "DS-14 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-14 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas50 in cells carrying cloned RMOR."
                    ),
                },
                {
                    "node_id": "ds_14_system_trait",
                    "label": "DS-14 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-14 phage-defense "
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
                    "subject": "ds_14_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-14/RMOR locus contributes to reduced "
                        "bacteriophage plaquing when plasmid expressed."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_VALIDATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. experimentally validate "
                                "DefensePredictor-discovered systems by "
                                "assaying cloned transcriptional units "
                                "against E. coli phages."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_14_system_trait",
                    "description": (
                        "DS-14-mediated phage plaquing reduction realizes "
                        "the DS-14 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name each validated "
                                "transcriptional unit as a "
                                "DefensePredictor discovered system."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "ds_14_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-14 system possession is a phage-defense-system "
                        "trait."
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
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ds-14-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-14 native host breadth, exact single-component "
                "activity, DS-14 profile-to-protein mapping, "
                "sensitive-phage breadth, exact AAA+ ATPase and PDDEXK "
                "nuclease chemistry, and rule-level detection criteria "
                "before minting narrower DS-14 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-14 as the defensive RMOR "
                "transcriptional unit that reduced Bas50 plaquing when "
                "cloned in E. coli MG1655, and the pinned DefenseFinder HMM "
                "inventory records one DS-14 profile row. The pinned rules "
                "table has no DS-14 row, and the first-pass record does not "
                "resolve native host breadth, exact component activity, "
                "profile-to-protein mapping, phage target breadth, or "
                "endogenous DS-14 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_VALIDATION_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. validate predicted transcriptional "
                        "units by measuring plaquing relative to an empty "
                        "vector control strain."
                    ),
                },
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-14, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_14_locus_reduces_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-28",
        }
    ],
}


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
            "Minted DS-14 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned RMOR "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-14 HMM row is not backed by a rules row; "
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
            "Reviewed DS-14 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned RMOR plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-14 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-14 activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
