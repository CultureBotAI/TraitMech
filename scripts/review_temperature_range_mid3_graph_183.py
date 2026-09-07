#!/usr/bin/env python3
"""Review temperature-range-mid3 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_range_mid3_graph_183.py
    python scripts/review_temperature_range_mid3_graph_183.py --apply
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

SLUG = "environment/temperature_range_mid3"
GRAPH_ID = "temperature_range_mid3_upper_mesophile"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T04:00:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "membrane_order",
            "predicate": "drives",
            "object": "desk_kinase_state",
            "description": (
                "Increased membrane order (reduced fluidity) drives DesK to a "
                "kinase-dominant state; membrane physical state is the proximate "
                "signal."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00069-23",
                    "notes": (
                        "increased membrane order (reduced fluidity) drives DesK "
                        "to a kinase-dominant state"
                    ),
                }
            ],
        },
        "after": {
            "subject": "membrane_order",
            "predicate": "positively regulates",
            "object": "desk_kinase_state",
            "description": (
                "Increased membrane order (reduced fluidity) promotes the DesK "
                "kinase-dominant state; membrane physical state is the proximate "
                "signal."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "snippet": "kinase-dominant state of DesK",
                    "notes": (
                        "Verified against the open Sidarta et al. introduction; "
                        "the current Des model links temperature-decrease-driven "
                        "membrane rigidification/thickening to the active "
                        "kinase-dominant state."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "desk",
            "predicate": "phosphorylates",
            "object": "desr",
            "description": (
                "Core two-component signaling step linking membrane physical state "
                "to transcriptional response."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "notes": "DesK autophosphorylates (His188) and phosphorylates DesR",
                }
            ],
        },
        "after": {
            "subject": "desk",
            "predicate": "positively regulates",
            "object": "desr",
            "description": (
                "DesK controls DesR phosphorylation in the core two-component "
                "signaling step linking membrane physical state to transcriptional "
                "response."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "snippet": "phosphorylating or dephosphorylating DesR",
                    "notes": (
                        "Verified against the open Sidarta et al. introduction; "
                        "DesK is described as a membrane-associated histidine "
                        "kinase that phosphorylates or dephosphorylates DesR "
                        "in a temperature-dependent manner."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "phospho_desr",
            "predicate": "activates transcription of",
            "object": "des_gene",
            "description": (
                "DesR-P tetramerizes, binds the des promoter and induces lipid "
                "desaturation to restore membrane fluidity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "notes": "P-DesR tetramerizes, binds Pdes, and activates des expression",
                }
            ],
        },
        "after": {
            "subject": "phospho_desr",
            "predicate": "positively regulates",
            "object": "des_gene",
            "description": (
                "DesR-P tetramerizes, binds the des promoter, and positively "
                "regulates des expression for lipid desaturation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "snippet": "activating expression of the des gene",
                    "notes": (
                        "Verified against the open Sidarta et al. introduction; "
                        "phosphorylated DesR tetramers bind Pdes and activate "
                        "des transcription."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "des_gene",
            "predicate": "introduces double bonds into",
            "object": "membrane_fatty_acyl_chains",
            "description": (
                "Des-mediated unsaturation fluidizes the membrane and reduces bilayer thickness."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "notes": (
                        "Des introduces double bonds into fatty acyl chains, "
                        "fluidizing the membrane and reducing thickness"
                    ),
                }
            ],
        },
        "after": {
            "subject": "des_gene",
            "predicate": "regulates",
            "object": "membrane_fatty_acyl_chains",
            "description": (
                "Des-mediated unsaturation regulates membrane fatty acyl chains, "
                "fluidizing the membrane and reducing bilayer thickness."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "snippet": "desaturates the fatty acyl chains",
                    "notes": (
                        "Verified against the open Sidarta et al. introduction; "
                        "Des desaturates membrane-lipid fatty acyl chains as the "
                        "effector of the DesK/DesR temperature-sensing system."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "temperature_decrease",
            "predicate": "causes",
            "object": "membrane_rigidity",
            "description": (
                "General physical trigger underlying homeoviscous adaptation across microbes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": (
                        "membrane rigidification and increased thickness are "
                        "proposed as sensing signals that trigger adaptive responses"
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "temperature_decrease",
            "predicate": "causes",
            "object": "membrane_rigidity",
            "description": (
                "A temperature decrease causes membrane rigidification and increased "
                "thickness, a physical trigger for homeoviscous adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/spectrum.03925-23",
                    "snippet": "rigidification and concomitant thickening",
                    "notes": (
                        "Verified against the open Sidarta et al. introduction; "
                        "temperature decrease is described as causing cell-membrane "
                        "rigidification and thickening."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "homeoviscous_adaptation",
            "predicate": "maintains",
            "object": "liquid_crystalline_membrane",
            "description": (
                "Broad mechanism relevant to upper-mesophile growth: cells preserve "
                "membrane function across temperature fluctuations."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": "maintain the liquid-crystalline phase at low temperature",
                }
            ],
        },
        "after": {
            "subject": "homeoviscous_adaptation",
            "predicate": "contributes to",
            "object": "liquid_crystalline_membrane",
            "description": (
                "Homeoviscous adaptation contributes to a functional "
                "liquid-crystalline membrane state at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "snippet": "maintain the liquid crystalline phase",
                    "notes": (
                        "Verified against the open Ramón et al. review; organisms "
                        "in cold environments are described as adapting their "
                        "membrane composition to maintain a liquid-crystalline "
                        "state."
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
            "Reviewed the temperature_range_mid3_upper_mesophile graph for issue "
            "#183: added snippets to 6 edge-level evidence items and grounded the "
            "DesK/DesR thermosensing predicates to RO:0002213, RO:0002211, or "
            "RO:0002326. No paid research service was called."
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
