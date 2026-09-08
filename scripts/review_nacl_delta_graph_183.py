#!/usr/bin/env python3
"""Review NaCl-delta graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_nacl_delta_graph_183.py
    python scripts/review_nacl_delta_graph_183.py --apply
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

SLUG = "environment/nacl_delta"
GRAPH_ID = "nacl_delta_euryhaline_breadth"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T07:20:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "compatible_solute_accumulation",
            "predicate": "enables",
            "object": "osmoadaptation",
            "description": (
                "Accumulation of neutral compatible solutes enables osmoadaptation "
                "and broader salt-supported growth."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/MMBR.00181-23",
                    "notes": (
                        "To avoid K+-induced cytotoxicity and high ionic strength, "
                        "cells accumulate or synthesize neutral compatible solutes "
                        "(glycine betaine, trehalose, ectoine, proline)."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "compatible_solute_accumulation",
            "predicate": "enables",
            "object": "osmoadaptation",
            "description": (
                "Compatible-solute uptake or synthesis enables osmoadaptation "
                "after an osmotic upshift."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pgen.1007574",
                    "snippet": (
                        "secondary response involving uptake or synthesis of compatible solutes"
                    ),
                    "notes": (
                        "Verified against the open Pham et al. introduction; "
                        "compatible-solute uptake and synthesis are retained as "
                        "a broad bacterial osmotic-upshift response."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "hyperosmotic_upshift",
            "predicate": "causes",
            "object": "potassium_uptake",
            "description": (
                "Hyperosmotic upshift triggers rapid K+ import as an early osmoadaptive response."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/MMBR.00181-23",
                    "notes": (
                        "Cells import large amounts of K+ during osmotic upshift; "
                        "potassium is the principal cytoplasmic cation."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "hyperosmotic_upshift",
            "predicate": "causes",
            "object": "potassium_uptake",
            "description": (
                "Hyperosmotic upshift triggers rapid K+ import as an early osmoadaptive response."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pgen.1007574",
                    "snippet": (
                        "In response to an osmotic upshift (hyperosmotic stress), "
                        "bacteria import potassium ions"
                    ),
                    "notes": (
                        "Verified against the open Pham et al. introduction; "
                        "K+ uptake is retained as the immediate bacterial "
                        "response to hyperosmotic stress."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "potassium_uptake",
            "predicate": "contributes to",
            "object": "osmoadaptation",
            "description": (
                "K+ accumulation is a core early osmoadaptive response to increased NaCl."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/MMBR.00181-23",
                    "notes": (
                        "Cytoplasmic K+ levels ~250 mM (E. coli) to ~500 mM "
                        "(C. glutamicum, L. lactis) accumulate as a core "
                        "osmoadaptive response."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "potassium_uptake",
            "predicate": "contributes to",
            "object": "osmoadaptation",
            "description": (
                "K+ accumulation is a core early osmoadaptive response to increased NaCl."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pgen.1007574",
                    "snippet": (
                        "This allows the cell to limit the loss of water and maintain turgor"
                    ),
                    "notes": (
                        "Verified against the open Pham et al. introduction; "
                        "the early K+ import and later compatible-solute "
                        "response are framed as limiting water loss and "
                        "maintaining turgor."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "salt_out_strategy",
            "predicate": "uses",
            "object": "compatible_solute_accumulation",
            "description": (
                "The salt-out strategy relies on accumulation of organic compatible solutes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "notes": (
                        "Salt-out excludes Na+ while accumulating organic compatible "
                        "solutes like sugars, polyalcohols, ectoine, trehalose, "
                        "glycine-betaine."
                    ),
                }
            ],
        },
        "after": {
            "subject": "compatible_solute_accumulation",
            "predicate": "part of",
            "object": "salt_out_strategy",
            "description": (
                "Compatible-solute import or synthesis is part of the salt-out "
                "osmoadaptation strategy."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "snippet": (
                        "The second phase starts with the import or de novo "
                        "synthesis of the compatible solute"
                    ),
                    "notes": (
                        "Verified against public Bonnaud et al. text; the edge "
                        "is reversed to ground the component-process relation."
                    ),
                }
            ],
            "predicate_id": "biolink:part_of",
        },
    },
    {
        "before": {
            "subject": "salt_in_strategy",
            "predicate": "supports",
            "object": "high_maximal_nacl_tolerance",
            "description": (
                "The salt-in strategy supports very high maximal salinity tolerance, "
                "extending the upper NaCl limit."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "notes": (
                        "Salt-out is energetically costly and less suited to "
                        "saturating salinities; salt-in is favored at very high salt."
                    ),
                }
            ],
        },
        "after": {
            "subject": "salt_in_strategy",
            "predicate": "contributes to",
            "object": "high_maximal_nacl_tolerance",
            "description": (
                "The salt-in strategy contributes to growth under very high ambient "
                "NaCl in haloarchaeal lineages."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "snippet": (
                        "haloarchaea favors the salt-in strategy at high salt "
                        "concentrations in the medium"
                    ),
                    "notes": (
                        "Verified against public Bonnaud et al. text; salt-in is "
                        "retained as a high-salt osmoadaptation strategy, not as "
                        "a direct determinant of an exact NaCl-delta interval."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "mechanosensitive_channels",
            "predicate": "protects against",
            "object": "hypoosmotic_shock",
            "description": (
                "Mechanosensitive channels act as safety valves protecting cells "
                "against sudden hypoosmotic shocks at the low-salinity end of the range."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "notes": (
                        "Mechanosensitive (Msc) channels and compatible-solute "
                        "efflux systems act as safety valves during sudden "
                        "hypoosmotic shocks."
                    ),
                }
            ],
        },
        "after": {
            "subject": "mechanosensitive_channels",
            "predicate": "mitigates",
            "object": "hypoosmotic_shock",
            "description": (
                "Mechanosensitive channels mitigate turgor stress during sudden "
                "hypoosmotic shocks at the low-salinity end of the range."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12081738",
                    "snippet": "mechanosensitive channels, which serve as safety valves",
                    "notes": (
                        "Verified against public Bonnaud et al. text; the broad "
                        "MscL/MscS label is kept reviewed-label-only in this "
                        "nonmechanistic quantitative graph."
                    ),
                }
            ],
            "predicate_id": "METPO:2007407",
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
            "Reviewed the nacl_delta_euryhaline_breadth graph for issue #183: "
            "added exact snippets to 6 causal-edge evidence items, grounded 3 "
            "residual predicates, and preserved the graph as a nonmechanistic "
            "quantitative NaCl-range-breadth classification. No paid research "
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
