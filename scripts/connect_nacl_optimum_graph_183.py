#!/usr/bin/env python3
"""Connect the NaCl-optimum contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_nacl_optimum_graph_183.py
    python scripts/connect_nacl_optimum_graph_183.py --apply
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

SLUG = "environment/nacl_optimum"
GRAPH_ID = "nacl_optimum_balanced_osmoadaptation"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T14:00:00Z"
EXPECTED_COMPONENTS = 5

GRAPH_METADATA_BEFORE = {
    "title": "NaCl-optimum balanced osmoadaptation",
    "description": (
        "DOI-backed graph linking ambient NaCl, osmotic balance via compatible "
        "solutes and ion homeostasis, and maximal growth rate to the NaCl-optimum "
        "phenotype."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "NaCl optimum with salt-in, salt-out, and transporter support",
    "description": (
        "DOI-backed nonmechanistic graph connecting ambient NaCl, osmotic "
        "balance, salt-in K+ accumulation, acidic-proteome support, "
        "compatible-solute accumulation and uptake, cation transport, and maximal "
        "growth rate for the NaCl-optimum phenotype."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
                "snippet": "transport systems that regulate intracellular Na+/K+/H+ concentration",
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
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "intracellular_k_accumulation",
        "predicate": "contributes to",
        "object": "osmotic_balance",
        "description": (
            "Intracellular KCl accumulation is a salt-in osmoadaptation route "
            "that contributes to balancing external salt."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2013.00315",
                "snippet": (
                    "Extremely halophilic microorganisms that accumulate KCl "
                    "for osmotic balance"
                ),
                "notes": (
                    "Verified against the open Oren minireview; the connector "
                    "links KCl accumulation to osmotic balance without making "
                    "the salt-in strategy universal for every NaCl optimum."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "salt_in_strategy",
        "predicate": "associated with",
        "object": "acidic_proteome",
        "description": (
            "Salt-in osmoadaptation is associated with proteome-scale acidic "
            "adaptation for molar intracellular KCl."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2013.00315",
                "snippet": "have a large excess of acidic amino acids in their proteins",
                "notes": (
                    "Verified against the open Oren minireview; the connector "
                    "keeps acidic-proteome composition scoped to salt-in "
                    "strategists."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "compatible_solute_uptake",
        "predicate": "associated with",
        "object": "compatible_solute_accumulation",
        "description": (
            "External compatible-solute uptake is associated with the salt-out "
            "branch that accumulates organic osmolytes for osmoadaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2022.846677",
                "snippet": (
                    "Uptake of ectoine from the medium is facilitated by the "
                    "osmoregulated TRAP transporter TeaABC"
                ),
                "notes": (
                    "Verified against the open Halomonas elongata review; the "
                    "connector treats uptake as an accumulation branch with a "
                    "lower energetic cost than de novo synthesis."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cellular_ion_homeostasis",
        "predicate": "associated with",
        "object": "osmotic_balance",
        "description": (
            "Na+/K+/H+ transporter control of cellular ion homeostasis is "
            "associated with osmotic balancing during salinity change."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/aem.00145-24",
                "snippet": "ensuring cellular ion homeostasis under varying salinities",
                "notes": (
                    "Verified against the Xing et al. long-term salinity-stress "
                    "study; the connector places the species-specific "
                    "transporter response inside the osmotic-balance context."
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
            "by adding 4 source- and verbatim-snippet-backed connectors among the "
            "salt-in KCl, acidic proteome, compatible-solute uptake, cation "
            "homeostasis, and osmotic-balance branches. No paid research service "
            "was called."
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
