#!/usr/bin/env python3
"""Repair PR #664 evidence after adversarial review.

The connector and review migrations in the dirty issue-183 batch are deliberately
strict once a record has migrated: they assert that each generated edge matches
its source script constant exactly. This follow-up repair updates the migrated
records from those corrected constants, then leaves one curation event per
record that ties the data refresh to the PR review issues.

Usage:
    python scripts/repair_pr664_adversarial_review.py
    python scripts/repair_pr664_adversarial_review.py --apply
"""

from __future__ import annotations

import argparse
import copy
import importlib
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

ACTION = "ADVERSARIAL_REVIEW_REPAIR"
TIMESTAMP = "2026-09-06T17:10:00Z"
FOLLOWUP_TIMESTAMP = "2026-09-07T02:20:00Z"
FINAL_FOLLOWUP_TIMESTAMP = "2026-09-07T03:40:00Z"
SNIPPET_FOLLOWUP_TIMESTAMP = "2026-09-07T04:24:00Z"
PRIMARY_SNIPPET_TIMESTAMP = "2026-09-07T06:14:00Z"
STRUCTURE_FOLLOWUP_TIMESTAMP = "2026-09-07T07:24:00Z"

CONNECTOR_MODULES = [
    "connect_cell_length_large_graph_183",
    "connect_gc_low_graph_183",
    "connect_mesophilic_graph_183",
    "connect_nacl_optimum_graph_183",
    "connect_ph_delta_mid2_graph_183",
    "connect_ph_delta_mid3_graph_183",
    "connect_ph_delta_very_low_graph_183",
    "connect_ph_phenotype_graph_183",
    "connect_soil_dwelling_graph_183",
    "connect_temperature_delta_high_graph_183",
    "connect_temperature_delta_very_low_graph_183",
    "connect_temperature_optimum_high_graph_183",
    "connect_temperature_optimum_very_low_graph_183",
    "connect_temperature_range_mid3_graph_183",
    "connect_temperature_range_mid4_graph_183",
    "connect_temperature_range_very_low_graph_183",
]

EDGE_REVIEW_MODULES = [
    "review_genomic_island_graph_183",
    "review_gram_stain_graph_183",
    "review_nacl_range_low_graph_183",
    "review_obligately_piezophilic_graph_183",
    "review_ph_delta_mid2_graph_183",
    "review_ph_delta_mid3_graph_183",
    "review_ph_delta_very_low_graph_183",
    "review_ph_phenotype_graph_183",
    "review_ph_range_mid2_graph_183",
    "review_oxidative_stress_response_graph_183",
    "review_ring_shaped_graph_183",
    "review_saprotrophy_graph_183",
    "review_soil_dwelling_graph_183",
    "review_temperature_range_mid3_graph_183",
    "review_temperature_range_mid4_graph_183",
    "review_temperature_range_very_low_graph_183",
]

GRAPH_REVIEW_MODULES = [
    "review_biosafety_level_5_graph_183",
]

FOLLOWUP_SLUGS = {
    "ecology/biosafety_level_5",
    "environment/obligately_piezophilic",
    "environment/ph_phenotype_with_numerical_limits",
    "environment/temperature_delta_very_low",
    "genomics/genomic_island",
    "morphology/gram_stain",
    "physiology/oxidative_stress_response",
}

FINAL_FOLLOWUP_SLUGS = {
    "environment/ph_delta_mid3",
    "genomics/genomic_island",
}

SNIPPET_FOLLOWUP_SLUGS = {
    "ecology/soil_dwelling",
    "ecology/saprotrophy",
    "environment/ph_delta_mid3",
    "environment/ph_phenotype_with_numerical_limits",
    "environment/ph_range_mid2",
    "environment/temperature_range_mid4",
    "morphology/cell_length_large",
    "morphology/ring_shaped",
}

PRIMARY_SNIPPET_SLUGS = {
    "environment/ph_delta_mid2",
    "environment/ph_delta_mid3",
    "environment/ph_delta_very_low",
    "environment/ph_phenotype_with_numerical_limits",
    "environment/temperature_range_mid4",
}

