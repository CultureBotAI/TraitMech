#!/usr/bin/env python3
"""Check every node-level pathway context link using the pinned local index."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
PIN_PATH = REPO_ROOT / "conf" / "pathwaymech_pin.yaml"
INDEX_PATH = REPO_ROOT / "conf" / "pathwaymech_index.json"
TRAIT_ROOT = REPO_ROOT / "data" / "traits"

from traitmech.validation.pathway_links import load_index, pathway_link_errors  # noqa: E402


def main() -> int:
    try:
        version, records = load_index(REPO_ROOT, pin_path=PIN_PATH, index_path=INDEX_PATH)
    except (OSError, ValueError, KeyError) as error:
        print(error, file=sys.stderr)
        return 1
    failures = []
    count = 0
    for path in sorted(TRAIT_ROOT.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        count += sum(len(node.get("related_records") or [])
                     for graph in doc.get("causal_graphs") or []
                     for node in graph.get("nodes") or [])
        failures.extend(f"{path.relative_to(REPO_ROOT)}: {error}"
                        for error in pathway_link_errors(doc, version, records))
    for error in failures:
        print(error, file=sys.stderr)
    print(f"Checked {count} pathway context links at PathwayMech {version}")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
