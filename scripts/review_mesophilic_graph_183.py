#!/usr/bin/env python3
"""Review broad mesophilic graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_mesophilic_graph_183.py
    python scripts/review_mesophilic_graph_183.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "environment/mesophilic"
GRAPH_ID = "mesophilic_homoviscous_adaptation"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T00:40:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "temperature_decrease",
            "predicate": "increases",
            "object": "unsaturated_fatty_acids",
            "description": (
                "Temperature downshift increases membrane unsaturated fatty acid "
                "content (homeoviscous adaptation)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": (
                        "Low-temperature adaptation includes increased "
                        "unsaturation of membrane acyl chains; broad bacterial "
                        "homeoviscous adaptation."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "temperature_decrease",
            "predicate": "increases",
            "object": "unsaturated_fatty_acids",
            "description": (
                "Temperature downshift increases membrane unsaturated fatty acid "
                "content through homeoviscous adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "snippet": "production of double bonds in lipids",
                    "notes": (
                        "Verified against the Ramón et al. cold-adaptation review; "
                        "low-temperature adaptation includes membrane-composition "
                        "remodeling through lipid double-bond production."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "cold_shock",
            "predicate": "induces",
            "object": "cspa",
            "description": "Cold shock induces the cold-shock protein CspA.",
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "Cold shock responses include induction of Csp proteins, "
                        "notably CspA (~15% of protein synthesis after cold shock)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cold_shock",
            "predicate": "positively regulates",
            "object": "cspa",
            "description": "Cold shock strongly increases CspA cold-shock protein synthesis.",
            "evidence": [
                {
                    "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                    "snippet": "more than 10% of the total cellular protein synthesis",
                    "notes": (
                        "Verified against the open Molecular Microbiology full "
                        "text; CspA is the major E. coli cold-shock protein and "
                        "its synthesis rises sharply after temperature downshift."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "cspa",
            "predicate": "promotes",
            "object": "translation",
            "description": (
                "CspA acts as an RNA chaperone preventing RNA secondary structure, "
                "promoting translation during cold shock."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "CspA binds/unwinds RNA to promote single-strandedness and "
                        "translation during cold shock."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "cspa",
            "predicate": "promotes",
            "object": "translation",
            "description": (
                "CspA RNA chaperone activity destabilizes inhibitory mRNA "
                "secondary structures, promoting translation during cold shock."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                    "snippet": "facilitates translation by destabilizing mRNA secondary structures",
                    "notes": (
                        "Verified against the open Molecular Microbiology full "
                        "text; CspA acts as an RNA chaperone that counters "
                        "low-temperature mRNA secondary structure."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "heat_shock",
            "predicate": "induces",
            "object": "rpoh_sigma32",
            "description": "Heat shock induces synthesis of sigma-32 (RpoH).",
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "Heat-induced synthesis of sigma-32 (rpoH); canonical "
                        "bacterial heat-shock regulation relevant to mesophiles "
                        "near the upper temperature range."
                    ),
                }
            ],
        },
        "after": {
            "subject": "heat_shock",
            "predicate": "positively regulates",
            "object": "rpoh_sigma32",
            "description": (
                "Heat shock transiently increases cellular sigma-32 (RpoH), the "
                "heat-shock sigma factor."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.183.18.5302-5310.2001",
                    "snippet": (
                        "transient increase in the RpoH level observed upon heat shock"
                    ),
                    "notes": (
                        "Verified against the open Journal of Bacteriology full "
                        "text; E. coli heat-shock induction is regulated by "
                        "increased RpoH translation and transient sigma-32 "
                        "stabilization."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "rpoh_sigma32",
            "predicate": "activates expression of",
            "object": "heat_shock_proteins",
            "description": (
                "Sigma-32 (RpoH) activates production of heat-shock response proteins."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "Heat shock regulation centers on sigma factor RpoH "
                        "(sigma-32) directing heat-shock gene expression."
                    ),
                }
            ],
        },
        "after": {
            "subject": "rpoh_sigma32",
            "predicate": "positively regulates",
            "object": "heat_shock_proteins",
            "description": (
                "Sigma-32 (RpoH) positively regulates heat-shock response protein expression."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.183.18.5302-5310.2001",
                    "snippet": "enhancing transcription of the heat shock genes",
                    "notes": (
                        "Verified against the open Journal of Bacteriology full "
                        "text; RpoH-dependent sigma-32 activity drives "
                        "heat-shock-gene transcription."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "dnak",
            "predicate": "negatively regulates",
            "object": "rpoh_sigma32",
            "description": (
                "DnaK chaperone sequesters sigma-32, negatively regulating its activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "RpoH is controlled by DnaK chaperone sequestration; "
                        "canonical negative regulation in Gram-negative bacteria."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "dnak",
            "predicate": "negatively regulates",
            "object": "rpoh_sigma32",
            "description": (
                "DnaK chaperone activity negatively regulates sigma-32 (RpoH) activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.183.18.5302-5310.2001",
                    "snippet": "negative regulation of RpoH activity",
                    "notes": (
                        "Verified against the open Journal of Bacteriology full "
                        "text; the DnaK chaperone system participates in negative "
                        "control of sigma-32 activity."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{SLUG}: expected exactly one graph, found {len(graphs)}")
    graph = graphs[0]
    if graph.get("graph_id") != GRAPH_ID:
        raise ValueError(f"{SLUG}: expected graph_id {GRAPH_ID!r}")
    if graph.get("scope_status") != "NONMECHANISTIC":
        raise ValueError(f"{SLUG}: expected a NONMECHANISTIC graph")
    return graph


def _replacements_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_edges(
    graph: dict[str, Any],
    expected_by_key: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
    state: str,
) -> None:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    missing = set(expected_by_key) - set(existing_by_key)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} edge(s): {sorted(missing)}")
    for key, expected in expected_by_key.items():
        if existing_by_key[key] != expected:
            raise ValueError(f"{SLUG}: {state} edge drifted: {key}")


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_edges = _replacements_by_state("before")
    after_edges = _replacements_by_state("after")
    migrated_keys = set(after_edges) - set(before_edges)
    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_keys = existing_keys & migrated_keys

    if _has_exact_edges(graph, after_edges):
        return False

    if present_migrated_keys == migrated_keys:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_keys:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_keys)}")

    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["edges"] = [
        copy.deepcopy(after_by_before_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the broad mesophilic_homoviscous_adaptation graph for "
            "issue #183: added snippets to 6 edge-level evidence items and "
            "regrounded 3 heat/cold shock response edges from legacy free-text "
            "predicates to RO:0002213 positive regulation. No paid research "
            "service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    path = REPO_ROOT / "data" / "traits" / f"{SLUG}.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if transform(SLUG, doc):
        changed = 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
