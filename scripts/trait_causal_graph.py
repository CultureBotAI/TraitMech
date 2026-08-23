"""Helpers for rendering TraitMech causal graphs as pathograph JSON."""
from __future__ import annotations

from typing import Any


NODE_COLORS = {
    "TRAIT": "#dbeafe",
    "PATHWAY": "#e0e7ff",
    "ENVIRONMENTAL_FACTOR": "#dcfce7",
    "EXPERIMENTAL_FACTOR": "#ccfbf1",
    "GENE_OR_PROTEIN": "#f3e8ff",
    "CHEMICAL": "#fef3c7",
    "ORGANELLE": "#fce7f3",
    "CELLULAR_LOCALIZATION": "#ede9fe",
    "MOLECULAR_FUNCTION": "#cffafe",
    "BIOLOGICAL_PROCESS": "#ecfccb",
    "ORPHAN": "#fee2e2",
    "UNKNOWN": "#f3f4f6",
}


def causal_graphs_for_template(record: dict[str, Any]) -> list[dict[str, Any]]:
    """Return pathograph-ready graph dictionaries for a TraitRecord."""
    graphs = record.get("causal_graphs") or []
    if not isinstance(graphs, list):
        return []
    return [_graph_for_template(graph) for graph in graphs if isinstance(graph, dict)]


def _graph_for_template(graph: dict[str, Any]) -> dict[str, Any]:
    nodes = graph.get("nodes") or []
    edges = graph.get("edges") or []
    node_by_id = {
        str(node.get("node_id")): node
        for node in nodes
        if isinstance(node, dict) and node.get("node_id")
    }

    used_node_ids: set[str] = set()
    issues: list[str] = []
    for edge in edges:
        if not isinstance(edge, dict):
            continue
        subject = str(edge.get("subject") or "")
        obj = str(edge.get("object") or "")
        if subject:
            used_node_ids.add(subject)
        if obj:
            used_node_ids.add(obj)
        if subject and subject not in node_by_id:
            issues.append(f"Subject '{subject}' is not defined in graph nodes.")
        if obj and obj not in node_by_id:
            issues.append(f"Object '{obj}' is not defined in graph nodes.")

    rendered_nodes = []
    for node_id in sorted(used_node_ids or set(node_by_id)):
        raw = node_by_id.get(node_id)
        if raw:
            node_type = str(raw.get("node_type") or "UNKNOWN")
            rendered_nodes.append({
                "id": node_id,
                "label": raw.get("label") or node_id,
                "node_type": node_type,
                "color": NODE_COLORS.get(node_type, NODE_COLORS["UNKNOWN"]),
                "grounding": raw.get("grounding"),
                "xrefs": raw.get("xrefs") or [],
                "description": raw.get("description"),
                "protein_examples": raw.get("protein_examples") or [],
                "is_orphan": False,
            })
        else:
            rendered_nodes.append({
                "id": node_id,
                "label": node_id,
                "node_type": "ORPHAN",
                "color": NODE_COLORS["ORPHAN"],
                "is_orphan": True,
            })

    rendered_edges = []
    evidence_rows = []
    for index, edge in enumerate(edges, start=1):
        if not isinstance(edge, dict):
            continue
        edge_id = f"edge-{index}"
        subject = str(edge.get("subject") or "")
        obj = str(edge.get("object") or "")
        evidence = edge.get("evidence") or []
        rendered_edges.append({
            "id": edge_id,
            "source": subject,
            "target": obj,
            "predicate": edge.get("predicate") or "",
            "predicate_id": edge.get("predicate_id"),
            "description": edge.get("description"),
            "evidence": evidence,
            "is_orphan": subject not in node_by_id or obj not in node_by_id,
        })
        evidence_rows.append({
            "edge_id": edge_id,
            "source": _node_label(node_by_id, subject),
            "target": _node_label(node_by_id, obj),
            "predicate": edge.get("predicate") or "",
            "predicate_id": edge.get("predicate_id"),
            "description": edge.get("description"),
            "evidence": evidence,
        })

    protein_example_rows = []
    for node in nodes:
        if not isinstance(node, dict) or node.get("node_type") != "GENE_OR_PROTEIN":
            continue
        for example in node.get("protein_examples") or []:
            if not isinstance(example, dict):
                continue
            protein_example_rows.append({
                "node_id": node.get("node_id"),
                "node_label": node.get("label") or node.get("node_id"),
                **example,
            })

    return {
        "graph_id": graph.get("graph_id") or "causal-graph",
        "title": graph.get("title") or "Causal graph",
        "description": graph.get("description"),
        "scope_status": graph.get("scope_status"),
        "scope_notes": graph.get("scope_notes"),
        "nodes": rendered_nodes,
        "edges": rendered_edges,
        "issues": issues,
        "evidence_rows": evidence_rows,
        "protein_example_rows": protein_example_rows,
    }


def _node_label(node_by_id: dict[str, dict[str, Any]], node_id: str) -> str:
    node = node_by_id.get(node_id)
    if not node:
        return node_id
    return str(node.get("label") or node_id)
