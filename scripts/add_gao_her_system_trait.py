#!/usr/bin/env python3
"""Add the Gao-Her system parent genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_system.yaml"
CHILD_TARGETS = {
    REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_duf_system.yaml": {
        "identifier": "traitmech:000361",
        "label": "Gao-Her-DUF system",
        "graph_id": "gao_her_duf_locus_restricts_phage",
        "trait_node_id": "gao_her_duf_system_trait",
        "subsystem": "Gao_Her_DUF",
    },
    REPO_ROOT / "data" / "traits" / "genomics" / "gao_her_sir_system.yaml": {
        "identifier": "traitmech:000362",
        "label": "Gao-Her-SIR system",
        "graph_id": "gao_her_sir_locus_restricts_phage",
        "trait_node_id": "gao_her_sir_system_trait",
        "subsystem": "Gao_Her_SIR",
    },
}

GAO = "DOI:10.1126/science.aba0372"
GAO_PMID = "PMID:32855333"
GAO_CASSETTES_SNIPPET = (
    "By systematic defense gene prediction and heterologous reconstitution, "
    "here we discover 29 widespread antiviral gene cassettes, collectively "
    "present in 32% of all sequenced bacterial and archaeal genomes, that "
    "mediate protection against specific bacteriophages."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T13:51:19Z"
IDENTIFIER = "traitmech:000409"
PARENT_IDENTIFIER = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v286"

ARTICLE_REGISTRY_SNIPPET = (
    "Gao_Her | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes"
)
RULE_ROWS = {
    "Gao_Her_DUF": (
        "Gao_Her\tGao_Her_DUF\t2\t2\tGao_Her_DUF__DUF4297, "
        "Gao_Her_DUF__HerA_DUF"
    ),
    "Gao_Her_SIR": (
        "Gao_Her\tGao_Her_SIR\t2\t2\tGao_Her_SIR__HerA_SIR2, "
        "Gao_Her_SIR__SIR2"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps Gao_Her to the Gao et al. "
            "prokaryotic antiviral-immunity paper."
        ),
    }


def gao_cassette_evidence() -> dict[str, str]:
    return {
        "reference": GAO_PMID,
        "snippet": GAO_CASSETTES_SNIPPET,
        "notes": (
            "Gao et al. support a systematic defense-gene prediction and "
            "heterologous reconstitution campaign that discovered widespread "
            "antiviral gene cassettes."
        ),
    }


def rules_evidence(subsystem: str) -> dict[str, str]:
    components = {
        "Gao_Her_DUF": "Gao_Her_DUF__DUF4297 and Gao_Her_DUF__HerA_DUF",
        "Gao_Her_SIR": "Gao_Her_SIR__HerA_SIR2 and Gao_Her_SIR__SIR2",
    }[subsystem]
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROWS[subsystem],
        "notes": (
            f"The DefenseFinder rules table models {subsystem} as a "
            f"two-profile Gao_Her subsystem requiring {components}."
        ),
    }


def all_rules_evidence() -> list[dict[str, str]]:
    return [rules_evidence("Gao_Her_DUF"), rules_evidence("Gao_Her_SIR")]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Gao-Her system",
    "definition": (
        "A phage defense system in which an organism possesses a Gao_Her "
        "locus represented by DefenseFinder as either a Gao_Her_DUF or "
        "Gao_Her_SIR two-profile subsystem."
    ),
    "definition_source": GAO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_IDENTIFIER],
    "synonyms": [
        {
            "synonym_text": "Gao_Her",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        gao_cassette_evidence(),
        article_registry_evidence(),
        *all_rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gao_her_locus_restricts_phage",
            "title": "Gao-Her loci confer bacterial phage defense",
            "description": (
                "Conservative family-level sketch linking Gao_Her loci to "
                "Gao et al. antiviral cassette defense without asserting the "
                "unresolved Her-DUF or Her-SIR component activities."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Gao-Her as the DefenseFinder Gao_Her "
                "family containing Gao_Her_DUF and Gao_Her_SIR subsystems "
                "while leaving natural hosts, subtype-specific phage triggers, "
                "and DUF4297, HerA_DUF, HerA_SIR2, and SIR2 molecular "
                "functions unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gao_her_locus",
                    "label": "Gao_Her locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Gao_Her phage-defense locus represented "
                        "as a Gao_Her_DUF or Gao_Her_SIR two-profile subsystem."
                    ),
                },
                {
                    "node_id": "gao_2020_antiviral_cassette_defense",
                    "label": "Gao 2020 antiviral cassette defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage protection by one of the antiviral gene "
                        "cassettes described in the Gao et al. systematic "
                        "defense-gene discovery campaign."
                    ),
                },
                {
                    "node_id": "gao_her_system_trait",
                    "label": "Gao-Her system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Gao-Her phage-defense "
                        "system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PARENT_IDENTIFIER,
                    "description": (
                        "Possession of one or more genome-encoded immune systems "
                        "that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "gao_her_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gao_2020_antiviral_cassette_defense",
                    "description": (
                        "DefenseFinder maps Gao_Her to the Gao et al. "
                        "systematic antiphage-system discovery paper and models "
                        "two Gao_Her subsystems, Gao_Her_DUF and Gao_Her_SIR."
                    ),
                    "evidence": [
                        gao_cassette_evidence(),
                        article_registry_evidence(),
                        *all_rules_evidence(),
                    ],
                },
                {
                    "subject": "gao_2020_antiviral_cassette_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "gao_her_system_trait",
                    "description": (
                        "Gao_Her-associated antiviral cassette defense realizes "
                        "the Gao-Her system trait."
                    ),
                    "evidence": [
                        gao_cassette_evidence(),
                    ],
                },
                {
                    "subject": "gao_her_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Gao-Her system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence(), *all_rules_evidence()],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "gao-her-family-mechanism-gap",
            "prompt": (
                "Resolve Gao_Her natural host breadth, subtype boundaries, "
                "phage triggers, and the effector outputs of Gao_Her_DUF and "
                "Gao_Her_SIR before minting narrower Gao-Her mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support bacteriophage protection by widespread "
                "antiviral gene cassettes, and DefenseFinder models Gao_Her_DUF "
                "and Gao_Her_SIR as two-profile subsystems under the Gao_Her "
                "family key. This first parent record captures the Gao_Her "
                "family while leaving subtype-specific triggers, natural host "
                "breadth, and direct effector activities unresolved."
            ),
            "attaches_to": ["causal_graphs#gao_her_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        },
    ],
}


def load_existing_trait(path: Path, expected: dict[str, str]) -> dict[str, Any]:
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise SystemExit(f"{path}: expected mapping")
    for field in ("identifier", "label", "mapping_status"):
        if doc.get(field) != expected[field]:
            raise SystemExit(
                f"{path}: expected {field} {expected[field]!r}, "
                f"found {doc.get(field)!r}"
            )
    if doc.get("parent_traits") != [PARENT_IDENTIFIER]:
        raise SystemExit(
            f"{path}: expected parent_traits [{PARENT_IDENTIFIER!r}], "
            f"found {doc.get('parent_traits')!r}"
        )
    return doc


def target_graph(doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    matches = [
        graph
        for graph in doc.get("causal_graphs") or []
        if graph.get("graph_id") == graph_id
    ]
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one graph {graph_id!r}, found {len(matches)}")
    return matches[0]


def reparent_child(doc: dict[str, Any], expected: dict[str, str]) -> None:
    graph = target_graph(doc, expected["graph_id"])
    node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    if "phage_defense_system" not in node_ids:
        raise SystemExit(f"{expected['graph_id']}: missing phage_defense_system node")
    if "gao_her_system" in node_ids:
        raise SystemExit(f"{expected['graph_id']}: Gao-Her parent node already exists")

    graph["nodes"].append(
        {
            "node_id": "gao_her_system",
            "label": "Gao-Her system",
            "node_type": "TRAIT",
            "grounding": IDENTIFIER,
            "description": "Possession of a genome-encoded Gao-Her phage-defense system.",
        }
    )
    graph["nodes"] = [
        node
        for node in graph["nodes"]
        if node.get("node_id") != "phage_defense_system"
    ]

    subclass_edges = [
        edge
        for edge in graph.get("edges") or []
        if edge.get("subject") == expected["trait_node_id"]
        and edge.get("predicate_id") == "rdfs:subClassOf"
        and edge.get("object") == "phage_defense_system"
    ]
    if len(subclass_edges) != 1:
        raise SystemExit(
            f"{expected['graph_id']}: expected one child-to-phage subclass edge, "
            f"found {len(subclass_edges)}"
        )

    child_edge = subclass_edges[0]
    child_edge["object"] = "gao_her_system"
    child_edge["description"] = (
        f"{expected['label']} possession is a Gao-Her family phage-defense-system "
        "trait."
    )
    child_edge["evidence"] = [rules_evidence(expected["subsystem"])]

    doc["parent_traits"] = [IDENTIFIER]
    record_curation_event(
        doc,
        curator=CURATOR,
        action="EDIT",
        changes=(
            "Reparented the record under traitmech:000409 Gao-Her system and "
            "added a Gao-Her parent node plus subclass edge to the causal graph."
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
            "Minted Gao-Her system as a DOI- and DefenseFinder-backed GENOMICS "
            "TraitRecord under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, history, or "
            f"prior proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
        help="write the Gao-Her parent and reparent the accepted children",
    )
    args = parser.parse_args()

    if not args.apply:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        for target in CHILD_TARGETS:
            print(f"would update {target.relative_to(REPO_ROOT)}")
        return 0

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    write_new_record()
    print(f"wrote {TARGET.relative_to(REPO_ROOT)}")

    for target, expected in CHILD_TARGETS.items():
        doc = load_existing_trait(
            target,
            {**expected, "mapping_status": "PROPOSED"},
        )
        reparent_child(doc, expected)
        write_validated_trait(doc, target)
        print(f"updated {target.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
