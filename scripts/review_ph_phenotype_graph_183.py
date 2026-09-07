#!/usr/bin/env python3
"""Review pH numerical-limits graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ph_phenotype_graph_183.py
    python scripts/review_ph_phenotype_graph_183.py --apply
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

SLUG = "environment/ph_phenotype_with_numerical_limits"
GRAPH_ID = "ph_phenotype_numerical_axis"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T02:20:00Z"

RECORD_EVIDENCE_BEFORE: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1038/nrmicro2549",
        "snippet": "external pH",
        "notes": (
            "pH-homeostasis review supports external pH as the quantitative axis "
            "underlying acidophile, neutrophile, and alkaliphile classification."
        ),
    },
    {
        "reference": "DOI:10.1016/j.tim.2007.02.005",
        "snippet": "proton motive force",
        "notes": (
            "pH-homeostasis review supports the proton motive force across the cell "
            "envelope as the physical link between external pH and microbial growth "
            "physiology."
        ),
    },
]

RECORD_EVIDENCE_AFTER: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1038/nrmicro2549",
        "snippet": "grow at external pH values",
        "notes": (
            "Verified against the open PMC manuscript of the Krulwich et al. review; "
            "external pH is the quantitative environmental axis represented by "
            "pH-growth numerical-limit phenotypes."
        ),
    },
    RECORD_EVIDENCE_BEFORE[1],
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "external_ph_axis",
            "predicate": "defines",
            "object": "ph_phenotype_trait",
            "description": "External pH is the quantitative axis defining pH phenotypes.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "external pH",
                    "notes": (
                        "Supports external pH as the standard descriptor axis for "
                        "microbial pH phenotypes."
                    ),
                }
            ],
            "predicate_id": "METPO:2007500",
        },
        "after": {
            "subject": "external_ph_axis",
            "predicate": "defines",
            "object": "ph_phenotype_trait",
            "description": "External pH is the quantitative axis defining pH phenotypes.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro2549",
                    "snippet": "external pH values that are outside",
                    "notes": (
                        "Verified against the open PMC manuscript of the Krulwich "
                        "et al. review; microbial pH phenotypes are expressed "
                        "relative to external growth pH values and internal "
                        "pH-homeostatic limits."
                    ),
                }
            ],
            "predicate_id": "METPO:2007500",
        },
    },
    {
        "before": {
            "subject": "external_ph_axis",
            "predicate": "determines",
            "object": "proton_motive_force",
            "description": (
                "External pH determines the proton motive force across the cell envelope."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Neutralophilic bacteria maintain a relatively constant "
                        "proton motive force across external pH ~5-8."
                    ),
                }
            ],
        },
        "after": {
            "subject": "external_ph_axis",
            "predicate": "regulates",
            "object": "proton_motive_force",
            "description": (
                "External pH influences the proton motive force across the cell envelope."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "pH gradient is largely determined",
                    "notes": (
                        "Verified against the open Poolman review; maintaining "
                        "near-neutral cytoplasmic pH makes external pH a major "
                        "determinant of the transmembrane pH-gradient component of "
                        "the PMF."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "f0f1_atpase",
            "predicate": "enables",
            "object": "atp_synthesis_from_pmf",
            "description": "F0F1-ATPase couples the proton motive force to ATP synthesis.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "F0F1-ATP synthase typically uses 3-5 protons per ATP, "
                        "linking PMF to ATP synthesis and pH homeostasis."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "na_h_antiport_activity",
            "predicate": "regulates",
            "object": "internal_ph_pmf",
            "description": "Na+/H+ antiporter activity regulates internal pH and PMF.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Main regulators of internal pH/PMF include Na+/H+ and "
                        "K+/H+ antiporters (general bacteria)."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "na_h_antiport_activity",
            "predicate": "regulates",
            "object": "internal_ph_pmf",
            "description": "Na+/H+ antiporter activity regulates internal pH and PMF.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "snippet": "Na+/H+ and K+/H+ antiporters",
                    "notes": (
                        "Verified against the open Poolman review; Na+/H+ "
                        "antiporters are listed as key bacterial pH-homeostasis "
                        "regulators."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "k_h_antiporter",
            "predicate": "regulates",
            "object": "internal_ph_pmf",
            "description": "K+/H+ antiporter activity regulates internal pH and PMF.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Main regulators of internal pH/PMF include Na+/H+ and "
                        "K+/H+ antiporters (general bacteria)."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
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
    },
    {
        "before": {
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
                    "notes": (
                        "Decarboxylation reaction consumes a proton, raising internal "
                        "pH; the equivalent of 1 proton is pumped per molecule "
                        "decarboxylated. Broad across amino-acid decarboxylase "
                        "systems."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "phosphate_buffering",
            "predicate": "stabilizes",
            "object": "internal_ph",
            "description": (
                "Cytoplasmic phosphate pools buffer protons and stabilize internal pH."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuad033",
                    "notes": (
                        "Cytoplasmic buffering is important; L. lactis has ~100 mM "
                        "organic/inorganic phosphates (general bacteria)."
                    ),
                }
            ],
        },
        "after": {
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


def _assert_record_evidence(
    doc: dict[str, Any], expected: list[dict[str, Any]], state: str
) -> None:
    if doc.get("evidence") != expected:
        raise ValueError(f"{SLUG}: {state} record evidence drifted")


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
    record_evidence_migrated = doc.get("evidence") == RECORD_EVIDENCE_AFTER

    if record_evidence_migrated and _has_exact_edges(graph, after_edges):
        return False

    if present_migrated_keys == migrated_keys and record_evidence_migrated:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_keys or record_evidence_migrated:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_keys)}")

    _assert_record_evidence(doc, RECORD_EVIDENCE_BEFORE, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    doc["evidence"] = copy.deepcopy(RECORD_EVIDENCE_AFTER)
    graph["edges"] = [
        copy.deepcopy(after_by_before_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the ph_phenotype_numerical_axis graph for issue #183: added "
            "snippets to 1 record-level and 7 edge-level evidence items, and "
            "grounded 2 unmapped pH-axis predicates to RO:0002211 or RO:0002326. "
            "No paid research service was called."
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
