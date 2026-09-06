#!/usr/bin/env python3
"""Review pH-range-mid2 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ph_range_mid2_graph_183.py
    python scripts/review_ph_range_mid2_graph_183.py --apply
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

SLUG = "environment/ph_range_mid2"
GRAPH_ID = "ph_range_mid2_mild_alkaline_tolerance"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T02:40:00Z"

NODE_REMOVALS: list[dict[str, Any]] = [
    {
        "node_id": "cytoplasm",
        "label": "cytoplasm",
        "node_type": "CELLULAR_LOCALIZATION",
        "description": "Intracellular compartment whose pH is regulated by antiport activity.",
        "grounding": "GO:0005737",
    },
]

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "membrane_potential",
            "label": "membrane potential (Δψ)",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Transmembrane electrical potential contributing to PMF.",
        },
        "after": {
            "node_id": "membrane_potential",
            "label": "membrane potential (Δψ)",
            "node_type": "STATE",
            "description": "Transmembrane electrical potential contributing to PMF.",
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "external_ph_7_8",
            "predicate": "permits maintenance of",
            "object": "cytoplasmic_ph_homeostasis",
            "description": "External pH 7-8 permits cells to keep internal pH near 7.0-7.5.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Internal pH kept within 7.0-7.5 and PMF relatively constant "
                        "across external pH 5-8."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_ph_7_8",
            "predicate": "associated with",
            "object": "cytoplasmic_ph_homeostasis",
            "description": (
                "External pH 7-8 is associated with cells maintaining internal pH near 7.0-7.5."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": (
                        "internal pH of many cell types is kept within the range of 7.0 to 7.5"
                    ),
                    "notes": (
                        "Verified against the open Poolman review; bacterial internal "
                        "pH is kept near 7.0-7.5 while neutralophilic bacteria maintain "
                        "PMF across mildly acidic to mildly alkaline external pH."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "cytoplasmic_buffering",
            "predicate": "stabilizes",
            "object": "cytoplasmic_ph_homeostasis",
            "description": (
                "Cytoplasmic buffering stabilizes internal pH given very low free proton count."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "A ~1 fL cytoplasm at pH 7.2 contains only ~10 free protons, "
                        "so buffering is critical."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cytoplasmic_buffering",
            "predicate": "contributes to",
            "object": "cytoplasmic_ph_homeostasis",
            "description": (
                "Cytoplasmic buffering contributes to internal pH homeostasis despite "
                "very low free-proton counts."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "buffering capacity of the cytoplasm",
                    "notes": (
                        "Verified against the open Poolman review; cytoplasmic "
                        "buffering is described as important for absorbing pH "
                        "fluctuations."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "na_h_antiport_activity",
            "predicate": "acidifies",
            "object": "cytoplasm",
            "description": (
                "Na+/H+ antiporter activity acidifies the cytoplasm when internal pH rises."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Na+/H+ and K+/H+ antiporters acidify the cytoplasm by "
                        "exchanging exported cations for H+."
                    ),
                }
            ],
        },
        "after": {
            "subject": "na_h_antiport_activity",
            "predicate": "regulates",
            "object": "cytoplasmic_ph_homeostasis",
            "description": ("Na+/H+ antiporter activity regulates cytoplasmic pH homeostasis."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "Na+/H+ and K+/H+ antiporters",
                    "notes": (
                        "Verified against the open Poolman review; Na+/H+ antiporters "
                        "are listed as key bacterial pH-homeostasis regulators and "
                        "acidifying exchangers when internal pH gets too high."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "proton_motive_force",
            "predicate": "remains relatively constant across",
            "object": "external_ph_5_8",
            "description": ("Neutralophiles keep PMF relatively constant across external pH ~5-8."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Neutralophilic bacteria adjust ΔpH vs Δψ so PMF stays "
                        "relatively constant across external pH ~5-8."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_ph_5_8",
            "predicate": "associated with",
            "object": "proton_motive_force",
            "description": ("Neutralophiles keep PMF relatively constant across external pH 5-8."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "kept relatively constant in the pH range from 5 to 8",
                    "notes": (
                        "Verified against the open Poolman review; neutralophilic "
                        "bacteria are described as maintaining a relatively constant "
                        "PMF across external pH 5-8."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "dpsi_dph_rebalancing",
            "predicate": "maintains",
            "object": "proton_motive_force",
            "description": ("Rebalancing of ΔpH and Δψ with external pH maintains PMF."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "The relative contribution of ΔpH and Δψ shifts with "
                        "external pH to preserve PMF."
                    ),
                }
            ],
        },
        "after": {
            "subject": "dpsi_dph_rebalancing",
            "predicate": "regulates",
            "object": "proton_motive_force",
            "description": ("Rebalancing of ΔpH and Δψ with external pH regulates PMF."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "interconvert the Δψ and ΔpH",
                    "notes": (
                        "Verified against the open Poolman review; transport "
                        "mechanisms are described as interconverting membrane "
                        "potential and ΔpH to maintain PMF and internal pH."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "f0f1_atpase",
            "predicate": "couples",
            "object": "atp_synthesis",
            "description": "F0F1-ATPase couples the proton motive force to ATP synthesis.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": "PMF drives ATP synthesis; F0F1 uses ~3-5 H+ per ATP.",
                }
            ],
        },
        "after": {
            "subject": "f0f1_atpase",
            "predicate": "enables",
            "object": "atp_synthesis",
            "description": "F0F1-ATPase couples the proton motive force to ATP synthesis.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "PMF for nutrient uptake and ATP synthesis",
                    "notes": (
                        "Verified against the open Poolman review; the PMF links "
                        "proton translocation by the F0F1-ATPase to ATP synthesis."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "proton_ion_antiporters",
            "predicate": "maintain",
            "object": "membrane_potential",
            "description": (
                "Proton:ion antiporters have a direct role in maintaining membrane potential."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-biophys-030822-032215",
                    "notes": (
                        "Antiporters have a direct role in maintaining membrane "
                        "potential in E. coli."
                    ),
                }
            ],
        },
        "after": {
            "subject": "proton_ion_antiporters",
            "predicate": "generates",
            "object": "membrane_potential",
            "description": (
                "Proton:ion antiporters generate membrane potential in the E. coli "
                "pH-homeostasis model."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1103/PRXLife.2.043015",
                    "snippet": "use antiporters to generate the plasma membrane potential",
                    "notes": (
                        "Verified against the open PRX Life abstract; Terradot et "
                        "al. model proton-ion antiporters as generators of membrane "
                        "potential and thus PMF in E. coli."
                    ),
                }
            ],
            "predicate_id": "biolink:produces",
        },
    },
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _node_key(node: dict[str, Any]) -> str | None:
    return node.get("node_id")


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


def _node_replacements_by_state(state: str) -> dict[str | None, dict[str, Any]]:
    return {_node_key(replacement[state]): replacement[state] for replacement in NODE_REPLACEMENTS}


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


def _assert_exact_nodes(
    graph: dict[str, Any],
    expected_by_key: dict[str | None, dict[str, Any]],
    state: str,
) -> None:
    existing_by_key = {_node_key(node): node for node in graph.get("nodes") or []}
    missing = set(expected_by_key) - set(existing_by_key)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} node(s): {sorted(missing)}")
    for key, expected in expected_by_key.items():
        if existing_by_key[key] != expected:
            raise ValueError(f"{SLUG}: {state} node drifted: {key}")


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def _has_exact_nodes(
    graph: dict[str, Any],
    nodes: dict[str | None, dict[str, Any]],
) -> bool:
    existing_by_key = {_node_key(node): node for node in graph.get("nodes") or []}
    return all(existing_by_key.get(key) == node for key, node in nodes.items())


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_edges = _replacements_by_state("before")
    after_edges = _replacements_by_state("after")
    before_nodes = _node_replacements_by_state("before")
    after_nodes = _node_replacements_by_state("after")
    removed_nodes = {_node_key(node): node for node in NODE_REMOVALS}

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    existing_nodes = {_node_key(node): node for node in graph.get("nodes") or []}
    migrated_nodes = _has_exact_nodes(graph, after_nodes)
    removed_nodes_absent = set(removed_nodes).isdisjoint(existing_nodes)

    if _has_exact_edges(graph, after_edges) and migrated_nodes and removed_nodes_absent:
        return False

    if present_migrated_edge_keys == migrated_edge_keys and removed_nodes_absent:
        _assert_exact_edges(graph, after_edges, "migrated")
        _assert_exact_nodes(graph, after_nodes, "migrated")
        return False

    if present_migrated_edge_keys or migrated_nodes or removed_nodes_absent:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_edge_keys)}")

    _assert_exact_edges(graph, before_edges, "source")
    _assert_exact_nodes(graph, before_nodes | removed_nodes, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    after_by_before_node_key = {
        _node_key(replacement["before"]): replacement["after"] for replacement in NODE_REPLACEMENTS
    }
    graph["nodes"] = [
        copy.deepcopy(after_by_before_node_key.get(_node_key(node), node))
        for node in graph.get("nodes") or []
        if _node_key(node) not in removed_nodes
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
            "Reviewed the ph_range_mid2_mild_alkaline_tolerance graph for issue "
            "#183: added snippets to 7 edge-level evidence items, grounded 7 "
            "unmapped pH-homeostasis predicates, retyped membrane_potential to "
            "STATE, and removed the no-longer-used cytoplasm node. No paid "
            "research service was called."
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
