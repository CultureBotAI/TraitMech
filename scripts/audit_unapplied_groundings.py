#!/usr/bin/env python3
"""Fail when a curated node grounding was never written into the trait records (#460).

`mappings/node_grounding.tsv` and `data/traits/**` can disagree, and nothing
noticed. A curator adds a `(label, node_type) -> CURIE` row, commits it, and the
row takes effect only when someone remembers to run
`scripts/ground_causal_nodes.py --apply`. Until then the mapping exists and the
node stays ungrounded.

## Why the existing gate does not catch this

`audit-derived-reports` checks that `reports/node_grounding_residual.tsv` is not
stale. That report answers **"which nodes have no mapping?"** — the complement
of the question that matters here. A node with a mapping that was never applied
is absent from the residual by construction, so the report is perfectly current
and the disagreement is invisible. Every gate stays green.

When this was written the count was 18, and the corpus was **internally
contradictory** rather than merely incomplete: `proton motive force` was
grounded to `METPO:1007500` in 18 causal nodes and left bare in 16 others, and
`salt-in strategy` grounded in 6 and bare in 1. Identical nodes disagreeing
about their own identity is the shape this gate exists to prevent.

## What is deliberately NOT counted

`ground_causal_nodes.py` declines a mapping when another node in the same graph
already carries that CURIE, because `audit-graphs` would then report
`DUPLICATE_GROUNDING` (#361). Those are correct refusals, not a backlog — this
audit asks the grounding script itself which nodes it *would* write, so the two
can never drift apart. Re-deriving the eligibility rule here would create a
second, subtly different definition of "applied".

    uv run python scripts/audit_unapplied_groundings.py
    just audit-unapplied-groundings
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# This gate delegates the actual work to ground_causal_nodes.py, so it opens
# neither of these itself — but its verdict depends on both, and a PR touching
# either can change the answer. Declared here so `audit-qc-paths` can derive the
# CI paths filter from them; without them this script contributes nothing to the
# read set and that audit correctly reports itself blind rather than satisfied.
MAPPING = REPO_ROOT / "mappings" / "node_grounding.tsv"
TRAITS_DIR = REPO_ROOT / "data" / "traits"
GROUNDER = REPO_ROOT / "scripts" / "ground_causal_nodes.py"

REMEDY = "uv run python scripts/ground_causal_nodes.py --apply"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--warn-only", action="store_true",
                    help="report the count without failing")
    args = ap.parse_args(argv)

    # Ask the grounding script what it would do. A dry run writes no YAML.
    # stderr is merged deliberately: ground_causal_nodes.py writes its summary
    # there, not to stdout. Reading stdout alone made this audit report a clean
    # "0 unapplied" no matter how many were pending — a gate that could never
    # fail. Caught by mutation-testing it rather than by reading it.
    proc = subprocess.run(
        [sys.executable, str(GROUNDER)],
        capture_output=True, text=True, cwd=REPO_ROOT)
    output = f"{proc.stdout}\n{proc.stderr}"
    if proc.returncode != 0:
        print("=== unapplied groundings ===")
        print("  ground_causal_nodes.py failed; cannot determine the backlog:")
        print("\n".join(f"    {ln}" for ln in output.splitlines()[-8:]))
        return 1

    pending = None
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("nodes grounded:"):
            pending = int(stripped.split(":", 1)[1].strip())
            break
    if pending is None:
        # Never assume zero from a line we failed to find: that is exactly how
        # this audit silently passed while a backlog of 18 sat in the corpus.
        print("=== unapplied groundings ===")
        print("  could not find the 'nodes grounded:' line in the grounding "
              "script's output — its format changed, so this gate is blind.")
        return 1

    print("=== unapplied groundings ===")
    print(f"  curated mappings not written into the trait records: {pending}")

    if not pending:
        print("  mappings and trait records agree")
        return 0

    detail = [ln for ln in output.splitlines()
              if ln.strip().startswith("METPO:") or ln.strip().startswith("GO:")]
    for d in detail[:10]:
        print(f"   {d.strip()}")
    print(f"\n{pending} node(s) have a curated entry in mappings/node_grounding.tsv "
          f"whose CURIE was never written into data/traits/.")
    print("The residual report does NOT cover this: it lists nodes with *no* "
          "mapping, so a mapping that was never applied is absent from it by "
          "construction and every other gate stays green (#460).")
    print(f"\nApply them and commit the result:\n  {REMEDY}")
    print("Then regenerate the derived artifacts (`just gen-pages`) and add a "
          "history record, since this edits trait records.")
    return 0 if args.warn_only else 1


if __name__ == "__main__":
    sys.exit(main())
