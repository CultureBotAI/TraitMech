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
``--provider rosalind`` (OpenAI's GPT-Rosalind) needs ``ROSALIND_API_KEY`` or
``OPENAI_API_KEY`` instead and writes ``-deep-research-rosalind.md``.

Usage:
    python scripts/run_trait_graph_audit.py --dry-run
    python scripts/run_trait_graph_audit.py            # full run (paid)
    python scripts/run_trait_graph_audit.py --limit 8  # pilot batch
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
from collections.abc import Mapping
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from research_trait import ROSALIND_CREDENTIALS, ROSALIND_PROVIDER, resolve_provider

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


# A report below this is a truncated write, a killed process mid-flush, or a
# provider returning an empty body — all of which satisfy `.exists()` (#244).
# The floor is set from the corpus rather than guessed: the smallest real report
# is 20,785 bytes (ecology/biosafety_level_4), so 1 KiB leaves a 20x margin and
# cannot fail on real data while still catching an artifact with nothing in it.
MIN_ARTIFACT_BYTES = 1024

PILOT_MANIFEST_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}-(?P<label>[a-z0-9][a-z0-9-]*-pilot)\.json$"
)
PILOT_TARGET_RE = re.compile(r"^(?P<category>[a-z0-9_]+)/(?P<slug>[a-z0-9_]+)$")

# A report on disk with no `ok` manifest row SUPPRESSES A CALL THAT WAS NEVER
# PAID FOR OR RECORDED — but only if resume would have looked for that name.
# Resume keys on `output_path()`, i.e. `{slug}-deep-research-{provider}.md` for
# the DEFAULT provider, so the gate is scoped to exactly that namespace (#244).
#
# The wide version of this check (every `*.md` under research/traits) was the
# review's finding on #396, and it was wrong for the reason the exception list
# itself gave: `cellulolysis-deep-research-codex.md` is harmless BECAUSE `-codex`
# is not the name resume looks for. That generalises. `just research-trait
# --provider openai` (README) writes `{slug}-deep-research-openai.md` and
# `just research-trait-edison` writes `{slug}-edison-{job}.md`; neither can
# suppress anything, and blocking on them would have turned `just qc` red on the
# first documented non-falcon run, remediable only by adding a filename to a
# constant — which is precisely how the `-codex` file came to need one.
#
# Scoping to the resume namespace means there is no exception list at all.
#
# One artifact kind lives INSIDE a resume namespace without having been paid
# for through the pipeline: a report a maintainer pasted in by hand. The two
# GPT-Rosalind answers under research/traits/ecology/ were saved as
# `-deep-research-rosalind.md` before `rosalind` became a pipeline provider,
# and each declares `pipeline_run: false` in its front matter. That flag, not
# a filename list, is what keeps them out of both sides of the gate: a
# hand-supplied file never suppresses a call (it is not a `done` for resume)
# and is never an orphan (no `ok` row was ever owed for it).
PIPELINE_RUN_FALSE_RE = re.compile(r"^pipeline_run:\s*false\s*$", re.MULTILINE)
FRONT_MATTER_PROBE_BYTES = 4096


def is_pipeline_report(path: Path) -> bool:
    """False for a report whose front matter declares ``pipeline_run: false``.

    Reads only the head of the file: the flag is front matter, and the sweep
    consults this for every target on every resume.
    """
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            head = fh.read(FRONT_MATTER_PROBE_BYTES)
    except OSError:
        return True
    if not head.startswith("---"):
        return True
    front = head.split("\n---", 1)[0]
    return PIPELINE_RUN_FALSE_RE.search(front) is None


def report_done(path: Path) -> bool:
    """Resume predicate: the pipeline's own report exists at this name."""
    return path.exists() and is_pipeline_report(path)


# What a real (non-dry-run, non-verify) run needs in the environment, per
# provider. Only the providers this harness has actually been run with are
# preflighted; anything else is left to deep-research-client, which reports a
# missing credential on the first call and fails that trait fail-soft.
PREFLIGHT_CREDENTIALS: dict[str, tuple[str, ...]] = {
    "falcon": ("EDISON_API_KEY", "FUTUREHOUSE_API_KEY"),
    "openai": ("OPENAI_API_KEY",),
    ROSALIND_PROVIDER: ROSALIND_CREDENTIALS,
}


def preflight_error(provider: str, environ: Mapping[str, str]) -> str | None:
    """Return the message to print when ``provider`` cannot be called, else None."""
    keys = PREFLIGHT_CREDENTIALS.get(resolve_provider(provider), ())
    if not keys or any(environ.get(key) for key in keys):
        return None
    return f"ERROR: {' / '.join(keys)} unset — set it or use --dry-run."


