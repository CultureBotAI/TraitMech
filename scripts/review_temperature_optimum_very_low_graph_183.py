#!/usr/bin/env python3
"""Review temperature-optimum-very-low graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_optimum_very_low_graph_183.py
    python scripts/review_temperature_optimum_very_low_graph_183.py --apply
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

SLUG = "environment/temperature_optimum_very_low"
GRAPH_ID = "temperature_optimum_very_low_psychrophile_setpoint"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T03:40:00Z"

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "fatty_acid_desaturase_activity",
            "predicate": "increases abundance of",
            "object": "unsaturated_fatty_acids",
            "description": ("Fatty acid desaturase activity increases unsaturated acyl chains."),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "notes": "activation of desaturases, increased unsaturated acyl chains",
                }
            ],
        },
        "after": {
            "subject": "fatty_acid_desaturase_activity",
            "predicate": "increases",
            "object": "unsaturated_fatty_acids",
            "description": ("Fatty acid desaturase activity increases unsaturated acyl chains."),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "increase in the proportion of unsaturated acyl chains",
                    "notes": (
                        "Verified against the open Hamdan review; lower growth "
                        "temperatures are described as activating desaturases "
                        "that convert saturated acyl fatty acids to unsaturated "
                        "ones."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "unsaturated_fatty_acids",
            "predicate": "maintains",
            "object": "membrane_fluidity",
            "description": (
                "Increased unsaturated fatty acids maintain membrane fluidity at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/AEM.01928-22",
                    "notes": (
                        "maintain membrane fluidity by improving the ratio of "
                        "unsaturated fatty acids"
                    ),
                }
            ],
        },
        "after": {
            "subject": "unsaturated_fatty_acids",
            "predicate": "contributes to",
            "object": "membrane_fluidity",
            "description": (
                "Increased unsaturated fatty acids contribute to membrane fluidity "
                "at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/AEM.01928-22",
                    "snippet": "proportion of unsaturated fatty acids was higher",
                    "notes": (
                        "Verified against the open Yang et al. abstract; "
                        "Bacillus simplex H-b cultured at low temperature "
                        "carried a higher unsaturated-fatty-acid proportion."
                    ),
                },
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "maintain optimum membrane fluidity",
                    "notes": (
                        "Verified against the open Hamdan review; fatty-acyl-chain "
                        "modifications are described as preserving membrane "
                        "fluidity in freezing environments."
                    ),
                },
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "membrane_fluidity",
            "predicate": "supports",
            "object": "psychrophile_machinery",
            "description": (
                "Maintained membrane fluidity supports cold-adapted cellular machinery."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/AEM.01928-22",
                    "notes": ("maintained membrane fluidity sustains function at low temperature"),
                }
            ],
        },
        "after": {
            "subject": "membrane_fluidity",
            "predicate": "contributes to",
            "object": "psychrophile_machinery",
            "description": (
                "Maintained membrane fluidity contributes to cold-adapted cellular machinery."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/AEM.01928-22",
                    "snippet": "contribute to the survival of the strain under cold conditions",
                    "notes": (
                        "Verified against the open Yang et al. abstract; the cold "
                        "adaptation model includes membrane transport adjustment "
                        "among mechanisms supporting Bacillus simplex H-b survival "
                        "under cold conditions."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "cold_shock_proteins",
            "predicate": "supports",
            "object": "translation_low_temperature",
            "description": (
                "Cold shock proteins / RNA chaperones support transcription and "
                "translation in the cold."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "notes": (
                        "Cold-shock proteins are major cold responses, functioning "
                        "in regulation of transcription/translation"
                    ),
                }
            ],
        },
        "after": {
            "subject": "cold_shock_proteins",
            "predicate": "contributes to",
            "object": "translation_low_temperature",
            "description": (
                "Cold shock proteins / RNA chaperones contribute to transcription "
                "and translation in the cold."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "regulation of cellular protein synthesis",
                    "notes": (
                        "Verified against the open Hamdan review; cold-shock "
                        "proteins are linked to cellular protein-synthesis "
                        "regulation, including transcription and translation "
                        "initiation."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "glycine_betaine",
            "predicate": "stabilizes",
            "object": "protein_membrane_stabilization",
            "description": (
                "Glycine betaine prevents protein aggregation and stabilizes "
                "membranes during cold stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "notes": (
                        "including glycine betaine and trehalose - prevent protein "
                        "aggregation and stabilize membranes"
                    ),
                }
            ],
        },
        "after": {
            "subject": "glycine_betaine",
            "predicate": "contributes to",
            "object": "protein_membrane_stabilization",
            "description": (
                "Glycine betaine contributes to protein and membrane stabilization "
                "during cold stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "growth-enhancing effect of glycine betaine",
                    "notes": (
                        "Verified against the open Hamdan review; the glycine "
                        "betaine paragraph cites low-temperature growth enhancement "
                        "and discusses compatible solutes as cold cryoprotectants."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "trehalose",
            "predicate": "acts as",
            "object": "cryoprotection",
            "description": "Trehalose acts as a cryoprotectant.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/sj.embor.7400662",
                    "notes": (
                        "Compatible solutes (trehalose) and extracellular "
                        "polysaccharides act as cryoprotectants"
                    ),
                }
            ],
        },
        "after": {
            "subject": "trehalose",
            "predicate": "contributes to",
            "object": "cryoprotection",
            "description": "Trehalose contributes to cryoprotection.",
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "preventing protein denaturation and aggregation",
                    "notes": (
                        "Verified against the open Hamdan review; trehalose is "
                        "reported as preventing protein denaturation and "
                        "aggregation in psychrophilic bacteria."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "antifreeze_proteins",
            "predicate": "causes",
            "object": "thermal_hysteresis",
            "description": ("Antifreeze proteins lower the freezing point via thermal hysteresis."),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": "AFPs lower freezing point via thermal hysteresis",
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "antifreeze_proteins",
            "predicate": "causes",
            "object": "thermal_hysteresis",
            "description": ("Antifreeze proteins lower the freezing point via thermal hysteresis."),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "snippet": "lower the water freezing point",
                    "notes": (
                        "Verified against the open Ramón et al. abstract and "
                        "review text; anti-freeze proteins are described as "
                        "lowering the water freezing point via thermal hysteresis "
                        "or ice-recrystallization inhibition."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "enzyme_structural_flexibility",
            "predicate": "increases",
            "object": "catalytic_activity_low_temperature",
            "description": (
                "Increased enzyme structural flexibility increases catalytic "
                "activity at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "notes": (
                        "Cold-adapted enzymes display increased structural "
                        "flexibility and higher catalytic efficiency"
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "enzyme_structural_flexibility",
            "predicate": "increases",
            "object": "catalytic_activity_low_temperature",
            "description": (
                "Increased enzyme structural flexibility increases catalytic "
                "activity at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.17159/sajs.2018/20170254",
                    "snippet": "up to 10-fold higher specific activity",
                    "notes": (
                        "Verified against the open Hamdan review; psychrophiles "
                        "are described as producing structurally flexible enzymes "
                        "with higher low-temperature specific activity than "
                        "mesophilic homologues."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
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
            "Reviewed the temperature_optimum_very_low_psychrophile_setpoint "
            "graph for issue #183: added snippets to 8 edge-level evidence "
            "items and grounded the desaturase, membrane-fluidity, cold-shock, "
            "glycine-betaine, and trehalose predicates to RO:0002213 or "
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
