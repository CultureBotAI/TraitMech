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
  ACTION_UNPINNED     a ``uses:`` naming a third-party action by tag or branch
                      rather than a 40-hex commit SHA. A tag is a pointer its
                      owner can move, so a compromised upstream reaches CI
                      holding repo credentials with no diff here. Policy and
                      rationale: docs/WORKFLOW_CONVENTIONS.md. A gate rather
                      than a convention because the one pin the repo had before
                      #272 was already commented with a version its SHA did not
                      match — one for one (#273). Checks the SHA only; whether
                      the trailing comment still names the right tag needs
                      network and is Dependabot's job.
  CONCURRENCY_SHARED_ACROSS_TRIGGERS
                      a cancelling concurrency group shared between
                      ``pull_request`` and a trigger that fires against the same
                      PR without a push (``issue_comment`` and friends).
                      Concurrency is evaluated before a job's ``if:``, so a run
                      that skips every job still cancels one that is working —
                      which is how the review workflow cancelled itself on every
                      PR (#215). Third bug of this shape after #199 and #196's
                      review, hence a gate rather than a convention (#218).
  CONFLICT_MARKER     an unresolved merge-conflict marker in a tracked file.
  BROKEN_LINK         a relative Markdown link pointing at a path that does not
                      exist. Links inside fenced code blocks, indented code
                      blocks, or inline code spans are prose *about* links and
                      are not checked (#202, #208).
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

# Triggers that resolve to the SAME pull request as a `pull_request` run, so
# they can land in a group keyed on the PR — which is what made #215 possible:
# the progress comment's `issue_comment` run reached the same PR number through
# the group's `||` chain.
#
# `push` and `schedule` are deliberately absent, and for the same reason: their
# `github.ref` is a branch, never `refs/pull/N/merge`, and they carry no PR
# context to key on. A ref-keyed cancelling group — `curation-history.yaml` — is
# safe with them and flagging it would be a day-one false positive. They can
# only collide under a constant group key, and that is equally true of `push`,
# so singling out `schedule` would be an asymmetry with no basis.
TRIGGERS_ON_THE_SAME_PR = (
    "issue_comment",
    "pull_request_review",
    "pull_request_review_comment",
    # Same PR, not a push — it satisfies the rule exactly. Unused in this repo
    # today, which is the only reason it was not obvious.
    "pull_request_target",
)

# `github.event_name == 'x'` / `!= 'x'` inside a cancel-in-progress expression.
# Polarity matters: `== 'pull_request'` confines cancellation to push runs and
# is a fix, while `== 'issue_comment'` confines it to comment runs and is #215.
EVENT_NAME_EQ = re.compile(r"github\.event_name\s*==\s*['\"]([^'\"]+)['\"]")
EVENT_NAME_NE = re.compile(r"github\.event_name\s*!=\s*['\"]([^'\"]+)['\"]")

# In the group key, either of these is enough to separate runs of different
# triggers.
CONCURRENCY_DISCRIMINATORS = ("github.run_id", "github.event_name")

# Only the unambiguous markers. A bare "=======" is a legitimate Markdown setext
# heading underline, so matching it would false-positive on ordinary prose.
CONFLICT_RE = re.compile(r"^(<{7}|>{7})(\s|$)")

# [text](target) — skips images (![...]) only incidentally; an image with a
# broken relative path is worth flagging too.
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

# Only a same-document anchor is skipped by prefix; everything else with a URI
# scheme is skipped by SCHEME_RE below.
SKIP_LINK_PREFIXES = ("#",)

# An RFC 3986 scheme. Replaces the old allowlist of http/https/mailto/tel, which
# had to grow every time a new one appeared — tracking research/ brought in
# Edison's `artifact:artifact-02` refs and broke CI on links that were never
# repo paths. Measured before changing it: across every tracked .md, this skips
# exactly those two links and nothing else that was previously checked.
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")

# A fenced block opens on 3+ backticks or tildes, indented at most 3 spaces
# (4+ would be an indented code block). It closes on a fence of the SAME
# character, AT LEAST as long, and carrying no info string. The length rule is
# what lets a ````-fence contain a ```-fence, which is how one documents fenced
# markdown at all — see this repo's own #202.
FENCE_RE = re.compile(r"^(?P<indent> {0,3})(?P<fence>`{3,}|~{3,})(?P<info>.*)$")

# A list marker, with the column its content starts at. Indented code is
# measured RELATIVE to that column: inside `- item`, content begins at 2, so a
# code block needs 6 spaces, not 4. Without this a list continuation paragraph
# indented 4 reads as code and its links go unchecked (#208 review).
LIST_MARKER_RE = re.compile(r"^(?P<indent> *)(?P<marker>[-*+]|\d{1,9}[.)])(?P<space> +)")

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


def trigger_names(triggers: object) -> set[str]:
    """Normalise ``on:`` to a set of trigger names.

    ``on:`` accepts a mapping, a list (``on: [pull_request, issue_comment]``) or
    a bare string. The shorthands are rare here but perfectly valid, and a check
    that quietly does nothing on them would be the same "green because nothing
    evaluated it" failure this file exists to prevent.
    """
    if isinstance(triggers, dict):
        return {str(k) for k in triggers}
    if isinstance(triggers, list):
        return {str(t) for t in triggers}
    if isinstance(triggers, str):
        return {triggers}
    return set()


def concurrency_blocks(doc: dict) -> list[tuple[str, dict]]:
    """Every concurrency block in a workflow, workflow-level and per job.

    A plain-string ``concurrency: foo`` is the shorthand for a group with
    cancel-in-progress defaulting to false, so it can never cancel anything and
    is not returned.
    """
    out: list[tuple[str, dict]] = []
    if isinstance(doc.get("concurrency"), dict):
        out.append(("workflow-level", doc["concurrency"]))
    jobs = doc.get("jobs")
    if isinstance(jobs, dict):
        for name, job in jobs.items():
            if isinstance(job, dict) and isinstance(job.get("concurrency"), dict):
                out.append((f"job `{name}`", job["concurrency"]))
    return out


def can_cancel(block: dict) -> bool:
    """Can this block's cancel-in-progress ever evaluate true?"""
    cancel = block.get("cancel-in-progress")
    if cancel is None or cancel is False:
        return False
    # `true`, or an expression we cannot evaluate here — assume it can fire.
    return True


def discriminates_by_event(block: dict, others: list[str]) -> bool:
    """Does this block keep runs of different triggers out of one group?

    Two shapes qualify, and both are in use in this repo:
      * the group key varies by event or run — `claude-code-review.yml`;
      * cancellation itself is conditioned on the event, so a comment-triggered
        run cancels nothing — `vendored-sync.yaml`, `pr-sanity.yaml`.

    The second is checked on POLARITY, not on whether `github.event_name` is
    mentioned. Both of these mention it and only one is a fix:

        cancel-in-progress: ${{ github.event_name == 'pull_request' }}   # fix
        cancel-in-progress: ${{ github.event_name == 'issue_comment' }}  # #215

    The second confines cancellation to comment runs, which is the bug stated
    as a condition. So an equality has to select events that are *not* the
    colliding ones, and an inequality has to exclude one that is.
    """
    if any(d in str(block.get("group", "")) for d in CONCURRENCY_DISCRIMINATORS):
        return True
    cancel = block.get("cancel-in-progress")
    if not isinstance(cancel, str):
        return False
    colliding = set(others)
    equals = set(EVENT_NAME_EQ.findall(cancel))
    not_equals = set(EVENT_NAME_NE.findall(cancel))
    if equals and not (equals & colliding):
        return True
    # EVERY colliding trigger has to be excluded, not just one. With both
    # `issue_comment` and `pull_request_review` on the workflow,
    # `!= 'issue_comment'` still leaves review runs cancelling in the group.
    return bool(colliding) and colliding.issubset(not_equals)


def check_workflow_concurrency(rel: str, doc: dict, triggers: object) -> list[dict[str, str]]:
    """Flag a cancelling concurrency group shared across triggers (#215, #218).

    GitHub evaluates ``concurrency`` at the RUN level, before a job's ``if:``.
    So a run that will skip every job still joins the group and still cancels
    whatever is in it. That is how `claude-code-review` killed itself on every
    PR: the progress comment it posted fired ``issue_comment``, which resolved
    through the group's ``||`` chain to the same PR number as the in-flight
    ``pull_request`` run, and cancel-in-progress did the rest.

    Heuristic by nature — this reads a template string and cannot prove the key
    really varies. It would have caught #215, and it is the third bug of this
    shape in the fleet after #199 and #196's review, so a cheap approximation
    beats the docs page that keeps not getting written.
    """
    names = trigger_names(triggers)
    if "pull_request" not in names:
        return []
    others = [t for t in TRIGGERS_ON_THE_SAME_PR if t in names]
    if not others:
        return []

    findings: list[dict[str, str]] = []
    for where, block in concurrency_blocks(doc):
        if not can_cancel(block) or discriminates_by_event(block, others):
            continue
        findings.append({
            "check": "CONCURRENCY_SHARED_ACROSS_TRIGGERS",
            "file": rel,
            "detail": (
                f"{where} concurrency group "
                f"{block.get('group', '(unset)')!r} can cancel in progress and "
                f"is shared with {', '.join(others)}, which fire against the "
                "same PR without a push. Concurrency is evaluated before a "
                "job's `if:`, so a run that skips everything still cancels one "
                "that is working (#215). Key the group by github.event_name or "
                "github.run_id, or condition cancel-in-progress on the event."
            ),
        })
    return findings


# 40 hex characters. Anything shorter is a tag, a branch, or an abbreviated SHA
# — and an abbreviated SHA is not immutable enough to rely on.
_PINNED_REF = re.compile(r"^[0-9a-f]{40}$")


def _action_refs(text: str):
    """Yield (line_no, uses_value) for every `uses:` in a workflow.

    Read from raw text rather than the parsed document on purpose: `uses:` can
    sit in a step, a reusable-workflow job, or a composite, and walking the text
    catches all of them without enumerating the shapes. A `uses:` that YAML
    would not accept is already caught by WORKFLOW_INVALID.
    """
    for line_no, line in enumerate(text.splitlines(), 1):
        match = re.match(r"\s*-?\s*uses:\s*(\S+)", line)
        if match:
            yield line_no, match.group(1).strip("'\"")


def check_action_pins(root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    wf_dir = root / WORKFLOW_DIR
    if not wf_dir.is_dir():
        return findings
    for path in sorted(wf_dir.iterdir()):
        if path.suffix not in {".yml", ".yaml"}:
            continue
        rel = str(path.relative_to(root))
        for line_no, ref in _action_refs(path.read_text()):
            # Local composites and container actions carry no upstream to pin:
            # ./ resolves inside this repo, docker:// is pinned by its own digest
            # or tag and is not a GitHub Action reference.
            if ref.startswith((".", "docker://")):
                continue
            if "@" not in ref:
                findings.append({
                    "check": "ACTION_UNPINNED", "file": f"{rel}:{line_no}",
                    "detail": f"`{ref}` names no ref at all — pin it to a commit SHA",
                })
                continue
            action, _, git_ref = ref.partition("@")
            if not _PINNED_REF.match(git_ref):
                findings.append({
                    "check": "ACTION_UNPINNED", "file": f"{rel}:{line_no}",
                    "detail": (f"`{action}` is pinned to `{git_ref}`, which is a "
                               "movable tag or branch. Use the 40-character commit "
                               "SHA with the version in a trailing comment "
                               "(docs/WORKFLOW_CONVENTIONS.md)"),
                })
    return findings


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
        # The list/string `on:` shorthands carry no `paths:`, so they are
        # unfiltered by construction. The old `isinstance(triggers, dict)` guard
        # skipped them, which would have under-counted the very invariant this
        # check exists to keep true.
        if "pull_request" in trigger_names(triggers):
            pr = triggers.get("pull_request") if isinstance(triggers, dict) else None
            if pr is None or (isinstance(pr, dict) and not pr.get("paths")):
                unfiltered.append(rel)

        findings.extend(check_workflow_concurrency(rel, doc, triggers))

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

    Indented code blocks are skipped too (#208), under two conditions that
    together keep prose in scope:

    * They may only open after a blank line. CommonMark forbids an indented
      block from interrupting a paragraph, so wrapped prose stays scanned.
    * Indentation is measured RELATIVE to the innermost open list item. Inside
      ``- item`` content begins at column 2, so code needs 6 spaces; a
      continuation paragraph indented 4 is prose and stays scanned. Measuring
      absolutely silently dropped every such paragraph — a coverage loss, which
      is worse than the false positive being fixed.

    Known limitations, both deliberate: tabs are not treated as indentation,
    and list tracking is a single innermost column rather than a container
    stack, so exotic nesting can still misjudge the threshold.
    """
    out: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_len = 0
    opened_at: int | None = None
    in_indented = False
    # Content column of the innermost open list item; 0 when not in a list.
    list_col = 0
    # Start of document behaves like "after a blank line" — an indented block
    # may open there.
    prev_blank = True

    for lineno, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence_char is None:
            if m:
                fence_char = m.group("fence")[0]
                fence_len = len(m.group("fence"))
                opened_at = lineno
                prev_blank = False
                # FENCE_RE caps indent at 3, so any fence line has already
                # dedented out of an indented block; clearing here keeps the
                # state from being stale across the fenced region regardless.
                in_indented = False
                continue
            blank = not line.strip()
            col = len(line) - len(line.lstrip(" "))
            indented = not blank and col >= list_col + 4
            if in_indented:
                # Blank lines belong to the block; only a dedented non-blank
                # line closes it.
                if blank or indented:
                    continue
                in_indented = False
            elif indented and prev_blank:
                # CommonMark: an indented code block cannot interrupt a
                # paragraph, so it only opens after a blank line. Requiring
                # that is what keeps ordinary wrapped prose out of it.
                in_indented = True
                prev_blank = False
                continue
            # Only now — the line is prose. Updating list_col any earlier let a
            # bullet-shaped line INSIDE a code block move the threshold, which
            # reopened the very false positive this skip exists to close.
            if not blank:
                lm = LIST_MARKER_RE.match(line)
                if lm:
                    # Content column of the innermost open list item.
                    list_col = len(lm.group("indent")) + len(lm.group("marker")) \
                        + len(lm.group("space"))
                elif col == 0:
                    # Back at the margin and not a marker: the list is closed.
                    list_col = 0
            out.append((lineno, INLINE_CODE_RE.sub("", line)))
            prev_blank = blank
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
                if target.startswith(SKIP_LINK_PREFIXES) or SCHEME_RE.match(target):
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
            + check_action_pins(root)
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
