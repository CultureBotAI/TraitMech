#!/usr/bin/env python3
"""Add the DS-9 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_9_system.yaml"

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
TIMESTAMP = "2026-09-28T12:06:48Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T12:06:49Z"

IDENTIFIER = "traitmech:000433"
PROPOSAL = "proposals/metpo_traitmech_v310"

DS_VALIDATION_SNIPPET = (
    "To test for anti-phage defense, we placed each TU with its predicted "
    "native promoter region on a low-copy number plasmid in E. coli MG1655 "
    "and challenged these strains with a panel of 24 diverse E. coli phages "
    "(Fig. 3; fig. S2). In total, 42 (45% of 94) of the cloned TUs produced "
    "smaller plaque sizes or reduced the efficiency of plating (EOP) at "
    "least ten-fold relative to an empty vector control strain"
)
DS_9_DOMAIN_SNIPPET = (
    "The system DS-9 has two genes, the first harboring a "
    "metallophosphatase domain homologous to that of DS-8, and the second "
    "a predicted haloacid dehalogenase-like (HAD) phosphatase"
)
DS_9_MUTANT_SNIPPET = (
    "When we mutated the predicted catalytic residues in the "
    "metallophosphatase domain of DS-9A, we saw a loss of defense, "
    "suggesting it is essential for protection"
)
ARTICLE_ROW = (
    "| DS-9 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-9__DS-9A": (
        "| DS-9__DS-9A                                      |"
        "                                                  | DS-9"
        "                   | Custom                  | 300    |"
    ),
    "DS-9__DS-9B": (
        "| DS-9__DS-9B                                      |"
        "                                                  | DS-9"
        "                   | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-9 "
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
            "custom DS-9 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "MHAD\tNZ_QOWZ01000056.1\tGCF_003334705.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t6224\t8706"
            "\tHAD-IA family hydrolase, metallophosphoesterase"
            "\tWP_000770925.1, WP_000665639.1\t4.506698206217075"
            "\t6.906754778648663\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-9"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id MHAD "
            "to DS_name DS-9, marks the cloned transcriptional unit as "
            "defensive, and records NZ_QOWZ01000056.1 positions 6224-8706 "
            "with product accessions WP_000770925.1 and WP_000665639.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t40000000\tMHAD\t24-03-08"
            "\t24-03-08_NYND_GHOS_MHAD_UDNG.png\t3\t3\t\t3000"
            "\t4.1249387366083\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an MHAD assay "
            "row with a Bas1 phage readout and a -log(EOP) value of 4.125."
        ),
    }


MHAD_BAS1_MUTANT_ROWS = {
    "WT": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMHAD\t\t24-07-17"
        "\t24-07-17_PN12-dACR_PN12_MHAD_MHAD-D207A_MHAD-N292A.png"
        "\t2\t8\t\t800\t3.574031268"
    ),
    "D207A": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMHAD\tD207A\t24-07-17"
        "\t24-07-17_PN12-dACR_PN12_MHAD_MHAD-D207A_MHAD-N292A.png"
        "\t6\t3\t\t3000000\t0"
    ),
    "N292A": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMHAD\tN292A\t24-07-17"
        "\t24-07-17_PN12-dACR_PN12_MHAD_MHAD-D207A_MHAD-N292A.png"
        "\t6\t2\t\t2000000\t0.1760912591"
    ),
}

MHAD_BAS1_MINUS_LOG_EOPS = {
    "WT": "3.574",
    "D207A": "0",
    "N292A": "0.176",
}


def table_s7_mhad_bas1_mutant_panel_evidence(variant: str) -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": MHAD_BAS1_MUTANT_ROWS[variant],
        "notes": (
            "The final Science supplementary Table S7 reports the MHAD "
            f"{variant} Bas1 mutant-panel row with a -log(EOP) value of "
            f"{MHAD_BAS1_MINUS_LOG_EOPS[variant]}."
        ),
    }


def all_table_s7_mhad_mutant_panel_evidence() -> list[dict[str, str]]:
    return [
        table_s7_mhad_bas1_mutant_panel_evidence(variant)
        for variant in MHAD_BAS1_MUTANT_ROWS
    ]


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "MHAD\tDS-9\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps MHAD to "
            "replicated display name DS-9."
        ),
    }


def table_s8_had_phosphatase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "MHAD\t2.0\t278.0\tWP_000770925.1\tHAD phosphatase"
            "\tcd02616\tHAD_PPase; pyrophosphatase"
            "\thhpred_3345609.hhr\t1.0\t277.0\t0.999"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a HAD "
            "phosphatase HHpred hit for WP_000770925.1 in MHAD."
        ),
    }


def table_s8_metallophosphatase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "MHAD\t1.0\t549.0\tWP_000665639.1\tMetallophosphatase"
            "\tcd07378\tMPP_ACP5; Homo sapiens acid phosphatase 5 and "
            "related proteins, metallophosphatase domain."
            "\thhpred_3407490.hhr\t200.0\t533.0\t0.9983"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "metallophosphatase HHpred hit for WP_000665639.1 in MHAD."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_had_phosphatase_evidence(), table_s8_metallophosphatase_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-9 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "two-gene DefensePredictor-discovered system 9 locus cataloged "
        "with working_id MHAD and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-9",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "MHAD",
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
            "snippet": DS_9_DOMAIN_SNIPPET,
            "notes": (
                "DeWeirdt et al. identify DS-9 as a two-gene system with "
                "metallophosphatase and HAD phosphatase domains."
            ),
        },
        {
            "reference": DEWEIRDT,
            "snippet": DS_9_MUTANT_SNIPPET,
            "notes": (
                "DeWeirdt et al. report that predicted DS-9A "
                "metallophosphatase catalytic-residue mutations caused a "
                "loss of defense."
            ),
        },
        table_s6_evidence(),
        table_s7_evidence(),
        *all_table_s7_mhad_mutant_panel_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_9_locus_reduces_phage_plaquing",
            "title": "DS-9 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the two-gene "
                "DS-9 locus to reduced bacteriophage plaquing without "
                "resolving DS-9 component functions or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-9 as the validated MHAD "
                "transcriptional unit with two product accessions and with "
                "DefenseFinder DS-9A and DS-9B profile rows. It does not "
                "assert native host breadth, exact DS-9A/DS-9B "
                "profile-to-protein correspondence, the direct viral "
                "trigger or metallophosphoesterase substrate, the HAD "
                "phosphatase target, phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_9_locus",
                    "label": "DS-9 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by DS-9A and DS-9B custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas1 in cells carrying cloned MHAD."
                    ),
                },
                {
                    "node_id": "ds_9_system_trait",
                    "label": "DS-9 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-9 phage-defense "
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
                    "subject": "ds_9_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-9/MHAD locus contributes to reduced "
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
                    "object": "ds_9_system_trait",
                    "description": (
                        "DS-9-mediated phage plaquing reduction realizes "
                        "the DS-9 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_9_DOMAIN_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. identify DS-9 as a "
                                "two-gene metallophosphatase/HAD-phosphatase "
                                "system."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "ds_9_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-9 system possession is a phage-defense-system "
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
            "discussion_id": "ds-9-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-9 native host breadth, DS-9A/DS-9B "
                "profile-to-protein mapping, sensitive-phage breadth, "
                "direct metallophosphoesterase substrate, HAD phosphatase "
                "target, and rule-level detection criteria before minting "
                "narrower DS-9 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-9 as the defensive MHAD "
                "transcriptional unit that reduced Bas1 plaquing when "
                "cloned in E. coli MG1655, identify DS-9 as a two-gene "
                "system with metallophosphatase and HAD phosphatase "
                "domains, and report that DS-9A predicted "
                "catalytic-residue mutations caused a loss of defense. "
                "Final Science Table S7 mutant rows show D207A and N292A "
                "Bas1 protection loss relative to wild-type MHAD in a "
                "matched panel. The pinned DefenseFinder HMM inventory "
                "records two DS-9 profile rows. The pinned rules table has "
                "no DS-9 row, and the first-pass record does not resolve "
                "native host breadth, exact DS-9A/DS-9B profile-to-protein "
                "correspondence, direct metallophosphoesterase substrate, "
                "HAD phosphatase target, phage target breadth, endogenous "
                "DS-9 activity, or DefenseFinder rule-level detection "
                "criteria."
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
                    "snippet": DS_9_DOMAIN_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. identify DS-9 as a two-gene "
                        "system."
                    ),
                },
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_9_MUTANT_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. state that DS-9A "
                        "metallophosphatase catalytic mutants lose defense."
                    ),
                },
                table_s6_evidence(),
                table_s7_evidence(),
                *all_table_s7_mhad_mutant_panel_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-9, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_9_locus_reduces_phage_plaquing"],
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
            "Minted DS-9 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned MHAD "
            "transcriptional-unit level because the DS-9A/DS-9B "
            "profile-to-protein mapping and rule-level DefenseFinder model "
            f"remain unresolved; {PROPOSAL} reserves the replacement "
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
            "Reviewed DS-9 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned MHAD plaquing assays in "
            "E. coli MG1655 plus DefenseFinder DS-9 model rows, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-9 activity. No paid "
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
