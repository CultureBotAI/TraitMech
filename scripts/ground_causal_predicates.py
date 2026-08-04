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
from pathlib import Path
from typing import Any

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import (
    ValidationFailedError,
    validate_trait,
    write_validated_trait,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "src/traitmech/schema/traitmech.yaml"
TRAITS_DIR = REPO_ROOT / "data/traits"
DEFAULT_MAPPING = REPO_ROOT / "mappings/predicate_grounding.tsv"
DEFAULT_RESIDUAL = REPO_ROOT / "reports/predicate_grounding_residual.tsv"
TARGET_CLASS = "TraitRecord"
CURATION_ACTION = "GROUND_CAUSAL_PREDICATES"


def _types(raw: str | None) -> frozenset[str] | None:
    """Parse a ``subject_types``/``object_types`` cell.

    ``*`` or empty means "any node type" and returns None. Anything else is a
    ``|``-separated set of CausalNodeTypeEnum names.
    """
    cell = (raw or "*").strip()
    if not cell or cell == "*":
        return None
    return frozenset(t.strip() for t in cell.split("|") if t.strip())


def load_mapping(path: Path) -> dict[str, tuple[str, str, frozenset | None, frozenset | None]]:
    """Read the curated label→CURIE mapping TSV.

    Returns ``{label: (target_curie, source, subject_types, object_types)}``.
    Skips rows with missing label/CURIE so a half-curated row can't quietly
    enable a bad mapping.

    The type columns are what make a grounding checkable at all. An exact label
    match is not sufficient: `causally upstream of` IS the label of RO:0002411
    and every corpus edge carrying it connects material entities, which RO's
    definition over occurrents forbids (#235). The id↔label gate cannot see
    that — it compares a CURIE to its label and never looks at the edge — so
    the constraint has to live beside the mapping and be enforced here (#236).
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
            out[label] = (curie, source,
                          _types(row.get("subject_types")),
                          _types(row.get("object_types")))
    return out


def ground_edges_in_doc(
    doc: dict[str, Any],
    mapping: dict[str, tuple[str, str, frozenset | None, frozenset | None]],
) -> tuple[int, Counter, Counter, Counter]:
    """Mutate ``doc`` in place, grounding empty predicate_ids.

    Returns ``(grounded_count, per_curie, residual, blocked)``. ``blocked``
    counts edges whose label IS mapped but whose node types fall outside the
    mapping's declared domain/range — they stay ungrounded and stay in the
    residual, because a wrong grounding is worse than a missing one.
    """
    grounded = 0
    per_curie: Counter = Counter()
    residual: Counter = Counter()
    blocked: Counter = Counter()
    for graph in (doc.get("causal_graphs") or []):
        node_type = {n.get("node_id"): n.get("node_type")
                     for n in (graph.get("nodes") or [])}
        for edge in (graph.get("edges") or []):
            pred = (edge.get("predicate") or "").strip()
            if not pred:
                continue
            existing = (edge.get("predicate_id") or "").strip()
            if existing:
                continue
            if pred in mapping:
                curie, _src, subj_ok, obj_ok = mapping[pred]
                s_type = node_type.get(edge.get("subject"))
                o_type = node_type.get(edge.get("object"))
                if ((subj_ok is not None and s_type not in subj_ok)
                        or (obj_ok is not None and o_type not in obj_ok)):
                    blocked[f"{pred} ({s_type}->{o_type})"] += 1
                    residual[pred] += 1
                    continue
                edge["predicate_id"] = curie
                grounded += 1
                per_curie[curie] += 1
            else:
                residual[pred] += 1
    return grounded, per_curie, residual, blocked


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

    files = sorted(args.traits_dir.rglob("*.yaml"))
    print(f"Scanning {len(files)} YAMLs under {args.traits_dir}", file=sys.stderr)

    files_modified = 0
    files_skipped_invalid: list[tuple[Path, str]] = []
    edges_grounded_total = 0
    per_curie_total: Counter = Counter()
    residual_total: Counter = Counter()
    blocked_total: Counter = Counter()
    residual_examples: dict[str, list[str]] = defaultdict(list)

    for path in files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"  SKIP (parse error): {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue

        grounded, per_curie, residual, blocked = ground_edges_in_doc(doc, mapping)
        blocked_total.update(blocked)
        for label, n in residual.items():
            residual_total[label] += n
            if len(residual_examples[label]) < 3:
                residual_examples[label].append(str(path.relative_to(REPO_ROOT)))

        if grounded == 0:
            continue

        mapped_str = ", ".join(f"{c}×{n}" for c, n in per_curie.most_common())
        record_curation_event(
            doc,
            curator="claude",
            action=CURATION_ACTION,
            changes=(
                f"Grounded {grounded} causal-edge predicate_id field(s) "
                f"via mappings/predicate_grounding.tsv ({mapped_str})."
            ),
            llm_assisted=True,
        )

        # Single validation per mode: dry-run uses the standalone validator
        # (no write); --apply lets write_validated_trait do the only check.
        invalid_msg: str | None = None
        if args.apply:
            try:
                write_validated_trait(doc, path, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
            except ValidationFailedError as exc:
                invalid_msg = exc.errors[0].message[:200] if exc.errors else str(exc)[:200]
        else:
            errors = validate_trait(doc, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
            if errors:
                invalid_msg = errors[0].message[:200]

        if invalid_msg is not None:
            files_skipped_invalid.append((path, invalid_msg))
            print(f"  SKIP (would-be invalid): {path}: {invalid_msg}", file=sys.stderr)
            continue

        files_modified += 1
        edges_grounded_total += grounded
        per_curie_total += per_curie

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
    if blocked_total:
        # Reported separately from the plain residual: these labels ARE mapped,
        # and are ungrounded only because the edge's node types fall outside the
        # mapping's declared domain/range. Folding them into the residual would
        # read as "no CURIE known", which is the opposite of the situation.
        print(f"  blocked by node-type constraint: {sum(blocked_total.values())}",
              file=sys.stderr)
        for shape, n in blocked_total.most_common(10):
            print(f"    {shape:60s} {n:>5d}", file=sys.stderr)
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
