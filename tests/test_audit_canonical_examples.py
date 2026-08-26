"""Tests for the canonical_examples audit (#445).

`canonical_examples` is the trait -> organism link, and until now nothing checked
any of it. The tests that matter are the ones pinning that a clean run cannot be
faked: an audit that silently skips resolution and prints "0 errors" is worse
than no audit, because the zero looks like a result.
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.error import URLError

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import audit_canonical_examples as ace  # noqa: E402
from audit_canonical_examples import ERRORS, example_rows  # noqa: E402


class _Adapter:
    """Stand-in for the OAK adapter: a dict of id -> label."""

    def __init__(self, labels: dict[str, str]):
        self._labels = labels

    def label(self, curie: str) -> str | None:
        return self._labels.get(curie)


def _doc(examples: list[dict]) -> dict:
    return {"canonical_examples": examples}


def _rows(examples: list[dict], labels: dict[str, str] | None = None):
    adapter = _Adapter(labels) if labels is not None else None
    rows, counts = example_rows(
        [("f.yaml", _doc(examples))], adapter=adapter, resolve=labels is not None
    )
    return rows, counts


def test_a_matching_id_and_label_is_clean():
    rows, _ = _rows(
        [{"taxon_id": "NCBITaxon:2261", "taxon_label": "Pyrococcus furiosus"}],
        {"NCBITaxon:2261": "Pyrococcus furiosus"},
    )
    assert rows == []


def test_label_drift_warns_rather_than_fails():
    """NCBI adding a strain synonym must not break the build."""
    rows, _ = _rows(
        [{"taxon_id": "NCBITaxon:103690", "taxon_label": "Nostoc sp. PCC 7120"}],
        {"NCBITaxon:103690": "Nostoc sp. PCC 7120 = FACHB-418"},
    )
    assert [r[1] for r in rows] == ["TAXON_LABEL_DRIFT"]
    assert rows[0][1] not in ERRORS


def test_an_id_the_ontology_does_not_know_is_an_error():
    rows, _ = _rows([{"taxon_id": "NCBITaxon:99999999", "taxon_label": "x"}], {})
    assert [r[1] for r in rows] == ["UNRESOLVED_TAXON"]
    assert rows[0][1] in ERRORS


def test_a_missing_taxon_id_is_an_error():
    rows, _ = _rows([{"taxon_label": "Pyrococcus furiosus"}])
    assert [r[1] for r in rows] == ["MISSING_TAXON_ID"]


def test_a_non_curie_is_malformed():
    rows, _ = _rows([{"taxon_id": "2261", "taxon_label": "x"}])
    assert [r[1] for r in rows] == ["MALFORMED_TAXON_CURIE"]


def test_a_non_numeric_ncbitaxon_id_is_malformed():
    rows, _ = _rows([{"taxon_id": "NCBITaxon:abc", "taxon_label": "x"}])
    assert [r[1] for r in rows] == ["MALFORMED_TAXON_CURIE"]


def test_a_non_ncbitaxon_curie_is_shape_checked_but_not_resolved():
    """Another prefix is legal; we just cannot resolve it here."""
    rows, _ = _rows([{"taxon_id": "GTDB:s__Foo_bar", "taxon_label": "x"}], {})
    assert rows == []


def test_without_an_adapter_resolution_is_reported_as_skipped():
    """The zero must not look like a verified result."""
    rows, counts = example_rows(
        [("f.yaml", _doc([{"taxon_id": "NCBITaxon:2261", "taxon_label": "wrong"}]))],
        resolve=False,
    )
    assert rows == [], "id shape is fine, so nothing to report"
    assert counts["resolution"] == 0, "must record that it could not resolve"
    assert counts["resolved"] == 0


def test_counts_report_examples_and_records():
    rows, counts = example_rows(
        [
            ("a.yaml", _doc([{"taxon_id": "NCBITaxon:1", "taxon_label": "a"}])),
            ("b.yaml", _doc([{"taxon_id": "NCBITaxon:2", "taxon_label": "b"}] * 2)),
            ("c.yaml", {}),
        ],
        resolve=False,
    )
    assert counts["examples"] == 3
    assert counts["records"] == 2


def test_the_real_corpus_has_no_errors():
    """Runs on the corpus: every committed example must at least be well formed."""
    rows, counts = example_rows(resolve=False)
    errors = [r for r in rows if r[1] in ERRORS]
    assert errors == [], f"malformed canonical_examples: {errors}"
    assert counts["examples"] > 300, counts


def test_resolve_false_disables_resolution_even_with_an_adapter():
    """The flag is authoritative (#451).

    Guarding only adapter construction meant a supplied adapter resolved anyway,
    so a test asserting "resolution was skipped" would pass for the wrong reason
    -- the exact failure the SKIPPED reporting exists to prevent.
    """
    doc = [("f.yaml", _doc([{"taxon_id": "NCBITaxon:1", "taxon_label": "right"}]))]
    rows, counts = example_rows(doc, adapter=_Adapter({"NCBITaxon:1": "WRONG"}), resolve=False)
    assert rows == [], "resolve=False must not report drift it was told not to look for"
    assert counts["resolution"] == 0
    # ...and with the flag on, the same adapter does find it.
    rows2, counts2 = example_rows(doc, adapter=_Adapter({"NCBITaxon:1": "WRONG"}), resolve=True)
    assert [r[1] for r in rows2] == ["TAXON_LABEL_DRIFT"]
    assert counts2["resolution"] == 1


def test_ncbi_xml_parser_returns_current_scientific_names():
    payload = b"""<?xml version="1.0"?>
    <TaxaSet>
      <Taxon><TaxId>2261</TaxId><ScientificName>Pyrococcus furiosus</ScientificName></Taxon>
      <Taxon><TaxId>103690</TaxId><ScientificName>Nostoc sp. PCC 7120 = FACHB-418</ScientificName></Taxon>
    </TaxaSet>"""
    assert ace._parse_ncbi_taxonomy(payload) == {
        "NCBITaxon:2261": "Pyrococcus furiosus",
        "NCBITaxon:103690": "Nostoc sp. PCC 7120 = FACHB-418",
    }


def test_ncbi_xml_error_cannot_look_like_every_id_is_unresolved():
    with pytest.raises(ValueError, match="temporarily unavailable"):
        ace._parse_ncbi_taxonomy(
            b"<eFetchResult><ERROR>temporarily unavailable</ERROR></eFetchResult>"
        )


def test_ncbi_api_posts_all_ids_once(monkeypatch):
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def read(self):
            return b"<TaxaSet><Taxon><TaxId>2261</TaxId><ScientificName>P. furiosus</ScientificName></Taxon></TaxaSet>"

    seen = {}

    def fake_urlopen(request, timeout):
        seen["body"] = request.data.decode("ascii")
        seen["timeout"] = timeout
        return Response()

    monkeypatch.setattr(ace.urllib.request, "urlopen", fake_urlopen)
    adapter = ace._ncbi_api_adapter(
        ["NCBITaxon:2261", "NCBITaxon:2285"], attempts=1, timeout=7
    )
    assert "id=2261%2C2285" in seen["body"]
    assert seen["timeout"] == 7
    assert adapter.label("NCBITaxon:2261") == "P. furiosus"
    assert adapter.label("NCBITaxon:2285") is None


def test_ncbi_api_failure_is_not_reported_as_a_skipped_clean_run(
    monkeypatch, capsys, tmp_path
):
    (tmp_path / "trait.yaml").write_text(
        "canonical_examples:\n"
        "  - taxon_id: NCBITaxon:2261\n"
        "    taxon_label: Pyrococcus furiosus\n"
    )

    def fail_adapter(_ids):
        raise RuntimeError("service unavailable")

    monkeypatch.setattr(ace, "_ncbi_api_adapter", fail_adapter)
    assert ace.main(["--traits-dir", str(tmp_path), "--ncbi-api"]) == 2
    captured = capsys.readouterr()
    assert "resolution FAILED" in captured.err
    assert "SKIPPED" not in captured.out


def test_ncbi_api_retries_transient_network_failures(monkeypatch):
    calls = 0

    def fail(_request, timeout):
        nonlocal calls
        calls += 1
        raise URLError("temporary")

    monkeypatch.setattr(ace.urllib.request, "urlopen", fail)
    monkeypatch.setattr(ace.time, "sleep", lambda _seconds: None)
    with pytest.raises(RuntimeError, match="after 3 attempt"):
        ace._ncbi_api_adapter(["NCBITaxon:2261"])
    assert calls == 3
