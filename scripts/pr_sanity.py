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
                      exist. Links inside fenced code blocks or inline code
                      spans are prose *about* links and are not checked (#202).
  UNTERMINATED_FENCE  a code fence that is opened and never closed. Everything
                      after it would go unchecked, so this is reported rather
                      than silently shrinking coverage.

Usage:
    python scripts/pr_sanity.py
    python scripts/pr_sanity.py --root .
"""
from __future__ import annotations

import argparse
import os
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

# A fenced block opens on 3+ backticks or tildes, indented at most 3 spaces
# (4+ would be an indented code block). It closes on a fence of the SAME
# character, AT LEAST as long, and carrying no info string. The length rule is
# what lets a ````-fence contain a ```-fence, which is how one documents fenced
# markdown at all — see this repo's own #202.
FENCE_RE = re.compile(r"^(?P<indent> {0,3})(?P<fence>`{3,}|~{3,})(?P<info>.*)$")

# An inline code span: matching runs of backticks on one line. `[x](y.md)`
# inside one is prose about a link, not a link.
INLINE_CODE_RE = re.compile(r"(`+)(?:(?!\1).)*?\1")

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


def _exists_exact(candidate: Path) -> bool:
    """``candidate.exists()``, but case-exact even on a case-insensitive
    filesystem.

    macOS resolves ``skill.md`` to a file named ``SKILL.md``; Linux does not. A
    plain ``exists()`` therefore passes locally and fails in CI — which is
    exactly how a stale lowercase link survived the SKILL.md rename in #190
    until this check first ran on a runner. Comparing the final component
    against the real directory listing makes the result the same on both.
    """
    if not candidate.exists():
        return False
    try:
        return candidate.name in os.listdir(candidate.parent)
    except OSError:
        return False


def _within(candidate: Path, root: Path) -> bool:
    """True if ``candidate`` is inside ``root``.

    Both sides go through ``abspath``, which normalises ``..`` lexically without
    requiring the path to exist — the targets being classified are often missing,
    which is the whole point. Both sides matter: comparing a relative candidate
    against an absolute root always raises ValueError, which would silently
    classify every in-repo link as external and make the link check vacuous.
    """
    try:
        Path(os.path.abspath(candidate)).relative_to(Path(os.path.abspath(root)))
        return True
    except ValueError:
        return False


def prose_lines(text: str) -> tuple[list[tuple[int, str]], int | None]:
    """Split ``text`` into (lineno, line) pairs outside fenced code blocks.

    Returns those pairs plus the line number of an unterminated opening fence,
    or None. That second value matters: an unclosed fence makes every following
    line invisible to the checks, so silently returning a short list would turn
    a typo into "the rest of this file is no longer verified" — the failure this
    whole script exists to prevent. The caller reports it.

    Inline code spans are blanked rather than dropped so column positions and
    surrounding prose on the same line are still scanned.
    """
    out: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_len = 0
    opened_at: int | None = None

    for lineno, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence_char is None:
            if m:
                fence_char = m.group("fence")[0]
                fence_len = len(m.group("fence"))
                opened_at = lineno
                continue
            out.append((lineno, INLINE_CODE_RE.sub("", line)))
        else:
            # Closing fence: same char, at least as long, and no info string.
            if (m and m.group("fence")[0] == fence_char
                    and len(m.group("fence")) >= fence_len
                    and not m.group("info").strip()):
                fence_char = None
                fence_len = 0
                opened_at = None
    return out, opened_at


def check_markdown_links(files: list[Path], root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in files:
        if path.suffix != ".md" or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        scannable, unterminated = prose_lines(text)
        if unterminated is not None:
            findings.append({
                "check": "UNTERMINATED_FENCE",
                "file": f"{path.relative_to(root)}:{unterminated}",
                "detail": ("code fence opened here is never closed, so every "
                           "later line in this file goes unchecked"),
            })
        for lineno, line in scannable:
            for target in MD_LINK_RE.findall(line):
                if target.startswith(SKIP_LINK_PREFIXES):
                    continue
                # Strip any #fragment; we only assert the file exists.
                bare = target.split("#", 1)[0]
                if not bare:
                    continue
                resolved = (root / bare[1:]) if bare.startswith("/") \
                    else (path.parent / bare)
                # Links that escape the repo (README's ../CultureMech, the
                # skills' ../../../../kg-microbe/...) point at sibling fleet
                # checkouts. Whether they resolve depends on what happens to be
                # cloned next door, so checking them makes the result depend on
                # the machine: they pass locally and fail on a CI runner. Out of
                # scope — this verifies links *within* the repo.
                if not _within(resolved, root):
                    continue
                if not _exists_exact(resolved):
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
