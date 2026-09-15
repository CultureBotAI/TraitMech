#!/usr/bin/env python3
"""Add the cold shock response physiology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "cold_shock_response.yaml"
PSYCHROTOLERANT = REPO_ROOT / "data" / "traits" / "environment" / "psychrotolerant.yaml"

WEBER = "DOI:10.3184/003685003783238707"
PHADTARE = "DOI:10.1046/j.1365-2958.1999.01541.x"
GOLDSTEIN = "DOI:10.1073/pnas.87.1.283"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T05:32:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000206",
    "label": "cold shock response",
    "definition": (
        "A stress response in which a rapid temperature downshift induces "
        "nucleic-acid-binding cold-shock proteins and RNA-remodeling "
        "functions that preserve gene expression at low temperature."
    ),
    "definition_source": WEBER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000078"],
    "synonyms": [
        {
            "synonym_text": "cold-shock response",
            "synonym_type": "EXACT_SYNONYM",
            "source": WEBER,
        }
    ],
    "evidence": [
        {
            "reference": WEBER,
            "snippet": (
                "bacteria express a well-defined set of proteins after a "
                "rapid decrease in temperature, which is termed cold shock"
            ),
            "notes": (
                "Weber and Marahiel define bacterial cold shock as the "
                "temperature-downshift response that induces a specific "
                "protein set."
            ),
        },
        {
            "reference": WEBER,
            "snippet": (
                "the cold shock response is organized as a complex stimulon "
                "in which post-transcriptional events play an important role"
            ),
            "notes": (
                "The bacterial cold-shock response is reviewed as a stimulon "
                "dominated by post-transcriptional control rather than a "
                "single cold-specific sigma-factor branch."
            ),
        },
        {
            "reference": WEBER,
            "snippet": (
                "nucleic acid-binding cold shock proteins which play a "
                "fundamental role not only during cold shock adaptation but "
                "also under optimal growth conditions"
            ),
            "notes": (
                "The review places nucleic-acid-binding cold-shock proteins "
                "among the core functional components of bacterial "
                "cold-shock adaptation."
            ),
        },
        {
            "reference": PHADTARE,
            "snippet": (
                "proposed function as an RNA chaperone to prevent the "
                "formation of secondary structures in RNA molecules, thus "
                "facilitating translation at low temperature"
            ),
            "notes": (
                "Phadtare and Inouye support RNA chaperoning by CspA-family "
                "proteins as a mechanism for preserving translation after "
                "cold shock."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "E. coli is a model for the bacterial cold-shock response, "
                "including induction of the major cold-shock protein CspA."
            ),
            "reference": GOLDSTEIN,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "cold_shock_response_rna_adaptation",
            "title": "Cold-shock RNA adaptation",
            "description": (
                "Evidence-backed causal sketch linking abrupt temperature "
                "downshift to bacterial cold-shock protein induction and "
                "RNA chaperone support for low-temperature translation."
            ),
            "scope_status": "MECHANISTIC",
            "scope_notes": (
                "This graph captures the conserved CspA-family RNA-support "
                "branch of the bacterial cold-shock response without making "
                "one cold-sensing regulator, one RNA helicase, or one "
                "post-transcriptional circuit universal across bacteria."
            ),
            "nodes": [
                {
                    "node_id": "cold_shock_response_trait",
                    "label": "cold shock response",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000206",
                    "description": (
                        "Capacity to induce cold-shock proteins after a "
                        "rapid temperature downshift."
                    ),
                },
                {
                    "node_id": "acute_cold_shock",
                    "label": "acute cold shock",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": "A sudden downward temperature shift.",
                },
                {
                    "node_id": "cold_shock_response_process",
                    "label": "cold-shock response",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Rapid expression of cold-shock proteins and RNA-"
                        "remodeling functions after a temperature downshift."
                    ),
                },
                {
                    "node_id": "cspa_family_cold_shock_proteins",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "Reviewed functional protein family; cold-shock "
                        "domain signatures and CspA-like orthology terms "
                        "are broader than bacterial proteins induced and "
                        "used as RNA chaperones during cold shock."
                    ),
                    "label": "CspA-family cold-shock proteins",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "Nucleic-acid-binding cold-shock proteins that act "
                        "as RNA chaperones after cold shock."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0A9X9",
                            "protein_label": "Cold shock protein CspA",
                            "gene_symbol": "cspA",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 146,
                            "sequence_version": 2,
                            "role": (
                                "E. coli K-12 CspA is the major CspA-family "
                                "cold-shock protein and model RNA chaperone "
                                "induced by temperature downshift."
                            ),
                            "evidence": [
                                {
                                    "reference": GOLDSTEIN,
                                    "snippet": (
                                        "the production of a 7.4-kDa "
                                        "cytoplasmic protein (CS7.4) was "
                                        "prominently induced"
                                    ),
                                    "notes": (
                                        "Goldstein et al. directly support "
                                        "strong induction of the E. coli "
                                        "major cold-shock protein later "
                                        "named CspA."
                                    ),
                                },
                                {
                                    "reference": PHADTARE,
                                    "snippet": (
                                        "CspA, the major cold shock protein, "
                                        "binds RNA with low sequence "
                                        "specificity"
                                    ),
                                    "notes": (
                                        "Phadtare and Inouye directly support "
                                        "CspA as an RNA-binding cold-shock "
                                        "protein."
                                    ),
                                },
                            ],
                        }
                    ],
                },
                {
                    "node_id": "rna_secondary_structure_control",
                    "label": "RNA secondary-structure control at low temperature",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "RNA chaperoning that limits inhibitory secondary "
                        "structure formation in cold-stressed cells."
                    ),
                },
                {
                    "node_id": "low_temperature_translation",
                    "label": "translation at low temperature",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protein synthesis preserved during low-temperature "
                        "stress."
                    ),
                    "grounding": "GO:0006412",
                },
            ],
            "edges": [
                {
                    "subject": "acute_cold_shock",
                    "predicate": "causes",
                    "predicate_id": "biolink:causes",
                    "object": "cold_shock_response_process",
                    "description": (
                        "Abrupt temperature downshift causes the bacterial "
                        "cold-shock protein-expression response."
                    ),
                    "evidence": [
                        {
                            "reference": WEBER,
                            "snippet": (
                                "bacteria express a well-defined set of "
                                "proteins after a rapid decrease in "
                                "temperature, which is termed cold shock"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; the cold-shock response follows "
                                "rapid temperature decrease."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cold_shock_response_process",
                    "predicate": "positively regulates",
                    "predicate_id": "RO:0002213",
                    "object": "cspa_family_cold_shock_proteins",
                    "description": (
                        "The cold-shock response induces CspA-family "
                        "nucleic-acid-binding cold-shock proteins."
                    ),
                    "evidence": [
                        {
                            "reference": WEBER,
                            "snippet": (
                                "nucleic acid-binding cold shock proteins "
                                "which play a fundamental role not only "
                                "during cold shock adaptation"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; nucleic-acid-binding cold-shock "
                                "proteins are central cold-shock-adaptation "
                                "components."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cspa_family_cold_shock_proteins",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rna_secondary_structure_control",
                    "description": (
                        "CspA-family cold-shock proteins contribute to "
                        "low-temperature RNA secondary-structure control."
                    ),
                    "evidence": [
                        {
                            "reference": PHADTARE,
                            "snippet": (
                                "RNA chaperone to prevent the formation of "
                                "secondary structures in RNA molecules"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; CspA-family RNA chaperone "
                                "activity limits RNA secondary-structure "
                                "formation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "rna_secondary_structure_control",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "low_temperature_translation",
                    "description": (
                        "Control of RNA secondary structures supports "
                        "translation at low temperature."
                    ),
                    "evidence": [
                        {
                            "reference": PHADTARE,
                            "snippet": (
                                "prevent the formation of secondary "
                                "structures in RNA molecules, thus "
                                "facilitating translation at low temperature"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; CspA-family RNA chaperoning "
                                "facilitates low-temperature translation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "low_temperature_translation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "cold_shock_response_trait",
                    "description": (
                        "Preservation of translation realizes the RNA-"
                        "adaptation branch of the cold-shock-response trait."
                    ),
                    "evidence": [
                        {
                            "reference": PHADTARE,
                            "snippet": (
                                "proposed function as an RNA chaperone to "
                                "prevent the formation of secondary "
                                "structures in RNA molecules, thus "
                                "facilitating translation at low temperature"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; RNA chaperoning connects "
                                "CspA-family proteins to preserved "
                                "translation during cold stress."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "cold-shock-response-xref-gap",
            "prompt": (
                "Resolve exact ontology xrefs for organism-level microbial "
                "cold shock response before adding TraitRecord xrefs."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0009409 response to cold can ground broad biological-"
                "process response nodes but is broader than the rapid "
                "temperature-downshift cold-shock response curated here. "
                "Cold-shock-domain signatures and CspA-family terms describe "
                "narrower molecular machinery rather than the whole "
                "organism-level stress-response trait."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        }
    ],
}


def _load_psychrotolerant() -> dict[str, Any]:
    doc = yaml.safe_load(PSYCHROTOLERANT.read_text())
    if not isinstance(doc, dict):
        raise SystemExit("psychrotolerant.yaml did not parse to a mapping")
    if doc.get("identifier") != "METPO:1000618":
        raise SystemExit("unexpected psychrotolerant identifier")
    if doc.get("label") != "psychrotolerant":
        raise SystemExit("unexpected psychrotolerant label")
    if doc.get("mapping_status") != "REVIEWED":
        raise SystemExit("unexpected psychrotolerant mapping_status")
    return doc


def _ground_psychrotolerant_cold_shock_response(doc: dict[str, Any]) -> None:
    graphs = doc.get("causal_graphs") or []
    graph = next(
        (
            candidate
            for candidate in graphs
            if candidate.get("graph_id") == "psychrotolerant_facultative_cold_adaptation"
        ),
        None,
    )
    if graph is None:
        raise SystemExit("psychrotolerant graph not found")

    node = next(
        (
            candidate
            for candidate in graph.get("nodes", [])
            if candidate.get("node_id") == "cold_shock_response"
        ),
        None,
    )
    if node is None:
        raise SystemExit("cold_shock_response node not found")

    expected = {
        "node_id": "cold_shock_response",
        "label": "cold-shock response",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": (
            "Cold-shock-protein induction supporting transient low-temperature "
            "acclimation."
        ),
    }
    if node != expected:
        raise SystemExit("unexpected psychrotolerant cold_shock_response preimage")

    node["grounding"] = "traitmech:000206"
    record_curation_event(
        doc,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the exact cold-shock-response biological-process node "
            "to the newly minted local traitmech:000206 cold shock response "
            "record."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write YAML files")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted cold shock response as a DOI-backed stress-response "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has only an "
            "obsolete cold shock response class and the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v83."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    psychrotolerant = _load_psychrotolerant()
    _ground_psychrotolerant_cold_shock_response(psychrotolerant)

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(psychrotolerant, PSYCHROTOLERANT)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        print(f"updated {PSYCHROTOLERANT.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would update {PSYCHROTOLERANT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
