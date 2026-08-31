#!/usr/bin/env python3
"""Connect five fragmented trophic physiology graphs for issue #183."""

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

TIMESTAMP = "2026-08-31T10:45:00Z"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
EXPECTED_COMPONENTS = {
    "physiology/autotrophic": 2,
    "physiology/carboxydotrophic": 2,
    "physiology/chemoheterotrophic": 2,
    "physiology/chemoorganoheterotrophic": 2,
    "physiology/oxidase_activity": 2,
}

ADDITIONS: dict[str, list[dict[str, Any]]] = {
    "physiology/autotrophic": [{
        "subject": "dissolved_inorganic_carbon",
        "predicate": "participates in",
        "object": "co2_fixation_pathway",
        "description": (
            "The environmental dissolved-inorganic-carbon pool supplies substrate "
            "to autotrophic carbon-fixation pathways."
        ),
        "evidence": [{
            "reference": "DOI:10.1128/aem.01557-23",
            "snippet": (
                "DIC transporters and carbonic anhydrase enzymes (CA) to facilitate "
                "DIC fixation"
            ),
            "notes": "Verified against the open Applied and Environmental Microbiology article.",
        }],
        "predicate_id": "biolink:participates_in",
    }],
    "physiology/carboxydotrophic": [{
        "subject": "cooa_regulator",
        "predicate": "regulates production of",
        "object": "carbon_monoxide_dehydrogenase",
        "description": (
            "CO-bound CooA transcriptionally regulates production of carbon monoxide "
            "dehydrogenase and its accessory machinery."
        ),
        "evidence": [{
            "reference": "DOI:10.1128/jb.00332-22",
            "snippet": (
                "Transcriptional activation leads to rapid expression of CODH and "
                "other accessory proteins"
            ),
            "notes": "Verified against the open Journal of Bacteriology article.",
        }],
        "predicate_id": "RO:0002211",
    }],
    "physiology/chemoheterotrophic": [{
        "subject": "mannitol",
        "predicate": "participates in",
        "object": "catabolism",
        "description": (
            "Imported mannitol is converted through mannitol-1-phosphate and "
            "fructose-6-phosphate before entering glycolytic catabolism."
        ),
        "evidence": [{
            "reference": "DOI:10.1371/journal.pbio.3002198",
            "snippet": (
                "mannitol 1P (toxic when accumulating) is oxidized by MtlD to fructose "
                "6P, where it enters glycolysis"
            ),
            "notes": "Verified against the open PLOS Biology primary article.",
        }],
        "predicate_id": "biolink:participates_in",
    }],
    "physiology/chemoorganoheterotrophic": [{
        "subject": "extracellular_cazymes",
        "predicate": "contributes to",
        "object": "catabolism",
        "description": (
            "Extracellular carbohydrate-active enzymes initiate the catabolism of "
            "complex polysaccharides by cleaving their sugar linkages."
        ),
        "evidence": [{
            "reference": "DOI:10.1371/journal.pgen.1004773",
            "snippet": (
                "Plants are primarily composed of heterogeneous polysaccharides, "
                "requiring plant-degrading microbes to encode many carbohydrate-active "
                "enzymes (CAZymes) to cleave different sugar linkages"
            ),
            "notes": "Verified against the open PLOS Genetics primary article.",
        }],
        "predicate_id": "RO:0002326",
    }],
    "physiology/oxidase_activity": [{
        "subject": "family_a_cytochrome_c_oxidase",
        "predicate": "example of",
        "object": "cytochrome_c_oxidase",
        "description": (
            "Family A heme-copper oxygen reductases are a class of cytochrome c "
            "oxidase."
        ),
        "evidence": [{
            "reference": "DOI:10.3390/microorganisms10050926",
            "snippet": "Cytochrome c oxidases of the heme–copper oxygen reductase family A",
            "notes": "Verified against the open Microorganisms review.",
        }],
        "predicate_id": "rdfs:subClassOf",
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
