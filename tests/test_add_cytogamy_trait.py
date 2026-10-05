"""Guard paired-cell scope, source uncertainty and reviewed preimages."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_cytogamy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "cytogamy.yaml")
    monkeypatch.setattr(writer, "NEIGHBOR", tmp_path / "autogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.neighbor_writer.build_record(), writer.NEIGHBOR)
    monkeypatch.setattr(writer, "NEIGHBOR_SHA", hashlib.sha256(writer.NEIGHBOR.read_bytes()).hexdigest())
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_record_scope_and_evidence():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000623"
    assert record["label"] == "cytogamy"
    assert record["definition"] == (
        "A sexual-reproduction phenotype in which paired cells undergo "
        "self-fertilization by fusion of gametic nuclei originating within "
        "each cell, without reciprocal gametic-nuclear exchange."
    )
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY" and record["term_kind"] == "CLASS"
    assert record["definition_source"] == writer.NOBILI_1967
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs", "canonical_examples"])
    definition, tentative, induced = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.NOBILI_1967, writer.DILLER_1958, writer.ORIAS_1979,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "do not exchange nuclei" in definition["snippet"]
    assert "do not directly demonstrate" in definition["notes"]
    assert "seems" in tentative["snippet"] and "double autogamy" in tentative["snippet"]
    for text in ["not a genetic exclusion", "Full text, actual figures", "tentative"]:
        assert text in tentative["notes"]
    for text in ["hyperosmotic-shock-induced", "not a universal", "remain unread",
                 "provenance is unresolved", "scientific abstract"]:
        assert text in induced["notes"]
    event, = record["curation_history"]
    assert event["action"] == "MINTED_TRAITMECH_ID" and event["llm_assisted"]


def test_open_gaps_preserve_source_attribution():
    scope, provenance = writer.build_record()["discussions"]
    assert scope["status"] == provenance["status"] == "OPEN"
    for text in ["traitmech:000622", "Diller (1958)", "double autogamy",
                 "not all selfing", "No universal", "species-level disjointness"]:
        assert text in scope["rationale"]
    assert "10.1002/jmor.1050660303" in provenance["rationale"]
    assert "not counted trait evidence" in provenance["rationale"]


def test_neighbor_change_is_scoped():
    before = writer.neighbor_writer.build_record()
    frozen = copy.deepcopy(before)
    after = writer.build_neighbor(before)
    assert before == frozen
    assert after["discussions"][0]["status"] == "OPEN"
    assert writer.OLD_SCOPE not in after["discussions"][0]["rationale"]
    assert writer.NEW_SCOPE in after["discussions"][0]["rationale"]
    assert after["curation_history"][:-1] == before["curation_history"]
    for key in before.keys() - {"discussions", "curation_history"}:
        assert before[key] == after[key]
    assert after["discussions"][1:] == before["discussions"][1:]


def test_proposal_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1057600"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][-1] == writer.IDENTIFIER
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["NEIGHBOR", "PROPOSAL", "TARGET"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_fails_closed(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    if target == "PROPOSAL":
        path.parent.mkdir(exist_ok=True)
        path.write_text("unreviewed drift\n")
    else:
        record = yaml.safe_load(path.read_text()) if path.exists() else writer.build_record()
        record["label"] = "unreviewed drift"
        writer.write_validated_trait(record, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_missing_neighbor_fails_closed(isolated, monkeypatch):
    writer.NEIGHBOR.unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing reviewed"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_record_cannot_mutate_outputs(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    before = snapshot(isolated)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
