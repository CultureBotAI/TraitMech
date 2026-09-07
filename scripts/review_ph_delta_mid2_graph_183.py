#!/usr/bin/env python3
"""Review broad pH-delta-mid2 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ph_delta_mid2_graph_183.py
    python scripts/review_ph_delta_mid2_graph_183.py --apply
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

SLUG = "environment/ph_delta_mid2"
GRAPH_ID = "ph_delta_mid2_broad_breadth"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T01:20:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "external_ph_stress",
            "predicate": "alters",
            "object": "pmf_component_balance",
            "description": (
                "External pH stress alters the balance/orientation of PMF "
                "components (delta-pH, delta-psi)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Relative magnitudes and even orientation of PMF "
                        "components change with external pH; under strong pH "
                        "stress a component can reverse orientation."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_ph_stress",
            "predicate": "regulates",
            "object": "pmf_component_balance",
            "description": (
                "External pH stress modulates the relative balance of proton-motive "
                "force components."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "relative magnitudes of the two PMF components",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; bacterial pH-homeostasis demands determine "
                        "how delta-psi and delta-pH contribute to the PMF."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "respiratory_proton_pumps",
            "predicate": "generates",
            "object": "pmf_generation",
            "description": "Primary respiratory-chain proton pumps generate the proton motive force.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Primary proton pumps (respiratory chain pumps) generate "
                        "PMF; broad mechanism across bacteria."
                    ),
                }
            ],
            "predicate_id": "biolink:produces",
        },
        "after": {
            "subject": "respiratory_proton_pumps",
            "predicate": "generates",
            "object": "pmf_generation",
            "description": "Primary respiratory-chain proton pumps generate proton motive force.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "Primary proton pumps generate the PMF",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; respiratory-chain complexes are listed "
                        "among the proton pumps that establish bacterial PMF."
                    ),
                }
            ],
            "predicate_id": "biolink:produces",
        },
    },
    {
        "before": {
            "subject": "f1fo_atpase",
            "predicate": "contributes to",
            "object": "proton_translocation_homeostasis",
            "description": (
                "Proton-coupled F1Fo-ATPase contributes to proton translocation "
                "supporting pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Proton-coupled ATPases are a primary strategy; F1-F0 "
                        "ATPase proton pump is an active pH-homeostasis mechanism."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "f1fo_atpase",
            "predicate": "contributes to",
            "object": "proton_translocation_homeostasis",
            "description": (
                "F1Fo-ATPase contributes to pH homeostasis by coupling ATP "
                "turnover to proton translocation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "ATP-dependent H+ extrusion under acidic conditions",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; F1Fo-ATPase can drive proton efflux in "
                        "acid-stressed non-respiratory neutralophiles."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "na_h_antiporter_activity",
            "predicate": "supports",
            "object": "alkaline_ph_homeostasis",
            "description": (
                "Na+/H+ antiporter activity imports H+ and extrudes Na+ to support "
                "alkaline pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Cation/proton antiporters are transcriptionally "
                        "up-regulated for inward proton transport under alkaline "
                        "stress."
                    ),
                }
            ],
        },
        "after": {
            "subject": "na_h_antiporter_activity",
            "predicate": "contributes to",
            "object": "alkaline_ph_homeostasis",
            "description": (
                "Na+/H+ antiporter activity imports H+ and extrudes Na+ as part of "
                "alkaline pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "proton entry driven by the transmembrane potential",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; electrogenic cation/proton antiport "
                        "supports proton entry during alkaline stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "glutamate_decarboxylase_system",
            "predicate": "consumes",
            "object": "intracellular_proton",
            "description": (
                "The glutamate decarboxylase system consumes intracellular protons "
                "during decarboxylation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/antibiotics12091474",
                    "notes": (
                        "Glutamate decarboxylase (GadB with its antiporter) is a "
                        "proton-consuming acid-tolerance mechanism (GDAR), broadly "
                        "curated in Gram-negatives."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
        "after": {
            "subject": "glutamate_decarboxylase_system",
            "predicate": "consumes",
            "object": "intracellular_proton",
            "description": (
                "The glutamate decarboxylase system consumes intracellular protons "
                "during acid-stress decarboxylation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "consumes a proton during decarboxylation",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; GadB consumes a cytoplasmic proton when it "
                        "decarboxylates glutamate in the E. coli acid-resistance "
                        "cycle."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
    },
    {
        "before": {
            "subject": "cytoplasmic_buffers",
            "predicate": "buffers",
            "object": "cytoplasmic_ph_buffering",
            "description": (
                "Small molecules (polyamines, amino acids, phosphate) passively "
                "buffer cytoplasmic pH."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/antibiotics12091474",
                    "notes": (
                        "Passive buffering of cytoplasmic pH is provided by small "
                        "molecules (amino acids, proteins, polyamines, "
                        "polyphosphate, inorganic phosphate)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cytoplasmic_buffers",
            "predicate": "contributes to",
            "object": "cytoplasmic_ph_buffering",
            "description": (
                "Small molecules, including polyamines, amino acids, and phosphate, "
                "contribute to passive cytoplasmic pH buffering."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/antibiotics12091474",
                    "snippet": "Cytoplasmic pH is buffered by small molecules",
                    "notes": (
                        "Verified against the open Rebelo et al. review; small "
                        "molecules contribute passive cytoplasmic buffering in pH "
                        "homeostasis."
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
            "Reviewed the broad ph_delta_mid2_broad_breadth graph for issue #183: "
            "added snippets to 6 edge-level evidence items and grounded 3 "
            "unmapped pH-homeostasis predicates to RO:0002211 or RO:0002326. No "
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
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