def ok_outputs(manifest: Path) -> dict[str, str]:
    """``{output path: first run_id}`` over the manifest's ``ok`` rows.

    Deduplicated per artifact on purpose. The manifest is append-only and 342 of
    the 353 artifacts carry two ``ok`` rows apiece -- the original sweep and the
    re-run after its output was lost -- so 700 rows describe 353 files. Every
    count derived from it is about artifacts, which is how the invariants are
    phrased and how the CURIE scan below already reports.
    """
    out: dict[str, str] = {}
    with manifest.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("status") != "ok":
                continue
            rel = (row.get("output") or "").strip()
            if rel:
                out.setdefault(rel, row.get("run_id", "?"))
    return out


def missing_artifacts(recorded: dict[str, str], repo_root: Path) -> list[tuple[str, str]]:
    """``ok`` rows whose artifact is gone -- a call paid for and unresumable."""
    return [(run_id, rel) for rel, run_id in sorted(recorded.items())
            if not (repo_root / rel).exists()]


def undersized_artifacts(recorded: dict[str, str], repo_root: Path,
                         floor: int = MIN_ARTIFACT_BYTES) -> list[tuple[str, str, int]]:
    """``ok`` artifacts that exist but are below ``floor`` bytes (#244).

    ``.exists()`` passes for a zero-byte file, so a truncated write, a process
    killed mid-flush, or a provider returning an empty body all read as success.
    """
    out = []
    for rel, run_id in sorted(recorded.items()):
        path = repo_root / rel
        if path.exists() and path.stat().st_size < floor:
            out.append((run_id, rel, path.stat().st_size))
    return out


