#!/usr/bin/env python3
"""Run Edison Scientific deep research against TraitMech trait records.

Uses the ``edison-client`` SDK directly. The companion ``research_trait.py``
wraps ``deep-research-client``, which reaches Edison through its ``falcon``
provider — but that path exposes none of Edison's job selection and none of the
response provenance. This is the TraitMech port of CommunityMech's
``research_community_edison.py``.

RESPONSE CAPTURE IS SHARED AND GOVERNED. A 2026-08-17 review (#389, #404)
found that ``_edison_capture.py`` had diverged and that TraitMech alone retained
the correct new-invocation sidecar tracking. That fix was selected as the
canonical payload and propagated. Claw's pinned governance manifest now covers
the helper in every Edison-capable Mech, so ``scripts/check_vendored_sync.sh``
detects any future one-copy edit. Change the canonical claw payload and roll a
reviewed pin across the fleet; do not edit this vendored helper locally.

The default job is LITERATURE (== ``job-futurehouse-paperqa3``), the PaperQA
agent — the best fit for "what mechanisms produce this trait, what conditions
express it, what is the evidence"-type questions. Use ``--job literature-high``
for the deeper variant (more reads, higher cost), ``--job precedent`` for
first-mention search, ``--job phoenix`` for synthesis.

Auth: reads ``EDISON_API_KEY`` from the repo-root ``.env`` (auto-loaded via
python-dotenv), falling back to ``EDISON_PLATFORM_API_KEY`` for shells that
export the SDK-native name. See ``.env.example``.

Addressing differs from the sibling Mechs: a TraitMech record is identified by
``category/slug`` (``physiology/autotrophic``), because slugs are only unique
within a category. A bare slug is accepted and resolved across categories, but
is rejected as ambiguous if it matches in more than one — silently picking the
first would attach research to the wrong trait.

Outputs land under ``research/traits/{category}/{slug}-edison-{job}.md``, with a
sibling ``-meta.yaml`` capturing the rendered query, task_id, total_cost,
status, template path and template vars — enough to audit or re-run.

Usage::

    # single record, fully qualified
    python scripts/research_trait_edison.py --target physiology/autotrophic

    # bare slug (resolved across categories; errors if ambiguous)
    python scripts/research_trait_edison.py --target autotrophic

    # batch from a JSON list of "category/slug" strings
    python scripts/research_trait_edison.py --batch queue.json --limit 5

    # dry-run: writes the meta yaml with the full rendered query, spends nothing
    python scripts/research_trait_edison.py --target physiology/autotrophic --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import _edison_capture as ec  # noqa: E402  -- response/citation/agent capture
import research_trait as rt  # noqa: E402  -- reuse template_vars + loaders

DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "trait_causal_graph_research.md"
DEFAULT_OUT_DIR = REPO_ROOT / "research" / "traits"


_JOB_ALIASES: dict[str, str] = {
    "literature": "LITERATURE",
    "paperqa": "LITERATURE",
    "literature-high": "LITERATURE_HIGH",
    "literature_high": "LITERATURE_HIGH",
    "paperqa-high": "LITERATURE_HIGH",
    "precedent": "PRECEDENT",
    "phoenix": "PHOENIX",
}


def resolve_job(name: str):
    """Map a user-friendly --job alias to the edison_client JobNames enum."""
    from edison_client import JobNames

    key = _JOB_ALIASES.get(name.lower())
    if key is None:
        raise SystemExit(
            f"Unknown --job '{name}'. Choose one of: " + ", ".join(sorted(_JOB_ALIASES))
        )
    return getattr(JobNames, key)


def load_api_key() -> str:
    """Pick up the Edison key from the repo ``.env`` or the environment.

    ``EDISON_API_KEY`` is the canonical name and what ``.env`` carries;
    ``EDISON_PLATFORM_API_KEY`` is the name the SDK reads natively and is
    honoured for shells that export it. If both are set they may be different
    Edison *accounts* — prefer setting exactly one, in ``.env``.
    """
    load_dotenv(REPO_ROOT / ".env")
    key = os.environ.get("EDISON_API_KEY") or os.environ.get("EDISON_PLATFORM_API_KEY")
    if not key:
        raise SystemExit(
            "EDISON_API_KEY is not set. Add it to .env at the repo root "
            "(see .env.example), or export it in your shell."
        )
    return key


def resolve_trait_target(target: str) -> tuple[Path, str, str]:
    """Resolve ``category/slug``, a bare slug, or a path to (path, category, slug).

    A bare slug is convenient but only safe when unique: trait slugs are unique
    *within* a category, not across them. When a bare slug matches several
    categories this raises rather than guessing, because guessing would silently
    file research against the wrong trait record.
    """
    raw = target.strip()

    # An explicit path
    candidate = Path(raw)
    if candidate.suffix == ".yaml" and candidate.exists():
        p = candidate.resolve()
        return p, p.parent.name, p.stem

    # category/slug
    if "/" in raw:
        category, _, slug = raw.partition("/")
        # Strip once, up front: returning the raw slug here leaked ".yaml" into
        # the output filenames and into trait_slug in the rendered (paid) query.
        slug = slug.removesuffix(".yaml")
        return rt.resolve_trait_file(category, slug), category.lower(), slug

    # bare slug — search every category
    slug = raw.removesuffix(".yaml")
    hits = sorted(rt.TRAITS_DIR.glob(f"*/{slug}.yaml"))
    if not hits:
        cats = ", ".join(sorted(p.name for p in rt.TRAITS_DIR.iterdir() if p.is_dir()))
        raise FileNotFoundError(
            f"No trait '{slug}' in any category. Categories: {cats}"
        )
    if len(hits) > 1:
        found = ", ".join(f"{p.parent.name}/{slug}" for p in hits)
        raise SystemExit(
            f"Ambiguous target '{slug}' — matches {len(hits)} categories: {found}. "
            "Qualify it as category/slug."
        )
    return hits[0], hits[0].parent.name, slug


class _DefaultEmpty(dict):
    """``str.format_map`` helper: leave unknown placeholders blank instead of KeyError."""

    def __missing__(self, key):  # noqa: ANN001
        return ""


def render_query(
    trait_path: Path,
    category: str,
    slug: str,
    template_path: Path,
    doc: dict[str, Any] | None = None,
) -> tuple[str, dict[str, str]]:
    """Render the deep-research template for a single trait.

    Returns ``(query_text, template_vars)`` so callers can stamp the variables
    into the meta file alongside the rendered query.
    """
    if doc is None:
        doc = rt.load_trait(trait_path)
    variables = rt.template_vars(doc, category, slug)
    template = template_path.read_text()
    return template.format_map(_DefaultEmpty(variables)), variables


def _short_job(job) -> str:
    """CLI-friendly filename suffix: ``JobNames.LITERATURE_HIGH`` -> ``literature-high``."""
    return job.name.lower().replace("_", "-")


def _display_path(path: Path) -> str:
    """Show ``path`` relative to the repo when possible; else absolute."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def run_one(
    client,
    trait_path: Path,
    category: str,
    slug: str,
    job,
    template_path: Path,
    out_root: Path,
    dry_run: bool,
    label: str = "",
) -> dict[str, Any]:
    """Submit one task; write results under ``out_root/<category>/``; return stats.

    On a successful call ``_edison_capture.capture_full_response`` writes the
    answer .md plus four sibling files (-response.json, -citations.md,
    -agent-state.json, -files.json) for provenance.
    """
    from edison_client import TaskRequest

    doc = rt.load_trait(trait_path)
    query, variables = render_query(trait_path, category, slug, template_path, doc)
    job_short = _short_job(job)
    label_suffix = f"-{label}" if label else ""
    stem = f"{slug}-edison-{job_short}{label_suffix}"
    # Mirror the repo's existing layout: research/traits/<category>/<file>
    out_dir = out_root / category
    meta_path = out_dir / f"{stem}-meta.yaml"

    def _safe_rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(REPO_ROOT))
        except ValueError:
            return str(p)

    base_meta: dict[str, Any] = {
        "slug": slug,
        "trait_category": category,
        "trait_path": _safe_rel(trait_path),
        "trait_identifier": str(doc.get("identifier") or ""),
        "job": job.name,
        "job_id": job.value,
        "label": label,
        "template_path": _safe_rel(template_path),
        "template_vars": variables,
        "query_chars": len(query),
        "query": query,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }

    if dry_run:
        meta = ec.capture_dry_run(out_dir=out_dir, stem=stem, query=query, base_meta=base_meta)
        out_dir.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100))
        md_path = out_dir / f"{stem}.md"
        print(f"[DRY RUN] {_display_path(trait_path)} -> {_display_path(md_path)}")
        print(f"          job={job.name} query_chars={len(query)} meta={_display_path(meta_path)}")
        return {"slug": slug, "status": "dry-run", "cost": 0.0}

    out_dir.mkdir(parents=True, exist_ok=True)
    task = TaskRequest(name=job, query=query)
    print(f"  + submitting {category}/{slug} ({job.name})...", flush=True)
    [response] = client.run_tasks_until_done(task, progress_bar=False)

    meta = ec.capture_full_response(
        response=response,
        client=client,
        out_dir=out_dir,
        stem=stem,
        query=query,
        base_meta=base_meta,
    )
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100))
    md_path = out_dir / f"{stem}.md"
    total_cost = meta.get("total_cost")
    print(
        f"    -> {_display_path(md_path)}  cost={total_cost}  "
        f"citations={meta.get('citations_parsed')}  "
        f"agent_state={meta.get('sidecar_files', {}).get('agent_state_json', False)}"
    )
    return {"slug": slug, "status": meta["status"], "cost": total_cost or 0.0}


