#!/usr/bin/env python3
"""Connect the gc_low contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_gc_low_graph_183.py
    python scripts/connect_gc_low_graph_183.py --apply
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

SLUG = "genomics/gc_low"
GRAPH_ID = "gc_low_mid_low_gc_bin"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T23:40:00Z"
EXPECTED_COMPONENTS = 2

GRAPH_METADATA_BEFORE = {
    "title": "GC-low (METPO 42.65\u201357.0%) mid-low GC bin",
    "description": (
        "DOI-backed graph linking moderate mutation bias to a GC content of "
        "~42.65\u201357.0% (the threshold encoded by the METPO synonym "
        "GC_42.65_57.0 on this record)."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "GC-low METPO 42.65-57.0% genome-composition context",
    "description": (
        "DOI-backed nonmechanistic graph connecting DNA-repair defects, "
        "mutational spectra, cytosine-deamination context, AT-enriching "
        "spectrum context, replication/repair enzyme bias, and moderate "
        "mutation bias to continuous genome-wide GC content and the METPO "
        "GC_42.65_57.0 bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "dna_repair_defect",
        "predicate": "causes",
        "object": "mutational_spectrum",
        "description": (
            "Defects in DNA repair genes (MMR, BER, HR) create distinctive "
            "bacterial mutational signatures."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-023-42916-w",
                "snippet": "defects in DNA repair create distinctive mutational signatures",
                "notes": (
                    "Verified against the open Ruis et al. abstract and "
                    "results; hypermutator lineages with mutations in MMR, "
                    "BER, or HR DNA-repair genes were used to extract "
                    "pathway-specific bacterial signatures."
                ),
            }
        ],
        "predicate_id": "biolink:causes",
    },
    {
        "subject": "cytosine_deamination",
        "predicate": "contributes to",
        "object": "at_enriching_spectrum",
        "description": (
            "Cytosine deamination and the resulting C>T transitions contribute "
            "to an AT-enriching bacterial mutation spectrum."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-023-42916-w",
                "snippet": (
                    "cytosine to thymine (C\u2009>\u2009T) was typically the most "
                    "common mutation type identified"
                ),
                "notes": (
                    "Verified against the open Ruis et al. results; C>T was "
                    "the most common mutation type in 69 of 84 bacterial "
                    "single-base-substitution spectra and is discussed as "
                    "potentially arising from cytosine deamination."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "at_enriching_spectrum",
        "predicate": "associated with",
        "object": "gc_content",
        "description": (
            "AT-enriching C>A/T and depleted C>G mutation spectra are "
            "associated with continuous genome-wide G+C content."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-023-42916-w",
                "snippet": (
                    "Genomic G\u2009+\u2009C content exhibited a negative correlation "
                    "with proportion of C\u2009>\u2009A/T mutations"
                ),
                "notes": (
                    "Verified against the open Ruis et al. results; the "
                    "spectrum-to-composition association is left on the "
                    "continuous GC-content node rather than asserted as "
                    "specific causation of this METPO numeric bin."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "at_enriching_spectrum",
        "predicate": "is a",
        "object": "mutational_spectrum",
        "description": (
            "The AT-enriching C>A/T spectrum is a mutational-spectrum context "
            "connecting cytosine-deamination bias to bacterial DNA-repair "
            "mutational signatures."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-023-42916-w",
                "snippet": (
                    "context-dependent patterns of base substitutions termed "
                    "mutational signatures, which combine to form a "
                    "mutational spectrum"
                ),
                "notes": (
                    "Verified against the open Ruis et al. results; this "
                    "connector identifies the AT-enriching C>A/T pattern as a "
                    "specific bacterial mutational-spectrum context rather "
                    "than a direct cause of the METPO GC_42.65_57.0 bin."
                ),
            }
        ],
        "predicate_id": "rdfs:subClassOf",
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
    has_after_metadata = {
        field: graph.get(field) for field in GRAPH_METADATA_AFTER
    } == GRAPH_METADATA_AFTER
    if before == 1 and present == addition_keys and has_after_metadata:
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
            "by adding 1 source- and exact-snippet-backed is-a connector "
            "from the AT-enriching mutation spectrum to the broader "
            "mutational-spectrum node. No paid research service was called."
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
