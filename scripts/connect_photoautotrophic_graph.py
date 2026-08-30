#!/usr/bin/env python3
"""Connect the photoautotrophic causal graph with tracked evidence (#183).

The record already contains four evidence-bearing graph components.  This
migration adds the three missing relations that join those components without
inventing new nodes or commissioning new research.

Usage:
    python scripts/connect_photoautotrophic_graph.py          # dry run
    python scripts/connect_photoautotrophic_graph.py --apply  # write
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET_PATH = Path("data/traits/physiology/photoautotrophic.yaml")
TARGET_IDENTIFIER = "METPO:1000656"
TARGET_GRAPH = "photoautotrophic_cyanobacterial_carbon_fixation"
TIMESTAMP = "2026-08-30T20:17:23Z"
CURATOR = "codex"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

NEW_EDGES: tuple[dict[str, Any], ...] = (
    {
        "subject": "light",
        "predicate": "enables",
        "object": "photosynthetic_electron_transport",
        "description": (
            "Captured light enables the high-energy electron transfer through "
            "the photosystems that constitutes photosynthetic electron transport."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1111/1751-7915.14519",
                "snippet": (
                    "Photosynthesis in cyanobacteria requires effective light "
                    "harvesting and the transfer of high-energy electrons through "
                    "two photosystems"
                ),
                "notes": (
                    "The review directly links light harvesting to electron "
                    "transfer through PSII and PSI in cyanobacterial photosynthesis."
                ),
            }
        ],
        "predicate_id": "RO:0002327",
    },
    {
        "subject": "carbon_concentrating_mechanism",
        "predicate": "includes",
        "object": "carboxysome",
        "description": (
            "The cyanobacterial carbon-concentrating mechanism includes the "
            "carboxysome microcompartment as a functional component."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1126/sciadv.adk7283",
                "snippet": (
                    "Proteinaceous microcompartments, called carboxysomes, play a "
                    "critical role in CCM function"
                ),
                "notes": (
                    "A primary structural and biochemical study identifies "
                    "carboxysomes as a critical component of cyanobacterial CCM "
                    "function."
                ),
            }
        ],
        "predicate_id": "biolink:has_part",
    },
    {
        "subject": "carboxysome",
        "predicate": "includes",
        "object": "rubisco",
        "description": "The carboxysome houses RuBisCO for concentrated CO2 fixation.",
        "evidence": [
            {
                "reference": "DOI:10.1126/sciadv.adk7283",
                "snippet": "carboxysomes that house CA and Rubisco",
                "notes": (
                    "The primary study explicitly places RuBisCO within the "
                    "carboxysome together with carbonic anhydrase."
                ),
            }
        ],
        "predicate_id": "biolink:has_part",
    },
)


def _edge_key(edge: dict[str, Any]) -> tuple[Any, Any, Any]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def transform(doc: dict[str, Any]) -> bool:
    """Add the exact three connecting edges; return false if already applied."""
    if doc.get("identifier") != TARGET_IDENTIFIER:
        raise ValueError(f"target identifier is not {TARGET_IDENTIFIER}")

    graphs = [
        graph
        for graph in doc.get("causal_graphs") or []
        if graph.get("graph_id") == TARGET_GRAPH
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected exactly one graph {TARGET_GRAPH}")
    graph = graphs[0]
    node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    required_nodes = {
        endpoint
        for edge in NEW_EDGES
        for endpoint in (edge["subject"], edge["object"])
    }
    missing_nodes = sorted(required_nodes - node_ids)
    if missing_nodes:
        raise ValueError(f"graph is missing required nodes: {missing_nodes}")

    edges = graph.setdefault("edges", [])
    by_key = {_edge_key(edge): edge for edge in edges}
    exact_present = [by_key.get(_edge_key(edge)) == edge for edge in NEW_EDGES]
    if all(exact_present):
        return False
    for new_edge, exact in zip(NEW_EDGES, exact_present, strict=True):
        key = _edge_key(new_edge)
        if key in by_key and not exact:
            raise ValueError(f"refusing to overwrite changed edge {key}")
    if any(exact_present):
        raise ValueError("only some connecting edges are present; refusing partial replay")

    edges.extend(dict(edge) for edge in NEW_EDGES)
    record_curation_event(
        doc,
        curator=CURATOR,
        action=ACTION,
        changes=(
            "Connected all four components of the oxygenic cyanobacterial "
            "photoautotrophy graph with three tracked, snippet-backed relations: "
            "light enables photosynthetic electron transport; the CCM includes "
            "the carboxysome; and the carboxysome includes RuBisCO. No new paid "
            "research was commissioned (#183, #426)."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    path = REPO_ROOT / TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    changed = transform(doc)
    if not changed:
        print("photoautotrophic graph is already connected; no change")
        return 0

    if write:
        write_validated_trait(doc, path)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            write_validated_trait(doc, Path(tmp) / TARGET_PATH.name)

    mode = "applied" if write else "dry run"
    print(f"{mode}: added 3 connecting edges to {TARGET_PATH}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write; default is dry run")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    sys.exit(main())
