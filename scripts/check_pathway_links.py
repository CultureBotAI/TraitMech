#!/usr/bin/env python3
"""Check every node-level pathway context link using the pinned local index."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from traitmech.validation.pathway_links import load_index, pathway_link_errors  # noqa: E402


def main() -> int:
    try:
        version, records = load_index(ROOT)
    except (OSError, ValueError, KeyError) as error:
        print(error, file=sys.stderr)
        return 1
    failures = []
    count = 0
    for path in sorted((ROOT / "data" / "traits").rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        count += sum(len(node.get("related_records") or [])
                     for graph in doc.get("causal_graphs") or []
                     for node in graph.get("nodes") or [])
        failures.extend(f"{path.relative_to(ROOT)}: {error}"
                        for error in pathway_link_errors(doc, version, records))
    for error in failures:
        print(error, file=sys.stderr)
    print(f"Checked {count} pathway context links at PathwayMech {version}")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
