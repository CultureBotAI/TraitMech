#!/usr/bin/env python3
"""Connect five fragmented phototrophy graphs for issue #183."""

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

TIMESTAMP = "2026-08-31T10:15:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
EXPECTED_COMPONENTS = {
    "physiology/photoheterotrophic": 2,
    "physiology/photolithoautotrophic": 3,
    "physiology/photolithotrophic": 3,
    "physiology/photoorganoheterotrophic": 3,
    "physiology/phototrophic": 2,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "physiology/photoheterotrophic": [{
        "subject": "proteorhodopsin",
        "predicate": "enables",
        "object": "proteorhodopsin_proton_pumping",
        "description": (
            "Proteorhodopsin directly enables the light-powered proton-pumping "
            "process in the retinal phototrophy branch."
        ),
        "evidence": [{
            "reference": "DOI:10.1073/pnas.0611035104",
            "snippet": "Proteorhodopsin (PR) is a light-powered proton pump",
            "notes": "Verified against the public PNAS article full text.",
        }],
        "predicate_id": "RO:0002327",
    }],
    "physiology/photolithoautotrophic": [
        {
            "subject": "sulfide",
            "predicate": "example of",
            "object": "inorganic_electron_donor",
            "description": (
                "Sulfide is a reduced inorganic electron donor used by anoxygenic "
                "photolithoautotrophs."
            ),
            "evidence": [{
                "reference": "DOI:10.3390/antiox10060829",
                "snippet": (
                    "These donors may be reduced sulfur compounds such as hydrogen "
                    "sulfide"
                ),
                "notes": "Verified against the open Antioxidants article full text.",
            }],
            "predicate_id": "rdfs:subClassOf",
        },
        {
            "subject": "bicarbonate",
            "predicate": "participates in",
            "object": "autotrophic_co2_fixation",
            "description": (
                "Transported bicarbonate supplies inorganic carbon for photosynthetic "
                "autotrophic fixation."
            ),
            "evidence": [{
                "reference": "DOI:10.1073/pnas.0405211101",
                "snippet": (
                    "cyanobacteria have evolved a very efficient mechanism for capturing "
                    "CO2 and HCO3- for photosynthetic fixation into sugars"
                ),
                "notes": "Verified against the public PNAS article full text.",
            }],
            "predicate_id": "biolink:participates_in",
        },
    ],
    "physiology/photolithotrophic": [
        {
            "subject": "hydrogen_sulfide",
            "predicate": "participates in",
            "object": "hydrogen_sulfide_oxidation",
            "description": (
                "Hydrogen sulfide is the substrate oxidized to elemental sulfur in "
                "the sulfur-photolithotrophy branch."
            ),
            "evidence": [{
                "reference": "DOI:10.3390/antiox10060829",
                "snippet": (
                    "The process of anoxygenic photosynthesis further involves the "
                    "oxidation of hydrogen sulfide to atomic sulfur"
                ),
                "notes": "Verified against the open Antioxidants article full text.",
            }],
            "predicate_id": "biolink:participates_in",
        },
        {
            "subject": "ferrous_iron",
            "predicate": "participates in",
            "object": "ferrous_iron_oxidation",
            "description": (
                "Ferrous iron is the electron-source substrate oxidized during "
                "photoferrotrophy."
            ),
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2014.00713",
                "snippet": (
                    "photoferrotrophic bacteria use light as energy and Fe(II) as an "
                    "electron source for carbon fixation and biomass formation"
                ),
                "notes": "Verified against the open Frontiers primary article.",
            }],
            "predicate_id": "biolink:participates_in",
        },
    ],
    "physiology/photoorganoheterotrophic": [
        {
            "subject": "fe_s_electron_transfer",
            "predicate": "contributes to",
            "object": "photosynthetic_electron_transport",
            "description": (
                "Electron transfer through Type I reaction-center Fe-S acceptors "
                "contributes to photosynthetic electron transport."
            ),
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2021.735666",
                "snippet": (
                    "The electron transfer pathway(s) in Type I RCs utilize iron-sulfur "
                    "([4Fe-4S]) clusters"
                ),
                "notes": "Verified against the open Frontiers article full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "diurnal_cycle",
            "predicate": "modulates",
            "object": "stationary_phase_survival",
            "description": (
                "The dark-light regime modulates stationary-phase survival in the "
                "facultative phototroph model."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s43705-023-00334-5",
                "snippet": (
                    "bacterial survival in stationary phase relies on functional "
                    "reaction centers and varies depending on the light regime"
                ),
                "notes": "Verified against the open primary article full text.",
            }],
            "predicate_id": "RO:0002211",
        },
    ],
    "physiology/phototrophic": [{
        "subject": "ion_transport",
        "predicate": "generates",
        "object": "proton_motive_force",
        "description": (
            "Light-driven proton transport by proteorhodopsin generates proton motive "
            "force in the retinal phototrophy branch."
        ),
        "evidence": [{
            "reference": "DOI:10.1073/pnas.0611035104",
            "snippet": (
                "Light-based proton pumping by proteorhodopsin can then increase the pmf"
            ),
            "notes": "Verified against the public PNAS article full text.",
        }],
        "predicate_id": "biolink:produces",
    }],
}


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    existing = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    expected = {_edge_key(edge): edge for edge in additions}
    present = set(existing) & set(expected)
    before = _components(graph)
    if before == 1:
        if present != set(expected):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        for key, edge in expected.items():
            if existing[key] != edge:
                raise ValueError(f"{slug}: connector drifted after migration: {key}")
        return False
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}")
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if any(not item.get("reference") or not item.get("snippet") for item in evidence) or not evidence:
            raise ValueError(f"{slug}: connector lacks source/snippet evidence: {key}")
        graph.setdefault("edges", []).append(edge)
    if _components(graph) != 1:
        raise ValueError(f"{slug}: repair did not reach one component")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            f"with {len(additions)} public-source, verbatim-snippet-backed connector(s). "
            "No paid research service was called."
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
        doc = yaml.safe_load(path.read_text()) or {}
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
