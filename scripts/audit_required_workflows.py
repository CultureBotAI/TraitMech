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
from functools import lru_cache
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


@lru_cache(maxsize=None)
def _glob_to_regex(pattern: str) -> re.Pattern[str]:
    """GitHub filter-pattern semantics, which are NOT fnmatch's.

    Cached: re.compile is memoized for the module-level re.* helpers but not for
    an explicit call, and this runs once per (pattern, changed file) pair.

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


def _matches_any(patterns: tuple[str, ...] | list[str], path: str) -> bool:
    return any(_glob_to_regex(p).fullmatch(path) for p in patterns)


# `types:` values that between them cover every possible head. GitHub's default
# is opened/synchronize/reopened, and every PR head arrives via `opened` (the
# first) or `synchronize` (any later push). A workflow narrowing `types:` to a
# subset that still contains both is therefore predictable; one that does not --
# `types: [labeled]`, say -- fires on a schedule this audit cannot model.
_TYPES_COVERING_EVERY_HEAD = frozenset({"opened", "synchronize"})


def parse_workflow(filename: str, text: str) -> dict | None:
    """One workflow's PR-trigger config, or None if it has no ``pull_request``.

    Split out from ``pr_workflows`` so the same parser serves both a local
    directory and files fetched at a PR head (#354 review).

    ``pull_request_target`` is deliberately NOT included: it runs against the
    base rather than the head, so its absence does not mean the head went
    unevaluated, which is the question this audit asks.
    """
    entry = {"file": f".github/workflows/{filename}",
             "name": Path(filename).stem, "paths": [], "paths_ignore": []}
    try:
        doc = yaml.safe_load(text) or {}
    except yaml.YAMLError as exc:
        # NAMED, not silently skipped. Everything else this module declines to
        # predict is reported; a workflow that vanishes because it did not parse
        # would shrink the required set invisibly (#354 review).
        return {**entry, "unsupported": [f"unparseable YAML: {str(exc)[:60]}"]}
    if not isinstance(doc, dict):
        return None
    # PyYAML parses the unquoted key `on:` as the BOOLEAN True (YAML 1.1), so
    # doc["on"] is absent in every workflow here. Reading only "on" would make
    # this audit find zero required workflows and pass, loudly and wrongly,
    # which is the same shape of vacuous green it exists to catch.
    on = doc.get("on", doc.get(True))
    if isinstance(on, str):
        on = {on: None}
    elif isinstance(on, list):
        on = {k: None for k in on}
    if not isinstance(on, dict) or "pull_request" not in on:
        return None
    cfg = on.get("pull_request") or {}
    cfg = cfg if isinstance(cfg, dict) else {}
    paths = list(cfg.get("paths") or [])
    ignore = list(cfg.get("paths-ignore") or [])
    unsupported = [p for p in paths + ignore if _UNSUPPORTED.search(p)]
    # `branches:`/`branches-ignore:` restrict which BASE a PR must target, and
    # this audit does not read the base. Left unmodelled they would make every
    # PR against another base a false offender, so they are declined by the same
    # escape hatch as unsupported glob syntax (#354 review).
    for key in ("branches", "branches-ignore"):
        if cfg.get(key):
            unsupported.append(f"{key}: {cfg[key]}")
    types = cfg.get("types")
    if types is not None and not _TYPES_COVERING_EVERY_HEAD <= set(types):
        unsupported.append(f"types: {types}")
    return {**entry, "name": str(doc.get("name") or entry["name"]),
            "paths": paths, "paths_ignore": ignore, "unsupported": unsupported}


def pr_workflows(workflow_dir: Path) -> list[dict]:
    """Every workflow in a directory with a ``pull_request`` trigger."""
    return workflows_from_texts({p.name: p.read_text()
                                 for p in sorted(workflow_dir.glob("*.y*ml"))})


def workflows_from_texts(texts: dict[str, str]) -> list[dict]:
    """Same, from ``{filename: contents}`` — used for the PR-head fetch."""
    out = [parse_workflow(name, text) for name, text in sorted(texts.items())]
    return [w for w in out if w is not None]


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

    A PR may carry its own ``workflows``, which OVERRIDE the passed-in set.
    GitHub dispatches ``pull_request`` events using the workflow files at the PR
    HEAD, while this process has whatever ref it was checked out at -- ``main``,
    since pr-checks-present.yaml runs on push. The two disagree exactly when a PR
    touches .github/workflows, which is routine here (#184, #200, #250, #252 and
    #354 itself all do). Reading main's copy would report a PR that DELETES a
    workflow as missing that workflow's run, since the deletion matches the
    filter listing the workflow's own file -- a false "expected, did not run",
    which is precisely what makes this check stop meaning anything (#354 review).
    ``collect`` fetches the head copy; a PR whose fetch failed carries
    ``workflows: None`` and is skipped rather than judged against the wrong ref.

    Skipped, with a reason, when the head is too young, when the changed-file
    count puts the PR past GitHub's path-filter evaluation limit, or when the
    head's workflow files could not be read.
    """
    bad, skipped = [], []
    for pr in prs:
        if "workflows" in pr and pr["workflows"] is None:
            skipped.append({**pr, "reason": "could not read .github/workflows at the "
                                            "PR head; refusing to judge against main"})
            continue
        # `in`, not `or`: a head that legitimately has NO pull_request
        # workflows yields [], which is falsy, and `or` would fall back to the
        # checked-out ref -- reporting every workflow as missing on a PR that
        # deleted them all. Exactly the bug the head fetch exists to prevent.
        head = pr["workflows"] if "workflows" in pr else workflows
        supported = [w for w in head if not w["unsupported"]]
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


def flatten_pages(stdout: str) -> list[str]:
    """Filenames from ``gh api --paginate --slurp`` output.

    --slurp is required. `gh api --paginate -q` applies the jq filter to EACH
    PAGE and concatenates the outputs, so a 31-file PR (GitHub's default
    per_page is 30) yields two `[...]` documents back to back and json.loads
    raises "Extra data" -- taking down collect() for every OTHER open PR too,
    and making the >300-file skip branch unreachable because the fetch dies at
    31. A corpus seeding pass touching hundreds of data/traits files is not an
    exotic input here (#354 review). gh 2.97 refuses --slurp together with
    --jq, so the extraction happens in Python.
    """
    pages = json.loads(stdout or "[]")
    return [f["filename"] for page in pages for f in page]


def changed_files(repo: str, number: int) -> list[str]:
    proc = subprocess.run(
        ["gh", "api", f"repos/{repo}/pulls/{number}/files", "--paginate", "--slurp"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"gh pulls/{number}/files failed: {proc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    return flatten_pages(proc.stdout)


def workflows_at_ref(repo: str, sha: str) -> list[dict] | None:
    """Parse .github/workflows AS OF ``sha``, or None if it could not be read.

    GitHub dispatches ``pull_request`` events using the HEAD's workflow files,
    not the checked-out ref's, and reading the wrong one manufactures offenders
    on any PR that touches the directory (#354 review). None is a refusal, and
    partition() skips-and-names such a PR rather than falling back to main --
    a fallback would silently reintroduce the bug it is guarding against.
    """
    listing = _gh_text_opt(["api", f"repos/{repo}/contents/.github/workflows?ref={sha}",
                            "-q", "[.[] | select(.type==\"file\") | .name] | @tsv"])
    if listing is None:
        return None
    texts: dict[str, str] = {}
    for name in listing.split("\t"):
        if not name.endswith((".yml", ".yaml")):
            continue
        body = _gh_text_opt(["api", f"repos/{repo}/contents/.github/workflows/{name}"
                                    f"?ref={sha}",
                             "-H", "Accept: application/vnd.github.raw"])
        if body is None:
            return None
        texts[name] = body
    return workflows_from_texts(texts)


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
        files = changed_files(repo, pr["number"])
        runs = _gh_json(["api",
                         f"repos/{repo}/actions/runs"
                         f"?head_sha={sha}&event=pull_request&per_page=100",
                         "-q", "[.workflow_runs[].path]"])
        iso = _gh_text_opt(["api", f"repos/{repo}/commits/{sha}",
                            "-q", ".commit.committer.date"]) or pr["createdAt"]
        collected.append({"number": pr["number"], "title": pr["title"],
                          "changed_files": files, "ran": sorted(set(runs)),  # type: ignore[arg-type]
                          "workflows": workflows_at_ref(repo, sha),
                          "age_minutes": _age_minutes(iso, now)})
    return collected


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",
                    default=os.environ.get("GITHUB_REPOSITORY", "CultureBotAI/TraitMech"))
    ap.add_argument("--workflows", type=Path, default=DEFAULT_WORKFLOWS)
    ap.add_argument("--json", help="pre-fetched PR list, for testing offline")
    args = ap.parse_args()

    # The local directory is only a FALLBACK, used for --json and if a head
    # fetch is unavailable. collect() attaches each PR's own head workflows,
    # which is what GitHub actually dispatched from.
    workflows = pr_workflows(args.workflows)
    prs = json.loads(args.json) if args.json else collect(args.repo)
    bad, skipped = partition(prs, workflows)

    print("=== required workflows that did not run ===", file=sys.stderr)
    print(f"  pull_request workflows: {len(workflows)} (at {args.workflows.name}; each "
          f"PR is judged against its own head)", file=sys.stderr)
    print(f"  open PRs:               {len(prs)}", file=sys.stderr)
    print(f"  with a missing run:     {len(bad)}", file=sys.stderr)
    print(f"  skipped:                {len(skipped)}", file=sys.stderr)
    # Reported per PR, since each PR is judged against its OWN head's workflows
    # and a construct this cannot model may exist on one head and not another.
    for pr in prs:
        for w in (pr["workflows"] if pr.get("workflows") is not None
                  else workflows):
            if w["unsupported"]:
                print(f"  not predicted on #{pr['number']}: {w['file']} -- "
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
