#!/usr/bin/env python3
"""Review gc_low graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_gc_low_graph_183.py
    python scripts/review_gc_low_graph_183.py --apply
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

SLUG = "genomics/gc_low"
GRAPH_ID = "gc_low_mid_low_gc_bin"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T05:00:00Z"

RECORD_EVIDENCE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "reference": "DOI:10.1038/nrg2358",
            "snippet": "GC content",
            "notes": (
                "Bacterial-genome review supports the mid-range GC content as a "
                "distinct genomic-composition phenotype."
            ),
        },
        "after": {
            "reference": "DOI:10.1371/journal.pgen.1001107",
            "snippet": (
                "The genomic GC-content of bacteria varies dramatically, from less "
                "than 20% to more than 70%"
            ),
            "notes": (
                "Verified against the open Hildebrand et al. abstract; bacterial "
                "genome-wide GC content spans the METPO 42.65-57.0% bin, whose "
                "cutpoints come from this record's METPO synonym."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "moderate_mutation_bias",
            "predicate": "confers",
            "object": "gc_low_trait",
            "description": "Moderate mutation-bias balance yields mid-range GC composition.",
            "evidence": [
                {
                    "reference": "DOI:10.1186/1471-2148-10-374",
                    "snippet": "mutation bias",
                    "notes": "Supports mutation-bias balance as the basis of mid-range GC bins.",
                }
            ],
            "predicate_id": "METPO:2007700",
        },
        "after": {
            "subject": "moderate_mutation_bias",
            "predicate": "contributes to",
            "object": "gc_content",
            "description": (
                "Moderate mutation-bias balance contributes to continuous "
                "genome-wide GC composition."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2024.1412318",
                    "snippet": (
                        "The GC% of genomes depends in part on the mutation rates "
                        "between each nucleotide"
                    ),
                    "notes": (
                        "Verified against the open Delgado et al. introduction; "
                        "mutation rates are described as one component of genome "
                        "GC percent, with selection pressures and codon-usage "
                        "effects also contributing."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "gc_low_trait",
            "predicate": "is a",
            "object": "gc_content",
            "description": "GC low is a quantitative bin of the GC-content phenotype.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrg2358",
                    "snippet": "GC content",
                    "notes": (
                        "Supports the 42.65–57.0% bin as a value within the "
                        "GC-content distribution."
                    ),
                }
            ],
            "predicate_id": "rdfs:subClassOf",
        },
        "after": {
            "subject": "gc_low_trait",
            "predicate": "is a",
            "object": "gc_content",
            "description": "GC low is a quantitative bin of the GC-content phenotype.",
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pgen.1001107",
                    "snippet": (
                        "The genomic GC-content of bacteria varies dramatically, from less "
                        "than 20% to more than 70%"
                    ),
                    "notes": (
                        "Verified against the open Hildebrand et al. abstract; "
                        "the public source supports genome-wide GC content as a "
                        "continuous bacterial genome-composition measurement, "
                        "while the METPO synonym supplies this bin's cutpoints."
                    ),
                }
            ],
            "predicate_id": "rdfs:subClassOf",
        },
    },
    {
        "before": {
            "subject": "dna_repair_defect",
            "predicate": "causes",
            "object": "mutational_spectrum",
            "description": (
                "Defects in DNA repair genes (MMR, BER, HR) create distinctive "
                "bacterial mutational signatures."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "notes": (
                        "Defects in DNA repair create distinctive mutational "
                        "signatures attributable to MMR, BER, or HR genes."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "dna_repair_defect",
            "predicate": "causes",
            "object": "mutational_spectrum",
            "description": (
                "Defects in DNA repair genes (MMR, BER, HR) create distinctive "
                "bacterial mutational signatures."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "snippet": ("defects in DNA repair create distinctive mutational signatures"),
                    "notes": (
                        "Verified against the open Ruis et al. abstract and "
                        "results; hypermutator lineages with mutations in MMR, "
                        "BER, or HR DNA-repair genes were used to extract "
                        "pathway-specific bacterial signatures."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "cytosine_deamination",
            "predicate": "shifts toward",
            "object": "at_enriching_spectrum",
            "description": (
                "Cytosine deamination / C>T transition bias shifts the spectrum "
                "toward AT-enriching substitutions."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "notes": (
                        "C>T was the most common mutation type in 69 of 84 SBS "
                        "spectra, potentially due to cytosine deamination."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cytosine_deamination",
            "predicate": "contributes to",
            "object": "at_enriching_spectrum",
            "description": (
                "Cytosine deamination and the resulting C>T transitions contribute "
                "to an AT-enriching bacterial mutation spectrum."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "snippet": (
                        "cytosine to thymine (C > T) was typically the most common "
                        "mutation type identified"
                    ),
                    "notes": (
                        "Verified against the open Ruis et al. results; C>T was "
                        "the most common mutation type in 69 of 84 bacterial "
                        "single-base-substitution spectra and is discussed as "
                        "potentially arising from cytosine deamination."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "at_enriching_spectrum",
            "predicate": "associated with",
            "object": "gc_low_trait",
            "description": (
                "A spectrum enriched for C>A/T and depleted for C>G is associated "
                "with lower genomic G+C content."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "notes": (
                        "Genomic G+C content negatively correlates with C>A/T "
                        "proportion and positively with C>G mutations."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
        "after": {
            "subject": "at_enriching_spectrum",
            "predicate": "associated with",
            "object": "gc_content",
            "description": (
                "AT-enriching C>A/T and depleted C>G mutation spectra are "
                "associated with continuous genome-wide G+C content."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-023-42916-w",
                    "snippet": (
                        "Genomic G + C content exhibited a negative correlation "
                        "with proportion of C > A/T mutations"
                    ),
                    "notes": (
                        "Verified against the open Ruis et al. results; the "
                        "spectrum-to-composition association is left on the "
                        "continuous GC-content node rather than asserted as "
                        "specific causation of this METPO numeric bin."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "repair_enzyme_bias",
            "predicate": "shapes",
            "object": "gc_content",
            "description": (
                "Biases of DNA replication/repair enzymes and inter-nucleotide "
                "mutation rates shape genomic GC percent."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2024.1412318",
                    "notes": (
                        "Genome GC% depends in part on mutation rates between "
                        "nucleotides; replication/repair enzymes present biases."
                    ),
                }
            ],
        },
        "after": {
            "subject": "repair_enzyme_bias",
            "predicate": "contributes to",
            "object": "gc_content",
            "description": (
                "Biases of DNA replication/repair enzymes and inter-nucleotide "
                "mutation rates contribute to genomic GC percent."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2024.1412318",
                    "snippet": (
                        "enzymes involved in DNA replication and/or repair are "
                        "known to present biases"
                    ),
                    "notes": (
                        "Verified against the open Delgado et al. introduction; "
                        "DNA replication and repair enzyme biases are framed as "
                        "mutation-rate effects that help determine genome GC "
                        "percent."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
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
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    has_after_record_evidence = _has_exact_record_evidence(doc, after_record_evidence)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_record_evidence and has_after_edges:
        return False

    if present_migrated_edge_keys == migrated_edge_keys and has_after_record_evidence:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys or has_after_record_evidence:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"record_evidence={has_after_record_evidence} "
            f"edges={sorted(present_migrated_edge_keys)}"
        )

    _assert_exact_record_evidence(doc, before_record_evidence, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    doc["evidence"] = [_replacement_for_record_evidence(item) for item in doc.get("evidence") or []]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the gc_low_mid_low_gc_bin graph for issue #183: added "
            "exact snippets to GC-low evidence and 6 causal-edge evidence "
            "items, grounded 2 residual predicates, and preserved the METPO "
            "GC_42.65_57.0 interval as a nonmechanistic whole-genome "
            "GC-content classification. No paid research service was called."
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
