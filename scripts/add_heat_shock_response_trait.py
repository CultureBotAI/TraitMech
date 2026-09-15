#!/usr/bin/env python3
"""Add the heat shock response physiology trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "heat_shock_response.yaml"
THERMOTOLERANT = REPO_ROOT / "data" / "traits" / "environment" / "thermotolerant.yaml"
SCHUMANN = "DOI:10.1007/s12192-016-0727-z"
GUISBERT = "DOI:10.1128/MMBR.00007-08"
LIBEREK = "DOI:10.1073/pnas.89.8.3516"
TOMOYASU = "DOI:10.1002/j.1460-2075.1995.tb07253.x"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T04:58:15Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000205",
    "label": "heat shock response",
    "definition": (
        "A stress response in which acute heat stress induces heat-shock "
        "proteins that refold or degrade denatured proteins to restore "
        "protein homeostasis."
    ),
    "definition_source": SCHUMANN,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000078"],
    "synonyms": [
        {
            "synonym_text": "heat-shock response",
            "synonym_type": "EXACT_SYNONYM",
            "source": SCHUMANN,
        },
        {
            "synonym_text": "HSR",
            "synonym_type": "RELATED_SYNONYM",
            "source": GUISBERT,
        },
    ],
    "evidence": [
        {
            "reference": SCHUMANN,
            "snippet": (
                "they transiently induce a group of genes called heat shock "
                "genes (HSGs) which code for heat shock proteins (HSPs)"
            ),
            "notes": (
                "Schumann reviews heat-shock gene induction and heat-shock "
                "protein production as the bacterial response to sudden "
                "temperature rise."
            ),
        },
        {
            "reference": SCHUMANN,
            "snippet": (
                "chaperones binding to denatured proteins and allowing "
                "refolding to their native state and ATP-dependent proteases "
                "degrading denatured proteins"
            ),
            "notes": (
                "Schumann summarizes the two major functional heat-shock "
                "protein classes that clear denatured proteins."
            ),
        },
        {
            "reference": GUISBERT,
            "snippet": (
                "The heat shock response (HSR) is classically defined as the "
                "cellular response to temperature increase"
            ),
            "notes": (
                "Guisbert et al. define the E. coli heat-shock response and "
                "review the sigma-32 regulatory model."
            ),
        },
        {
            "reference": GUISBERT,
            "snippet": (
                "The rapid upregulation of chaperones and proteases during "
                "the HSR restores an appropriate protein-folding environment "
                "in the cell"
            ),
            "notes": (
                "Guisbert et al. support protein-folding homeostasis as the "
                "primary function of the E. coli sigma-32-mediated heat-shock "
                "response."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "E. coli is a model for the sigma-32-mediated heat-shock "
                "response, including heat-shock chaperone and protease "
                "upregulation."
            ),
            "reference": GUISBERT,
        },
        {
            "taxon_id": "NCBITaxon:1423",
            "taxon_label": "Bacillus subtilis",
            "note": (
                "B. subtilis is a Gram-positive model for heat-shock "
                "stimulon regulation by repressor and alternative-sigma "
                "branches."
            ),
            "reference": SCHUMANN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "heat_shock_response_proteostasis",
            "title": "Heat-shock proteostasis restoration",
            "description": (
                "Evidence-backed causal sketch linking acute heat shock to "
                "protein unfolding, heat-shock protein induction, and "
                "restored protein homeostasis."
            ),
            "scope_status": "MECHANISTIC",
            "scope_notes": (
                "This graph captures the conserved proteostasis output of "
                "the heat-shock response without making the E. coli "
                "sigma-32 branch, B. subtilis HrcA/CtsR branches, or other "
                "lineage-specific heat-shock regulators universal."
            ),
            "nodes": [
                {
                    "node_id": "heat_shock_response_trait",
                    "label": "heat shock response",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000205",
                    "description": (
                        "Capacity to induce heat-shock proteins after acute "
                        "heat stress."
                    ),
                },
                {
                    "node_id": "acute_heat_shock",
                    "label": "acute heat shock",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": "A sudden upward temperature shift.",
                },
                {
                    "node_id": "protein_unfolding",
                    "label": "heat-induced protein unfolding",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protein unfolding and aggregation triggered by heat "
                        "shock."
                    ),
                },
                {
                    "node_id": "heat_shock_response_process",
                    "label": "heat-shock response",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Rapid, transient production of heat-shock proteins "
                        "after protein unfolding or aggregation."
                    ),
                },
                {
                    "node_id": "heat_shock_chaperones",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "Reviewed functional protein set; no single family, "
                        "complex, or molecular-function term captures all "
                        "heat-shock-induced chaperones across bacteria."
                    ),
                    "label": "heat-shock chaperones",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "Induced chaperone systems that bind denatured "
                        "proteins and promote refolding."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0A6Y8",
                            "protein_label": "Chaperone protein DnaK",
                            "gene_symbol": "dnaK",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 183,
                            "sequence_version": 2,
                            "role": (
                                "E. coli K-12 DnaK is an Hsp70 heat-shock "
                                "chaperone that binds sigma-32 in the "
                                "chaperone-mediated heat-shock control branch."
                            ),
                            "evidence": [
                                {
                                    "reference": LIBEREK,
                                    "snippet": (
                                        "purified sigma 32 bound to DnaK and "
                                        "that this complex was disrupted in "
                                        "the presence of ATP"
                                    ),
                                    "notes": (
                                        "Liberek et al. directly support DnaK "
                                        "as an E. coli heat-shock chaperone "
                                        "that binds the sigma-32 "
                                        "transcription factor."
                                    ),
                                },
                            ],
                        },
                    ],
                },
                {
                    "node_id": "atp_dependent_proteases",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "Reviewed functional protein set; bacterial "
                        "ATP-dependent proteases belong to multiple "
                        "non-equivalent families and complexes."
                    ),
                    "label": "ATP-dependent proteases",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "Proteases that clear denatured proteins or degrade "
                        "heat-shock regulators during the heat-shock response."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0AAI3",
                            "protein_label": (
                                "ATP-dependent zinc metalloprotease FtsH"
                            ),
                            "gene_symbol": "ftsH",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 155,
                            "sequence_version": 1,
                            "role": (
                                "E. coli K-12 FtsH is an ATP-dependent "
                                "membrane metalloprotease that degrades the "
                                "sigma-32 heat-shock transcription factor."
                            ),
                            "evidence": [
                                {
                                    "reference": TOMOYASU,
                                    "snippet": (
                                        "FtsH catalyzed ATP-dependent "
                                        "degradation of biologically active "
                                        "histidine-tagged sigma 32"
                                    ),
                                    "notes": (
                                        "Tomoyasu et al. directly support FtsH "
                                        "as the E. coli ATP-dependent "
                                        "protease that degrades sigma-32."
                                    ),
                                },
                            ],
                        },
                    ],
                },
                {
                    "node_id": "protein_homeostasis",
                    "label": "protein homeostasis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cellular protein-folding state restored by chaperone "
                        "refolding and protease degradation of denatured "
                        "proteins."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "acute_heat_shock",
                    "predicate": "causes",
                    "predicate_id": "biolink:causes",
                    "object": "protein_unfolding",
                    "description": (
                        "Acute heat shock causes protein unfolding and "
                        "aggregate formation."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "A sudden heat shock results in protein "
                                "unfolding leading to the formation of "
                                "protein aggregates"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "heat shock immediately destabilizes cellular "
                                "proteins."
                            ),
                        },
                    ],
                },
                {
                    "subject": "protein_unfolding",
                    "predicate": "causes",
                    "predicate_id": "biolink:causes",
                    "object": "heat_shock_response_process",
                    "description": (
                        "Protein unfolding and aggregation trigger rapid, "
                        "transient heat-shock protein production."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "It responds to protein unfolding, aggregation "
                                "and damage by the rapid and transient "
                                "production of HSPs"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; the "
                                "edge links damaged unfolded proteins to the "
                                "protective heat-shock response."
                            ),
                        },
                    ],
                },
                {
                    "subject": "heat_shock_response_process",
                    "predicate": "positively regulates",
                    "predicate_id": "RO:0002213",
                    "object": "heat_shock_chaperones",
                    "description": (
                        "The heat-shock response induces chaperones that "
                        "refold denatured proteins."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "chaperones binding to denatured proteins and "
                                "allowing refolding to their native state"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "chaperones are a major heat-shock protein "
                                "class."
                            ),
                        },
                    ],
                },
                {
                    "subject": "heat_shock_response_process",
                    "predicate": "positively regulates",
                    "predicate_id": "RO:0002213",
                    "object": "atp_dependent_proteases",
                    "description": (
                        "The heat-shock response induces ATP-dependent "
                        "proteases that remove denatured proteins."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "ATP-dependent proteases degrading denatured "
                                "proteins"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "ATP-dependent proteases are a major "
                                "heat-shock protein class."
                            ),
                        },
                    ],
                },
                {
                    "subject": "heat_shock_chaperones",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "protein_homeostasis",
                    "description": (
                        "Heat-shock chaperones help restore proteostasis by "
                        "refolding denatured proteins."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "chaperones binding to denatured proteins and "
                                "allowing refolding to their native state"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "induced chaperones support refolding of "
                                "denatured proteins."
                            ),
                        },
                    ],
                },
                {
                    "subject": "atp_dependent_proteases",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "protein_homeostasis",
                    "description": (
                        "ATP-dependent proteases help restore proteostasis by "
                        "degrading denatured proteins."
                    ),
                    "evidence": [
                        {
                            "reference": SCHUMANN,
                            "snippet": (
                                "ATP-dependent proteases degrading denatured "
                                "proteins"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "induced proteases clear denatured proteins."
                            ),
                        },
                    ],
                },
                {
                    "subject": "protein_homeostasis",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "heat_shock_response_trait",
                    "description": (
                        "Restoration of protein-folding homeostasis realizes "
                        "the heat-shock-response trait."
                    ),
                    "evidence": [
                        {
                            "reference": GUISBERT,
                            "snippet": (
                                "restores an appropriate protein-folding "
                                "environment in the cell"
                            ),
                            "notes": (
                                "Verified against the open PMC full text; "
                                "Guisbert et al. describe proteostasis "
                                "restoration as the sigma-32-mediated "
                                "heat-shock response output."
                            ),
                        },
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "heat-shock-response-xref-gap",
            "prompt": (
                "Resolve exact ontology xrefs for organism-level microbial "
                "heat shock response before adding TraitRecord xrefs."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0009408 response to heat can ground biological-process "
                "nodes but is broader than this organism-level stress "
                "response trait. Candidate heat-shock-protein, chaperone, "
                "and ATP-dependent-protease terms describe narrower "
                "molecular machinery rather than the whole response "
                "phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
    ],
}


def _load_thermotolerant() -> dict[str, Any]:
    doc = yaml.safe_load(THERMOTOLERANT.read_text())
    if not isinstance(doc, dict):
        raise SystemExit("thermotolerant.yaml did not parse to a mapping")
    if doc.get("identifier") != "METPO:1000619":
        raise SystemExit("unexpected thermotolerant identifier")
    if doc.get("label") != "thermotolerant":
        raise SystemExit("unexpected thermotolerant label")
    if doc.get("mapping_status") != "REVIEWED":
        raise SystemExit("unexpected thermotolerant mapping_status")
    return doc


def _ground_thermotolerant_heat_shock_response(doc: dict[str, Any]) -> None:
    graphs = doc.get("causal_graphs") or []
    graph = next(
        (
            candidate
            for candidate in graphs
            if candidate.get("graph_id") == "thermotolerant_facultative_heat_adaptation"
        ),
        None,
    )
    if graph is None:
        raise SystemExit("thermotolerant graph not found")

    node = next(
        (
            candidate
            for candidate in graph.get("nodes", [])
            if candidate.get("node_id") == "heat_shock_response"
        ),
        None,
    )
    if node is None:
        raise SystemExit("heat_shock_response node not found")

    expected = {
        "node_id": "heat_shock_response",
        "label": "heat-shock response",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": (
            "Induction of heat-shock chaperones (GroEL, DnaK) protecting "
            "protein folding under heat stress."
        ),
    }
    if node != expected:
        raise SystemExit("unexpected thermotolerant heat_shock_response preimage")

    node["grounding"] = "traitmech:000205"
    record_curation_event(
        doc,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the exact heat-shock-response biological-process node "
            "to the newly minted local traitmech:000205 heat shock response "
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
            "Minted heat shock response as a DOI-backed stress-response "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has only an "
            "obsolete heat shock response class and the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v82."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    thermotolerant = _load_thermotolerant()
    _ground_thermotolerant_heat_shock_response(thermotolerant)

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(thermotolerant, THERMOTOLERANT)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        print(f"updated {THERMOTOLERANT.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would update {THERMOTOLERANT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
