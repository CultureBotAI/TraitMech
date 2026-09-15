#!/usr/bin/env python3
"""Normalize exact homeoviscous causal-node labels before grounding."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

CURATOR = "codex"
TIMESTAMP = "2026-09-15T07:02:39Z"
TARGETS = {
    REPO_ROOT / "data" / "traits" / "environment" / "temperature_delta_low.yaml": {
        "identifier": "METPO:1000484",
        "graph_id": "temperature_delta_low_limited_breadth",
        "node_id": "homeoviscous_adaptation",
        "old_label": "homeoviscous adaptation / restored fluidity",
        "new_label": "homeoviscous adaptation",
    },
    REPO_ROOT / "data" / "traits" / "environment" / "temperature_delta_mid2.yaml": {
        "identifier": "METPO:1000486",
        "graph_id": "temperature_delta_mid2_broad_breadth",
        "node_id": "membrane_fluidity",
        "old_label": "membrane fluidity / homeoviscous adaptation",
        "new_label": "membrane fluidity",
        "grounding": "METPO:1007505",
    },
}


def update_doc(doc: dict, *, spec: dict) -> dict:
    if doc.get("identifier") != spec["identifier"]:
        raise ValueError(f"unexpected identifier: {doc.get('identifier')!r}")

    graphs = {
        graph.get("graph_id"): graph
        for graph in doc.get("causal_graphs", [])
    }
    graph = graphs.get(spec["graph_id"])
    if graph is None:
        raise ValueError(f"missing graph {spec['graph_id']}")

    nodes = {
        node.get("node_id"): node
        for node in graph.get("nodes", [])
    }
    node = nodes.get(spec["node_id"])
    if node is None:
        raise ValueError(f"missing node {spec['node_id']}")
    if node.get("label") != spec["old_label"]:
        raise ValueError(
            f"{spec['node_id']} label is {node.get('label')!r}, "
            f"expected {spec['old_label']!r}"
        )

    updated = copy.deepcopy(doc)
    for graph in updated["causal_graphs"]:
        if graph["graph_id"] != spec["graph_id"]:
            continue
        for node in graph["nodes"]:
            if node["node_id"] != spec["node_id"]:
                continue
            node["label"] = spec["new_label"]
            if "grounding" in spec:
                if node.get("grounding") and node["grounding"] != spec["grounding"]:
                    raise ValueError(
                        f"{spec['node_id']} has unexpected grounding "
                        f"{node['grounding']!r}"
                    )
                node["grounding"] = spec["grounding"]

    record_curation_event(
        updated,
        curator=CURATOR,
        action="NORMALIZED_CAUSAL_NODE_LABELS",
        changes=(
            "Normalized the homeoviscous-adaptation causal-node label before "
            "grounding it through proposals/metpo_traitmech_v85."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    for path, spec in TARGETS.items():
        doc = yaml.safe_load(path.read_text())
        updated = update_doc(doc, spec=spec)
        rel = path.relative_to(REPO_ROOT)
        if args.apply:
            write_validated_trait(updated, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