STRUCTURE_FOLLOWUP_SLUGS = {
    "ecology/biosafety_level_5",
    "environment/ph_range_mid2",
    "environment/temperature_delta_high",
    "environment/temperature_range_mid3",
}

CANONICAL_EVENT_CHANGES: dict[str, list[dict[str, str]]] = {
    "ecology/biosafety_level_5": [
        {
            "action": "REVIEW_CAUSAL_EVIDENCE",
            "timestamp": "2026-09-04T10:00:00Z",
            "changes": (
                "Reviewed the biosafety_level_5_proposed_enhanced_hazard graph "
                "for issue #183: kept the generic proposed enhanced-hazard "
                "BSL-5 graph grounded in the pathogen-hazard definition DOI, "
                "added DOI-backed historical PPL-alpha name-use evidence from "
                "the Cohen 2002 SAE paper, added exact snippets to record and "
                "edge evidence, and kept BSL-5 scoped as an explicitly "
                "hypothetical nonmechanistic containment proposal. No paid "
                "research service was called."
            ),
        },
    ],
    "environment/temperature_range_mid3": [
        {
            "action": "CONNECT_CAUSAL_GRAPH_COMPONENTS",
            "timestamp": "2026-09-04T22:00:00Z",
            "changes": (
                "Resolved issue #183 graph fragmentation (5 components to 1) by "
                "adding 4 source- and verbatim-snippet-backed association "
                "connectors among DesK/DesR membrane-order sensing, des "
                "expression, cooling-induced membrane rigidification, and "
                "homeoviscous liquid-crystalline membrane branches. No paid "
                "research service was called."
            ),
        },
    ],
}


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(slug: str, doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{slug}: expected exactly one graph, found {len(graphs)}")
    return graphs[0]


def _replace_edges(
    slug: str,
    doc: dict[str, Any],
    replacements: list[dict[str, Any]],
) -> None:
    graph = _find_graph(slug, doc)
    by_key = {_edge_key(edge): edge for edge in replacements}
    seen: set[tuple[str | None, str | None, str | None]] = set()

    replaced_edges = []
    for edge in graph.get("edges") or []:
        key = _edge_key(edge)
        if key in by_key:
            seen.add(key)
            replaced_edges.append(copy.deepcopy(by_key[key]))
        else:
            replaced_edges.append(edge)

    missing = set(by_key) - seen
    if missing:
        raise ValueError(f"{slug}: missing replacement edge(s): {sorted(missing)}")

    graph["edges"] = replaced_edges


def _replace_record_evidence(
    slug: str,
    doc: dict[str, Any],
    replacements: list[dict[str, Any]],
) -> None:
    by_reference = {item["reference"]: item for item in replacements}
    seen: set[str] = set()

    replaced_evidence = []
    for item in doc.get("evidence") or []:
        reference = item.get("reference")
        if reference in by_reference:
            if reference in seen:
                raise ValueError(f"{slug}: duplicate record evidence: {reference}")
            seen.add(reference)
            replaced_evidence.append(copy.deepcopy(by_reference[reference]))
        else:
            replaced_evidence.append(item)

    missing = set(by_reference) - seen
    if missing:
        raise ValueError(f"{slug}: missing replacement record evidence: {sorted(missing)}")

    doc["evidence"] = replaced_evidence


def _drop_stale_nodes(slug: str, doc: dict[str, Any], node_ids: set[str]) -> None:
    if not node_ids:
        return

    graph = _find_graph(slug, doc)
    graph["nodes"] = [
        node for node in graph.get("nodes") or [] if node.get("node_id") not in node_ids
    ]


def _drop_stale_edges(
    slug: str,
    doc: dict[str, Any],
    edge_keys: set[tuple[str, str, str]],
) -> None:
    if not edge_keys:
        return

    graph = _find_graph(slug, doc)
    graph["edges"] = [edge for edge in graph.get("edges") or [] if _edge_key(edge) not in edge_keys]


def _add_repair_edges(slug: str, doc: dict[str, Any], edges: list[dict[str, Any]]) -> None:
    if not edges:
        return

    graph = _find_graph(slug, doc)
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    for edge in edges:
        key = _edge_key(edge)
        existing = existing_by_key.get(key)
        if existing == edge:
            continue
        if existing is not None:
            raise ValueError(f"{slug}: repair edge drifted: {key}")
        graph.setdefault("edges", []).append(copy.deepcopy(edge))


def _connector_edges(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, module.ADDED_EDGES


def _cell_length_large_edges(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, [
        *[replacement["after"] for replacement in module.EDGE_REPLACEMENTS],
        *module.ADDITIONS,
    ]


def _review_edges(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    repair_addition_keys = {
        _edge_key(edge) for edge in getattr(module, "REPAIR_EDGE_ADDITIONS", [])
    }
    return module.SLUG, [
        *[
            edge
            for edge in [replacement["after"] for replacement in module.EDGE_REPLACEMENTS]
            if _edge_key(edge) not in repair_addition_keys
        ],
        *[
            edge
            for edge in getattr(module, "EDGE_ADDITIONS", [])
            if _edge_key(edge) not in repair_addition_keys
        ],
    ]


def _graph(module_name: str) -> tuple[str, list[dict[str, Any]]]:
    module = importlib.import_module(module_name)
    return module.SLUG, [module.AFTER_GRAPH]


def _path_for_slug(slug: str) -> Path:
    return REPO_ROOT / "data" / "traits" / f"{slug}.yaml"


def _event_changes(slug: str) -> str:
    if slug == "ecology/biosafety_level_5":
        return (
            "Addressed PR #664 adversarial review issue #694: upserted the "
            "original issue-183 review event so BSL-5 provenance describes the "
            "generic two-edge enhanced-hazard graph that shipped."
        )
    if slug == "environment/ph_range_mid2":
        return (
            "Addressed PR #664 adversarial review issue #692: normalized the "
            "Poolman PMF snippet to quote the source's uppercase membrane "
            "potential symbol."
        )
    if slug == "environment/temperature_delta_high":
        return (
            "Addressed PR #664 adversarial review issue #692: requoted the Wu "
            "et al. trans-UFA connector snippet without the markup-flattening "
            "space before the hyphen."
        )
    if slug == "environment/temperature_range_mid3":
        return (
            "Addressed PR #664 adversarial review issue #693: replaced weak "
            "DesK/DesR connector edges by routing DesK directly to "
            "phosphorylated DesR, removed the redundant unphosphorylated DesR "
            "node, and updated the original connector history."
        )
    if slug in {
        "environment/ph_delta_mid2",
        "environment/ph_delta_very_low",
    }:
        return (
            "Addressed PR #664 adversarial review issues #688 and #689: "
            "requoted the F1Fo-ATPase acid-stress edge with a longer Krulwich "
            "span and replaced its connector quote with distinct Sekiya "
            "F-ATPase acid-tolerance support."
        )
    if slug == "environment/ph_delta_mid3":
        return (
            "Addressed PR #664 adversarial review issues #688 and #690: "
            "restored a supporting Krulwich snippet on the pH-delta bin "
            "membership edge and requoted the Poolman phosphate-buffering edge "
            "from the primary source text."
        )
    if slug == "environment/ph_phenotype_with_numerical_limits":
        return (
            "Addressed PR #664 adversarial review issues #688, #689, and "
            "#690: restored record-level Krulwich pH-axis support, replaced "
            "cross-trait Poolman antiporter and phosphate-buffering fragments "
            "with primary-source spans, and made the PMF connector snippet "
            "distinct."
        )
    if slug == "environment/temperature_range_mid4":
        return (
            "Addressed PR #664 adversarial review issue #689: expanded the "
            "Hoogerland FabI/FabB branch quote and replaced the warm-mesophile "
            "connector quote with an independent homeoviscous-adaptation span."
        )
    if slug in {
        "environment/ph_delta_mid3",
        "environment/ph_phenotype_with_numerical_limits",
        "environment/ph_range_mid2",
    }:
        return (
            "Addressed PR #664 adversarial review issue #685: replaced weak pH "
            "edge snippets with exact source spans that carry their edge claims, "
            "and left derived pH-axis bin membership in notes instead of fragment "
            "snippets."
        )
    if slug in {
        "ecology/saprotrophy",
        "ecology/soil_dwelling",
        "environment/temperature_range_mid4",
        "morphology/ring_shaped",
    }:
        return (
            "Addressed PR #664 adversarial review issue #686: replaced "
            "fragmented ring-shape, soil-life-history, heat-shock, and "
            "ligninolysis snippets with exact source spans that carry their edge "
            "claims."
        )
    if slug == "morphology/cell_length_large":
        return (
            "Addressed PR #664 adversarial review issue #687: gave the two SulA "
            "edges distinct exact snippets, separating the FtsZ-polymerization "
            "claim from the SulA division-inhibitor connector."
        )
    if slug == "ecology/biosafety_level_5":
        return (
            "Addressed PR #664 adversarial review issue #679: moved the PPL-alpha "
            "historical naming support to DOI-backed record-level evidence and "
            "removed the ungrounded lexical naming edge from the BSL-5 graph."
        )
    if slug == "environment/nacl_range_low":
        return (
            "Addressed PR #664 adversarial review: replaced the unsupported "
            "compatible-solute bridge snippet with exact Bhowmick et al. wording "
            "that normalizes the K+ superscript and names both cation and "
            "compatible-solute accumulation after an external osmotic upshift."
        )
    if slug == "environment/obligately_piezophilic":
        return (
            "Addressed PR #664 adversarial review issue #680: replaced the "
            "subjectless HHP lipid-packing connector snippet with exact Tamby "
            "et al. wording that names unsaturation and branching as membrane "
            "adaptations to HHP and extreme temperature."
        )
    if slug == "environment/ph_delta_mid3":
        return (
            "Addressed PR #664 adversarial review issue #683: normalized the "
            "Poolman F0F1-ATPase evidence snippet by removing MathML brace "
            "markup so the snippet matches the source text."
        )
    if slug == "environment/ph_phenotype_with_numerical_limits":
        return (
            "Addressed PR #664 adversarial review issue #682: replaced the "
            "short Poolman PMF snippet nested inside another connector snippet "
            "with exact near-neutral cytoplasmic-pH wording."
        )
    if slug == "environment/temperature_delta_high":
        return (
            "Addressed PR #664 adversarial review: requoted the de Mendoza "
            "membrane-fluidity adaptation evidence with the exact "
            "homeoviscous spelling from the cited source."
        )
    if slug == "environment/temperature_optimum_very_low":
        return (
            "Addressed PR #664 adversarial review: corrected the Phadtare and "
            "Severinov cold-shock connector note so it names the DOI-matched "
            "source instead of the Hamdan psychrophile review."
        )
    if slug == "environment/temperature_range_very_low":
        return (
            "Addressed PR #664 adversarial review: replaced copied Ramasamy "
            "cold-adaptation snippets with independent exact text supporting "
            "compatible-osmolyte and ice-binding-protein context edges."
        )
    if slug == "morphology/cell_length_large":
        return (
            "Addressed PR #664 adversarial review: corrected the SulA "
            "cell-division-inhibitor snippet to match the exact peer-reviewed "
            "Wiley text with comma punctuation."
        )
    if slug == "genomics/gc_low":
        return (
            "Addressed PR #664 adversarial review: replaced the copied GC-low "
            "connector snippet with exact Ruis et al. wording defining a "
            "mutational spectrum as combined context-dependent substitution "
            "signatures."
        )
    if slug == "environment/temperature_delta_very_low":
        return (
            "Addressed PR #664 adversarial review issues #678 and #681: removed "
            "the unsupported membrane phase-transition temperature branch, "
            "requoted the cold RNA connector with exact Phadtare and Inouye "
            "wording, and replaced generic Springer endpoint notes with the "
            "specific Siliakus et al. full-text endpoint."
        )
    if slug == "genomics/genomic_island":
        return (
            "Addressed PR #664 adversarial review issue #684: added a "
            "Bioteau-backed ICE subclass edge to reconnect the "
            "ICE/IME/T4SS/conjugation branch to the genomic island trait."
        )
    if slug == "morphology/gram_stain":
        return (
            "Addressed PR #664 adversarial review issue #682: replaced nested "
            "Popescu and Doyle dye-retention snippets with distinct exact "
            "cell-wall and dye-retention wording."
        )
    if slug == "physiology/oxidative_stress_response":
        return (
            "Addressed PR #664 adversarial review issues #680 through #682: "
            "requoted the RpoS edge and Imlay record evidence, and replaced the "
            "generic ASM endpoint note with Europe PMC abstract verification."
        )
    return (
        "Addressed PR #664 adversarial review: replaced copied "
        "nonmechanistic bridge snippets with independent exact source snippets "
        "while preserving the existing connector edge scope."
    )


def _event_timestamp(slug: str) -> str:
    if slug in STRUCTURE_FOLLOWUP_SLUGS:
        return STRUCTURE_FOLLOWUP_TIMESTAMP
    if slug in PRIMARY_SNIPPET_SLUGS:
        return PRIMARY_SNIPPET_TIMESTAMP
    if slug in SNIPPET_FOLLOWUP_SLUGS:
        return SNIPPET_FOLLOWUP_TIMESTAMP
    if slug in FINAL_FOLLOWUP_SLUGS:
        return FINAL_FOLLOWUP_TIMESTAMP
    if slug in FOLLOWUP_SLUGS:
        return FOLLOWUP_TIMESTAMP
    return TIMESTAMP


def _write_or_validate(path: Path, doc: dict[str, Any], write: bool) -> None:
    if write:
        write_validated_trait(doc, path)
        return
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(doc, Path(tmp) / path.name)


def repair(write: bool = False) -> int:
    changed: list[Path] = []
    graph_modules = {module: _graph for module in GRAPH_REVIEW_MODULES}
    edge_modules = {
        **{
            module: (
                _cell_length_large_edges
                if module == "connect_cell_length_large_graph_183"
                else _connector_edges
            )
            for module in CONNECTOR_MODULES
        },
        **{module: _review_edges for module in EDGE_REVIEW_MODULES},
    }

    for module_name, loader in {**edge_modules, **graph_modules}.items():
        slug, replacements = loader(module_name)
        path = _path_for_slug(slug)
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        before = copy.deepcopy(doc)

        if module_name in graph_modules:
            doc["causal_graphs"] = copy.deepcopy(replacements)
            module = importlib.import_module(module_name)
            if hasattr(module, "AFTER_DEFINITION_SOURCE"):
                doc["definition_source"] = module.AFTER_DEFINITION_SOURCE
            if hasattr(module, "AFTER_RECORD_EVIDENCE"):
                doc["evidence"] = copy.deepcopy(module.AFTER_RECORD_EVIDENCE)
        else:
            _replace_edges(slug, doc, replacements)
            module = importlib.import_module(module_name)
            if hasattr(module, "RECORD_EVIDENCE_REPLACEMENTS"):
                _replace_record_evidence(
                    slug,
                    doc,
                    [replacement["after"] for replacement in module.RECORD_EVIDENCE_REPLACEMENTS],
                )
            elif hasattr(module, "RECORD_EVIDENCE_AFTER"):
                doc["evidence"] = copy.deepcopy(module.RECORD_EVIDENCE_AFTER)
            _drop_stale_edges(slug, doc, getattr(module, "STALE_EDGE_KEYS", set()))
            _drop_stale_nodes(slug, doc, getattr(module, "STALE_NODE_IDS", set()))
            _add_repair_edges(slug, doc, getattr(module, "REPAIR_EDGE_ADDITIONS", []))

        record_curation_event(
            doc,
            curator="codex",
            action=ACTION,
            changes=_event_changes(slug),
            llm_assisted=True,
            timestamp=_event_timestamp(slug),
            upsert=True,
        )
        for event in CANONICAL_EVENT_CHANGES.get(slug, []):
            record_curation_event(
                doc,
                curator="codex",
                action=event["action"],
                changes=event["changes"],
                llm_assisted=True,
                timestamp=event["timestamp"],
                upsert=True,
            )

        if doc == before:
            continue

        _write_or_validate(path, doc, write)
        changed.append(path)

    changed = list(dict.fromkeys(changed))
    for path in changed:
        print(f"  repair {path.relative_to(REPO_ROOT)}")
    print(f"{'applied' if write else 'dry run'}: repaired {len(changed)} record(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return repair(write=parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
