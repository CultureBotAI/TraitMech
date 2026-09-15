#!/usr/bin/env python3
"""Add the SOS response physiology trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "sos_response.yaml"
FILAMENT_SHAPED = REPO_ROOT / "data" / "traits" / "morphology" / "filament_shaped.yaml"
PROPHAGE = REPO_ROOT / "data" / "traits" / "genomics" / "prophage.yaml"

MASLOWSKA = "DOI:10.1002/em.22267"
YU = "DOI:10.1002/advs.202203260"
CHEN = "DOI:10.1073/pnas.2407832121"
RECA_UNIPROT = "https://rest.uniprot.org/uniprotkb/P0A7G6.json"
LEXA_UNIPROT = "https://rest.uniprot.org/uniprotkb/P0A7C2.json"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T06:22:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000207",
    "label": "SOS response",
    "definition": (
        "A stress response in which RecA/LexA-mediated sensing of DNA "
        "damage derepresses an SOS regulon that coordinates DNA repair, "
        "damage tolerance, transient division arrest, and mutagenic "
        "survival functions."
    ),
    "definition_source": MASLOWSKA,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000078"],
    "synonyms": [
        {
            "synonym_text": "SOS system",
            "synonym_type": "RELATED_SYNONYM",
            "source": MASLOWSKA,
        }
    ],
    "evidence": [
        {
            "reference": MASLOWSKA,
            "snippet": (
                "Most bacteria have evolved a coordinated response to DNA "
                "damage"
            ),
            "notes": (
                "Maslowska et al. review the bacterial SOS response as a "
                "coordinated DNA-damage response."
            ),
        },
        {
            "reference": MASLOWSKA,
            "snippet": (
                "The SOS global regulatory network consists of multiple "
                "factors promoting the integrity of DNA as well as "
                "error-prone factors allowing for survival and continuous "
                "replication upon extensive DNA damage"
            ),
            "notes": (
                "The SOS regulon coordinates high-fidelity DNA-integrity "
                "functions with error-prone survival functions induced "
                "under extensive DNA damage."
            ),
        },
        {
            "reference": YU,
            "snippet": (
                "the SOS response is activated through the binding of recA "
                "with single stranded DNA and the self-cleavage of the lexA "
                "repressor, enabling expression of SOS regulon genes"
            ),
            "notes": (
                "Yu et al. directly support the RecA/LexA activation branch "
                "of the SOS response."
            ),
        },
        {
            "reference": YU,
            "snippet": (
                "cell division inhibitor, sulA, blocks FtsZ (a master "
                "regulator of bacterial cell division and responsible for "
                "the Z ring formation at mid-cell) polymerization"
            ),
            "notes": (
                "Yu et al. support SOS-induced division inhibition as one "
                "physiological output of the response."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "E. coli is the canonical RecA/LexA SOS-response model "
                "reviewed by Maslowska et al."
            ),
            "reference": MASLOWSKA,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "sos_response_dna_damage_regulon",
            "title": "DNA-damage SOS regulon induction",
            "description": (
                "Evidence-backed causal sketch linking DNA damage and "
                "single-stranded DNA accumulation to RecA/LexA derepression "
                "of SOS-regulon functions."
            ),
            "scope_status": "MECHANISTIC",
            "scope_notes": (
                "This graph captures the classical E. coli RecA/LexA branch "
                "of SOS induction. It does not make every SOS-regulon "
                "member, error-prone polymerase, or prophage-induction "
                "branch universal across bacteria."
            ),
            "nodes": [
                {
                    "node_id": "sos_response_trait",
                    "label": "SOS response",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000207",
                    "description": (
                        "Capacity to mount the bacterial SOS DNA-damage "
                        "response."
                    ),
                },
                {
                    "node_id": "genotoxic_stress",
                    "label": "genotoxic stress",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "Genotoxic stress or replication inhibition that "
                        "exposes single-stranded DNA."
                    ),
                },
                {
                    "node_id": "single_stranded_dna_accumulation",
                    "label": "single-stranded DNA accumulation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Production or exposure of single-stranded DNA after "
                        "DNA damage or replication stress."
                    ),
                },
                {
                    "node_id": "reca_nucleoprotein_filament",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "Reviewed activated protein state; no single "
                        "taxon-agnostic family, activity, or complex term "
                        "captures RecA polymerized on DNA in its SOS-inducing "
                        "state."
                    ),
                    "label": "RecA nucleoprotein filament",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "Activated RecA filament on single-stranded DNA that "
                        "stimulates LexA autoproteolysis."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0A7G6",
                            "protein_label": "Protein RecA",
                            "gene_symbol": "recA",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 168,
                            "sequence_version": 2,
                            "role": (
                                "E. coli K-12 RecA polymerizes on "
                                "single-stranded DNA and activates LexA "
                                "autoproteolysis during SOS induction."
                            ),
                            "evidence": [
                                {
                                    "reference": RECA_UNIPROT,
                                    "snippet": (
                                        "Interacts with and activates LexA "
                                        "leading to autocatalytic cleavage of "
                                        "LexA, which derepresses the SOS "
                                        "regulon"
                                    ),
                                    "notes": (
                                        "Verified against the live UniProt "
                                        "REST entry for P0A7G6 retrieved on "
                                        "2026-09-15."
                                    ),
                                }
                            ],
                        }
                    ],
                },
                {
                    "node_id": "lexa_repressor",
                    "label": "LexA repressor",
                    "node_type": "GENE_OR_PROTEIN",
                    "grounding": "InterPro:IPR050077",
                    "description": (
                        "SOS master repressor inactivated by RecA-stimulated "
                        "autoproteolysis."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0A7C2",
                            "protein_label": "LexA repressor",
                            "gene_symbol": "lexA",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 160,
                            "sequence_version": 1,
                            "role": (
                                "E. coli K-12 LexA represses SOS genes and "
                                "undergoes RecA-stimulated autocleavage to "
                                "derepress the SOS regulon."
                            ),
                            "evidence": [
                                {
                                    "reference": LEXA_UNIPROT,
                                    "snippet": (
                                        "RecA interacts with LexA causing an "
                                        "autocatalytic cleavage which "
                                        "disrupts the DNA-binding part of "
                                        "LexA, leading to derepression of the "
                                        "SOS regulon"
                                    ),
                                    "notes": (
                                        "Verified against the live UniProt "
                                        "REST entry for P0A7C2 retrieved on "
                                        "2026-09-15."
                                    ),
                                }
                            ],
                        }
                    ],
                },
                {
                    "node_id": "lexa_autoproteolysis",
                    "label": "LexA autoproteolysis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "RecA-stimulated autocleavage of the LexA SOS "
                        "repressor."
                    ),
                },
                {
                    "node_id": "sos_regulon_expression",
                    "label": "SOS regulon expression",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Induced expression of LexA-repressed genes in the "
                        "SOS regulon."
                    ),
                },
                {
                    "node_id": "dna_repair_damage_tolerance",
                    "label": "DNA repair and damage tolerance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DNA-integrity, translesion-synthesis, mutagenesis, "
                        "and division-delay functions induced by the SOS "
                        "regulon."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "genotoxic_stress",
                    "predicate": "causes",
                    "predicate_id": "biolink:causes",
                    "object": "single_stranded_dna_accumulation",
                    "description": (
                        "Genotoxic stress and replication inhibition expose "
                        "single-stranded DNA that initiates the SOS cascade."
                    ),
                    "evidence": [
                        {
                            "reference": CHEN,
                            "snippet": (
                                "AZT increases the burden of ssDNA at the "
                                "replication fork and induces the SOS "
                                "response via the RecAFOR pathway"
                            ),
                            "notes": (
                                "Verified against the open PNAS/PMC full "
                                "text; the replication inhibitor AZT raises "
                                "single-stranded DNA at replication forks "
                                "and induces SOS through RecFOR."
                            ),
                        }
                    ],
                },
                {
                    "subject": "single_stranded_dna_accumulation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "reca_nucleoprotein_filament",
                    "description": (
                        "Single-stranded DNA supports activated RecA "
                        "nucleoprotein filament formation."
                    ),
                    "evidence": [
                        {
                            "reference": RECA_UNIPROT,
                            "snippet": (
                                "Polymerizes non-specifically on ssDNA to "
                                "form filaments; filament formation requires "
                                "ATP or ATP-gamma-S"
                            ),
                            "notes": (
                                "Verified against the live UniProt REST "
                                "entry for P0A7G6 retrieved on 2026-09-15."
                            ),
                        }
                    ],
                },
                {
                    "subject": "reca_nucleoprotein_filament",
                    "predicate": "promotes",
                    "predicate_id": "RO:0002213",
                    "object": "lexa_autoproteolysis",
                    "description": (
                        "Activated RecA promotes LexA autocleavage."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": (
                                "the SOS response is activated through the "
                                "binding of recA with single stranded DNA and "
                                "the self-cleavage of the lexA repressor"
                            ),
                            "notes": (
                                "Verified against the open Wiley full text "
                                "during the cell-length graph curation; the "
                                "source links RecA-ssDNA to LexA "
                                "self-cleavage."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lexa_repressor",
                    "predicate": "negatively regulates",
                    "predicate_id": "RO:0002212",
                    "object": "sos_regulon_expression",
                    "description": (
                        "LexA represses SOS-regulon expression before it is "
                        "inactivated."
                    ),
                    "evidence": [
                        {
                            "reference": LEXA_UNIPROT,
                            "snippet": (
                                "Represses a number of genes involved in the "
                                "response to DNA damage (SOS response), "
                                "including recA and lexA"
                            ),
                            "notes": (
                                "Verified against the live UniProt REST "
                                "entry for P0A7C2 retrieved on 2026-09-15."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lexa_autoproteolysis",
                    "predicate": "derepresses",
                    "object": "sos_regulon_expression",
                    "description": (
                        "LexA autocleavage disrupts DNA binding and releases "
                        "repression of SOS genes."
                    ),
                    "evidence": [
                        {
                            "reference": LEXA_UNIPROT,
                            "snippet": (
                                "disrupts the DNA-binding part of LexA, "
                                "leading to derepression of the SOS regulon"
                            ),
                            "notes": (
                                "Verified against the live UniProt REST "
                                "entry for P0A7C2 retrieved on 2026-09-15."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sos_regulon_expression",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dna_repair_damage_tolerance",
                    "description": (
                        "SOS-regulon expression coordinates DNA-integrity and "
                        "damage-tolerance functions."
                    ),
                    "evidence": [
                        {
                            "reference": MASLOWSKA,
                            "snippet": (
                                "multiple factors promoting the integrity of "
                                "DNA as well as error-prone factors allowing "
                                "for survival and continuous replication upon "
                                "extensive DNA damage"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; SOS-regulon functions span DNA "
                                "integrity and error-prone survival."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dna_repair_damage_tolerance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sos_response_trait",
                    "description": (
                        "The induced repair and damage-tolerance program "
                        "realizes the SOS-response trait."
                    ),
                    "evidence": [
                        {
                            "reference": MASLOWSKA,
                            "snippet": (
                                "Most bacteria have evolved a coordinated "
                                "response to DNA damage"
                            ),
                            "notes": (
                                "Verified against the public Crossref "
                                "abstract; the SOS response is an induced, "
                                "coordinated bacterial DNA-damage response."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "sos-response-xref-gap",
            "prompt": (
                "Resolve exact ontology xrefs for organism-level microbial "
                "SOS response before adding TraitRecord xrefs."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0009432 SOS response exactly grounds "
                "biological-process nodes in causal graphs but is shifted "
                "from this organism-level response trait. RecA, LexA, SulA, "
                "translesion-polymerase, prophage-induction, DNA-repair, and "
                "DNA-damage terms describe narrower machinery, downstream "
                "processes, or related triggers rather than the whole "
                "microbial SOS-response phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        }
    ],
}


def _load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _ground_filament_shaped(doc: dict[str, Any]) -> None:
    if (
        doc.get("identifier") != "METPO:1000674"
        or doc.get("label") != "filament shaped"
        or doc.get("mapping_status") != "REVIEWED"
        or doc.get("parent_traits") != ["METPO:1000666"]
    ):
        raise SystemExit("unexpected filament_shaped identity preimage")

    graphs = {
        graph.get("graph_id"): graph
        for graph in doc.get("causal_graphs", [])
    }
    graph = graphs.get("filament_shaped_streptomyces_polar_growth")
    if graph is None:
        raise SystemExit("filament_shaped graph not found")

    nodes = {node.get("node_id"): node for node in graph.get("nodes", [])}
    node = nodes.get("dna_damage_sos_response")
    if node is None:
        raise SystemExit("dna_damage_sos_response node not found")

    if (
        node.get("label") != "RecA/LexA SOS response"
        or node.get("node_type") != "BIOLOGICAL_PROCESS"
        or node.get("grounding") is not None
    ):
        raise SystemExit("unexpected filament_shaped SOS node preimage")

    node["grounding"] = "GO:0009432"
    record_curation_event(
        doc,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the RecA/LexA SOS-response biological-process node to "
            "GO:0009432 while adding the organism-level traitmech:000207 "
            "SOS response record."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def _ground_prophage(doc: dict[str, Any]) -> None:
    if (
        doc.get("identifier") != "traitmech:000091"
        or doc.get("label") != "prophage"
        or doc.get("mapping_status") != "REVIEWED"
        or doc.get("parent_traits") != ["traitmech:000089"]
    ):
        raise SystemExit("unexpected prophage identity preimage")

    graphs = {
        graph.get("graph_id"): graph
        for graph in doc.get("causal_graphs", [])
    }
    graph = graphs.get("prophage_lysogeny")
    if graph is None:
        raise SystemExit("prophage_lysogeny graph not found")

    nodes = {node.get("node_id"): node for node in graph.get("nodes", [])}
    node = nodes.get("sos_response")
    if node is None:
        raise SystemExit("prophage sos_response node not found")

    if (
        node.get("label") != "RecA-LexA SOS response"
        or node.get("node_type") != "BIOLOGICAL_PROCESS"
        or node.get("grounding") is not None
    ):
        raise SystemExit("unexpected prophage SOS node preimage")

    node["grounding"] = "GO:0009432"
    record_curation_event(
        doc,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the RecA-LexA SOS-response biological-process node to "
            "GO:0009432 while adding the organism-level traitmech:000207 "
            "SOS response record."
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
            "Minted SOS response as a DOI-backed stress-response "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has no "
            "active exact SOS response class and the replacement placeholder "
            "is reserved in proposals/metpo_traitmech_v84."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    filament_shaped = _load_record(FILAMENT_SHAPED)
    prophage = _load_record(PROPHAGE)
    _ground_filament_shaped(filament_shaped)
    _ground_prophage(prophage)

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(filament_shaped, FILAMENT_SHAPED)
        write_validated_trait(prophage, PROPHAGE)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        print(f"updated {FILAMENT_SHAPED.relative_to(REPO_ROOT)}")
        print(f"updated {PROPHAGE.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would update {FILAMENT_SHAPED.relative_to(REPO_ROOT)}")
        print(f"would update {PROPHAGE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
