#!/usr/bin/env python3
"""Review temperature-delta-high graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_delta_high_graph_183.py
    python scripts/review_temperature_delta_high_graph_183.py --apply
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

SLUG = "environment/temperature_delta_high"
GRAPH_ID = "temperature_delta_high_eurythermal"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T03:00:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "decreased_growth_temperature",
            "predicate": "increases",
            "object": "unsaturated_fatty_acid_biosynthesis",
            "description": (
                "Lower growth temperature increases incorporation of unsaturated "
                "fatty acids (homoviscous adaptation)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "notes": (
                        "Bacteria remodel membrane fluidity via proportionally more "
                        "unsaturated fatty acids as growth temperature decreases."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "decreased_growth_temperature",
            "predicate": "increases",
            "object": "unsaturated_fatty_acid_biosynthesis",
            "description": (
                "Lower growth temperature increases incorporation of unsaturated "
                "fatty acids (homoviscous adaptation)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "snippet": (
                        "incorporation of proportionally more unsaturated fatty acids"
                    ),
                    "notes": (
                        "Verified against the de Mendoza Annual Review abstract; "
                        "bacterial membranes remodel by incorporating proportionally "
                        "more unsaturated fatty acids as growth temperature decreases."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "homoviscous_adaptation",
            "predicate": "maintains",
            "object": "membrane_fluidity_homeostasis",
            "description": (
                "Homoviscous adaptation maintains membrane fluidity/permeability "
                "homeostasis across thermal shifts."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "notes": (
                        "Homoviscous adaptation disrupts lipid bilayer order and "
                        "optimizes cellular processes at the new temperature."
                    ),
                }
            ],
        },
        "after": {
            "subject": "homoviscous_adaptation",
            "predicate": "contributes to",
            "object": "membrane_fluidity_homeostasis",
            "description": (
                "Homoviscous adaptation contributes to membrane "
                "fluidity/permeability homeostasis across thermal shifts."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "snippet": "remodel the fluidity of their membrane bilayer",
                    "notes": (
                        "Verified against the de Mendoza Annual Review abstract; "
                        "homoviscous adaptation is the named membrane-fluidity "
                        "remodeling process used after growth temperature decreases."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "decreased_membrane_fluidity",
            "predicate": "upregulates",
            "object": "unsaturated_fatty_acid_biosynthesis",
            "description": (
                "Reduced membrane fluidity is sensed and upregulates unsaturated "
                "fatty acid biosynthesis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "notes": (
                        "Microbes sense decreased membrane fluidity and initiate "
                        "responses that upregulate unsaturated fatty acid biosynthesis."
                    ),
                }
            ],
        },
        "after": {
            "subject": "decreased_membrane_fluidity",
            "predicate": "positively regulates",
            "object": "unsaturated_fatty_acid_biosynthesis",
            "description": (
                "Reduced membrane fluidity is sensed and positively regulates "
                "unsaturated fatty acid biosynthesis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "snippet": "upregulate the biosynthesis of unsaturated fatty acids",
                    "notes": (
                        "Verified against the de Mendoza Annual Review abstract; "
                        "bacteria sense decreased membrane fluidity and initiate "
                        "responses that upregulate unsaturated fatty acid biosynthesis."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "lipid_desaturase_activity",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Lipid desaturases introduce cis double bonds (~30 deg kink) "
                "creating packing defects that increase fluidity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "notes": (
                        "Organisms maintain membrane fluidity by activating lipid "
                        "desaturases that introduce cis double bonds to increase "
                        "packing defects and fluidity."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "lipid_desaturase_activity",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Lipid desaturases introduce cis double bonds that loosen packing "
                "and increase fluidity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "snippet": "cis-double bonds, result in looser packing and increased fluidity",
                    "notes": (
                        "Verified against the Wu et al. Cells review; lipid "
                        "desaturase-generated cis double bonds loosen acyl-chain "
                        "packing and increase membrane-bilayer fluidity."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "cis_trans_isomerase_activity",
            "predicate": "increases",
            "object": "membrane_viscosity_high_temperature",
            "description": (
                "Cis-trans isomerization of existing UFAs yields trans-UFAs "
                "resembling SFAs, raising membrane viscosity during warming."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "notes": (
                        "Cis-trans isomerase converts UFAs; trans-UFAs resemble "
                        "SFAs and raise membrane viscosity, compensating at higher "
                        "temperature."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "cis_trans_isomerase_activity",
            "predicate": "increases",
            "object": "membrane_viscosity_high_temperature",
            "description": (
                "Cis-trans isomerization of existing UFAs yields trans-UFAs "
                "resembling SFAs, raising membrane viscosity during warming."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "snippet": "properties that resemble SFAs",
                    "notes": (
                        "Verified against the Wu et al. Cells review; converting "
                        "cis-UFAs to trans-UFAs makes them more SFA-like and closer "
                        "packing at higher temperature."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "increased_fatty_acid_diversity",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Shifts in acyl chain length/branching and unsaturation jointly "
                "increase membrane fluidity at lower temperatures."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "notes": (
                        "Membrane composition adjustments (SCFA, BCFA, unsaturation, "
                        "lysophospholipids) can increase membrane fluidity at lower "
                        "temperatures."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "increased_fatty_acid_diversity",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Shifts in acyl chain length/branching and unsaturation jointly "
                "increase membrane fluidity at lower temperatures."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/cells12101353",
                    "snippet": ("increase the proportion of UFAs and short-chain fatty acids"),
                    "notes": (
                        "Verified against the Wu et al. Cells review; cold-adapted "
                        "membranes can increase unsaturated and short-chain fatty "
                        "acid proportions and modify branched-chain fatty-acid "
                        "content."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "thermostable_enzyme",
            "predicate": "resists",
            "object": "irreversible_protein_inactivation",
            "description": (
                "Intrinsic enzyme thermostability resists irreversible inactivation, "
                "extending upper growth limits."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
                    "notes": (
                        "Enzymes from hyperthermophiles are typically thermostable, "
                        "i.e., resistant to irreversible inactivation at high "
                        "temperatures."
                    ),
                }
            ],
        },
        "after": {
            "subject": "thermostable_enzyme",
            "predicate": "prevents",
            "object": "irreversible_protein_inactivation",
            "description": (
                "Intrinsic enzyme thermostability prevents irreversible inactivation, "
                "extending upper growth limits."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
                    "snippet": "resistant to irreversible inactivation at high temperatures",
                    "notes": (
                        "Verified against the open Vieille and Zeikus review; "
                        "hyperthermophilic enzymes are described as thermostable "
                        "and resistant to irreversible inactivation at high "
                        "temperatures."
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
            "Reviewed the temperature_delta_high_eurythermal graph for issue #183: "
            "added snippets to 7 edge-level evidence items and grounded 3 "
            "unmapped homoviscous-adaptation and thermostability predicates to "
            "RO:0002326, RO:0002213, or RO:0002212. No paid research service was "
            "called."
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
