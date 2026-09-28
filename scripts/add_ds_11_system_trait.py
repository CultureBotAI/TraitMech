#!/usr/bin/env python3
"""Add the DS-11 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_11_system.yaml"

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
TIMESTAMP = "2026-09-28T13:46:45Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T13:46:46Z"

IDENTIFIER = "traitmech:000435"
PROPOSAL = "proposals/metpo_traitmech_v312"

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
    "| DS-11 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-11__DS-11": (
        "| DS-11__DS-11                                     |"
        "                                                  | DS-11"
        "                  | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-11 "
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
            "custom DS-11 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "IMPD\tNZ_RRVY01000003.1\tGCF_003886375.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t365785\t366882"
            "\tCBS domain-containing protein\tWP_000257686.1"
            "\t4.37610109478113\t1.840433765255303\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-11"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id IMPD "
            "to DS_name DS-11, marks the cloned transcriptional unit as "
            "defensive, and records NZ_RRVY01000003.1 positions "
            "365785-366882 with product accession WP_000257686.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T3\t1.1\tpLAND\t24-03-08_NYND_PIN2_MHAD_EV.png\t300000000"
            "\tIMPD\t24-03-08\t24-03-08_MNAC_GHOS_BRNT_IMPD.png"
            "\t5\t3\t\t300000\t3\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an IMPD assay "
            "row with a T3 phage readout and a -log(EOP) value of 3.0."
        ),
    }


def table_s7_mutant_panel_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "T3\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t200000000\tIMPD\t\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t5\t4\t\t400000\t2.698970004\n"
            "Bas67\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tIMPD\t\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t5\t5\t\t500000\t1.602059991\n"
            "T3\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t200000000\tIMPD\tY157A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t8\t2\t\t200000000\t0\n"
            "Bas67\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tIMPD\tY157A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t7\t2\t\t20000000\t0\n"
            "T3\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t200000000\tIMPD\tR330A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t8\t3\t\t300000000\t-0.1760912591\n"
            "Bas67\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tIMPD\tR330A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t7\t3\t\t30000000\t-0.1760912591\n"
            "T3\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t200000000\tIMPD\tH335A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t8\t1\t\t100000000\t0.3010299957\n"
            "Bas67\tB.2\tMG1655\t24-07-17_AAA2_VPUS_VAME_EV.png"
            "\t20000000\tIMPD\tH335A\t24-07-18"
            "\t24-07-18_IMPD-Y157A_IMPD_IMPD-R330A_IMPD-H335A_HIPA_HIPA-D139A.png"
            "\t6\t6\t\t6000000\t0.5228787453"
        ),
        "notes": (
            "The final Science supplementary Table S7 System Mutants sheet "
            "pairs wild-type IMPD with IMPD Y157A, R330A, and H335A rows in "
            "T3 and Bas67 assay panels."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "IMPD\tDS-11\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps IMPD to "
            "replicated display name DS-11."
        ),
    }


def table_s8_hepn_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "IMPD\t1.0\t365.0\tWP_000257686.1\tHEPN\tPF18731.5"
            "\tHEPN_Swt1 ; Swt1-like HEPN\thhpred_1021051.hhr"
            "\t252.0\t359.0\t0.98\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a HEPN "
            "HHpred hit for WP_000257686.1 in IMPD."
        ),
    }


def table_s8_cbs_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "IMPD\t1.0\t365.0\tWP_000257686.1\tCBS\tcd04614"
            "\tCBS_pair_arch2_repeat2; Two tandem repeats of the "
            "cystathionine beta-synthase (CBS pair) domains present in "
            "archaea\thhpred_1021051.hhr\t134.0\t241.0\t0.9916"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a CBS "
            "HHpred hit for WP_000257686.1 in IMPD."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_hepn_evidence(), table_s8_cbs_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-11 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 11 locus cataloged "
        "as working transcriptional unit IMPD and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-11",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "IMPD",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-11__DS-11",
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
        table_s7_mutant_panel_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_11_locus_reduces_phage_plaquing",
            "title": "DS-11 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-11 locus to reduced bacteriophage plaquing without "
                "resolving DS-11 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-11 as the validated IMPD "
                "transcriptional unit with one product accession, final "
                "Table S8 HEPN and CBS HHpred-domain rows, and one "
                "DefenseFinder DS-11 profile row. It does not assert "
                "native host breadth, exact profile-to-protein "
                "correspondence, the direct viral trigger or ligand, the "
                "HEPN substrate, whether ATP binding or CBS-ligand binding "
                "activates the effector, phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_11_locus",
                    "label": "DS-11 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-11 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage T3 "
                        "in cells carrying cloned IMPD."
                    ),
                },
                {
                    "node_id": "ds_11_system_trait",
                    "label": "DS-11 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-11 phage-defense "
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
                    "subject": "ds_11_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-11/IMPD locus contributes to reduced "
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
                    "object": "ds_11_system_trait",
                    "description": (
                        "DS-11-mediated phage plaquing reduction realizes "
                        "the DS-11 system trait."
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
                    "subject": "ds_11_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-11 system possession is a phage-defense-system "
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
            "discussion_id": "ds-11-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-11 native host breadth, profile-to-protein "
                "mapping, sensitive-phage breadth, direct viral trigger, "
                "direct HEPN-family nuclease substrate, CBS-ligand or "
                "ATP-dependent activation model, and rule-level detection "
                "criteria before minting narrower DS-11 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-11 as the defensive IMPD "
                "transcriptional unit that reduced T3 and Bas67 plaquing "
                "when cloned in E. coli MG1655, and the final Table S8 "
                "HHpred sheet reports HEPN and CBS hits for the single IMPD "
                "product. The pinned DefenseFinder HMM inventory records "
                "one DS-11 profile row, the pinned rules table has no DS-11 "
                "row, and the first-pass record does not resolve native "
                "host breadth, exact profile-to-protein correspondence, "
                "the direct HEPN substrate, the activation ligand, phage "
                "target breadth, or endogenous DS-11 activity."
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
                table_s7_mutant_panel_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-11, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_11_locus_reduces_phage_plaquing"],
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
            "Minted DS-11 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned IMPD "
            "transcriptional-unit level because HEPN/CBS domain and mutant "
            "readouts do not resolve native DS-11 activation or effector "
            f"chemistry and {PROPOSAL} reserves the replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-11 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned IMPD plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-11 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-11 activity. No paid "
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
