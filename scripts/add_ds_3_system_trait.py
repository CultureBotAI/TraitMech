#!/usr/bin/env python3
"""Add the DS-3 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_3_system.yaml"

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
TIMESTAMP = "2026-09-28T05:06:03Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T05:06:04Z"

IDENTIFIER = "traitmech:000426"
PROPOSAL = "proposals/metpo_traitmech_v303"

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
DS3_PIN_SNIPPET = (
    "DS-3 is a one-protein system with a PIN ribonuclease domain split "
    "between its N and C-terminus"
)
DS3_MUTATION_SNIPPET = (
    "When we mutated catalytic residues in DS-3, the system no longer "
    "defended against phage, suggesting this domain is essential for "
    "protection."
)
ARTICLE_ROW = (
    "| DS-3 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPET = (
    "| DS-3__DS-3                                       |"
    "                                                  | DS-3"
    "                   | Custom                  | 50     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-3 source "
            "key to the preprint DOI for the DeWeirdt et al. "
            "DefensePredictor study, which has since been published in "
            "Science."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DS-3__DS-3 as a "
            "custom DS-3 profile."
        ),
    }


def table_s6_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S6,
        "snippet": (
            "PIN8\tNZ_RRWT01000005.1\tGCF_003892645.1\t+\tTrue"
            "\tFalse\tFalse\tTrue\tDefensePredictor hits\t244326"
            "\t245348\thypothetical protein\tWP_022645725.1"
            "\t8.909458355458062\t-2.350827761940385\tTrue"
            "\tFalse\tPredicted novel defense gene\tDS-3"
        ),
        "notes": (
            "The final Science supplementary Table S6 maps working_id PIN8 "
            "to DS_name DS-3, marks the cloned transcriptional unit as "
            "defensive, and records NZ_RRWT01000005.1 positions "
            "244326-245348 with product accession WP_022645725.1."
        ),
    }


def table_s7_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S7,
        "snippet": (
            "RB69\t1.1\tpLAND\t24-03-08_NYND_PIN2_MHAD_EV.png"
            "\t400000\tPIN8\t24-03-12"
            "\t24-03-12_PIN8_D390_NADR_PN12.png\t0\t1\t\t1"
            "\t5.6020599913279625\tTrue\t\t\tLB\t37"
        ),
        "notes": (
            "The final Science supplementary Table S7 reports a PIN8 assay "
            "row with an RB69 readout and a -log(EOP) value of 5.602."
        ),
    }


def table_s8_evidence() -> dict[str, str]:
    return {
        "reference": TABLE_S8,
        "snippet": "PIN8\tDS-3\tTrue",
        "notes": (
            "The final Science supplementary Table S8 maps PIN8 to "
            "replicated display name DS-3."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-3 system",
    "definition": (
        "A phage defense system in which an organism possesses the one-gene "
        "DefensePredictor-discovered system 3 locus cataloged as working "
        "transcriptional unit PIN8 and whose plasmid expression in E. coli "
        "MG1655 reduced bacteriophage plaquing."
    ),
    "definition_source": DEWEIRDT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DS-3",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEWEIRDT,
        },
        {
            "synonym_text": "PIN8",
            "synonym_type": "RELATED_SYNONYM",
            "source": TABLE_S6,
        },
        {
            "synonym_text": "DS-3__DS-3",
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
        {
            "reference": DEWEIRDT,
            "snippet": DS3_PIN_SNIPPET,
            "notes": (
                "DeWeirdt et al. describe DS-3 as a one-protein PIN "
                "ribonuclease-domain system."
            ),
        },
        {
            "reference": DEWEIRDT,
            "snippet": DS3_MUTATION_SNIPPET,
            "notes": (
                "DeWeirdt et al. report that mutating predicted catalytic "
                "residues removed DS-3-mediated phage defense."
            ),
        },
        table_s6_evidence(),
        table_s7_evidence(),
        table_s8_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_3_locus_reduces_phage_plaquing",
            "title": "DS-3 locus reduces bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking the one-gene DS-3 "
                "locus to reduced bacteriophage plaquing without resolving "
                "DS-3 effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-3 as the validated PIN8 "
                "transcriptional unit with one product accession and with a "
                "DefenseFinder DS-3 profile row. It does not assert native "
                "host breadth, exact profile-to-protein correspondence, the "
                "direct viral trigger or substrate, exact molecular output, "
                "phage target breadth, or DefenseFinder rule-level detection "
                "criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_3_locus",
                    "label": "DS-3 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A one-gene DefensePredictor-discovered system locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by a custom DS-3 profile."
                    ),
                },
                {
                    "node_id": "reduced_phage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing or reduced plaque "
                        "size by bacteriophages in cells carrying cloned "
                        "PIN8."
                    ),
                },
                {
                    "node_id": "ds_3_system_trait",
                    "label": "DS-3 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-3 phage-defense "
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
                    "subject": "ds_3_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_phage_plaquing",
                    "description": (
                        "The DS-3/PIN8 locus contributes to reduced "
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
                        {
                            "reference": DEWEIRDT,
                            "snippet": DS3_MUTATION_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. show DS-3 protection "
                                "depends on predicted catalytic residues."
                            ),
                        },
                        table_s6_evidence(),
                        table_s7_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ds_3_system_trait",
                    "description": (
                        "DS-3-mediated phage plaquing reduction realizes the "
                        "DS-3 system trait."
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
                    "subject": "ds_3_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-3 system possession is a phage-defense-system "
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
            "discussion_id": "ds-3-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-3 native host breadth, exact PIN ribonuclease "
                "activity, DS-3 profile-to-protein mapping, sensitive-phage "
                "breadth, molecular output, and rule-level detection "
                "criteria before minting narrower DS-3 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DeWeirdt et al. support DS-3 as the defensive PIN8 "
                "transcriptional unit that reduced plaquing when cloned in "
                "E. coli MG1655, and the pinned DefenseFinder HMM inventory "
                "records a DS-3 profile row. The pinned rules table has no "
                "DS-3 row, and the first-pass record does not resolve native "
                "host breadth, exact PIN substrate or output, profile-to-"
                "protein mapping, phage target breadth, or endogenous DS-3 "
                "activity."
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
                {
                    "reference": DEWEIRDT,
                    "snippet": DS3_PIN_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. report a split PIN ribonuclease "
                        "domain in the one-protein DS-3 system."
                    ),
                },
                table_s6_evidence(),
                table_s7_evidence(),
                table_s8_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-3, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_3_locus_reduces_phage_plaquing"],
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
            "Minted DS-3 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; kept the graph at cloned PIN8 "
            "transcriptional-unit level because the pinned DefenseFinder "
            "DS-3 HMM row is not backed by a rules row; "
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
            "Reviewed DS-3 system canonical_examples and left them empty "
            "because DeWeirdt et al. support cloned PIN8 plaquing assays in "
            "E. coli MG1655 plus a DefenseFinder DS-3 model, but not a "
            "direct named native microbial isolate exemplar with "
            "experimentally verified endogenous DS-3 activity. No paid "
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
