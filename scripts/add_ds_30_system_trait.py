#!/usr/bin/env python3
"""Add the DS-30 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_30_system.yaml"

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
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-29T17:57:26Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T17:57:27Z"

IDENTIFIER = "traitmech:000470"
PROPOSAL = "proposals/metpo_traitmech_v347"
LAMASSU_SYSTEM = "traitmech:000232"

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
HMM_ROWS = {
    "Lamassu-Fam__Lmu_DS-30A": (
        "| Lamassu-Fam__Lmu_DS-30A                          |"
        "                                                  | Lamassu-Fam"
        "            | Custom                  | 50     |"
    ),
    "Lamassu-Fam__LmuA_DS-30B": (
        "| Lamassu-Fam__LmuA_DS-30B                         |"
        "                                                  | Lamassu-Fam"
        "            | Custom                  | 60     |"
    ),
    "Lamassu-Fam__LmuB_DS-30D": (
        "| Lamassu-Fam__LmuB_DS-30D                         |"
        "                                                  | Lamassu-Fam"
        "            | Custom                  | 150    |"
    ),
    "Lamassu-Fam__LmuC_DS-30C": (
        "| Lamassu-Fam__LmuC_DS-30C                         |"
        "                                                  | Lamassu-Fam"
        "            | Custom                  | 20     |"
    ),
}


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "ABC3\tNZ_QOYR01000032.1\tGCF_003333645.1\t+\tTrue"
            "\tFalse\tTrue\tTrue\tDefensePredictor hits\t1906\t4621"
            "\thypothetical protein, hypothetical protein, hypothetical "
            "protein, DUF2326 domain-containing protein"
            "\tWP_001553315.1, WP_000534626.1, WP_000628292.1, "
            "WP_087889773.1\t8.95063706554687\t6.906754778648663"
            "\tTrue\tTrue\tPredicted novel defense gene\tDS-30"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id ABC3 "
            "to DS_name DS-30, marks the cloned transcriptional unit as "
            "defensive, and records four product accessions in "
            "NZ_QOYR01000032.1 positions 1906-4621."
        ),
    }


def table_s7_secphi27_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "SECphi27\t5.1\tpLAND\t24-05-31_EV_CRDO_BRNT_ABC3.png"
            "\t100000000\tABC3\t24-05-31"
            "\t24-05-31_EV_CRDO_BRNT_ABC3.png\t5\t1\tY\t100000"
            "\t3\t\tTrue\t\tM9\t30"
        ),
        "notes": (
            "The final Science supplementary Table S7 Systems sheet reports "
            "an ABC3 assay row with a SECphi27 phage readout, a "
            "smaller-plaque-size call, and a -log(EOP) value of 3."
        ),
    }


def table_s8_display_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "ABC3\tDS-30\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps ABC3 to "
            "replicated display name DS-30."
        ),
    }


def table_s8_hhpred_ctd10_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ABC3\t2.0\t182.0\tWP_000534626.1\tABC-3C C-term"
            "\tPF20275.3\tCTD10 ; C-terminal domain 10 of the ABC-three "
            "component (ABC-3C) systems\thhpred_7102862.hhr\t26.0"
            "\t176.0\t1.0\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability CTD10 HHpred hit for ABC3 protein 2, "
            "WP_000534626.1."
        ),
    }


def table_s8_hhpred_mc6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ABC3\t3.0\t77.0\tWP_000628292.1\tABC-3C Mid\tPF20293.3"
            "\tMC6 ; ABC-three component (ABC-3C) system Middle Component 6"
            "\thhpred_3406401.hhr\t1.0\t75.0\t1.0"
            "\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability MC6 HHpred hit for ABC3 protein 3, "
            "WP_000628292.1."
        ),
    }


def table_s8_hhpred_abc_atpase_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ABC3\t4.0\t565.0\tWP_087889773.1\tABC ATPase\t5XEI_A"
            "\tChromosome partition protein Smc; Condensin, Smc, head "
            "domain, ABC-ATPase,\thhpred_6417130.hhr\t1.0\t540.0"
            "\t1.0\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports a "
            "high-probability ABC ATPase HHpred hit for ABC3 protein 4, "
            "WP_087889773.1."
        ),
    }


def table_s8_hhpred_ftsl_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": (
            "ABC3\t1.0\t86.0\tWP_001553315.1\tFtsL\t8HHF_L"
            "\tCell division protein FtsL; Bacterial cell division, "
            "divisome, FtsB, FtsL, FtsQ, FtsBLQ, membrane protein complex, "
            "heterotrimer, MEMBRANE PROTEIN\thhpred_2515914.hhr\t2.0"
            "\t53.0\t0.942\t2024-07-30 00:00:00"
        ),
        "notes": (
            "The final Science supplementary Table S8 reports an FtsL "
            "HHpred hit for ABC3 protein 1, WP_001553315.1."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            f"{profile} as a custom Lamassu-Fam profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-30 system",
    "definition": (
        "A phage defense system in which an organism possesses the "
        "four-gene DefensePredictor-discovered system 30 locus cataloged "
        "as working transcriptional unit ABC3 and whose plasmid expression "
        "in E. coli MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [LAMASSU_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "DS-30",
            "synonym_type": "EXACT_SYNONYM",
            "source": TABLE_S8,
        },
        {
            "synonym_text": "ABC3",
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
        table_s7_secphi27_evidence(),
        table_s8_display_evidence(),
        table_s8_hhpred_ctd10_evidence(),
        table_s8_hhpred_mc6_evidence(),
        table_s8_hhpred_abc_atpase_evidence(),
        table_s8_hhpred_ftsl_evidence(),
        *[hmm_inventory_evidence(profile) for profile in HMM_ROWS],
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_30_locus_reduces_phage_plaquing",
            "title": "DS-30 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the four-gene "
                "DS-30 locus to reduced bacteriophage plaquing without "
                "resolving DS-30 component functions or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-30 as the validated ABC3 "
                "transcriptional unit with four product accessions, ABC-3C, "
                "SMC-family, and FtsL HHpred-domain rows, and four "
                "Lamassu-Fam custom HMM-profile rows. It does not assert "
                "native host breadth, exact profile-to-protein "
                "correspondence, DS-30/Lamassu-Fam component activity, "
                "Lamassu subtype chemistry, LmuC requirement, complete "
                "phage breadth, or DS-30-specific DefenseFinder rule-level "
                "detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_30_locus",
                    "label": "DS-30 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A four-gene DefensePredictor-discovered system 30 "
                        "locus cataloged as ABC3 and represented in the "
                        "pinned DefenseFinder HMM inventory by four "
                        "Lamassu-Fam DS-30 custom profiles."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage plaquing in cells carrying "
                        "cloned ABC3."
                    ),
                },
                {
                    "node_id": "ds_30_system_trait",
                    "label": "DS-30 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-30 Lamassu-family "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "lamassu_system",
                    "label": "Lamassu system",
                    "node_type": "TRAIT",
                    "grounding": LAMASSU_SYSTEM,
                    "description": (
                        "Possession of a genome-encoded Lamassu "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "ds_30_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-30/ABC3 locus contributes to reduced "
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
                        table_s7_secphi27_evidence(),
                        table_s8_display_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_30_system_trait",
                    "description": (
                        "DS-30-mediated phage plaquing reduction realizes "
                        "the DS-30 system trait."
                    ),
                    "evidence": [
                        table_s6_evidence(),
                        table_s7_secphi27_evidence(),
                        table_s8_display_evidence(),
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
                    "subject": "ds_30_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "lamassu_system",
                    "description": (
                        "DS-30 system possession is represented in "
                        "DefenseFinder by DS-30 custom profiles under "
                        "Lamassu-Fam."
                    ),
                    "evidence": [
                        *[
                            hmm_inventory_evidence(profile)
                            for profile in HMM_ROWS
                        ],
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ds-30-lamassu-family-model-gap",
            "prompt": (
                "Resolve DS-30 native host breadth, exact "
                "profile-to-protein correspondence, DS-30/Lamassu-Fam "
                "component activities, Lamassu subtype and effector "
                "chemistry, LmuC requirement, complete phage breadth, and "
                "DS-30-specific DefenseFinder rule-level criteria before "
                "minting narrower DS-30 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-30 as the defensive ABC3 "
                "transcriptional unit and final Science Tables S6/S7/S8 "
                "map it to four product accessions, a SECphi27 phage "
                "readout, four HHpred-domain rows, and display name DS-30. "
                "The pinned DefenseFinder HMM inventory records four "
                "Lamassu-Fam DS-30 custom profile rows. The pinned "
                "DefenseFinder rules table only lists generic Lamassu-Fam "
                "effector-subtype rows, and the first-pass record does not "
                "resolve native host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, LmuC requirement, "
                "molecular output, subtype-specific Lamassu chemistry, or "
                "endogenous DS-30 activity."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                table_s6_evidence(),
                table_s7_secphi27_evidence(),
                table_s8_display_evidence(),
                table_s8_hhpred_ctd10_evidence(),
                table_s8_hhpred_mc6_evidence(),
                table_s8_hhpred_abc_atpase_evidence(),
                table_s8_hhpred_ftsl_evidence(),
                *[hmm_inventory_evidence(profile) for profile in HMM_ROWS],
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table contains "
                        "generic Lamassu-Fam subtype rows, but no "
                        "DS-30-specific model row or DS-30 custom-profile "
                        "criteria."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_30_locus_reduces_phage_plaquing"],
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
            "Minted DS-30 system as a DOI-backed GENOMICS TraitRecord "
            "under Lamassu system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or "
            "prior proposal record; kept the graph at ABC3 "
            "transcriptional-unit level because native host breadth, exact "
            "DS-30 profile-to-component mapping, Lamassu subtype "
            "chemistry, LmuC requirement, complete phage breadth, and "
            "DefenseFinder rule-level criteria remain unresolved, and "
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
            "Reviewed DS-30 system canonical_examples and left them empty "
            "because DeWeirdt et al. directly support cloned ABC3 assays "
            "in E. coli MG1655 and Lamassu-Fam DS-30 profile rows, but "
            "not a direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-30 activity. No paid "
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
