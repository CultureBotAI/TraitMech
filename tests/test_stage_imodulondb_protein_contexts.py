"""Tests for iModulonDB protein-example staging."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from stage_imodulondb_protein_contexts import (
    ImodulonStageError,
    iter_jsonl,
    load_component,
    load_protein_examples,
    main,
    stage_components,
)


def _write_trait(root: Path, *, accession: str = "UniProtKB:P0A6Y8") -> Path:
    path = root / "data" / "traits" / "physiology" / "heat_shock_response.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(
        yaml.safe_dump(
            {
                "identifier": "traitmech:000205",
                "label": "heat shock response",
                "trait_category": "PHYSIOLOGY",
                "causal_graphs": [
                    {
                        "graph_id": "heat_shock_response_proteostasis",
                        "title": "Heat-shock proteostasis restoration",
                        "nodes": [
                            {
                                "node_id": "dnaK",
                                "label": "DnaK",
                                "node_type": "GENE_OR_PROTEIN",
                                "grounding": "InterPro:IPR013126",
                                "protein_examples": [
                                    {
                                        "uniprot_id": accession,
                                        "protein_label": "Chaperone protein DnaK",
                                        "gene_symbol": "dnaK",
                                        "taxon_id": "NCBITaxon:83333",
                                        "taxon_label": "Escherichia coli K-12",
                                        "role": "Heat-shock chaperone.",
                                    }
                                ],
                            }
                        ],
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return path


def _component(**updates):
    row = {
        "organism": "e_coli",
        "dataset": "precise2",
        "k": 42,
        "imodulon": "Heat Shock",
        "imodulon_id": "heat-shock",
        "gene_id": "b0014",
        "gene_locus": "b0014",
        "gene_name": "dnaK",
        "gene_product": "Chaperone protein DnaK",
        "weight": 0.55,
        "in_imodulon": True,
        "cog": "O",
        "all_regulators": "rpoH",
        "string_id": "511145.b0014",
        "uniprot_id": "P0A6Y8",
        "uniprot_protein_name": "Chaperone protein DnaK",
        "uniprot_function": "Molecular chaperone",
    }
    row.update(updates)
    return row


def test_stage_components_joins_existing_trait_protein_examples(tmp_path):
    _write_trait(tmp_path)
    examples = load_protein_examples(tmp_path / "data" / "traits")

    result = stage_components(
        _load(
            _component(),
            _component(gene_id="b9999", uniprot_id=None),
            _component(gene_id="b9998", uniprot_id="BAD"),
            _component(gene_id="b9997", uniprot_id="Q8ZIN0"),
            _component(gene_id="b9996", in_imodulon=False),
        ),
        examples,
    )

    assert len(result.candidates) == 1
    candidate = result.candidates[0]
    assert candidate.uniprot_id == "UniProtKB:P0A6Y8"
    assert candidate.trait_id == "traitmech:000205"
    assert candidate.node_id == "dnaK"
    assert "computational expression-module context" in candidate.evidence_guardrail

    assert [row.block_reason for row in result.blocked] == [
        "INVALID_UNIPROT",
        "NO_TRAIT_PROTEIN_EXAMPLE",
        "NO_UNIPROT",
        "OUTSIDE_IMODULON",
    ]


def test_apply_writes_candidate_blocker_and_summary_reports(tmp_path):
    _write_trait(tmp_path)
    source = tmp_path / "imodulondb.jsonl"
    source.write_text(
        json.dumps(_component()) + "\n" + json.dumps(_component(in_imodulon=False)) + "\n",
        encoding="utf-8",
    )
    report_dir = tmp_path / "reports" / "imodulondb"

    assert main(
        [
            str(source),
            "--traits-dir",
            str(tmp_path / "data" / "traits"),
            "--report-dir",
            str(report_dir),
            "--apply",
        ]
    ) == 0

    assert len((report_dir / "candidates.jsonl").read_text().splitlines()) == 1
    assert "OUTSIDE_IMODULON" in (report_dir / "blocked.tsv").read_text()
    assert "Candidates: 1" in (report_dir / "summary.md").read_text()


def test_malformed_component_rows_fail_closed(tmp_path):
    source = tmp_path / "imodulondb.jsonl"
    source.write_text(json.dumps(_component(weight="not-a-number")) + "\n", encoding="utf-8")

    with pytest.raises(ImodulonStageError, match="weight"):
        list(iter_jsonl(source))


def test_duplicate_candidate_keys_fail_closed(tmp_path):
    _write_trait(tmp_path)
    examples = load_protein_examples(tmp_path / "data" / "traits")

    with pytest.raises(ImodulonStageError, match="duplicate"):
        stage_components(_load(_component(), _component()), examples)


def _load(*rows):
    return [load_component(row, line_no) for line_no, row in enumerate(rows, start=1)]
