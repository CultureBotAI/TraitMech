#!/usr/bin/env python3
"""Fail a PR that changes trait records and records no provenance (#325).

`history/README.md` describes a per-session record as the thing that captures
*which model, using which tool, changed what, why, and under which issue*. The
per-file ``curation_history:`` block captures what changed; it has no slot for
the model, the tool, or the issue, and because it hangs off an edit it cannot
record a session that changed **nothing** -- an ``AUDIT`` that checked a trait
and correctly found nothing wrong is invisible without a record here.

PRESENCE WAS ADVISORY UNTIL #325, on the reasoning that a hard gate "trains
people to route around it". The measurement disagreed. Of the 134 commits that
modified `data/traits/*.yaml`, **2** added a history record -- 1.5%. Nobody
routed around the gate, because there was no gate; the convention simply did not
happen. What did happen is that **275** trait records grew an issue number
hand-typed into a `changes` string, which is the same provenance in a form
nothing can query.

THE GATE IS ONLY REASONABLE BECAUSE THE GRANULARITY WAS FIXED FIRST. Read
literally, "one record per session per target" makes a 128-file migration owe 128
near-identical records, which would bury the three substantive hand-written
records the directory exists for -- destroying the signal in the name of
provenance. Blocking on that would have been a fair thing to route around. One
record per CHANGE costs one file per PR, and that is what this enforces.

WHAT THIS DELIBERATELY DOES NOT CHECK. That the record is *about* the change. A
record added for an unrelated reason satisfies it. Checking the correspondence
would mean parsing intent, and the cheap proxies (does `target.path` name a
changed file?) are wrong for the migration case, where the honest target is the
script rather than any of the records it edited. The gate against an empty record
is `validate-history`, which fails while the `--details` TODO placeholder is
unfilled -- so the cheapest way to game this one does not work.

The rule is kept out of the workflow YAML so it is testable without a repo, a
network, or a PR; ``main`` shells out to git and hands the file lists in.

Usage:
    just audit-history-records --base origin/main
    python scripts/audit_history_records.py --changed a.yaml --added b.yaml
"""
from __future__ import annotations

import argparse
import subprocess
import sys

TRAIT_GLOB = "data/traits/**/*.yaml"
HISTORY_GLOB = "history/**/*.yaml"


def missing_record(changed_traits: list[str], added_history: list[str]) -> bool:
    """True when trait records changed and no history record was added.

    ``added_history`` must be files ADDED, not merely modified: editing an
    existing record is explicitly not how corrections work here -- the README
    says records are written once and never edited, and a correction goes in a
    NEW record that references the old one. Counting modifications would accept
    exactly the thing the append-only design forbids.
    """
    return bool(changed_traits) and not added_history


def _git(args: list[str]) -> list[str]:
    proc = subprocess.run(["git", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"git {' '.join(args)} failed: {proc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    return [ln for ln in proc.stdout.splitlines() if ln.strip()]


def collect(base: str) -> tuple[list[str], list[str]]:
    """(changed trait records, added history records) for base...HEAD."""
    changed = _git(["diff", "--name-only", f"{base}...HEAD", "--", TRAIT_GLOB])
    added = _git(["diff", "--name-only", "--diff-filter=A", f"{base}...HEAD",
                  "--", HISTORY_GLOB])
    return changed, added


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", help="base ref to diff against, e.g. origin/main")
    ap.add_argument("--changed", nargs="*", default=None,
                    help="changed trait records, for testing offline")
    ap.add_argument("--added", nargs="*", default=None,
                    help="added history records, for testing offline")
    args = ap.parse_args()

    if args.changed is not None or args.added is not None:
        changed, added = list(args.changed or []), list(args.added or [])
    elif args.base:
        changed, added = collect(args.base)
    else:
        ap.error("pass --base, or --changed/--added")

    print("=== curation history ===", file=sys.stderr)
    print(f"  trait records changed: {len(changed)}", file=sys.stderr)
    print(f"  history records added: {len(added)}", file=sys.stderr)
    for f in added:
        print(f"    + {f}", file=sys.stderr)

    if missing_record(changed, added):
        print(
            "\nThis PR changes trait records and adds no history record (#325).\n"
            "Write ONE record for the whole change, not one per file. For a\n"
            "migration the honest target is the script that drove it:\n\n"
            "  just new-history --kind infrastructure \\\n"
            "      --path scripts/<the migration script>.py \\\n"
            "      --event EDIT --outcome changed \\\n"
            "      --summary '<what the change did>' \\\n"
            "      --model claude-opus-5 --agent-tool claude-code \\\n"
            "      --issue https://github.com/CultureBotAI/TraitMech/issues/<n> \\\n"
            "      --details '<how many records, which selection rule, how verified>'\n\n"
            "See history/README.md. The per-file curation_history: block does not\n"
            "cover this: it has no slot for the model, the tool, or the issue.",
            file=sys.stderr)
        return 1
    if changed:
        print("  provenance recorded for this change", file=sys.stderr)
    else:
        print("  no trait records changed; nothing to record", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
