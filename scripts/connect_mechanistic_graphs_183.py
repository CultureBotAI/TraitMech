#!/usr/bin/env python3
"""Connect the first remaining mechanistic graph tranche for issue #183.

All connector evidence was already captured in the tracked deep-research reports.
The restriction-modification change removes a Type IV island because that report
explicitly says modification-dependent restriction is a distinct subtype and must
not be forced into the canonical Types I-III self/non-self mechanism.

Usage:
    python scripts/connect_mechanistic_graphs_183.py
    python scripts/connect_mechanistic_graphs_183.py --apply
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

TIMESTAMP = "2026-08-31T05:40:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "ecology/biofilm_formation": [
        {
            "subject": "planktonic_cell",
            "predicate": "participates in",
            "object": "biofilm_formation_process",
            "description": "Attachment of a planktonic cell initiates the biofilm-development process.",
            "evidence": [{
                "reference": "DOI:10.1042/BCJ20210301",
                "snippet": "biofilm formation begins when a planktonic cell attaches to an amenable surface",
                "notes": "The source explicitly places the attachment event at the start of biofilm formation.",
            }],
            "predicate_id": "biolink:participates_in",
        },
        {
            "subject": "biofilm_dispersal",
            "predicate": "negatively regulates",
            "object": "sessile_state",
            "description": "Dispersal is the lifecycle exit from the sessile biofilm state.",
            "evidence": [{
                "reference": "DOI:10.3390/antibiotics13111047",
                "snippet": "one of the key anti-biofilm properties of NO is its ability to induce biofilm dispersal",
                "notes": "The anti-biofilm dispersal claim supports loss of the sessile state, not inhibition of an unrelated pathway.",
            }],
            "predicate_id": "RO:0002212",
        },
    ],
    "genomics/crispr_cas_system": [
        {
            "subject": "crrna_effector_complex",
            "predicate": "contributes to",
            "object": "crispr_trait",
            "description": "crRNA-guided interference by the effector complex realizes the adaptive-defense trait.",
            "evidence": [{
                "reference": "DOI:10.5483/bmbrep.2023-0050",
                "snippet": "Effector-crRNA complexes perform RNA-guided interference against invading targets",
                "notes": "The connector is scoped to the interference branch and does not universalize one effector subtype.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "cas1_cas2_complex",
            "predicate": "confers",
            "object": "crispr_trait",
            "description": "Cas1-Cas2 spacer acquisition realizes the adaptation branch of CRISPR-Cas immunity.",
            "evidence": [{
                "reference": "DOI:10.1038/nsmb.2820",
                "snippet": "Cas1 and Cas2 from Escherichia coli form a stable complex that is essential for spacer acquisition",
                "notes": "The primary study directly tests the Cas1-Cas2 adaptation complex; this branch is not projected onto interference-only systems.",
            }],
            "predicate_id": "METPO:2007700",
        },
    ],
}

REMOVALS = {
    "genomics/restriction_modification_system": {
        "nodes": {"type_iv_restriction_enzyme", "methylated_dna_motif"},
        "edges": {("type_iv_restriction_enzyme", "cleaves", "methylated_dna_motif")},
        "reason": (
            "Removed the explicitly out-of-scope Type IV subtype island; the tracked "
            "report identifies modification-dependent restriction as distinct from "
            "the canonical Types I-III self/non-self mechanism."
        ),
    },
}


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _components(graph: dict[str, Any]) -> int:
    nodes = {node["node_id"] for node in graph.get("nodes") or []}
    adjacency = {node: set() for node in nodes}
    referenced: set[str] = set()
    for edge in graph.get("edges") or []:
        subject, _predicate, object_ = _edge_key(edge)
        if subject in nodes and object_ in nodes:
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
            node = queue.popleft()
            if node in reached:
                continue
            reached.add(node)
            queue.extend(adjacency[node] - reached)
        unseen -= reached
    return count


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    before = _components(graph)
    if before < 2:
        return False

    additions = list(ADDITIONS.get(slug, []))
    removal = REMOVALS.get(slug)
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    existing = {_edge_key(edge) for edge in graph.get("edges") or []}
    for edge in additions:
        key = _edge_key(edge)
        if key in existing:
            raise ValueError(f"{slug}: partial replay at {key}")
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(not item.get("snippet") for item in evidence):
            raise ValueError(f"{slug}: connector lacks verbatim snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)

    if removal:
        present = {_edge_key(edge) for edge in graph.get("edges") or []}
        if not removal["edges"] <= present or not removal["nodes"] <= node_ids:
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
            + (
                f"using {len(additions)} snippet-backed connector(s) supported by "
                "source passages. "
                if additions else ""
            )
            + (f"{removal['reason']} " if removal else "")
            + "No research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    slugs = sorted(set(ADDITIONS) | set(REMOVALS))
    changed = 0
    for slug in slugs:
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
