#!/usr/bin/env python3
"""Connect gas-vesicle and heterocyst mechanistic graphs for issue #183.

Every connector passage was checked against openly available source text. The
isolated FurC promoter branch is removed because its own primary source says the
direction of FurC regulation of hetR expression remains unresolved.

Usage:
    python scripts/connect_gas_heterocyst_graphs_183.py
    python scripts/connect_gas_heterocyst_graphs_183.py --apply
"""

from __future__ import annotations

import argparse
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

TIMESTAMP = "2026-08-31T06:30:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

EXPECTED_COMPONENTS = {
    "morphology/gas_vesicle": 5,
    "morphology/heterocyst": 4,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "morphology/gas_vesicle": [
        {
            "subject": "gas_vesicle_shell",
            "predicate": "part of",
            "object": "gas_vesicle_trait",
            "description": (
                "The gas-filled compartment and its protein shell constitute the "
                "gas-vesicle structure."
            ),
            "evidence": [{
                "reference": "DOI:10.1186/s13036-024-00426-3",
                "snippet": (
                    "The gas vesicle (GV) is like a hollow nanoparticle consisting "
                    "of an internal gas and a protein shell"
                ),
                "notes": (
                    "Verified against the open article abstract; the edge represents "
                    "structural composition, not a functional consequence."
                ),
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "gas_vesicle_collapse",
            "predicate": "negatively regulates",
            "object": "gas_vesicle_trait",
            "description": (
                "Irreversible pressure collapse eliminates the intact gas-vesicle "
                "structural state."
            ),
            "evidence": [{
                "reference": "DOI:10.1186/s13036-024-00426-3",
                "snippet": (
                    "when GVs are under pressure, there is a critical point at which "
                    "the GV irreversibly collapses"
                ),
                "notes": "Verified against the open full text's physical-properties section.",
            }],
            "predicate_id": "RO:0002212",
        },
        {
            "subject": "gvpd_protein",
            "predicate": "negatively regulates",
            "object": "gas_vesicle_trait",
            "description": (
                "GvpD inhibits formation of the gas-vesicle structure under the "
                "reviewed regulatory model."
            ),
            "evidence": [{
                "reference": "DOI:10.1186/s13036-024-00426-3",
                "snippet": "GvpD has an inhibitory effect on GV formation",
                "notes": (
                    "Verified against the open full text; this connects the existing "
                    "formation-regulation module without asserting a universal mechanism."
                ),
            }],
            "predicate_id": "RO:0002212",
        },
        {
            "subject": "hydrophobic_inner_surface",
            "predicate": "part of",
            "object": "gas_vesicle_shell",
            "description": (
                "The hydrophobic luminal face is the inner surface of the gas-vesicle "
                "protein shell."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s44318-024-00178-2",
                "snippet": (
                    "GVs maintain an inner gas compartment by having a hydrophobic "
                    "inner surface"
                ),
                "notes": (
                    "Verified against the open full text; the same passage explains "
                    "how this surface prevents liquid-water condensation."
                ),
            }],
            "predicate_id": "biolink:part_of",
        },
    ],
    "morphology/heterocyst": [
        {
            "subject": "hetr_regulator",
            "predicate": "contributes to",
            "object": "heterocyst_trait",
            "description": (
                "HetR is the central positive regulator of heterocyst development "
                "and contributes to realization of the differentiated cell trait."
            ),
            "evidence": [{
                "reference": "DOI:10.1371/journal.pone.0289761",
                "snippet": "hetR, the master regulator of heterocyst development",
                "notes": (
                    "The source supports the central regulatory role; the edge does "
                    "not claim that HetR alone is sufficient for differentiation."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "glycolipid_layer",
            "predicate": "part of",
            "object": "het_envelope",
            "description": (
                "The oxygen-limiting heterocyst glycolipid layer is the inner layer "
                "of the specialized heterocyst envelope."
            ),
            "evidence": [{
                "reference": "DOI:10.1101/2023.10.04.560878",
                "snippet": "the inner heterocyst-specific glycolipid layer (HGL)",
                "notes": (
                    "The contiguous source phrase directly identifies the layer's "
                    "position in the heterocyst envelope."
                ),
            }],
            "predicate_id": "biolink:part_of",
        },
    ],
}

REMOVALS = {
    "morphology/heterocyst": {
        "nodes": {"furc_perr", "hetr_promoter"},
        "edges": {("furc_perr", "binds promoter of", "hetr_promoter")},
        "reason": (
            "Removed the isolated FurC/hetR-promoter branch: its primary source "
            "states that more studies are required to understand the regulation "
            "exerted by FurC on hetR expression (DOI:10.1371/journal.pone.0289761), "
            "so no directional bridge was asserted."
        ),
    },
}


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    removal = REMOVALS.get(slug)
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    expected_by_key = {_edge_key(edge): edge for edge in additions}
    present = set(existing_by_key) & set(expected_by_key)
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    removed = bool(removal) and not (removal["nodes"] & node_ids)

    before = _components(graph)
    if before == 1:
        if present != set(expected_by_key) or (removal and not removed):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        for key, expected in expected_by_key.items():
            if existing_by_key[key] != expected:
                raise ValueError(f"{slug}: connector drifted after migration: {key}")
        return False
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(
            f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}"
        )
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")

    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{slug}: connector lacks source/snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)

    if removal:
        edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
        if not removal["nodes"] <= node_ids or not removal["edges"] <= edge_keys:
            raise ValueError(f"{slug}: removal target drifted")
        graph["edges"] = [
            edge for edge in graph["edges"] if _edge_key(edge) not in removal["edges"]
        ]
        graph["nodes"] = [
            node for node in graph["nodes"] if node["node_id"] not in removal["nodes"]
        ]

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{slug}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            f"using {len(additions)} source- and verbatim-snippet-backed connector(s). "
            + (f"{removal['reason']} " if removal else "")
            + "No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    for slug in sorted(ADDITIONS):
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not transform(slug, doc):
            continue
        changed += 1
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
