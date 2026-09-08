#!/usr/bin/env python3
"""Connect the mesophilic contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_mesophilic_graph_183.py
    python scripts/connect_mesophilic_graph_183.py --apply
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

SLUG = "environment/mesophilic"
GRAPH_ID = "mesophilic_homoviscous_adaptation"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T13:00:00Z"
EXPECTED_COMPONENTS = 5

GRAPH_METADATA_BEFORE = {
    "title": "Mesophilic homoviscous and enzymatic adaptation mechanism",
    "description": (
        "DOI-backed graph linking mesophily to moderate ambient temperature, "
        "homoviscous membrane lipid composition, mesophile enzyme repertoire, "
        "and balanced growth at intermediate temperatures."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Mesophilic growth with membrane and temperature-boundary support",
    "description": (
        "DOI-backed nonmechanistic graph connecting mesophily to moderate "
        "temperature, balanced growth, homoviscous membrane fluidity, and "
        "cold- and heat-shock boundary-support branches."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "homoviscous_lipid_composition",
        "predicate": "regulates",
        "object": "membrane_fluidity",
        "description": (
            "Homoviscous lipid composition maintains target membrane fluidity "
            "at mesophilic temperatures."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "more unsaturated fatty acids",
                "notes": (
                    "Supports homoviscous adaptation as the mechanism setting "
                    "membrane fluidity."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "balanced_growth",
        "predicate": "manifests as",
        "object": "mesophilic_trait",
        "description": (
            "Balanced growth at moderate temperatures manifests the mesophilic "
            "trait."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1016/j.bpj.2013.06.029",
                "snippet": "Escherichia coli, a mesophilic bacterium",
                "notes": "Supports the trait endpoint in a representative organism.",
            }
        ],
        "predicate_id": "METPO:2007400",
    },
    {
        "subject": "temperature_decrease",
        "predicate": "increases",
        "object": "unsaturated_fatty_acids",
        "description": (
            "Temperature downshift increases membrane unsaturated fatty acid "
            "content through homeoviscous adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "production of double bonds in lipids",
                "notes": (
                    "Verified against the Ramón et al. cold-adaptation review; "
                    "low-temperature adaptation includes membrane-composition "
                    "remodeling through lipid double-bond production."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "cspa",
        "predicate": "promotes",
        "object": "translation",
        "description": (
            "CspA RNA chaperone activity destabilizes inhibitory mRNA secondary "
            "structures, promoting translation during cold shock."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                "snippet": "facilitates translation by destabilizing mRNA secondary structures",
                "notes": (
                    "Verified against the open Molecular Microbiology full "
                    "text; CspA acts as an RNA chaperone that counters "
                    "low-temperature mRNA secondary structure."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "rpoh_sigma32",
        "predicate": "positively regulates",
        "object": "heat_shock_proteins",
        "description": (
            "Sigma-32 (RpoH) positively regulates heat-shock response protein "
            "expression."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.183.18.5302-5310.2001",
                "snippet": "enhancing transcription of the heat shock genes",
                "notes": (
                    "Verified against the open Journal of Bacteriology full "
                    "text; RpoH-dependent sigma-32 activity drives "
                    "heat-shock-gene transcription."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "unsaturated_fatty_acids",
        "predicate": "associated with",
        "object": "homoviscous_lipid_composition",
        "description": (
            "Unsaturated fatty-acid changes are associated with the "
            "homeoviscous lipid composition branch in this mesophilic "
            "temperature-response graph."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "incorporation of proportionally more unsaturated fatty acids",
                "notes": (
                    "Verified against the public Annual Review of Microbiology "
                    "abstract; unsaturated fatty-acid incorporation is part of "
                    "homeoviscous membrane remodeling as growth temperature "
                    "decreases."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "balanced_growth",
        "description": (
            "Mesophilic balanced growth is associated with maintenance of "
            "target cytoplasmic-membrane fluidity."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "remodel the fluidity of their membrane bilayer",
                "notes": (
                    "Verified against the public Annual Review of Microbiology "
                    "abstract; the connector links membrane-fluidity remodeling "
                    "to growth-temperature acclimation without making a single "
                    "lipid ratio define mesophily."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "translation",
        "predicate": "associated with",
        "object": "balanced_growth",
        "description": (
            "Cold-shock maintenance of translation is a lower-temperature "
            "boundary-support branch for balanced mesophilic growth."
        ),
        "evidence": [
            {
                "reference": "DOI:10.4161/rna.7.6.13482",
                "snippet": "facilitating transcription and translation at low temperature",
                "notes": (
                    "Verified against the open Phadtare and Severinov PMC "
                    "abstract; the connector keeps CspA-family RNA chaperones "
                    "as low-temperature translation context, not as a "
                    "definition of mesophily."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "heat_shock_proteins",
        "predicate": "associated with",
        "object": "balanced_growth",
        "description": (
            "RpoH-regulated heat-shock response proteins form an upper-temperature "
            "boundary-support branch for balanced mesophilic growth."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.02174-23",
                "snippet": "heat shock genes encoding chaperones, such as DnaK and GroEL",
                "notes": (
                    "Verified against the open Grunberger et al. PMC text; the "
                    "connector keeps heat-shock chaperones as an upper-boundary "
                    "proteostasis branch, not as a definition of mesophily."
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
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")

    _assert_exact_edges(graph, source_connectors, "source")
    _assert_endpoints(graph, ADDED_EDGES)

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
            "by adding 4 source- and verbatim-snippet-backed association "
            "connectors among the homoviscous membrane, cold-shock RNA, and "
            "heat-shock boundary branches. No paid research service was called."
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
