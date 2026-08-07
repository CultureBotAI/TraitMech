#!/usr/bin/env python3
"""Flag open PRs where a workflow that SHOULD have run did not (#348).

``audit_pr_checks_present`` catches TOTAL silence — a PR with no
pull-request-triggered runs at all, which is the shape the Actions outage
produced in #345. It cannot catch a PARTIAL silence, and for a structural
reason: ``claude-code-review.yml`` fires on ``pull_request`` with no ``paths:``
filter and records a run even when its ``if:`` gates skip the job, so nearly
every PR here has at least one qualifying event. ``qc``, ``pytest`` and
``validate-strict`` could all be mute and that check would still pass.

This is the stronger property: every workflow that should have run, ran. It is
a different rule rather than a tweak, which is why #346 did not attempt it.

THE REQUIRED SET IS DERIVED, NOT DECLARED. It is "every workflow in
.github/workflows with a ``pull_request:`` trigger", read from the files
themselves. A hand-maintained list would drift out of step with the workflows
the moment someone adds one — which is exactly the argument #252 used to reject
a declared list for ``audit-qc-paths``, and it applies here unchanged. Adding a
workflow adds it to the required set with no second edit.

A ``paths:`` FILTER IS NOT A MISSING RUN. Five of the eight PR-triggered
workflows here are filtered (the unfiltered three are claude-code-review,
pr-sanity and vendored-sync), and a filtered workflow legitimately does not run
on an unrelated PR. So the filters are evaluated against the PR's own changed files
and only an unfiltered-or-matching workflow is expected. That evaluation is the
hard part of this check, and it is also the payoff: a ``paths:`` regression --
the failure class #184, #200, #250 and #252 are all instances of -- shows up
here as "expected, did not run".

A SKIPPED RUN COUNTS AS HAVING RUN. GitHub records a run for a workflow whose
job-level ``if:`` gates skip it, and that record is the evidence this check
wants: the event was delivered and the workflow was evaluated. Whether the job
then chose to do nothing is the workflow's business, not this audit's.

WHAT THIS DOES NOT CATCH. A workflow's own ``paths:`` list being too narrow --
it will agree with the filter and expect nothing. ``audit-qc-paths`` is the
check for that, and the two are complementary rather than redundant: this one
asks whether the declared filter was honoured, that one asks whether the
declared filter is right.

Fetching is kept out of the rule so it is testable without network or a token;
``main`` shells out to ``gh`` and hands the parsed result in.

Usage:
    just audit-required-workflows
    python scripts/audit_required_workflows.py --json '<prs>'
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_WORKFLOWS = REPO_ROOT / ".github" / "workflows"

# Same grace period as audit_pr_checks_present: a head pushed seconds ago has no
# runs yet through no fault of its own.
MIN_AGE_MINUTES = 10

# Past this many changed files GitHub's own path-filter evaluation is documented
# as incomplete, so a workflow can legitimately fail to fire on a PR that our
# matcher says it should have. Predicting on such a PR would manufacture
# offenders, so it is SKIPPED AND NAMED rather than dropped (#346 review's rule:
# a PR that vanishes from both counts makes the output read as full coverage of
# a set it did not fully check).
PATHS_FILTER_FILE_LIMIT = 300


def _glob_to_regex(pattern: str) -> re.Pattern[str]:
    """GitHub filter-pattern semantics, which are NOT fnmatch's.

    ``*`` matches any run of characters except ``/``; ``**`` matches any run
    INCLUDING ``/``. fnmatch's ``*`` crosses ``/``, so using it would make
    ``scripts/*`` match ``scripts/a/b.py`` and quietly over-predict.
    """
    out: list[str] = []
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if c == "*":
            if pattern.startswith("**", i):
                out.append(".*")
                i += 2
            else:
                out.append("[^/]*")
                i += 1
            continue
        out.append(re.escape(c))
        i += 1
    # fullmatch, not search: a filter pattern is matched against the WHOLE
    # repo-relative path. Anchoring only the end would let `data/traits/**`
    # match `vendor/data/traits/x.yaml` and over-predict.
    return re.compile("".join(out))


# Constructs whose semantics this matcher does not implement. A workflow using
# one is reported as UNSUPPORTED rather than guessed at: silently mis-predicting
# would be worse than declining, because the whole value here is that "expected,
# did not run" means something.
_UNSUPPORTED = re.compile(r"[\[\]!+?]")


def _matches_any(patterns: list[str], path: str) -> bool:
    return any(_glob_to_regex(p).fullmatch(path) for p in patterns)


def pr_workflows(workflow_dir: Path) -> list[dict]:
    """Every workflow with a ``pull_request`` trigger, with its path filters.

    ``pull_request_target`` is deliberately NOT included: it runs against the
    base rather than the head, so its absence does not mean the head went
    unevaluated, which is the question this audit asks.
    """
    out: list[dict] = []
    for path in sorted(workflow_dir.glob("*.y*ml")):
        try:
            doc = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        # PyYAML parses the unquoted key `on:` as the BOOLEAN True (YAML 1.1),
        # so doc["on"] is absent in every workflow here. Reading only "on" would
        # make this audit find zero required workflows and pass, loudly and
        # wrongly, which is the same shape of vacuous green it exists to catch.
        on = doc.get("on", doc.get(True))
        if isinstance(on, str):
            on = {on: None}
        elif isinstance(on, list):
            on = {k: None for k in on}
        if not isinstance(on, dict) or "pull_request" not in on:
            continue
        cfg = on.get("pull_request") or {}
        cfg = cfg if isinstance(cfg, dict) else {}
        paths = list(cfg.get("paths") or [])
        ignore = list(cfg.get("paths-ignore") or [])
        out.append({
            "file": f".github/workflows/{path.name}",
            "name": str(doc.get("name") or path.stem),
            "paths": paths,
            "paths_ignore": ignore,
            "unsupported": [p for p in paths + ignore if _UNSUPPORTED.search(p)],
        })
    return out


def should_run(wf: dict, changed: list[str]) -> bool:
    """Would GitHub have dispatched ``wf`` for a PR touching ``changed``?

    No filter means always. With ``paths``, ANY changed file matching ANY
    pattern is enough. With ``paths-ignore``, the workflow runs unless EVERY
    changed file is ignored.
    """
    if wf["paths"]:
        if not any(_matches_any(wf["paths"], f) for f in changed):
            return False
    if wf["paths_ignore"]:
        if all(_matches_any(wf["paths_ignore"], f) for f in changed):
            return False
    return True


def partition(prs: list[dict], workflows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split into (offenders, skipped).

    ``prs`` entries are ``{"number", "title", "changed_files", "ran", "age_minutes"}``
    where ``ran`` is the set of workflow FILE PATHS that produced a run on the
    head SHA. Matched on path rather than ``name:`` because ``name:`` is a
    display string a curator can edit without touching anything functional --
    and a required workflow that silently drops out of the required set when
    someone retitles it is the failure mode this check exists to prevent.

    Skipped, with a reason, when the head is too young or when the changed-file
    count puts the PR past GitHub's path-filter evaluation limit.
    """
    supported = [w for w in workflows if not w["unsupported"]]
    bad, skipped = [], []
    for pr in prs:
        changed = list(pr.get("changed_files") or [])
        ran = set(pr.get("ran") or ())
        missing = [w for w in supported
                   if should_run(w, changed) and w["file"] not in ran]
        if not missing:
            continue
        # Evidence first, as in audit_pr_checks_present: a young PR that already
        # has every expected run is simply fine, and calling it "skipped" would
        # understate the coverage the run actually achieved. Youth and file count
        # only excuse an ABSENCE.
        if len(changed) > PATHS_FILTER_FILE_LIMIT:
            skipped.append({**pr, "reason": f"{len(changed)} changed files "
                            f"(> {PATHS_FILTER_FILE_LIMIT}; path filters unreliable)"})
            continue
        age = pr.get("age_minutes")
        if age is not None and age < MIN_AGE_MINUTES:
            skipped.append({**pr, "reason": f"head pushed < {MIN_AGE_MINUTES} min ago"})
            continue
        bad.append({**pr, "missing": [w["file"] for w in missing]})
    return bad, skipped


def offenders(prs: list[dict], workflows: list[dict]) -> list[dict]:
    return partition(prs, workflows)[0]


def _gh_json(args: list[str]) -> object:
    proc = subprocess.run(["gh", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"gh {' '.join(args)} failed: {proc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    return json.loads(proc.stdout or "[]")


def _gh_text_opt(args: list[str]) -> str | None:
    """Raw stdout, or None if gh failed or produced no usable value.

    A transient failure here must DEGRADE rather than terminate: the run's job is
    to report on the other PRs. `gh api -q` prints the literal "null" for a
    missing field, which is truthy, so it is filtered rather than left to an `or`.
    """
    proc = subprocess.run(["gh", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"  warning: gh {' '.join(args)} failed, falling back "
              f"({proc.stderr.strip()[:80]})", file=sys.stderr)
        return None
    out = proc.stdout.strip()
    return None if out in ("", "null") else out


def _age_minutes(iso: str, now: datetime) -> float | None:
    try:
        when = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except ValueError:
        print(f"  warning: unparseable timestamp {iso!r}; not applying the age gate",
              file=sys.stderr)
        return None
    return (now - when).total_seconds() / 60


def collect(repo: str) -> list[dict]:
    """Fetch open PRs, their changed files, and which workflows ran on the head."""
    # --limit EXPLICIT: gh pr list defaults to 30, so past 30 open PRs the rest
    # go unfetched and this prints a clean bill of health for a set it never
    # looked at -- #345's failure reproduced inside its own detector (#346 review).
    prs = _gh_json(["pr", "list", "--repo", repo, "--state", "open", "--limit", "500",
                    "--json", "number,title,headRefOid,createdAt"])
    now = datetime.now(timezone.utc)
    collected = []
    for pr in prs:  # type: ignore[union-attr]
        sha = pr["headRefOid"]
        files = _gh_json(["api", f"repos/{repo}/pulls/{pr['number']}/files",
                          "--paginate", "-q", "[.[].filename]"])
        runs = _gh_json(["api",
                         f"repos/{repo}/actions/runs"
                         f"?head_sha={sha}&event=pull_request&per_page=100",
                         "-q", "[.workflow_runs[].path]"])
        iso = _gh_text_opt(["api", f"repos/{repo}/commits/{sha}",
                            "-q", ".commit.committer.date"]) or pr["createdAt"]
        collected.append({"number": pr["number"], "title": pr["title"],
                          "changed_files": files, "ran": sorted(set(runs)),  # type: ignore[arg-type]
                          "age_minutes": _age_minutes(iso, now)})
    return collected


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",
                    default=os.environ.get("GITHUB_REPOSITORY", "CultureBotAI/TraitMech"))
    ap.add_argument("--workflows", type=Path, default=DEFAULT_WORKFLOWS)
    ap.add_argument("--json", help="pre-fetched PR list, for testing offline")
    args = ap.parse_args()

    workflows = pr_workflows(args.workflows)
    prs = json.loads(args.json) if args.json else collect(args.repo)
    bad, skipped = partition(prs, workflows)

    print("=== required workflows that did not run ===", file=sys.stderr)
    print(f"  pull_request workflows: {len(workflows)}", file=sys.stderr)
    print(f"  open PRs:               {len(prs)}", file=sys.stderr)
    print(f"  with a missing run:     {len(bad)}", file=sys.stderr)
    print(f"  skipped:                {len(skipped)}", file=sys.stderr)
    for w in workflows:
        if w["unsupported"]:
            print(f"  not predicted: {w['file']} uses unsupported filter syntax "
                  f"{w['unsupported']}", file=sys.stderr)
    for pr in skipped:
        print(f"  skipped: #{pr['number']}  {pr['title']} -- {pr['reason']}",
              file=sys.stderr)
    for pr in bad:
        print(f"  #{pr['number']}  {pr['title']}", file=sys.stderr)
        for f in pr["missing"]:
            print(f"      no run: {f}", file=sys.stderr)
    if bad:
        print("\nThese workflows are triggered by `pull_request` and their `paths:`\n"
              "filters match files this PR changes, yet no run exists on the head SHA\n"
              "(#348). A green checks tab here does NOT mean the PR was gated. Push a\n"
              "fresh commit or dispatch the workflow before trusting it.", file=sys.stderr)
        return 1
    print("  every expected workflow ran on every open PR head", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
