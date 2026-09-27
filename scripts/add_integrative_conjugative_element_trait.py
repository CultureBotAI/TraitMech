#!/usr/bin/env python3
"""Add the integrative conjugative element genomics trait."""

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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "integrative_conjugative_element.yaml"
)
GENOMIC_ISLAND = REPO_ROOT / "data" / "traits" / "genomics" / "genomic_island.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T14:42:32Z"
IDENTIFIER = "traitmech:000410"
PARENT_IDENTIFIER = "traitmech:000093"
PROPOSAL = "proposals/metpo_traitmech_v287"

JOHNSON_GROSSMAN = "DOI:10.1146/annurev-genet-112414-055018"
BIOTEAU_ATOLLGEN = "DOI:10.1093/nar/gkad644"


def johnson_definition_evidence() -> dict[str, str]:
    return {
        "reference": JOHNSON_GROSSMAN,
        "snippet": (
            "There are two defining features of ICEs: (a) They are found integrated "
            "in a host genome; and (b) they encode a functional conjugation system, "
            "a type IV secretion system"
        ),
        "notes": (
            "Johnson and Grossman define integrative and conjugative elements as "
            "host-integrated mobile genetic elements that encode a functional "
            "type IV secretion conjugation system."
        ),
    }


def bioteau_genomic_island_evidence() -> dict[str, str]:
    return {
        "reference": BIOTEAU_ATOLLGEN,
        "snippet": (
            "The term ‘genomic island’ encompasses diverse types of mobile genetic "
            "elements that exhibit various structures and gene contents, including "
            "prophages, transposons, integrated plasmids, integrative and "
            "mobilizable elements (IMEs), and integrative and conjugative "
            "elements (ICEs)"
        ),
        "notes": (
            "Bioteau et al. place integrative and conjugative elements among "
            "the mobile-genetic-element subclasses encompassed by genomic islands."
        ),
    }


def johnson_excision_evidence() -> dict[str, str]:
    return {
        "reference": JOHNSON_GROSSMAN,
        "snippet": (
            "When ICE gene expression is induced, by specific cellular conditions "
            "or perhaps stochastically, the ICE excises from the chromosome and "
            "forms a circular dsDNA molecule"
        ),
        "notes": (
            "Johnson and Grossman summarize induction-linked ICE excision and "
            "circular double-stranded DNA intermediate formation."
        ),
    }


def johnson_relaxosome_evidence() -> dict[str, str]:
    return {
        "reference": JOHNSON_GROSSMAN,
        "snippet": (
            "Other host and ICE-encoded proteins recognize the origin of transfer "
            "(oriT) and process the ICE DNA to generate a linear ssDNA-protein "
            "complex"
        ),
        "notes": (
            "Johnson and Grossman describe oriT recognition and ICE DNA processing "
            "that produces the linear transfer-DNA complex."
        ),
    }


def johnson_transfer_evidence() -> dict[str, str]:
    return {
        "reference": JOHNSON_GROSSMAN,
        "snippet": "The mating machinery pumps the T-DNA into the recipient",
        "notes": (
            "The Johnson and Grossman life-cycle summary places mating-machinery "
            "transport after transfer-DNA generation."
        ),
    }


