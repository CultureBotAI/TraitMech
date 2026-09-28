#!/usr/bin/env python3
"""Add the DS-12 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_12_system.yaml"

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
TIMESTAMP = "2026-09-28T15:20:46Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T15:20:47Z"

IDENTIFIER = "traitmech:000436"
PROPOSAL = "proposals/metpo_traitmech_v313"

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
    "| DS-12B | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-12__DS-12B": (
        "| DS-12__DS-12B                                    |"
        "                                                  | DS-12"
        "                  | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-12B "
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
            "custom DS-12 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "PD3A\tNZ_RRVF01000002.1\tGCF_003886115.1\t-\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t104144\t108678"
            "\trestriction endonuclease, AAA family ATPase"
            "\tWP_059339975.1, WP_064766070.1\t14.31811904122612"
            "\t6.906754778648663\tTrue\tTrue\tRemote defense homolog"
            "\tDS-12"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id PD3A "
            "to DS_name DS-12, marks the cloned transcriptional unit as "
            "defensive, and records NZ_RRVF01000002.1 positions "
            "104144-108678 with product accessions WP_059339975.1 and "
            "WP_064766070.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas25\t4.2\tpLAND\t24-05-17_EV_HHNH.png\t200000000"
            "\tPD3A\t24-05-17\t24-05-17_VAME_AAA1_PD3A_PDP7.png"
            "\t3\t2\t\t2000\t5\t\tTrue\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a PD3A "
            "assay row with a Bas25 phage readout and a -log(EOP) value "
            "of 5.0."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "PD3A\tDS-12\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps PD3A to "
            "replicated display name DS-12."
        ),
    }


def table_s8_abc_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PD3A\t1.0\t750.0\tWP_064766070.1\tABC ATPase\t3ZGX_B"
            "\tCHROMOSOME PARTITION PROTEIN SMC; CELL CYCLE; 3.4A "
            "{BACILLUS SUBTILIS}\thhpred_5638008.hhr\t495.0\t581.0"
            "\t1.0\t2024-05-21 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports an ABC "
            "ATPase HHpred hit for WP_064766070.1 in PD3A."
        ),
    }


def table_s8_pddexk_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PD3A\t2.0\t761.0\tWP_059339975.1\tPDDEXK\tcd22335"
            "\tMspjI-like; Modification-dependent restriction endonuclease "
            "MspjI and similar endonucleases.\thhpred_5143119.hhr\t4.0"
            "\t129.0\t0.98\t2024-07-30 00:00:00\t335-337\t322.0"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a PDDEXK "
            "HHpred hit for WP_059339975.1 in PD3A."
        ),
    }


def table_s8_nacht_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "PD3A\t2.0\t761.0\tWP_059339975.1\tNACHT\tPF20720.2"
            "\tnSTAND3 ; Novel STAND NTPase 3\thhpred_5143119.hhr"
            "\t174.0\t327.0\t0.99\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a NACHT "
            "HHpred hit for WP_059339975.1 in PD3A."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [
        table_s8_abc_evidence(),
        table_s8_pddexk_evidence(),
        table_s8_nacht_evidence(),
    ]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-12 system",
    "definition": (
        "A phage defense system in which an organism possesses the two-gene "
        "DefensePredictor-discovered system 12 locus cataloged as working "
        "transcriptional unit PD3A and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-12",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "PD3A",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-12__DS-12B",
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
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_12_locus_reduces_phage_plaquing",
            "title": "DS-12 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-12 locus to reduced bacteriophage plaquing without "
                "resolving DS-12 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-12 as the validated PD3A "
                "transcriptional unit with two product accessions, final "
                "Table S8 ABC ATPase, PDDEXK, and NACHT HHpred-domain "
                "rows, and one DefenseFinder DS-12B profile row. It does "
                "not assert native host breadth, DS-12A model coverage, "
                "exact DS-12B profile-to-protein correspondence, the "
                "direct viral trigger or substrate, exact ABC ATPase or "
                "nuclease chemistry, phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_12_locus",
                    "label": "DS-12 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-12B custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing by cells carrying "
                        "cloned PD3A."
                    ),
                },
                {
                    "node_id": "ds_12_system_trait",
                    "label": "DS-12 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-12 phage-defense "
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
                    "subject": "ds_12_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-12/PD3A locus contributes to reduced "
                        "bacteriophage plaquing when plasmid expressed."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_12_system_trait",
                    "description": (
                        "DS-12-mediated phage plaquing reduction realizes "
                        "the DS-12 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name each validated "
                                "transcriptional unit as a DefensePredictor "
                                "discovered system."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "ds_12_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-12 system possession is a phage-defense-system "
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
            "discussion_id": "ds-12-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-12 native host breadth, DS-12A model coverage, "
                "DS-12B profile-to-protein mapping, sensitive-phage "
                "breadth, direct viral trigger or substrate, exact ABC "
                "ATPase and PDDEXK/nSTAND nuclease chemistry, and "
                "rule-level detection criteria before minting narrower "
                "DS-12 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-12 as the defensive PD3A "
                "transcriptional unit that reduced Bas25 plaquing when "
                "cloned in E. coli MG1655, and the final Table S8 HHpred "
                "sheet reports ABC ATPase, PDDEXK, and NACHT hits across "
                "the two PD3A products. The pinned DefenseFinder HMM "
                "inventory records one DS-12B profile row, the pinned "
                "article registry names DS-12B rather than DS-12, the "
                "pinned rules table has no DS-12 row, and the first-pass "
                "record does not resolve native host breadth, DS-12A "
                "model coverage, exact profile-to-protein correspondence, "
                "direct ATPase or nuclease activity, phage target breadth, "
                "or endogenous DS-12 activity."
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
                        "DS-12, DS-12B, PD3A, or the PD3A product "
                        "accessions, leaving complete component coverage "
                        "and rule-level detection criteria unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_12_locus_reduces_phage_plaquing"],
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
            "Minted DS-12 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned PD3A "
            "transcriptional-unit level because the pinned DefenseFinder "
            f"DS-12B HMM row leaves DS-12A coverage unresolved and {PROPOSAL} "
            "reserves the replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-12 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned PD3A plaquing assays "
            "in E. coli MG1655 plus a partial DefenseFinder DS-12B model, "
            "but not a direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-12 activity. No paid "
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
        print(f"Wrote {rel}")
    else:
        import yaml

        print(yaml.safe_dump(record, sort_keys=False, allow_unicode=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
