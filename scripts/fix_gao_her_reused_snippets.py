#!/usr/bin/env python3
"""Trim repeated Gao-Her subclass evidence snippets."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-09-27T13:56:56Z"
CURATOR = "codex"

PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_system.yaml"
CHILDREN = [
    (
        REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_duf_system.yaml",
        "traitmech:000361",
        "gao_her_duf_locus_restricts_phage",
    ),
    (
        REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_sir_system.yaml",
        "traitmech:000362",
        "gao_her_sir_locus_restricts_phage",
    ),
]


def load(path: Path) -> dict[str, Any]:
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise SystemExit(f"{path}: expected mapping")
    return doc


def one_graph(doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    matches = [
        graph
        for graph in doc.get("causal_graphs") or []
        if graph.get("graph_id") == graph_id
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected one {graph_id} graph, found {len(matches)}")
    return matches[0]


def fix_parent(doc: dict[str, Any]) -> None:
    if doc.get("identifier") != "traitmech:000409":
        raise SystemExit("unexpected Gao-Her parent identifier")
    graph = one_graph(doc, "gao_her_locus_restricts_phage")
    edges = [
        edge
        for edge in graph.get("edges") or []
        if edge.get("subject") == "gao_2020_antiviral_cassette_defense"
        and edge.get("object") == "gao_her_system_trait"
    ]
    if len(edges) != 1:
        raise SystemExit(f"expected one Gao-Her confers edge, found {len(edges)}")
    edge = edges[0]
    evidence = edge.get("evidence") or []
    if len(evidence) != 2 or evidence[1].get("snippet", "").split(" | ", 1)[0] != "Gao_Her":
        raise SystemExit("unexpected Gao-Her confers evidence preimage")
    edge["evidence"] = evidence[:1]
    record_curation_event(
        doc,
        curator=CURATOR,
        action="EDIT",
        changes=(
            "Removed a repeated DefenseFinder article-row citation from the "
            "Gao-Her confers edge so no graph reuses the same snippet more "
            "than twice."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def fix_child(doc: dict[str, Any], expected_id: str, graph_id: str) -> None:
    if doc.get("identifier") != expected_id:
        raise SystemExit(f"expected {expected_id}, found {doc.get('identifier')!r}")

    graph = one_graph(doc, graph_id)
    parent_edges = [
        edge
        for edge in graph.get("edges") or []
        if edge.get("subject") == "gao_her_system"
        and edge.get("object") == "phage_defense_system"
    ]
    if len(parent_edges) != 1:
        raise SystemExit(f"{graph_id}: expected one Gao-Her-to-phage edge")

    graph["edges"] = [
        edge
        for edge in graph["edges"]
        if not (
            edge.get("subject") == "gao_her_system"
            and edge.get("object") == "phage_defense_system"
        )
    ]
    graph["nodes"] = [
        node
        for node in graph.get("nodes") or []
        if node.get("node_id") != "phage_defense_system"
    ]
    for edge in graph["edges"]:
        if edge.get("object") == "phage_defense_system":
            raise SystemExit(f"{graph_id}: phage_defense_system edge still present")

    record_curation_event(
        doc,
        curator=CURATOR,
        action="EDIT",
        changes=(
            "Removed the redundant Gao-Her-to-phage subclass edge from the "
            "child graph; the Gao-Her parent record now carries that edge."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def main() -> int:
    parent = load(PARENT)
    fix_parent(parent)
    write_validated_trait(parent, PARENT)
    print(f"updated {PARENT.relative_to(REPO_ROOT)}")

    for path, expected_id, graph_id in CHILDREN:
        child = load(path)
        fix_child(child, expected_id, graph_id)
        write_validated_trait(child, path)
        print(f"updated {path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
