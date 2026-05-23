#!/usr/bin/env python3
"""Cross-check predicate labels and CURIEs against the Biolink model.

Reads:
  - `mappings/predicate_grounding.tsv` — our applied mappings (label → CURIE).
  - `reports/predicate_grounding_residual.tsv` — Scope-B candidate labels.
  - `data/raw/biolink-model.yaml` — full biolink LinkML schema (slots + aliases + exact_mappings).

For each label, reports whether Biolink defines an exact slot match (by
name or alias) or a mapping match (a biolink slot whose `exact_mappings`
list contains our target CURIE). The result tells us:

  - For applied mappings: whether we should record a `biolink:` alias
    alongside the `RO:`/`METPO:` CURIE (e.g. RO:0002327 ⇔ biolink:enables).
  - For residual Scope-B candidates: whether a biolink slot already exists
    (in which case ground to biolink instead of proposing a new METPO term).

Output: `reports/biolink_coverage.tsv` and a stderr summary.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BIOLINK_YAML = REPO_ROOT / "data/raw/biolink-model.yaml"
MAPPING_TSV = REPO_ROOT / "mappings/predicate_grounding.tsv"
RESIDUAL_TSV = REPO_ROOT / "reports/predicate_grounding_residual.tsv"
DEFAULT_OUT = REPO_ROOT / "reports/biolink_coverage.tsv"


def slot_to_curie(name: str) -> str:
    """Convert a biolink slot name to its CURIE form (`biolink:slot_name`)."""
    return f"biolink:{name.replace(' ', '_')}"


def load_biolink_indices(path: Path) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Return (label→curie, curie→list-of-biolink-curies).

    - `label_index` maps a lowercase slot name or alias to `biolink:<slot>`.
    - `mapping_index` maps a CURIE (string, e.g. "RO:0002327") to the list of
      biolink slot CURIEs whose `exact_mappings` contains it.
    """
    data = yaml.safe_load(path.read_text())
    slots = data.get("slots") or {}

    label_index: dict[str, str] = {}
    mapping_index: dict[str, list[str]] = {}

    for slot_name, slot_def in slots.items():
        slot_def = slot_def or {}
        biolink_curie = slot_to_curie(slot_name)

        # Index the slot name itself plus any aliases.
        label_index.setdefault(slot_name.lower(), biolink_curie)
        for alias in (slot_def.get("aliases") or []):
            label_index.setdefault(str(alias).lower(), biolink_curie)

        # Index every exact_mapping CURIE so we can ask "does any biolink
        # slot have RO:0002327 as an exact mapping?".
        for em in (slot_def.get("exact_mappings") or []):
            mapping_index.setdefault(str(em), []).append(biolink_curie)

    return label_index, mapping_index


def read_tsv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--biolink", type=Path, default=BIOLINK_YAML)
    ap.add_argument("--mappings", type=Path, default=MAPPING_TSV)
    ap.add_argument("--residual", type=Path, default=RESIDUAL_TSV)
    args = ap.parse_args()

    print(f"Loading {args.biolink} ...", file=sys.stderr)
    label_index, mapping_index = load_biolink_indices(args.biolink)
    print(
        f"  {len(label_index)} indexed labels/aliases, "
        f"{len(mapping_index)} indexed exact-mapping CURIEs.",
        file=sys.stderr,
    )

    mappings_rows = read_tsv_rows(args.mappings)
    residual_rows = read_tsv_rows(args.residual)

    print(
        f"Checking {len(mappings_rows)} applied mappings and "
        f"{len(residual_rows)} residual labels.",
        file=sys.stderr,
    )

    out_rows: list[dict] = []

    for row in mappings_rows:
        label = (row.get("label") or "").strip()
        target = (row.get("target_curie") or "").strip()
        bl_label = label_index.get(label.lower())
        bl_via_curie = mapping_index.get(target, [])
        out_rows.append({
            "source": "applied",
            "label": label,
            "current_curie": target,
            "biolink_via_label": bl_label or "",
            "biolink_via_exact_mapping": "|".join(bl_via_curie),
            "edge_count": "",
        })

    for row in residual_rows:
        label = (row.get("predicate_label") or "").strip()
        n = row.get("edge_count", "") or ""
        bl_label = label_index.get(label.lower())
        out_rows.append({
            "source": "residual",
            "label": label,
            "current_curie": "",
            "biolink_via_label": bl_label or "",
            "biolink_via_exact_mapping": "",
            "edge_count": n,
        })

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "source", "label", "current_curie",
                "biolink_via_label", "biolink_via_exact_mapping", "edge_count",
            ],
            delimiter="\t",
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(out_rows)

    applied_label_hits = sum(1 for r in out_rows if r["source"] == "applied" and r["biolink_via_label"])
    applied_curie_hits = sum(1 for r in out_rows if r["source"] == "applied" and r["biolink_via_exact_mapping"])
    residual_hits = sum(1 for r in out_rows if r["source"] == "residual" and r["biolink_via_label"])

    print("", file=sys.stderr)
    print("=== biolink coverage summary ===", file=sys.stderr)
    print(f"  applied mappings:                  {len(mappings_rows)}", file=sys.stderr)
    print(f"    biolink slot has same label:     {applied_label_hits}", file=sys.stderr)
    print(f"    biolink slot maps to our CURIE:  {applied_curie_hits}", file=sys.stderr)
    print(f"  residual labels:                   {len(residual_rows)}", file=sys.stderr)
    print(f"    biolink slot has same label:     {residual_hits}", file=sys.stderr)
    print(f"  output:                            {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
