#!/usr/bin/env python3
"""Batch Edison (deep-research) runner for the causal-graph completeness audit.

Enumerates every REVIEWED ``term_kind: CLASS`` trait that already carries a
causal graph, and runs ``scripts/research_trait.py`` (FutureHouse Falcon /
Edison) on each, capturing the literature mechanism into
``research/traits/<category>/<slug>-deep-research-falcon.md``. Those research
notes are the input to the completeness assessment (phase 2): does each
trait's existing causal graph capture the mechanism the literature describes?

Designed for a long, paid run:
  * RESUMABLE   — skips any trait whose research output already exists.
  * FAIL-SOFT   — one trait's failure is logged, the batch continues.
  * PACED       — optional --sleep between calls (rate-limit friendly).
  * MANIFEST    — appends status rows to reports/trait_graph_audit_manifest.tsv.

Requires ``EDISON_API_KEY`` (or ``FUTUREHOUSE_API_KEY``) in the environment for
a real run; ``--dry-run`` needs no key and just lists the planned calls.

Usage:
    python scripts/run_trait_graph_audit.py --dry-run
    python scripts/run_trait_graph_audit.py            # full run (paid)
    python scripts/run_trait_graph_audit.py --limit 8  # pilot batch
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from research_trait import resolve_provider

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
MANIFEST = REPO_ROOT / "reports" / "trait_graph_audit_manifest.tsv"
# Default deep-research provider. "edison" is a TraitMech-side alias resolved by
# research_trait.resolve_provider() to deep-research-client's `falcon` — Falcon is
# the Edison Scientific platform's research agent, and the client has no provider
# literally named `edison`. Resolving here too keeps output filenames (and hence
# resume detection) in the established `-deep-research-falcon.md` namespace.
DEFAULT_PROVIDER = "edison"

# `--extra dev` is REQUIRED: deep-research-client lives in the dev optional-
# dependency group, and a plain `uv run` re-syncs the venv without it, deleting
# the binary the child needs. Omitting it makes every call in the sweep fail
# with a bare exit 1. Mirrors the justfile's `research-trait` recipe.
SPAWN = ["uv", "run", "--extra", "dev", "python", "scripts/research_trait.py"]


def target_traits() -> list[tuple[str, str, str]]:
    """Return (category, slug, label) for REVIEWED CLASS traits with a graph."""
    out: list[tuple[str, str, str]] = []
    for path in sorted(TRAITS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        if not isinstance(doc, dict):
            continue
        if doc.get("mapping_status") != "REVIEWED" or doc.get("term_kind") != "CLASS":
            continue
        if not (doc.get("causal_graphs") or []):
            continue
        out.append((path.parent.name, path.stem, doc.get("label", path.stem)))
    return out


def output_path(category: str, slug: str, provider: str = DEFAULT_PROVIDER) -> Path:
    return RESEARCH_DIR / category / f"{slug}-deep-research-{resolve_provider(provider)}.md"


# CURIE shapes that are always wrong in a research artifact. These are cheap
# textual checks, not ontology lookups — whether `GO:0009860` is the RIGHT id for
# the label beside it is a different (and much larger) question, tracked in #243.
_CURIE_PREFIXES = "GO|CHEBI|ENVO|PATO|RO|UBERON|CL|NCBITaxon|METPO"
MALFORMED_CURIE_PATTERNS: tuple[tuple[str, "re.Pattern[str]"], ...] = (
    # `METPO:METPO:1000059`. The template asks the provider to quote an already-
    # prefixed identifier verbatim, and four reports came back having prefixed it
    # again anyway. A fifth (nitrogen_fixing_symbiosis) was generated while the
    # manual grep for these was running, so the grep missed it and it needed a
    # third paid pass — which is why this lives in the tree rather than in a
    # shell history.
    ("double prefix",
     re.compile(r"\b([A-Za-z][A-Za-z0-9_]{1,15}):\1:[A-Za-z0-9_]+", re.IGNORECASE)),
    # `go:0009860` — CURIE prefixes are case-sensitive and no consumer lowercases.
    ("lowercase prefix", re.compile(rf"\b(?:{_CURIE_PREFIXES})\b:\d+", re.IGNORECASE)),
    # `GO_0009860`: the OBO underscore form used where a CURIE was expected. The
    # negative lookbehind spares the same string inside a real PURL
    # (http://purl.obolibrary.org/obo/GO_0009860), which is legitimate.
    ("underscore form", re.compile(rf"(?<![/\w])(?:{_CURIE_PREFIXES})_\d+\b")),
    # `\d+` rather than `\d{4,}`: local ids in these ontologies are not all long.
    # The corpus carries 65 one-to-three-digit CURIEs across 42 files —
    # `NCBITaxon:562`, `NCBITaxon:2`, `CHEBI:422` — and a digit floor would hide
    # every lowercased or underscored form of them. The floor is also
    # unnecessary: both patterns pin the prefix to the list above, so prose like
    # `step 3_2024` cannot reach them at any digit count.
)


def scan_malformed_curies(paths: list[Path]) -> list[tuple[Path, int, str, str]]:
    """Return (path, line_no, pattern_name, matched_text) for every bad CURIE."""
    bad: list[tuple[Path, int, str, str]] = []
    for path in paths:
        for line_no, line in enumerate(path.read_text().splitlines(), 1):
            for name, pattern in MALFORMED_CURIE_PATTERNS:
                for match in pattern.finditer(line):
                    text = match.group(0)
                    # The lowercase-prefix pattern is case-insensitive so it can
                    # find the bad casing at all; drop the correctly-cased hits it
                    # necessarily also matches.
                    if name == "lowercase prefix" and text.split(":")[0] in (
                            _CURIE_PREFIXES.split("|")):
                        continue
                    bad.append((path, line_no, name, text))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true",
                    help="check every ok row's artifact exists; exit 1 if any is "
                         "missing. No calls, no cost.")
    ap.add_argument("--limit", type=int, default=0, help="cap number of NEW calls (0 = all)")
    ap.add_argument("--sleep", type=float, default=2.0, help="seconds to stagger worker launches")
    ap.add_argument("--workers", type=int, default=1, help="concurrent deep-research-client calls")
    ap.add_argument("--category", default="", help="restrict to one category")
    ap.add_argument("--provider", default=DEFAULT_PROVIDER,
                    help=f"provider or alias (default: {DEFAULT_PROVIDER}, the Edison "
                         "research agent, resolved to deep-research-client's `falcon`)")
    args = ap.parse_args()
    provider = args.provider

    # The Edison platform credential is provisioned as EDISON_PLATFORM_API_KEY
    # (the name the edison_client SDK reads), but this harness's preflight and the
    # research_trait.py subprocess it spawns (which inherits this env) read
    # EDISON_API_KEY. Alias it so a run works regardless of which name is set —
    # mirrors research_trait.py:research_env().
    if not os.environ.get("EDISON_API_KEY") and os.environ.get("EDISON_PLATFORM_API_KEY"):
        os.environ["EDISON_API_KEY"] = os.environ["EDISON_PLATFORM_API_KEY"]

    # --verify and --dry-run make no calls, so neither should need a credential.
    # Gating the integrity check behind the key would make it unrunnable on a
    # fresh clone and in CI — the two places most likely to notice that an `ok`
    # row has no artifact.
    if not (args.dry_run or args.verify) and not (
            os.environ.get("EDISON_API_KEY") or os.environ.get("FUTUREHOUSE_API_KEY")):
        print("ERROR: EDISON_API_KEY / FUTUREHOUSE_API_KEY unset — set it or use --dry-run.", file=sys.stderr)
        return 2

    targets = target_traits()
    if args.category:
        targets = [t for t in targets if t[0] == args.category.lower()]
    pending = [
        (cat, slug, label)
        for cat, slug, label in targets
        if not output_path(cat, slug, provider).exists()
    ]
    done_already = len(targets) - len(pending)
    print(f"targets: {len(targets)}  already-researched: {done_already}  pending: {len(pending)}", file=sys.stderr)
    if args.limit:
        pending = pending[: args.limit]
        print(f"  (limited to {len(pending)} this run)", file=sys.stderr)

    if args.verify:
        # The manifest is a spend record, so an `ok` row whose artifact is gone
        # is the one failure mode that matters: it says a call was paid for and
        # cannot be resumed into, because resume keys on the file existing.
        # 342 rows were in that state before research/ was tracked, and four
        # more were created by deleting reports the running sweep had already
        # passed. Relying on someone remembering is how the first 342 were lost.
        missing = []
        with MANIFEST.open() as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("status") != "ok":
                    continue
                out = (row.get("output") or "").strip()
                if out and not (REPO_ROOT / out).exists():
                    missing.append((row.get("run_id", "?"), out))
        print(f"manifest ok rows with a missing artifact: {len(missing)}",
              file=sys.stderr)
        for run_id, out in missing[:20]:
            print(f"  {run_id}  {out}", file=sys.stderr)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more", file=sys.stderr)

        # Scanned over every .md under research/. This used to mean reports AND
        # their citation sidecars, justified by the sidecar echoing the rendered
        # prompt — but #249 dropped the sidecars as a broken duplicate, and that
        # rationale was itself the redundancy it complained of: the same
        # identifiers live in the report's own `template_variables` front matter.
        # Checked before removing them: ZERO CURIE-shaped tokens appeared in a
        # sidecar that were not also in its report, so coverage is unchanged and
        # the artifact count simply halves.
        artifacts = sorted(RESEARCH_DIR.rglob("*.md"))
        bad_curies = scan_malformed_curies(artifacts)
        # Reported per-report, because that is how the invariant is phrased —
        # one report with two bad CURIEs is one report, not two. The match count
        # rides alongside so the number of lines to fix is still visible.
        bad_files = {path for path, _, _, _ in bad_curies}
        print(f"reports carrying a malformed CURIE: {len(bad_files)} "
              f"({len(bad_curies)} matches; scanned {len(artifacts)} artifacts)",
              file=sys.stderr)
        for path, line_no, name, text in bad_curies[:20]:
            rel = path.relative_to(REPO_ROOT)
            print(f"  {rel}:{line_no}  {name}: {text}", file=sys.stderr)
        if len(bad_curies) > 20:
            print(f"  ... and {len(bad_curies) - 20} more", file=sys.stderr)

        return 1 if (missing or bad_curies) else 0

    # One id for every row this invocation writes. The manifest is append-only
    # and a trait can legitimately appear more than once — a failure and its
    # retry, or a re-run after the artifacts were lost — and without this there
    # is no field distinguishing those. `biofilm_formation` carried three
    # indistinguishable rows before this existed, so "what was billed, when"
    # was the one question the spend record could not answer about itself.
    run_id = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    print(f"run_id: {run_id}", file=sys.stderr)

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    new = not MANIFEST.exists()
    mf = MANIFEST.open("a", newline="")
    w = csv.writer(mf, delimiter="\t", lineterminator="\n")
    if new:
        w.writerow(["run_id", "category", "slug", "status", "output"])

    if args.dry_run:
        for i, (cat, slug, label) in enumerate(pending, 1):
            cmd = SPAWN + ["--provider", provider, "--category", cat, "--slug", slug]
            print(f"[{i}/{len(pending)}] {cat}/{slug}  ({label})")
            print("   " + " ".join(cmd))
        mf.close()
        return 0

    lock = threading.Lock()
    counts = {"ok": 0, "fail": 0, "started": 0}
    total = len(pending)

    def run_one(item: tuple[str, str, str]) -> None:
        cat, slug, label = item
        # Stagger launches so N workers don't all hit the API in the same instant.
        with lock:
            counts["started"] += 1
            idx = counts["started"]
        if args.sleep:
            time.sleep(args.sleep * ((idx - 1) % max(args.workers, 1)))
        cmd = SPAWN + ["--provider", provider, "--category", cat, "--slug", slug]
        print(f"[start {idx}/{total}] {cat}/{slug}  ({label})", file=sys.stderr)
        try:
            # Capture rather than discard: a swallowed stderr turns every
            # failure into an undiagnosable `fail:1` in the manifest.
            subprocess.run(cmd, check=True, cwd=REPO_ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            status, ok = "ok", True
        except subprocess.CalledProcessError as e:
            tail = (e.stderr or "").strip().splitlines()
            status, ok = f"fail:{e.returncode}", False
            if tail:
                print(f"       {cat}/{slug}: {tail[-1][:200]}", file=sys.stderr)
        with lock:
            counts["ok" if ok else "fail"] += 1
            w.writerow([run_id, cat, slug, status,
                        str(output_path(cat, slug, provider).relative_to(REPO_ROOT)) if ok else ""])
            mf.flush()
            done = counts["ok"] + counts["fail"]
            print(f"[done {done}/{total}] {cat}/{slug}  -> {status}  "
                  f"(ok={counts['ok']} fail={counts['fail']})", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=max(args.workers, 1)) as ex:
        futures = [ex.submit(run_one, item) for item in pending]
        for _ in as_completed(futures):
            pass

    mf.close()
    print(f"\ndone: ok={counts['ok']} fail={counts['fail']} "
          f"(skipped {done_already} already-researched)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