def load_batch_targets(batch_path: Path) -> list[str]:
    """Return target strings from a JSON batch file.

    Accepts a JSON list of strings ("category/slug" or bare slug) or of objects
    carrying ``target`` / ``slug`` / ``identifier`` / ``file_path``. Objects that
    supply ``category`` alongside ``slug`` are joined so the result stays
    unambiguous.
    """
    data = json.loads(batch_path.read_text())
    if not isinstance(data, list):
        raise SystemExit(f"--batch expects a JSON list: {batch_path}")
    out: list[str] = []
    for entry in data:
        if isinstance(entry, str):
            out.append(entry)
        elif isinstance(entry, dict):
            if entry.get("category") and entry.get("slug"):
                out.append(f"{entry['category']}/{entry['slug']}")
                continue
            for key in ("target", "slug", "identifier", "file_path"):
                if entry.get(key):
                    out.append(str(entry[key]))
                    break
    return out


def main(argv: list[str] | None = None) -> int:
    # RawDescriptionHelpFormatter, because the default one runs __doc__ through
    # _fill_text, which collapses all whitespace before wrapping — the drift
    # table above renders as run-on prose without it. The docstring already
    # leaked into --help before the table existed; the table is the first part
    # of it that depends on alignment (#404 review).
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--target", help="category/slug, a bare slug, or a path to a trait YAML.")
    src.add_argument("--batch", type=Path, help="Path to a JSON list of targets.")
    ap.add_argument(
        "--job",
        default="literature",
        help="literature (paperqa3, default) | literature-high | precedent | phoenix",
    )
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument(
        "--label",
        default="",
        help="Optional suffix on output filenames so a non-default template's run "
        "doesn't overwrite the default one for the same trait+job.",
    )
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--limit", type=int, default=None, help="With --batch, cap how many run.")
    ap.add_argument("--start", type=int, default=0, help="With --batch, skip this many first.")
    ap.add_argument(
        "--dry-run", action="store_true", help="Render queries + print plan; do NOT call the API."
    )
    args = ap.parse_args(argv)

    job = resolve_job(args.job)

    targets: list[tuple[Path, str, str]]
    if args.target:
        targets = [resolve_trait_target(args.target)]
    else:
        names = load_batch_targets(args.batch)[args.start :]
        if args.limit is not None:
            names = names[: args.limit]
        targets = []
        unresolved: list[str] = []
        for name in names:
            try:
                targets.append(resolve_trait_target(name))
            except (FileNotFoundError, SystemExit):
                unresolved.append(name)
        if unresolved:
            print(f"Note: skipped {len(unresolved)} unresolvable batch entries:", file=sys.stderr)
            for u in unresolved[:5]:
                print(f"  - {u}", file=sys.stderr)
            if len(unresolved) > 5:
                print(f"  - ... {len(unresolved) - 5} more", file=sys.stderr)

    if not targets:
        print("No targets to research.", file=sys.stderr)
        return 2

    print(f"Edison job:    {job.name} ({job.value})")
    print(f"Template:      {_display_path(args.template.resolve())}")
    print(f"Output root:   {_display_path(args.out_dir.resolve())}")
    print(f"Traits:        {len(targets)}")
    if args.dry_run:
        print("Mode:          DRY RUN (no API calls, no credits spent)")
    print()

    client = None
    if not args.dry_run:
        api_key = load_api_key()
        from edison_client import EdisonClient

        client = EdisonClient(api_key=api_key)

    results: list[dict[str, Any]] = []
    try:
        for trait_path, category, slug in targets:
            results.append(
                run_one(
                    client,
                    trait_path,
                    category,
                    slug,
                    job,
                    args.template,
                    args.out_dir,
                    args.dry_run,
                    args.label,
                )
            )
    finally:
        if client is not None:
            client.close()

    if not args.dry_run:
        total_cost = sum(r["cost"] or 0.0 for r in results)
        print()
        print(f"Done. {len(results)} traits researched. Total reported cost: {total_cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
