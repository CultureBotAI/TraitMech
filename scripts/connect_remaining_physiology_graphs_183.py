#!/usr/bin/env python3
"""Connect four fragmented physiology graphs for issue #183."""

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

TIMESTAMP = "2026-08-31T11:15:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
EXPECTED_COMPONENTS = {
    "physiology/antibiotic_resistance": 5,
    "physiology/methanotrophic": 3,
    "physiology/methylotrophic": 4,
    "physiology/natural_competence": 4,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "physiology/antibiotic_resistance": [
        {
            "subject": "antibiotic_influx",
            "predicate": "increases",
            "object": "intracellular_antibiotic_concentration",
            "description": (
                "Porin-mediated antibiotic influx raises the intracellular drug "
                "concentration available to reach bacterial targets."
            ),
            "evidence": [{
                "reference": "DOI:10.1371/journal.pone.0005453",
                "snippet": "efficient influx through porins for β-lactams to reach their target sites",
                "notes": "Verified against the open PLOS ONE primary article.",
            }],
            "predicate_id": "RO:0002213",
        },
        {
            "subject": "beta_lactamase",
            "predicate": "confers",
            "object": "antibiotic_resistance_trait",
            "description": (
                "Beta-lactamase-mediated drug hydrolysis confers resistance to "
                "beta-lactam antibiotics."
            ),
            "evidence": [{
                "reference": "DOI:10.1016/j.jbc.2021.100799",
                "snippet": "β-lactamase, which inactivates the drug by hydrolysis",
                "notes": "Verified against the public Journal of Biological Chemistry primary article.",
            }],
            "predicate_id": "METPO:2007700",
        },
        {
            "subject": "qrdr_mutation",
            "predicate": "confers",
            "object": "antibiotic_resistance_trait",
            "description": (
                "Resistance-associated QRDR mutations alter fluoroquinolone targets "
                "and confer the antibiotic-resistance phenotype."
            ),
            "evidence": [{
                "reference": "DOI:10.1186/s13756-020-00793-8",
                "snippet": (
                    "gyrA as the main mutated gene associated with conferring "
                    "fluoroquinolone resistance"
                ),
                "notes": "Verified against the open primary evolution experiment.",
            }],
            "predicate_id": "METPO:2007700",
        },
        {
            "subject": "rrna_methylation_23s",
            "predicate": "confers",
            "object": "antibiotic_resistance_trait",
            "description": (
                "Methylation of the 23S rRNA drug-binding region confers macrolide "
                "resistance."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/mbio.02665-19",
                "snippet": (
                    "increased methylation of G748 in 23S rRNA and thereby conferring "
                    "resistance to this antibiotic"
                ),
                "notes": "Verified against the open mBio primary article.",
            }],
            "predicate_id": "METPO:2007700",
        },
    ],
    "physiology/methanotrophic": [
        {
            "subject": "particulate_methane_monooxygenase",
            "predicate": "example of",
            "object": "methane_monooxygenase",
            "description": "Particulate MMO is one of the two methane-monooxygenase enzyme types.",
            "evidence": [{
                "reference": "DOI:10.3109/10409238.2012.697865",
                "snippet": (
                    "There are two types of MMOs. The soluble form (sMMO)"
                ),
                "notes": (
                    "Verified in the public full text, which immediately identifies "
                    "the membrane-bound particulate MMO as the other type."
                ),
            }],
            "predicate_id": "rdfs:subClassOf",
        },
        {
            "subject": "methanol_dehydrogenase",
            "predicate": "produces",
            "object": "formaldehyde",
            "description": (
                "Methanol dehydrogenase converts methanol to formaldehyde, joining "
                "methane oxidation to the assimilation branch."
            ),
            "evidence": [{
                "reference": "DOI:10.3109/10409238.2012.697865",
                "snippet": "Methanol is further converted to formaldehyde by methanol dehydrogenase",
                "notes": "Verified against the public full text.",
            }],
            "predicate_id": "METPO:2007800",
        },
    ],
    "physiology/methylotrophic": [
        {
            "subject": "mxa_methanol_dehydrogenase",
            "predicate": "example of",
            "object": "pqq_dependent_mdh",
            "description": (
                "The calcium-dependent Mxa enzyme is a PQQ-dependent alcohol "
                "dehydrogenase used for methanol oxidation."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/msphere.00685-24",
                "snippet": (
                    "Xox- and Mxa-type MDHs belong to the diverse group of "
                    "pyrroloquinoline quinone (PQQ)-dependent alcohol dehydrogenases"
                ),
                "notes": "Verified against the open mSphere primary article.",
            }],
            "predicate_id": "rdfs:subClassOf",
        },
        {
            "subject": "formaldehyde",
            "predicate": "oxidized by",
            "object": "formaldehyde_dehydrogenase",
            "description": (
                "Formaldehyde dehydrogenase oxidizes formaldehyde to formate in the "
                "dissimilatory branch."
            ),
            "evidence": [{
                "reference": "DOI:10.3109/10409238.2012.697865",
                "snippet": "formaldehyde is then oxidized to formate",
                "notes": "Verified against the public full text.",
            }],
        },
        {
            "subject": "formate",
            "predicate": "oxidized by",
            "object": "formate_dehydrogenase",
            "description": (
                "Formate dehydrogenase continues C1 dissimilation by oxidizing "
                "formate to carbon dioxide."
            ),
            "evidence": [{
                "reference": "DOI:10.3109/10409238.2012.697865",
                "snippet": (
                    "formate and carbon dioxide by formaldehyde and formate "
                    "dehydrogenases, respectively"
                ),
                "notes": "Verified against the public full text.",
            }],
        },
    ],
    "physiology/natural_competence": [
        {
            "subject": "pilus_retraction",
            "predicate": "contributes to",
            "object": "competence_process",
            "description": (
                "Retraction of DNA-bound competence pili initiates uptake during the "
                "competence process."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41564-018-0174-y",
                "snippet": (
                    "retraction of DNA-bound type IV competence pili initiates the "
                    "process of DNA uptake"
                ),
                "notes": "Verified against the open Nature Microbiology primary article.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "comea",
            "predicate": "contributes to",
            "object": "dna_uptake",
            "description": (
                "ComEA-dependent molecular ratcheting contributes to DNA uptake into "
                "the periplasm."
            ),
            "evidence": [{
                "reference": "DOI:10.1038/s41564-018-0174-y",
                "snippet": "uptake facilitated by ComEA-dependent molecular ratcheting",
                "notes": "Verified against the open Nature Microbiology primary article.",
            }],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "homologous_recombination",
            "predicate": "contributes to",
            "object": "competence_process",
            "description": (
                "RecA-mediated homologous recombination integrates incoming DNA and "
                "completes natural transformation."
            ),
            "evidence": [{
                "reference": "DOI:10.1128/jb.00156-23",
                "snippet": (
                    "RecA binds to the ssDNA and directs homologous recombination of "
                    "the incoming ssDNA into the chromosome"
                ),
                "notes": "Verified against the open Journal of Bacteriology primary article.",
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
