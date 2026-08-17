#!/usr/bin/env python3
"""Check that every `discussions[].attaches_to` anchor resolves (#409).

`attaches_to` is free-form by design -- each Mech anchors into its own record
shape -- so nothing in the schema can check that `causal_graphs#foo` names a
node that exists. That makes the anchors decorative: rename a node in a
migration and the discussion silently points at nothing, with no error anywhere.
This audit closes that, and is the reason it was safe to anchor the ten curated
gaps to node ids rather than leaving them unanchored.

Defects:

  UNRESOLVED_ANCHOR (ERROR)   `<section>#<anchor>` where the section exists in
                              this record but nothing in it carries that id.
  UNKNOWN_ANCHOR_SECTION (WARN)
                              A section this audit does not know how to resolve.
                              WARN, not ERROR: a Mech may legitimately anchor
                              into a section this script has never seen, and
                              failing those would punish the free-form design
                              rather than the mistake it is meant to catch.
  MALFORMED_ANCHOR (ERROR)    Not in `<section>#<anchor>` form at all.

Sections are resolved by the ids they actually contain, so a record with no
causal graphs cannot accidentally pass an anchor into one.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")


def causal_graph_anchors(doc: dict) -> set[str]:
    """Every id a `causal_graphs#...` anchor may legitimately name.

    Both node ids and graph ids: a discussion about a whole mechanism should be
    able to anchor to the graph rather than to an arbitrary node inside it.
    """
    anchors: set[str] = set()
    for graph in doc.get("causal_graphs") or []:
        if graph.get("graph_id"):
            anchors.add(graph["graph_id"])
        for node in graph.get("nodes") or []:
            if node.get("node_id"):
                anchors.add(node["node_id"])
    return anchors


def _ids(doc: dict, section: str, key: str) -> set[str]:
    return {
        item[key] for item in (doc.get(section) or []) if isinstance(item, dict) and item.get(key)
    }


# Sections this audit knows how to resolve, and where each keeps its ids.
RESOLVERS = {
    "causal_graphs": causal_graph_anchors,
    "ontology_mapping": lambda doc: _ids(doc, "ontology_mapping", "mapped_id"),
    "ecological_interactions": lambda doc: _ids(doc, "ecological_interactions", "interaction_id"),
    "discussions": lambda doc: _ids(doc, "discussions", "discussion_id"),
}


def anchor_rows(source: Path | Corpus = DEFAULT_TRAITS) -> list[tuple[str, str, str, str]]:
    """Return (file, discussion_id, defect, detail) for every bad anchor."""
    rows: list[tuple[str, str, str, str]] = []
    for rel, doc in _as_corpus(source):
        for disc in doc.get("discussions") or []:
            did = disc.get("discussion_id", "?")
            for anchor in disc.get("attaches_to") or []:
                if "#" not in anchor:
                    rows.append((rel, did, "MALFORMED_ANCHOR", f"{anchor} expected <section>#<id>"))
                    continue
                section, _, target = anchor.partition("#")
                resolver = RESOLVERS.get(section)
                if resolver is None:
                    rows.append((rel, did, "UNKNOWN_ANCHOR_SECTION", f"{anchor} section={section}"))
                    continue
                if target not in resolver(doc):
                    rows.append((rel, did, "UNRESOLVED_ANCHOR", f"{anchor} no such id in {section}"))
    return rows


ERRORS = {"UNRESOLVED_ANCHOR", "MALFORMED_ANCHOR"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    args = ap.parse_args()

    rows = anchor_rows(args.traits_dir)
    for rel, did, defect, detail in rows:
        print(f"{defect}\t{rel}\t{did}\t{detail}")
    errors = [r for r in rows if r[2] in ERRORS]
    warns = len(rows) - len(errors)
    print(f"discussion anchors: {len(errors)} error(s), {warns} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
