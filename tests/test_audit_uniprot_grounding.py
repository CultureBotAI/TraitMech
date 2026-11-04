"""Unit tests for taxon-aware UniProt exemplar verification."""

from __future__ import annotations

import csv
import sys
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_uniprot_grounding import (  # noqa: E402
    FIELDS,
    audit_uses,
    check_inventory,
    fetch,
    iter_nodes,
    iter_uses,
    write_report,
)


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


def test_rest_transport_failure_stays_failed_in_report(monkeypatch, tmp_path):
    def unavailable(url, timeout):
        assert url == "https://rest.uniprot.org/uniprotkb/P0A6Y8.json"
        raise urllib.error.HTTPError(url, 503, "Service Unavailable", {}, None)

    monkeypatch.setattr("audit_uniprot_grounding.urllib.request.urlopen", unavailable)
    uses = iter_uses([(Path("f.yaml"), "g", _node(_example()))])
    rows = audit_uses(uses, delay=0)
    report = tmp_path / "report.tsv"
    write_report(rows, report)
    with report.open(newline="") as handle:
        row, = csv.DictReader(handle, delimiter="\t")
    assert row["status"] == "error"
    assert row["uniprot_name"] == "HTTP 503"
    assert "UNIPROT_ERROR" in row["finding"].split("|")
    assert row["primary_accession"] == ""
    assert row["primary_accession_match"] != "YES"
    assert row["taxon_match"] != "YES"
    assert row["entry_version_match"] != "YES"


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


def test_generic_uniprot_grounding_on_rna_is_discovered_from_disk(tmp_path):
    category = tmp_path / "category"
    category.mkdir()
    (category / "record.yaml").write_text(
        "causal_graphs:\n"
        "- graph_id: g\n"
        "  nodes:\n"
        "  - node_id: rna\n"
        "    label: regulatory RNA\n"
        "    node_type: RNA\n"
        "    grounding: UniProtKB:P0A6Y8\n",
        encoding="utf-8",
    )

    uses = iter_uses(iter_nodes(tmp_path))

    assert len(uses) == 1
    assert uses[0]["node"]["node_type"] == "RNA"
    assert uses[0]["usage"] == "GENERIC_GROUNDING"


def test_declared_proteome_is_compared_with_all_resolved_proteomes():
    matching = _audit(_node(_example(proteome_id="UP000000625")))
    assert matching["finding"] == ""

    mismatch = _audit(_node(_example(proteome_id="UP000999999")))
    assert "PROTEOME_MISMATCH" in mismatch["finding"]


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


def test_write_report_quotes_empty_final_finding_without_changing_value(tmp_path):
    report = tmp_path / "report.tsv"
    row = {field: "value" for field in FIELDS}
    row["finding"] = ""

    write_report([row], report)

    text = report.read_text(encoding="utf-8")
    assert text.splitlines()[1].endswith('\t""')
    with report.open(encoding="utf-8", newline="") as handle:
        round_tripped = list(csv.DictReader(handle, delimiter="\t"))
    assert round_tripped[0]["finding"] == ""


