#!/usr/bin/env python3
"""Connect three two-component physiology graphs for issue #183."""

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

TIMESTAMP = "2026-08-31T09:35:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
EXPECTED_COMPONENTS = {
    "physiology/chemotaxis": 2,
    "physiology/dormancy": 2,
    "physiology/persister_cell_formation": 2,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "physiology/chemotaxis": [{
        "subject": "chemoreceptor_mcp",
        "predicate": "contributes to",
        "object": "chemotaxis_process",
        "description": (
            "Chemoreceptor arrays contribute ligand sensing and CheA control to "
            "the chemotaxis process."
        ),
        "evidence": [{
            "reference": "DOI:10.1016/j.tim.2022.10.007",
            "snippet": (
                "The chemoreceptor nanoarray complexes with the cytosolic histidine "
                "kinase chemotaxis protein A (CheA) and regulates its "
                "autophosphorylation based on chemoreceptor ligand occupancy"
            ),
            "notes": "Verified against the public PMC author manuscript.",
        }],
        "predicate_id": "RO:0002326",
    }],
    "physiology/dormancy": [{
        "subject": "ribosome_hibernation_factors",
        "predicate": "contributes to",
        "object": "dormancy_process",
        "description": (
            "Stress-induced ribosome hibernation contributes translational arrest "
            "to the dormancy process."
        ),
        "evidence": [{
            "reference": "DOI:10.3389/fmicb.2024.1386179",
            "snippet": (
                "environmental stress might govern the formation of 100S ribosomes, "
                "which were only detectable during periods of protein synthesis arrest"
            ),
            "notes": "Verified against the open Frontiers article full text.",
        }],
        "predicate_id": "RO:0002326",
    }],
    "physiology/persister_cell_formation": [{
        "subject": "antibiotic_resistance",
        "predicate": "is distinct from",
        "object": "persister_trait",
        "description": (
            "Genetic antibiotic resistance is explicitly distinct from the "
            "phenotypic persistence trait."
        ),
        "evidence": [{
            "reference": "DOI:10.1038/s41579-019-0196-3",
            "snippet": (
                "Resistance, tolerance and persistence are distinct responses to "
                "antibiotic treatment"
            ),
            "notes": (
                "Verified against the open consensus statement; this contrast edge "
                "does not treat resistance as a persistence mechanism."
            ),
        }],
    }],
}


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    existing = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    expected = {_edge_key(edge): edge for edge in additions}
    present = set(existing) & set(expected)
    before = _components(graph)
    if before == 1:
        if present != set(expected):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        for key, edge in expected.items():
            if existing[key] != edge:
                raise ValueError(f"{slug}: connector drifted after migration: {key}")
        return False
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}")
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if any(not item.get("reference") or not item.get("snippet") for item in evidence) or not evidence:
            raise ValueError(f"{slug}: connector lacks source/snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)
    if _components(graph) != 1:
        raise ValueError(f"{slug}: repair did not reach one component")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            "with one public-source, verbatim-snippet-backed connector. No paid "
            "research service was called."
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
        doc = yaml.safe_load(path.read_text()) or {}
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
