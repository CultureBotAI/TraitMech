#!/usr/bin/env python3
"""Structural-integrity audit for TraitMech causal graphs.

LinkML/`validate-strict` check field *types*, but not graph *connectivity*.
This audit walks every ``data/traits/**/*.yaml`` causal graph and flags
structural defects the schema cannot catch:

  DANGLING_EDGE           an edge whose ``subject`` or ``object`` is not a
                          declared ``node_id`` in the same graph (a typo or a
                          deleted node).                            [ERROR]
  ORPHAN_NODE             a declared node that no edge references (a fully
                          disconnected node).                       [ERROR]
  NO_TRAIT_NODE           a graph with no ``node_type: TRAIT`` node, so there
                          is nothing to anchor reachability to.     [ERROR]
  UNREACHABLE_FROM_TRAIT  a node that IS referenced by some edge, but sits in
                          an island with no undirected path back to any TRAIT
                          node. The graph is several disjoint fragments rather
                          than one mechanism.                        [WARN]

Why UNREACHABLE_FROM_TRAIT is needed: ORPHAN_NODE catches a node with *zero*
edges, but says nothing about a well-connected cluster that never reaches the
trait. A graph can be four separate islands and still be "clean" under the
original two checks. That is the common failure mode of bulk enrichment
passes, which append a cluster of new nodes and edges without wiring them
into the existing cascade.

Reachability is deliberately **undirected**. Curated predicates mix directions
(``cellulase -enables-> trait`` but ``trait -produces-> glucose``), so a
directed walk would flag correctly-modelled graphs. The question here is
"is this one graph or several?", not "does causality flow one way?".

Because a large fraction of the corpus currently has at least one unreachable
node, a blocking check would be un-landable as-is. Use ``--write-baseline`` to
freeze the known set and ratchet: pre-existing fragmentation stays a warning,
while any *new* unreachable node fails the build.

Writes ``reports/causal_graph_audit.tsv``. Exit code is governed by
``--fail-on``:

  new    (default) any finding NOT in the baseline fails. Baselined findings
         never fail regardless of severity. This is the ratchet: the corpus
         cannot get more fragmented than it is today, but today's 1314
         findings do not block.
  error  only new ERROR-severity findings fail. New fragmentation is still
         reported, but non-blocking — use if the ratchet proves too noisy.
  any    every finding fails and the baseline is ignored. Use once the
         backlog has been burned down.

Note that severity governs *reporting* and the ``error`` mode; under the
default ``new`` mode a WARN-severity regression blocks just like an ERROR,
because the point is to prevent backsliding.

Usage:
    python scripts/audit_causal_graphs.py
    python scripts/audit_causal_graphs.py --out reports/causal_graph_audit.tsv
    python scripts/audit_causal_graphs.py --write-baseline   # freeze today
    python scripts/audit_causal_graphs.py --fail-on any      # once burned down
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict, deque
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
DEFAULT_OUT = REPO_ROOT / "reports" / "causal_graph_audit.tsv"
DEFAULT_BASELINE = REPO_ROOT / "conf" / "causal_graph_audit_baseline.tsv"

ERROR = "ERROR"
WARN = "WARN"

# Severity per defect. Promote UNREACHABLE_FROM_TRAIT to ERROR once the
# backlog is burned down (or just run with --fail-on any).
SEVERITY = {
    "DANGLING_EDGE": ERROR,
    "ORPHAN_NODE": ERROR,
    "NO_TRAIT_NODE": ERROR,
    "UNREACHABLE_FROM_TRAIT": WARN,
}

FIELDNAMES = ["file", "graph_id", "defect", "severity", "detail"]


def _reachable(seeds: list[str], adjacency: dict[str, set[str]]) -> set[str]:
    """Undirected breadth-first closure from ``seeds``."""
    seen: set[str] = set()
    queue = deque(seeds)
    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        queue.extend(adjacency[node] - seen)
    return seen


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
            nodes = graph.get("nodes") or []
            node_set = {n.get("node_id") for n in nodes}
            referenced: set = set()
            adjacency: dict[str, set[str]] = defaultdict(set)

            for e in (graph.get("edges") or []):
                subj, obj = e.get("subject"), e.get("object")
                for end, ref in (("subject", subj), ("object", obj)):
                    referenced.add(ref)
                    if ref not in node_set:
                        findings.append({
                            "file": rel, "graph_id": gid, "defect": "DANGLING_EDGE",
                            "severity": SEVERITY["DANGLING_EDGE"],
                            "detail": f"{end}={ref!r} ({subj} -[{e.get('predicate')}]-> {obj})",
                        })
                # Only wire up edges whose ends both exist, so a dangling edge
                # cannot fabricate reachability through a phantom node.
                if subj in node_set and obj in node_set:
                    adjacency[subj].add(obj)
                    adjacency[obj].add(subj)

            for n in nodes:
                if n.get("node_id") not in referenced:
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "ORPHAN_NODE",
                        "severity": SEVERITY["ORPHAN_NODE"],
                        "detail": f"node_id={n.get('node_id')!r} label={n.get('label')!r} type={n.get('node_type')}",
                    })

            if not nodes:
                continue

            trait_nodes = [n.get("node_id") for n in nodes
                           if n.get("node_type") == "TRAIT"]
            if not trait_nodes:
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "NO_TRAIT_NODE",
                    "severity": SEVERITY["NO_TRAIT_NODE"],
                    "detail": f"{len(nodes)} node(s), no node_type: TRAIT to anchor reachability",
                })
                continue

            reached = _reachable(trait_nodes, adjacency)
            for n in nodes:
                nid = n.get("node_id")
                # ORPHAN_NODE already covers zero-edge nodes; don't double-report.
                if nid in reached or nid not in referenced:
                    continue
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "UNREACHABLE_FROM_TRAIT",
                    "severity": SEVERITY["UNREACHABLE_FROM_TRAIT"],
                    "detail": (f"node_id={nid!r} label={n.get('label')!r} "
                               f"type={n.get('node_type')} — in an island with no path to "
                               f"{'/'.join(trait_nodes)}"),
                })
    return findings


def _key(row: dict[str, str]) -> tuple[str, str, str, str]:
    """Baseline identity: (file, graph, defect, discriminator).

    The discriminator is the leading fragment of ``detail`` — ``node_id=...``
    for node-shaped findings, ``subject=...``/``object=...`` for edge-shaped
    ones. Taking only the leading fragment means editing a still-broken node's
    *label* does not silently un-suppress it, while keeping distinct nodes and
    distinct dangling edges on distinct keys. Falling back to "" here would
    collapse every DANGLING_EDGE in a graph onto one key, so baselining one
    would suppress the rest.
    """
    detail = row.get("detail", "")
    node = detail.split(" ", 1)[0] if detail else ""
    return (row["file"], row["graph_id"], row["defect"], node)


def partition(
    findings: list[dict[str, str]],
    baseline: set[tuple[str, str, str, str]],
    fail_on: str,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Split ``findings`` into (not-in-baseline, blocking) for a ``--fail-on``.

    Kept separate from ``main`` so the exit-code contract is unit-testable: a
    regression here silently disarms the gate, which is exactly how the first
    cut of this check shipped without actually ratcheting.
    """
    new = [r for r in findings if _key(r) not in baseline]
    if fail_on == "any":
        # Strictest: ignore the baseline entirely. Use once the backlog is gone.
        blocking = list(findings)
    elif fail_on == "error":
        blocking = [r for r in new if r["severity"] == ERROR]
    else:  # "new" — the ratchet: never regress past the frozen baseline.
        blocking = list(new)
    return new, blocking


