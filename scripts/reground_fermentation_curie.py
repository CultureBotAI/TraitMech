#!/usr/bin/env python3
"""Repair the fermentation grounding in chemoorganoheterotrophic.yaml (#391).

`fermentation` appears as a causal-graph node in five records. Four agree it is
fermentation; one grounds it to a different concept entirely:

    BIOLOGICAL_PROCESS  GO:0006113     substrate_level_phosphorylation.yaml
    BIOLOGICAL_PROCESS  GO:0006113     chemoorganotrophic.yaml
    BIOLOGICAL_PROCESS  GO:0006113     heterotrophic.yaml
    BIOLOGICAL_PROCESS  METPO:1002005  chemoheterotrophic.yaml
    BIOLOGICAL_PROCESS  METPO:1000845  chemoorganoheterotrophic.yaml   <- WRONG

METPO:1000845 is **Acetogenesis** — "produces acetate ... through the
reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl
pathway". The node's own description reads "Energy metabolism using organic
electron acceptors and substrate-level phosphorylation", which is fermentation,
not acetogenesis. The likely route in: METPO:1000845 carries the related
synonym "Acetate fermentation", so a synonym match on "fermentation" lands on
it — the same right-sounding-name shape as the #402/#405 repairs.

The replacement is GO:0006113 ("fermentation"), NOT a guess: it is the exact
row `mappings/node_grounding.tsv` already holds for
(fermentation, BIOLOGICAL_PROCESS) — skos:exactMatch, confidence high — and the
grounding eight other records already carry (the six metabolism fermentation
records plus heterotrophic.yaml and chemoorganotrophic.yaml — #504 corrected an
undercount here). `label-correspondence` re-checks the
(id, label) pair in CI.

Deliberately NOT touched:

  - chemoheterotrophic.yaml's METPO:1002005 — a METPO respiration subclass
    whose definition IS fermentation (dbxref GO:0006113, related synonym
    "fermentation"). Defensible, and #391 does not name it as wrong.
  - acetogenesis.yaml's METPO:1000845 — the term used for its actual concept.
  - The five curation_history NOTEs from the #497 tranche that flag this
    disagreement: history is append-only; this pass adds its own event instead.
  - mappings/node_grounding.tsv — no row maps anything to METPO:1000845, so
    there is nothing for `just ground-nodes --apply` to restore (the #405
    lesson does not bite here; confirmed by grep before writing this).

Usage:
    python scripts/reground_fermentation_curie.py           # dry run (default)
    python scripts/reground_fermentation_curie.py --apply   # write
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "chemoorganoheterotrophic.yaml"
NODE_ID = "fermentation"
OLD = "METPO:1000845"
NEW = "GO:0006113"
TIMESTAMP = "2026-08-22T04:30:00Z"
ACTION = "REGROUND_CAUSAL_NODES"
CHANGES = (
    "Repaired a wrong CURIE (issue 391): fermentation: METPO:1000845 -> GO:0006113. "
    "Was METPO:1000845 'Acetogenesis' — a Wood-Ljungdahl acetate-producing "
    "metabolism, while the node describes 'Energy metabolism using organic electron "
    "acceptors and substrate-level phosphorylation', i.e. fermentation. The term's "
    "related synonym 'Acetate fermentation' explains the mismatch. Replaced with "
    "GO:0006113, the (fermentation, BIOLOGICAL_PROCESS) row mappings/"
    "node_grounding.tsv already holds and the grounding eight sibling records "
    "already carry."
)


def apply(write: bool = False) -> int:
    doc = yaml.safe_load(TARGET.read_text())
    hits = 0
    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            if node.get("node_id") == NODE_ID and node.get("grounding") == OLD:
                node["grounding"] = NEW
                hits += 1
                print(f"  reground {TARGET.name} {NODE_ID} {OLD} -> {NEW}")
    if hits != 1:
        print(f"expected exactly 1 node with {OLD}, found {hits}; not writing",
              file=sys.stderr)
        return 1
    record_curation_event(
        doc, curator="claude", action=ACTION, llm_assisted=True,
        timestamp=TIMESTAMP, upsert=True, changes=CHANGES,
    )
    if write:
        write_validated_trait(doc, TARGET)
    print(f"1 node regrounded{'' if write else ' (dry run)'}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="write the change (default is a dry run)")
    return apply(ap.parse_args().apply)


if __name__ == "__main__":
    sys.exit(main())
