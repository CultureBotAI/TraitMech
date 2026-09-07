#!/usr/bin/env python3
"""Review cell_length_small graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_cell_length_small_graph_183.py
    python scripts/review_cell_length_small_graph_183.py --apply
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

SLUG = "morphology/cell_length_small"
GRAPH_ID = "cell_length_small_size_setpoint"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T05:40:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "ftsz_abundance",
            "grounding_status": "REVIEWED_LABEL_ONLY",
            "grounding_notes": (
                "This contextual node denotes abundance of a protein family rather "
                "than the FtsZ molecular entity itself."
            ),
            "label": "FtsZ abundance",
            "node_type": "GENE_OR_PROTEIN",
            "description": "Cellular level of the tubulin-like division protein FtsZ.",
        },
        "after": {
            "node_id": "ftsz_abundance",
            "label": "FtsZ abundance",
            "node_type": "QUALITY",
            "description": ("Relative cellular level of the tubulin-like division protein FtsZ."),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "ftsz_abundance",
            "predicate": "rate_limiting_for",
            "object": "division_timing",
            "description": (
                "FtsZ levels are a rate-limiting factor for division timing; higher "
                "FtsZ promotes earlier division."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-54242-w",
                    "notes": (
                        "FtsZ numbers are identified as one of the rate-limiting "
                        "factors for cell divisions."
                    ),
                }
            ],
        },
        "after": {
            "subject": "ftsz_abundance",
            "predicate": "contributes to",
            "object": "division_timing",
            "description": (
                "FtsZ abundance is a rate-limiting factor for E. coli cell division timing."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-54242-w",
                    "snippet": (
                        "FtsZ numbers in the cell are one of the rate-limiting "
                        "factors for cell divisions in E. coli"
                    ),
                    "notes": (
                        "Verified against the public Nature Communications "
                        "abstract; Männik et al. identify FtsZ number as a "
                        "rate-limiting factor for E. coli cell division."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "ftsz_ring_formation",
            "predicate": "modulates",
            "object": "cell_length_trait",
            "description": (
                "Delayed FtsZ ring formation delays division until the cell reaches "
                "a larger size, increasing cell length."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-41487-0",
                    "notes": "Delay cell division until the cell reaches a larger size.",
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "ftsz_ring_formation",
            "predicate": "modulates",
            "object": "cell_length_trait",
            "description": (
                "Delayed FtsZ ring formation delays division until the cell reaches "
                "a larger size, increasing cell length."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-41487-0",
                    "snippet": (
                        "delays the FtsZ ring formation, which in turn allows the "
                        "cell to grow for a longer time"
                    ),
                    "notes": (
                        "Verified against the open Nature Communications "
                        "introduction; Vashistha et al. describe Min-imbalance "
                        "delaying FtsZ ring formation and giving cells more time "
                        "to grow before division."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "ftsn",
            "predicate": "activates",
            "object": "ftswi_complex",
            "description": "FtsN allosterically activates the FtsWI septal PG synthase complex.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-52217-5",
                    "notes": (
                        "Activation of the sPG synthase (FtsWI within the FtsQLBWI "
                        "complex) depends on FtsN."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "ftsn",
            "predicate": "activates",
            "object": "ftswi_complex",
            "description": "FtsN allosterically activates the FtsWI septal PG synthase complex.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-52217-5",
                    "snippet": (
                        "FtsN activates sPG synthesis by switching FtsA and the "
                        "FtsQLBWI complex to the active state"
                    ),
                    "notes": (
                        "Verified against the open Nature Communications full "
                        "text; Gong et al. route FtsN-mediated septal "
                        "peptidoglycan synthesis through the active FtsQLBWI "
                        "complex that contains FtsW and FtsI."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "septal_pg_synthesis",
            "predicate": "promotes",
            "object": "zring_condensation",
            "description": (
                "Septal peptidoglycan synthesis feeds back to promote Z-ring "
                "condensation and stability."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-52217-5",
                    "notes": (
                        "Septal cell wall synthesis feeds back to promote Z ring "
                        "condensation and stability."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "septal_pg_synthesis",
            "predicate": "promotes",
            "object": "zring_condensation",
            "description": (
                "Septal peptidoglycan synthesis feeds back to promote Z-ring "
                "condensation and stability."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-52217-5",
                    "snippet": ("sPG synthesis in turn promotes Z ring condensation and stability"),
                    "notes": (
                        "Verified against the open Nature Communications full "
                        "text; Gong et al. show a positive-feedback loop from "
                        "septal peptidoglycan synthesis to the Z ring."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "ftsz_protoring",
            "predicate": "organizes",
            "object": "divisome_assembly",
            "description": (
                "The FtsZ proto-ring with FtsA/ZipA organizes divisome assembly and "
                "is required for localization of other divisome proteins."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41579-023-00942-x",
                    "notes": ("FtsZ is required for localization of all other divisome proteins."),
                }
            ],
        },
        "after": {
            "subject": "ftsz_protoring",
            "predicate": "enables",
            "object": "divisome_assembly",
            "description": (
                "The FtsZ proto-ring with FtsA/ZipA localizes and organizes "
                "divisome assembly at midcell."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41579-023-00942-x",
                    "snippet": (
                        "FtsZ, to localize and organize the cell division machinery, the divisome"
                    ),
                    "notes": (
                        "Verified against the public PubMed abstract for the "
                        "Nature Reviews Microbiology article; Cameron and "
                        "Margolin review FtsZ as the tubulin homolog that "
                        "organizes the divisome."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "min_nucleoid_occlusion",
            "predicate": "positions",
            "object": "ftsz_midcell_positioning",
            "description": (
                "Min system and nucleoid occlusion position FtsZ at midcell for "
                "proper division-site placement."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s42003-024-07279-y",
                    "notes": "For positioning FtsZ at mid cell division sites.",
                }
            ],
        },
        "after": {
            "subject": "min_nucleoid_occlusion",
            "predicate": "regulates",
            "object": "ftsz_midcell_positioning",
            "description": (
                "Min and nucleoid-occlusion systems regulate FtsZ placement at "
                "midcell for proper division-site selection."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s42003-024-07279-y",
                    "snippet": (
                        "Min or nucleoid occlusion systems for positioning FtsZ "
                        "at mid cell division sites"
                    ),
                    "notes": (
                        "Verified against the public Communications Biology "
                        "abstract; Hayashi et al. require at least one of the "
                        "Min or nucleoid-occlusion systems for midcell FtsZ "
                        "positioning in E. coli L-forms."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
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


def _nodes_by_state(state: str) -> dict[str, dict[str, Any]]:
    return {replacement[state]["node_id"]: replacement[state] for replacement in NODE_REPLACEMENTS}


def _edges_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_nodes(
    graph: dict[str, Any], expected_by_id: dict[str, dict[str, Any]], state: str
) -> None:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    missing = set(expected_by_id) - set(existing_by_id)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} node(s): {sorted(missing)}")
    for node_id, expected in expected_by_id.items():
        if existing_by_id[node_id] != expected:
            raise ValueError(f"{SLUG}: {state} node drifted: {node_id}")


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


def _has_exact_nodes(graph: dict[str, Any], nodes: dict[str, dict[str, Any]]) -> bool:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    return all(existing_by_id.get(node_id) == node for node_id, node in nodes.items())


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
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    has_after_nodes = _has_exact_nodes(graph, after_nodes)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_nodes and has_after_edges:
        return False

    if present_migrated_edge_keys == migrated_edge_keys:
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_edge_keys)}")

    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_node_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }
    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["nodes"] = [
        copy.deepcopy(after_by_before_node_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the cell_length_small_size_setpoint graph for issue #183: "
            "added exact snippets to 6 FtsZ/divisome evidence items, grounded 3 "
            "residual predicates, and retyped FtsZ abundance as a QUALITY node. "
            "The METPO 1.3-2 micrometre length bin remains a nonmechanistic "
            "classification. No paid research service was called."
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
