#!/usr/bin/env python3
"""Connect the lithotrophic donor branches with tracked evidence (#183).

The existing record has a connected bioenergetic core plus six two-node donor
islands.  This migration adds six source-backed relations that join the sulfur
and bacterial nitrification branches to that core.  It does not universalize
those donor-specific mechanisms to every lithotroph.

Usage:
    python scripts/connect_lithotrophic_graph.py          # dry run
    python scripts/connect_lithotrophic_graph.py --apply  # write
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET_PATH = Path("data/traits/physiology/lithotrophic.yaml")
TARGET_IDENTIFIER = "METPO:1000649"
TARGET_GRAPH = "lithotrophic_inorganic_donor_energy"
TIMESTAMP = "2026-08-30T20:34:43Z"
CURATOR = "codex"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

NEW_EDGES: tuple[dict[str, Any], ...] = (
    {
        "subject": "sox_multienzyme_system",
        "predicate": "participates in",
        "object": "sulfur_oxidation_process",
        "description": (
            "The Sox multienzyme system is a prominent pathway for oxidation of "
            "reduced sulfur compounds."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/microorganisms11061436",
                "snippet": (
                    "The Sox multienzyme complex, first described using the model "
                    "organism Paracoccus panthotrophus, is widespread in photo- and "
                    "chemotrophic sulfur-oxidizing bacteria and appears to be the "
                    "most prominent sulfur oxidation system"
                ),
                "notes": (
                    "The review identifies the multicomponent Sox system as a "
                    "sulfur-oxidation pathway rather than a single enzyme."
                ),
            }
        ],
        "predicate_id": "biolink:participates_in",
    },
    {
        "subject": "soeabc_sulfite_dehydrogenase",
        "predicate": "participates in",
        "object": "sulfur_oxidation_process",
        "description": (
            "Membrane-bound SoeABC participates in sulfur oxidation by oxidizing "
            "sulfite to sulfate."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/microorganisms11061436",
                "snippet": (
                    "sulfite, which is subsequently oxidized by the activity of the "
                    "membrane-bound protein SoeABC (sulfite dehydrogenase) to sulfate"
                ),
                "notes": (
                    "The review explicitly places SoeABC in the sulfite-to-sulfate "
                    "step of sulfur oxidation."
                ),
            }
        ],
        "predicate_id": "biolink:participates_in",
    },
    {
        "subject": "sox_multienzyme_system",
        "predicate": "feeds electrons into",
        "object": "membrane_electron_transport_chain",
        "description": (
            "Complete Sox-mediated thiosulfate oxidation supplies electrons to "
            "energy-conserving electron transport."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/microorganisms11061436",
                "snippet": (
                    "The yield of the respective reaction is 8 electrons/1 mol of "
                    "thiosulfate for the electron transport systems"
                ),
                "notes": (
                    "The review quantifies the electrons supplied by complete Sox "
                    "thiosulfate oxidation to electron-transport systems."
                ),
            }
        ],
        "predicate_id": "METPO:2007402",
    },
    {
        "subject": "ammonia_monooxygenase",
        "predicate": "produces",
        "object": "hydroxylamine",
        "description": (
            "In bacterial ammonia oxidation, ammonia monooxygenase converts ammonia "
            "to hydroxylamine."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.185.9.2759-2773.2003",
                "snippet": "NH3 + O2 + 2H+ + 2e− → NH2OH + H2O",
                "notes": (
                    "The primary N. europaea genome paper gives the AMO-catalyzed "
                    "first reaction of ammonia oxidation explicitly."
                ),
            }
        ],
        "predicate_id": "METPO:2007800",
    },
    {
        "subject": "hydroxylamine_oxidoreductase",
        "predicate": "produces",
        "object": "nitrite",
        "description": (
            "In the bacterial branch represented here, hydroxylamine oxidoreductase "
            "oxidizes hydroxylamine to nitrite."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.185.9.2759-2773.2003",
                "snippet": "NH2OH + H2O → NO2− + 5H+ + 4e−",
                "notes": (
                    "The primary N. europaea paper gives the HAO-associated second "
                    "reaction; the graph scope does not project this bacterial route "
                    "onto ammonia-oxidizing archaea."
                ),
            }
        ],
        "predicate_id": "METPO:2007800",
    },
    {
        "subject": "hydroxylamine_oxidoreductase",
        "predicate": "feeds electrons into",
        "object": "membrane_electron_transport_chain",
        "description": (
            "Electrons released during hydroxylamine oxidation enter the respiratory "
            "electron-transport chain through cytochromes and ubiquinone."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/jb.185.9.2759-2773.2003",
                "snippet": (
                    "Electrons from hydroxylamine oxidation flow through cytochrome "
                    "c554 and cytochrome cm552 into the electron transport chain at "
                    "the level of ubiquinone"
                ),
                "notes": (
                    "The primary N. europaea study directly connects the HAO branch "
                    "to membrane electron transport."
                ),
            }
        ],
        "predicate_id": "METPO:2007402",
    },
)


def _edge_key(edge: dict[str, Any]) -> tuple[Any, Any, Any]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def transform(doc: dict[str, Any]) -> bool:
    """Add the exact six connecting edges; return false if already applied."""
    if doc.get("identifier") != TARGET_IDENTIFIER:
        raise ValueError(f"target identifier is not {TARGET_IDENTIFIER}")

    graphs = [
        graph
        for graph in doc.get("causal_graphs") or []
        if graph.get("graph_id") == TARGET_GRAPH
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected exactly one graph {TARGET_GRAPH}")
    graph = graphs[0]
    node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    required_nodes = {
        endpoint
        for edge in NEW_EDGES
        for endpoint in (edge["subject"], edge["object"])
    }
    missing_nodes = sorted(required_nodes - node_ids)
    if missing_nodes:
        raise ValueError(f"graph is missing required nodes: {missing_nodes}")

    edges = graph.setdefault("edges", [])
    by_key = {_edge_key(edge): edge for edge in edges}
    exact_present = [by_key.get(_edge_key(edge)) == edge for edge in NEW_EDGES]
    if all(exact_present):
        return False
    for new_edge, exact in zip(NEW_EDGES, exact_present, strict=True):
        key = _edge_key(new_edge)
        if key in by_key and not exact:
            raise ValueError(f"refusing to overwrite changed edge {key}")
    if any(exact_present):
        raise ValueError("only some connecting edges are present; refusing partial replay")

    edges.extend(dict(edge) for edge in NEW_EDGES)
    record_curation_event(
        doc,
        curator=CURATOR,
        action=ACTION,
        changes=(
            "Connected the seven lithotrophic graph components with six tracked, "
            "snippet-backed relations. Sox and SoeABC now join the sulfur-oxidation "
            "branch to electron transport; the explicitly bacterial AMO-HAO branch "
            "now joins ammonia, hydroxylamine, nitrite, NXR, and electron transport. "
            "No new paid research was commissioned (#183, #426)."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    path = REPO_ROOT / TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    changed = transform(doc)
    if not changed:
        print("lithotrophic graph is already connected; no change")
        return 0

    if write:
        write_validated_trait(doc, path)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            write_validated_trait(doc, Path(tmp) / TARGET_PATH.name)

    mode = "applied" if write else "dry run"
    print(f"{mode}: added 6 connecting edges to {TARGET_PATH}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write; default is dry run")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    sys.exit(main())
