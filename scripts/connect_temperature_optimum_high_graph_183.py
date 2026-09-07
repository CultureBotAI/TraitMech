#!/usr/bin/env python3
"""Connect the temperature-optimum-high contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_optimum_high_graph_183.py
    python scripts/connect_temperature_optimum_high_graph_183.py --apply
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
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from connect_morphology_graphs_183 import _components, _edge_key  # noqa: E402
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "environment/temperature_optimum_high"
GRAPH_ID = "temperature_optimum_high_thermophile_setpoint"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T20:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-optimum-high thermophile setpoint",
    "description": (
        "DOI-backed graph linking thermophile membrane and protein "
        "thermostability adaptation to a temperature optimum above 40 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-optimum-high thermophile context",
    "description": (
        "DOI-backed nonmechanistic graph connecting thermophile "
        "thermostability, genome thermostability, heat-shock protein-quality "
        "control, membrane-lipid remodeling, and amino-acid composition "
        "branches to the above-40-degrees-C optimum bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "reverse_gyrase",
        "predicate": "positively regulates",
        "object": "dna_positive_supercoiling",
        "description": (
            "Reverse gyrase introduces positive supercoils into DNA, a "
            "thermophile hallmark."
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
    {
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
    {
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
    {
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
    {
        "subject": "thermosome",
        "predicate": "enables",
        "object": "denatured_protein_refolding",
        "description": "The thermosome enables ATP-dependent refolding of denatured proteins.",
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
    {
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
    {
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
                    "Verified against the open Gr\u00fcnberger et al. introduction; "
                    "the review context lists hydrophobic and charged amino-acid "
                    "enrichment among molecular mechanisms used by "
                    "hyperthermophilic archaea."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "dna_positive_supercoiling",
        "predicate": "associated with",
        "object": "genome_thermostability",
        "description": (
            "Reverse-gyrase-linked positive DNA supercoiling is associated "
            "with thermophile genome-thermostability context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1264/jsme2.me23087",
                "snippet": "protect genomes at high temperatures",
                "notes": (
                    "Verified against the open Takemata minireview; this "
                    "connector keeps positive DNA supercoiling as one genome "
                    "thermostability branch."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "genome_thermostability",
        "predicate": "associated with",
        "object": "thermophile_thermostability",
        "description": (
            "DNA and genome thermostability are associated with the broad "
            "thermophile-thermostability context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1264/jsme2.me23087",
                "snippet": "enhancing the thermostability of DNA in thermophiles",
                "notes": (
                    "Verified against the open Takemata minireview; this "
                    "connector keeps nucleoid-associated proteins as DNA "
                    "thermostability context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "protein_aggregation_heat",
        "predicate": "associated with",
        "object": "denatured_protein_refolding",
        "description": (
            "Heat-induced protein-aggregation prevention and denatured-protein "
            "refolding are associated heat-shock protein-quality-control "
            "branches."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03593-22",
                "snippet": "Small HSPs (sHSPs) and prefoldin bind to denaturing proteins",
                "notes": (
                    "Verified against the open Baes et al. introduction; this "
                    "connector joins complementary small-HSP protection and "
                    "thermosome refolding context for heat-damaged proteins."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "denatured_protein_refolding",
        "predicate": "associated with",
        "object": "thermophile_thermostability",
        "description": (
            "Thermosome-linked refolding of denatured proteins is associated "
            "with the broad thermophile-thermostability context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03593-22",
                "snippet": (
                    "thermosome complexes with different subunit compositions "
                    "and substrate specificities"
                ),
                "notes": (
                    "Verified against the open Baes et al. introduction; this "
                    "connector keeps thermosome refolding as protein-quality "
                    "context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_thermostability",
        "predicate": "associated with",
        "object": "thermophile_thermostability",
        "description": (
            "Cytoplasmic membrane thermostability is associated with the broad "
            "thermophile-thermostability context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03593-22",
                "snippet": (
                    "A sudden increase in temperature above the already high "
                    "optimal growth temperature could lead to detrimental "
                    "cellular damage"
                ),
                "notes": (
                    "Verified against the open Baes et al. introduction; this "
                    "connector keeps high-temperature membrane lipid remodeling "
                    "as a contextual thermophile branch."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
]


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


def _edges_by_key(edges: list[dict[str, Any]]) -> dict[
    tuple[str | None, str | None, str | None], dict[str, Any]
]:
    return {_edge_key(edge): edge for edge in edges}


def _assert_graph_metadata(graph: dict[str, Any], expected: dict[str, str], state: str) -> None:
    actual = {field: graph.get(field) for field in expected}
    if actual != expected:
        raise ValueError(f"{SLUG}: {state} graph metadata drifted: {actual!r}")


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


def _assert_endpoints(graph: dict[str, Any], edges: list[dict[str, Any]]) -> None:
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in edges:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{SLUG}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{SLUG}: connector lacks source/snippet evidence: {key}")


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    additions = _edges_by_key(ADDED_EDGES)
    source_connectors = _edges_by_key(SOURCE_CONNECTOR_EDGES)

    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    addition_keys = set(additions)
    present = existing_keys & addition_keys

    before = _components(graph)
    if before == 1 and present == addition_keys:
        _assert_graph_metadata(graph, GRAPH_METADATA_AFTER, "migrated")
        _assert_exact_edges(graph, additions, "migrated")
        return False

    _assert_graph_metadata(graph, GRAPH_METADATA_BEFORE, "source")
    if present:
        raise ValueError(f"{SLUG}: partial connector replay: {sorted(present)}")

    _assert_exact_edges(graph, source_connectors, "source")
    _assert_endpoints(graph, ADDED_EDGES)
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")

    graph.update(GRAPH_METADATA_AFTER)
    graph.setdefault("edges", []).extend(copy.deepcopy(ADDED_EDGES))

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{SLUG}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            "by adding 5 source- and verbatim-snippet-backed association "
            "connectors among genome thermostability, small-HSP/thermosome "
            "protein quality control, and membrane-thermostability branches. No "
            "paid research service was called."
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
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
