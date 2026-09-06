#!/usr/bin/env python3
"""Repair PR #664 evidence after adversarial review.

The connector and review migrations in the dirty issue-183 batch are deliberately
strict once a record has migrated: they assert that each generated edge matches
its source script constant exactly. This follow-up repair updates the migrated
records from those corrected constants, then leaves one curation event per
record that ties the data refresh to the PR review issues.

Usage:
    python scripts/repair_pr664_adversarial_review.py
    python scripts/repair_pr664_adversarial_review.py --apply
"""

from __future__ import annotations

import argparse
import copy
import importlib
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

ACTION = "ADVERSARIAL_REVIEW_REPAIR"
TIMESTAMP = "2026-09-06T17:10:00Z"

CONNECTOR_MODULES = [
    "connect_gc_low_graph_183",
    "connect_mesophilic_graph_183",
    "connect_nacl_optimum_graph_183",
    "connect_ph_delta_mid3_graph_183",
    "connect_ph_delta_very_low_graph_183",
    "connect_ph_phenotype_graph_183",
    "connect_temperature_delta_high_graph_183",
    "connect_temperature_delta_very_low_graph_183",
    "connect_temperature_optimum_high_graph_183",
    "connect_temperature_optimum_very_low_graph_183",
    "connect_temperature_range_mid3_graph_183",
    "connect_temperature_range_mid4_graph_183",
    "connect_temperature_range_very_low_graph_183",
]

EDGE_REVIEW_MODULES = [
    "review_nacl_range_low_graph_183",
    "review_obligately_piezophilic_graph_183",
]

GRAPH_REVIEW_MODULES = [
    "review_biosafety_level_5_graph_183",
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(slug: str, doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{slug}: expected exactly one graph, found {len(graphs)}")
    return graphs[0]


def _replace_edges(
    slug: str,
    doc: dict[str, Any],
    replacements: list[dict[str, Any]],
) -> None:
    graph = _find_graph(slug, doc)
    by_key = {_edge_key(edge): edge for edge in replacements}
    seen: set[tuple[str | None, str | None, str | None]] = set()

    replaced_edges = []
    for edge in graph.get("edges") or []:
        key = _edge_key(edge)
        if key in by_key:
            seen.add(key)
            replaced_edges.append(copy.deepcopy(by_key[key]))
        else:
            replaced_edges.append(edge)

    missing = set(by_key) - seen
    if missing:
        raise ValueError(f"{slug}: missing replacement edge(s): {sorted(missing)}")

    graph["edges"] = replaced_edges


def _connector_edges(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, module.ADDED_EDGES


def _review_edges(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, [
        replacement["after"] for replacement in module.EDGE_REPLACEMENTS
    ]


def _graph(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, [module.AFTER_GRAPH]


def _path_for_slug(slug: str) -> Path:
    return REPO_ROOT / "data" / "traits" / f"{slug}.yaml"


def _event_changes(slug: str) -> str:
    if slug == "ecology/biosafety_level_5":
        return (
            "Addressed PR #664 adversarial review: expanded two terse SAE 2002 "
            "PPL-alpha snippets so the BSL-5 edge evidence identifies the exact "
            "BSL-4 comparison and closed-system sample-handling context."
        )
    if slug == "environment/nacl_range_low":
        return (
            "Addressed PR #664 adversarial review: replaced the unsupported "
            "compatible-solute bridge snippet with exact Bhowmick et al. wording "
            "that names both cation and compatible-solute accumulation after an "
            "external osmotic upshift."
        )
    if slug == "environment/obligately_piezophilic":
        return (
            "Addressed PR #664 adversarial review: replaced the HHP-damage "
            "snippet with exact Tamby et al. wording that supports "
            "high-pressure lipid-membrane integrity as piezophile adaptation."
        )
    if slug == "genomics/gc_low":
        return (
            "Addressed PR #664 adversarial review: replaced the copied GC-low "
            "connector snippet with exact Ruis et al. wording defining a "
            "mutational spectrum as combined context-dependent substitution "
            "signatures."
        )
    return (
        "Addressed PR #664 adversarial review: replaced copied "
        "nonmechanistic bridge snippets with independent exact source snippets "
        "while preserving the existing connector edge scope."
    )


def _write_or_validate(path: Path, doc: dict[str, Any], write: bool) -> None:
    if write:
        write_validated_trait(doc, path)
        return
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(doc, Path(tmp) / path.name)


def repair(write: bool = False) -> int:
    changed: list[Path] = []
    graph_modules = {module: _graph for module in GRAPH_REVIEW_MODULES}
    edge_modules = {
        **{module: _connector_edges for module in CONNECTOR_MODULES},
        **{module: _review_edges for module in EDGE_REVIEW_MODULES},
    }

    for module_name, loader in {**edge_modules, **graph_modules}.items():
        slug, replacements = loader(module_name)
        path = _path_for_slug(slug)
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        before = copy.deepcopy(doc)

        if module_name in graph_modules:
            doc["causal_graphs"] = copy.deepcopy(replacements)
        else:
            _replace_edges(slug, doc, replacements)

        record_curation_event(
            doc,
            curator="codex",
            action=ACTION,
            changes=_event_changes(slug),
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )

        if doc == before:
            continue

        _write_or_validate(path, doc, write)
        changed.append(path)

    for path in changed:
        print(f"  repair {path.relative_to(REPO_ROOT)}")
    print(
        f"{'applied' if write else 'dry run'}: repaired {len(changed)} record(s)"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return repair(write=parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
