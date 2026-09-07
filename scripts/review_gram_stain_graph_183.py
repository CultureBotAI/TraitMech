#!/usr/bin/env python3
"""Review gram_stain graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_gram_stain_graph_183.py
    python scripts/review_gram_stain_graph_183.py --apply
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

SLUG = "morphology/gram_stain"
GRAPH_ID = "gram_stain_cell_envelope_retention"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T06:00:00Z"

NODE_ADDITIONS: list[dict[str, Any]] = [
    {
        "node_id": "crystal_violet_iodine_retention",
        "label": "crystal violet-iodine retention",
        "node_type": "QUALITY",
        "description": (
            "Retention of the crystal violet-iodine complex after Gram decolorization."
        ),
    }
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "crystal_violet",
            "predicate": "reacts with",
            "object": "iodine_mordant",
            "description": ("Crystal violet and iodine form a dye complex during the Gram stain."),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.156.2.837-845.1983",
                    "snippet": "produce a chemical precipitate",
                    "notes": (
                        "Supports chemical formation of the crystal violet-iodine precipitate."
                    ),
                }
            ],
        },
        "after": {
            "subject": "crystal_violet",
            "predicate": "contributes to",
            "object": "crystal_violet_iodine_complex",
            "description": (
                "Crystal violet contributes the dye cation to the insoluble "
                "crystal violet-iodide precipitate formed during the Gram stain."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.156.2.837-845.1983",
                    "snippet": (
                        "interacts with aqueous KI-I2 during the Gram stain via a "
                        "simple metathetical anion exchange"
                    ),
                    "notes": (
                        "Verified against the open Davies et al. abstract; crystal "
                        "violet reacts with the iodide mordant during Gram staining "
                        "to form the insoluble dye-iodide precipitate."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "crystal_violet_iodine_complex",
            "predicate": "is retained by",
            "object": "peptidoglycan_cell_wall",
            "description": (
                "Cell-wall architecture determines whether the dye complex remains "
                "after decolorization."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3109/10520299609117151",
                    "snippet": "cell wall ... responsible for retention",
                    "notes": (
                        "Review supports the Gram-positive cell wall as responsible "
                        "for retaining the dye-iodine complex."
                    ),
                }
            ],
        },
        "after": {
            "subject": "peptidoglycan_cell_wall",
            "predicate": "contributes to",
            "object": "crystal_violet_iodine_retention",
            "description": (
                "Peptidoglycan wall architecture determines whether the dye complex "
                "remains after decolorization."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3109/10520299609117151",
                    "snippet": ("responsible for retention of a crystal violet:iodine complex"),
                    "notes": (
                        "Verified against the public Popescu and Doyle abstract; "
                        "the Gram-positive cell wall is the structural determinant "
                        "for retaining the dye-iodine complex."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "alcohol_decolorization",
            "predicate": "removes",
            "object": "outer_membrane",
            "description": (
                "Decolorization disrupts the Gram-negative outer membrane and helps "
                "remove dye complex."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.156.2.837-845.1983",
                    "snippet": "alcohol-acetone decolorization",
                    "notes": (
                        "Supports decolorization as a chemical step differentiating Gram reactions."
                    ),
                }
            ],
        },
        "after": {
            "subject": "alcohol_decolorization",
            "predicate": "contributes to",
            "object": "gram_stain_trait",
            "description": (
                "Decolorization contributes to the differential Gram reaction by "
                "damaging Gram-negative cell surfaces and causing dye-complex loss."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3109/10520299609117151",
                    "snippet": (
                        "staining procedures damage the cell surface resulting in "
                        "loss of dye complexes"
                    ),
                    "notes": (
                        "Verified against the public Popescu and Doyle abstract; "
                        "decolorization is retained as an assay step contributing "
                        "to the broad Gram stain phenotype rather than asserted as "
                        "complete outer-membrane removal."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "peptidoglycan_cell_wall",
            "predicate": "causes",
            "object": "gram_stain_trait",
            "description": (
                "Peptidoglycan thickness and envelope architecture determine Gram stain outcome."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3109/10520299609117151",
                    "snippet": "mechanism of the Gram stain",
                    "notes": "Supports cell-wall mediated Gram reaction.",
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "peptidoglycan_cell_wall",
            "predicate": "causes",
            "object": "gram_stain_trait",
            "description": (
                "Peptidoglycan wall structure is the major structural determinant "
                "of differential Gram-stain retention."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3109/10520299609117151",
                    "snippet": "Gram-stainability is a function of the cell wall",
                    "notes": (
                        "Verified against the public Popescu and Doyle abstract; "
                        "the review ties the Gram reaction to the cell wall rather "
                        "than chemistry of intracellular constituents."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
]

EDGE_ADDITIONS: list[dict[str, Any]] = [
    {
        "subject": "iodine_mordant",
        "predicate": "contributes to",
        "object": "crystal_violet_iodine_complex",
        "description": (
            "The iodide mordant supplies the bulky anion that reacts with crystal "
            "violet to form the dye-iodide precipitate."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.156.2.837-845.1983",
                "snippet": "apparent 1:1 stoichiometry between anion (I-) and cation",
                "notes": (
                    "Verified against the open Davies et al. abstract; the iodide "
                    "anion and crystal-violet cation react stoichiometrically in "
                    "the Gram stain."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "crystal_violet_iodine_complex",
        "predicate": "contributes to",
        "object": "crystal_violet_iodine_retention",
        "description": (
            "The insoluble crystal violet-iodine complex is the retained dye "
            "precipitate that initiates the Gram reaction."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.156.2.837-845.1983",
                "snippet": "same precipitate which forms in the cellular substance of bacteria",
                "notes": (
                    "Verified against the open Davies et al. abstract; the "
                    "crystal violet-iodide precipitate forms inside both "
                    "Gram-positive and Gram-negative bacteria before the "
                    "differential decolorization step."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "crystal_violet_iodine_retention",
        "predicate": "confers",
        "object": "gram_stain_trait",
        "description": (
            "Differential retention of the dye-iodine complex is the proximal "
            "assay state for the Gram stain phenotype."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3109/10520299609117151",
                "snippet": "retention of a crystal violet:iodine complex",
                "notes": (
                    "Verified against the public Popescu and Doyle abstract; the "
                    "review frames Gram staining around retention of the "
                    "crystal violet-iodine complex."
                ),
            }
        ],
        "predicate_id": "METPO:2007700",
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


def _nodes_by_id(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {node["node_id"]: node for node in nodes}


def _edges_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _edges_by_key(
    edges: list[dict[str, Any]],
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(edge): edge for edge in edges}


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
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")
    addition_nodes = _nodes_by_id(NODE_ADDITIONS)
    addition_edges = _edges_by_key(EDGE_ADDITIONS)

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_addition_node_ids = existing_node_ids & set(addition_nodes)
    present_addition_edge_keys = existing_edge_keys & set(addition_edges)
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    has_after_nodes = _has_exact_nodes(graph, addition_nodes)
    has_after_edges = _has_exact_edges(graph, after_edges) and _has_exact_edges(
        graph, addition_edges
    )
    if has_after_nodes and has_after_edges:
        return False

    if (
        present_addition_node_ids == set(addition_nodes)
        and present_addition_edge_keys == set(addition_edges)
        and present_migrated_edge_keys == migrated_edge_keys
    ):
        _assert_exact_nodes(graph, addition_nodes, "migrated")
        _assert_exact_edges(graph, after_edges | addition_edges, "migrated")
        return False

    if present_addition_node_ids or present_addition_edge_keys or present_migrated_edge_keys:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"nodes={sorted(present_addition_node_ids)} "
            f"edges={sorted(present_addition_edge_keys | present_migrated_edge_keys)}"
        )

    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["nodes"] = [*graph.get("nodes", []), *copy.deepcopy(NODE_ADDITIONS)]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]
    graph["edges"].extend(copy.deepcopy(EDGE_ADDITIONS))

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the gram_stain_cell_envelope_retention graph for issue "
            "#183: added exact snippets to 4 assay evidence entries, replaced "
            "3 residual predicates, added a dye-retention node with 3 grounded "
            "connector edges, and connected the reagent chemistry to the "
            "retention phenotype. No paid research service was called."
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
