#!/usr/bin/env python3
"""Review very-low pH-delta graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ph_delta_very_low_graph_183.py
    python scripts/review_ph_delta_very_low_graph_183.py --apply
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

SLUG = "environment/ph_delta_very_low"
GRAPH_ID = "ph_delta_very_low_stenotopic"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T02:00:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "external_ph_stress",
            "predicate": "alters",
            "object": "pmf_partitioning",
            "description": (
                "External pH stress alters partitioning of the proton motive force "
                "between delta-pH and delta-psi."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "The two PMF components, delta-psi and delta-pH, are "
                        "adjustable according to pH demand and can even reverse "
                        "orientation under strong pH stress; broad foundational "
                        "pH-homeostasis edge."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_ph_stress",
            "predicate": "regulates",
            "object": "pmf_partitioning",
            "description": (
                "External pH stress modulates partitioning of the proton motive "
                "force between Delta-pH and Delta-psi."
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
            "subject": "constitutive_ph_homeostasis_expression",
            "predicate": "imposes energetic cost on",
            "object": "energetic_cost",
            "description": (
                "Constitutive expression of pH-homeostatic machinery imposes an "
                "energetic cost impairing growth near neutral pH."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Extremophiles often express major pH homeostatic mechanisms "
                        "constitutively; this preparedness imposes an energetic cost "
                        "and can impair growth at near-neutral pH (inferred "
                        "breadth-constraint mechanism)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "constitutive_ph_homeostasis_expression",
            "predicate": "causes",
            "object": "energetic_cost",
            "description": (
                "Constitutive expression of pH-homeostatic machinery can impose a "
                "growth cost near neutral pH."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "energetic cost of expressing proteins",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; constitutive pH-homeostatic preparedness in "
                        "extremophiles can negatively affect growth near neutral pH."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "na_h_antiporter_activity",
            "predicate": "enables",
            "object": "alkaline_ph_homeostasis",
            "description": "Na+/H+ antiporter activity enables alkaline pH homeostasis.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Na+/H+ antiport (notably the hetero-oligomeric Mrp system) "
                        "is a major, causally important strategy for alkaline pH "
                        "homeostasis."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "na_h_antiporter_activity",
            "predicate": "contributes to",
            "object": "alkaline_ph_homeostasis",
            "description": "Na+/H+ antiporter activity contributes to alkaline pH homeostasis.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "proton entry driven by the transmembrane potential",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; electrogenic cation/proton antiport supports "
                        "proton entry during alkaline stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "f1fo_atpase_proton_pumping",
            "predicate": "promotes",
            "object": "acid_stress_survival",
            "description": ("Hydrolytic F1Fo-ATPase proton pumping promotes acid stress survival."),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Hydrolytic F1Fo-ATPase activity can be increased for "
                        "ATP-dependent H+ extrusion under acid stress; strong "
                        "acid-side homeostasis mechanism."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "f1fo_atpase_proton_pumping",
            "predicate": "contributes to",
            "object": "acid_stress_survival",
            "description": (
                "Hydrolytic F1Fo-ATPase proton pumping contributes to acid-stress survival."
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
            "subject": "glutamate_decarboxylase_system",
            "predicate": "consumes",
            "object": "cytoplasmic_proton_consumption",
            "description": (
                "Glutamate decarboxylase GadB coupled with a GABA/glutamate "
                "antiporter consumes cytoplasmic protons."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "notes": (
                        "Amino acid decarboxylases like GadB with its antiporter "
                        "coupling; canonical acid-resistance mechanism consuming "
                        "cytoplasmic protons."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
        "after": {
            "subject": "glutamate_decarboxylase_system",
            "predicate": "contributes to",
            "object": "cytoplasmic_proton_consumption",
            "description": (
                "Glutamate decarboxylase GadB coupled with a GABA/glutamate "
                "antiporter contributes to cytoplasmic proton consumption."
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
            "Reviewed the very-low ph_delta_very_low_stenotopic graph for issue "
            "#183: added snippets to 5 edge-level evidence items, grounded 2 "
            "unmapped predicates, and narrowed 3 broad pH-homeostasis predicates "
            "to RO:0002326. No paid research service was called."
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
