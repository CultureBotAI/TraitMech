#!/usr/bin/env python3
"""Review temperature-optimum-high graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_optimum_high_graph_183.py
    python scripts/review_temperature_optimum_high_graph_183.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "environment/temperature_optimum_high"
GRAPH_ID = "temperature_optimum_high_thermophile_setpoint"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T03:20:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "reverse_gyrase",
            "predicate": "positively regulates",
            "object": "dna_positive_supercoiling",
            "description": (
                "Reverse gyrase introduces positive supercoils into DNA, a thermophile hallmark."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "notes": (
                        "Reverse gyrase introduces positive supercoils into DNA "
                        "and is a hallmark of many thermophiles."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "reverse_gyrase",
            "predicate": "positively regulates",
            "object": "dna_positive_supercoiling",
            "description": (
                "Reverse gyrase introduces positive supercoils into DNA, a thermophile hallmark."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "snippet": "introduces positive supercoils into DNA",
                    "notes": (
                        "Verified against the open Takemata minireview; reverse "
                        "gyrase is described as the characteristic thermophile "
                        "topoisomerase that introduces positive supercoils into DNA."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "dna_positive_supercoiling",
            "predicate": "decreases",
            "object": "dna_melting_high_temperature",
            "description": (
                "Positive supercoiling limits DNA melting and prevents thermal denaturation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "notes": (
                        "Reverse gyrase / positive supercoiling proposed to limit "
                        "DNA melting and prevent thermal denaturation."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "dna_positive_supercoiling",
            "predicate": "decreases",
            "object": "dna_melting_high_temperature",
            "description": (
                "Positive supercoiling limits DNA melting and prevents thermal denaturation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "snippet": "prevents the thermal denaturation of DNA",
                    "notes": (
                        "Verified against the open Takemata minireview; the "
                        "review presents reverse-gyrase-dependent positive "
                        "supercoiling as the accepted route limiting DNA thermal "
                        "denaturation."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
    {
        "before": {
            "subject": "nucleoid_associated_proteins",
            "predicate": "increases",
            "object": "genome_thermostability",
            "description": "Nucleoid-associated proteins enhance DNA/genome thermostability.",
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "notes": (
                        "NAPs affect 3D genome organization and enhance DNA "
                        "thermostability; abundance correlates with growth temperature."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "nucleoid_associated_proteins",
            "predicate": "increases",
            "object": "genome_thermostability",
            "description": "Nucleoid-associated proteins enhance DNA/genome thermostability.",
            "evidence": [
                {
                    "reference": "DOI:10.1264/jsme2.me23087",
                    "snippet": "increase the melting temperature of DNA",
                    "notes": (
                        "Verified against the open Takemata minireview; in vitro "
                        "studies of NAPs from prokaryotes show increased DNA "
                        "melting temperature, and archaeal NAP abundance is "
                        "correlated with growth temperature."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "small_heat_shock_proteins",
            "predicate": "prevents",
            "object": "protein_aggregation_heat",
            "description": (
                "Small heat shock proteins bind denaturing proteins to prevent "
                "heat-induced aggregation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "notes": (
                        "Small HSPs bind denaturing proteins and protect them from "
                        "aggregation under heat stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "small_heat_shock_proteins",
            "predicate": "prevents",
            "object": "protein_aggregation_heat",
            "description": (
                "Small heat shock proteins bind denaturing proteins to prevent "
                "heat-induced aggregation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "snippet": "protecting them from aggregation",
                    "notes": (
                        "Verified against the open Baes et al. introduction; "
                        "small archaeal heat-shock proteins are described as "
                        "binding denaturing proteins to protect them from aggregation."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
    {
        "before": {
            "subject": "thermosome",
            "predicate": "refolds",
            "object": "denatured_protein_refolding",
            "description": ("Thermosome refolds denatured proteins in an ATP-dependent manner."),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "notes": ("Thermosome refolds denatured proteins in an ATP-dependent manner."),
                }
            ],
        },
        "after": {
            "subject": "thermosome",
            "predicate": "enables",
            "object": "denatured_protein_refolding",
            "description": (
                "The thermosome enables ATP-dependent refolding of denatured proteins."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "snippet": "refolds denatured proteins in an ATP-dependent manner",
                    "notes": (
                        "Verified against the open Baes et al. introduction; the "
                        "archaeal thermosome is described as the group-II "
                        "chaperonin complex that performs ATP-dependent refolding "
                        "of denatured proteins."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "membrane_lipid_composition",
            "predicate": "stabilizes",
            "object": "membrane_thermostability",
            "description": (
                "Altered membrane lipid composition stabilizes the cytoplasmic "
                "membrane at high temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "notes": (
                        "Heat shock leads to an altered lipid composition of the "
                        "cytoplasmic membrane; unique membrane composition is a "
                        "recognized thermophile adaptation."
                    ),
                }
            ],
        },
        "after": {
            "subject": "membrane_lipid_composition",
            "predicate": "contributes to",
            "object": "membrane_thermostability",
            "description": (
                "Altered membrane lipid composition contributes to cytoplasmic "
                "membrane thermostability at high temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03593-22",
                    "snippet": "altered lipid composition of the cytoplasmic membrane",
                    "notes": (
                        "Verified against the open Baes et al. introduction; "
                        "Sulfolobales heat shock is described as altering "
                        "cytoplasmic-membrane lipid composition, matching this "
                        "as a membrane-stabilization response branch rather than "
                        "a single determinant of thermophily."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "aa_composition_thermostability",
            "predicate": "increases",
            "object": "thermophile_thermostability",
            "description": (
                "Enrichment in hydrophobic and charged amino acids increases "
                "protein thermostability."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.02174-23",
                    "notes": (
                        "Thermophiles show enrichment in hydrophobic and charged "
                        "amino acids contributing to intrinsic protein thermostability."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "aa_composition_thermostability",
            "predicate": "increases",
            "object": "thermophile_thermostability",
            "description": (
                "Enrichment in hydrophobic and charged amino acids increases "
                "protein thermostability."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.02174-23",
                    "snippet": "enrichment in hydrophobic and charged amino acids",
                    "notes": (
                        "Verified against the open Grünberger et al. introduction; "
                        "the review context lists hydrophobic and charged amino-acid "
                        "enrichment among molecular mechanisms used by "
                        "hyperthermophilic archaea."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{SLUG}: expected exactly one graph, found {len(graphs)}")
    graph = graphs[0]
    if graph.get("graph_id") != GRAPH_ID:
        raise ValueError(f"{SLUG}: expected graph_id {GRAPH_ID!r}")
    if graph.get("scope_status") != "NONMECHANISTIC":
        raise ValueError(f"{SLUG}: expected a NONMECHANISTIC graph")
    return graph


def _replacements_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_edges(
    graph: dict[str, Any],
    expected_by_key: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
    state: str,
) -> None:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    missing = set(expected_by_key) - set(existing_by_key)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} edge(s): {sorted(missing)}")
    for key, expected in expected_by_key.items():
        if existing_by_key[key] != expected:
            raise ValueError(f"{SLUG}: {state} edge drifted: {key}")


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_edges = _replacements_by_state("before")
    after_edges = _replacements_by_state("after")
    migrated_keys = set(after_edges) - set(before_edges)
    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_keys = existing_keys & migrated_keys

    if _has_exact_edges(graph, after_edges):
        return False

    if present_migrated_keys == migrated_keys:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_keys:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_keys)}")

    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["edges"] = [
        copy.deepcopy(after_by_before_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the temperature_optimum_high_thermophile_setpoint graph "
            "for issue #183: added snippets to 7 edge-level evidence items "
            "and grounded the thermosome and membrane-lipid predicates to "
            "RO:0002327 or RO:0002326. No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    path = REPO_ROOT / "data" / "traits" / f"{SLUG}.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if transform(SLUG, doc):
        changed = 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
