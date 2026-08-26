#!/usr/bin/env python3
"""Backfill curation_history events for the protein-taxon review tranche (#517).

Commit f32b3168 ("Complete the protein-taxon exemplar tranche across the
corpus") changed 352 trait records but added a curation_history event to only
84 of them. The other 268 gained scope dispositions, reviewed-label-only
groundings, taxon-paired protein examples, regroundings, node/edge removals,
and citation changes with no per-record provenance, which the safe-mutation
contract in CLAUDE.md requires.

This one-shot migration compares each record with its state at the tranche's
parent commit (BASE), describes what the tranche actually changed in that
record, and appends one event carrying that description. Records that already
received a tranche event are left alone. The event is written through
``record_curation_event`` with a fixed timestamp and ``upsert=True`` so a re-run
refreshes the wording instead of appending a duplicate (#395), and every write
goes through ``write_validated_trait``.

Usage:
    python scripts/backfill_protein_taxon_events.py            # dry run (default)
    python scripts/backfill_protein_taxon_events.py --apply    # write
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"
# Parent of the tranche commit; the tranche is everything between it and the tree.
BASE = "70aef2c5"
TIMESTAMP = "2026-08-26T03:23:00Z"
CURATOR = "claude"
ACTION_EXAMPLES = "CURATE_PROTEIN_TAXON_EXAMPLE"
ACTION_REVIEW = "REVIEW_GRAPH_PROTEIN_TAXON"
MAX_IDS = 8


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=False
    )


def changed_trait_files() -> list[Path]:
    out = _git("diff", "--name-only", BASE, "--", "data/traits")
    if out.returncode != 0:
        raise SystemExit(f"git diff failed: {out.stderr.strip()}")
    return [REPO_ROOT / line for line in out.stdout.split() if line.endswith(".yaml")]


def base_doc(rel: str) -> dict[str, Any] | None:
    out = _git("show", f"{BASE}:{rel}")
    if out.returncode != 0:
        return None
    return yaml.safe_load(out.stdout) or {}


def _events(doc: dict[str, Any]) -> list[tuple[str, str, str]]:
    return [
        (str(e.get("timestamp")), str(e.get("curator")), str(e.get("action")))
        for e in doc.get("curation_history") or []
        if isinstance(e, dict)
    ]


def has_tranche_event(doc: dict[str, Any], base: dict[str, Any]) -> bool:
    """True when the tranche itself already left an event on this record."""
    new = set(_events(doc)) - set(_events(base))
    new.discard((TIMESTAMP, CURATOR, ACTION_EXAMPLES))
    new.discard((TIMESTAMP, CURATOR, ACTION_REVIEW))
    return bool(new)


def _ids(items: list[str]) -> str:
    shown = items[:MAX_IDS]
    extra = len(items) - len(shown)
    return ", ".join(shown) + (f" and {extra} more" if extra > 0 else "")


def _graphs(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(g.get("graph_id")): g
        for g in doc.get("causal_graphs") or []
        if isinstance(g, dict)
    }


def _nodes(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(n.get("node_id")): n
        for n in graph.get("nodes") or []
        if isinstance(n, dict)
    }


def _edge_keys(graph: dict[str, Any]) -> dict[tuple[str, str, str], set[str]]:
    keys: dict[tuple[str, str, str], set[str]] = {}
    for e in graph.get("edges") or []:
        if not isinstance(e, dict):
            continue
        key = (str(e.get("subject")), str(e.get("predicate")), str(e.get("object")))
        refs = {
            str(ev.get("reference"))
            for ev in e.get("evidence") or []
            if isinstance(ev, dict) and ev.get("reference")
        }
        keys[key] = refs
    return keys


def _examples(node: dict[str, Any]) -> dict[str, str]:
    return {
        str(ex.get("uniprot_id")): str(ex.get("taxon_id"))
        for ex in node.get("protein_examples") or []
        if isinstance(ex, dict)
    }


def describe(doc: dict[str, Any], base: dict[str, Any]) -> tuple[str, bool]:
    """Return (description of the tranche's changes, examples_added)."""
    parts: list[str] = []
    examples_added = False

    scopes: list[str] = []
    label_only: list[str] = []
    examples: list[str] = []
    regrounded: list[str] = []
    retyped: list[str] = []
    removed_nodes: list[str] = []
    added_nodes: list[str] = []
    removed_edges = 0
    added_edges = 0
    edge_refs_changed = 0

    base_graphs = _graphs(base)
    for gid, graph in _graphs(doc).items():
        bgraph = base_graphs.get(gid, {})
        scope = graph.get("scope_status")
        if scope and scope != bgraph.get("scope_status"):
            scopes.append(f"{gid}={scope}")
        nodes, bnodes = _nodes(graph), _nodes(bgraph)
        for nid, node in nodes.items():
            bnode = bnodes.get(nid)
            if bnode is None:
                added_nodes.append(nid)
            else:
                if node.get("node_type") != bnode.get("node_type"):
                    retyped.append(f"{nid}->{node.get('node_type')}")
                if node.get("grounding") != bnode.get("grounding"):
                    regrounded.append(
                        f"{nid}: {bnode.get('grounding') or 'none'}->"
                        f"{node.get('grounding') or 'none'}"
                    )
            if (
                node.get("grounding_status") == "REVIEWED_LABEL_ONLY"
                and (bnode or {}).get("grounding_status") != "REVIEWED_LABEL_ONLY"
            ):
                label_only.append(nid)
            for acc, taxon in _examples(node).items():
                if acc not in _examples(bnode or {}):
                    examples.append(f"{acc} on {nid} ({taxon})")
        removed_nodes.extend(sorted(set(bnodes) - set(nodes)))
        edges, bedges = _edge_keys(graph), _edge_keys(bgraph)
        removed_edges += len(set(bedges) - set(edges))
        added_edges += len(set(edges) - set(bedges))
        edge_refs_changed += sum(
            1 for key in set(edges) & set(bedges) if edges[key] != bedges[key]
        )
    removed_nodes.extend(sorted(set(base_graphs) - set(_graphs(doc))))

    canon = {
        str(ex.get("taxon_id")): str(ex.get("reference"))
        for ex in doc.get("canonical_examples") or []
        if isinstance(ex, dict)
    }
    bcanon = {
        str(ex.get("taxon_id")): str(ex.get("reference"))
        for ex in base.get("canonical_examples") or []
        if isinstance(ex, dict)
    }
    canon_added = sorted(set(canon) - set(bcanon))
    canon_removed = sorted(set(bcanon) - set(canon))
    canon_recited = sum(1 for t in set(canon) & set(bcanon) if canon[t] != bcanon[t])

    if scopes:
        parts.append("set graph scope " + _ids(scopes) + " with scope_notes")
    if label_only:
        parts.append(
            f"marked {len(label_only)} GENE_OR_PROTEIN node(s) REVIEWED_LABEL_ONLY "
            f"with grounding_notes ({_ids(label_only)})"
        )
    if examples:
        examples_added = True
        parts.append("added taxon-paired protein example(s) " + _ids(examples))
    if regrounded:
        parts.append(f"regrounded {len(regrounded)} node(s) ({_ids(regrounded)})")
    if retyped:
        parts.append(f"retyped {len(retyped)} node(s) ({_ids(retyped)})")
    if added_nodes or added_edges:
        parts.append(
            f"added {len(added_nodes)} node(s) and {added_edges} edge(s)"
            + (f" ({_ids(added_nodes)})" if added_nodes else "")
        )
    if removed_nodes or removed_edges:
        parts.append(
            f"removed {len(removed_nodes)} node(s) and {removed_edges} edge(s) "
            f"together with their evidence ({_ids(removed_nodes)})"
        )
    if canon_added:
        parts.append("added canonical example(s) " + _ids(canon_added))
    if canon_removed:
        parts.append("removed canonical example(s) " + _ids(canon_removed))
    if canon_recited or edge_refs_changed:
        parts.append(
            f"changed the citation on {canon_recited} canonical example(s) and the "
            f"evidence references on {edge_refs_changed} surviving edge(s) "
            "(scope questioned in review issue 520)"
        )
    return "; ".join(parts), examples_added


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="write (default: dry run)")
    ap.add_argument(
        "--only", metavar="SLUG", help="restrict to one record slug (canary before the batch)"
    )
    args = ap.parse_args()

    written = skipped = undescribed = 0
    for path in changed_trait_files():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.is_file() or (args.only and path.stem != args.only):
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        base = base_doc(rel)
        if base is None:
            print(f"  skip {rel}: not present at {BASE}", file=sys.stderr)
            skipped += 1
            continue
        if has_tranche_event(doc, base):
            skipped += 1
            continue
        description, examples_added = describe(doc, base)
        if not description:
            print(f"  WARN {rel}: changed but no describable difference", file=sys.stderr)
            undescribed += 1
            continue
        changes = (
            "Backfilled provenance (review issue 517) for the codex protein-taxon "
            "review tranche of 2026-08-24/25, which shipped without a per-record "
            f"event. In this record the tranche: {description}."
        )
        record_curation_event(
            doc,
            curator=CURATOR,
            action=ACTION_EXAMPLES if examples_added else ACTION_REVIEW,
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
            changes=changes,
        )
        print(f"  {rel}: {changes[:160]}...")
        if args.apply:
            write_validated_trait(doc, path)
        written += 1

    mode = "" if args.apply else " (dry run)"
    print(
        f"{written} record(s) backfilled{mode}; {skipped} already carried a tranche "
        f"event; {undescribed} changed without a describable difference",
        file=sys.stderr,
    )
    return int(undescribed > 0)


if __name__ == "__main__":
    sys.exit(main())