def johnson_integration_evidence() -> dict[str, str]:
    return {
        "reference": JOHNSON_GROSSMAN,
        "snippet": (
            "In both the donor and recipient, the circular dsDNA ICE integrates "
            "into the host chromosome."
        ),
        "notes": (
            "Johnson and Grossman's ICE life-cycle figure caption states that the "
            "circular double-stranded ICE reintegrates in donor and recipient cells."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "integrative conjugative element",
    "definition": (
        "A genomic island trait in which an organism possesses an integrative "
        "and conjugative element, a self-transmissible mobile genetic element "
        "that integrates into host DNA, excises under induced expression, and "
        "encodes type IV secretion machinery for conjugative transfer to "
        "recipient cells."
    ),
    "definition_source": JOHNSON_GROSSMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_IDENTIFIER],
    "synonyms": [
        {
            "synonym_text": "ICE",
            "synonym_type": "RELATED_SYNONYM",
            "source": JOHNSON_GROSSMAN,
        },
    ],
    "evidence": [
        johnson_definition_evidence(),
        bioteau_genomic_island_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1423",
            "taxon_label": "Bacillus subtilis",
            "note": "ICEBs1",
            "reference": JOHNSON_GROSSMAN,
        },
        {
            "taxon_id": "NCBITaxon:1351",
            "taxon_label": "Enterococcus faecalis",
            "note": "Tn916",
            "reference": JOHNSON_GROSSMAN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "ice_excision_conjugation_integration",
            "title": "ICEs excise, transfer by conjugation, and reintegrate",
            "description": (
                "Conservative ICE life-cycle sketch linking an integrated ICE "
                "locus to circularization, oriT processing, T4SS-mediated "
                "conjugative transfer, recipient integration, and the "
                "genomic-island possession trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "This genomics graph summarizes the shared ICE life cycle at the "
                "mobile-element level. It does not assert exact protein-family "
                "groundings for heterogeneous ICE integrases, relaxases, type IV "
                "coupling proteins, or T4SS subunits."
            ),
            "nodes": [
                {
                    "node_id": "integrated_ice_locus",
                    "label": "integrated ICE locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An integrative and conjugative element integrated into a "
                        "host replicon."
                    ),
                },
                {
                    "node_id": "ice_excision_circularization",
                    "label": "ICE excision and circularization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Induction-associated excision of an integrated ICE to a "
                        "circular double-stranded DNA intermediate."
                    ),
                },
                {
                    "node_id": "orit_processing",
                    "label": "oriT processing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Processing at the ICE origin of transfer to generate the "
                        "linear transfer-DNA complex."
                    ),
                },
                {
                    "node_id": "conjugation",
                    "label": "conjugation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "grounding": "GO:0009291",
                    "description": (
                        "Contact-dependent transfer of ICE DNA into a recipient "
                        "cell through the conjugation machinery."
                    ),
                },
                {
                    "node_id": "ice_integration",
                    "label": "ICE integration",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recombination of circular ICE DNA into the recipient "
                        "host chromosome."
                    ),
                },
                {
                    "node_id": "integrative_conjugative_element",
                    "label": "integrative conjugative element",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded integrative and "
                        "conjugative element."
                    ),
                },
                {
                    "node_id": "genomic_island",
                    "label": "genomic island",
                    "node_type": "TRAIT",
                    "grounding": PARENT_IDENTIFIER,
                    "description": (
                        "Possession of a horizontally acquired chromosomal island."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "integrated_ice_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "ice_excision_circularization",
                    "description": (
                        "Upon induction, an integrated ICE excises from the "
                        "chromosome and forms a circular dsDNA intermediate."
                    ),
                    "evidence": [johnson_excision_evidence()],
                },
                {
                    "subject": "ice_excision_circularization",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "orit_processing",
                    "description": (
                        "The circular ICE is processed at oriT to generate the "
                        "linear ssDNA-protein transfer complex."
                    ),
                    "evidence": [johnson_relaxosome_evidence()],
                },
                {
                    "subject": "orit_processing",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "conjugation",
                    "description": (
                        "The mating machinery transports the processed transfer "
                        "DNA into a recipient cell."
                    ),
                    "evidence": [johnson_transfer_evidence()],
                },
                {
                    "subject": "conjugation",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "ice_integration",
                    "description": (
                        "Transferred ICE DNA recircularizes and becomes a "
                        "double-stranded integration substrate in the recipient."
                    ),
                    "evidence": [johnson_integration_evidence()],
                },
                {
                    "subject": "ice_integration",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "integrative_conjugative_element",
                    "description": (
                        "Recipient-chromosome integration completes possession "
                        "of an integrated conjugative element."
                    ),
                    "evidence": [johnson_definition_evidence()],
                },
                {
                    "subject": "integrative_conjugative_element",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "genomic_island",
                    "description": (
                        "Integrative-conjugative-element possession is a "
                        "genomic-island possession trait."
                    ),
                    "evidence": [bioteau_genomic_island_evidence()],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "ice-family-resolution-gap",
            "prompt": (
                "Resolve bacterial ICE subfamilies, Actinomycete ICE boundaries, "
                "integrase/relaxase/T4SS signatures, and cargo-phenotype scope "
                "before minting narrower ICE mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Johnson and Grossman define ICEs by host-genome integration and "
                "a functional type IV secretion conjugation system, while Bioteau "
                "et al. classify ICEs as self-transmissible genomic islands. This "
                "first record captures the genome-level possession trait without "
                "claiming exact molecular groundings for heterogeneous integrases, "
                "relaxases, T4SS variants, Actinomycete ICE machinery, or adaptive "
                "cargo phenotypes."
            ),
            "attaches_to": ["causal_graphs#ice_excision_conjugation_integration"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        },
    ],
}


