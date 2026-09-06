#!/usr/bin/env python3
"""Review saprotrophy graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_saprotrophy_graph_183.py
    python scripts/review_saprotrophy_graph_183.py --apply
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

SLUG = "ecology/saprotrophy"
GRAPH_ID = "saprotrophy_decomposition_cycling"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T07:00:00Z"

RECORD_EVIDENCE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "reference": "DOI:10.3389/fmicb.2012.00348",
            "notes": (
                'Schimel & Schaeffer, "Microbial control over carbon cycling '
                'in soil", support microbial decomposition of organic matter '
                "as a central ecosystem process."
            ),
        },
        "after": {
            "reference": "DOI:10.3389/fmicb.2012.00348",
            "snippet": "soil microbial community structure influences C cycling",
            "notes": (
                "Verified against the open Schimel and Schaeffer abstract; "
                "the review frames microbial organic-matter breakdown and "
                "extracellular enzymes as controls on soil carbon cycling."
            ),
        },
    },
    {
        "before": {
            "reference": "DOI:10.1038/nrmicro.2017.87",
            "notes": (
                "Fierer supports decomposer/saprotrophic activity as a key "
                "function of soil microbial communities."
            ),
        },
        "after": {
            "reference": "DOI:10.1038/nrmicro.2017.87",
            "snippet": (
                "crucial roles in nutrient cycling, the maintenance of soil "
                "fertility and soil carbon sequestration"
            ),
            "notes": (
                "Verified against a public copy of Fierer; the review supports "
                "the broad ecosystem role of soil microbial communities in "
                "nutrient cycling, fertility, and carbon storage."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "saprotrophy_trait",
            "predicate": "enables",
            "object": "decomposition",
            "description": "Saprotrophic activity breaks down dead organic matter.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2012.00348",
                    "notes": (
                        "Schimel & Schaeffer support microbial decomposition "
                        "of organic matter as a central ecosystem process."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "saprotrophy_trait",
            "predicate": "enables",
            "object": "decomposition",
            "description": "Saprotrophic activity breaks down dead organic matter.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2012.00348",
                    "snippet": ("rate of OM breakdown in the rhizosphere and in detritus"),
                    "notes": (
                        "Verified against the open Schimel and Schaeffer "
                        "abstract; the edge links decomposer activity to organic "
                        "matter turnover without asserting a single mechanism."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "decomposition",
            "predicate": "consumes",
            "object": "dead_organic_matter",
            "description": "Decomposition uses dead organic matter as substrate.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro.2017.87",
                    "notes": (
                        "Fierer supports decomposer activity as a key function "
                        "of soil microbial communities."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
        "after": {
            "subject": "decomposition",
            "predicate": "consumes",
            "object": "dead_organic_matter",
            "description": "Decomposition uses dead organic matter as substrate.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2012.00348",
                    "snippet": ("exoenzyme breakdown is necessary for microbes to metabolize them"),
                    "notes": (
                        "Verified against the open Schimel and Schaeffer text; "
                        "dead detrital organic structures are retained as "
                        "substrates that require extracellular breakdown."
                    ),
                }
            ],
            "predicate_id": "biolink:consumes",
        },
    },
    {
        "before": {
            "subject": "extracellular_exoenzymes",
            "predicate": "converts insoluble organic matter into",
            "object": "soluble_organic_compounds",
            "description": (
                "Saprotrophs use secreted exoenzymes to hydrolyze/oxidize "
                "insoluble dead organic matter into soluble compounds for uptake."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/ismejo/wrae073",
                    "notes": (
                        "Saprotrophic microbes obtain carbon and energy by "
                        "hydrolyzing/oxidizing dead organic matter into soluble "
                        "compounds; insoluble compounds require extracellular "
                        "enzymes."
                    ),
                }
            ],
        },
        "after": {
            "subject": "extracellular_exoenzymes",
            "predicate": "contributes to",
            "object": "soluble_organic_compounds",
            "description": (
                "Extracellular exoenzymes contribute soluble decomposition "
                "products by acting on complex organic compounds."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/ismejo/wrae073",
                    "snippet": (
                        "products released by extracellular reactions of "
                        "exoenzymes produced by another group"
                    ),
                    "notes": (
                        "Verified against the open Wang et al. text; the edge "
                        "keeps a broad substrate-cross-feeding claim about "
                        "diffusible exoenzyme products in soil."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "cellulolytic_enzymes",
            "predicate": "depolymerizes",
            "object": "cellulose",
            "description": (
                "Cellobiohydrolases, endoglucanases, and beta-glucosidases act "
                "in concert to break down cellulose."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "Complete degradation of cellulose into glucose involves "
                        "concerted action of cellobiohydrolases, endoglucanases, "
                        "and beta-glucosidases."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cellulolytic_enzymes",
            "predicate": "hydrolyzes",
            "object": "cellulose",
            "description": (
                "Cellobiohydrolases, endoglucanases, and beta-glucosidases act "
                "in concert to break down cellulose."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": (
                        "degradation of cellulose into glucose involves a "
                        "concerted action of several enzymes"
                    ),
                    "notes": (
                        "Verified against the open Gurovic et al. text; "
                        "cellobiohydrolases, endoglucanases, and "
                        "beta-glucosidases are retained as a cellulolytic "
                        "enzyme-system node."
                    ),
                }
            ],
            "predicate_id": "METPO:2007808",
        },
    },
    {
        "before": {
            "subject": "cellulose",
            "predicate": "is converted to",
            "object": "glucose",
            "description": "Cellulose depolymerization yields glucose.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "Complete degradation of cellulose into glucose by the "
                        "cellulolytic enzyme system."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cellulose",
            "predicate": "is hydrolyzed to",
            "object": "glucose",
            "description": "Cellulose hydrolysis yields glucose.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": "The complete degradation of cellulose into glucose",
                    "notes": (
                        "Verified against the open Gurovic et al. text; "
                        "cellulose is retained as a substrate that derives into "
                        "glucose after enzymatic hydrolysis."
                    ),
                }
            ],
            "predicate_id": "RO:0001001",
        },
    },
    {
        "before": {
            "subject": "cazymes",
            "predicate": "hydrolyzes",
            "object": "hemicellulose",
            "description": (
                "Extracellular CAZymes hydrolyze hemicellulose polysaccharides at glycosidic bonds."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "CAZymes act on glycosidic bonds; hemicellulose is "
                        "targeted by xylanases, beta-mannanases, pectate lyases "
                        "and related enzymes."
                    ),
                }
            ],
            "predicate_id": "METPO:2007808",
        },
        "after": {
            "subject": "cazymes",
            "predicate": "hydrolyzes",
            "object": "hemicellulose",
            "description": (
                "Extracellular CAZymes hydrolyze hemicellulose polysaccharides at glycosidic bonds."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": "Cellulose and hemicelluloses are substrates for these enzymes",
                    "notes": (
                        "Verified against the open Gurovic et al. figure text; "
                        "the broad CAZyme node is retained for "
                        "hemicellulose-active enzymes."
                    ),
                }
            ],
            "predicate_id": "METPO:2007808",
        },
    },
    {
        "before": {
            "subject": "laccase",
            "predicate": "oxidizes and depolymerizes",
            "object": "lignin",
            "description": (
                "Laccase oxidatively depolymerizes lignin and phenolic "
                "substrates via electron transfer."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "Laccases and peroxidases degrade lignin and the "
                        "corresponding monomers; laccases modify lignin via "
                        "hydrogen atom abstraction or electron transfer."
                    ),
                }
            ],
        },
        "after": {
            "subject": "laccase",
            "predicate": "oxidizes",
            "object": "lignin",
            "description": (
                "Laccase oxidatively degrades lignin and phenolic substrates via electron transfer."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": "Laccases and peroxidases degrade not only lignin",
                    "notes": (
                        "Verified against the open Gurovic et al. figure text; "
                        "laccase is retained as a contextual fungal and "
                        "bacterial ligninolytic enzyme."
                    ),
                }
            ],
            "predicate_id": "METPO:2007803",
        },
    },
    {
        "before": {
            "subject": "manganese_peroxidase",
            "predicate": "catalyzes H2O2-dependent oxidation of",
            "object": "lignin",
            "description": (
                "Manganese peroxidase performs H2O2-dependent oxidative degradation of lignin."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "Fungal ligninolytic enzymes are mainly manganese "
                        "peroxidases (MnP) and lignin peroxidases (LiP) "
                        "catalyzing oxidative reactions dependent on H2O2."
                    ),
                }
            ],
        },
        "after": {
            "subject": "manganese_peroxidase",
            "predicate": "oxidizes",
            "object": "lignin",
            "description": (
                "Manganese peroxidase performs H2O2-dependent oxidative degradation of lignin."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": (
                        "manganese peroxidases (MnP), lignin peroxidases (LiP) "
                        "catalyzing a variety of oxidative reactions"
                    ),
                    "notes": (
                        "Verified against the open Gurovic et al. text; the "
                        "edge is grounded to the canonical oxidative predicate "
                        "for the fungal MnP ligninolysis claim."
                    ),
                }
            ],
            "predicate_id": "METPO:2007803",
        },
    },
    {
        "before": {
            "subject": "glucose",
            "predicate": "represses",
            "object": "lignocellulolytic_gene_expression",
            "description": (
                "Simple sugars/glucose trigger carbon catabolite repression "
                "that represses lignocellulolytic gene expression."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "notes": (
                        "Glucose is a repressor of fungal cellulolytic enzymes; "
                        "preferred simple carbon sources cause "
                        "CreA/Cre1-mediated repression."
                    ),
                }
            ],
        },
        "after": {
            "subject": "glucose",
            "predicate": "negatively regulates",
            "object": "lignocellulolytic_gene_expression",
            "description": (
                "Simple sugars/glucose trigger carbon catabolite repression "
                "that represses lignocellulolytic gene expression."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/jambio/lxac002",
                    "snippet": "glucose is a repressor of fungal cellulolytic enzymes",
                    "notes": (
                        "Verified against the open Gurovic et al. text; the "
                        "edge is a broad carbon-catabolite-repression "
                        "regulatory edge."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
]


def _find_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = [graph for graph in doc.get("causal_graphs", []) if graph.get("graph_id") == GRAPH_ID]
    if len(graphs) != 1:
        raise ValueError(f"{SLUG}: expected exactly one {GRAPH_ID} graph, found {len(graphs)}")
    return graphs[0]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _edges_by_state(state: str) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _record_evidence_by_state(state: str) -> list[dict[str, Any]]:
    return [replacement[state] for replacement in RECORD_EVIDENCE_REPLACEMENTS]


def _assert_exact_record_evidence(
    doc: dict[str, Any], expected: list[dict[str, Any]], state: str
) -> None:
    existing = doc.get("evidence") or []
    missing = [item for item in expected if item not in existing]
    if missing:
        raise ValueError(f"{SLUG}: missing {state} record evidence: {missing}")


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


def _has_any_exact_record_evidence(doc: dict[str, Any], expected: list[dict[str, Any]]) -> bool:
    evidence = doc.get("evidence") or []
    return any(item in evidence for item in expected)


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

    has_after_record_evidence = _has_exact_record_evidence(doc, after_record_evidence)
    has_some_after_record_evidence = _has_any_exact_record_evidence(doc, after_record_evidence)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_record_evidence and has_after_edges:
        return False

    if has_after_record_evidence:
        _assert_exact_edges(graph, after_edges, "migrated")

    if has_after_record_evidence or has_after_edges:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"record_evidence={has_after_record_evidence} "
            f"edges={has_after_edges}"
        )
    if has_some_after_record_evidence:
        raise ValueError(f"{SLUG}: partial evidence replay: record_evidence=partial")

    _assert_exact_record_evidence(doc, before_record_evidence, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    doc["evidence"] = [_replacement_for_record_evidence(item) for item in doc["evidence"]]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the saprotrophy_decomposition_cycling graph for issue "
            "#183: added exact snippets to 2 record-level evidence items and "
            "9 decomposition and lignocellulose causal-edge evidence entries, "
            "grounded 6 residual predicates, and preserved the graph as a "
            "nonmechanistic saprotrophy classification. No paid research "
            "service was called."
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
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write changes to data/traits/ecology/saprotrophy.yaml",
    )
    args = parser.parse_args()
    return apply(write=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
