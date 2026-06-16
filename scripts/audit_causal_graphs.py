#!/usr/bin/env python3
"""Structural-integrity audit for TraitMech causal graphs.

LinkML/`validate-strict` check field *types*, but not graph *connectivity*.
This audit walks every ``data/traits/**/*.yaml`` causal graph and flags two
structural defects the schema cannot catch:

  DANGLING_EDGE  an edge whose ``subject`` or ``object`` is not a declared
                 ``node_id`` in the same graph (a typo or a deleted node).
  ORPHAN_NODE    a declared node that no edge references (a disconnected node —
                 usually a modelling gap, e.g. the trait node left unlinked).

Writes ``reports/causal_graph_audit.tsv`` and exits non-zero if any defect is
found, so it can gate CI alongside ``validate-strict`` / the other audits.

Usage:
    python scripts/audit_causal_graphs.py
    python scripts/audit_causal_graphs.py --out reports/causal_graph_audit.tsv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
DEFAULT_OUT = REPO_ROOT / "reports" / "causal_graph_audit.tsv"


def audit(traits_dir: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in sorted(traits_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        try:
            rel = str(path.relative_to(REPO_ROOT))
        except ValueError:
            rel = str(path)
        for graph in (doc.get("causal_graphs") or []):
            gid = graph.get("graph_id", "")
            node_ids = [n.get("node_id") for n in (graph.get("nodes") or [])]
            node_set = set(node_ids)
            referenced: set = set()
            for e in (graph.get("edges") or []):
                for end in ("subject", "object"):
                    ref = e.get(end)
                    referenced.add(ref)
                    if ref not in node_set:
                        findings.append({
                            "file": rel, "graph_id": gid, "defect": "DANGLING_EDGE",
                            "detail": f"{end}={ref!r} ({e.get('subject')} -[{e.get('predicate')}]-> {e.get('object')})",
                        })
            for n in (graph.get("nodes") or []):
                if n.get("node_id") not in referenced:
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "ORPHAN_NODE",
                        "detail": f"node_id={n.get('node_id')!r} label={n.get('label')!r} type={n.get('node_type')}",
                    })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    args = ap.parse_args()

    findings = audit(args.traits_dir)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "graph_id", "defect", "detail"],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(findings)

    by_defect: dict[str, int] = {}
    for r in findings:
        by_defect[r["defect"]] = by_defect.get(r["defect"], 0) + 1
    print("=== causal-graph structural audit ===", file=sys.stderr)
    print(f"  findings: {len(findings)}", file=sys.stderr)
    for d, n in sorted(by_defect.items()):
        print(f"    {d:<14} {n}", file=sys.stderr)
    print(f"  TSV: {args.out}", file=sys.stderr)
    for r in findings[:20]:
        print(f"  {r['defect']}  {r['file']} [{r['graph_id']}]  {r['detail']}", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
