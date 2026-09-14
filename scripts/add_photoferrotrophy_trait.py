#!/usr/bin/env python3
"""Add photoferrotrophy and ground the photolithotrophic Fe(II) branch."""
from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "photoferrotrophy.yaml"
PHOTOLITHOTROPHIC = (
    REPO_ROOT / "data" / "traits" / "physiology" / "photolithotrophic.yaml"
)
CAMACHO = "DOI:10.3389/fmicb.2017.00323"
WALTER = "DOI:10.3389/fmicb.2014.00713"
JIAO = "DOI:10.1128/JB.00776-06"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T22:07:00Z"

RECORD = {
    "identifier": "traitmech:000193",
    "label": "photoferrotrophy",
    "definition": (
        "A metabolism in which anoxygenic phototrophs use light energy to "
        "oxidize Fe(II) as an electron donor for carbon fixation and biomass "
        "formation."
    ),
    "definition_source": WALTER,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000035", "traitmech:000107"],
    "synonyms": [
        {
            "synonym_text": "phototrophic Fe(II) oxidation",
            "synonym_type": "EXACT_SYNONYM",
            "source": WALTER,
        },
        {
            "synonym_text": "anoxygenic phototrophic Fe(II) oxidation",
            "synonym_type": "EXACT_SYNONYM",
            "source": CAMACHO,
        },
    ],
    "evidence": [
        {
            "reference": WALTER,
            "snippet": (
                "photoferrotrophic bacteria use light as energy and Fe(II) as "
                "an electron source for carbon fixation and biomass formation"
            ),
            "notes": (
                "Walter et al. directly describe the defining light-powered "
                "Fe(II)-donor physiology of photoferrotrophic bacteria."
            ),
        },
        {
            "reference": CAMACHO,
            "snippet": "reduced iron [Fe(II)] as an electron donor",
            "notes": (
                "Camacho et al. review Fe(II) as the inorganic electron donor "
                "used by photoferrotrophs during anoxygenic photosynthesis."
            ),
        },
        {
            "reference": JIAO,
            "snippet": "that is necessary for phototrophic Fe(II) oxidation",
            "notes": (
                "Jiao & Newman discovered the R. palustris TIE-1 pio operon "
                "and showed that it is necessary for phototrophic Fe(II) "
                "oxidation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:395960",
            "taxon_label": "Rhodopseudomonas palustris TIE-1",
            "note": "PioABC-model purple nonsulfur photoferrotroph.",
            "reference": JIAO,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "photoferrotrophy_light_feii_oxidation",
            "title": "Photoferrotrophy couples light to Fe(II) oxidation",
            "description": (
                "Evidence-backed causal sketch linking light, Fe(II) oxidation, "
                "photosynthetic electron transport, and carbon fixation in "
                "photoferrotrophic metabolism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the shared light, Fe(II)-donor, Fe(III) "
                "product, and carbon-fixation processes. It stays process-level "
                "because lineage-specific PioABC, FoxEYZ, and Cyc2 branches do "
                "not yet have a reviewed or audit-verifiable exact UniProt "
                "protein example for this TraitRecord."
            ),
            "nodes": [
                {
                    "node_id": "photoferrotrophy_trait",
                    "label": "photoferrotrophy",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000193",
                    "description": (
                        "Anoxygenic photosynthetic Fe(II)-oxidizing metabolism."
                    ),
                },
                {
                    "node_id": "light",
                    "label": "light",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "grounding": "PATO:0001717",
                    "description": (
                        "Energy source for anoxygenic phototrophic Fe(II) "
                        "oxidation."
                    ),
                },
                {
                    "node_id": "ferrous_iron",
                    "label": "ferrous iron",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:29033",
                    "description": "Fe(II), the electron-donor substrate.",
                },
                {
                    "node_id": "ferric_iron",
                    "label": "ferric iron",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:29034",
                    "description": "Fe(III), the oxidized iron product.",
                },
                {
                    "node_id": "photosynthetic_electron_transport",
                    "label": "photosynthetic electron transport",
                    "node_type": "PATHWAY",
                    "grounding": "GO:0009767",
                    "description": (
                        "Light-driven electron-transport chain powered by "
                        "photochemical reaction centers."
                    ),
                },
                {
                    "node_id": "carbon_fixation",
                    "label": "carbon fixation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "grounding": "GO:0015977",
                    "description": (
                        "Inorganic carbon assimilation into organic compounds."
                    ),
                },
                {
                    "node_id": "carbon_dioxide",
                    "label": "carbon dioxide",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:16526",
                    "description": "Inorganic carbon source fixed by photoferrotrophs.",
                },
                {
                    "node_id": "biomass",
                    "label": "biomass",
                    "node_type": "CHEMICAL",
                    "grounding": "METPO:1007501",
                    "description": "Cell material formed from fixed carbon.",
                },
            ],
            "edges": [
                {
                    "subject": "photoferrotrophy_trait",
                    "predicate": "has energy source",
                    "object": "light",
                    "description": (
                        "Photoferrotrophy uses light as the metabolism's "
                        "energy source."
                    ),
                    "evidence": [
                        {
                            "reference": WALTER,
                            "snippet": (
                                "photoferrotrophic bacteria use light as energy"
                            ),
                            "notes": (
                                "Verified against the open Frontiers primary "
                                "article full text."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007807",
                },
                {
                    "subject": "photoferrotrophy_trait",
                    "predicate": "has electron donor",
                    "object": "ferrous_iron",
                    "description": "Fe(II) is the electron donor for photoferrotrophy.",
                    "evidence": [
                        {
                            "reference": CAMACHO,
                            "snippet": "reduced iron [Fe(II)] as an electron donor",
                            "notes": (
                                "Supports Fe(II) as the inorganic electron "
                                "donor for anoxygenic photoferrotrophy."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007701",
                },
                {
                    "subject": "light",
                    "predicate": "enables",
                    "object": "photosynthetic_electron_transport",
                    "description": (
                        "Light powers the photosynthetic electron flow in "
                        "photoferrotrophic metabolism."
                    ),
                    "evidence": [
                        {
                            "reference": WALTER,
                            "snippet": (
                                "photoferrotrophic bacteria use light as energy"
                            ),
                            "notes": (
                                "Supports light as the energetic input for "
                                "the photoferrotrophic electron-transport chain."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002327",
                },
                {
                    "subject": "ferrous_iron",
                    "predicate": "feeds electrons into",
                    "object": "photosynthetic_electron_transport",
                    "description": (
                        "Fe(II) supplies electrons to anoxygenic photosynthetic "
                        "electron transport in photoferrotrophs."
                    ),
                    "evidence": [
                        {
                            "reference": WALTER,
                            "snippet": (
                                "Fe(II) as an electron source for carbon "
                                "fixation and biomass formation"
                            ),
                            "notes": (
                                "Supports ferrous iron as the electron source "
                                "feeding photoferrotrophic carbon fixation."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007402",
                },
                {
                    "subject": "ferrous_iron",
                    "predicate": "oxidized to",
                    "object": "ferric_iron",
                    "description": "Photoferrotrophy oxidizes Fe(II) to Fe(III).",
                    "evidence": [
                        {
                            "reference": JIAO,
                            "snippet": (
                                "phototrophic Fe(II) oxidation in "
                                "Rhodopseudomonas palustris TIE-1"
                            ),
                            "notes": (
                                "Supports Fe(II) oxidation by the model "
                                "R. palustris TIE-1 photoferrotrophy system."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007405",
                },
                {
                    "subject": "photosynthetic_electron_transport",
                    "predicate": "enables",
                    "object": "carbon_fixation",
                    "description": (
                        "Light-driven electron transport supports carbon "
                        "fixation in photoferrotrophic metabolism."
                    ),
                    "evidence": [
                        {
                            "reference": WALTER,
                            "snippet": (
                                "Fe(II) as an electron source for carbon "
                                "fixation"
                            ),
                            "notes": (
                                "Supports electron flow from Fe(II) into "
                                "photoferrotrophic carbon fixation."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002327",
                },
                {
                    "subject": "carbon_dioxide",
                    "predicate": "fixed during",
                    "object": "carbon_fixation",
                    "description": (
                        "Photoferrotrophs assimilate inorganic carbon by "
                        "carbon fixation."
                    ),
                    "evidence": [
                        {
                            "reference": CAMACHO,
                            "snippet": "inorganic carbon is fixed into organic matter",
                            "notes": (
                                "Supports carbon fixation during "
                                "photoferrotrophic anoxygenic photosynthesis."
                            ),
                        },
                    ],
                },
                {
                    "subject": "carbon_fixation",
                    "predicate": "has output",
                    "object": "biomass",
                    "description": (
                        "Carbon fixed during photoferrotrophy supports biomass "
                        "formation."
                    ),
                    "evidence": [
                        {
                            "reference": WALTER,
                            "snippet": (
                                "photoferrotrophic bacteria use light as "
                                "energy and Fe(II) as an electron source for "
                                "carbon fixation and biomass formation"
                            ),
                            "notes": (
                                "Supports biomass formation coupled to "
                                "Fe(II)-fed photoferrotrophic metabolism."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002234",
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "photoferrotrophy-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for photoferrotrophy "
                "before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot has no active photoferrotrophy or "
                "anoxygenic phototrophic Fe(II) oxidation class. Candidate GO "
                "classes for photosynthesis, photosynthetic electron transport, "
                "and carbon fixation are broader than this Fe(II)-donor "
                "organismal metabolism, so no exact external class has yet been "
                "resolved."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
        },
        {
            "discussion_id": "photoferrotrophy-protein-example-gap",
            "prompt": (
                "Resolve a live, audit-clean UniProt protein example for a "
                "taxon-specific photoferrotrophy branch."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "R. palustris TIE-1 PioA and R. ferrooxidans SW2 FoxE have "
                "DOI-backed primary evidence, but their current exact UniProtKB "
                "accessions are unreviewed entries without live Proteomes "
                "cross-references. The first graph therefore stays process-level "
                "until a reviewed or audit-verifiable exact entry is available."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
        },
    ],
}


def ground_photolithotrophic_branch(record: dict) -> None:
    if record.get("identifier") != "METPO:1000658":
        raise ValueError(f"expected METPO:1000658, got {record.get('identifier')!r}")
    if record.get("label") != "photolithotrophic":
        raise ValueError(f"expected photolithotrophic, got {record.get('label')!r}")
    if record.get("mapping_status") != "REVIEWED":
        raise ValueError(f"expected REVIEWED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000631"]:
        raise ValueError(f"unexpected parents: {record.get('parent_traits')!r}")

    graphs = [
        graph
        for graph in record.get("causal_graphs") or []
        if graph.get("graph_id") == "photolithotrophic_inorganic_electron_donors"
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected one photolithotrophic graph, got {len(graphs)}")

    graph = graphs[0]
    nodes = [
        node
        for node in graph.get("nodes") or []
        if node.get("node_id") == "photoferrotrophy"
    ]
    if len(nodes) != 1:
        raise ValueError(f"expected one photoferrotrophy node, got {len(nodes)}")

    node = nodes[0]
    expected = {
        "node_id": "photoferrotrophy",
        "label": "photoferrotrophy",
        "node_type": "TRAIT",
        "description": (
            "Photolithotrophic subtype oxidizing Fe(II) via anoxygenic "
            "photosynthesis."
        ),
    }
    if node != expected:
        raise ValueError(f"unexpected photoferrotrophy node preimage: {node!r}")

    node["grounding"] = "traitmech:000193"

    record_curation_event(
        record,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the photoferrotrophy causal node to traitmech:000193 "
            "after minting the same-scope phototrophic Fe(II) oxidation "
            "TraitRecord."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def write_record(path: Path, record: dict, write: bool) -> None:
    if write:
        write_validated_trait(record, path)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            write_validated_trait(record, Path(tmp) / path.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted photoferrotrophy as a DOI-backed anoxygenic "
            "photosynthesis and iron-oxidation TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; the pinned METPO snapshot has no exact photoferrotrophy "
            "class and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v70."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    photolithotrophic = yaml.safe_load(PHOTOLITHOTROPHIC.read_text(encoding="utf-8"))
    ground_photolithotrophic_branch(photolithotrophic)

    write_record(TARGET, record, args.apply)
    write_record(PHOTOLITHOTROPHIC, photolithotrophic, args.apply)

    mode = "wrote" if args.apply else "would write"
    print(f"{mode} {TARGET.relative_to(REPO_ROOT)}")
    print(f"{mode} {PHOTOLITHOTROPHIC.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
