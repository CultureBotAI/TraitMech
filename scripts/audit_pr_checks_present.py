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

Runs triggered by ``workflow_dispatch`` are deliberately NOT counted. Dispatching
by hand is exactly what someone does after noticing the problem, so counting
those would make the check pass on precisely the PRs it exists to find.

Fetching is kept out of ``offenders`` so the rule is testable without network or
a GitHub token; ``main`` shells out to ``gh`` and hands the parsed result in.

Usage:
    just audit-pr-checks              # every open PR
    python scripts/audit_pr_checks_present.py --json '<gh json>'
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

# A run whose event is in here does not count as evidence the PR was evaluated.
NON_EVIDENCE_EVENTS = frozenset({"workflow_dispatch", "schedule"})


def offenders(prs: list[dict]) -> list[dict]:
    """PRs with no run triggered by the pull request itself.

    ``prs`` entries are ``{"number": int, "title": str, "events": [str, ...]}``
    where ``events`` are the ``event`` fields of that PR head's workflow runs.
    """
    out = []
    for pr in prs:
        events = set(pr.get("events") or ())
        if not (events - NON_EVIDENCE_EVENTS):
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
    prs = _gh_json(["pr", "list", "--repo", repo, "--state", "open",
                    "--json", "number,title,headRefOid"])
    collected = []
    for pr in prs:  # type: ignore[union-attr]
        runs = _gh_json(["api",
                         f"repos/{repo}/actions/runs?head_sha={pr['headRefOid']}",
                         "-q", "[.workflow_runs[].event]"])
        collected.append({"number": pr["number"], "title": pr["title"],
                          "events": runs})
    return collected


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", default="CultureBotAI/TraitMech")
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