def load_existing_trait(path: Path) -> dict[str, Any]:
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise SystemExit(f"{path}: expected mapping")
    if doc.get("identifier") != PARENT_IDENTIFIER:
        raise SystemExit(
            f"{path}: expected identifier {PARENT_IDENTIFIER!r}, "
            f"found {doc.get('identifier')!r}"
        )
    if doc.get("label") != "genomic island":
        raise SystemExit(
            f"{path}: expected label 'genomic island', found {doc.get('label')!r}"
        )
    if doc.get("mapping_status") != "REVIEWED":
        raise SystemExit(
            f"{path}: expected REVIEWED record, found {doc.get('mapping_status')!r}"
        )
    if doc.get("parent_traits") != ["traitmech:000089"]:
        raise SystemExit(
            f"{path}: expected mobile-genetic-element parent, "
            f"found {doc.get('parent_traits')!r}"
        )
    return doc


def target_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = [
        graph
        for graph in doc.get("causal_graphs") or []
        if graph.get("graph_id") == "gi_hgt_accessory_function"
    ]
    if len(graphs) != 1:
        raise SystemExit(f"expected one genomic-island graph, found {len(graphs)}")
    return graphs[0]


def ground_ice_node(doc: dict[str, Any]) -> None:
    graph = target_graph(doc)
    nodes = [
        node
        for node in graph.get("nodes") or []
        if node.get("node_id") == "integrative_conjugative_element"
    ]
    if len(nodes) != 1:
        raise SystemExit(f"expected one ICE node, found {len(nodes)}")
    node = nodes[0]
    expected = {
        "node_id": "integrative_conjugative_element",
        "label": "integrative conjugative element (ICE)",
        "node_type": "GENETIC_ELEMENT",
        "description": (
            "Self-transmissible genomic island subclass that excises, transfers by "
            "conjugation, and reintegrates."
        ),
    }
    if node != expected:
        raise SystemExit(f"unexpected ICE node preimage: {node!r}")

    subclass_edges = [
        edge
        for edge in graph.get("edges") or []
        if edge.get("subject") == "integrative_conjugative_element"
        and edge.get("predicate_id") == "rdfs:subClassOf"
    ]
    if subclass_edges:
        raise SystemExit("genomic-island graph already has an ICE subclass edge")

    node.update(
        {
            "label": "integrative conjugative element",
            "node_type": "TRAIT",
            "grounding": IDENTIFIER,
            "description": (
                "Possession of a self-transmissible integrative and conjugative "
                "genomic island."
            ),
        }
    )
    graph["edges"].append(
        {
            "subject": "integrative_conjugative_element",
            "predicate": "is a",
            "predicate_id": "rdfs:subClassOf",
            "object": "gi_trait",
            "description": (
                "Integrative-conjugative-element possession is a genomic-island "
                "possession trait."
            ),
            "evidence": [bioteau_genomic_island_evidence()],
        }
    )

    record_curation_event(
        doc,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODES",
        changes=(
            "Resolved the exact ICE causal node by grounding it to traitmech:000410 "
            "and reintroducing an rdfs:subClassOf edge only after the node was "
            "retyped from a raw genetic element to the possession trait."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def write_new_record() -> None:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted integrative conjugative element as a DOI-backed GENOMICS "
            "TraitRecord under genomic island with ICEBs1 and Tn916 canonical "
            "examples after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    write_validated_trait(record, TARGET)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the ICE trait and ground the old genomic-island ICE node",
    )
    args = parser.parse_args()

    if not args.apply:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would update {GENOMIC_ISLAND.relative_to(REPO_ROOT)}")
        return 0

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    write_new_record()
    print(f"wrote {TARGET.relative_to(REPO_ROOT)}")

    genomic_island = load_existing_trait(GENOMIC_ISLAND)
    ground_ice_node(genomic_island)
    write_validated_trait(genomic_island, GENOMIC_ISLAND)
    print(f"updated {GENOMIC_ISLAND.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
