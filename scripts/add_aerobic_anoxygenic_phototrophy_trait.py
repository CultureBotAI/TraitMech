#!/usr/bin/env python3
"""Add aerobic anoxygenic phototrophy and ground its AAP mention."""
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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "physiology"
    / "aerobic_anoxygenic_phototrophy.yaml"
)
PHOTOHETEROTROPHIC = (
    REPO_ROOT / "data" / "traits" / "physiology" / "photoheterotrophic.yaml"
)
PHOTOTROPHIC = REPO_ROOT / "data" / "traits" / "physiology" / "phototrophic.yaml"
HAURUSEU = "DOI:10.1128/AEM.01747-12"
VILLENA = "DOI:10.1186/s40168-024-01786-0"
STOJAN = "DOI:10.1186/s40793-024-00573-6"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T23:14:00Z"

RECORD = {
    "identifier": "traitmech:000194",
    "label": "aerobic anoxygenic phototrophy",
    "definition": (
        "A photoheterotrophy in which aerobic heterotrophic bacteria use "
        "bacteriochlorophyll-containing reaction centers to harvest light as "
        "auxiliary energy while requiring organic carbon substrates for growth."
    ),
    "definition_source": HAURUSEU,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000657", "traitmech:000035", "METPO:1000602"],
    "synonyms": [
        {
            "synonym_text": "aerobic anoxygenic phototroph",
            "synonym_type": "EXACT_SYNONYM",
            "source": HAURUSEU,
        },
        {
            "synonym_text": "aerobic anoxygenic phototrophic bacteria",
            "synonym_type": "EXACT_SYNONYM",
            "source": VILLENA,
        },
        {
            "synonym_text": "AAP bacteria",
            "synonym_type": "RELATED_SYNONYM",
            "source": VILLENA,
        },
        {
            "synonym_text": "aerobic_anoxygenic_phototrophy",
            "synonym_type": "RELATED_SYNONYM",
            "source": "metpo.owl",
        },
    ],
    "evidence": [
        {
            "reference": HAURUSEU,
            "snippet": (
                "Aerobic anoxygenic phototrophs contain photosynthetic "
                "reaction centers composed of bacteriochlorophyll"
            ),
            "notes": (
                "Hauruseu and Koblizek define AAPs by "
                "bacteriochlorophyll-containing photosynthetic reaction "
                "centers."
            ),
        },
        {
            "reference": HAURUSEU,
            "snippet": (
                "These organisms are photoheterotrophs, as they require "
                "organic carbon substrates for their growth whereas "
                "light-derived energy has only an auxiliary function"
            ),
            "notes": (
                "The Erythrobacter sp. NAP1 chemostat study supports organic "
                "carbon as required for AAP growth and light as an auxiliary "
                "energy input."
            ),
        },
        {
            "reference": VILLENA,
            "snippet": (
                "Aerobic anoxygenic phototrophic (AAP) bacteria are "
                "heterotrophic bacteria that supply their metabolism with "
                "light energy harvested by bacteriochlorophyll-a-containing "
                "reaction centers"
            ),
            "notes": (
                "Villena-Alemany et al. corroborate the AAP scope as "
                "heterotrophic bacteria with light-harvesting "
                "bacteriochlorophyll-a reaction centers."
            ),
        },
        {
            "reference": STOJAN,
            "snippet": (
                "Aerobic anoxygenic phototrophs (AAPs) are a polyphyletic "
                "group of bacteria capable of photoheterotrophy"
            ),
            "notes": (
                "Stojan et al. place AAPs as a polyphyletic bacterial "
                "photoheterotrophic functional group rather than a taxonomic "
                "lineage."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:237727",
            "taxon_label": "Erythrobacter sp. NAP1",
            "note": (
                "Carbon-limited aerobic anoxygenic phototroph showing "
                "light-enhanced organic-carbon assimilation."
            ),
            "reference": HAURUSEU,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "aerobic_anoxygenic_phototrophy_light_organic_carbon",
            "title": (
                "Aerobic anoxygenic phototrophy couples light to organic "
                "carbon assimilation"
            ),
            "description": (
                "Evidence-backed causal sketch linking "
                "bacteriochlorophyll-based light harvesting, "
                "photophosphorylation, and light-enhanced organic-carbon "
                "assimilation in aerobic anoxygenic phototrophs."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "This first graph captures process-level light harvesting, "
                "photophosphorylation, and organic-carbon assimilation "
                "without claiming an exact AAP reaction-center protein "
                "family. pufLM examples need an audit-verifiable "
                "accession/proteome pair before promotion to a mechanistic "
                "protein-level graph."
            ),
            "nodes": [
                {
                    "node_id": "aerobic_anoxygenic_phototrophy_trait",
                    "label": "aerobic anoxygenic phototrophy",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000194",
                    "description": (
                        "Aerobic photoheterotrophy using "
                        "bacteriochlorophyll-containing reaction centers."
                    ),
                },
                {
                    "node_id": "light",
                    "label": "light",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "grounding": "PATO:0001717",
                    "description": "Auxiliary energy source harvested by AAPs.",
                },
                {
                    "node_id": "bacteriochlorophyll",
                    "label": "bacteriochlorophyll",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:38201",
                    "description": (
                        "Light-harvesting pigment in AAP reaction centers."
                    ),
                },
                {
                    "node_id": "photophosphorylation",
                    "label": "photophosphorylation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Light-driven ATP synthesis in AAPs.",
                },
                {
                    "node_id": "atp",
                    "label": "ATP",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:30616",
                    "description": (
                        "Energy carrier produced by photophosphorylation."
                    ),
                },
                {
                    "node_id": "organic_carbon",
                    "label": "organic carbon",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:50860",
                    "description": (
                        "Required organic substrate used as carbon source."
                    ),
                },
                {
                    "node_id": "biomass",
                    "label": "biomass",
                    "node_type": "CHEMICAL",
                    "grounding": "METPO:1007501",
                    "description": (
                        "Cell material accumulated from supplied organic "
                        "carbon."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "aerobic_anoxygenic_phototrophy_trait",
                    "predicate": "has energy source",
                    "object": "light",
                    "description": (
                        "AAPs supplement their heterotrophic metabolism with "
                        "light energy."
                    ),
                    "evidence": [
                        {
                            "reference": VILLENA,
                            "snippet": "supply their metabolism with light energy",
                            "notes": (
                                "Verified against the Springer full text."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007807",
                },
                {
                    "subject": "aerobic_anoxygenic_phototrophy_trait",
                    "predicate": "has carbon source",
                    "object": "organic_carbon",
                    "description": (
                        "AAP growth relies on external organic carbon."
                    ),
                    "evidence": [
                        {
                            "reference": VILLENA,
                            "snippet": (
                                "rely upon external sources of organic carbon"
                            ),
                            "notes": (
                                "Verified against the Springer full text."
                            ),
                        },
                    ],
                    "predicate_id": "METPO:2007806",
                },
                {
                    "subject": "bacteriochlorophyll",
                    "predicate": "captures",
                    "object": "light",
                    "description": (
                        "Bacteriochlorophyll-containing AAP reaction centers "
                        "harvest light."
                    ),
                    "evidence": [
                        {
                            "reference": VILLENA,
                            "snippet": (
                                "energy obtained from light through "
                                "bacteriochlorophyll-a (BChl-a) type II "
                                "reaction centers"
                            ),
                            "notes": (
                                "Verified against the Springer full text."
                            ),
                        },
                    ],
                },
                {
                    "subject": "light",
                    "predicate": "enables",
                    "object": "photophosphorylation",
                    "description": (
                        "Light drives the AAP photophosphorylation branch."
                    ),
                    "evidence": [
                        {
                            "reference": STOJAN,
                            "snippet": (
                                "harvest light energy and generate ATP by "
                                "photophosphorylation"
                            ),
                            "notes": (
                                "Verified against the Springer full text."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002327",
                },
                {
                    "subject": "photophosphorylation",
                    "predicate": "has output",
                    "object": "atp",
                    "description": (
                        "AAP photophosphorylation conserves light energy as "
                        "ATP."
                    ),
                    "evidence": [
                        {
                            "reference": HAURUSEU,
                            "snippet": (
                                "respiration decreased to approximately 25% "
                                "of its dark value and was replaced by "
                                "photophosphorylation"
                            ),
                            "notes": (
                                "Supports replacement of respiration by "
                                "photophosphorylation as light intensity "
                                "increased in carbon-limited Erythrobacter "
                                "sp. NAP1 cultures."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002234",
                },
                {
                    "subject": "organic_carbon",
                    "predicate": "assimilated into",
                    "object": "biomass",
                    "description": (
                        "Light lets AAPs accumulate supplied organic carbon "
                        "as biomass."
                    ),
                    "evidence": [
                        {
                            "reference": HAURUSEU,
                            "snippet": (
                                "accumulate the supplied organic carbon "
                                "which would otherwise be respired"
                            ),
                            "notes": (
                                "Supports light-enhanced organic-carbon "
                                "assimilation into biomass by AAPs."
                            ),
                        },
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "aerobic-anoxygenic-phototrophy-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for aerobic "
                "anoxygenic phototrophy before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot carries "
                "aerobic_anoxygenic_phototrophy only as a related synonym on "
                "broad phototrophic, and GO photosynthetic electron transport "
                "classes denote the intracellular pathway rather than this "
                "organism-level aerobic photoheterotrophic trait."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
        },
    ],
}


def ground_photoheterotrophic_aap_node(record: dict) -> None:
    if record.get("identifier") != "METPO:1000657":
        raise ValueError(f"expected METPO:1000657, got {record.get('identifier')!r}")
    if record.get("label") != "photoheterotrophic":
        raise ValueError(f"expected photoheterotrophic, got {record.get('label')!r}")
    if record.get("mapping_status") != "REVIEWED":
        raise ValueError(f"expected REVIEWED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000631"]:
        raise ValueError(f"unexpected parents: {record.get('parent_traits')!r}")

    graphs = [
        graph
        for graph in record.get("causal_graphs") or []
        if graph.get("graph_id") == "photoheterotrophic_light_organic_carbon"
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected one photoheterotrophic graph, got {len(graphs)}")

    graph = graphs[0]
    nodes = [
        node
        for node in graph.get("nodes") or []
        if node.get("node_id") == "aerobic_anoxygenic_phototrophs"
    ]
    if len(nodes) != 1:
        raise ValueError(f"expected one AAP node, got {len(nodes)}")

    node = nodes[0]
    expected = {
        "node_id": "aerobic_anoxygenic_phototrophs",
        "label": "aerobic anoxygenic phototrophs",
        "node_type": "TRAIT",
        "description": (
            "Facultative photoheterotrophs harvesting light to generate ATP "
            "while relying on organic matter."
        ),
    }
    if node != expected:
        raise ValueError(f"unexpected AAP node preimage: {node!r}")

    node["grounding"] = "traitmech:000194"

    record_curation_event(
        record,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the aerobic anoxygenic phototrophs causal node to "
            "traitmech:000194 after minting the same-scope aerobic "
            "anoxygenic phototrophy TraitRecord."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def narrow_phototrophic_synonym(record: dict) -> None:
    if record.get("identifier") != "METPO:1000660":
        raise ValueError(f"expected METPO:1000660, got {record.get('identifier')!r}")
    if record.get("label") != "phototrophic":
        raise ValueError(f"expected phototrophic, got {record.get('label')!r}")
    if record.get("mapping_status") != "REVIEWED":
        raise ValueError(f"expected REVIEWED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000631"]:
        raise ValueError(f"unexpected parents: {record.get('parent_traits')!r}")

    stale_synonym = {
        "synonym_text": "aerobic_anoxygenic_phototrophy",
        "synonym_type": "RELATED_SYNONYM",
        "source": "metpo.owl",
    }
    synonyms = record.get("synonyms") or []
    matches = [synonym for synonym in synonyms if synonym == stale_synonym]
    if len(matches) != 1:
        raise ValueError(f"expected one moved synonym, got {len(matches)}")

    record["synonyms"] = [synonym for synonym in synonyms if synonym != stale_synonym]

    record_curation_event(
        record,
        curator=CURATOR,
        action="NARROWED_RELATED_SYNONYM",
        changes=(
            "Moved the aerobic_anoxygenic_phototrophy metpo.owl source key "
            "from broad phototrophic to the newly minted same-scope aerobic "
            "anoxygenic phototrophy TraitRecord."
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
            "Minted aerobic anoxygenic phototrophy as a DOI-backed "
            "photoheterotrophy, anoxygenic photosynthesis, and aerobic trait "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; the pinned METPO snapshot only stores "
            "aerobic_anoxygenic_phototrophy as a related synonym on broad "
            "phototrophic."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    photoheterotrophic = yaml.safe_load(PHOTOHETEROTROPHIC.read_text(encoding="utf-8"))
    ground_photoheterotrophic_aap_node(photoheterotrophic)

    phototrophic = yaml.safe_load(PHOTOTROPHIC.read_text(encoding="utf-8"))
    narrow_phototrophic_synonym(phototrophic)

    write_record(TARGET, record, args.apply)
    write_record(PHOTOHETEROTROPHIC, photoheterotrophic, args.apply)
    write_record(PHOTOTROPHIC, phototrophic, args.apply)

    mode = "wrote" if args.apply else "would write"
    print(f"{mode} {TARGET.relative_to(REPO_ROOT)}")
    print(f"{mode} {PHOTOHETEROTROPHIC.relative_to(REPO_ROOT)}")
    print(f"{mode} {PHOTOTROPHIC.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
