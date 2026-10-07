"""Offline validation of node-level links against a pinned PathwayMech index."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]


def load_index(root: Path = ROOT, *, pin_path: Path | None = None,
               index_path: Path | None = None) -> tuple[str, dict[str, dict]]:
    pin = yaml.safe_load((pin_path or root / "conf" / "pathwaymech_pin.yaml").read_text())
    content = (index_path or root / "conf" / "pathwaymech_index.json").read_bytes()
    if hashlib.sha256(content).hexdigest() != pin["sha256"]:
        raise ValueError("PathwayMech index differs from its pinned SHA-256")
    data = json.loads(content)
    if data.get("format") != "pathwaymech-pathway-index/1":
        raise ValueError("unsupported PathwayMech index format")
    rows = data["records"]
    records = {row["id"]: row for row in rows}
    if len(records) != len(rows):
        raise ValueError("duplicate PathwayMech record identifiers")
    return pin["commit"], records


def pathway_link_errors(doc: dict, version: str, records: dict[str, dict]) -> list[str]:
    errors = []
    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            seen = set()
            for link in node.get("related_records") or []:
                prefix = f"{graph['graph_id']}/{node['node_id']}"
                key = (link.get("corpus"), link.get("identifier"), link.get("relation"))
                if key in seen:
                    errors.append(f"{prefix}: duplicate pathway link")
                seen.add(key)
                if link.get("corpus") != "PathwayMech":
                    errors.append(f"{prefix}: unsupported corpus")
                if link.get("identifier") not in records:
                    errors.append(f"{prefix}: unknown PathwayMech record {link.get('identifier')}")
                if link.get("source_version") != version:
                    errors.append(f"{prefix}: source_version differs from the pinned index")
                if link.get("relation") != "PATHWAY_CONTEXT":
                    errors.append(f"{prefix}: unsupported pathway relation")
                basis = link.get("basis")
                if not isinstance(basis, str) or not basis.strip():
                    errors.append(f"{prefix}: missing correspondence basis")
    return errors
