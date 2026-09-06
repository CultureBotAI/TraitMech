#!/usr/bin/env python3
"""Review obligately-piezophilic graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_obligately_piezophilic_graph_183.py
    python scripts/review_obligately_piezophilic_graph_183.py --apply
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

SLUG = "environment/obligately_piezophilic"
GRAPH_ID = "obligate_piezophily_high_pressure_requirement"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T08:20:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "obligate_hhp",
            "predicate": "causes",
            "object": "obligate_piezophilic_trait",
            "description": (
                "HHP adaptation that no longer functions at 0.1 MPa makes high "
                "pressure obligatory for growth."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1099/ijsem.0.001671",
                    "notes": (
                        "Colwellia marinimaniae MTCD1 has a growth range of "
                        "80-140 MPa (optimum 120 MPa) and does not grow at "
                        "atmospheric pressure."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "obligate_hhp",
            "predicate": "causes",
            "object": "obligate_piezophilic_trait",
            "description": (
                "HHP adaptation that no longer functions at 0.1 MPa makes high "
                "pressure obligatory for growth."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1099/ijsem.0.001671",
                    "snippet": (
                        "grew at extremely high hydrostatic pressures, with a "
                        "growth range of 80-140 MPa"
                    ),
                    "notes": (
                        "Verified against public Kusube et al. abstract text; "
                        "Colwellia marinimaniae MTCD1 is retained as a "
                        "hyperpiezophilic obligate-HHP exemplar."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "pressure_dependent_machinery",
            "predicate": "confers",
            "object": "obligate_piezophilic_trait",
            "description": (
                "Cellular machinery requiring HHP for function realizes the "
                "obligate-piezophile phenotype."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/srep27289",
                    "notes": (
                        "Pyrococcus yayanosii is an obligate piezophile requiring HHP for growth."
                    ),
                }
            ],
            "predicate_id": "METPO:2007700",
        },
        "after": {
            "subject": "pressure_dependent_machinery",
            "predicate": "confers",
            "object": "obligate_piezophilic_trait",
            "description": (
                "Cellular machinery requiring HHP for function realizes the "
                "obligate-piezophile phenotype."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/srep27289",
                    "snippet": (
                        "hydrostatic pressure-responsive genes involved in "
                        "translation, chemotaxis, energy metabolism"
                    ),
                    "notes": (
                        "Verified against the open Michoud and Jebbar abstract; "
                        "the edge is kept as a broad cellular-machinery "
                        "dependency in an obligate piezophile."
                    ),
                }
            ],
            "predicate_id": "METPO:2007700",
        },
    },
    {
        "before": {
            "subject": "obligate_piezophilic_trait",
            "predicate": "has characteristic",
            "object": "ambient_pressure_growth_failure",
            "description": (
                "The obligate-piezophile phenotype is defined by inability to "
                "grow at ambient pressure (0.1 MPa)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41396-021-00930-0",
                    "notes": (
                        "Obligate piezophiles (or hyperpiezophiles) are unable "
                        "to grow at ambient pressure (0.1 MPa)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "ambient_pressure_growth_failure",
            "predicate": "manifests as",
            "object": "obligate_piezophilic_trait",
            "description": (
                "Inability to grow at 0.1 MPa is the diagnostic pressure-growth "
                "failure state represented by obligate piezophily."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41396-021-00930-0",
                    "snippet": (
                        "obligate piezophiles (or hyperpiezophiles) unable to "
                        "grow at ambient pressure"
                    ),
                    "notes": (
                        "Verified against public Scoma et al. text; the edge is "
                        "reversed from ungrounded trait-to-quality wording to a "
                        "grounded manifestation relation."
                    ),
                }
            ],
            "predicate_id": "METPO:2007400",
        },
    },
    {
        "before": {
            "subject": "obligate_hhp",
            "predicate": "increases amount of",
            "object": "membrane_unsaturated_branched_lipids",
            "description": (
                "Elevated hydrostatic pressure increases the requirement for and "
                "abundance of unsaturated/branched-chain membrane lipids."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "notes": (
                        "The abundance of specific membrane lipids, such as "
                        "those containing unsaturated and branched-chain fatty "
                        "acids, rises with increasing HHP across marine "
                        "piezophiles."
                    ),
                }
            ],
        },
        "after": {
            "subject": "obligate_hhp",
            "predicate": "increases",
            "object": "membrane_unsaturated_branched_lipids",
            "description": (
                "Elevated hydrostatic pressure increases the requirement for and "
                "abundance of unsaturated/branched-chain membrane lipids."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "snippet": (
                        "specific membrane lipids, such as those containing "
                        "unsaturated and branched-chain fatty acids, rises with "
                        "increasing HHP"
                    ),
                    "notes": (
                        "Verified against the open Tamby et al. abstract; the "
                        "edge is retained as a broad pressure-associated lipid "
                        "adaptation, not a universal claim for all piezophiles."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "membrane_unsaturated_branched_lipids",
            "predicate": "enables",
            "object": "membrane_fluidity_maintenance",
            "description": (
                "Unsaturated/branched-chain lipids maintain membrane fluidity "
                "under HHP (homeoviscous adaptation)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "notes": (
                        "Membrane lipid adaptation (unsaturated/branched fatty "
                        "acids) is a homeoviscous response maintaining membrane "
                        "fluidity under high hydrostatic pressure."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "membrane_unsaturated_branched_lipids",
            "predicate": "enables",
            "object": "membrane_fluidity_maintenance",
            "description": (
                "Unsaturated/branched-chain lipids maintain membrane fluidity "
                "under HHP (homeoviscous adaptation)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "snippet": "can be adapted by modifying the degree of lipid packing",
                    "notes": (
                        "Verified against the open Tamby et al. introduction; "
                        "membrane unsaturation and branching are retained as "
                        "contextual ways to remodel lipid packing under HHP."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "membrane_fluidity_maintenance",
            "predicate": "contributes to",
            "object": "pressure_dependent_machinery",
            "description": (
                "Maintained membrane fluidity supports the pressure-dependent "
                "cellular machinery underlying obligate piezophily."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "notes": (
                        "Membrane fluidity maintenance via lipid adaptation "
                        "underlies the pressure-adapted membrane systems of "
                        "piezophiles."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "membrane_fluidity_maintenance",
            "predicate": "contributes to",
            "object": "pressure_dependent_machinery",
            "description": (
                "Maintained membrane fluidity supports the pressure-dependent "
                "cellular machinery underlying obligate piezophily."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmolb.2022.1058381",
                    "snippet": (
                        "HHP impacts protein folding, metabolic rate, and "
                        "membrane stability, leading to cell disruption"
                    ),
                    "notes": (
                        "Verified against the open Tamby et al. introduction; "
                        "the edge is retained as a high-level bridge from "
                        "homeoviscous adaptation to HHP-dependent machinery."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
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


def _edges_by_state(
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
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    if _has_exact_edges(graph, after_edges):
        return False

    if present_migrated_edge_keys == migrated_edge_keys:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys:
        raise ValueError(
            f"{SLUG}: partial evidence replay: edges={sorted(present_migrated_edge_keys)}"
        )

    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the obligate_piezophily_high_pressure_requirement graph "
            "for issue #183: added exact snippets to 6 causal-edge evidence "
            "items and grounded 2 residual predicates. No paid research "
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
