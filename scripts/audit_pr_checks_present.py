#!/usr/bin/env python3
"""Flag open PRs that received no CI at all (#345).

PR #344 produced ZERO `pull_request` workflow runs — not failures, not skips.
`gh pr checks` printed "no checks reported", `mergeStateStatus` stayed `CLEAN`,
and nothing distinguished "verified" from "never evaluated". Two of the
workflows that failed to fire (`pr-sanity`, `vendored-sync`) carry no ``paths:``
filter at all, deliberately, so the usual filter explanations do not apply and
the mechanism is still unidentified.

This audit therefore detects the SILENCE rather than any one cause of it. It
asks a question that stays meaningful however the runs went missing: does this
open PR have at least one check that was triggered by the pull request itself?

Evidence is an ALLOWLIST, not "anything but dispatch". A denylist would let a
trigger type added later silently start counting; this fails closed instead.
``workflow_dispatch`` in particular must never count — dispatching by hand is
exactly what someone does *after* noticing the problem, so counting it would
make the check pass on precisely the PRs it exists to find.

WHAT THIS DOES NOT CATCH. ``claude-code-review.yml`` fires on ``pull_request``
with no ``paths:`` filter, and records a run even when its ``if:`` gates skip the
job. So essentially every PR here gets at least one ``pull_request`` run from the
reviewer bot, and this audit can only detect TOTAL event silence — #344's shape.
A PARTIAL silence (``qc``/``pytest``/``validate-strict`` mute while the reviewer
bot fires) passes. Do not read a green ``audit-pr-checks`` as "the gating
workflows ran". The stronger property needs a named set of REQUIRED workflows
checked by name, which is a different rule, not a tweak to this one.

Fetching is kept out of ``offenders`` so the rule is testable without network or
a GitHub token; ``main`` shells out to ``gh`` and hands the parsed result in.

Usage:
    just audit-pr-checks              # every open PR
    python scripts/audit_pr_checks_present.py --json '<gh json>'
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

# Events that count as "the pull request itself triggered this". An ALLOWLIST so
# a trigger type added later fails closed rather than silently becoming evidence
# (#346 review). `push` is deliberately absent: every workflow here is
# `push: branches: [main]`, so a push run against a PR head would not mean the PR
# was evaluated.
EVIDENCE_EVENTS = frozenset({"pull_request", "pull_request_target"})

# A PR opened seconds before this runs has no runs yet through no fault of its
# own. Below this age it is skipped rather than reported (#346 review).
MIN_AGE_MINUTES = 10


def offenders(prs: list[dict]) -> list[dict]:
    """PRs with no run triggered by the pull request itself.

    ``prs`` entries are ``{"number", "title", "events", "age_minutes"}`` where
    ``events`` are the ``event`` fields of that PR head's workflow runs. A PR
    younger than ``MIN_AGE_MINUTES`` is skipped; ``age_minutes`` may be omitted,
    in which case age is not considered.
    """
    out = []
    for pr in prs:
        if pr.get("age_minutes") is not None and pr["age_minutes"] < MIN_AGE_MINUTES:
            continue
        if not (set(pr.get("events") or ()) & EVIDENCE_EVENTS):
            out.append(pr)
    return out


def _gh_json(args: list[str]) -> object:
    proc = subprocess.run(["gh", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"gh {' '.join(args)} failed: {proc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    return json.loads(proc.stdout or "[]")


def collect(repo: str) -> list[dict]:
    """Fetch open PRs and the trigger events of each head SHA's runs."""
    # --limit is EXPLICIT, not inherited: gh pr list defaults to 30, so past 30
    # open PRs the rest are never fetched and this prints a clean bill of health
    # for a set it never looked at — the exact failure #345 is about, reproduced
    # inside the detector (#346 review).
    prs = _gh_json(["pr", "list", "--repo", repo, "--state", "open", "--limit", "500",
                    "--json", "number,title,headRefOid,createdAt"])
    now = datetime.now(timezone.utc)
    collected = []
    for pr in prs:  # type: ignore[union-attr]
        # per_page likewise explicit: the API defaults to 30, and a PR with many
        # hand-dispatched runs can push a genuine pull_request run off page one.
        runs = _gh_json(["api",
                         f"repos/{repo}/actions/runs"
                         f"?head_sha={pr['headRefOid']}&per_page=100",
                         "-q", "[.workflow_runs[].event]"])
        created = datetime.fromisoformat(pr["createdAt"].replace("Z", "+00:00"))
        collected.append({"number": pr["number"], "title": pr["title"],
                          "events": runs,
                          "age_minutes": (now - created).total_seconds() / 60})
    return collected


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    # GITHUB_REPOSITORY is set in Actions; the literal is only a local convenience.
    ap.add_argument("--repo",
                    default=os.environ.get("GITHUB_REPOSITORY", "CultureBotAI/TraitMech"))
    ap.add_argument("--json", help="pre-fetched PR list, for testing offline")
    args = ap.parse_args()

    prs = json.loads(args.json) if args.json else collect(args.repo)
    bad = offenders(prs)

    print("=== open PRs with no pull-request-triggered checks ===", file=sys.stderr)
    print(f"  open PRs:   {len(prs)}", file=sys.stderr)
    print(f"  unchecked:  {len(bad)}", file=sys.stderr)
    for pr in bad:
        print(f"  #{pr['number']}  {pr['title']}", file=sys.stderr)
    if bad:
        print("\nThese PRs look mergeable and were never evaluated (#345). Dispatch the\n"
              "gating workflows against the branch, or push a fresh commit, before\n"
              "trusting a green-looking checks tab.", file=sys.stderr)
        return 1
    print("  every open PR has at least one pull-request-triggered check",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
