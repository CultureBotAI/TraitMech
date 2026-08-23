"""Unit tests for taxon-aware UniProt exemplar verification."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_uniprot_grounding import audit_uses, iter_uses  # noqa: E402


def _node(example=None, grounding=None):
    node = {
        "node_id": "p",
        "label": "Protein",
        "node_type": "GENE_OR_PROTEIN",
    }
    if grounding:
        node["grounding"] = grounding
    if example:
        node["protein_examples"] = [example]
    return node


def _example(**updates):
    value = {
        "uniprot_id": "UniProtKB:P0A6Y8",
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli",
        "entry_status": "REVIEWED",
        "entry_version": 180,
        "sequence_version": 1,
    }
    value.update(updates)
    return value


def _resolved(**updates):
    value = {
        "status": "reviewed",
        "entry_status": "REVIEWED",
        "primary_accession": "P0A6Y8",
        "uniprot_name": "DNA gyrase subunit B",
        "gene_symbol": "gyrB",
        "organism": "Escherichia coli",
        "taxon_id": "562",
        "entry_version": 180,
        "sequence_version": 1,
        "proteome_ids": "UP000000625",
    }
    value.update(updates)
    return value


def _audit(node, response=None):
    uses = iter_uses([(Path("f.yaml"), "g", node)])
    rows = audit_uses(uses, delay=0, resolver=lambda _acc, _delay: response or _resolved())
    return rows[0]


def test_matching_protein_example_is_clean():
    row = _audit(_node(_example()))
    assert row["finding"] == ""
    assert row["taxon_match"] == "YES"
    assert row["entry_version_match"] == "YES"


def test_taxon_and_version_drift_are_findings():
    row = _audit(
        _node(_example()),
        _resolved(taxon_id="1423", entry_version=181, sequence_version=2),
    )
    assert row["finding"].split("|") == [
        "TAXON_MISMATCH",
        "ENTRY_VERSION_MISMATCH",
        "SEQUENCE_VERSION_MISMATCH",
    ]


def test_secondary_accession_is_rejected():
    row = _audit(_node(_example()), _resolved(primary_accession="P0A6Y9"))
    assert "NOT_PRIMARY_ACCESSION" in row["finding"]


def test_generic_uniprot_grounding_is_always_a_finding():
    row = _audit(_node(grounding="UniProtKB:P0A6Y8"))
    assert row["usage"] == "GENERIC_GROUNDING"
    assert "GENERIC_UNIPROT_GROUNDING" in row["finding"]


def test_resolver_called_once_for_reused_accession():
    nodes = [
        (Path("a.yaml"), "g1", _node(_example())),
        (Path("b.yaml"), "g2", _node(_example())),
    ]
    calls = []

    def resolver(accession, delay):
        calls.append((accession, delay))
        return _resolved()

    rows = audit_uses(iter_uses(nodes), delay=0, resolver=resolver)
    assert calls == [("P0A6Y8", 0)]
    assert [row["reused_in_n_files"] for row in rows] == [2, 2]
