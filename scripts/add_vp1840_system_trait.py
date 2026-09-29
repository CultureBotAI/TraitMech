#!/usr/bin/env python3
"""Add the VP1840 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "vp1840_system.yaml"

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
TIMESTAMP = "2026-09-29T02:26:23Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T02:26:24Z"
EVIDENCE_CLARIFICATION_TIMESTAMP = "2026-09-29T02:51:42Z"
PSIBLAST_QUERY_CLARIFICATION_TIMESTAMP = "2026-09-29T03:13:39Z"
PHAGE_PLATING_SCOPE_TIMESTAMP = "2026-09-29T03:27:44Z"

IDENTIFIER = "traitmech:000450"
PROPOSAL = "proposals/metpo_traitmech_v327"

DISCOVERY_SNIPPET = (
    "Intrigued by this discovery, we cloned 57 integron gene cassettes "
    "and identified 9 previously unrecognized systems that mediate defence."
)
VP1840_CLONE_SNIPPET = (
    "VP_RS08920\tVp1840\tY\tWP_005483293.1 \tHypothetical Protein"
)
VP1840_BAS21_SNIPPET = "Strain\tPhage\tFold Change\tNotes\nVP1840\tBas21\t2e-09"
VP1840_LL1_SNIPPET = "Strain\tPhage\tFold Change\tNotes\nVP1840\tLL1\t0"
VP1840_CONSTRUCT_SNIPPET = (
    "VSV105-vp1840\tVSV105 carrying gene vp1840 behind the lac promoter, "
    "cloned into KpnI by In-Fusion\tThis Study"
)
VP1840_PSIBLAST_QUERY_SNIPPET = (
    ">BAC60103.1 hypothetical protein "
    "[Vibrio parahaemolyticus RIMD 2210633]"
)
VP1840_PSIBLAST_SNIPPET = (
    "Scientific Name\tQuery Cover\tE value\tPer. ident\tAccession  \n"
    "Vibrio parahaemolyticus\t1\t3e-121\t100\tWP_229652597.1"
)
ARTICLE_ROW = (
    "| VP1840 | 10\\.1038/s41564-025-01927-7 | Integrons are "
    "anti-phage defence libraries in Vibrio parahaemolyticus | "
)
HMM_ROW = (
    "| VP1840__VP1840                                   |"
    "                                                  | VP1840"
    "                 | Custom                  | 75     |"
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


def cloned_vp1840_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1840_CLONE_SNIPPET,
        "notes": (
            "Supplementary Table 8 lists VP_RS08920/Vp1840 as a cloned "
            "RIMD 2210633 integron cassette with protein accession "
            "WP_005483293.1."
        ),
    }


def bas21_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1840_BAS21_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1840/Bas21 "
            "phage-plating readout as a Fold Change value of 2e-09."
        ),
    }


def ll1_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1840_LL1_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1840/LL1 "
            "phage-plating readout as a Fold Change value of 0."
        ),
    }


def construct_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1840_CONSTRUCT_SNIPPET,
        "notes": (
            "Supplementary Table 12 records the VSV105-vp1840 lac-expression "
            "plasmid used to express vp1840 behind the lac promoter."
        ),
    }


def psiblast_query_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1840_PSIBLAST_QUERY_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1840 worksheet labels BAC60103.1 "
            "from Vibrio parahaemolyticus RIMD 2210633 as the PSI-BLAST "
            "query protein."
        ),
    }


def psiblast_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1840_PSIBLAST_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1840 worksheet records a full-length "
            "100% PSI-BLAST hit from the BAC60103.1 query to the separate "
            "Vibrio parahaemolyticus homolog WP_229652597.1."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the VP1840 "
            "model namespace to the Getz et al. Vibrio parahaemolyticus "
            "integron-defense paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records VP1840__VP1840 "
            "as a custom VP1840 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "VP1840 system",
    "definition": (
        "A phage defense system in which an organism possesses a VP1840-family "
        "locus represented by the DefenseFinder VP1840__VP1840 custom HMM "
        "profile and experimentally linked to reduced bacteriophage plaquing "
        "when the cloned Vibrio parahaemolyticus RIMD 2210633 vp1840 cassette "
        "is expressed from a VSV105 plasmid."
    ),
    "definition_source": GETZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "VP1840",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Vp1840",
            "synonym_type": "RELATED_SYNONYM",
            "source": SUPPLEMENTARY_TABLES,
        },
        {
            "synonym_text": "VP1840__VP1840",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        discovery_evidence(),
        cloned_vp1840_evidence(),
        construct_evidence(),
        bas21_plating_evidence(),
        ll1_plating_evidence(),
        psiblast_query_evidence(),
        psiblast_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "vp1840_locus_reduces_bacteriophage_plaquing",
            "title": "VP1840 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking VP1840-family "
                "locus possession to reduced bacteriophage plaquing without "
                "resolving VP1840 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures VP1840 as a RIMD 2210633 integron "
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
                    "node_id": "vp1840_locus",
                    "label": "VP1840 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Vp1840-like integron cassette locus represented "
                        "in the pinned DefenseFinder HMM inventory by the "
                        "VP1840__VP1840 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_bacteriophage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced plaquing of bacteriophages "
                        "in cells expressing cloned vp1840."
                    ),
                },
                {
                    "node_id": "vp1840_system_trait",
                    "label": "VP1840 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded VP1840 "
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
                    "subject": "vp1840_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_bacteriophage_plaquing",
                    "description": (
                        "The cloned V. parahaemolyticus vp1840 integron "
                        "cassette contributes to reduced bacteriophage "
                        "plaquing in VSV105 plasmid-expression assays, and "
                        "DefenseFinder represents the VP1840 family with one "
                        "custom HMM profile."
                    ),
                    "evidence": [
                        cloned_vp1840_evidence(),
                        construct_evidence(),
                        bas21_plating_evidence(),
                        ll1_plating_evidence(),
                        psiblast_query_evidence(),
                        psiblast_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_bacteriophage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "vp1840_system_trait",
                    "description": (
                        "VP1840-mediated bacteriophage plaquing reduction "
                        "realizes the VP1840 system trait."
                    ),
                    "evidence": [
                        bas21_plating_evidence(),
                        ll1_plating_evidence(),
                    ],
                },
                {
                    "subject": "vp1840_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "VP1840 system possession is a phage-defense-system "
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
            "discussion_id": "vp1840-defensefinder-model-gap",
            "prompt": (
                "Resolve VP1840 native host breadth, exact "
                "single-component activity, profile-to-protein mapping, "
                "homolog boundary, full phage breadth, molecular "
                "output, and rule-level DefenseFinder criteria before "
                "minting narrower VP1840 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Getz et al. support VP1840 as one of nine RIMD 2210633 "
                "integron-encoded cassettes whose cloned expression reduced "
                "phage plaquing, Supplementary Tables 8, 9, and 12 map "
                "VP1840 to VP_RS08920/Vp1840, WP_005483293.1, "
                "VSV105-vp1840, and phage-plating fold changes, and "
                "Supplementary Data 1 reports PSI-BLAST homologs. The "
                "pinned DefenseFinder HMM inventory records one VP1840 "
                "custom profile row. The pinned rules table has no VP1840 "
                "row, and the first-pass record does not resolve native "
                "host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, molecular output, or "
                "endogenous activity."
            ),
            "evidence": [
                discovery_evidence(),
                cloned_vp1840_evidence(),
                construct_evidence(),
                bas21_plating_evidence(),
                psiblast_query_evidence(),
                psiblast_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list VP1840, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#vp1840_locus_reduces_bacteriophage_plaquing"
            ],
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
            "Minted VP1840 system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at cloned "
            "integron-cassette level because the molecular output and rule "
            f"rows remain unresolved, and {PROPOSAL} reserves the "
            "replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed VP1840 system canonical_examples and left them empty "
            "because Getz et al. directly support cloned Vp1840 "
            "VSV105-plasmid assays, PSI-BLAST homologs, and a "
            "DefenseFinder VP1840 model, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous VP1840 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CLARIFIED_EVIDENCE_SNIPPETS",
        changes=(
            "Clarified Supplementary Table 9 VP1840 phage-plating notes to "
            "name the paper's Fold Change column and expanded the "
            "Supplementary Data 1 VP1840 PSI-BLAST snippet with its column "
            "header so the WP_229652597.1 hit is self-identifying."
        ),
        llm_assisted=True,
        timestamp=EVIDENCE_CLARIFICATION_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="GROUNDED_PSIBLAST_QUERY_ACCESSION",
        changes=(
            "Quoted the Supplementary Data 1 VP1840 worksheet query row so "
            "the BAC60103.1 PSI-BLAST query named in the WP_229652597.1 "
            "homolog-hit note is directly evidenced."
        ),
        llm_assisted=True,
        timestamp=PSIBLAST_QUERY_CLARIFICATION_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CLARIFIED_PHAGE_PLATING_SCOPE",
        changes=(
            "Quoted the Supplementary Table 9 Fold Change header in the "
            "Bas21 and LL1 snippets and neutralized unsupported VP1840 "
            "host-clade phrasing to bacteriophage wording."
        ),
        llm_assisted=True,
        timestamp=PHAGE_PLATING_SCOPE_TIMESTAMP,
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
