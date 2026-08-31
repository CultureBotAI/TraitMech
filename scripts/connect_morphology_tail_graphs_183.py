#!/usr/bin/env python3
"""Connect the six remaining fragmented morphology graphs for issue #183.

All 21 connectors were checked against freely available public source text.
The migration is dry-run by default, validates every rendered record before
writing, rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_morphology_tail_graphs_183.py
    python scripts/connect_morphology_tail_graphs_183.py --apply
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

TIMESTAMP = "2026-08-31T06:48:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

EXPECTED_COMPONENTS = {
    "morphology/magnetosome": 4,
    "morphology/polyhydroxyalkanoate_granule": 4,
    "morphology/spore_forming": 4,
    "morphology/spore_shaped": 5,
    "morphology/sporulation": 6,
    "morphology/twitching_motility": 4,
}

NODE_UPDATES = {
    "morphology/magnetosome": {
        "magnetite_magnetosome": {
            "before": {
                "label": "magnetite magnetosome",
                "description": "Magnetosome containing a magnetite (Fe3O4) crystal.",
            },
            "after": {
                "label": "magnetite crystal",
                "description": (
                    "Iron oxide magnetite (Fe3O4) crystal contained within a "
                    "magnetosome."
                ),
            },
        },
        "greigite_magnetosome": {
            "before": {
                "label": "greigite magnetosome",
                "description": "Magnetosome containing a greigite (Fe3S4) crystal.",
            },
            "after": {
                "label": "greigite crystal",
                "description": (
                    "Iron sulfide greigite (Fe3S4) crystal contained within a "
                    "magnetosome."
                ),
            },
        },
    },
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "morphology/magnetosome": [
        {
            "subject": "membrane_invagination",
            "predicate": "precedes",
            "object": "biomineralization",
            "description": (
                "Magnetosome-membrane invagination forms the vesicle before mineral "
                "biomineralization begins."
            ),
            "evidence": [{
                "reference": "DOI:10.1111/mmi.15330",
                "snippet": (
                    "Biomineralization of magnetite crystals occurs after the "
                    "formation of magnetosome vesicles"
                ),
                "notes": (
                    "Verified against the public PMC full text; this orders two "
                    "existing biogenesis stages without asserting simultaneity is impossible."
                ),
            }],
        },
        {
            "subject": "magnetite_magnetosome",
            "predicate": "located in",
            "object": "magnetosome_trait",
            "description": "Magnetite is one mineral-crystal form contained by magnetosomes.",
            "evidence": [{
                "reference": "DOI:10.1111/mmi.15330",
                "snippet": (
                    "The structure and morphology of magnetosomes differ across all "
                    "MTB species, with some producing iron oxide magnetite (Fe3O4)"
                ),
                "notes": (
                    "Verified against the public PMC full text; the node wording is "
                    "tightened from a whole organelle to its mineral crystal."
                ),
            }],
            "predicate_id": "biolink:located_in",
        },
        {
            "subject": "greigite_magnetosome",
            "predicate": "located in",
            "object": "magnetosome_trait",
            "description": "Greigite is one mineral-crystal form contained by magnetosomes.",
            "evidence": [{
                "reference": "DOI:10.1111/mmi.15330",
                "snippet": (
                    "others synthesizing iron sulfide greigite (Fe3S4), and some "
                    "capable of producing both, depending on their environmental conditions"
                ),
                "notes": (
                    "Verified against the public PMC full text; the environmental "
                    "preference remains explicitly contextual."
                ),
            }],
            "predicate_id": "biolink:located_in",
        },
    ],
    "morphology/polyhydroxyalkanoate_granule": [
        {
            "subject": "pha_accumulation",
            "predicate": "contributes to",
            "object": "pha_granule_trait",
            "description": (
                "Intracellular accumulation of amorphous PHA produces the polymer "
                "body represented by the granule trait."
            ),
            "evidence": [{
                "reference": "DOI:10.1016/j.jbc.2024.107523",
                "snippet": (
                    "When synthetized, PHA aggregates in an amorphous state surrounded "
                    "by several PHA granule-associated proteins forming the so called "
                    "carbonosomes"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "phb_mobilization",
            "predicate": "contributes to",
            "object": "carbon_energy_storage",
            "description": (
                "Mobilization makes stored PHA available for utilization and is part "
                "of the granule's carbon-and-energy reserve function."
            ),
            "evidence": [{
                "reference": "DOI:10.1016/j.jbc.2024.107523",
                "snippet": (
                    "Phasins and PHA degrading enzymes are important for PHA storage "
                    "and utilization"
                ),
                "notes": (
                    "Verified against the open Europe PMC full text; the edge covers "
                    "reserve utilization rather than claiming degradation creates storage."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "phb_degradation",
            "predicate": "contributes to",
            "object": "phb_mobilization",
            "description": "Degradation of accumulated PHB contributes to reserve mobilization.",
            "evidence": [{
                "reference": "DOI:10.1016/j.jbc.2024.107523",
                "snippet": (
                    "reduced ppGpp alarmone levels leading to enhanced degradation of "
                    "PHA suggesting that ppGpp acts as repressor of the PHA mobilization "
                    "system (PhaZ1)"
                ),
                "notes": (
                    "Verified against the open Europe PMC full text; the connector "
                    "links the existing starvation/degradation and PhaZ/mobilization branches."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "morphology/spore_forming": [
        {
            "subject": "forespore_engulfment",
            "predicate": "contributes to",
            "object": "resistant_endospore",
            "description": (
                "Forespore engulfment is a morphogenetic stage leading into maturation "
                "of the resistant endospore."
            ),
            "evidence": [{
                "reference": "DOI:10.1101/gad.1335705",
                "snippet": (
                    "engulfment of the forespore by the mother cell; maturation of the "
                    "developing (fore)spore; and, finally, release of the ripened spore"
                ),
                "notes": "Verified against the freely available primary article full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "coat_assembly",
            "predicate": "contributes to",
            "object": "resistant_endospore",
            "description": (
                "Assembly of the multilayered coat contributes the protein shell of "
                "the resistant endospore."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/nrmicro2921",
                "snippet": (
                    "the spore coat, which consists of four layers: the basement layer "
                    "(blue), inner coat (orange), outer coat (purple) and crust (red)"
                ),
                "notes": "Verified against the public PMC author-manuscript full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "spo0a_phosphorylated",
            "predicate": "contributes to",
            "object": "spore_forming_trait",
            "description": (
                "Accumulation of active Spo0A~P is a required regulatory contribution "
                "to entry into the spore-forming program."
            ),
            "evidence": [{
                "reference": "DOI:10.1101/gad.1335705",
                "snippet": (
                    "Evidence indicates that this gradual increase in Spo0A protein and "
                    "activity plays a critical role in triggering sporulation and "
                    "requires the action of the phosphorelay"
                ),
                "notes": (
                    "Verified against the freely available article; contributes-to "
                    "does not claim Spo0A~P alone is sufficient."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "morphology/spore_shaped": [
        {
            "subject": "spore_encasement",
            "predicate": "contributes to",
            "object": "mature_spore_body",
            "description": (
                "Encasement changes the coat scaffold into the complete shell of the "
                "mature spore body."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/nrmicro2921",
                "snippet": (
                    "SpoVM and SpoVID are crucial for the transition from a single cap "
                    "to a full spherical shell that encases the spore"
                ),
                "notes": "Verified against the public PMC author-manuscript full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "outer_coat",
            "predicate": "part of",
            "object": "spore_coat_surface",
            "description": "The outer coat is a structural layer of the spore coat.",
            "evidence": [{
                "reference": "DOI:10.1038/nrmicro2921",
                "snippet": (
                    "Three layers of the B. subtilis spore coat are observed in "
                    "thin-section electron microscopy: a lamellar inner coat, a more "
                    "coarsely layered outer coat and a recently identified layer named "
                    "the crust"
                ),
                "notes": "Verified against the public PMC author-manuscript full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "inner_coat",
            "predicate": "part of",
            "object": "spore_coat_surface",
            "description": "The inner coat is a structural layer of the spore coat.",
            "evidence": [{
                "reference": "DOI:10.1038/nrmicro2921",
                "snippet": (
                    "The core is protected by the cortex (green) and the spore coat, "
                    "which consists of four layers"
                ),
                "notes": "Verified against the public PMC author-manuscript full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "spore_coat_surface",
            "predicate": "part of",
            "object": "mature_spore_body",
            "description": "The spore coat forms a shell attached around the mature forespore.",
            "evidence": [{
                "reference": "DOI:10.1038/nrmicro2921",
                "snippet": (
                    "the coat did not form a shell of protein around the forespore and "
                    "was often found detached from the forespore surface"
                ),
                "notes": (
                    "Verified against the public PMC author manuscript; mutant failure "
                    "defines the normal coat-shell attachment represented by this edge."
                ),
            }],
            "predicate_id": "biolink:part_of",
        },
    ],
    "morphology/sporulation": [
        {
            "subject": "chromosome_translocation",
            "predicate": "precedes",
            "object": "forespore_engulfment",
            "description": (
                "Chromosome translocation after asymmetric division precedes completion "
                "of forespore engulfment."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-51654-6",
                "snippet": (
                    "After asymmetric division and chromosome translocation, genes in "
                    "σF and σE regulons drive metabolic and morphological changes to "
                    "the cell which conclude in forespore engulfment"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
        },
        {
            "subject": "cell_within_cell_state",
            "predicate": "contributes to",
            "object": "forespore_maturation",
            "description": (
                "The engulfed cell-within-a-cell state permits activation of the late "
                "forespore program responsible for maturation."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-51654-6",
                "snippet": (
                    "This is required for activation of the late sporulation spore "
                    "specific sigma factor σG responsible for spore maturation, spore "
                    "DNA protection via Ssp proteins and preparation for germination"
                ),
                "notes": (
                    "In the source, 'This' immediately follows the cell-within-a-cell "
                    "state created by forespore engulfment."
                ),
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "sigma_f",
            "predicate": "part of",
            "object": "compartment_sigma_factors",
            "description": "Sigma F is one of the compartment-specific sporulation factors.",
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-51654-6",
                "snippet": (
                    "compartment specific RNA polymerase sigma factors – σF and σE – "
                    "responsible for further activation of sporulation genes in the "
                    "forespore and mother cell respectively"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "sigma_g",
            "predicate": "positively regulates",
            "object": "forespore_maturation",
            "description": "Late forespore sigma G drives the spore-maturation program.",
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-51654-6",
                "snippet": (
                    "the late sporulation spore specific sigma factor σG responsible "
                    "for spore maturation, spore DNA protection via Ssp proteins and "
                    "preparation for germination"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002213",
        },
        {
            "subject": "sigma_k",
            "predicate": "contributes to",
            "object": "forespore_maturation",
            "description": (
                "Late mother-cell sigma K contributes coat and cortex maturation to "
                "the developing spore."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-51654-6",
                "snippet": (
                    "Finally, the late mother cell σK activation, regulated by σG, "
                    "results in spore coat and cortex maturation, preparation for "
                    "germination and eventually, mother cell lysis"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "morphology/twitching_motility": [
        {
            "subject": "pilus_extension",
            "predicate": "contributes to",
            "object": "pilus_assembly",
            "description": (
                "Extension polymerizes pilin subunits into the assembled type IV pilus fiber."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/jb.00359-24",
                "snippet": (
                    "PilA subunits are ultimately extracted from their reservoir in "
                    "the cytoplasmic membrane and polymerized to form a pilus fiber"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "pilus_filament_surface_exposure",
            "predicate": "contributes to",
            "object": "type_iv_pilus",
            "description": (
                "Extrusion through the secretin exposes the assembled type IV pilus "
                "beyond the outer membrane."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/jb.00359-24",
                "snippet": (
                    "The pilus is extruded through the periplasm, guided by the "
                    "cylindrical alignment subcomplex, and finally through a gated "
                    "secretin pore in the outer membrane"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "t4p_machine",
            "predicate": "enables",
            "object": "pilus_assembly",
            "description": (
                "The envelope-spanning type IV pilus machine enables motor-driven "
                "assembly and disassembly of the pilus filament."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41467-024-53638-y",
                "snippet": (
                    "PilC is the inner membrane platform protein that coordinates with "
                    "ATPase motors to drive assembly and disassembly of major pilin "
                    "subunits into the extending and retracting pilus, respectively"
                ),
                "notes": "Verified against the open Europe PMC full text.",
            }],
            "predicate_id": "RO:0002327",
        },
    ],
}


def _node_map(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {node["node_id"]: node for node in graph.get("nodes") or []}


def _update_nodes(slug: str, graph: dict[str, Any], *, migrated: bool) -> None:
    nodes = _node_map(graph)
    for node_id, update in NODE_UPDATES.get(slug, {}).items():
        node = nodes.get(node_id)
        if node is None:
            raise ValueError(f"{slug}: node-update target missing: {node_id}")
        expected = update["after"] if migrated else update["before"]
        actual = {field: node.get(field) for field in expected}
        if actual != expected:
            raise ValueError(f"{slug}: node metadata drifted for {node_id}: {actual!r}")
        if not migrated:
            node.update(update["after"])


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
        _update_nodes(slug, graph, migrated=True)
        return False
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(
            f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}"
        )
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")

    _update_nodes(slug, graph, migrated=False)
    node_ids = set(_node_map(graph))
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
            f"using {len(additions)} source- and verbatim-snippet-backed connector(s). "
            + (
                "Clarified the magnetite and greigite nodes as mineral crystals "
                "contained within magnetosomes. "
                if slug == "morphology/magnetosome"
                else ""
            )
            + "No paid research service was called."
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