def orphan_reports(research_dir: Path, repo_root: Path, recorded: dict[str, str],
                   provider: str = DEFAULT_PROVIDER) -> list[str]:
    """Reports in the RESUME NAMESPACE with no ``ok`` row (#244).

    Such a file suppresses a call that was never paid for or recorded, because
    the `pending` filter skips a target whose ``output_path()`` exists.

    Scoped to ``*-deep-research-{provider}.md`` rather than every ``*.md``,
    because that is the only name resume consults -- see the note above the
    MIN_ARTIFACT_BYTES/namespace commentary. A report from another provider is untidy and
    may well be a defect (#245), but it cannot cause the harm this gate exists
    to prevent, and failing on it would block documented workflows.

    ``.md`` only: a ``-meta.yaml`` written by ``--dry-run`` also lives here and
    represents NO research (``status: dry-run``, ``cost: None``, ``task_id:
    None`` -- #246), so counting it would let a plan nobody paid for satisfy an
    existence check.

    A report declaring ``pipeline_run: false`` is skipped: it was never owed an
    ``ok`` row, and ``report_done()`` ignores it for resume, so it cannot cause
    the harm this gate exists to prevent.
    """
    pattern = f"*-deep-research-{resolve_provider(provider)}.md"
    return sorted(
        str(p.relative_to(repo_root)) for p in research_dir.rglob(pattern)
        if str(p.relative_to(repo_root)) not in recorded and is_pipeline_report(p)
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


def audit_pilot_artifacts(research_root: Path) -> tuple[list[str], int, int]:
    """Validate root pilot manifests and their dry-run metadata sidecars (#525).

    A pilot manifest is a dated JSON list of ``category/slug`` targets. Each
    target must have exactly one matching metadata sidecar, every sidecar must
    be declared by the manifest, and the captured query hash must still match
    its query. Dry-run provenance must not claim a task id or cost.
    """
    errors: list[str] = []
    manifest_count = 0
    sidecars_seen: set[Path] = set()

    for manifest in sorted(research_root.glob("*.json")):
        match = PILOT_MANIFEST_RE.fullmatch(manifest.name)
        if not match:
            continue
        manifest_count += 1
        label = match.group("label")
        manifest_sidecars: set[Path] = set()
        try:
            targets = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{manifest}: invalid JSON: {exc}")
            continue
        if not isinstance(targets, list):
            errors.append(f"{manifest}: expected a JSON list")
            continue

        declared: set[str] = set()
        for index, target in enumerate(targets):
            if not isinstance(target, str) or not (parsed := PILOT_TARGET_RE.fullmatch(target)):
                errors.append(f"{manifest}: item {index} is not category/slug: {target!r}")
                continue
            if target in declared:
                errors.append(f"{manifest}: duplicate target {target}")
                continue
            declared.add(target)
            category, slug = parsed.group("category"), parsed.group("slug")
            matches = sorted(
                (research_root / "traits" / category).glob(
                    f"{slug}-*-{label}-meta.yaml"
                )
            )
            if len(matches) != 1:
                errors.append(
                    f"{manifest}: {target} has {len(matches)} matching meta sidecars"
                )
                manifest_sidecars.update(matches)
                sidecars_seen.update(matches)
                continue
            meta_path = matches[0]
            manifest_sidecars.add(meta_path)
            sidecars_seen.add(meta_path)
            try:
                meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
            except (OSError, yaml.YAMLError) as exc:
                errors.append(f"{meta_path}: invalid YAML: {exc}")
                continue
            if not isinstance(meta, dict):
                errors.append(f"{meta_path}: expected a YAML mapping")
                continue

            expected = {
                "slug": slug,
                "trait_category": category,
                "trait_path": f"data/traits/{category}/{slug}.yaml",
                "label": label,
                "status": "dry-run",
            }
            for field, value in expected.items():
                if meta.get(field) != value:
                    errors.append(
                        f"{meta_path}: {field}={meta.get(field)!r}, expected {value!r}"
                    )
            for field in ("job", "template_path", "submitted_at"):
                if not meta.get(field):
                    errors.append(f"{meta_path}: missing {field}")
            if meta.get("task_id") not in (None, ""):
                errors.append(f"{meta_path}: dry-run unexpectedly has task_id")
            if meta.get("total_cost") not in (None, ""):
                errors.append(f"{meta_path}: dry-run unexpectedly has total_cost")

            query = meta.get("query")
            declared_hash = meta.get("query_sha256")
            if not isinstance(query, str) or not query:
                errors.append(f"{meta_path}: missing query")
            elif not isinstance(declared_hash, str):
                errors.append(f"{meta_path}: missing query_sha256")
            elif hashlib.sha256(query.encode("utf-8")).hexdigest() != declared_hash:
                errors.append(f"{meta_path}: query_sha256 does not match query")

        all_sidecars = set((research_root / "traits").rglob(f"*-{label}-meta.yaml"))
        for extra in sorted(all_sidecars - manifest_sidecars):
            errors.append(f"{manifest}: undeclared meta sidecar {extra}")
        sidecars_seen.update(all_sidecars)

    if manifest_count == 0:
        errors.append(f"{research_root}: no dated *-pilot.json manifest found")

    return errors, manifest_count, len(sidecars_seen)


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
                         "research agent, resolved to deep-research-client's `falcon`; "
                         "`rosalind` for OpenAI's GPT-Rosalind)")
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
    if not (args.dry_run or args.verify):
        error = preflight_error(provider, os.environ)
        if error:
            print(error, file=sys.stderr)
            return 2

    targets = target_traits()
    if args.category:
        targets = [t for t in targets if t[0] == args.category.lower()]
    pending = [
        (cat, slug, label)
        for cat, slug, label in targets
        if not report_done(output_path(cat, slug, provider))
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
        recorded = ok_outputs(MANIFEST)

        missing = missing_artifacts(recorded, REPO_ROOT)
        print(f"ok artifacts missing from disk: {len(missing)}", file=sys.stderr)
        for run_id, out in missing[:20]:
            print(f"  {run_id}  {out}", file=sys.stderr)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more", file=sys.stderr)

        undersized = undersized_artifacts(recorded, REPO_ROOT)
        print(f"ok artifacts below {MIN_ARTIFACT_BYTES} bytes: {len(undersized)}",
              file=sys.stderr)
        for run_id, out, size in undersized[:20]:
            print(f"  {run_id}  {out}  ({size} bytes)", file=sys.stderr)
        if len(undersized) > 20:
            print(f"  ... and {len(undersized) - 20} more", file=sys.stderr)

        orphans = orphan_reports(RESEARCH_DIR, REPO_ROOT, recorded, provider)
        print(f"resume-namespace reports with no ok manifest row: {len(orphans)}",
              file=sys.stderr)
        for rel in orphans[:20]:
            print(f"  {rel}", file=sys.stderr)
        if len(orphans) > 20:
            print(f"  ... and {len(orphans) - 20} more", file=sys.stderr)

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

        pilot_errors, pilot_manifests, pilot_sidecars = audit_pilot_artifacts(
            REPO_ROOT / "research"
        )
        print(
            f"pilot manifests / meta sidecars: {pilot_manifests} / {pilot_sidecars}",
            file=sys.stderr,
        )
        print(f"pilot artifact errors: {len(pilot_errors)}", file=sys.stderr)
        for error in pilot_errors[:20]:
            print(f"  {error}", file=sys.stderr)
        if len(pilot_errors) > 20:
            print(f"  ... and {len(pilot_errors) - 20} more", file=sys.stderr)

        return 1 if (missing or undersized or orphans or bad_curies or pilot_errors) else 0

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
