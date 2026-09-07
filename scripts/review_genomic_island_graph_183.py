#!/usr/bin/env python3
"""Review genomic_island graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_genomic_island_graph_183.py
    python scripts/review_genomic_island_graph_183.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "genomics/genomic_island"
GRAPH_ID = "gi_hgt_accessory_function"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T05:20:00Z"

RECORD_EVIDENCE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "reference": "DOI:10.1038/nrmicro884",
            "notes": (
                "Dobrindt et al. review genomic islands in pathogenic and "
                "environmental microorganisms."
            ),
        },
        "after": {
            "reference": "DOI:10.1038/nrmicro884",
            "snippet": (
                "widely distributed in pathogenic, non-pathogenic and environmental microorganisms"
            ),
            "notes": (
                "Verified against the public Nature article preview; Dobrindt et "
                "al. frame genomic islands across pathogenic, non-pathogenic, and "
                "environmental microorganisms."
            ),
        },
    },
    {
        "before": {
            "reference": "DOI:10.1111/j.1574-6976.2008.00136.x",
            "notes": (
                "Juhas et al. review genomic islands as tools of bacterial "
                "horizontal gene transfer and evolution."
            ),
        },
        "after": {
            "reference": "DOI:10.1111/j.1574-6976.2008.00136.x",
            "snippet": ("horizontal gene transfer is or has been facilitated by genomic islands"),
            "notes": (
                "Verified against the open Juhas et al. abstract; the review "
                "summarizes genomic islands as mediators of bacterial horizontal "
                "gene transfer and evolution."
            ),
        },
    },
]

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "integrative_conjugative_element",
            "label": "integrative conjugative element (ICE)",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Self-transmissible genomic island subclass that excises, "
                "transfers by conjugation, and reintegrates."
            ),
        },
        "after": {
            "node_id": "integrative_conjugative_element",
            "label": "integrative conjugative element (ICE)",
            "node_type": "GENETIC_ELEMENT",
            "description": (
                "Self-transmissible genomic island subclass that excises, "
                "transfers by conjugation, and reintegrates."
            ),
        },
    },
    {
        "before": {
            "node_id": "conjugation",
            "label": "conjugation",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Contact-dependent transfer of DNA between cells.",
        },
        "after": {
            "node_id": "conjugation",
            "label": "conjugation",
            "node_type": "BIOLOGICAL_PROCESS",
            "grounding": "GO:0009291",
            "description": "Contact-dependent transfer of DNA between cells.",
        },
    },
    {
        "before": {
            "node_id": "integrative_mobilizable_element",
            "label": "integrative mobilizable element (IME)",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Genomic island subclass that lacks its own conjugation apparatus "
                "and spreads using a helper ICE or conjugative plasmid."
            ),
        },
        "after": {
            "node_id": "integrative_mobilizable_element",
            "label": "integrative mobilizable element (IME)",
            "node_type": "GENETIC_ELEMENT",
            "description": (
                "Genomic island subclass that lacks its own conjugation apparatus "
                "and spreads using a helper ICE or conjugative plasmid."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "horizontal_gene_transfer",
            "predicate": "causes",
            "object": "gi_trait",
            "description": "Genomic islands are integrated into host chromosomes via HGT.",
            "evidence": [
                {
                    "reference": "DOI:10.1111/j.1574-6976.2008.00136.x",
                    "notes": ("Juhas et al. review genomic islands as tools of bacterial HGT."),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "horizontal_gene_transfer",
            "predicate": "causes",
            "object": "gi_trait",
            "description": "Genomic islands are integrated into host chromosomes via HGT.",
            "evidence": [
                {
                    "reference": "DOI:10.1111/j.1574-6976.2008.00136.x",
                    "snippet": (
                        "acquisition by horizontal gene transfer; (2) integration "
                        "into the host's chromosome"
                    ),
                    "notes": (
                        "Verified against the open Juhas et al. full text; the "
                        "review's mobile-genomic-island life cycle places HGT "
                        "acquisition before chromosomal integration."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "gi_trait",
            "predicate": "contributes to",
            "object": "accessory_function",
            "description": (
                "Genomic islands deliver pathogenicity, symbiosis, or metabolic "
                "modules to the host."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro884",
                    "notes": (
                        "Dobrindt et al. review genomic islands carrying virulence "
                        "and metabolic functions in pathogens and environmental "
                        "microbes."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "gi_trait",
            "predicate": "contributes to",
            "object": "accessory_function",
            "description": (
                "Genomic islands deliver pathogenicity, symbiosis, or metabolic "
                "modules to the host."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro884",
                    "snippet": "GEIs contribute to fitness and adaptation",
                    "notes": (
                        "Verified against the public Nature article preview; "
                        "Dobrindt et al. describe genomic islands as "
                        "gain-of-function elements affecting ecological and "
                        "pathogenic traits."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "gi_trait",
            "predicate": "carries",
            "object": "mobility_module",
            "description": (
                "Genomic islands often encode a dedicated mobility module (DDE "
                "transposase or tyrosine/serine recombinase)."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "notes": (
                        "Intracellular mobility is often mediated by dedicated DDE "
                        "transposases or integrases belonging to serine or tyrosine "
                        "recombinases."
                    ),
                }
            ],
        },
        "after": {
            "subject": "gi_trait",
            "predicate": "includes",
            "object": "mobility_module",
            "description": (
                "Genomic islands often include integration modules made up of DDE "
                "transposases or tyrosine/serine recombinases."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "snippet": (
                        "tyrosine (INT_Tyr) and serine (large unidirectional type, "
                        "INT_Ser) recombinases, as well as DDE transposases"
                    ),
                    "notes": (
                        "Verified against the open Bioteau et al. methods; the "
                        "AtollGenDB integrase module tracks the same DDE "
                        "transposase, serine recombinase, and tyrosine recombinase "
                        "families used for genomic-island mobility classification."
                    ),
                }
            ],
            "predicate_id": "biolink:has_part",
        },
    },
    {
        "before": {
            "subject": "integrative_conjugative_element",
            "predicate": "disseminates by",
            "object": "conjugation",
            "description": "ICE-type genomic islands spread by conjugation.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "notes": "ICEs disseminate by conjugation.",
                }
            ],
        },
        "after": {
            "subject": "integrative_conjugative_element",
            "predicate": "enables",
            "object": "conjugation",
            "description": (
                "Self-transmissible ICE-type genomic islands disseminate by conjugation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "snippet": (
                        "ICEs disseminate by conjugation, a mechanism involving "
                        "the secretion of DNA from the donor cell"
                    ),
                    "notes": (
                        "Verified against the open Bioteau et al. introduction; "
                        "ICEs are presented as self-transmissible genomic islands "
                        "that disseminate DNA by conjugation."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "integrative_conjugative_element",
            "predicate": "requires",
            "object": "type_iv_secretion_system",
            "description": "ICE conjugative transfer requires a type IV secretion system.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "notes": (
                        "ICEs disseminate by conjugation using a type IV secretion system (T4SS)."
                    ),
                }
            ],
        },
        "after": {
            "subject": "type_iv_secretion_system",
            "predicate": "enables",
            "object": "conjugation",
            "description": (
                "ICE-encoded type IV secretion systems translocate DNA between "
                "mating cells in direct contact."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "snippet": (
                        "the DNA is translocated between mating cells in direct "
                        "contact by a type IV secretion system"
                    ),
                    "notes": (
                        "Verified against the open Bioteau et al. introduction; "
                        "the paper describes ICE conjugation as direct-contact "
                        "DNA translocation mediated by a T4SS."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "integrative_mobilizable_element",
            "predicate": "uses",
            "object": "conjugation",
            "description": (
                "IME-type islands lack their own apparatus and spread via the "
                "conjugative apparatus of a helper ICE or conjugative plasmid."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "notes": (
                        "IMEs spread via the conjugative apparatus encoded by a "
                        "helper ICE or conjugative plasmid."
                    ),
                }
            ],
        },
        "after": {
            "subject": "integrative_mobilizable_element",
            "predicate": "depends on",
            "object": "conjugation",
            "description": (
                "IME-type genomic islands depend on helper ICE or "
                "conjugative-plasmid transfer machinery for conjugative "
                "mobilization."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkad644",
                    "snippet": (
                        "spread via the conjugative apparatus encoded by a helper "
                        "ICE or conjugative plasmid"
                    ),
                    "notes": (
                        "Verified against the open Bioteau et al. introduction; "
                        "IMEs are framed as mobilizable genomic islands that rely "
                        "on helper ICE or conjugative-plasmid apparatus."
                    ),
                }
            ],
            "predicate_id": "RO:0002502",
        },
    },
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{SLUG}: expected exactly one graph, found {len(graphs)}")
    graph = graphs[0]
    if graph.get("graph_id") != GRAPH_ID:
        raise ValueError(f"{SLUG}: expected graph_id {GRAPH_ID!r}")
    if graph.get("scope_status") != "NONMECHANISTIC":
        raise ValueError(f"{SLUG}: expected a NONMECHANISTIC graph")
    return graph


def _record_evidence_by_state(state: str) -> list[dict[str, Any]]:
    return [replacement[state] for replacement in RECORD_EVIDENCE_REPLACEMENTS]


def _nodes_by_state(state: str) -> dict[str, dict[str, Any]]:
    return {replacement[state]["node_id"]: replacement[state] for replacement in NODE_REPLACEMENTS}


def _edges_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_record_evidence(
    doc: dict[str, Any], expected: list[dict[str, Any]], state: str
) -> None:
    evidence = doc.get("evidence") or []
    for item in expected:
        if item not in evidence:
            raise ValueError(f"{SLUG}: missing {state} record evidence")


def _assert_exact_nodes(
    graph: dict[str, Any], expected_by_id: dict[str, dict[str, Any]], state: str
) -> None:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    missing = set(expected_by_id) - set(existing_by_id)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} node(s): {sorted(missing)}")
    for node_id, expected in expected_by_id.items():
        if existing_by_id[node_id] != expected:
            raise ValueError(f"{SLUG}: {state} node drifted: {node_id}")


def _assert_exact_edges(
    graph: dict[str, Any],
    expected_by_key: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
    state: str,
) -> None:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    missing = set(expected_by_key) - set(existing_by_key)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} edge(s): {sorted(missing)}")
    for key, expected in expected_by_key.items():
        if existing_by_key[key] != expected:
            raise ValueError(f"{SLUG}: {state} edge drifted: {key}")


def _has_exact_record_evidence(doc: dict[str, Any], expected: list[dict[str, Any]]) -> bool:
    evidence = doc.get("evidence") or []
    return all(item in evidence for item in expected)


def _has_exact_nodes(graph: dict[str, Any], nodes: dict[str, dict[str, Any]]) -> bool:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    return all(existing_by_id.get(node_id) == node for node_id, node in nodes.items())


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def _replacement_for_record_evidence(item: dict[str, Any]) -> dict[str, Any]:
    for replacement in RECORD_EVIDENCE_REPLACEMENTS:
        if item == replacement["before"]:
            return copy.deepcopy(replacement["after"])
    return item


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_record_evidence = _record_evidence_by_state("before")
    after_record_evidence = _record_evidence_by_state("after")
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    has_after_record_evidence = _has_exact_record_evidence(doc, after_record_evidence)
    has_after_nodes = _has_exact_nodes(graph, after_nodes)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_record_evidence and has_after_nodes and has_after_edges:
        return False

    if present_migrated_edge_keys == migrated_edge_keys and has_after_record_evidence:
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys or has_after_record_evidence:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"record_evidence={has_after_record_evidence} "
            f"edges={sorted(present_migrated_edge_keys)}"
        )

    _assert_exact_record_evidence(doc, before_record_evidence, "source")
    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_node_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }
    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    doc["evidence"] = [_replacement_for_record_evidence(item) for item in doc.get("evidence") or []]
    graph["nodes"] = [
        copy.deepcopy(after_by_before_node_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the gi_hgt_accessory_function graph for issue #183: "
            "added exact snippets to 8 genomic-island evidence items, grounded "
            "4 residual predicates, retyped ICE/IME nodes as GENETIC_ELEMENT, "
            "and grounded the conjugation process. No paid research service "
            "was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    path = REPO_ROOT / "data" / "traits" / f"{SLUG}.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if transform(SLUG, doc):
        changed = 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
