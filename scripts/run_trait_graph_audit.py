#!/usr/bin/env python3
"""Batch Edison (deep-research) runner for the causal-graph completeness audit.

Enumerates every REVIEWED ``term_kind: CLASS`` trait that already carries a
causal graph, and runs ``scripts/research_trait.py`` (FutureHouse Falcon /
Edison) on each, capturing the literature mechanism into
``research/traits/<category>/<slug>-deep-research-falcon.md``. Those research
notes are the input to the completeness assessment (phase 2): does each
trait's existing causal graph capture the mechanism the literature describes?

Designed for a long, paid run:
  * RESUMABLE   — skips any trait whose research output already exists.
  * FAIL-SOFT   — one trait's failure is logged, the batch continues.
  * PACED       — optional --sleep between calls (rate-limit friendly).
  * MANIFEST    — appends status rows to reports/trait_graph_audit_manifest.tsv.

Requires ``EDISON_API_KEY`` (or ``FUTUREHOUSE_API_KEY``) in the environment for
a real run; ``--dry-run`` needs no key and just lists the planned calls.

Usage:
    python scripts/run_trait_graph_audit.py --dry-run
    python scripts/run_trait_graph_audit.py            # full run (paid)
    python scripts/run_trait_graph_audit.py --limit 8  # pilot batch
"""
from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
import time
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
MANIFEST = REPO_ROOT / "reports" / "trait_graph_audit_manifest.tsv"
PROVIDER = "falcon"


def target_traits() -> list[tuple[str, str, str]]:
    """Return (category, slug, label) for REVIEWED CLASS traits with a graph."""
    out: list[tuple[str, str, str]] = []
    for path in sorted(TRAITS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        if not isinstance(doc, dict):
            continue
        if doc.get("mapping_status") != "REVIEWED" or doc.get("term_kind") != "CLASS":
            continue
        if not (doc.get("causal_graphs") or []):
            continue
        out.append((path.parent.name, path.stem, doc.get("label", path.stem)))
    return out


def output_path(category: str, slug: str) -> Path:
    return RESEARCH_DIR / category / f"{slug}-deep-research-{PROVIDER}.md"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="cap number of NEW calls (0 = all)")
    ap.add_argument("--sleep", type=float, default=2.0, help="seconds between calls")
    ap.add_argument("--category", default="", help="restrict to one category")
    args = ap.parse_args()

    # The Edison platform credential is provisioned as EDISON_PLATFORM_API_KEY
    # (the name the edison_client SDK reads), but this harness's preflight and the
    # research_trait.py subprocess it spawns (which inherits this env) read
    # EDISON_API_KEY. Alias it so a run works regardless of which name is set —
    # mirrors research_trait.py:research_env().
    if not os.environ.get("EDISON_API_KEY") and os.environ.get("EDISON_PLATFORM_API_KEY"):
        os.environ["EDISON_API_KEY"] = os.environ["EDISON_PLATFORM_API_KEY"]

    if not args.dry_run and not (os.environ.get("EDISON_API_KEY") or os.environ.get("FUTUREHOUSE_API_KEY")):
        print("ERROR: EDISON_API_KEY / FUTUREHOUSE_API_KEY unset — set it or use --dry-run.", file=sys.stderr)
        return 2

    targets = target_traits()
    if args.category:
        targets = [t for t in targets if t[0] == args.category.lower()]
    pending = [(c, s, l) for c, s, l in targets if not output_path(c, s).exists()]
    done_already = len(targets) - len(pending)
    print(f"targets: {len(targets)}  already-researched: {done_already}  pending: {len(pending)}", file=sys.stderr)
    if args.limit:
        pending = pending[: args.limit]
        print(f"  (limited to {len(pending)} this run)", file=sys.stderr)

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    new = not MANIFEST.exists()
    mf = MANIFEST.open("a", newline="")
    w = csv.writer(mf, delimiter="\t", lineterminator="\n")
    if new:
        w.writerow(["category", "slug", "status", "output"])

    ok = fail = 0
    for i, (cat, slug, label) in enumerate(pending, 1):
        cmd = ["uv", "run", "python", "scripts/research_trait.py",
               "--provider", PROVIDER, "--category", cat, "--slug", slug]
        print(f"[{i}/{len(pending)}] {cat}/{slug}  ({label})", file=sys.stderr)
        if args.dry_run:
            print("   " + " ".join(cmd))
            continue
        try:
            subprocess.run(cmd, check=True, cwd=REPO_ROOT)
            w.writerow([cat, slug, "ok", str(output_path(cat, slug).relative_to(REPO_ROOT))]); mf.flush()
            ok += 1
        except subprocess.CalledProcessError as e:
            w.writerow([cat, slug, f"fail:{e.returncode}", ""]); mf.flush()
            fail += 1
            print(f"   FAILED ({e.returncode})", file=sys.stderr)
        if args.sleep:
            time.sleep(args.sleep)

    mf.close()
    print(f"\ndone: ok={ok} fail={fail} (skipped {done_already} already-researched)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
