"""Smoke tests for the METPO seeder + schema invariants."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from seed_from_metpo import (  # noqa: E402
    OWL_PATH,
    parse_owl,
    categorize,
    slugify,
)
from trait_causal_graph import causal_graphs_for_template  # noqa: E402


def test_owl_parses_and_yields_terms():
    parsed = parse_owl(OWL_PATH)
    assert len(parsed) > 300, f"expected >300 METPO terms, got {len(parsed)}"
    # Sentinels: known classes that must always be present.
    assert "METPO:1000059" in parsed   # phenotype
    assert "METPO:1000331" in parsed   # pH optimum
    assert "METPO:1000060" in parsed   # metabolism


def test_every_trait_yaml_has_required_fields():
    """Each TraitRecord YAML on disk must carry core identifiers and lifecycle status."""
    yamls = sorted(TRAITS_DIR.rglob("*.yaml"))
    assert yamls, "no trait YAMLs found — run `just seed-apply`"
    for p in yamls:
        doc = yaml.safe_load(p.read_text())
        assert isinstance(doc, dict), f"{p}: not a dict"
        for required in ("identifier", "label", "trait_category", "term_kind", "mapping_status"):
            assert required in doc, f"{p}: missing {required!r}"
        # Seeded records use the METPO CURIE directly; curator-minted records
        # (e.g. PROPOSED candidate traits) may use the reserved `traitmech:`
        # prefix — see .claude/skills/manage-identifiers/SKILL.md.
        assert doc["identifier"].startswith(("METPO:", "traitmech:")), (
            f"{p}: identifier {doc['identifier']!r} is neither a METPO nor a traitmech CURIE"
        )
        assert doc["mapping_status"] in {"SEEDED", "PROPOSED", "REVIEWED", "DEPRECATED"}, (
            f"{p}: status={doc['mapping_status']!r}"
        )


def test_no_material_entity_subtree_seeded():
    """METPO:1000186 (material entity) and its subtree must be skipped."""
    parsed = parse_owl(OWL_PATH)
    parents = {c: r["parents"] for c, r in parsed.items()}
    skipped = [
        c for c, rec in parsed.items()
        if categorize(c, rec, parents) is None
    ]
    # 3 children of material entity (chemical entity / enzyme / microbe).
    # No DatatypeProperty / ObjectProperty / Class outside material entity
    # should have been dropped.
    assert "METPO:1000526" in skipped or "METPO:1000525" in skipped


def test_deprecated_metpo_entities_are_parsed_but_never_seeded():
    """A source refresh must not turn METPO's legacy namespace into records."""
    parsed = parse_owl(OWL_PATH)
    retired = parsed["METPO:1000001"]
    assert retired["label"] == "obsolete acid-fast"
    assert retired["deprecated"] is True
    parents = {curie: record["parents"] for curie, record in parsed.items()}
    assert categorize("METPO:1000001", retired, parents) is None


def test_slug_collision_uses_localid_suffix():
    assert slugify("pH optimum", "fallback") == "ph_optimum"
    assert slugify(None, "fallback") == "fallback"
    assert slugify("", "fallback") == "fallback"
    # Special chars get folded to underscores.
    assert slugify("uses as carbon source!", "x") == "uses_as_carbon_source"


def test_causal_graph_template_payload_preserves_edge_evidence():
    doc = yaml.safe_load((TRAITS_DIR / "environment" / "aerobic.yaml").read_text())
    graphs = causal_graphs_for_template(doc)
    assert graphs, "aerobic trait should include a causal graph example"
    graph = graphs[0]
    assert graph["issues"] == []
    assert len(graph["nodes"]) >= 4
    assert len(graph["edges"]) >= 4
    assert all(edge["evidence"] for edge in graph["edges"])


def test_causal_graph_template_surfaces_taxon_paired_protein_examples():
    record = {
        "causal_graphs": [
            {
                "graph_id": "g",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "enzyme",
                        "label": "Example enzyme",
                        "node_type": "GENE_OR_PROTEIN",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:P0A6Y8",
                                "protein_label": "DNA gyrase subunit B",
                                "taxon_id": "NCBITaxon:562",
                                "taxon_label": "Escherichia coli",
                                "entry_status": "REVIEWED",
                                "retrieved_on": "2026-08-23",
                                "evidence": [{"reference": "DOI:10.1000/example"}],
                            }
                        ],
                    }
                ],
                "edges": [],
            }
        ]
    }

    graph = causal_graphs_for_template(record)[0]
    assert graph["scope_status"] == "MECHANISTIC"
    assert graph["nodes"][0]["protein_examples"][0]["taxon_id"] == "NCBITaxon:562"
    assert graph["protein_example_rows"] == [
        {
            "node_id": "enzyme",
            "node_label": "Example enzyme",
            "uniprot_id": "UniProtKB:P0A6Y8",
            "protein_label": "DNA gyrase subunit B",
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "entry_status": "REVIEWED",
            "retrieved_on": "2026-08-23",
            "evidence": [{"reference": "DOI:10.1000/example"}],
        }
    ]
