#!/usr/bin/env python3
"""Add the VP1823 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "vp1823_system.yaml"

GETZ = "DOI:10.1038/s41564-025-01927-7"

SPRINGER_PREFIX = (
    "https://media.springernature.com/original/springer-static/esm/"
    "art%3A10.1038%2Fs41564-025-01927-7/MediaObjects/"
)
SUPPLEMENTARY_TABLES = f"{SPRINGER_PREFIX}41564_2025_1927_MOESM2_ESM.xlsx"
SUPPLEMENTARY_DATA = f"{SPRINGER_PREFIX}41564_2025_1927_MOESM3_ESM.xlsx"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T06:58:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T06:58:01Z"

IDENTIFIER = "traitmech:000485"
PROPOSAL = "proposals/metpo_traitmech_v362"

DISCOVERY_SNIPPET = (
    "Intrigued by this discovery, we cloned 57 integron gene cassettes "
    "and identified 9 previously unrecognized systems that mediate defence."
)
VP1823_CLONE_SNIPPET = (
    "VP_RS08795\tVP1823\tY\tWP_079749463.1 \tHypothetical Protein"
)
VP1823_CONSTRUCT_SNIPPET = (
    "VSV105-vp1823\tVSV105 carrying gene vp1823 behind the lac promoter, "
    "cloned into KpnI by In-Fusion\tThis Study"
)
VP1823_BAS30_SNIPPET = "VP1823\tBas30\t0.0003"
VP1823_T4_SNIPPET = "VP1823\tT4\t1e-05"
VP1823_PSIBLAST_QUERY_SNIPPET = (
    ">BAC60086.1 hypothetical protein "
    "[Vibrio parahaemolyticus RIMD 2210633]"
)
VP1823_PSIBLAST_SNIPPET = (
    "Scientific Name\tQuery Cover\tE value\tPer. ident\tAccession  \n"
    "Vibrio parahaemolyticus\t1\t2e-166\t100\tWP_237666972.1"
)
ARTICLE_ROW = (
    "| VP1823 | 10\\.1038/s41564-025-01927-7 | Integrons are "
    "anti-phage defence libraries in Vibrio parahaemolyticus | "
)
HMM_ROW = (
    "| VP1823__VP1823                                   |"
    "                                                  | VP1823"
    "                 | Custom                  | 200    |"
)


def discovery_evidence() -> dict[str, str]:
    return {
        "reference": GETZ,
        "snippet": DISCOVERY_SNIPPET,
        "notes": (
            "Getz et al. identify nine previously unrecognized "
            "Vibrio parahaemolyticus integron cassettes as anti-phage "
            "defense systems."
        ),
    }


def cloned_vp1823_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1823_CLONE_SNIPPET,
        "notes": (
            "Supplementary Table 8 lists VP_RS08795/VP1823 as a cloned "
            "RIMD 2210633 integron cassette with protein accession "
            "WP_079749463.1."
        ),
    }


def construct_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1823_CONSTRUCT_SNIPPET,
        "notes": (
            "Supplementary Table 12 records the VSV105-vp1823 lac-expression "
            "plasmid used to express vp1823 behind the lac promoter."
        ),
    }


def bas30_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1823_BAS30_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1823/Bas30 "
            "phage-plating readout as a Fold Change value of 0.0003."
        ),
    }


def t4_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1823_T4_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1823/T4 phage-plating "
            "readout as a Fold Change value of 1e-05."
        ),
    }


def psiblast_query_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1823_PSIBLAST_QUERY_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1823 worksheet labels BAC60086.1 "
            "from Vibrio parahaemolyticus RIMD 2210633 as the PSI-BLAST "
            "query protein."
        ),
    }


def psiblast_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1823_PSIBLAST_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1823 worksheet records a full-length "
            "100% PSI-BLAST hit from the BAC60086.1 query to the separate "
            "Vibrio parahaemolyticus homolog WP_237666972.1."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the VP1823 "
            "model namespace to the Getz et al. Vibrio parahaemolyticus "
            "integron-defense paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records VP1823__VP1823 "
            "as a custom VP1823 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "VP1823 system",
    "definition": (
        "A phage defense system in which an organism possesses a VP1823-family "
        "locus represented by the DefenseFinder VP1823__VP1823 custom HMM "
        "profile and experimentally linked to reduced bacteriophage plaquing "
        "when the cloned Vibrio parahaemolyticus RIMD 2210633 vp1823 cassette "
        "is expressed from a VSV105 plasmid."
    ),
    "definition_source": GETZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "VP1823",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "VP1823__VP1823",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        discovery_evidence(),
        cloned_vp1823_evidence(),
        construct_evidence(),
        bas30_plating_evidence(),
        t4_plating_evidence(),
        psiblast_query_evidence(),
        psiblast_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "vp1823_locus_reduces_bacteriophage_plaquing",
            "title": "VP1823 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking VP1823-family "
                "locus possession to reduced bacteriophage plaquing without "
                "resolving VP1823 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures VP1823 as a RIMD 2210633 integron "
                "cassette with cloned phage-plating readouts, a PSI-BLAST "
                "homolog lead, one pinned DefenseFinder custom HMM-profile "
                "row, and no pinned DefenseFinder rule row. It does not "
                "assert native host breadth, exact profile-to-protein "
                "correspondence, molecular activity, phage trigger, "
                "substrate, complete homolog boundary, endogenous "
                "activity, or rule-level DefenseFinder detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "vp1823_locus",
                    "label": "VP1823 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A VP1823-like integron cassette locus represented "
                        "in the pinned DefenseFinder HMM inventory by the "
                        "VP1823__VP1823 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_bacteriophage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced plaquing of bacteriophages in cells "
                        "expressing cloned vp1823."
                    ),
                },
                {
                    "node_id": "vp1823_system_trait",
                    "label": "VP1823 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded VP1823 "
                        "phage-defense system."
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
                    "subject": "vp1823_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_bacteriophage_plaquing",
                    "description": (
                        "The cloned V. parahaemolyticus vp1823 integron "
                        "cassette contributes to reduced bacteriophage "
                        "plaquing in VSV105 plasmid-expression assays, and "
                        "DefenseFinder represents the VP1823 family with one "
                        "custom HMM profile."
                    ),
                    "evidence": [
                        cloned_vp1823_evidence(),
                        construct_evidence(),
                        bas30_plating_evidence(),
                        t4_plating_evidence(),
                        psiblast_query_evidence(),
                        psiblast_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_bacteriophage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "vp1823_system_trait",
                    "description": (
                        "VP1823-mediated bacteriophage plaquing reduction "
                        "realizes the VP1823 system trait."
                    ),
                    "evidence": [
                        bas30_plating_evidence(),
                        t4_plating_evidence(),
                    ],
                },
                {
                    "subject": "vp1823_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "VP1823 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        discovery_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "vp1823-defensefinder-model-gap",
            "prompt": (
                "Resolve VP1823 native host breadth, exact "
                "single-component activity, profile-to-protein mapping, "
                "homolog boundary, full phage breadth, molecular output, "
                "and rule-level DefenseFinder criteria before minting "
                "narrower VP1823 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Getz et al. support VP1823 as one of nine RIMD 2210633 "
                "integron-encoded cassettes whose cloned expression reduced "
                "phage plaquing, Supplementary Tables 8, 9, and 12 map "
                "VP1823 to VP_RS08795/VP1823, WP_079749463.1, "
                "VSV105-vp1823, and phage-plating fold changes, and "
                "Supplementary Data 1 reports PSI-BLAST homologs. The "
                "pinned DefenseFinder HMM inventory records one VP1823 "
                "custom profile row. The pinned rules table has no VP1823 "
                "row, and the first-pass record does not resolve native "
                "host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, molecular output, or "
                "endogenous activity."
            ),
            "evidence": [
                discovery_evidence(),
                cloned_vp1823_evidence(),
                construct_evidence(),
                bas30_plating_evidence(),
                psiblast_query_evidence(),
                psiblast_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list VP1823, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#vp1823_locus_reduces_bacteriophage_plaquing"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
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
            "Minted VP1823 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact same-scope live TraitMech, "
            "METPO, history, or prior proposal record; kept the graph at "
            "cloned integron-cassette level because molecular output, "
            f"native activity, and rule rows remain unresolved; {PROPOSAL} "
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
            "Reviewed VP1823 system canonical_examples and left them empty "
            "because Getz et al. directly support cloned VP1823 "
            "VSV105-plasmid assays, PSI-BLAST homologs, and a "
            "DefenseFinder VP1823 model, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous VP1823 activity. No paid research was used."
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
