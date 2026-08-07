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
  FRAGMENTED_GRAPH        a graph that splits into several disconnected
                          components. Catches what UNREACHABLE_FROM_TRAIT cannot:
                          a split where each side happens to contain a node typed
                          TRAIT, so every node reaches *a* trait but not the one
                          the record is about (#220).
  DUPLICATE_GROUNDING     two nodes in one graph carrying the same ``grounding``.
                          The machine-readable signature of one concept modelled
                          twice — #351 grounded `growth_external_ph_5_5_9` to the
                          same METPO CURIE its own record's trait node already
                          had, which made the duplication legible but which
                          nothing detected (#352).            [WARN]
  DISPOSITION_MISTYPED    a CAPACITY or STATE node whose own description reads as
                          a disposition — "capacity to", "ability to",
                          "tolerance of". Those describe what an organism CAN do,
                          i.e. a TRAIT. Three separate defects this session were
                          a mis-typed node rather than a wrong predicate (#328,
                          #330, #331), and #334 retyped six on exactly this
                          evidence; the ones left behind survived only because
                          their in-edges happened not to violate a range, which
                          is an unrelated fact (#352).         [WARN]
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
         cannot get more fragmented than it is today, but today's 1541
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
import re
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
    "DUPLICATE_GROUNDING": WARN,
    "DISPOSITION_MISTYPED": WARN,
    "DANGLING_EDGE": ERROR,
    "ORPHAN_NODE": ERROR,
    "NO_TRAIT_NODE": ERROR,
    "UNREACHABLE_FROM_TRAIT": WARN,
    "FRAGMENTED_GRAPH": WARN,
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


def _components(node_set: set[str], adjacency: dict[str, set[str]]) -> list[set[str]]:
    """Undirected connected components, largest first.

    Anchor-free by design — it asks "is this one graph?" without needing to know
    which node the record is about, which is what makes it immune to the two
    ways UNREACHABLE_FROM_TRAIT can be fooled (several TRAIT nodes, or a trait
    node whose id does not follow the `<slug>_trait` convention).
    """
    seen: set[str] = set()
    out: list[set[str]] = []
    for node in sorted(n for n in node_set if n is not None):
        if node in seen:
            continue
        component = _reachable([node], adjacency)
        seen |= component
        out.append(component)
    return sorted(out, key=len, reverse=True)


# "capacity of a cell to", "ability to", "tolerance of" -- deliberately anchored
# on the phrasing a curator writes, not on the label, because the label is often
# just the concept name ("buoyancy") while the description is where the
# disposition shows.
_DISPOSITION_RE = re.compile(
    r"\b(capacit(?:y|ies)\b[^.]{0,30}?\bto|ability to|able to|tolerance (?:of|to))\b",
    re.IGNORECASE)


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

            # UNREACHABLE_FROM_TRAIT anchors on ANY node typed TRAIT, and that is
            # correct: 85 of 353 graphs legitimately carry more than one, because
            # a record links its parent and child traits as nodes
            # (`bsl1_trait` + `biosafety_level`, `nacl_delta_high_trait` +
            # `nacl_delta`). But it means a graph splitting into components that
            # EACH contain a TRAIT node reports clean — every node reaches *a*
            # trait, just not the one the record is about (#220).
            #
            # Anchoring on the record's own trait node instead was the obvious
            # alternative and does not work: `<slug>_trait` holds for 297 graphs
            # and not for the other 56, which use abbreviated ids
            # (`bsl1_trait` for biosafety_level_1, `predatory_trait` for
            # predatory_bacterium). Counting components needs no anchor at all,
            # so it cannot be fooled by either naming or typing.
            # Computed over edge-referenced nodes only. A zero-edge node is its
            # own component, but ORPHAN_NODE already reports it as an ERROR with
            # a clearer remedy — counting it here would raise a second finding
            # for one defect, which is the same reason UNREACHABLE_FROM_TRAIT
            # skips unreferenced nodes above.
            # Two nodes with the same grounding are one concept modelled twice.
            by_grounding: dict[str, list[str]] = defaultdict(list)
            for n in nodes:
                g = (n.get("grounding") or "").strip()
                if g:
                    by_grounding[g].append(n.get("node_id"))
            for g, ids in sorted(by_grounding.items()):
                if len(ids) > 1:
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "DUPLICATE_GROUNDING",
                        "severity": SEVERITY["DUPLICATE_GROUNDING"],
                        "detail": (f"grounding={g} on {len(ids)} nodes: "
                                   f"{', '.join(sorted(i for i in ids if i))}"),
                    })

            for n in nodes:
                if n.get("node_type") not in ("CAPACITY", "STATE"):
                    continue
                blob = f"{n.get('label') or ''} {n.get('description') or ''}"
                if _DISPOSITION_RE.search(blob):
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "DISPOSITION_MISTYPED",
                        "severity": SEVERITY["DISPOSITION_MISTYPED"],
                        "detail": (f"node_id={n.get('node_id')!r} "
                                   f"type={n.get('node_type')} — description reads as a "
                                   f"disposition, which is a TRAIT"),
                    })

            components = _components(node_set & referenced, adjacency)
            if len(components) > 1:
                sizes = ", ".join(str(len(c)) for c in components)
                # Detail MUST lead with the component count, because `_key` takes
                # the leading whitespace-delimited token as the baseline
                # discriminator. Leading with the node count instead made the
                # ratchet fail open in both directions on the 220 graphs this
                # baselines: 3 components -> 4 keeps the node count, so real
                # backsliding stayed suppressed; while adding a node inside an
                # already-connected component changed the key and blocked a PR
                # whose fragmentation was unchanged — the ordinary shape of
                # #183's backfill. This is the first WARN-severity whole-graph
                # defect, so it is the first time the discriminator has had to be
                # anything but a node_id.
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "FRAGMENTED_GRAPH",
                    "severity": SEVERITY["FRAGMENTED_GRAPH"],
                    "detail": (f"components={len(components)} of {len(nodes)} node(s) "
                               f"(sizes: {sizes}) — one record, several unrelated "
                               "mechanisms"),
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