def load_baseline(path: Path) -> set[tuple[str, str, str, str]]:
    if not path.exists():
        return set()
    with path.open(newline="") as f:
        return {_key(r) for r in csv.DictReader(f, delimiter="\t")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="TSV of known findings to suppress from the exit code.")
    ap.add_argument("--no-baseline", action="store_true",
                    help="Ignore the baseline file; report everything.")
    ap.add_argument("--write-baseline", action="store_true",
                    help="Freeze current WARN findings into --baseline and exit 0. "
                         "Refuses if any ERROR-severity finding exists.")
    ap.add_argument("--fail-on", choices=["new", "error", "any"], default="new",
                    help="new (default): any finding not in the baseline fails — a "
                         "true ratchet. error: only new ERROR-severity findings fail, "
                         "so new fragmentation is reported but non-blocking. "
                         "any: every finding fails, baseline ignored (post-burndown).")
    args = ap.parse_args()

    findings = audit(args.traits_dir)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(findings)

    if args.write_baseline:
        # The baseline parks the known WARN backlog so the check can run
        # non-blocking. It is NOT a suppression channel for structural errors:
        # freezing an ERROR here would keep the gate green forever after.
        errors = [r for r in findings if r["severity"] == ERROR]
        if errors:
            print(f"Refusing to write baseline: {len(errors)} ERROR-severity "
                  f"finding(s) present. Fix these first — the baseline is for "
                  f"the WARN backlog only.", file=sys.stderr)
            for r in errors[:20]:
                print(f"  {r['defect']}  {r['file']} [{r['graph_id']}]  "
                      f"{r['detail']}", file=sys.stderr)
            return 1
        warns = [r for r in findings if r["severity"] != ERROR]
        args.baseline.parent.mkdir(parents=True, exist_ok=True)
        with args.baseline.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                               lineterminator="\n")
            w.writeheader()
            w.writerows(warns)
        print(f"Wrote baseline: {args.baseline} ({len(warns)} finding(s))",
              file=sys.stderr)
        return 0

    baseline = set() if args.no_baseline else load_baseline(args.baseline)
    new, blocking = partition(findings, baseline, args.fail_on)

    by_defect: dict[str, int] = {}
    for r in findings:
        by_defect[r["defect"]] = by_defect.get(r["defect"], 0) + 1
    print("=== causal-graph structural audit ===", file=sys.stderr)
    print(f"  findings: {len(findings)}"
          f"  (baselined: {len(findings) - len(new)}, new: {len(new)},"
          f" blocking: {len(blocking)})", file=sys.stderr)
    for d, n in sorted(by_defect.items()):
        print(f"    {d:<22} {n:>5}  [{SEVERITY.get(d, WARN)}]", file=sys.stderr)
    print(f"  TSV: {args.out}", file=sys.stderr)
    for r in (blocking or new)[:20]:
        print(f"  {r['severity']}  {r['defect']}  {r['file']} [{r['graph_id']}]"
              f"  {r['detail']}", file=sys.stderr)
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
