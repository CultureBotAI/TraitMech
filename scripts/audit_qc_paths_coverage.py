#!/usr/bin/env python3
"""Fail when the `qc` chain reads a directory that qc.yaml's paths filter omits.

`.github/workflows/qc.yaml` carries the comment "A filter narrower than what the
job verifies is how #184 and #200 happened." #250 was the third recurrence, and
the fourth was live when this script was written: both ratchet baselines
(`conf/causal_graph_audit_baseline.tsv`, `conf/evidence_snippet_baseline.tsv`)
live under `conf/`, which the filter did not list — so weakening a baseline did
not re-run `qc` (#252).

Each recurrence was caught by review rather than CI, and each PR passed only
because it happened to touch a directory already in the filter. The comments help
someone already editing qc.yaml; they do not help the person who adds a target to
`qc` and never opens it, which is how all four happened.

HOW THE READ-SET IS DERIVED. #252 proposed having each recipe declare the
directories it reads. Inferring instead, because a declaration is one more thing
to forget in the same way:

  1. parse the `qc:` dependency chain out of the justfile;
  2. for each recipe, find the `scripts/*.py` it invokes;
  3. in each script, find `REPO_ROOT / "..."` path constants;
  4. reduce those to top-level entries and check each against the filter.

Deliberately coarse — top-level entries, not exact paths. `data/embeddings/**`
and `data/raw/metpo.owl` cover different parts of `data/`, and demanding an exact
match would mean flagging every recipe that touches `data/` at all. The failure
this guards is a directory missing ENTIRELY, which is what all four instances
were.

Known limitation, stated rather than hidden: a script reading a path built some
other way (an f-string, a config value, a helper in another module) is invisible
here. This narrows the gap; it does not close it.

Usage:
    just audit-qc-paths
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
JUSTFILE = REPO_ROOT / "justfile"
QC_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "qc.yaml"

# Read by the runner itself or by uv, not by a qc recipe, so their absence from
# the filter is not the bug this looks for.
IGNORED_TOPS = {"pyproject.toml", "uv.lock", ".github", ".venv"}

# The read-set from the last audit() call, so main() can print what was actually
# inferred. A gate that prints only "0 findings" cannot be told apart from one
# that inspected nothing (#286).
AUDIT_READ_SET: set[str] = set()


def qc_chain(justfile_text: str) -> list[str]:
    """Recipe names in the `qc:` dependency list."""
    match = re.search(r"^qc:(.*)$", justfile_text, re.M)
    return match.group(1).split() if match else []


def recipe_body(justfile_text: str, name: str) -> str:
    # The lookahead makes the name exact. Without it the pattern prefix-matches
    # and re.search takes the first hit in file order, so recipe_body("check")
    # returned check-biolink-coverage's body — harmless only because `check` is
    # not in the qc chain, and a fault the moment a recipe extends the name of
    # one that is (#287).
    match = re.search(rf"^{re.escape(name)}(?=[ \t:])[^\n:]*:.*?\n((?:[ \t].*\n|\n)*)",
                      justfile_text, re.M)
    return match.group(1) if match else ""


def scripts_invoked(body: str) -> list[str]:
    return sorted(set(re.findall(r"(scripts/\w+\.py)", body)))


def paths_read(script: Path, root: Path) -> set[str]:
    """Top-level repo entries a script names via a REPO_ROOT constant.

    Filtered to entries that actually exist. The regex cannot tell code from
    prose, and this script's own docstring contains a literal
    `REPO_ROOT / "..."` as illustration — which it duly flagged as an uncovered
    directory named `...` on the first run. An entry absent from the tree is
    also not a tracked input that could need a filter line.
    """
    tops: set[str] = set()
    text = script.read_text()
    # REPO_ROOT / "data" / "traits"  and  REPO_ROOT / "reports/x.tsv"
    for literal in re.findall(r'REPO_ROOT\s*/\s*"([^"]+)"', text):
        top = literal.split("/")[0]
        if (root / top).exists():
            tops.add(top)
    return tops


def filter_tops(workflow_text: str) -> set[str]:
    """Top-level entries named by qc.yaml's pull_request paths filter."""
    doc = yaml.safe_load(workflow_text)
    # PyYAML resolves the bare key `on` to boolean True under YAML 1.1.
    triggers = doc.get("on", doc.get(True)) or {}
    pull_request = triggers.get("pull_request") or {}
    patterns = pull_request.get("paths") or []
    return {str(p).split("/")[0].replace("**", "").strip() or "/" for p in patterns}


class BlindGate(RuntimeError):
    """The audit could not inspect anything, so a clean result means nothing.

    Raised rather than returned because every caller — main(), the tests, `just
    qc` — would otherwise read an empty finding list as success. This gate
    guards a bug that has recurred four times; one that passes while blind is
    worse than none, which is the rule docs/WORKFLOW_CONVENTIONS.md states and
    #286 caught this violating.
    """


def audit(root: Path = REPO_ROOT) -> list[dict[str, str]]:
    justfile_text = (root / "justfile").read_text()
    workflow = root / ".github" / "workflows" / "qc.yaml"
    covered = filter_tops(workflow.read_text())

    chain = qc_chain(justfile_text)
    if not chain:
        raise BlindGate(
            "no `qc:` dependency chain found in the justfile — the recipe may "
            "have been renamed or given arguments, and this audit inspected "
            "nothing")

    findings: list[dict[str, str]] = []
    seen: dict[str, set[str]] = {}
    read_set: set[str] = set()
    for recipe in chain:
        for rel in scripts_invoked(recipe_body(justfile_text, recipe)):
            script = root / rel
            if not script.exists():
                continue
            for top in paths_read(script, root):
                read_set.add(top)
                if top in IGNORED_TOPS or top in covered:
                    continue
                seen.setdefault(top, set()).add(f"{recipe} → {rel}")

    if not read_set:
        raise BlindGate(
            f"the qc chain ({len(chain)} recipes) yielded no readable paths — "
            "REPO_ROOT constants may have moved into a shared helper, in which "
            "case this audit is blind rather than satisfied")
    AUDIT_READ_SET.clear()
    AUDIT_READ_SET.update(read_set)
    for top, readers in sorted(seen.items()):
        findings.append({
            "path": top,
            "readers": ", ".join(sorted(readers)),
            "detail": (f"`{top}` is read by the qc chain but is not in "
                       "qc.yaml's pull_request paths filter, so a PR changing "
                       "only that directory does not run qc"),
        })
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=REPO_ROOT)
    args = ap.parse_args(argv)

    print("=== qc paths-filter coverage ===")
    try:
        findings = audit(args.root)
    except BlindGate as exc:
        print(f"  ERROR this audit inspected nothing: {exc}", file=sys.stderr)
        return 1
    print(f"  inferred read-set: {', '.join(sorted(AUDIT_READ_SET))}")
    print(f"  uncovered directories read by the qc chain: {len(findings)}")
    for row in findings:
        print(f"  ! {row['path']}  (read by {row['readers']})", file=sys.stderr)
        print(f"      {row['detail']}", file=sys.stderr)
    if not findings:
        print("  every directory the qc chain reads is in the filter")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
