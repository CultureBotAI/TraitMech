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
# DO NOT DELETE AS UNUSED. audit() recomputes both from its `root` argument, so
# these have no callers — but they are the only path constants this script owns,
# and therefore the entire read-set it contributes ({justfile, .github}). Sweep
# them away and audit-qc-paths becomes a `silent` script and fails itself, with
# a message about constants "moving into a shared helper" that would badly
# misdescribe what happened.
JUSTFILE = REPO_ROOT / "justfile"
QC_WORKFLOW = REPO_ROOT / ".github" / "workflows" / "qc.yaml"

# Entries whose absence from the filter would not be the bug this looks for.
# Deliberately small, and note `.github` is NOT among them: pr_sanity reads
# .github/workflows, and the filter covers it via .github/workflows/qc.yaml, so
# it is genuinely read and genuinely covered rather than exempted.
IGNORED_TOPS = {"uv.lock", ".venv"}

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
    """Top-level repo entries a script names as a path constant.

    Parsed with `ast`, not matched with a regex. A regex cannot tell code from
    prose, and this file proved it twice: its docstring's illustrative
    `REPO_ROOT / "..."` was reported as an uncovered directory named `...`, and
    then the comment explaining the two idioms contributed `data` and `src` from
    its own explanatory text — which would have made this script permanently
    incapable of tripping the silent check no matter what happened to its real
    constants (#288).

    Two shapes, because the chain uses both:
      REPO_ROOT / "data" / "traits"        (absolute)
      Path("src/traitmech/schema/…")       (repo-relative)
    """
    import ast

    literals: list[str] = []
    try:
        tree = ast.parse(script.read_text())
    except SyntaxError:
        return set()

    for node in ast.walk(tree):
        # Path("a/b")
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "Path" and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            literals.append(node.args[0].value)
        # REPO_ROOT / "a" — and for the chain REPO_ROOT / "src" / "traitmech" /
        # "templates", ONLY "src". Requiring node.left to be REPO_ROOT itself
        # rather than walking down the nesting is the whole point: collecting
        # every segment made "templates" look like a top-level read, and the
        # tracked top-level templates/ directory made that false positive
        # indistinguishable from a real finding.
        if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
                and isinstance(node.left, ast.Name)
                and node.left.id.lstrip("_") == "REPO_ROOT"
                and isinstance(node.right, ast.Constant)
                and isinstance(node.right.value, str)):
            literals.append(node.right.value)

    tops: set[str] = set()
    for literal in literals:
        top = literal.split("/")[0]
        if top and (root / top).exists():
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
    silent: set[str] = set()
    for recipe in chain:
        invoked = scripts_invoked(recipe_body(justfile_text, recipe))
        if not invoked:
            # A dependency-only recipe — the shape of `check: lint test` and of
            # `qc:` itself — has an empty body, so it would contribute nothing
            # and be skipped in silence. Grouping the chain
            # (`qc: … audit-data …` with `audit-data: audit-graphs
            # audit-snippets`) would then drop conf/data/reports/research in one
            # edit. The ratchet catches that for directories already read; it
            # cannot catch a NEW composite target reading a NEW directory,
            # because there is no ratchet entry for a directory nobody has read
            # yet. No-op today: all chain recipes invoke at least one script.
            silent.add(f"{recipe} (no scripts/*.py in its body — dependency-only "
                       "recipes are not followed)")
            continue
        for rel in invoked:
            script = root / rel
            if not script.exists():
                continue
            script_reads = paths_read(script, root)
            if not script_reads:
                silent.add(rel)
            for top in script_reads:
                read_set.add(top)
                if top in IGNORED_TOPS or top in covered:
                    continue
                seen.setdefault(top, set()).add(f"{recipe} → {rel}")

    # Per-script, not just the union. Testing only the union means the check
    # fires when EVERY script goes blind, while its own message describes one
    # script's constants moving to a shared helper — the case it would miss
    # (#288). A script contributing nothing is unexamined, not clean.
    if silent:
        raise BlindGate(
            "these qc-chain scripts yielded no readable paths, so they were not "
            "examined at all: " + ", ".join(sorted(silent))
            + ". Their path constants may have moved into a shared helper, in "
            "which case this audit is blind rather than satisfied.")
    if not read_set:
        raise BlindGate(
            f"the qc chain ({len(chain)} recipes) yielded no readable paths")
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
