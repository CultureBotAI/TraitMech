#!/usr/bin/env python3
"""Add the VP1817 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "vp1817_system.yaml"

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
TIMESTAMP = "2026-09-30T08:41:53Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T08:41:54Z"

IDENTIFIER = "traitmech:000487"
PROPOSAL = "proposals/metpo_traitmech_v364"

DISCOVERY_SNIPPET = (
    "Intrigued by this discovery, we cloned 57 integron gene cassettes "
    "and identified 9 previously unrecognized systems that mediate defence."
)
VP1817_CLONE_SNIPPET = (
    "VP_RS08765\tVP1817\tY\tWP_024699215.1\tHypothetical Protein"
)
VP1817_CONSTRUCT_SNIPPET = (
    "VSV105-vp1817\tVSV105 carrying gene vp1817 behind the lac promoter, "
    "cloned into KpnI by In-Fusion\tThis Study"
)
VP1817_BAS27_SNIPPET = "VP1817\tBas27\t0.01"
VP1817_BAS37_SNIPPET = "VP1817\tBas37\t0.03125"
VP1817_PSIBLAST_QUERY_SNIPPET = (
    ">BAC60080.1 hypothetical protein [Vibrio parahaemolyticus RIMD 2210633]"
)
VP1817_PSIBLAST_SNIPPET = (
    "Scientific Name\tQuery Cover\tE value\tPer. ident\tAccession  \n"
    "Vibrio parahaemolyticus\t1\t8e-56\t100\tARC19819.1"
)
ARTICLE_ROW = (
    "| VP1817 | 10\\.1038/s41564-025-01927-7 | Integrons are "
    "anti-phage defence libraries in Vibrio parahaemolyticus | "
)
HMM_ROW = (
    "| VP1817__VP1817                                   |"
    "                                                  | VP1817"
    "                 | Custom                  | 30     |"
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


def cloned_vp1817_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1817_CLONE_SNIPPET,
        "notes": (
            "Supplementary Table 8 lists VP_RS08765/VP1817 as a cloned "
            "RIMD 2210633 integron cassette with protein accession "
            "WP_024699215.1."
        ),
    }


def construct_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1817_CONSTRUCT_SNIPPET,
        "notes": (
            "Supplementary Table 12 records the VSV105-vp1817 "
            "lac-expression plasmid used to express vp1817 behind the "
            "lac promoter."
        ),
    }


def bas27_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1817_BAS27_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1817/Bas27 "
            "phage-plating readout as a Fold Change value of 0.01."
        ),
    }


def bas37_plating_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_TABLES,
        "snippet": VP1817_BAS37_SNIPPET,
        "notes": (
            "Supplementary Table 9 identifies the VP1817/Bas37 "
            "phage-plating readout as a Fold Change value of 0.03125."
        ),
    }


def psiblast_query_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1817_PSIBLAST_QUERY_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1817 worksheet labels BAC60080.1 "
            "from Vibrio parahaemolyticus RIMD 2210633 as the "
            "PSI-BLAST query protein."
        ),
    }


def psiblast_evidence() -> dict[str, str]:
    return {
        "reference": SUPPLEMENTARY_DATA,
        "snippet": VP1817_PSIBLAST_SNIPPET,
        "notes": (
            "Supplementary Data 1's VP1817 worksheet records a full-length "
            "100% PSI-BLAST hit from the BAC60080.1 query to the separate "
            "Vibrio parahaemolyticus homolog ARC19819.1."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the VP1817 "
            "model namespace to the Getz et al. Vibrio parahaemolyticus "
            "integron-defense paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records VP1817__VP1817 "
            "as a custom VP1817 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "VP1817 system",
    "definition": (
        "A phage defense system in which an organism possesses a VP1817-family "
        "locus represented by the DefenseFinder VP1817__VP1817 custom HMM "
        "profile and experimentally linked to reduced bacteriophage plaquing "
        "when the cloned Vibrio parahaemolyticus RIMD 2210633 vp1817 cassette "
        "is expressed from a VSV105 plasmid."
    ),
    "definition_source": GETZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "VP1817",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "VP1817__VP1817",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        discovery_evidence(),
        cloned_vp1817_evidence(),
        construct_evidence(),
        bas27_plating_evidence(),
        bas37_plating_evidence(),
        psiblast_query_evidence(),
        psiblast_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "vp1817_locus_reduces_bacteriophage_plaquing",
            "title": "VP1817 loci reduce bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking VP1817-family "
                "locus possession to reduced bacteriophage plaquing without "
                "resolving VP1817 component function or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures VP1817 as a RIMD 2210633 integron "
                "cassette with cloned phage-plating readouts, a PSI-BLAST "
                "homolog lead, one pinned DefenseFinder custom HMM-profile "
                "row, and no pinned DefenseFinder rule row. It does not "
                "assert native host breadth, exact profile-to-protein "
                "correspondence, molecular activity, phage trigger, "
                "substrate, complete homolog boundary, endogenous activity, "
                "or rule-level DefenseFinder detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "vp1817_locus",
                    "label": "VP1817 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A VP1817-like integron cassette locus represented "
                        "in the pinned DefenseFinder HMM inventory by the "
                        "VP1817__VP1817 custom profile."
                    ),
                },
                {
                    "node_id": "reduced_bacteriophage_plaquing",
                    "label": "reduced bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced plaquing of bacteriophages in cells "
                        "expressing cloned vp1817."
                    ),
                },
                {
                    "node_id": "vp1817_system_trait",
                    "label": "VP1817 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded VP1817 "
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
                    "subject": "vp1817_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_bacteriophage_plaquing",
                    "description": (
                        "The cloned V. parahaemolyticus vp1817 integron "
                        "cassette contributes to reduced bacteriophage "
                        "plaquing in VSV105 plasmid-expression assays, and "
                        "DefenseFinder represents the VP1817 family with "
                        "one custom HMM profile."
                    ),
                    "evidence": [
                        cloned_vp1817_evidence(),
                        construct_evidence(),
                        bas27_plating_evidence(),
                        bas37_plating_evidence(),
                        psiblast_query_evidence(),
                        psiblast_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "reduced_bacteriophage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "vp1817_system_trait",
                    "description": (
                        "VP1817-mediated bacteriophage plaquing reduction "
                        "realizes the VP1817 system trait."
                    ),
                    "evidence": [
                        bas27_plating_evidence(),
                        bas37_plating_evidence(),
                    ],
                },
                {
                    "subject": "vp1817_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "VP1817 system possession is a phage-defense-system "
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
            "discussion_id": "vp1817-defensefinder-model-gap",
            "prompt": (
                "Resolve VP1817 native host breadth, exact "
                "single-component activity, profile-to-protein mapping, "
                "homolog boundary, full phage breadth, molecular output, "
                "and rule-level DefenseFinder criteria before minting "
                "narrower VP1817 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Getz et al. support VP1817 as one of nine RIMD 2210633 "
                "integron-encoded cassettes whose cloned expression reduced "
                "phage plaquing, Supplementary Tables 8, 9, and 12 map "
                "VP1817 to VP_RS08765/VP1817, WP_024699215.1, "
                "VSV105-vp1817, and phage-plating fold changes, and "
                "Supplementary Data 1 reports PSI-BLAST homologs. The "
                "pinned DefenseFinder HMM inventory records one VP1817 "
                "custom profile row. The pinned rules table has no VP1817 "
                "row, and the first-pass record does not resolve native "
                "host breadth, complete phage breadth, direct "
                "profile-to-protein correspondence, molecular output, or "
                "endogenous activity."
            ),
            "evidence": [
                discovery_evidence(),
                cloned_vp1817_evidence(),
                construct_evidence(),
                bas27_plating_evidence(),
                bas37_plating_evidence(),
                psiblast_query_evidence(),
                psiblast_evidence(),
                article_registry_evidence(),
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list VP1817, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#vp1817_locus_reduces_bacteriophage_plaquing"
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
            "Minted VP1817 system as a DOI-backed GENOMICS TraitRecord "
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
            "Reviewed VP1817 system canonical_examples and left them empty "
            "because Getz et al. directly support cloned VP1817 "
            "VSV105-plasmid assays, PSI-BLAST homologs, and a "
            "DefenseFinder VP1817 model, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous VP1817 activity. No paid research was used."
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
