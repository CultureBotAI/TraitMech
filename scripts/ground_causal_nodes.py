#!/usr/bin/env python3
"""Node-grounding migration for TraitMech causal graphs.

Walks every `data/traits/**/*.yaml`, looks at each
`causal_graphs[].nodes[]` entry, and — if the node has an empty
`grounding` and the (label, node_type) pair has a curated entry in
`mappings/node_grounding.tsv` — writes the mapped CURIE into
`grounding`. One `CurationEvent` is appended per modified file.

Default is **dry-run**; pass `--apply` to actually write.

Idempotency contract:
  - existing non-empty `grounding` values are never overwritten;
  - a file with zero new groundings is never modified (no no-op
    CurationEvent appended).

Closed-mode `linkml.validator` runs before any write. Files that
would become invalid are logged and skipped.

The mapping TSV is keyed on (label, node_type) because the same
free-text label can refer to different ontology classes depending
on node type — e.g. "terminal electron acceptor" appears as both a
CHEMICAL and a MOLECULAR_FUNCTION node, which map to different
CURIEs (CHEBI vs GO).

Usage:
    python scripts/ground_causal_nodes.py                  # dry-run
    python scripts/ground_causal_nodes.py --apply          # write
    python scripts/ground_causal_nodes.py --mapping path/to/other.tsv
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
DEFAULT_MAPPING = REPO_ROOT / "mappings/node_grounding.tsv"
DEFAULT_RESIDUAL = REPO_ROOT / "reports/node_grounding_residual.tsv"
TARGET_CLASS = "TraitRecord"
CURATION_ACTION = "GROUND_CAUSAL_NODES"

MappingKey = tuple[str, str]  # (label_lower, node_type)


def load_mapping(path: Path) -> dict[MappingKey, tuple[str, str]]:
    """Read the curated (label, node_type) → CURIE mapping TSV."""
    if not path.exists():
        raise FileNotFoundError(f"mapping file not found: {path}")
    out: dict[MappingKey, tuple[str, str]] = {}
    with path.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            label = (row.get("label") or "").strip().lower()
            node_type = (row.get("node_type") or "").strip()
            curie = (row.get("target_curie") or "").strip()
            source = (row.get("source") or "").strip()
            if not label or not node_type or not curie:
                continue
            key = (label, node_type)
            if key in out and out[key][0] != curie:
                raise ValueError(
                    f"mapping conflict for ({label!r}, {node_type}): "
                    f"{out[key][0]} vs {curie}"
                )
            out[key] = (curie, source)
    return out


def build_validator() -> Validator:
    return Validator(
        schema=str(SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def ground_nodes_in_doc(
    doc: dict[str, Any],
    mapping: dict[MappingKey, tuple[str, str]],
) -> tuple[int, Counter, Counter]:
    """Mutate ``doc`` in place, grounding empty grounding slots.

    Returns ``(grounded_count, per_curie_counter, residual_counter)``
    where residual_counter is keyed on (label, node_type).
    """
    grounded = 0
    per_curie: Counter = Counter()
    residual: Counter = Counter()
    for graph in (doc.get("causal_graphs") or []):
        for node in (graph.get("nodes") or []):
            label = (node.get("label") or "").strip()
            node_type = (node.get("node_type") or "").strip()
            if not label or not node_type:
                continue
            existing = (node.get("grounding") or "").strip()
            if existing:
                continue
            key = (label.lower(), node_type)
            if key in mapping:
                curie, _src = mapping[key]
                node["grounding"] = curie
                grounded += 1
                per_curie[curie] += 1
            else:
                residual[key] += 1
    return grounded, per_curie, residual


def append_curation_event(doc: dict[str, Any], grounded: int, per_curie: Counter) -> None:
    history = doc.setdefault("curation_history", [])
    mapped_str = ", ".join(f"{c}×{n}" for c, n in per_curie.most_common())
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "curator": "claude",
        "action": CURATION_ACTION,
        "changes": (
            f"Grounded {grounded} causal-node grounding field(s) "
            f"via mappings/node_grounding.tsv ({mapped_str})."
        ),
        "llm_assisted": True,
    }
    history.append(event)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write modified YAMLs (default: dry-run)")
    ap.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING,
                    help="curated (label, node_type) → CURIE TSV (default: mappings/node_grounding.tsv)")
    ap.add_argument("--out", type=Path, default=DEFAULT_RESIDUAL,
                    help="residual TSV output (default: reports/node_grounding_residual.tsv)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR,
                    help="trait YAML root (default: data/traits/)")
    args = ap.parse_args()

    mapping = load_mapping(args.mapping)
    print(f"Loaded {len(mapping)} mapped (label, node_type) keys from {args.mapping}", file=sys.stderr)

    validator = build_validator()

    files = sorted(args.traits_dir.rglob("*.yaml"))
    print(f"Scanning {len(files)} YAMLs under {args.traits_dir}", file=sys.stderr)

    files_modified = 0
    files_skipped_invalid: list[tuple[Path, str]] = []
    nodes_grounded_total = 0
    per_curie_total: Counter = Counter()
    residual_total: Counter = Counter()
    residual_examples: dict[MappingKey, list[str]] = defaultdict(list)

    for path in files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"  SKIP (parse error): {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue

        grounded, per_curie, residual = ground_nodes_in_doc(doc, mapping)
        for key, n in residual.items():
            residual_total[key] += n
            if len(residual_examples[key]) < 3:
                residual_examples[key].append(str(path.relative_to(REPO_ROOT)))

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
        nodes_grounded_total += grounded
        per_curie_total += per_curie

        if args.apply:
            path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["node_label", "node_type", "node_count", "example_files"])
        for (label, node_type), n in residual_total.most_common():
            w.writerow([label, node_type, n, "|".join(residual_examples[(label, node_type)])])

    print("", file=sys.stderr)
    print("=== ground-nodes summary ===", file=sys.stderr)
    print(f"  mode:                {'APPLY' if args.apply else 'DRY-RUN'}", file=sys.stderr)
    print(f"  files scanned:       {len(files)}", file=sys.stderr)
    print(f"  files modifiable:    {files_modified}", file=sys.stderr)
    print(f"  files skip-invalid:  {len(files_skipped_invalid)}", file=sys.stderr)
    print(f"  nodes grounded:      {nodes_grounded_total}", file=sys.stderr)
    print(f"  residual nodes:      {sum(residual_total.values())} across {len(residual_total)} distinct (label, type) keys", file=sys.stderr)
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
