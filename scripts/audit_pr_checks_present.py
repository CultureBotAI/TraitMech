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


def partition(prs: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split into (offenders, skipped-for-youth).

    Returned separately rather than dropped, so main() can NAME the skipped ones.
    A PR that vanished from both counts would make the output read as full
    coverage of a set it did not fully check — the same silent-omission shape
    this tool exists to catch, one level down (#346 review).
    """
    bad, young = [], []
    for pr in prs:
        age = pr.get("age_minutes")
        if age is not None and age < MIN_AGE_MINUTES:
            young.append(pr)
        elif not (set(pr.get("events") or ()) & EVIDENCE_EVENTS):
            bad.append(pr)
    return bad, young


def offenders(prs: list[dict]) -> list[dict]:
    """PRs with no run triggered by the pull request itself.

    ``prs`` entries are ``{"number", "title", "events", "age_minutes"}`` where
    ``events`` are the ``event`` fields of that PR head's workflow runs. A PR
    younger than ``MIN_AGE_MINUTES`` is skipped; ``age_minutes`` may be omitted,
    in which case age is not considered.
    """
    return partition(prs)[0]


def _gh_text(args: list[str]) -> str:
    """Raw stdout from gh. `-q` unwraps to a bare scalar, which is NOT valid JSON
    for a string value -- `json.loads("2026-08-06T21:47:27Z")` raises."""
    proc = subprocess.run(["gh", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"gh {' '.join(args)} failed: {proc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    return proc.stdout.strip()


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
        sha = pr["headRefOid"]
        # Filter SERVER-SIDE rather than paginating. per_page=100 was a bigger
        # ceiling, not the absence of one — hand-dispatched runs could still
        # crowd a genuine run off page one. `event=` cannot (#346 review).
        found = []
        for event in sorted(EVIDENCE_EVENTS):
            n = _gh_json(["api",
                          f"repos/{repo}/actions/runs"
                          f"?head_sha={sha}&event={event}&per_page=1",
                          "-q", ".total_count"])
            if n:
                found.append(event)
                break  # one is enough; skips a call on the healthy path
        # Age is only consulted for a PR that would otherwise be reported, so the
        # extra request costs nothing on the healthy path — which also keeps the
        # per-PR call count from compounding at --limit scale (#346 review).
        age = None
        if not found:
            # The HEAD COMMIT's clock, not the PR's. A PR opened last week and
            # pushed twenty seconds ago has a brand-new SHA with no runs yet, and
            # push is far more frequent than open, so createdAt covered the rarer
            # case. Falls back to createdAt if the commit lookup fails.
            iso = _gh_text(["api", f"repos/{repo}/commits/{sha}",
                            "-q", ".commit.committer.date"]) or pr["createdAt"]
            when = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
            age = (now - when).total_seconds() / 60
        collected.append({"number": pr["number"], "title": pr["title"],
                          "events": found, "age_minutes": age})
    return collected


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    # GITHUB_REPOSITORY is set in Actions; the literal is only a local convenience.
    ap.add_argument("--repo",
                    default=os.environ.get("GITHUB_REPOSITORY", "CultureBotAI/TraitMech"))
    ap.add_argument("--json", help="pre-fetched PR list, for testing offline")
    args = ap.parse_args()

    prs = json.loads(args.json) if args.json else collect(args.repo)
    bad, young = partition(prs)

    print("=== open PRs with no pull-request-triggered checks ===", file=sys.stderr)
    print(f"  open PRs:   {len(prs)}", file=sys.stderr)
    print(f"  unchecked:  {len(bad)}", file=sys.stderr)
    print(f"  skipped:    {len(young)} (head pushed < {MIN_AGE_MINUTES} min ago)",
          file=sys.stderr)
    for pr in young:
        print(f"  skipped (too new): #{pr['number']}  {pr['title']}", file=sys.stderr)
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
