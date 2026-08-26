"""Tests for protein/taxon coverage and grounding dispositions."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_graph_protein_taxa import coverage_rows, write_report  # noqa: E402


def _example(**overrides):
    example = {
        "uniprot_id": "UniProtKB:P0A6Y8",
        "protein_label": "DNA gyrase subunit B",
        "gene_symbol": "gyrB",
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli",
        "entry_status": "REVIEWED",
        "retrieved_on": "2026-08-23",
        "entry_version": 180,
        "sequence_version": 1,
        "role": "Example enzyme component.",
        "evidence": [
            {
                "reference": "DOI:10.1000/example",
                "snippet": "The gyrB product was required for the measured activity.",
                "notes": "The source tests this protein in E. coli.",
            }
        ],
    }
    example.update(overrides)
    return example


def _record(*, node=None, graph_updates=None, canonical=None):
    graph = {
        "graph_id": "g",
        "scope_status": "MECHANISTIC",
        "nodes": [
            {"node_id": "trait", "label": "trait", "node_type": "TRAIT"},
            node
            or {
                "node_id": "protein",
                "label": "DNA gyrase B",
                "node_type": "GENE_OR_PROTEIN",
                "grounding": "InterPro:IPR000565",
                "protein_examples": [_example()],
            },
        ],
        "edges": [],
    }
    graph.update(graph_updates or {})
    return {
        "identifier": "traitmech:1",
        "label": "trait",
        "canonical_examples": canonical
        if canonical is not None
        else [
            {
                "taxon_id": "NCBITaxon:562",
                "taxon_label": "Escherichia coli",
                "reference": "DOI:10.1000/example",
            }
        ],
        "causal_graphs": [graph],
    }


def _row(record):
    return coverage_rows([("f.yaml", record)])[0]


def test_complete_mechanistic_graph_passes():
    row = _row(_record())
    assert row["status"] == "PASS"
    assert row["taxon_matched_examples"] == 1
    assert row["unmet_requirements"] == ""


def test_report_uses_a_visible_sentinel_for_no_unmet_requirements(tmp_path):
    report = tmp_path / "coverage.tsv"
    write_report([_row(_record())], report)

    assert report.read_text(encoding="utf-8").splitlines()[-1].endswith("\t-")


def test_missing_minimum_coverage_is_reported_exactly():
    row = _row(
        _record(
            node={"node_id": "chemical", "label": "x", "node_type": "CHEMICAL"},
            canonical=[],
            graph_updates={"scope_status": "REVIEW_NEEDED"},
        )
    )
    requirements = row["unmet_requirements"]
    assert "SCOPE_NOT_REVIEWED" in requirements
    assert "NO_PROTEIN_NODE" in requirements
    assert "NO_CITED_CANONICAL_TAXON" in requirements
    assert "NO_TAXON_MATCHED_PROTEIN_EXAMPLE" in requirements


def test_generic_uniprot_grounding_is_an_error():
    node = {
        "node_id": "protein",
        "label": "protein",
        "node_type": "GENE_OR_PROTEIN",
        "grounding": "UniProtKB:P0A6Y8",
        "protein_examples": [_example()],
    }
    row = _row(_record(node=node))
    assert row["status"] == "ERROR"
    assert "GENERIC_UNIPROT_GROUNDING:protein" in row["unmet_requirements"]


def test_taxon_must_match_a_canonical_example():
    node = {
        "node_id": "protein",
        "label": "protein",
        "node_type": "GENE_OR_PROTEIN",
        "grounding": "GO:0003674",
        "protein_examples": [_example(taxon_id="NCBITaxon:1423")],
    }
    row = _row(_record(node=node))
    assert "PROTEIN_EXAMPLE_TAXON_NOT_CANONICAL" in row["unmet_requirements"]
    assert "NO_TAXON_MATCHED_PROTEIN_EXAMPLE" in row["unmet_requirements"]


def test_protein_example_evidence_requires_all_three_fields():
    node = {
        "node_id": "protein",
        "label": "protein",
        "node_type": "GENE_OR_PROTEIN",
        "grounding": "GO:0003674",
        "protein_examples": [_example(evidence=[{"reference": "DOI:10.1/x"}])],
    }
    row = _row(_record(node=node))
    assert "PROTEIN_EXAMPLE_EVIDENCE_INCOMPLETE" in row["unmet_requirements"]


def test_reviewed_label_only_node_satisfies_grounding_review():
    node = {
        "node_id": "protein",
        "label": "broad protein label",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "The cited source does not identify an exact family.",
        "protein_examples": [_example()],
    }
    row = _row(_record(node=node))
    assert row["status"] == "PASS"
    assert row["reviewed_label_only_nodes"] == 1


def test_nonmechanistic_disposition_exempts_protein_coverage():
    record = _record(
        node={"node_id": "value", "label": "value", "node_type": "QUALITY"},
        canonical=[],
        graph_updates={
            "scope_status": "NONMECHANISTIC",
            "scope_notes": "Numeric measurement bin without a biological mechanism.",
        },
    )
    row = _row(record)
    assert row["status"] == "NONMECHANISTIC"
    assert row["unmet_requirements"] == ""


def test_unreviewed_example_requires_proteome_id():
    node = {
        "node_id": "protein",
        "label": "protein",
        "node_type": "GENE_OR_PROTEIN",
        "grounding": "GO:0003674",
        "protein_examples": [_example(entry_status="UNREVIEWED")],
    }
    row = _row(_record(node=node))
    assert "UNREVIEWED_EXAMPLE_MISSING_PROTEOME" in row["unmet_requirements"]


def test_gene_or_operon_primary_node_does_not_satisfy_protein_coverage():
    node = {
        "node_id": "ars_operon",
        "label": "ars operon",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Legacy genetic context.",
    }
    row = _row(_record(node=node))

    assert row["protein_nodes"] == 0
    assert "GENE_OR_OPERON_PRIMARY_NODE:ars_operon" in row["unmet_requirements"]
    assert "NO_PROTEIN_NODE" in row["unmet_requirements"]


def test_nonprotein_legacy_node_does_not_satisfy_protein_coverage():
    node = {
        "node_id": "crrna",
        "label": "crRNA",
        "node_type": "GENE_OR_PROTEIN",
    }
    row = _row(_record(node=node))

    assert row["protein_nodes"] == 0
    assert "GENE_OR_OPERON_PRIMARY_NODE:crrna" in row["unmet_requirements"]
    assert "NO_PROTEIN_NODE" in row["unmet_requirements"]


def test_real_corpus_has_one_row_per_graph():
    rows = coverage_rows()
    assert len(rows) == 353
    assert not any("GENERIC_UNIPROT_GROUNDING" in row["unmet_requirements"] for row in rows)
