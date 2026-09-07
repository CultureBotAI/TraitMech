#!/usr/bin/env python3
"""Review wide pH-delta-mid3 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ph_delta_mid3_graph_183.py
    python scripts/review_ph_delta_mid3_graph_183.py --apply
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

SLUG = "environment/ph_delta_mid3"
GRAPH_ID = "ph_delta_mid3_wide_breadth"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T01:40:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "ph_delta_mid3_trait",
            "predicate": "is a",
            "object": "ph_delta",
            "description": "pH delta mid3 is a quantitative bin of the pH-delta phenotype.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "external pH",
                    "notes": (
                        "Supports the 4–5 unit breadth as a value within the pH-delta distribution."
                    ),
                }
            ],
            "predicate_id": "rdfs:subClassOf",
        },
        "after": {
            "subject": "ph_delta_mid3_trait",
            "predicate": "is a",
            "object": "ph_delta",
            "description": "pH delta mid3 is a quantitative bin of the pH-delta phenotype.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "grow at external pH values",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; pH breadth is represented as a quantitative "
                        "external-growth-pH bin under the pH-delta phenotype."
                    ),
                }
            ],
            "predicate_id": "rdfs:subClassOf",
        },
    },
    {
        "before": {
            "subject": "external_alkaline_ph",
            "predicate": "increases reliance on",
            "object": "na_h_antiport",
            "description": (
                "High external pH increases reliance on electrogenic Na+/H+ antiport "
                "for cytoplasmic pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Multiple Na+/H+ and K+/H+ antiporters are critical for "
                        "alkaline homeostasis, driven by membrane potential."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_alkaline_ph",
            "predicate": "regulates",
            "object": "na_h_antiport",
            "description": (
                "High external pH modulates the contribution of electrogenic Na+/H+ "
                "antiport to cytoplasmic pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "energize active proton uptake",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; cation/proton antiporters use PMF from "
                        "respiration or ATPases to drive proton uptake under alkaline "
                        "stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "pmf_regulation",
            "predicate": "supports",
            "object": "cytoplasmic_ph_maintenance",
            "description": (
                "Regulation of Delta-psi and Delta-pH supports maintenance of "
                "cytoplasmic pH across external pH changes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "PMF (Delta-pH and Delta-psi) is central to pH homeostasis; "
                        "neutralophiles keep cytoplasmic pH near 7.5 across external "
                        "pH ~5.5-9.0."
                    ),
                }
            ],
        },
        "after": {
            "subject": "pmf_regulation",
            "predicate": "contributes to",
            "object": "cytoplasmic_ph_maintenance",
            "description": (
                "Regulation of Delta-psi and Delta-pH contributes to maintenance of "
                "cytoplasmic pH across external pH changes."
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
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "proton_pumping_respiratory_complexes",
            "predicate": "contribute to",
            "object": "proton_motive_force",
            "description": (
                "Proton-pumping respiratory complexes contribute to the PMF used for "
                "pH homeostasis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Cells use primary proton pumps including respiratory-chain "
                        "pumps to create PMF for transport and pH regulation."
                    ),
                }
            ],
        },
        "after": {
            "subject": "proton_pumping_respiratory_complexes",
            "predicate": "generates",
            "object": "proton_motive_force",
            "description": "Proton-pumping respiratory complexes generate proton motive force.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "Primary proton pumps generate the PMF",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; respiratory-chain complexes are listed among "
                        "the proton pumps that establish bacterial PMF."
                    ),
                }
            ],
            "predicate_id": "biolink:produces",
        },
    },
    {
        "before": {
            "subject": "f0f1_atpase",
            "predicate": "contributes to",
            "object": "cytoplasmic_ph_maintenance",
            "description": (
                "F0F1-ATPase can extrude protons and contributes to pH homeostasis "
                "under acid stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "F1Fo-ATPase hydrolytic activity can drive H+ extrusion; "
                        "key regulator in low-pH contexts."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "f0f1_atpase",
            "predicate": "contributes to",
            "object": "cytoplasmic_ph_maintenance",
            "description": ("F0F1-ATPase proton pumping contributes to bacterial pH homeostasis."),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "Key regulators of bacterial pH homeostasis",
                    "notes": (
                        "Verified against the open Poolman review; proton-pumping "
                        "enzymes, including F0F1-ATPase in lactic acid bacteria, are "
                        "listed as bacterial pH-homeostasis regulators."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "phosphate_buffering",
            "predicate": "stabilizes",
            "object": "intracellular_ph_stability",
            "description": (
                "Cytoplasmic phosphate buffering capacity stabilizes intracellular pH."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "At pH ~7.2 only ~10 free protons present; cytoplasmic "
                        "phosphate buffering (~100 mM) makes buffering essential."
                    ),
                }
            ],
        },
        "after": {
            "subject": "phosphate_buffering",
            "predicate": "contributes to",
            "object": "intracellular_ph_stability",
            "description": (
                "Cytoplasmic phosphate buffering contributes to intracellular pH stability."
            ),
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
    },
    {
        "before": {
            "subject": "aa_decarboxylation",
            "predicate": "contributes to",
            "object": "proton_motive_force",
            "description": (
                "Amino-acid decarboxylation pathways consume protons and contribute "
                "to PMF and intracellular pH control."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Decarboxylation releases ~20 kJ/mol that can be stored as "
                        "PMF; decarboxylation pathways are key pH regulators."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "aa_decarboxylation",
            "predicate": "contributes to",
            "object": "proton_motive_force",
            "description": (
                "Amino-acid decarboxylation pathways consume protons and contribute "
                "to PMF and intracellular pH control."
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
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "membrane_lipid_remodeling",
            "predicate": "decreases",
            "object": "proton_permeability",
            "description": "Membrane lipid composition shifts reduce proton permeability.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2022.1034164",
                    "notes": (
                        "Membrane composition adjustments limit proton permeability "
                        "and alter phospholipid headgroups under high pH."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "membrane_lipid_remodeling",
            "predicate": "decreases",
            "object": "proton_permeability",
            "description": "Membrane lipid composition shifts reduce proton permeability.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2022.1034164",
                    "snippet": "higher content of saturated fatty acids",
                    "notes": (
                        "Verified against the open Frontiers methanotroph review; "
                        "saturated bacterial membranes are described as lowering "
                        "proton permeability under acid stress."
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
            "Reviewed the wide ph_delta_mid3_wide_breadth graph for issue #183: "
            "added snippets to 8 edge-level evidence items and grounded 4 unmapped "
            "pH-homeostasis predicates to RO:0002211, RO:0002326, or "
            "biolink:produces. No paid research service was called."
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
