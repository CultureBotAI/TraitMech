#!/usr/bin/env python3
"""Connect the temperature-range-mid4 contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_range_mid4_graph_183.py
    python scripts/connect_temperature_range_mid4_graph_183.py --apply
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

SLUG = "environment/temperature_range_mid4"
GRAPH_ID = "temperature_range_mid4_warm_mesophile"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T23:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-range-mid4 warm-mesophile range",
    "description": (
        "DOI-backed graph linking warm-mesophile adaptation to a temperature "
        "growth range of approximately 34\u201340 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-range-mid4 warm-mesophile context",
    "description": (
        "DOI-backed nonmechanistic graph connecting warm-mesophile "
        "growth-range context, Fab-mediated homeoviscous membrane "
        "adaptation, compensatory membrane-fluidity restoration, "
        "high-temperature protein damage, and RpoH-governed heat-shock "
        "protection branches."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "fab_branchpoint_valve",
        "predicate": "enables",
        "object": "homeoviscous_adaptation",
        "description": (
            "The FabI/FabB branchpoint valve reallocates flux between saturated "
            "and unsaturated fatty acid synthesis, enabling homeoviscous adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "allocates flux between the saturated and unsaturated",
                "notes": (
                    "Verified against the open Hoogerland et al. abstract; the E. "
                    "coli temperature-sensitive metabolic valve allocates fatty-acid "
                    "synthesis flux through FabI and FabB."
                ),
            }
        ],
        "predicate_id": "RO:0002327",
    },
    {
        "subject": "fab_c10_competition",
        "predicate": "regulates",
        "object": "saturated_unsaturated_membrane_lipid_composition",
        "description": (
            "Competition of FabA/FabI/FabB for the common C10:1 pool shifts "
            "flux between saturated and unsaturated fatty acids, changing "
            "saturated/unsaturated membrane lipid composition."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "compete for a common pool of substrates",
                "notes": (
                    "Verified against the open Hoogerland et al. Figure 1 legend; "
                    "FabA interconverts the C10:1 acyl-ACP substrates used by "
                    "FabI and FabB, making the enzymes indirectly compete for "
                    "one pool."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "membrane_fluidity_restoration",
        "predicate": "contributes to",
        "object": "growth_after_temperature_shock",
        "description": (
            "Valve plus transcriptional feedback restores optimal membrane fluidity "
            "within a single generation, contributing to growth after a temperature "
            "shock."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "restores optimal membrane fluidity within a single generation",
                "notes": (
                    "Verified against the open Hoogerland et al. abstract; the "
                    "measured E. coli fatty-acid and phospholipid pathway connects "
                    "membrane-fluidity restoration to recovery from temperature "
                    "shock."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "heat_stress",
        "predicate": "causes",
        "object": "protein_unfolding_aggregation",
        "description": "High temperatures cause protein unfolding and aggregation.",
        "evidence": [
            {
                "reference": "DOI:10.1186/s12864-023-09266-9",
                "snippet": "unfold or misfold proteins",
                "notes": (
                    "Verified against the open McGuire and Nano introduction; "
                    "the review context lists unfolding, misfolding, and "
                    "aggregation among the high-temperature cellular problems "
                    "near TMAX."
                ),
            }
        ],
        "predicate_id": "biolink:causes",
    },
    {
        "subject": "protein_unfolding_aggregation",
        "predicate": "contributes to",
        "object": "mesophile_growth_impairment",
        "description": (
            "Protein unfolding and aggregation contributes to mesophile growth "
            "impairment unless compensated."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1186/s12864-023-09266-9",
                "notes": (
                    "Verified against the open McGuire and Nano introduction; "
                    "the paper frames high-temperature RNA, protein, lipid, "
                    "and DNA effects as cellular problems near the maximum "
                    "growth temperature."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "heat_stress",
        "predicate": "positively regulates",
        "object": "membrane_fluidity",
        "description": (
            "High temperatures increase membrane fluidity, requiring compensatory adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1186/s12864-023-09266-9",
                "snippet": "cause increased membrane fluidity",
                "notes": (
                    "Verified against the open McGuire and Nano introduction; "
                    "increased membrane fluidity is listed as a "
                    "high-temperature effect on cells."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "compensatory_adaptation",
        "predicate": "regulates",
        "object": "membrane_fluidity",
        "description": (
            "Compensatory membrane adaptation regulates temperature-driven "
            "membrane-fluidity changes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "maintains cell membranes at a fixed viscosity level",
                "notes": (
                    "Verified against the open Hoogerland et al. introduction; "
                    "homeoviscous adaptation counteracts temperature by varying "
                    "unsaturated, branched-chain, or chain-length lipid features "
                    "to stabilize viscosity."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "rpoh_regulon",
        "predicate": "positively regulates",
        "object": "heat_shock_chaperone_systems",
        "description": (
            "The sigma-32/RpoH regulon positively regulates the "
            "DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03105-23",
                "snippet": "RpoH) that drives the expression",
                "notes": (
                    "Verified against the open Berdejo et al. introduction; "
                    "RpoH is described as the main governor of the Salmonella "
                    "Typhimurium heat-shock response and as driving protective "
                    "heat-shock-protein expression."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "heat_shock_chaperone_systems",
        "predicate": "enables",
        "object": "heat_stress_protection",
        "description": (
            "The DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems protect "
            "against heat stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03105-23",
                "snippet": "protective heat shock proteins",
                "notes": (
                    "Verified against the open Berdejo et al. introduction; "
                    "DnaK/DnaJ/GrpE and GroES/GroEL are named as molecular "
                    "chaperone systems in the protective heat-shock-protein "
                    "response."
                ),
            }
        ],
        "predicate_id": "RO:0002327",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "saturated_unsaturated_membrane_lipid_composition",
        "predicate": "associated with",
        "object": "homeoviscous_adaptation",
        "description": (
            "Fab-mediated saturated/unsaturated lipid composition is associated "
            "with homeoviscous adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "compete for a common pool of substrates",
                "notes": (
                    "Verified against the open Hoogerland et al. Figure 1 legend; "
                    "this connector keeps the FabA/FabI/FabB C10:1 branch as "
                    "membrane-lipid composition context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "homeoviscous_adaptation",
        "predicate": "associated with",
        "object": "membrane_fluidity_restoration",
        "description": (
            "Homeoviscous adaptation is associated with rapid membrane-fluidity "
            "restoration after temperature shock."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "restores optimal membrane fluidity within a single generation",
                "notes": (
                    "Verified against the open Hoogerland et al. abstract; this "
                    "connector keeps the Fab branchpoint valve as membrane-fluidity "
                    "restoration context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_fluidity_restoration",
        "predicate": "associated with",
        "object": "warm_mesophile_adaptation",
        "description": (
            "Rapid membrane-fluidity restoration is associated with "
            "warm-mesophile adaptation after temperature shock."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": "allocates flux between the saturated and unsaturated",
                "notes": (
                    "Verified against the open Hoogerland et al. abstract; this "
                    "connector keeps fatty-acid flux allocation as membrane "
                    "context for the broad warm-mesophile range bin."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "homeoviscous_adaptation",
        "description": (
            "Temperature-driven membrane fluidity is associated with the "
            "homeoviscous adaptation branch."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1186/s12864-023-09266-9",
                "snippet": "cause increased membrane fluidity",
                "notes": (
                    "Verified against the open McGuire and Nano introduction; "
                    "this connector keeps high-temperature membrane fluidity as "
                    "context for compensatory membrane adaptation."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "heat_stress_protection",
        "predicate": "associated with",
        "object": "protein_unfolding_aggregation",
        "description": (
            "RpoH-governed chaperone protection is associated with heat-induced "
            "protein unfolding and aggregation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/mbio.03105-23",
                "snippet": "protective heat shock proteins",
                "notes": (
                    "Verified against the open Berdejo et al. introduction; this "
                    "connector keeps DnaK/DnaJ/GrpE and GroES/GroEL as protective "
                    "heat-shock context."
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
            "connectors among Fab-mediated membrane adaptation, compensatory "
            "membrane-fluidity restoration, high-temperature protein damage, "
            "and RpoH heat-shock protection branches. No paid research service "
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
