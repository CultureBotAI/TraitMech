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

A coinage is legitimate when nothing upstream fits. What is not legitimate is
spelling it as a ``biolink:`` CURIE, because that is what gets written into trait
records and it reads as an upstream term there. #342's coinage was therefore
minted as ``METPO:2007813`` rather than exempted, and ``ALLOWED_UNBACKED`` is
empty: an exemption is a code change someone reviews, not a cell edit.

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

# CURIEs allowed to have no backing slot. EMPTY, and keyed to the CURIE rather
# than to a free-text column value (#350 review).
#
# The first cut exempted any row whose `source` said "local", which meant a
# future unbacked CURIE could be silenced by typing five characters into a TSV
# cell -- the same shape of failure this gate exists to catch, one level up. The
# repo's other blocking gate keys its escapes to specific identifiers
# (`exceptions:` in conf/id_label_targets.yaml), and this now follows it.
#
# It is empty because #342's only coinage was minted as METPO:2007813 instead.
# Adding an entry is deliberately a code change, so a second coinage is an
# explicit decision someone reviews rather than a cell edit.
ALLOWED_UNBACKED: frozenset[str] = frozenset()


def slot_names(model_path: Path) -> set[str]:
    model = yaml.safe_load(model_path.read_text())
    return set(model.get("slots") or {})


def curie_to_slot(curie: str) -> str:
    """``biolink:has_gene_product`` -> ``has gene product``."""
    return curie.split(":", 1)[1].replace("_", " ")


def unbacked(mapping_path: Path, model_path: Path) -> list[dict[str, str]]:
    """Rows grounding to a biolink CURIE with no slot in the pinned model."""
    slots = slot_names(model_path)
    out: list[dict[str, str]] = []
    with mapping_path.open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            curie = (row.get("target_curie") or "").strip()
            if not curie.startswith("biolink:"):
                continue
            if curie in ALLOWED_UNBACKED:
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
