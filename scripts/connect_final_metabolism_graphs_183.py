#!/usr/bin/env python3
"""Connect the final ten fragmented metabolism graphs for issue #183."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "scripts"), str(ROOT / "src")]
from connect_morphology_graphs_183 import _components, _edge_key  # noqa: E402
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-31T12:15:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
EXPECTED_COMPONENTS = {
    "metabolism/anaerobic_respiration": 4,
    "metabolism/carbon_fixation": 4,
    "metabolism/dissimilatory_metal_reduction": 3,
    "metabolism/dissimilatory_nitrate_reduction_to_ammonium": 3,
    "metabolism/electron_transfer": 4,
    "metabolism/fermentation": 4,
    "metabolism/iron_oxidation": 5,
    "metabolism/lignin_degradation": 4,
    "metabolism/metabolism": 4,
    "metabolism/substrate_level_phosphorylation": 3,
}


def ev(doi: str, snippet: str, notes: str) -> list[dict[str, str]]:
    return [{"reference": f"DOI:{doi}", "snippet": snippet, "notes": notes}]


def edge(
    subject: str,
    predicate: str,
    object_: str,
    description: str,
    doi: str,
    snippet: str,
    predicate_id: str,
) -> dict[str, Any]:
    return {
        "subject": subject,
        "predicate": predicate,
        "object": object_,
        "description": description,
        "evidence": ev(doi, snippet, "Verified against the free public article text."),
        "predicate_id": predicate_id,
    }


ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "metabolism/anaerobic_respiration": [
        edge(
            "nitrate_reductase",
            "example of",
            "denitrification_reductases",
            "Respiratory NarGHI is one of the reductase systems used in denitrifying respiration.",
            "10.1128/msystems.00967-23",
            "the narGHI nitrate reductase cluster; NarGHI catalyzes nitrate reduction to nitrite, the canonical first step of nitrate respiration.",
            "rdfs:subClassOf",
        ),
        edge(
            "nitrous_oxide_reductase",
            "example of",
            "denitrification_reductases",
            "NosZ is the terminal member of the denitrification-reductase set.",
            "10.1128/mmbr.61.4.533-616.1997",
            "the isolation of the novel enzymes nitric oxide reductase and nitrous oxide reductase",
            "rdfs:subClassOf",
        ),
        edge(
            "denitrification_reductases",
            "contributes to",
            "denitrification",
            "The respiratory reductase ensemble executes the sequential reductions of denitrification.",
            "10.1128/mmbr.61.4.533-616.1997",
            "unexpected relationships among denitrification enzymes and respiratory oxygen reductases",
            "RO:0002326",
        ),
    ],
    "metabolism/carbon_fixation": [
        edge(
            "cbb_cycle",
            "contributes to",
            "carbon_fixation_process",
            "The Calvin-Benson cycle is an autotrophic carbon-dioxide-fixation mechanism.",
            "10.1128/AEM.02473-10",
            "The reductive pentose phosphate cycle is the quantitatively most important mechanism of autotrophic CO2 fixation in nature.",
            "RO:0002326",
        ),
        edge(
            "rtca_cycle",
            "contributes to",
            "carbon_fixation_process",
            "The reductive TCA cycle is an autotrophic carbon-dioxide-fixation route.",
            "10.1128/AEM.02473-10",
            "the second autotrophic CO2 fixation cycle (the reductive citric acid cycle) had been discovered",
            "RO:0002326",
        ),
        edge(
            "wood_ljungdahl_pathway",
            "contributes to",
            "carbon_fixation_process",
            "The Wood-Ljungdahl pathway fixes carbon dioxide into acetyl-CoA.",
            "10.1128/AEM.02473-10",
            "The Wood-Ljungdahl pathway is a noncyclic pathway that results in the fixation of two CO2 molecules to form acetyl-CoA",
            "RO:0002326",
        ),
    ],
    "metabolism/dissimilatory_metal_reduction": [
        edge(
            "fe3_reduction",
            "contributes to",
            "metal_reduction_trait",
            "Ferric-iron reduction is a defining process within dissimilatory metal reduction.",
            "10.1007/s11783-019-1173-9",
            "FeRB transfers electrons to Fe(III), Fe(III) is reduced to Fe(II), and organic compounds are mineralized",
            "RO:0002326",
        ),
        edge(
            "insoluble_metal_substrate",
            "example of",
            "extracellular_acceptor",
            "Oxidized insoluble metals are extracellular respiratory electron acceptors.",
            "10.1128/aem.00044-24",
            "oxidized, insoluble metals are an abundant electron acceptor that microbes could potentially utilize as a respiratory substrate",
            "rdfs:subClassOf",
        ),
    ],
    "metabolism/dissimilatory_nitrate_reduction_to_ammonium": [
        edge(
            "nrfa",
            "contributes to",
            "dnra_trait",
            "NrfA executes the canonical nitrite-to-ammonium step of DNRA.",
            "10.1128/aem.00292-25",
            "The second step of the pathway is performed by cytochrome c nitrite reductase (NrfA)",
            "RO:0002326",
        ),
        edge(
            "nrf_operon",
            "contributes to",
            "dnra_trait",
            "Regulated expression of the nrf operon supplies the Nrf machinery for DNRA.",
            "10.1128/aem.00292-25",
            "The regulation of nrf operons is a complex and finely tuned process involving multiple layers of control",
            "RO:0002326",
        ),
    ],
    "metabolism/electron_transfer": [
        edge(
            "membrane_electron_transport_chain",
            "contributes to",
            "electron_transfer_trait",
            "A membrane electron-transport chain is a principal cellular electron-transfer system.",
            "10.1016/j.bbabio.2008.09.008",
            "membrane-bound electron transport chain",
            "RO:0002326",
        ),
        edge(
            "complex_i",
            "participates in",
            "membrane_electron_transport_chain",
            "Complex I is an entry enzyme of the membrane respiratory electron-transport chain.",
            "10.3390/ijms252413421",
            "Complex I oxidizes NADH using ubiquinone",
            "biolink:participates_in",
        ),
        edge(
            "cytochrome_c",
            "example of",
            "cytochrome",
            "Cytochrome c is a mobile member of the cytochrome electron-carrier class.",
            "10.1073/pnas.2307093120",
            "electrons flow to the bc1 complex and onward via cytochrome c",
            "rdfs:subClassOf",
        ),
    ],
    "metabolism/fermentation": [
        edge(
            "glycolysis_emp",
            "contributes to",
            "fermentation_trait",
            "EMP glycolysis supplies pyruvate to downstream fermentation branches.",
            "10.1093/femsre/fuae016",
            "Glycolysis (EMP) and the pentose phosphate pathway feed to pyruvate.",
            "RO:0002326",
        ),
        edge(
            "pfor",
            "oxidizes",
            "pyruvate",
            "Pyruvate:ferredoxin oxidoreductase oxidizes pyruvate while reducing ferredoxin.",
            "10.1093/femsre/fuae016",
            "Pyruvate:ferredoxin oxidoreductase produces reduced ferredoxin; central to redox balancing.",
            "METPO:2007803",
        ),
        edge(
            "fnor",
            "oxidizes",
            "reduced_ferredoxin",
            "Ferredoxin-NAD+ reductase oxidizes reduced ferredoxin while reducing NAD+.",
            "10.1093/femsre/fuae016",
            "Ferredoxin-NAD+ reductase transfers electrons from reduced ferredoxin to NAD+; strong redox-balancing edge.",
            "METPO:2007803",
        ),
    ],
    "metabolism/iron_oxidation": [
        edge(
            "cbb3_oxidase",
            "contributes to",
            "iron_oxidation_trait",
            "High-affinity terminal oxidation supports iron-oxidizer respiration in microaerobic niches.",
            "10.1128/AEM.00599-24",
            "These terminal oxidases have high affinity for oxygen and therefore are widely understood to be used under microaerobic conditions",
            "RO:0002326",
        ),
        edge(
            "low_oxygen_organic_rich",
            "example of",
            "microaerobic_conditions",
            "A low-oxygen, organic-rich setting is a specific microaerobic condition.",
            "10.1128/mSystems.00038-23",
            "bd-type oxidases have a high affinity for oxygen, and recent studies show they can be more highly expressed than cbb3-type oxidases under low-oxygen, organic-rich conditions",
            "rdfs:subClassOf",
        ),
        edge(
            "enzymatic_iron_oxidation",
            "contributes to",
            "iron_oxidation_trait",
            "Enzymatic Fe(II) oxidation realizes the biological iron-oxidation capacity.",
            "10.1128/mSystems.00038-23",
            "they bind to hemes, inhibiting the activity of cytochromes, and also directly oxidize Fe(II), thus competing with enzymatic iron oxidation",
            "RO:0002326",
        ),
        edge(
            "extracellular_electron_transfer",
            "contributes to",
            "iron_oxidation_trait",
            "Extracellular electron uptake extends iron oxidation across mineral substrates.",
            "10.1128/mSystems.00038-23",
            "multiheme cytochromes (MHCs) in Gallionellaceae FeOB, which may facilitate extracellular electron uptake and the oxidation of different iron substrates",
            "RO:0002326",
        ),
    ],
    "metabolism/lignin_degradation": [
        edge(
            "oxidative_enzymes",
            "participates in",
            "lignin_depolymerization",
            "Oxidative lignin-modifying enzymes carry out lignin depolymerization.",
            "10.1186/s13068-024-02470-z",
            "LME including laccase (EC 1.10.3.2) participated in depolymerization of large lignin polymers",
            "biolink:participates_in",
        ),
        edge(
            "manganese_peroxidase",
            "example of",
            "oxidative_enzymes",
            "Manganese peroxidase is a lignin-modifying oxidative enzyme.",
            "10.3390/polym16172388",
            "Manganese peroxidase oxidizes Mn2+ to Mn3+",
            "rdfs:subClassOf",
        ),
        edge(
            "lignin_peroxidase",
            "example of",
            "oxidative_enzymes",
            "Lignin peroxidase is a lignin-modifying oxidative enzyme.",
            "10.1186/s13068-023-02447-4",
            "ALiP-P3 breaks the Calpha-Cbeta bond of the beta-O-4 model compound",
            "rdfs:subClassOf",
        ),
    ],
    "metabolism/metabolism": [
        edge(
            "respiratory_electron_transport",
            "contributes to",
            "catabolism",
            "Respiratory electron transport is an energy-conserving component of catabolism.",
            "10.1016/j.heliyon.2023.e22459",
            "The transfer of electrons through the respiratory chain is tied to proton movement",
            "RO:0002326",
        ),
        edge(
            "carbon_use_efficiency",
            "contributes to",
            "cellular_growth",
            "Carbon-use efficiency measures allocation of assimilated carbon to new biomass.",
            "10.1038/s41467-024-52160-5",
            "represents the fraction of C uptake allocated to the production of new microbial biomass",
            "RO:0002326",
        ),
        edge(
            "substrate_uptake",
            "contributes to",
            "metabolic_energy_cost",
            "The accessibility of substrates determines the energetic cost of uptake and processing.",
            "10.1038/s41467-024-52160-5",
            "Polymeric substrates like lignin and cellulose need depolymerization before cellular uptake, whereas smaller substrates readily diffuse across membranes",
            "RO:0002326",
        ),
    ],
    "metabolism/substrate_level_phosphorylation": [
        edge(
            "kinase_reaction",
            "has input",
            "high_energy_phosphorylated_intermediate",
            "The kinase reaction accepts a phosphoryl group from a high-energy metabolic intermediate.",
            "10.1111/1751-7915.13746",
            "transferring a phosphate group to ADP",
            "RO:0002233",
        ),
        edge(
            "kinase_reaction",
            "contributes to",
            "substrate_level_phosphorylation_trait",
            "Kinase-catalyzed direct phosphoryl transfer realizes substrate-level phosphorylation.",
            "10.1111/1751-7915.13746",
            "kinase-catalysed reactions can be applied for SLP",
            "RO:0002326",
        ),
    ],
}


def transform(slug: str, doc: dict[str, Any]) -> bool:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("scope_status") != "MECHANISTIC":
        raise ValueError(f"{slug}: expected one MECHANISTIC graph")
    graph = graphs[0]
    additions = ADDITIONS[slug]
    before = _components(graph)
    expected = {_edge_key(item): item for item in additions}
    existing = {_edge_key(item): item for item in graph.get("edges") or []}
    present = set(existing) & set(expected)
    if before == 1:
        if present != set(expected):
            raise ValueError(f"{slug}: connected graph does not match exact migration state")
        if any(existing[key] != item for key, item in expected.items()):
            raise ValueError(f"{slug}: connector drifted after migration")
        return False
    if present:
        raise ValueError(f"{slug}: partial connector replay: {sorted(present)}")
    if before != EXPECTED_COMPONENTS[slug]:
        raise ValueError(
            f"{slug}: expected {EXPECTED_COMPONENTS[slug]} components, found {before}"
        )
    nodes = {node["node_id"] for node in graph.get("nodes") or []}
    for item in additions:
        if item["subject"] not in nodes or item["object"] not in nodes:
            raise ValueError(f"{slug}: connector endpoint missing")
        evidence = item.get("evidence") or []
        if any(not value.get("reference") or not value.get("snippet") for value in evidence):
            raise ValueError(f"{slug}: connector lacks evidence")
        graph.setdefault("edges", []).append(item)
    if _components(graph) != 1:
        raise ValueError(f"{slug}: repair did not reach one component")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            f"with {len(additions)} public-source connector(s). No paid research "
            "service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    for slug in sorted(ADDITIONS):
        path = ROOT / "data" / "traits" / f"{slug}.yaml"
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    raise SystemExit(apply(parser.parse_args().apply))
