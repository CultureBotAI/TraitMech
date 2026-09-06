#!/usr/bin/env python3
"""Connect the cell_length_large FtsZ/SOS graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_cell_length_large_graph_183.py
    python scripts/connect_cell_length_large_graph_183.py --apply
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
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from connect_morphology_graphs_183 import _components, _edge_key  # noqa: E402
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "morphology/cell_length_large"
GRAPH_ID = "cell_length_large_division_delay"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T00:00:00Z"
EXPECTED_COMPONENTS = 4

GRAPH_METADATA_BEFORE = {
    "title": "Large cell-length from fast growth or division delay",
    "description": (
        "DOI-backed graph linking fast elongation, delayed FtsZ-ring constriction, "
        "or filamentous growth programs to large cell length (>3 μm)."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Large cell-length via FtsZ division delay",
    "description": (
        "DOI-backed graph linking fast elongation, SOS/SulA-mediated FtsZ "
        "inhibition, FtsZ Z-ring control, and delayed constriction to large cell "
        "length (>3 μm)."
    ),
}

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "sos_response",
            "predicate": "induces",
            "object": "sula_division_inhibition",
            "description": (
                "DNA damage/stress activates the SOS program, inducing division "
                "inhibitors that halt septation and promote elongation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1101/2025.05.13.653778",
                    "notes": (
                        "SOS regulon upregulates sulA; SulA prevents Z-ring "
                        "formation and halts division."
                    ),
                }
            ],
        },
        "after": {
            "subject": "sos_response",
            "predicate": "positively regulates",
            "object": "sula_division_inhibition",
            "description": (
                "The SOS response increases SulA-mediated division inhibition "
                "after DNA damage or replication stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1002/advs.202203260",
                    "snippet": "SOS response is activated",
                    "notes": (
                        "Verified against the open Wiley full text; DNA damage "
                        "activates the RecA/LexA SOS response and enables "
                        "expression of SOS regulon genes, including sulA."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "sula_protein",
            "predicate": "inhibits assembly of",
            "object": "ftsz_zring",
            "description": (
                "SulA blocks FtsZ polymerization/assembly, delaying cytokinesis "
                "and allowing continued elongation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1101/2025.05.13.653778",
                    "notes": (
                        "Canonical edge for many bacteria: SulA inhibits FtsZ "
                        "assembly by sequestering monomers, directly blocking "
                        "polymerization."
                    ),
                }
            ],
        },
        "after": {
            "subject": "sula_protein",
            "predicate": "negatively regulates",
            "object": "ftsz_zring",
            "description": "SulA inhibits FtsZ polymerization, blocking productive Z-ring assembly.",
            "evidence": [
                {
                    "reference": "DOI:10.1002/advs.202203260",
                    "snippet": "cell division inhibitor, sulA, blocks FtsZ",
                    "notes": (
                        "Verified against the open Wiley full text; the source "
                        "links SOS activation to SulA blocking FtsZ polymerization."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
    {
        "before": {
            "subject": "ftsz_protein",
            "predicate": "delays",
            "object": "constriction_onset",
            "description": (
                "FtsZ copy number is rate-limiting for division; reduced FtsZ "
                "delays septation and can increase cell length before division."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-54242-w",
                    "notes": (
                        "FtsZ numbers are rate-limiting for cell division; ~20% "
                        "downregulation may delay division."
                    ),
                }
            ],
        },
        "after": {
            "subject": "ftsz_protein",
            "predicate": "positively regulates",
            "object": "constriction_onset",
            "description": (
                "FtsZ accumulation in the Z-ring is a rate-limiting driver for "
                "onset of constriction at faster growth rates."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-54242-w",
                    "snippet": "rate limit the onset of constriction",
                    "notes": (
                        "Verified against the open Nature Communications full "
                        "text; FtsZ numbers were rate-limiting for constriction "
                        "onset in moderately fast E. coli growth."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
]

ADDITIONS: list[dict[str, Any]] = [
    {
        "subject": "sula_protein",
        "predicate": "contributes to",
        "object": "sula_division_inhibition",
        "description": "SOS-induced SulA is the inhibitory protein mediating this division-arrest branch.",
        "evidence": [
            {
                "reference": "DOI:10.1002/advs.202203260",
                "snippet": "cell division inhibitor sulA",
                "notes": (
                    "Verified against the open Wiley full text; the study frames "
                    "SulA as the SOS-linked cell-division inhibitor."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "sula_division_inhibition",
        "predicate": "contributes to",
        "object": "division_timing_delay",
        "description": (
            "SulA-mediated inhibition of septation contributes to delayed "
            "division and continued elongation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1002/advs.202203260",
                "snippet": "contributes to non-septate cellular filamentation",
                "notes": (
                    "Verified against the open Wiley full text; SulA-mediated "
                    "FtsZ inhibition is linked to blocked septation and "
                    "filamentation."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "ftsz_zring",
        "predicate": "positively regulates",
        "object": "constriction_onset",
        "description": (
            "FtsZ bundles promote the FtsA/FtsN/core-divisome transition that starts constriction."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-54242-w",
                "snippet": "starts the onset of constriction",
                "notes": (
                    "Verified against the open Nature Communications full text; "
                    "the proposed model routes FtsZ bundles through FtsA "
                    "antiparallel filaments, FtsN recruitment, and core-divisome "
                    "activation."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
]


def _replacements_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


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


def _assert_graph_metadata(graph: dict[str, Any], expected: dict[str, str], state: str) -> None:
    actual = {field: graph.get(field) for field in expected}
    if actual != expected:
        raise ValueError(f"{SLUG}: {state} graph metadata drifted: {actual!r}")


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
            raise ValueError(f"{SLUG}: {state} connector drifted: {key}")


def _assert_endpoints(graph: dict[str, Any], edges: list[dict[str, Any]]) -> None:
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in edges:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{SLUG}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{SLUG}: connector lacks source/snippet evidence: {key}")


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_by_key = _replacements_by_state("before")
    after_by_key = _replacements_by_state("after")
    addition_by_key = {_edge_key(edge): edge for edge in ADDITIONS}
    migrated_by_key = {**after_by_key, **addition_by_key}

    edges = graph.get("edges") or []
    existing_keys = {_edge_key(edge) for edge in edges}
    before_keys = set(before_by_key)
    migrated_keys = set(migrated_by_key)
    before = _components(graph)

    if before == 1 and not (existing_keys & before_keys):
        _assert_graph_metadata(graph, GRAPH_METADATA_AFTER, "migrated")
        _assert_exact_edges(graph, migrated_by_key, "migrated")
        return False

    _assert_graph_metadata(graph, GRAPH_METADATA_BEFORE, "source")
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")
    if existing_keys & migrated_keys:
        raise ValueError(
            f"{SLUG}: partial connector replay: {sorted(existing_keys & migrated_keys)}"
        )
    _assert_exact_edges(graph, before_by_key, "source")
    _assert_endpoints(graph, list(migrated_by_key.values()))

    replacement_after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph.update(GRAPH_METADATA_AFTER)
    graph["edges"] = [
        copy.deepcopy(replacement_after_by_before_key.get(_edge_key(edge), edge)) for edge in edges
    ]
    graph["edges"].extend(copy.deepcopy(ADDITIONS))

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{SLUG}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            "by re-citing the SOS/SulA branch to peer-reviewed evidence, grounding "
            "the two residual FtsZ/SulA predicates, and adding 3 source- and "
            "verbatim-snippet-backed connectors. No paid research service was called."
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
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