def test_check_inventory_detects_missing_or_drifted_report_rows(tmp_path):
    category = tmp_path / "physiology"
    category.mkdir()
    record = category / "catalase.yaml"
    record.write_text(
        "causal_graphs:\n"
        "- graph_id: g1\n"
        "  nodes:\n"
        "  - node_id: p\n"
        "    label: Protein\n"
        "    node_type: GENE_OR_PROTEIN\n"
        "    protein_examples:\n"
        "    - uniprot_id: UniProtKB:P0A6Y8\n"
        "      taxon_id: NCBITaxon:562\n"
        "      taxon_label: Escherichia coli\n"
        "      entry_status: REVIEWED\n"
        "      entry_version: 180\n"
        "      sequence_version: 1\n",
        encoding="utf-8",
    )
    uses = iter_uses(iter_nodes(tmp_path))
    rows = audit_uses(uses, delay=0, resolver=lambda _acc, _delay: _resolved())
    report = tmp_path / "uniprot_grounding_audit.tsv"
    write_report(rows, report)

    assert check_inventory(tmp_path, report) == []

    # Mutate entry_version on disk without refreshing report -> metadata mismatch
    record.write_text(
        record.read_text(encoding="utf-8").replace("entry_version: 180", "entry_version: 181"),
        encoding="utf-8",
    )
    # Mutate entry_version on disk AND hand-edit declared_entry_version in report without
    # updating resolved entry_version -> intra-row entry_version_match consistency error
    write_report([{**rows[0], "declared_entry_version": 181}], report)
    errors_intra = check_inventory(tmp_path, report)
    assert any("declared_entry_version='181', entry_version='180'" in err for err in errors_intra)

    # Restore report to original 180 -> metadata mismatch vs corpus 181
    write_report(rows, report)
    errors = check_inventory(tmp_path, report)
    assert len(errors) == 1
    assert "declared_entry_version: corpus='181' vs report='180'" in errors[0]

    # Add a second protein example on disk without refreshing report -> missing from report
    record.write_text(
        record.read_text(encoding="utf-8")
        + "    - uniprot_id: UniProtKB:P13029\n"
        "      taxon_id: NCBITaxon:562\n"
        "      taxon_label: Escherichia coli\n"
        "      entry_status: REVIEWED\n"
        "      entry_version: 195\n"
        "      sequence_version: 1\n",
        encoding="utf-8",
    )
    errors2 = check_inventory(tmp_path, report)
    assert any("missing from report (1x):" in err and "P13029" in err for err in errors2)


def test_committed_uniprot_grounding_audit_matches_corpus_inventory():
    assert check_inventory() == []


def test_fetch_retries_transient_http_5xx_and_429_then_succeeds(monkeypatch):
    import io
    import json

    payload = {
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "primaryAccession": "P0A6Y8",
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Chaperone protein DnaK"}}
        },
        "genes": [{"geneName": {"value": "dnaK"}}],
        "organism": {"scientificName": "Escherichia coli", "taxonId": 562},
        "entryAudit": {"entryVersion": 180, "sequenceVersion": 1},
        "uniProtKBCrossReferences": [{"database": "Proteomes", "id": "UP000000625"}],
    }
    attempts = []
    sleeps = []

    class _DummyResp(io.StringIO):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.close()

    def flaky_urlopen(url, timeout):
        attempts.append(url)
        if len(attempts) == 1:
            raise urllib.error.HTTPError(url, 500, "Internal Server Error", {}, None)
        if len(attempts) == 2:
            raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, None)
        return _DummyResp(json.dumps(payload))

    monkeypatch.setattr("audit_uniprot_grounding.urllib.request.urlopen", flaky_urlopen)
    monkeypatch.setattr("audit_uniprot_grounding.time.sleep", sleeps.append)

    resolved = fetch("P0A6Y8", delay=0.1, max_retries=3, retry_delay=0.5)
    assert len(attempts) == 3
    assert sleeps == [0.1, 0.5, 1.0]
    assert resolved["status"] == "reviewed"
    assert resolved["primary_accession"] == "P0A6Y8"
    assert resolved["taxon_id"] == "562"


def test_fetch_does_not_retry_http_404_or_400_and_retries_urlerror(monkeypatch):
    attempts_404 = []

    def not_found(url, timeout):
        attempts_404.append(url)
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

    monkeypatch.setattr("audit_uniprot_grounding.urllib.request.urlopen", not_found)
    assert fetch("P00000", delay=0, max_retries=3) == {"status": "deleted"}
    assert len(attempts_404) == 1

    attempts_400 = []

    def bad_request(url, timeout):
        attempts_400.append(url)
        raise urllib.error.HTTPError(url, 400, "Bad Request", {}, None)

    monkeypatch.setattr("audit_uniprot_grounding.urllib.request.urlopen", bad_request)
    assert fetch("BADACC", delay=0, max_retries=3) == {
        "status": "error",
        "uniprot_name": "HTTP 400",
    }
    assert len(attempts_400) == 1

    attempts_net = []

    def net_down(url, timeout):
        attempts_net.append(url)
        raise urllib.error.URLError("temporary DNS failure")

    monkeypatch.setattr("audit_uniprot_grounding.urllib.request.urlopen", net_down)
    res_net = fetch("P0A6Y8", delay=0, max_retries=2)
    assert len(attempts_net) == 3
    assert res_net["status"] == "error"
    assert "temporary DNS failure" in res_net["uniprot_name"]


