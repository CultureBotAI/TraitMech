#!/usr/bin/env python3
"""Review oxidative_stress_response graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_oxidative_stress_response_graph_183.py
    python scripts/review_oxidative_stress_response_graph_183.py --apply
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

SLUG = "physiology/oxidative_stress_response"
GRAPH_ID = "oxidative_stress_response_ros_defense"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T06:40:00Z"

RECORD_EVIDENCE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "reference": "DOI:10.1038/nrmicro3032",
            "notes": (
                "Imlay reviews the molecular mechanisms and physiological "
                "consequences of oxidative stress and the cellular defenses "
                "against reactive oxygen species."
            ),
        },
        "after": {
            "reference": "DOI:10.1038/nrmicro3032",
            "snippet": "scavenging enzymes and repair systems",
            "notes": (
                "Verified against the public Imlay abstract; the review "
                "summarizes oxidative damage from superoxide and hydrogen "
                "peroxide plus induced detoxification and repair defenses."
            ),
        },
    },
    {
        "before": {
            "reference": "DOI:10.1007/s00018-003-3206-5",
            "notes": (
                "Chelikani, Fita & Loewen support catalases as core enzymes of "
                "the oxidative-stress defense."
            ),
        },
        "after": {
            "reference": "DOI:10.1007/s00018-003-3206-5",
            "snippet": (
                "hydrogen peroxide to water and molecular oxygen, serving to protect cells"
            ),
            "notes": (
                "Verified against the public Europe PMC abstract; Chelikani et "
                "al. review catalase enzymes that detoxify hydrogen peroxide."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "hydrogen_peroxide",
            "predicate": "causes",
            "object": "oxidative_stress_process",
            "description": "Reactive oxygen species trigger the oxidative-stress response.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro3032",
                    "notes": "Imlay reviews ROS damage and induced defenses.",
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "hydrogen_peroxide",
            "predicate": "causes",
            "object": "oxidative_stress_process",
            "description": "Hydrogen peroxide damages cells and triggers ROS defense.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro3032",
                    "snippet": (
                        "hydrogen peroxide. These species can destroy the "
                        "activities of metalloenzymes and the integrity of DNA"
                    ),
                    "notes": (
                        "Verified against the public Imlay abstract; hydrogen "
                        "peroxide is retained as a representative ROS damaging "
                        "metalloenzymes and DNA."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "oxidative_stress_process",
            "predicate": "confers",
            "object": "oxidative_stress_response_trait",
            "description": "The induced defense realizes the oxidative-stress-response trait.",
            "evidence": [
                {
                    "reference": "DOI:10.1007/s00018-003-3206-5",
                    "notes": (
                        "Chelikani et al. support catalases as core oxidative-stress enzymes."
                    ),
                }
            ],
            "predicate_id": "METPO:2007700",
        },
        "after": {
            "subject": "oxidative_stress_process",
            "predicate": "confers",
            "object": "oxidative_stress_response_trait",
            "description": "The induced defense realizes the oxidative-stress-response trait.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro3032",
                    "snippet": (
                        "forcing organisms to protect themselves with scavenging "
                        "enzymes and repair systems"
                    ),
                    "notes": (
                        "Verified against the public Imlay abstract; the edge "
                        "connects ROS-induced scavenging and repair defenses to "
                        "the broad oxidative-stress-response trait."
                    ),
                }
            ],
            "predicate_id": "METPO:2007700",
        },
    },
    {
        "before": {
            "subject": "oxyr_regulator",
            "predicate": "positively regulates",
            "object": "oxidative_stress_process",
            "description": (
                "OxyR activates transcription of genes that defend the cell against "
                "oxidative stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1099/mic.0.001481",
                    "notes": (
                        "OxyR is widely conserved in bacteria and activates "
                        "transcription of a set of genes that influence cellular "
                        "defence against oxidative stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "oxyr_regulator",
            "predicate": "positively regulates",
            "object": "oxidative_stress_process",
            "description": (
                "OxyR activates transcription of genes that defend the cell against "
                "oxidative stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1099/mic.0.001481",
                    "snippet": (
                        "activates the transcription of a set of genes that "
                        "influence cellular defence against oxidative stress"
                    ),
                    "notes": (
                        "Verified against the open Bientz et al. abstract; this "
                        "supports OxyR as a bacterial transcriptional regulator "
                        "of oxidative-stress defense genes."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "rpos_sigma_factor",
            "predicate": "positively regulates",
            "object": "oxidative_stress_process",
            "description": (
                "The general stress sigma factor RpoS controls oxidative-stress "
                "defense outputs; its loss increases sensitivity to oxidative stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00151-22",
                    "notes": (
                        "Cells devoid of RpoS are sensitive to oxidative stress; "
                        "the RpoS regulon includes oxidative-stress genes (dps, "
                        "catalases, sodA, osmC)."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "rpos_sigma_factor",
            "predicate": "positively regulates",
            "object": "oxidative_stress_process",
            "description": (
                "The general stress sigma factor RpoS controls oxidative-stress "
                "defense outputs; its loss increases sensitivity to oxidative stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00151-22",
                    "snippet": "are sensitive to oxidative stress",
                    "notes": (
                        "Verified against the ASM article preview; RpoS is "
                        "retained as a broad E. coli general-stress regulator "
                        "whose loss increases oxidative-stress sensitivity."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "thioredoxin_system",
            "predicate": "contributes to",
            "object": "oxidative_stress_process",
            "description": (
                "Thioredoxin thiol-repair systems support survival under "
                "oxidative/oxidant stress, including in anaerobes and spores."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.ppat.1012001",
                    "notes": (
                        "Multiple thioredoxin systems are involved in the response "
                        "to oxidative stresses, broadening thiol-repair scope "
                        "beyond classic aerobes."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "thioredoxin_system",
            "predicate": "contributes to",
            "object": "oxidative_stress_process",
            "description": (
                "Thioredoxin thiol-repair systems support survival under "
                "oxidative/oxidant stress, including in anaerobes and spores."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.ppat.1012001",
                    "snippet": "ubiquitous system for thiol and protein repair",
                    "notes": (
                        "Verified against the open Anjou et al. abstract; the "
                        "thioredoxin system is retained as a bacterial thiol and "
                        "protein repair branch."
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
    if graph.get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{SLUG}: expected a MECHANISTIC graph")
    return graph


def _record_evidence_by_state(state: str) -> list[dict[str, Any]]:
    return [replacement[state] for replacement in RECORD_EVIDENCE_REPLACEMENTS]


def _edges_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_record_evidence(
    doc: dict[str, Any], expected: list[dict[str, Any]], state: str
) -> None:
    evidence = doc.get("evidence") or []
    for item in expected:
        if item not in evidence:
            raise ValueError(f"{SLUG}: missing {state} record evidence")


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


def _has_exact_record_evidence(doc: dict[str, Any], expected: list[dict[str, Any]]) -> bool:
    evidence = doc.get("evidence") or []
    return all(item in evidence for item in expected)


def _has_any_exact_record_evidence(doc: dict[str, Any], expected: list[dict[str, Any]]) -> bool:
    evidence = doc.get("evidence") or []
    return any(item in evidence for item in expected)


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def _replacement_for_record_evidence(item: dict[str, Any]) -> dict[str, Any]:
    for replacement in RECORD_EVIDENCE_REPLACEMENTS:
        if item == replacement["before"]:
            return copy.deepcopy(replacement["after"])
    return item


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_record_evidence = _record_evidence_by_state("before")
    after_record_evidence = _record_evidence_by_state("after")
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    has_after_record_evidence = _has_exact_record_evidence(doc, after_record_evidence)
    has_some_after_record_evidence = _has_any_exact_record_evidence(doc, after_record_evidence)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_record_evidence and has_after_edges:
        return False

    if has_after_record_evidence:
        _assert_exact_edges(graph, after_edges, "migrated")

    if has_after_record_evidence or has_after_edges:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"record_evidence={has_after_record_evidence} "
            f"edges={has_after_edges}"
        )
    if has_some_after_record_evidence:
        raise ValueError(f"{SLUG}: partial evidence replay: record_evidence=partial")

    _assert_exact_record_evidence(doc, before_record_evidence, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    doc["evidence"] = [_replacement_for_record_evidence(item) for item in doc["evidence"]]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the oxidative_stress_response_ros_defense graph for "
            "issue #183: added exact snippets to 2 record-level evidence "
            "items and 5 peroxide, OxyR, RpoS, and thioredoxin causal-edge "
            "evidence entries. No paid research service was called."
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
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write changes to data/traits/physiology/oxidative_stress_response.yaml",
    )
    args = parser.parse_args()
    return apply(write=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
