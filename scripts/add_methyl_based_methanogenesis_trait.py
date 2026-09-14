#!/usr/bin/env python3
"""Add methyl-based methanogenesis and ground its methanogenesis branch."""
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

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "methyl_based_methanogenesis.yaml"
METHANOGENESIS = REPO_ROOT / "data" / "traits" / "metabolism" / "methanogenesis.yaml"
DE_MESQUITA = "DOI:10.1128/mmbr.00024-22"
EVANS = "DOI:10.3389/fmicb.2017.01198"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T21:27:00Z"

RECORD = {
    "identifier": "traitmech:000192",
    "label": "methyl-based methanogenesis",
    "definition": (
        "A methanogenesis in which methylated compounds donate methyl groups "
        "that are transferred to coenzyme M and reduced to methane."
    ),
    "definition_source": DE_MESQUITA,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000844"],
    "synonyms": [
        {
            "synonym_text": "methylotrophic methanogenesis",
            "synonym_type": "RELATED_SYNONYM",
            "source": EVANS,
        },
        {
            "synonym_text": "methanogenesis using methylated compounds",
            "synonym_type": "RELATED_SYNONYM",
            "source": EVANS,
        },
    ],
    "evidence": [
        {
            "reference": DE_MESQUITA,
            "snippet": (
                "Methyl-based methanogenesis is one of three broad categories "
                "of archaeal anaerobic methanogenesis, including both the "
                "methyl dismutation (methylotrophic) pathway and the "
                "methyl-reducing (also known as hydrogen-dependent "
                "methylotrophic) pathway"
            ),
            "notes": (
                "Bueno de Mesquita et al. define methyl-based methanogenesis "
                "as the methanogenesis branch covering methyl dismutation and "
                "hydrogen-dependent methyl-reducing pathways."
            ),
        },
        {
            "reference": EVANS,
            "snippet": (
                "acetoclastic methanogenesis using acetate, and methylotrophic "
                "methanogenesis using methylated compounds, such as methanol, "
                "methylamines"
            ),
            "notes": (
                "Evans et al. describe methylotrophic methanogenesis as the "
                "methylated-compound-using branch among major methanogenic "
                "carbon-source pathways."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "methyl-based-methanogenesis-xref-gap",
            "prompt": (
                "Resolve an exact external ontology xref for methyl-substrate "
                "methanogenesis before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only obsolete METPO:1000866 "
                "Methylotrophic methanogenesis. The existing methylotrophic "
                "record is the broader reduced-one-carbon trophic type, and "
                "GO:0015948 methane biosynthetic process is exact only for "
                "the broader methanogenesis parent, so no exact active "
                "external class has yet been resolved for this methyl-substrate "
                "branch."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
        },
    ],
}


def ground_methanogenesis_branch(record: dict) -> None:
    if record.get("identifier") != "METPO:1000844":
        raise ValueError(f"expected METPO:1000844, got {record.get('identifier')!r}")
    if record.get("label") != "Methanogenesis":
        raise ValueError(f"expected Methanogenesis, got {record.get('label')!r}")
    if record.get("mapping_status") != "REVIEWED":
        raise ValueError(f"expected REVIEWED, got {record.get('mapping_status')!r}")
    if record.get("parent_traits") != ["METPO:1000060"]:
        raise ValueError(f"unexpected parents: {record.get('parent_traits')!r}")

    graphs = [
        graph
        for graph in record.get("causal_graphs") or []
        if graph.get("graph_id") == "methanogenesis_c1_reduction"
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected one methanogenesis graph, got {len(graphs)}")

    graph = graphs[0]
    nodes = [
        node
        for node in graph.get("nodes") or []
        if node.get("node_id") == "methyl_based_methanogenesis"
    ]
    if len(nodes) != 1:
        raise ValueError(f"expected one methyl-based node, got {len(nodes)}")

    node = nodes[0]
    expected = {
        "node_id": "methyl_based_methanogenesis",
        "label": "methyl-based methanogenesis",
        "node_type": "PATHWAY",
        "description": "Methanogenic pathway using methylated compounds as substrate.",
    }
    if node != expected:
        raise ValueError(f"unexpected methyl-based node preimage: {node!r}")

    node.clear()
    node.update(
        {
            "node_id": "methyl_based_methanogenesis",
            "label": "methyl-based methanogenesis",
            "node_type": "TRAIT",
            "grounding": "traitmech:000192",
            "description": "Methyl-substrate methanogenesis branch.",
        }
    )

    for graph_edge in graph.get("edges") or []:
        if (
            graph_edge.get("subject") == "methyl_based_methanogenesis"
            and graph_edge.get("predicate") == "part of"
            and graph_edge.get("object") == "methanogenesis_trait"
        ):
            if (
                graph_edge.get("description")
                != "Methylotrophic methanogenesis is a methyl-substrate branch."
            ):
                raise ValueError(
                    "unexpected methyl-based part-of edge preimage: "
                    f"{graph_edge!r}"
                )
            graph_edge["description"] = (
                "Methyl-based methanogenesis is a methyl-substrate branch."
            )
            break
    else:
        raise ValueError("expected methyl-based methanogenesis part-of edge")

    record_curation_event(
        record,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE",
        changes=(
            "Grounded the methyl-based methanogenesis causal node to "
            "traitmech:000192 after minting the same-scope methyl-substrate "
            "methanogenesis TraitRecord."
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
            "Minted methyl-based methanogenesis as a DOI-backed child of "
            "methanogenesis after a repository-wide duplicate review covering "
            "ignored and hidden files; the pinned METPO snapshot has only an "
            "obsolete Methylotrophic methanogenesis class."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    methanogenesis = yaml.safe_load(METHANOGENESIS.read_text(encoding="utf-8"))
    ground_methanogenesis_branch(methanogenesis)

    write_record(TARGET, record, args.apply)
    write_record(METHANOGENESIS, methanogenesis, args.apply)

    mode = "wrote" if args.apply else "would write"
    print(f"{mode} {TARGET.relative_to(REPO_ROOT)}")
    print(f"{mode} {METHANOGENESIS.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
