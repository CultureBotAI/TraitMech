#!/usr/bin/env python3
"""Predicate-grounding migration for TraitMech causal graphs.

Walks every `data/traits/**/*.yaml`, looks at each
`causal_graphs[].edges[]` entry, and — if the edge has an empty
`predicate_id` and the free-text `predicate:` label has a curated entry in
`mappings/predicate_grounding.tsv` — writes the mapped CURIE into
`predicate_id`. One `CurationEvent` is appended per modified file.

Default is **dry-run**; pass `--apply` to actually write.

Idempotency contract:
  - existing non-empty `predicate_id` values are never overwritten;
  - a file with zero new groundings is never modified (no no-op
    CurationEvent appended).

Closed-mode `linkml.validator` runs before any write. Files that would
become invalid are logged and skipped.

Usage:
    python scripts/ground_causal_predicates.py                  # dry-run
    python scripts/ground_causal_predicates.py --apply          # write
    python scripts/ground_causal_predicates.py --mapping path/to/other.tsv
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
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
DEFAULT_MAPPING = REPO_ROOT / "mappings/predicate_grounding.tsv"
DEFAULT_RESIDUAL = REPO_ROOT / "reports/predicate_grounding_residual.tsv"
TARGET_CLASS = "TraitRecord"
CURATION_ACTION = "GROUND_CAUSAL_PREDICATES"


def load_mapping(path: Path) -> dict[str, tuple[str, str]]:
    """Read the curated label→CURIE mapping TSV.

    Returns ``{label: (target_curie, source)}``. Skips rows with missing
    label/CURIE so a half-curated row can't quietly enable a bad mapping.
    """
    if not path.exists():
        raise FileNotFoundError(f"mapping file not found: {path}")
    out: dict[str, tuple[str, str]] = {}
    with path.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            label = (row.get("label") or "").strip()
            curie = (row.get("target_curie") or "").strip()
            source = (row.get("source") or "").strip()
            if not label or not curie:
                continue
            if label in out and out[label][0] != curie:
                raise ValueError(
                    f"mapping conflict for label {label!r}: {out[label][0]} vs {curie}"
                )
            out[label] = (curie, source)
    return out


def build_validator() -> Validator:
    return Validator(
        schema=str(SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def ground_edges_in_doc(
    doc: dict[str, Any],
    mapping: dict[str, tuple[str, str]],
) -> tuple[int, Counter, Counter]:
    """Mutate ``doc`` in place, grounding empty predicate_ids.

    Returns ``(grounded_count, per_curie_counter, residual_counter)``.
    """
    grounded = 0
    per_curie: Counter = Counter()
    residual: Counter = Counter()
    for graph in (doc.get("causal_graphs") or []):
        for edge in (graph.get("edges") or []):
            pred = (edge.get("predicate") or "").strip()
            if not pred:
                continue
            existing = (edge.get("predicate_id") or "").strip()
            if existing:
                continue
            if pred in mapping:
                curie, _src = mapping[pred]
                edge["predicate_id"] = curie
                grounded += 1
                per_curie[curie] += 1
            else:
                residual[pred] += 1
    return grounded, per_curie, residual


def append_curation_event(doc: dict[str, Any], grounded: int, per_curie: Counter) -> None:
    history = doc.setdefault("curation_history", [])
    mapped_str = ", ".join(f"{c}×{n}" for c, n in per_curie.most_common())
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "curator": "claude",
        "action": CURATION_ACTION,
        "changes": (
            f"Grounded {grounded} causal-edge predicate_id field(s) "
            f"via mappings/predicate_grounding.tsv ({mapped_str})."
        ),
        "llm_assisted": True,
    }
    history.append(event)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write modified YAMLs (default: dry-run)")
    ap.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING,
                    help="curated label→CURIE TSV (default: mappings/predicate_grounding.tsv)")
    ap.add_argument("--out", type=Path, default=DEFAULT_RESIDUAL,
                    help="residual TSV output (default: reports/predicate_grounding_residual.tsv)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR,
                    help="trait YAML root (default: data/traits/)")
    args = ap.parse_args()

    mapping = load_mapping(args.mapping)
    print(f"Loaded {len(mapping)} mapped labels from {args.mapping}", file=sys.stderr)

    validator = build_validator()

    files = sorted(args.traits_dir.rglob("*.yaml"))
    print(f"Scanning {len(files)} YAMLs under {args.traits_dir}", file=sys.stderr)

    files_modified = 0
    files_skipped_invalid: list[tuple[Path, str]] = []
    edges_grounded_total = 0
    per_curie_total: Counter = Counter()
    residual_total: Counter = Counter()
    residual_examples: dict[str, list[str]] = defaultdict(list)

    for path in files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"  SKIP (parse error): {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue

        grounded, per_curie, residual = ground_edges_in_doc(doc, mapping)
        for label, n in residual.items():
            residual_total[label] += n
            if len(residual_examples[label]) < 3:
                residual_examples[label].append(str(path.relative_to(REPO_ROOT)))

        if grounded == 0:
            continue

        append_curation_event(doc, grounded, per_curie)

        report = validator.validate(doc, target_class=TARGET_CLASS)
        errors = [r for r in report.results if r.severity == Severity.ERROR]
        if errors:
            msg = errors[0].message[:200]
            files_skipped_invalid.append((path, msg))
            print(f"  SKIP (would-be invalid): {path}: {msg}", file=sys.stderr)
            continue

        files_modified += 1
        edges_grounded_total += grounded
        per_curie_total += per_curie

        if args.apply:
            path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["predicate_label", "edge_count", "example_files"])
        for label, n in residual_total.most_common():
            w.writerow([label, n, "|".join(residual_examples[label])])

    print("", file=sys.stderr)
    print("=== ground-predicates summary ===", file=sys.stderr)
    print(f"  mode:                {'APPLY' if args.apply else 'DRY-RUN'}", file=sys.stderr)
    print(f"  files scanned:       {len(files)}", file=sys.stderr)
    print(f"  files modifiable:    {files_modified}", file=sys.stderr)
    print(f"  files skip-invalid:  {len(files_skipped_invalid)}", file=sys.stderr)
    print(f"  edges grounded:      {edges_grounded_total}", file=sys.stderr)
    print(f"  residual edges:      {sum(residual_total.values())} across {len(residual_total)} distinct labels", file=sys.stderr)
    print(f"  residual TSV:        {args.out}", file=sys.stderr)
    if per_curie_total:
        print("  by target CURIE:", file=sys.stderr)
        for curie, n in per_curie_total.most_common():
            print(f"    {curie:30s} {n:>6d}", file=sys.stderr)
    if not args.apply and files_modified:
        print("", file=sys.stderr)
        print("  Re-run with --apply to write the changes.", file=sys.stderr)
    if files_skipped_invalid:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
