#!/usr/bin/env python3
"""Connect six fragmented metabolism pathway spines for issue #183.

All 17 connectors were checked against freely available public article text.
The migration is dry-run by default, validates before writing, rejects partial
replay and metadata drift, and is exactly idempotent.
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

TIMESTAMP = "2026-08-31T09:00:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"

EXPECTED_COMPONENTS = {
    "metabolism/calvin_benson_bassham_cycle": 3,
    "metabolism/methanogenesis": 4,
    "metabolism/oxygenic_photosynthesis": 3,
    "metabolism/propionic_acid_fermentation": 4,
    "metabolism/three_hydroxypropionate_bicycle": 5,
    "metabolism/wood_ljungdahl_pathway": 4,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "metabolism/calvin_benson_bassham_cycle": [
        {
            "subject": "cbb_operon",
            "predicate": "part of",
            "object": "cbb_pathway",
            "description": "The cbb operon specifies enzymes of the CBB pathway.",
            "evidence": [{
                "reference": "DOI:10.1128/JB.00442-15",
                "snippet": (
                    "cbb operons that specify enzymes of the "
                    "Calvin-Bassham-Benson (CBB) pathway"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "co2_leakage",
            "predicate": "negatively regulates",
            "object": "cbb_pathway",
            "description": (
                "CO2 leakage opposes the carboxysome concentration mechanism that "
                "supplies Rubisco for the CBB pathway."
            ),
            "evidence": [{
                "reference": "DOI:10.1371/journal.pone.0007521",
                "snippet": (
                    "the carboxysome shell constitutes a diffusional barrier for "
                    "CO2, thereby preventing leakage of this Ci species out of the "
                    "microcompartment"
                ),
                "notes": (
                    "Verified against the public PMC full text; the same introduction "
                    "identifies Rubisco as catalyzing the first CBB-cycle step."
                ),
            }],
            "predicate_id": "RO:0002212",
        },
    ],
    "metabolism/methanogenesis": [
        {
            "subject": "carbon_dioxide",
            "predicate": "participates in",
            "object": "methanogenesis_trait",
            "description": "CO2 is the carbon substrate of hydrogenotrophic methanogenesis.",
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2017.01198",
                "snippet": (
                    "Three major methanogenic pathways are known based on the type "
                    "of carbon sources catabolized, i.e., hydrogenotrophic "
                    "methanogenesis using CO2 and H2"
                ),
                "notes": "Verified against the freely available article full text.",
            }],
            "predicate_id": "biolink:participates_in",
        },
        {
            "subject": "acetoclastic_methanogenesis",
            "predicate": "part of",
            "object": "methanogenesis_trait",
            "description": "Acetoclastic methanogenesis is an acetate-using branch.",
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2017.01198",
                "snippet": (
                    "hydrogenotrophic methanogenesis using CO2 and H2, acetoclastic "
                    "methanogenesis using acetate"
                ),
                "notes": "Verified against the freely available article full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
        {
            "subject": "methyl_based_methanogenesis",
            "predicate": "part of",
            "object": "methanogenesis_trait",
            "description": "Methylotrophic methanogenesis is a methyl-substrate branch.",
            "evidence": [{
                "reference": "DOI:10.3389/fmicb.2017.01198",
                "snippet": (
                    "acetoclastic methanogenesis using acetate, and methylotrophic "
                    "methanogenesis using methylated compounds, such as methanol, "
                    "methylamines"
                ),
                "notes": "Verified against the freely available article full text.",
            }],
            "predicate_id": "biolink:part_of",
        },
    ],
    "metabolism/oxygenic_photosynthesis": [
        {
            "subject": "photosystem_ii",
            "predicate": "contributes to",
            "object": "oxygenic_photosynthesis_trait",
            "description": "PSII supplies the water-oxidation entry point.",
            "evidence": [{
                "reference": "DOI:10.1007/s11120-019-00648-3",
                "snippet": (
                    "The electrons for this process originate from water oxidation "
                    "that takes place in PS II"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "ferredoxin",
            "predicate": "donates electrons to",
            "object": "fnr",
            "description": "Reduced ferredoxin transfers PSI electrons to FNR.",
            "evidence": [{
                "reference": "DOI:10.1039/D2SC01546C",
                "snippet": (
                    "Fd (or Fld) then shuttles the electrons from PSI to ferredoxin "
                    "NADP+-reductase (FNR) for the reduction of NADP+ to NADPH that "
                    "is used in carbon fixation"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
            "predicate_id": "METPO:2007403",
        },
    ],
    "metabolism/propionic_acid_fermentation": [
        {
            "subject": "pyruvate",
            "predicate": "contributes to",
            "object": "wood_werkman_cycle",
            "description": "Pyruvate carboxylation initiates the Wood-Werkman cycle.",
            "evidence": [{
                "reference": "DOI:10.3390/molecules31020333",
                "snippet": (
                    "It starts from pyruvate, generated via glycolysis, which can "
                    "follow two alternative routes: Carboxylation to oxaloacetate: "
                    "this initiates the Wood–Werkman cycle and leads to propionic acid"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "succinate",
            "predicate": "causally upstream of",
            "object": "succinyl_coa",
            "description": "The propionate pathway converts succinate through succinyl-CoA.",
            "evidence": [{
                "reference": "DOI:10.1186/s12864-016-3367-x",
                "snippet": (
                    "Succinate is then converted into succinyl-CoA, methyl malonyl "
                    "CoA, propanoyl CoA and propionate by specific enzymes"
                ),
                "notes": "Verified against the open article full text.",
            }],
        },
        {
            "subject": "mmc_carboxytransferase",
            "predicate": "catalyzes conversion of",
            "object": "pyruvate",
            "description": (
                "Methylmalonyl-CoA carboxytransferase catalyzes the pyruvate-to-"
                "oxaloacetate entry reaction."
            ),
            "evidence": [{
                "reference": "DOI:10.3390/molecules31020333",
                "snippet": (
                    "pyruvate is converted to oxaloacetate in a biotin-dependent "
                    "carboxyl transfer reaction catalyzed by methylmalonyl-CoA "
                    "carboxytransferase"
                ),
                "notes": "Verified against the public PMC full text.",
            }],
        },
    ],
    "metabolism/three_hydroxypropionate_bicycle": [
        {
            "subject": "acetyl_coa_carboxylase",
            "predicate": "contributes to",
            "object": "three_hp_bicycle_trait",
            "description": "Acetyl-CoA carboxylase is an enzyme of the 3HP bicycle.",
            "evidence": [{
                "reference": "DOI:10.1128/AEM.02473-10",
                "snippet": (
                    "The 3-hydroxypropionate (Fuchs-Holo) bi-cycle. Enzymes: 1, "
                    "acetyl-CoA carboxylase"
                ),
                "notes": "Verified against the public PMC figure caption.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "malonyl_coa_reductase",
            "predicate": "contributes to",
            "object": "three_hp_bicycle_trait",
            "description": "Malonyl-CoA reductase is an enzyme of the 3HP bicycle.",
            "evidence": [{
                "reference": "DOI:10.1128/AEM.02473-10",
                "snippet": (
                    "Enzymes: 1, acetyl-CoA carboxylase; 2, malonyl-CoA reductase"
                ),
                "notes": "Verified against the public PMC figure caption.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "propionyl_coa_synthase",
            "predicate": "contributes to",
            "object": "three_hp_bicycle_trait",
            "description": "Propionyl-CoA synthase is an enzyme of the 3HP bicycle.",
            "evidence": [{
                "reference": "DOI:10.1128/AEM.02473-10",
                "snippet": (
                    "Enzymes: 1, acetyl-CoA carboxylase; 2, malonyl-CoA reductase; "
                    "3, propionyl-CoA synthase"
                ),
                "notes": "Verified against the public PMC figure caption.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "propionyl_coa_carboxylase",
            "predicate": "contributes to",
            "object": "three_hp_bicycle_trait",
            "description": "Propionyl-CoA carboxylase is an enzyme of the 3HP bicycle.",
            "evidence": [{
                "reference": "DOI:10.1128/AEM.02473-10",
                "snippet": (
                    "malonyl-CoA reductase; 3, propionyl-CoA synthase; 4, "
                    "propionyl-CoA carboxylase"
                ),
                "notes": "Verified against the public PMC figure caption.",
            }],
            "predicate_id": "RO:0002326",
        },
    ],
    "metabolism/wood_ljungdahl_pathway": [
        {
            "subject": "formyl_thf_synthetase",
            "predicate": "contributes to",
            "object": "wood_ljungdahl_pathway",
            "description": "Formyl-THF synthetase performs the ATP-consuming formate step.",
            "evidence": [{
                "reference": "DOI:10.3389/fbioe.2024.1395540",
                "snippet": (
                    "The second step is the reaction of formate with "
                    "tetrahydrofolate (THF), catalyzed by formyl-THF synthetase "
                    "(FTS) and consuming one ATP"
                ),
                "notes": "Verified against the freely available article PDF.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "methyltransferase",
            "predicate": "contributes to",
            "object": "wood_ljungdahl_pathway",
            "description": "The methyltransferase loads the WLP corrinoid protein.",
            "evidence": [{
                "reference": "DOI:10.3389/fbioe.2024.1395540",
                "snippet": (
                    "the methyl group of methyl-THF is transferred to a corrinoid "
                    "iron-sulfur-containing protein (CoFeSP) via the "
                    "methyltransferase (MT)"
                ),
                "notes": "Verified against the freely available article PDF.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "acetyl_coa_synthase",
            "predicate": "contributes to",
            "object": "wood_ljungdahl_pathway",
            "description": "CODH/ACS performs the acetyl-CoA-forming WLP step.",
            "evidence": [{
                "reference": "DOI:10.3389/fbioe.2024.1395540",
                "snippet": (
                    "In the final step of WLP, the bi-functional CODH/ACS enzyme "
                    "complex catalyzes the reaction that converts CO, "
                    "methyl-CoFeSP and CoA into acetyl-CoA"
                ),
                "notes": "Verified against the freely available article PDF.",
            }],
            "predicate_id": "RO:0002326",
        },
    ],
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
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}")
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")

    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in additions:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{slug}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(not item.get("reference") or not item.get("snippet") for item in evidence):
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
