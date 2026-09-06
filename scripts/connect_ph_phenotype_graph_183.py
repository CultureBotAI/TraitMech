#!/usr/bin/env python3
"""Connect the pH numerical-limits graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_ph_phenotype_graph_183.py
    python scripts/connect_ph_phenotype_graph_183.py --apply
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

SLUG = "environment/ph_phenotype_with_numerical_limits"
GRAPH_ID = "ph_phenotype_numerical_axis"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T18:00:00Z"
EXPECTED_COMPONENTS = 5

GRAPH_METADATA_BEFORE = {
    "title": "pH phenotype numerical-limits axis",
    "description": (
        "DOI-backed graph linking the external pH (H+ activity) axis to the "
        "three numerical-limit measurement types (optimum, range, delta) that "
        "together classify acidophile, neutrophile, and alkaliphile physiology."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "pH numerical-limits and homeostasis context axis",
    "description": (
        "DOI-backed nonmechanistic graph connecting the external-pH "
        "measurement axis and pH optimum, range, and delta subclasses with "
        "contextual PMF, F0F1-ATPase, antiporter, amino-acid decarboxylase, "
        "and cytoplasmic-buffering branches."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "f0f1_atpase",
        "predicate": "enables",
        "object": "atp_synthesis_from_pmf",
        "description": "F0F1-ATPase couples the proton motive force to ATP synthesis.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "PMF for nutrient uptake and ATP synthesis",
                "notes": (
                    "Verified against the open Poolman review; the PMF links "
                    "proton translocation by the F0F1-ATPase to ATP synthesis."
                ),
            }
        ],
        "predicate_id": "RO:0002327",
    },
    {
        "subject": "na_h_antiport_activity",
        "predicate": "regulates",
        "object": "internal_ph_pmf",
        "description": "Na+/H+ antiporter activity regulates internal pH and PMF.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "maintain a relatively constant PMF and internal pH",
                "notes": (
                    "Verified against the open Poolman review; Na+/H+ "
                    "antiporters are listed as key bacterial pH-homeostasis "
                    "regulators."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "k_h_antiporter",
        "predicate": "regulates",
        "object": "internal_ph_pmf",
        "description": "K+/H+ antiporter activity regulates internal pH and PMF.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "Na+/H+ and K+/H+ antiporters",
                "notes": (
                    "Verified against the open Poolman review; K+/H+ antiporters "
                    "are listed as key bacterial pH-homeostasis regulators."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "aa_decarboxylase_antiporter",
        "predicate": "consumes",
        "object": "intracellular_proton",
        "description": (
            "Amino-acid decarboxylase plus antiporter systems consume "
            "intracellular protons, raising internal pH."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "Proton motive force generation by substrate decarboxylation",
                "notes": (
                    "Verified against the open Poolman review; substrate "
                    "decarboxylation is linked to bacterial PMF generation in "
                    "pH homeostasis."
                ),
            }
        ],
        "predicate_id": "biolink:consumes",
    },
    {
        "subject": "phosphate_buffering",
        "predicate": "contributes to",
        "object": "internal_ph",
        "description": "Cytoplasmic phosphate pools contribute to internal-pH stability.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "buffering capacity of the cytoplasm",
                "notes": (
                    "Verified against the open Poolman review; cytoplasmic "
                    "buffering is described as important for absorbing pH "
                    "fluctuations."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "atp_synthesis_from_pmf",
        "predicate": "associated with",
        "object": "proton_motive_force",
        "description": (
            "F0F1-coupled ATP synthesis from the PMF is associated with the "
            "PMF branch of pH numerical-limit context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "drive the synthesis of ATP and the transport of solutes",
                "notes": (
                    "Verified against the open Poolman review; this connector "
                    "keeps PMF-driven ATP synthesis as bioenergetic context "
                    "rather than direct proof of a pH numerical limit."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "internal_ph_pmf",
        "predicate": "associated with",
        "object": "proton_motive_force",
        "description": (
            "Regulated internal pH and PMF homeostasis is associated with the "
            "PMF branch of pH numerical-limit context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": (
                    "simultaneously maintain a relatively constant PMF and "
                    "internal pH"
                ),
                "notes": (
                    "Verified against the open Poolman review; this connector "
                    "keeps Na+/H+ and K+/H+ antiport activity as pH-homeostasis "
                    "context rather than a universal mechanism for every pH bin."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "intracellular_proton",
        "predicate": "associated with",
        "object": "internal_ph",
        "description": (
            "Intracellular proton consumption is associated with cytoplasmic "
            "pH homeostasis in the pH numerical-limit context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "metabolite decarboxylation pathways",
                "notes": (
                    "Verified against the open Poolman review; this connector "
                    "keeps amino-acid decarboxylation as cytoplasmic proton "
                    "control context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "internal_ph",
        "predicate": "associated with",
        "object": "ph_phenotype_trait",
        "description": (
            "Cytoplasmic pH homeostasis is associated with external-pH "
            "numerical-limit phenotypes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "free protons at pH 7.2 is only about 10",
                "notes": (
                    "Verified against the open Poolman review; this connector "
                    "keeps phosphate buffering as internal-pH context rather "
                    "than direct proof of a measured external-pH limit."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
]


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


def _edges_by_key(edges: list[dict[str, Any]]) -> dict[
    tuple[str | None, str | None, str | None], dict[str, Any]
]:
    return {_edge_key(edge): edge for edge in edges}


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
            raise ValueError(f"{SLUG}: {state} edge drifted: {key}")


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
    additions = _edges_by_key(ADDED_EDGES)
    source_connectors = _edges_by_key(SOURCE_CONNECTOR_EDGES)

    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    addition_keys = set(additions)
    present = existing_keys & addition_keys

    before = _components(graph)
    if before == 1 and present == addition_keys:
        _assert_graph_metadata(graph, GRAPH_METADATA_AFTER, "migrated")
        _assert_exact_edges(graph, additions, "migrated")
        return False

    _assert_graph_metadata(graph, GRAPH_METADATA_BEFORE, "source")
    if present:
        raise ValueError(f"{SLUG}: partial connector replay: {sorted(present)}")

    _assert_exact_edges(graph, source_connectors, "source")
    _assert_endpoints(graph, ADDED_EDGES)
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")

    graph.update(GRAPH_METADATA_AFTER)
    graph.setdefault("edges", []).extend(copy.deepcopy(ADDED_EDGES))

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{SLUG}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            "by adding 4 source- and verbatim-snippet-backed association "
            "connectors among PMF, F0F1-ATPase/ATP-synthesis, antiporter, "
            "amino-acid-decarboxylase, and phosphate-buffering branches. No "
            "paid research service was called."
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
