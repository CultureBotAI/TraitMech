#!/usr/bin/env python3
"""Connect eight two-component metabolism graphs for issue #183.

Every connector was checked against freely available public article text. The
migration is dry-run by default, validates every rendered record before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_metabolism_two_component_graphs_183.py
    python scripts/connect_metabolism_two_component_graphs_183.py --apply
"""

from __future__ import annotations

import argparse
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

TIMESTAMP = "2026-08-31T08:20:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

EXPECTED_COMPONENTS = {
    "metabolism/dicarboxylate_four_hydroxybutyrate_cycle": 2,
    "metabolism/dissimilatory_sulfate_reduction": 2,
    "metabolism/homoacetogenesis": 2,
    "metabolism/mixed_acid_fermentation": 2,
    "metabolism/photosynthesis": 2,
    "metabolism/phototrophy": 2,
    "metabolism/respiration": 2,
    "metabolism/syntrophy": 2,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "metabolism/dicarboxylate_four_hydroxybutyrate_cycle": [
        {
            "subject": "pep_carboxylase",
            "predicate": "contributes to",
            "object": "dc_four_hb_trait",
            "description": (
                "PEP carboxylase performs one of the two carboxylating reactions "
                "that constitute the DC/4HB carbon-fixation cycle."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/AEM.02473-10",
                "snippet": (
                    "In the DC/HB cycle, pyruvate synthase and PEP carboxylase "
                    "are the two carboxylating enzymes"
                ),
                "notes": (
                    "Verified against the public PMC full text; contributes-to does "
                    "not claim that PEP carboxylase alone is sufficient for the cycle."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "metabolism/dissimilatory_sulfate_reduction": [
        {
            "subject": "sulfate",
            "predicate": "participates in",
            "object": "sulfate_reduction_trait",
            "description": (
                "Sulfate participates in dissimilatory sulfate reduction as the "
                "alternative terminal electron acceptor."
            ),
            "evidence": [{
                "reference": "DOI:10.3390/antiox12030767",
                "snippet": (
                    "Sulfate can be used as an alternative terminal electron "
                    "acceptor under anaerobic conditions"
                ),
                "notes": (
                    "Verified against the public PMC full text; this bridges the "
                    "named respiratory trait to its existing Sat-Apr-Dsr pathway."
                ),
            }],
            "predicate_id": "biolink:participates_in",
        },
    ],
    "metabolism/homoacetogenesis": [
        {
            "subject": "methyl_branch",
            "predicate": "part of",
            "object": "wood_ljungdahl_pathway",
            "description": (
                "The methyl branch is one of the two converging branches of the "
                "Wood-Ljungdahl pathway."
            ),
            "evidence": [{
                "reference": "DOI:10.1186/s13068-024-02554-w",
                "snippet": (
                    "The WLP, which was elucidated over decades, proceeds through "
                    "two branches"
                ),
                "notes": (
                    "Verified against the public PMC full text; the existing edge "
                    "between methyl and carbonyl branches keeps both branches connected."
                ),
            }],
            "predicate_id": "biolink:part_of",
        },
    ],
    "metabolism/mixed_acid_fermentation": [
        {
            "subject": "acetyl_coa",
            "predicate": "is metabolized by",
            "object": "pta_acka",
            "description": (
                "The Pta/AckA enzyme pair metabolizes acetyl-CoA through the "
                "acetate-producing branch of mixed-acid fermentation."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/iai.00176-23",
                "snippet": (
                    "Acetyl-CoA is further metabolized by Pta and AckA to generate "
                    "acetate"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
        },
    ],
    "metabolism/photosynthesis": [
        {
            "subject": "electron_transport",
            "predicate": "contributes to",
            "object": "reducing_power",
            "description": (
                "Photosynthetic electron-transfer reactions contribute the NADPH "
                "reducing power used by downstream carbon fixation."
            ),
            "evidence": [{
                "reference": "DOI:10.1111/1751-7915.14519",
                "snippet": (
                    "NADPH and ATP are produced from a proton gradient formed "
                    "coincident with the electron transfer reactions and fuel "
                    "downstream processes, including carbon fixation"
                ),
                "notes": (
                    "Verified against the public PMC full text; the passage describes "
                    "the oxygenic branch represented by the existing PSII node."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "metabolism/phototrophy": [
        {
            "subject": "photosystem_ii",
            "predicate": "contributes to",
            "object": "phototrophy_trait",
            "description": (
                "Photosystem II contributes the light-sensing and reaction-center "
                "machinery of the graph's oxygenic phototrophy branch."
            ),
            "evidence": [{
                "reference": "DOI:10.1111/1751-7915.14519",
                "snippet": (
                    "Both photosystems bind chlorophylls to sense light, use "
                    "chlorophylls and other pigments to transfer light to a "
                    "photosynthetic reaction centre"
                ),
                "notes": (
                    "Verified against the public PMC full text; the description "
                    "keeps this connector scoped to oxygenic phototrophy."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "metabolism/respiration": [
        {
            "subject": "membrane_electron_transport_chain",
            "predicate": "contributes to",
            "object": "respiration_trait",
            "description": (
                "The membrane respiratory chain contributes donor-to-acceptor "
                "electron flow to the respiration trait."
            ),
            "evidence": [{
                "reference": "DOI:10.3390/ijms252413421",
                "snippet": (
                    "Ubiquinol, produced by complex I, passes those reducing "
                    "equivalents down the respiratory chain to the terminal "
                    "acceptor—oxygen"
                ),
                "notes": (
                    "Verified against the public PMC full text; the connector "
                    "represents the aerobic branch without excluding alternative acceptors."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "metabolism/syntrophy": [
        {
            "subject": "direct_interspecies_electron_transfer",
            "predicate": "mediates",
            "object": "syntrophy_trait",
            "description": (
                "Direct interspecies electron transfer is one mechanism that can "
                "mediate syntrophic growth without diffusible hydrogen or formate."
            ),
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2016.00236",
                "snippet": (
                    "Direct interspecies electron transfer (DIET) has been recognized "
                    "as an alternative to interspecies H2 transfer as a mechanism for "
                    "syntrophic growth"
                ),
                "notes": (
                    "Verified against the freely available primary-study abstract; "
                    "the edge does not assert that DIET occurs in every syntrophic pair."
                ),
            }],
        },
    ],
}


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    expected_by_key = {_edge_key(edge): edge for edge in additions}
    present = set(existing_by_key) & set(expected_by_key)

    before = _components(graph)
    if before == 1:
        if present != set(expected_by_key):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        for key, expected in expected_by_key.items():
            if existing_by_key[key] != expected:
                raise ValueError(f"{slug}: connector drifted after migration: {key}")
        return False
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(
            f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}"
        )
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")

    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{slug}: connector lacks source/snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{slug}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            f"using {len(additions)} public-source, verbatim-snippet-backed "
            "connector(s). No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    for slug in sorted(ADDITIONS):
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not transform(slug, doc):
            continue
        changed += 1
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
