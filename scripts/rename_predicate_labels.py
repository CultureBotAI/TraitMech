#!/usr/bin/env python3
"""Rename free-text `predicate:` labels in causal_graphs[].edges[].

One-off migration to normalize the largest curator-paraphrased
predicate clusters that lack a clean RO/Biolink home (the
"predicate residual v3" backlog item). The companion grounding
pass in `ground_causal_predicates.py` then picks up each renamed
label via its already-existing mapping in
`mappings/predicate_grounding.tsv`.

Renames only apply to edges that have **no** existing `predicate_id`
— a grounded edge is left as-is because its `predicate:` is the
curator's preferred free-text and the ground truth is the CURIE.

Default is **dry-run**; pass `--apply` to actually write. Validates
each file closed-mode before writing.

Usage:
    python scripts/rename_predicate_labels.py            # dry-run
    python scripts/rename_predicate_labels.py --apply    # write
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "src/traitmech/schema/traitmech.yaml"
TRAITS_DIR = REPO_ROOT / "data/traits"
TARGET_CLASS = "TraitRecord"
CURATION_ACTION = "RENAME_PREDICATE_LABELS"

# Rename map: old label → (new label, target CURIE the new label grounds to).
# The CURIE column is informational — the actual grounding happens via the
# separate ground_causal_predicates.py pass after this script runs.
RENAMES: dict[str, tuple[str, str]] = {
    "supports": ("enables", "RO:0002327"),
    "drives": ("regulates", "RO:0002211"),
    "maintains": ("regulates", "RO:0002211"),
    "shapes": ("causes", "biolink:causes"),
}


def build_validator() -> Validator:
    return Validator(
        schema=str(SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def rename_edges_in_doc(doc: dict[str, Any]) -> tuple[int, Counter]:
    """Mutate ``doc`` in place. Returns (renamed_count, per-rename counter)."""
    renamed = 0
    counts: Counter = Counter()
    for graph in (doc.get("causal_graphs") or []):
        for edge in (graph.get("edges") or []):
            existing_id = (edge.get("predicate_id") or "").strip()
            if existing_id:
                continue
            pred = (edge.get("predicate") or "").strip()
            if pred in RENAMES:
                new_label, _curie = RENAMES[pred]
                edge["predicate"] = new_label
                renamed += 1
                counts[f"{pred} → {new_label}"] += 1
    return renamed, counts


def append_curation_event(doc: dict[str, Any], renamed: int, counts: Counter) -> None:
    history = doc.setdefault("curation_history", [])
    summary = "; ".join(f"{k} ×{n}" for k, n in counts.most_common())
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "curator": "claude",
        "action": CURATION_ACTION,
        "changes": (
            f"Renamed {renamed} causal-edge predicate label(s) to align with "
            f"existing groundings: {summary}."
        ),
        "llm_assisted": True,
    }
    history.append(event)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write modified YAMLs (default: dry-run)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR,
                    help="trait YAML root (default: data/traits/)")
    args = ap.parse_args()

    print(f"Rename map: {len(RENAMES)} entries:", file=sys.stderr)
    for old, (new, curie) in RENAMES.items():
        print(f"  {old!r:>16}  →  {new!r:<14} ({curie})", file=sys.stderr)

    validator = build_validator()

    files = sorted(args.traits_dir.rglob("*.yaml"))
    print(f"\nScanning {len(files)} YAMLs under {args.traits_dir}", file=sys.stderr)

    files_modified = 0
    files_skipped_invalid: list[tuple[Path, str]] = []
    renames_total = 0
    counts_total: Counter = Counter()

    for path in files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"  SKIP (parse error): {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue

        renamed, counts = rename_edges_in_doc(doc)
        if renamed == 0:
            continue

        append_curation_event(doc, renamed, counts)

        report = validator.validate(doc, target_class=TARGET_CLASS)
        errors = [r for r in report.results if r.severity == Severity.ERROR]
        if errors:
            msg = errors[0].message[:200]
            files_skipped_invalid.append((path, msg))
            print(f"  SKIP (would-be invalid): {path}: {msg}", file=sys.stderr)
            continue

        files_modified += 1
        renames_total += renamed
        counts_total += counts

        if args.apply:
            path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))

    print("", file=sys.stderr)
    print("=== rename-predicate-labels summary ===", file=sys.stderr)
    print(f"  mode:                {'APPLY' if args.apply else 'DRY-RUN'}", file=sys.stderr)
    print(f"  files scanned:       {len(files)}", file=sys.stderr)
    print(f"  files modifiable:    {files_modified}", file=sys.stderr)
    print(f"  files skip-invalid:  {len(files_skipped_invalid)}", file=sys.stderr)
    print(f"  edges renamed:       {renames_total}", file=sys.stderr)
    if counts_total:
        print("  by rename:", file=sys.stderr)
        for k, n in counts_total.most_common():
            print(f"    {k:<28} {n:>4}", file=sys.stderr)
    if not args.apply and files_modified:
        print("", file=sys.stderr)
        print("  Re-run with --apply to write the changes.", file=sys.stderr)
        print("  Then re-run `just ground-predicates --apply` to ground them.", file=sys.stderr)
    if files_skipped_invalid:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
