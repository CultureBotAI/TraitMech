#!/usr/bin/env python3
"""Add the DS-8 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_8_system.yaml"

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
TIMESTAMP = "2026-09-28T10:43:27Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T10:43:28Z"
REVIEW_FIX_TIMESTAMP = "2026-09-28T11:24:51Z"

IDENTIFIER = "traitmech:000432"
PROPOSAL = "proposals/metpo_traitmech_v309"

DS_VALIDATION_SNIPPET = (
    "To test for anti-phage defense, we placed each TU with its predicted "
    "native promoter region on a low-copy number plasmid in E. coli MG1655 "
    "and challenged these strains with a panel of 24 diverse E. coli phages "
    "(Fig. 3; fig. S2). In total, 42 (45% of 94) of the cloned TUs produced "
    "smaller plaque sizes or reduced the efficiency of plating (EOP) at "
    "least ten-fold relative to an empty vector control strain"
)
DS_SINGLE_PROTEIN_SNIPPET = (
    "First, we investigated DS-8, a single protein system containing a "
    "metallophosphatase domain (Fig. 5A) which is homologous to the human "
    "protein SMPDL3A, a phosphodiesterase that cleaves cGAMP to modulate "
    "cGAS-STING immunity signaling"
)
DS_MUTANT_SNIPPET = (
    "Mutating either of two predicted catalytic residues in the "
    "metallophosphatase domain or a residue likely critical to NACHT ATPase "
    "activity completely ablated defense by DS-8, indicating that both "
    "domains and metallophosphatase activity are essential for protection"
)
ARTICLE_ROW = (
    "| DS-8 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-8__DS-8": (
        "| DS-8__DS-8                                       |"
        "                                                  | DS-8"
        "                   | Custom                  | 200    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-8 "
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
            "custom DS-8 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "MNAC\tNZ_RRWS01000004.1\tGCF_003892555.1\t-\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t83803\t86847"
            "\tmetallophosphoesterase\tWP_032203427.1"
            "\t9.394229333124514\t6.212606095751518\tTrue\tTrue"
            "\tPredicted novel defense gene\tDS-8"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id MNAC "
            "to DS_name DS-8, marks the cloned transcriptional unit as "
            "defensive, and records NZ_RRWS01000004.1 positions 83803-86847 "
            "with product accession WP_032203427.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "Bas1\t1.2\tpLAND\t24-03-08_EV_HHHD_PIN2_CRDO.png"
            "\t40000000\tMNAC\t24-03-08"
            "\t24-03-08_MNAC_GHOS_BRNT_IMPD.png\t1\t10\tY\t100"
            "\t5.6020599913279625\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports an MNAC assay "
            "row with a Bas1 phage readout and a -log(EOP) value of 5.602."
        ),
    }


MNAC_MUTANT_ROWS = {
    "K375A": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMNAC\tK375A\t24-07-10"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t6\t3\t\t3000000\t0"
    ),
    "N84A": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMNAC\tN84A\t24-07-10"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t6\t2\t\t2000000\t0.1760912591"
    ),
    "D52A": (
        "Bas1\tA.1\tMG1655"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t3000000\tMNAC\tD52A\t24-07-10"
        "\t24-07-10_EV_MNAC-K375A_MNAC-N84A_MNAC-D52A.png"
        "\t6\t4\t\t4000000\t-0.1249387366"
    ),
}

MNAC_MUTANT_MINUS_LOG_EOPS = {
    "K375A": "0",
    "N84A": "0.176",
    "D52A": "-0.125",
}


def table_s7_mnac_mutant_evidence(mutation: str) -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": MNAC_MUTANT_ROWS[mutation],
        "notes": (
            "The final Science supplementary Table S7 reports the MNAC "
            f"{mutation} Bas1 mutant row with a -log(EOP) value of "
            f"{MNAC_MUTANT_MINUS_LOG_EOPS[mutation]}."
        ),
    }


def all_table_s7_mnac_mutant_evidence() -> list[dict[str, str]]:
    return [table_s7_mnac_mutant_evidence(mutation) for mutation in MNAC_MUTANT_ROWS]


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "MNAC\tDS-8\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps MNAC to "
            "replicated display name DS-8."
        ),
    }


def table_s8_metallophosphatase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "MNAC\t1.0\t1014.0\tWP_032203427.1\tMetallophosphatase"
            "\t5KAR_A\tAcid sphingomyelinase-like phosphodiesterase 3b; "
            "phosphoesterase, extracellular, membrane"
            "\thhpred_8521728.hhr\t1.0\t275.0\t0.997"
            "\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "metallophosphatase HHpred hit for WP_032203427.1 in MNAC."
        ),
    }


def table_s8_nacht_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "MNAC\t1.0\t1014.0\tWP_032203427.1\tNACHT\t8FML_A"
            "\tBaculoviral IAP repeat-containing protein 1e; Inflammasome, "
            "Innate immunity, Bacterial ligand, host-pathogen interaction, "
            "Protein complex, IMMUNE SYSTEM\thhpred_8521728.hhr"
            "\t331.0\t734.0\t1.0\t2024-04-16 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a NACHT "
            "HHpred hit for WP_032203427.1 in MNAC."
        ),
    }


def all_hhpred_evidence() -> list[dict[str, str]]:
    return [table_s8_metallophosphatase_evidence(), table_s8_nacht_evidence()]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-8 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "single-gene DefensePredictor-discovered system 8 locus cataloged "
        "with working_id MNAC and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-8",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "MNAC",
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
            "snippet": DS_SINGLE_PROTEIN_SNIPPET,
            "notes": (
                "DeWeirdt et al. identify DS-8 as a single-protein "
                "metallophosphatase-domain system."
            ),
        },
        {
            "reference": DEWEIRDT,
            "snippet": DS_MUTANT_SNIPPET,
            "notes": (
                "DeWeirdt et al. report that predicted metallophosphatase "
                "catalytic-residue and NACHT ATPase-residue mutations "
                "ablated DS-8 defense."
            ),
        },
        table_s6_evidence(),
        table_s7_evidence(),
        *all_table_s7_mnac_mutant_evidence(),
        table_s8_display_evidence(),
        *all_hhpred_evidence(),
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_8_locus_reduces_phage_plaquing",
            "title": "DS-8 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the single-gene "
                "DS-8 locus to reduced bacteriophage plaquing without "
                "resolving DS-8 component function or effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-8 as the validated MNAC "
                "transcriptional unit with one product accession and with a "
                "DefenseFinder DS-8 profile row. It does not assert native "
                "host breadth, exact profile-to-protein correspondence, the "
                "direct viral trigger or cyclic-nucleotide substrate, the "
                "exact NACHT-mediated activation step, relationship to "
                "NLR-like bNACHT systems, phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_8_locus",
                    "label": "DS-8 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DefensePredictor-discovered system "
                        "locus represented in the pinned DefenseFinder HMM "
                        "inventory by one DS-8 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophage "
                        "Bas1 in cells carrying cloned MNAC."
                    ),
                },
                {
                    "node_id": "ds_8_system_trait",
                    "label": "DS-8 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-8 phage-defense "
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
                    "subject": "ds_8_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-8/MNAC locus contributes to reduced "
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
                    "object": "ds_8_system_trait",
                    "description": (
                        "DS-8-mediated phage plaquing reduction realizes "
                        "the DS-8 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS_SINGLE_PROTEIN_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. identify DS-8 as a "
                                "single-protein metallophosphatase-domain "
                                "system."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                    ],
                },
                {
                    "subject": "ds_8_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-8 system possession is a phage-defense-system "
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
            "discussion_id": "ds-8-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-8 native host breadth, DS-8 "
                "profile-to-protein mapping, sensitive-phage breadth, "
                "direct cyclic-nucleotide substrate, NACHT-mediated "
                "activation route, relationship to NLR-like bNACHT systems, "
                "and "
                "rule-level detection criteria before minting narrower DS-8 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-8 as the defensive MNAC "
                "transcriptional unit that reduced Bas1 plaquing when "
                "cloned in E. coli MG1655, identify DS-8 as a "
                "single-protein system with metallophosphatase and NACHT "
                "domains, and report that D52A, N84A, and K375A mutations "
                "ablated Bas1 protection. The pinned DefenseFinder HMM "
                "inventory records one DS-8 profile row. The pinned rules "
                "table has no DS-8 row, and the first-pass record does not "
                "resolve native host breadth, exact profile-to-protein "
                "correspondence, direct cyclic-nucleotide substrate, exact "
                "NACHT-mediated activation route, phage target breadth, "
                "endogenous DS-8 activity, or whether DS-8 should be "
                "related to the broader NLR-like bNACHT system family."
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
                    "snippet": DS_SINGLE_PROTEIN_SNIPPET,
                    "notes": "DeWeirdt et al. identify DS-8 as single-protein.",
                },
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_MUTANT_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. state that DS-8 "
                        "metallophosphatase and NACHT catalytic mutants "
                        "ablate defense."
                    ),
                },
                table_s6_evidence(),
                table_s7_evidence(),
                *all_table_s7_mnac_mutant_evidence(),
                table_s8_display_evidence(),
                *all_hhpred_evidence(),
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-8, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_8_locus_reduces_phage_plaquing"],
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
            "Minted DS-8 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned MNAC "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-8 HMM row is not backed by a rules row; "
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
            "Reviewed DS-8 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned MNAC plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-8 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-8 activity. No paid "
            "research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_REVIEW_FINDINGS",
        changes=(
            "Addressed PR review issues #1397 and #1398 by replacing the "
            "ambiguous generic DS naming quote with DS-8-specific "
            "single-protein and catalytic-mutant article snippets, adding "
            "final Science Table S7 MNAC K375A/N84A/D52A Bas1 mutant "
            "evidence, and narrowing the open DS-8 knowledge gap to "
            "substrate identity, NACHT-mediated activation route, "
            "native-host and phage breadth, exact profile mapping, and "
            "DefenseFinder rule-level criteria."
        ),
        llm_assisted=True,
        timestamp=REVIEW_FIX_TIMESTAMP,
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
