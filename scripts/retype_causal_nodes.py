#!/usr/bin/env python3
"""Re-type free-text `node_type:` values in causal_graphs[].nodes[].

One-off migration that fixes specific (label, current_type) pairs
identified in the v3 METPO proposal cohort as mis-typed against the
`CausalNodeTypeEnum`. Mirrors the structure of
`rename_predicate_labels.py`.

Only re-types nodes whose **(label_lower, current_node_type)** pair
matches a hardcoded `RETYPES` entry. Matching is exact on
`node_type`; the label is matched case-insensitively but the
original label string in the YAML is preserved.

Default is **dry-run**; pass `--apply` to actually write. Validates
each file closed-mode before writing.

Usage:
    python scripts/retype_causal_nodes.py            # dry-run
    python scripts/retype_causal_nodes.py --apply    # write
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
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
TARGET_CLASS = "TraitRecord"
CURATION_ACTION = "RETYPE_CAUSAL_NODES"

# (label_lower, current_node_type) → new_node_type.
#
# Scope rule: only re-type when an existing CausalNodeTypeEnum value
# is a clean semantic fit. For mis-typed nodes whose proper category
# is missing from the enum (bioenergetic STATE, membrane QUALITY,
# metabolic CAPACITY), defer to a follow-up that extends the enum.
RETYPES: dict[tuple[str, str], str] = {
    # Microbial biomass is aggregate biochemistry — best existing fit
    # in CausalNodeTypeEnum is CHEMICAL (a chemical entity / mixture).
    # Currently mis-typed as BIOLOGICAL_PROCESS in the v3 proposal
    # (proposals/metpo_traitmech_v3/proposal.md, "Node-typing notes").
    ("biomass", "BIOLOGICAL_PROCESS"): "CHEMICAL",
}

# Mis-typed labels that the current enum can't represent cleanly.
# Listed here so the PR description and proposal.md stay in sync.
DEFERRED = [
    ("proton motive force", "BIOLOGICAL_PROCESS",
     "needs a bioenergetic-STATE enum value"),
    ("membrane fluidity", "BIOLOGICAL_PROCESS",
     "needs a QUALITY enum value (PATO axis)"),
    ("reducing power", "CHEMICAL",
     "needs a metabolic-CAPACITY enum value"),
]


def retype_nodes_in_doc(doc: dict[str, Any]) -> tuple[int, Counter]:
    """Mutate ``doc`` in place. Returns (retyped_count, per-rule counter)."""
    retyped = 0
    counts: Counter = Counter()
    for graph in (doc.get("causal_graphs") or []):
        for node in (graph.get("nodes") or []):
            label = (node.get("label") or "").strip().lower()
            current = (node.get("node_type") or "").strip()
            key = (label, current)
            if key in RETYPES:
                new_type = RETYPES[key]
                node["node_type"] = new_type
                retyped += 1
                counts[f"{label}: {current} → {new_type}"] += 1
    return retyped, counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write modified YAMLs (default: dry-run)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR,
                    help="trait YAML root (default: data/traits/)")
    args = ap.parse_args()

    print(f"Retype map: {len(RETYPES)} entries:", file=sys.stderr)
    for (lbl, cur), new in RETYPES.items():
        print(f"  ({lbl!r}, {cur!r}) → {new!r}", file=sys.stderr)
    if DEFERRED:
        print("\nDeferred (no clean enum fit):", file=sys.stderr)
        for lbl, cur, reason in DEFERRED:
            print(f"  ({lbl!r}, {cur!r}) — {reason}", file=sys.stderr)

    files = sorted(args.traits_dir.rglob("*.yaml"))
    print(f"\nScanning {len(files)} YAMLs under {args.traits_dir}", file=sys.stderr)

    files_modified = 0
    files_skipped_invalid: list[tuple[Path, str]] = []
    retypes_total = 0
    counts_total: Counter = Counter()

    for path in files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"  SKIP (parse error): {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue

        retyped, counts = retype_nodes_in_doc(doc)
        if retyped == 0:
            continue

        summary = "; ".join(f"{k} ×{n}" for k, n in counts.most_common())
        record_curation_event(
            doc,
            curator="claude",
            action=CURATION_ACTION,
            changes=(
                f"Re-typed {retyped} causal-node node_type field(s) to align with "
                f"CausalNodeTypeEnum semantics: {summary}."
            ),
            llm_assisted=True,
        )

        errors = validate_trait(doc, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
        if errors:
            msg = errors[0].message[:200]
            files_skipped_invalid.append((path, msg))
            print(f"  SKIP (would-be invalid): {path}: {msg}", file=sys.stderr)
            continue

        files_modified += 1
        retypes_total += retyped
        counts_total += counts

        if args.apply:
            try:
                write_validated_trait(doc, path, target_class=TARGET_CLASS, schema_path=SCHEMA_PATH)
            except ValidationFailedError as exc:
                print(f"  ✗ validation failed for {path.name}: {exc.summary()}", file=sys.stderr)
                continue

    print("", file=sys.stderr)
    print("=== retype-causal-nodes summary ===", file=sys.stderr)
    print(f"  mode:                {'APPLY' if args.apply else 'DRY-RUN'}", file=sys.stderr)
    print(f"  files scanned:       {len(files)}", file=sys.stderr)
    print(f"  files modifiable:    {files_modified}", file=sys.stderr)
    print(f"  files skip-invalid:  {len(files_skipped_invalid)}", file=sys.stderr)
    print(f"  nodes retyped:       {retypes_total}", file=sys.stderr)
    if counts_total:
        print("  by retype:", file=sys.stderr)
        for k, n in counts_total.most_common():
            print(f"    {k:<60} {n:>4}", file=sys.stderr)
    if not args.apply and files_modified:
        print("", file=sys.stderr)
        print("  Re-run with --apply to write the changes.", file=sys.stderr)
    if files_skipped_invalid:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
