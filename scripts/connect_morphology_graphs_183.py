#!/usr/bin/env python3
"""Connect the first morphology graph tranche for issue #183.

The three connector passages were verified against openly available source text.
The flagellar stator island is removed rather than forced into a structural trait:
the tracked report explicitly distinguishes possession of an assembled flagellum
from ion-driven motor activity.

Usage:
    python scripts/connect_morphology_graphs_183.py
    python scripts/connect_morphology_graphs_183.py --apply
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from collections import deque
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-31T06:15:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

EXPECTED_COMPONENTS = {
    "morphology/brown_pigmented": 2,
    "morphology/ellipsoidal": 2,
    "morphology/flagellated": 3,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "morphology/brown_pigmented": [{
        "subject": "homogentisic_acid",
        "predicate": "converted to",
        "object": "maleylacetoacetate",
        "description": (
            "HmgA converts homogentisic acid to maleylacetoacetate, diverting "
            "substrate away from pyomelanin formation."
        ),
        "evidence": [{
            "reference": "DOI:10.1128/spectrum.00410-24",
            "snippet": "converts HGA to maleylacetoacetate",
            "notes": (
                "Verified against the open primary article; this joins the HmgA "
                "catabolic branch to its homogentisate substrate."
            ),
        }],
    }],
    "morphology/ellipsoidal": [{
        "subject": "septal_pg_synthesis",
        "predicate": "part of",
        "object": "combined_septal_peripheral",
        "description": (
            "Septal peptidoglycan synthesis is one arm of the simultaneous septal "
            "and peripheral synthesis program at ovococcal midcell."
        ),
        "evidence": [{
            "reference": "DOI:10.1111/mmi.14659",
            "snippet": (
                "septal and peripheral (elongation) PG synthesis occur "
                "simultaneously at midcell"
            ),
            "notes": (
                "Verified against the open primary article abstract; the connector "
                "does not imply that the two synthesis machines are identical."
            ),
        }],
        "predicate_id": "biolink:part_of",
    }],
    "morphology/flagellated": [{
        "subject": "flagellar_structural_subunits",
        "predicate": "contributes to",
        "object": "flagellar_filament",
        "description": (
            "Exported flagellin structural subunits assemble to form the flagellar "
            "filament that realizes the morphology."
        ),
        "evidence": [{
            "reference": "DOI:10.3390/biom11020186",
            "snippet": (
                "Around 20,000 subunits of flagellin assemble to form the "
                "flagellar filament"
            ),
            "notes": (
                "Verified against the open review full text; this connects the "
                "exported-subunit module to the assembled structural filament."
            ),
        }],
        "predicate_id": "RO:0002326",
    }],
}

REMOVALS = {
    "morphology/flagellated": {
        "nodes": {"ion_motive_force", "proton_channel", "stator_complex"},
        "edges": {
            ("ion_motive_force", "powers", "stator_complex"),
            ("stator_complex", "has function", "proton_channel"),
        },
        "reason": (
            "Removed the isolated stator/ion-channel branch because the tracked "
            "report explicitly scopes flagellated to appendage possession and says "
            "stator activity is not required for that structural state."
        ),
    },
}


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _components(graph: dict[str, Any]) -> int:
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    adjacency = {node_id: set() for node_id in node_ids}
    referenced: set[str] = set()
    for edge in graph.get("edges") or []:
        subject, _predicate, object_ = _edge_key(edge)
        if subject in node_ids and object_ in node_ids:
            adjacency[subject].add(object_)
            adjacency[object_].add(subject)
            referenced.update((subject, object_))

    unseen = set(referenced)
    count = 0
    while unseen:
        count += 1
        queue = deque([next(iter(unseen))])
        reached: set[str] = set()
        while queue:
            node_id = queue.popleft()
            if node_id in reached:
                continue
            reached.add(node_id)
            queue.extend(adjacency[node_id] - reached)
        unseen -= reached
    return count


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    removal = REMOVALS.get(slug)
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    expected_by_key = {_edge_key(edge): edge for edge in additions}
    present = set(existing_by_key) & set(expected_by_key)
    removed = bool(removal) and not (
        removal["nodes"] & {node["node_id"] for node in graph.get("nodes") or []}
    )

    before = _components(graph)
    if before == 1:
        if present != set(expected_by_key) or (removal and not removed):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        for key, expected in expected_by_key.items():
            if existing_by_key[key] != expected:
                raise ValueError(f"{slug}: connector drifted after migration: {key}")
        return False
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(
            f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}"
        )
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")

    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{slug}: connector lacks source/snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)

    if removal:
        edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
        if not removal["nodes"] <= node_ids or not removal["edges"] <= edge_keys:
            raise ValueError(f"{slug}: removal target drifted")
        graph["edges"] = [
            edge for edge in graph["edges"] if _edge_key(edge) not in removal["edges"]
        ]
        graph["nodes"] = [
            node for node in graph["nodes"] if node["node_id"] not in removal["nodes"]
        ]

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{slug}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            f"using {len(additions)} source- and verbatim-snippet-backed connector(s). "
            + (f"{removal['reason']} " if removal else "")
            + "No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    for slug in sorted(ADDITIONS):
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not transform(slug, doc):
            continue
        changed += 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
