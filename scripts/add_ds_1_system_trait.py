#!/usr/bin/env python3
"""Add the DS-1 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_1_system.yaml"

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
TIMESTAMP = "2026-09-28T02:18:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T02:18:01Z"

IDENTIFIER = "traitmech:000424"
PROPOSAL = "proposals/metpo_traitmech_v301"

DS_VALIDATION_SNIPPET = (
    "In total, 42 (45% of 94) of the cloned TUs produced smaller "
    "plaque sizes or reduced the efficiency of plating (EOP) at least "
    "ten-fold relative to an empty vector control strain"
)
DS_NAMING_SNIPPET = (
    "We refer to these validated TUs as DefensePredictor discovered systems "
    "(DSs), with genes in multi-gene TUs denoted by an alphabetical suffix, "
    "e.g., DS-8A is the first gene of DS-8."
)
ARTICLE_ROW = (
    "| DS-1 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-1__DS-1A": (
        "| DS-1__DS-1A                                      |"
        "                                                  | DS-1"
        "                   | Custom                  | 30     |"
    ),
    "DS-1__DS-1B": (
        "| DS-1__DS-1B                                      |"
        "                                                  | DS-1"
        "                   | Custom                  | 50     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-1 source "
            "key to the preprint DOI for the DeWeirdt et al. DefensePredictor "
            "study, which has since been published in Science."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom DS-1 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "D390\tNZ_RRVY01000002.1\tGCF_003886375.1\t+\tTrue\tFalse"
            "\tTrue\tTrue\tDefensePredictor hits\t220602\t222994"
            "\thypothetical protein, nucleoid-associated protein"
            "\tWP_000150292.1, WP_000355468.1\t12.74067081596784"
            "\t-2.197224577336219\tTrue\tFalse\tPredicted novel defense gene"
            "\tDS-1"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id D390 to "
            "DS_name DS-1, marks the cloned transcriptional unit as defensive, "
            "and records NZ_RRVY01000002.1 positions 220602-222994 with "
            "product accessions WP_000355468.1 and WP_000150292.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t40000000\tD390\t24-03-12\t24-03-12_PIN8_D390_NADR_PN12.png"
            "\t0\t1\t\t1\t7.6020599913279625\tTrue\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a D390 assay "
            "row with a 1-PFU Bas1 readout and a -log(EOP) value of 7.602."
        ),
    }


def table_s8_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "D390\tDS-1\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps D390 to replicated "
            "display name DS-1."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-1 system",
    "definition": (
        "A phage defense system in which an organism possesses the two-gene "
        "DefensePredictor-discovered system 1 locus that was cloned as E. "
        "coli transcriptional unit D390 and whose plasmid expression reduced "
        "bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-1",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "D390",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-1__DS-1A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DS-1__DS-1B",
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
        table_s7_evidence(),
        table_s8_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_1_locus_reduces_phage_plaquing",
            "title": "DS-1 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene DS-1 "
                "locus to reduced bacteriophage plaquing without resolving "
                "DS-1 component functions or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-1 as the validated D390 transcriptional "
                "unit with two product accessions and with DefenseFinder "
                "DS-1A and DS-1B profile rows. It does not assert native host "
                "breadth, exact profile-to-protein correspondence, the direct "
                "viral trigger or substrate, exact molecular output, phage "
                "target breadth, or DefenseFinder rule-level detection "
                "criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_1_locus",
                    "label": "DS-1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system locus "
                        "represented in the pinned DefenseFinder HMM inventory "
                        "by DS-1A and DS-1B custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing or reduced plaque "
                        "size by bacteriophages in cells carrying cloned D390."
                    ),
                },
                {
                    "node_id": "ds_1_system_trait",
                    "label": "DS-1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-1 phage-defense "
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
                    "subject": "ds_1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-1/D390 locus contributes to reduced "
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
                    "object": "ds_1_system_trait",
                    "description": (
                        "DS-1-mediated phage plaquing reduction realizes the "
                        "DS-1 system trait."
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
                    "subject": "ds_1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-1 system possession is a phage-defense-system "
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
            "discussion_id": "ds-1-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-1 native host breadth, exact DS-1A/DS-1B "
                "component functions, profile-to-component mapping, "
                "sensitive-phage breadth, molecular output, and rule-level "
                "detection criteria before minting narrower DS-1 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-1 as the defensive D390 "
                "transcriptional unit that reduced plaquing when cloned in "
                "E. coli MG1655, and the pinned DefenseFinder HMM inventory "
                "records DS-1A and DS-1B profile rows. The pinned rules "
                "table has no DS-1 row, and the first-pass record does not "
                "resolve native host breadth, exact component activities, "
                "profile-to-component mapping, phage target breadth, the "
                "direct molecular output, or endogenous DS-1 activity."
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
                table_s8_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-1, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_1_locus_reduces_phage_plaquing"],
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
            "Minted DS-1 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned D390 transcriptional "
            "unit level because the pinned DefenseFinder DS-1 HMM rows are "
            f"not backed by a rules row; {PROPOSAL} reserves the replacement "
            "placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-1 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned D390 plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-1 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-1 activity. No paid "
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
