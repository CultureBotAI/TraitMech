#!/usr/bin/env python3
"""Every ``biolink:`` CURIE we ground to must exist in the pinned model (#342).

``mappings/predicate_grounding.tsv`` grounded the label ``encodes`` to
``biolink:encodes`` with ``source=biolink`` and a note claiming an "exact label
match against biolink slot". The pinned ``data/raw/biolink-model.yaml`` (4.4.0)
has no slot of that name — the gene-to-product slot is ``has gene product`` —
so the CURIE resolved to nothing upstream.

``reports/biolink_coverage.tsv`` already recorded it as the only applied
``biolink:`` CURIE with both backing columns empty. **The signal existed and
nothing read it**, which is the actual defect: a report nobody consults is not a
check. This is that check.

The rule is deliberately narrow. It does NOT require the corpus LABEL to match a
slot name — most labels are synonyms (``generates``, ``yields`` and seven others
all ground to ``biolink:produces``), and demanding otherwise would flag correct
rows. It requires only that the CURIE names a real slot, converting
``biolink:has_gene_product`` to ``has gene product`` the way the model spells it.

A local coinage is legitimate when nothing upstream fits — ``encodes`` is kept
precisely because a gene CLUSTER to protein COMPLEX edge does not fit
``has gene product``'s range. What is not legitimate is claiming it came from
biolink, so such rows must say ``source=local`` and are exempt here.

Usage:
    just audit-biolink-curies
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MAPPING = REPO_ROOT / "mappings" / "predicate_grounding.tsv"
DEFAULT_MODEL = REPO_ROOT / "data" / "raw" / "biolink-model.yaml"

# A row may ground to a biolink: CURIE that does not exist upstream ONLY if it
# declares itself local. That keeps the coinage possible and the claim honest.
LOCAL_SOURCE = "local"


def slot_names(model_path: Path) -> set[str]:
    model = yaml.safe_load(model_path.read_text())
    return set(model.get("slots") or {})


def curie_to_slot(curie: str) -> str:
    """``biolink:has_gene_product`` -> ``has gene product``."""
    return curie.split(":", 1)[1].replace("_", " ")


def unbacked(mapping_path: Path, model_path: Path) -> list[dict[str, str]]:
    """Rows grounding to a biolink CURIE with no slot, not marked local."""
    slots = slot_names(model_path)
    out: list[dict[str, str]] = []
    with mapping_path.open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            curie = (row.get("target_curie") or "").strip()
            if not curie.startswith("biolink:"):
                continue
            if (row.get("source") or "").strip() == LOCAL_SOURCE:
                continue
            if curie_to_slot(curie) not in slots:
                out.append({"label": row.get("label", ""), "curie": curie,
                            "source": (row.get("source") or "").strip()})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING)
    ap.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    args = ap.parse_args()

    bad = unbacked(args.mapping, args.model)
    print("=== biolink CURIE resolution ===", file=sys.stderr)
    print(f"  unbacked rows: {len(bad)}", file=sys.stderr)
    for r in bad:
        print(f"  {r['label']} -> {r['curie']} (source={r['source']})", file=sys.stderr)
    if bad:
        print("\nThese ground to a biolink: CURIE with no slot in the pinned model.\n"
              "Either repoint to a real slot, or -- if nothing upstream fits -- keep\n"
              "the coinage and set source=local so the row stops claiming biolink\n"
              "provenance it does not have (#342).", file=sys.stderr)
        return 1
    print("  every biolink: CURIE resolves to a slot in the pinned model",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
