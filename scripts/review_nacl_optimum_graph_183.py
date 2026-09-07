#!/usr/bin/env python3
"""Review broad NaCl-optimum graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_nacl_optimum_graph_183.py
    python scripts/review_nacl_optimum_graph_183.py --apply
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

SLUG = "environment/nacl_optimum"
GRAPH_ID = "nacl_optimum_balanced_osmoadaptation"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T01:00:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "na_antiport_activity",
            "label": "Na+/H+ antiport activity",
            "node_type": "MOLECULAR_FUNCTION",
            "description": (
                "Antiporter-mediated Na+ extrusion lowering cytoplasmic Na+ to prevent toxicity."
            ),
        },
        "after": {
            "node_id": "na_k_h_transport_activity",
            "label": "Na+/K+/H+ transporter activity",
            "node_type": "MOLECULAR_FUNCTION",
            "description": (
                "Cation/proton transporter activity preserving intracellular K+ "
                "concentration and broader ion homeostasis under varying salinities."
            ),
        },
    },
    {
        "before": {
            "node_id": "cytoplasmic_na_homeostasis",
            "label": "cytoplasmic Na+ homeostasis",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Maintenance of low cytoplasmic Na+ concentration to prevent ion toxicity."
            ),
        },
        "after": {
            "node_id": "cellular_ion_homeostasis",
            "label": "cellular ion homeostasis",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Maintenance of cytoplasmic potassium concentration and broader "
                "cellular ion balance during salinity change."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "ambient_nacl",
            "predicate": "induces",
            "object": "osmotic_stress",
            "description": (
                "External NaCl concentration imposes osmotic stress that drives osmoadaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "notes": (
                        "Halophilic microorganisms use two strategies to balance "
                        "their cytoplasm osmotically with their medium (broad "
                        "review-level mechanism)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "ambient_nacl",
            "predicate": "causes",
            "object": "osmotic_stress",
            "description": (
                "External NaCl creates the osmotic imbalance that requires "
                "osmoadaptive compensation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "snippet": "cytoplasm has to be at least isoosmotic",
                    "notes": (
                        "Verified against the open Oren review; halophilic cells "
                        "must osmotically balance the cytoplasm against high-salt "
                        "medium."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "salt_in_strategy",
            "predicate": "increases",
            "object": "intracellular_k_accumulation",
            "description": (
                "The salt-in strategy accumulates molar concentrations of KCl in the cytoplasm."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "notes": (
                        "The first involves accumulation of molar concentrations of "
                        "KCl; strong general mechanism across extreme halophiles."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "salt_in_strategy",
            "predicate": "increases",
            "object": "intracellular_k_accumulation",
            "description": (
                "The salt-in strategy accumulates molar potassium and chloride "
                "concentrations in the cytoplasm."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "snippet": "accumulation of molar concentrations of potassium and chloride",
                    "notes": (
                        "Verified against the open Oren review; high-salt-in "
                        "organisms balance external salt primarily with "
                        "intracellular KCl."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "acidic_proteome",
            "predicate": "enables",
            "object": "protein_stability_high_salt",
            "description": (
                "An acidic proteome enables protein stability and enzymatic function "
                "at high intracellular salt."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "notes": (
                        "The proteome of such organisms is highly acidic; requires "
                        "adaptation of the intracellular enzymatic machinery at "
                        "near-saturating salt."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "acidic_proteome",
            "predicate": "enables",
            "object": "protein_stability_high_salt",
            "description": (
                "An acidic proteome enables protein folding and enzymatic function "
                "under near-saturating intracellular salt."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "snippet": "extensive adaptation of the intracellular enzymatic machinery",
                    "notes": (
                        "Verified against the open Oren review; high-salt-in "
                        "strategists require intracellular enzymatic machinery "
                        "adapted to molar salt."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "compatible_solute_accumulation",
            "predicate": "regulates",
            "object": "osmotic_balance",
            "description": (
                "Accumulation of organic compatible solutes maintains osmotic "
                "balance without interfering with enzyme activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "notes": (
                        "Exclude salt from the cytoplasm and synthesize/accumulate "
                        "organic compatible solutes that do not interfere with "
                        "enzymatic activity; broad canonical mechanism."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "compatible_solute_accumulation",
            "predicate": "regulates",
            "object": "osmotic_balance",
            "description": (
                "Organic compatible-solute accumulation regulates osmotic balance "
                "while limiting inorganic salt in the cytoplasm."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/1746-1448-4-2",
                    "snippet": "exclude salt from their cytoplasm as much as possible",
                    "notes": (
                        "Verified against the open Oren review; the salt-out "
                        "strategy excludes salt from the cytoplasm and accumulates "
                        "organic solutes that minimally perturb enzymatic activity."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "compatible_solute_uptake",
            "predicate": "associated with",
            "object": "lower_energetic_cost",
            "description": (
                "Uptake of compatible solutes from the medium is energetically "
                "favored over de novo synthesis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2022.846677",
                    "notes": (
                        "Uptake of compatible solute from the medium is preferred "
                        "over de novo synthesis, reflecting an energetically "
                        "favored mechanism."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
        "after": {
            "subject": "compatible_solute_uptake",
            "predicate": "associated with",
            "object": "lower_energetic_cost",
            "description": (
                "Compatible-solute uptake is associated with lower energetic cost "
                "than de novo compatible-solute synthesis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2022.846677",
                    "snippet": "uptake of compatible solute from the medium is preferred",
                    "notes": (
                        "Verified against the open Halomonas elongata review; "
                        "external compatible-solute uptake is energetically "
                        "preferred over de novo synthesis."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "na_antiport_activity",
            "predicate": "regulates",
            "object": "cytoplasmic_na_homeostasis",
            "description": (
                "Na+/H+ antiport activity lowers cytoplasmic Na+ to maintain ion "
                "homeostasis and prevent toxicity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/aem.00145-24",
                    "notes": (
                        "Na+/H+ antiporters function to lower cytoplasmic Na+ to "
                        "prevent toxicity and contribute to salt acclimation."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "na_k_h_transport_activity",
            "predicate": "regulates",
            "object": "cellular_ion_homeostasis",
            "description": (
                "Na+/K+/H+ transporter activity contributes to cellular ion "
                "homeostasis under varying salinities."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/aem.00145-24",
                    "snippet": (
                        "transport systems that regulate intracellular Na+/K+/H+ concentration"
                    ),
                    "notes": (
                        "Verified against the Xing et al. long-term salinity-stress "
                        "study; the edge was broadened from Na+ homeostasis to "
                        "match the reported Na+/K+/H+ transporter and intracellular "
                        "K+ response."
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


def _assert_exact_nodes(
    graph: dict[str, Any],
    expected_by_id: dict[str | None, dict[str, Any]],
    state: str,
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


def _replacements_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _nodes_by_state(state: str) -> dict[str | None, dict[str, Any]]:
    return {
        replacement[state].get("node_id"): replacement[state] for replacement in NODE_REPLACEMENTS
    }


def _has_exact_state(
    graph: dict[str, Any],
    nodes: dict[str | None, dict[str, Any]],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_edges = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    existing_nodes = {node.get("node_id"): node for node in graph.get("nodes") or []}
    return all(existing_nodes.get(node_id) == node for node_id, node in nodes.items()) and all(
        existing_edges.get(key) == edge for key, edge in edges.items()
    )


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_edges = _replacements_by_state("before")
    after_edges = _replacements_by_state("after")
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    migrated_keys = set(after_edges) - set(before_edges)
    migrated_node_ids = set(after_nodes) - set(before_nodes)
    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    existing_node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    present_migrated_keys = existing_keys & migrated_keys
    present_migrated_node_ids = existing_node_ids & migrated_node_ids

    if _has_exact_state(graph, after_nodes, after_edges):
        return False

    if present_migrated_keys == migrated_keys and present_migrated_node_ids == migrated_node_ids:
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_keys or present_migrated_node_ids:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"{sorted(present_migrated_keys)}, {sorted(present_migrated_node_ids)}"
        )

    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    after_node_by_before_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }

    graph["nodes"] = [
        copy.deepcopy(after_node_by_before_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the broad nacl_optimum_balanced_osmoadaptation graph for "
            "issue #183: added snippets to 6 edge-level evidence items, regrounded "
            "the ambient-NaCl osmotic-stress edge to biolink:causes, and broadened "
            "one transporter edge from Na+ homeostasis to Na+/K+/H+ transporter "
            "control of cellular ion homeostasis. No paid research service was "
            "called."
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
