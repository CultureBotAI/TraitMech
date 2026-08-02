#!/usr/bin/env python3
"""Cheap repo-wide sanity checks that run on EVERY pull request.

Every other workflow in this repo sits behind a ``paths:`` filter, so a PR
confined to ``docs/**``, a brand-new workflow file, or ``README.md`` used to run
*nothing at all* — ``gh pr checks`` reported "no checks", which reads like
"nothing to verify" but means "nothing was verified" (#200). #196 gave the repo
a floor by adding one unfiltered workflow; this adds a check that is actually
about the change in front of it.

Deliberately dependency-light and fast (stdlib + PyYAML, no network, no uv sync
beyond what is already installed) so there is never a reason to put it behind a
``paths:`` filter — which is the failure this exists to prevent.

Checks:

  WORKFLOW_INVALID    a .github/workflows/*.y{a,}ml that does not parse, or is
                      missing ``on`` / ``jobs``. A malformed workflow does not
                      fail loudly on GitHub — it silently never runs.
  NO_UNFILTERED_CI    no workflow triggers on ``pull_request`` without a
                      ``paths:`` filter. This is the #200 invariant itself: if
                      the last unfiltered workflow ever gains a filter, some PRs
                      go back to being unverified. Self-referential on purpose —
                      this script is what keeps its own guarantee true.
  CONFLICT_MARKER     an unresolved merge-conflict marker in a tracked file.
  BROKEN_LINK         a relative Markdown link pointing at a path that does not
                      exist.

Usage:
    python scripts/pr_sanity.py
    python scripts/pr_sanity.py --root .
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

WORKFLOW_DIR = Path(".github/workflows")

# Only the unambiguous markers. A bare "=======" is a legitimate Markdown setext
# heading underline, so matching it would false-positive on ordinary prose.
CONFLICT_RE = re.compile(r"^(<{7}|>{7})(\s|$)")

# [text](target) — skips images (![...]) only incidentally; an image with a
# broken relative path is worth flagging too.
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

SKIP_LINK_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")

# Text extensions worth scanning for conflict markers. Everything else (images,
# lockfiles, vendored data dumps) is skipped for speed.
TEXT_SUFFIXES = {
    ".py", ".md", ".yaml", ".yml", ".toml", ".sh", ".just", ".tsv", ".csv",
    ".json", ".html", ".css", ".js", ".txt", ".cfg", ".ini",
}


def tracked_files(root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, text=True, check=True
    ).stdout
    return [root / p for p in out.split("\0") if p]


def check_workflows(root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    wf_dir = root / WORKFLOW_DIR
    if not wf_dir.is_dir():
        # Not "nothing to check" — no workflows means no unfiltered CI, which is
        # the invariant failing in its most complete form. Returning [] here
        # would make `just qc` pass on a repo whose CI had been deleted.
        return [{
            "check": "NO_UNFILTERED_CI", "file": str(WORKFLOW_DIR),
            "detail": "no .github/workflows directory — nothing runs on any PR",
        }]

    unfiltered: list[str] = []
    for path in sorted(wf_dir.iterdir()):
        if path.suffix not in {".yml", ".yaml"}:
            continue
        rel = str(path.relative_to(root))
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            findings.append({
                "check": "WORKFLOW_INVALID", "file": rel,
                "detail": f"does not parse as YAML: {str(exc).splitlines()[0]}",
            })
            continue
        if not isinstance(doc, dict):
            findings.append({
                "check": "WORKFLOW_INVALID", "file": rel,
                "detail": "top level is not a mapping",
            })
            continue
        # PyYAML resolves the bare key `on` to boolean True (YAML 1.1), so a
        # plain doc["on"] misses it on most real workflows.
        triggers = doc.get("on", doc.get(True))
        if triggers is None:
            findings.append({
                "check": "WORKFLOW_INVALID", "file": rel, "detail": "no `on:` triggers",
            })
            continue
        if not doc.get("jobs"):
            findings.append({
                "check": "WORKFLOW_INVALID", "file": rel, "detail": "no `jobs:`",
            })
            continue
        if isinstance(triggers, dict) and "pull_request" in triggers:
            pr = triggers["pull_request"]
            if pr is None or (isinstance(pr, dict) and not pr.get("paths")):
                unfiltered.append(rel)

    if not unfiltered:
        findings.append({
            "check": "NO_UNFILTERED_CI", "file": str(WORKFLOW_DIR),
            "detail": ("no workflow runs on pull_request without a `paths:` filter, "
                       "so a PR touching only unlisted paths would run no checks "
                       "at all (#200)"),
        })
    return findings


def check_conflict_markers(files: list[Path], root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in files:
        if path.suffix not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if CONFLICT_RE.match(line):
                findings.append({
                    "check": "CONFLICT_MARKER",
                    "file": f"{path.relative_to(root)}:{lineno}",
                    "detail": line[:60],
                })
    return findings


def check_markdown_links(files: list[Path], root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in files:
        if path.suffix != ".md" or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for target in MD_LINK_RE.findall(line):
                if target.startswith(SKIP_LINK_PREFIXES):
                    continue
                # Strip any #fragment; we only assert the file exists.
                bare = target.split("#", 1)[0]
                if not bare:
                    continue
                resolved = (root / bare[1:]) if bare.startswith("/") \
                    else (path.parent / bare)
                if not resolved.exists():
                    findings.append({
                        "check": "BROKEN_LINK",
                        "file": f"{path.relative_to(root)}:{lineno}",
                        "detail": f"{target} -> {bare} does not exist",
                    })
    return findings


def sanity(root: Path) -> list[dict[str, str]]:
    files = tracked_files(root)
    return (check_workflows(root)
            + check_conflict_markers(files, root)
            + check_markdown_links(files, root))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args()

    findings = sanity(args.root)

    by_check: dict[str, int] = {}
    for f in findings:
        by_check[f["check"]] = by_check.get(f["check"], 0) + 1

    print("=== PR sanity ===", file=sys.stderr)
    print(f"  findings: {len(findings)}", file=sys.stderr)
    for name, count in sorted(by_check.items()):
        print(f"    {name:<18} {count}", file=sys.stderr)
    for f in findings[:40]:
        print(f"  {f['check']}  {f['file']}  {f['detail']}", file=sys.stderr)
    if len(findings) > 40:
        print(f"  ... and {len(findings) - 40} more", file=sys.stderr)
    if not findings:
        print("  all clear", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
