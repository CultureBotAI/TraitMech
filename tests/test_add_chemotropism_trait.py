"""Protect growth polarity, source limitations and guarded trait creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_chemotropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "chemotropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_growth_response_has_neutral_polarity_and_not_motile_parent():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000597"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A phenotype in which polarized growth is directionally biased "
        "in response to a spatial chemical gradient."
    )
    assert not any(k in record for k in ["canonical_examples", "xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["positive and negative", "not whole-cell locomotion",
                      "faster extension", "conflicts", "Figure 3"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["unengineered", "taxon-paired protein accessions", "PmaA",
                      "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_two_sources_preserve_growth_and_provenance_limits():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {writer.YAMAMOTO, writer.SRIDHAR}
    for item in record["evidence"]:
        assert 24 <= len(item["snippet"])
        assert len(item["snippet"].split()) <= 25
        assert "Europe PMC full text" in item["notes"]
    aspergillus, fusarium = record["evidence"]
    assert "changed direction" in aspergillus["snippet"]
    assert aspergillus["snippet"].endswith("layer (Fig 3B).")
    for qualifier in ["pH 6.5 and 8", "not only greater biomass", "conflicts",
                      "Growth inhibition", "engineered", "not inspected"]:
        assert qualifier in aspergillus["notes"]
    assert "towards or away" in fusarium["snippet"]
    for qualifier in ["They refers to filamentous fungi", "not significantly directional",
                      "not independently verified", "not visually inspected"]:
        assert qualifier in fusarium["notes"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055100"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_output_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["definition"] = "Unreviewed drift."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_either_output(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)


def test_exact_initial_draft_upgrade_preserves_history(isolated, monkeypatch):
    original = writer.initial_draft()
    writer.write_validated_trait(original, writer.TARGET)
    assert run(monkeypatch, True) == 0
    corrected = yaml.safe_load(writer.TARGET.read_text())
    assert corrected["curation_history"][:-1] == original["curation_history"]
    assert corrected["evidence"][0]["snippet"].endswith(" (Fig 3B).")
