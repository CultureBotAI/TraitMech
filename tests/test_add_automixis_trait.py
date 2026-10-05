"""Guard automixis scope, coupled hierarchy and no-partial-write validation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_automixis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TRAITS", tmp_path)
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "new/template.tsv")
    for slug, record in writer.preimages().items():
        writer.write_validated_trait(record, tmp_path / f"{slug}.yaml")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_evidence_and_qualified_example():
    r = writer.build_record()
    assert r["identifier"] == "traitmech:000625"
    assert r["mapping_status"] == "PROPOSED"
    assert r["definition"].startswith("A reproductive phenotype")
    assert "one meiotically dividing cell or their descendants" in r["definition"]
    assert "ploidy is prevented or compensated" in r["definition"]
    assert r["parent_traits"] == ["METPO:1000059"]
    assert {e["reference"] for e in r["evidence"]} == {writer.MOGIE, writer.YEAST}
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in r["evidence"])
    assert "non-fusion routes" in r["evidence"][0]["notes"]
    assert "not a measured automixis rate" in r["evidence"][1]["notes"]
    example, = r["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:36035"
    assert example["reference"] == writer.YEAST
    for phrase in ["NBRC 1721", "single-spore descendant", "wild diploid", writer.SUPPLEMENT_URL]:
        assert phrase in example["note"]
    assert not any(k in r for k in ["synonyms", "xrefs", "causal_graphs"])


@pytest.mark.parametrize("slug", list(writer.CHILD_IDS))
def test_child_changes_only_parent_discussion_and_history(slug):
    before = writer.preimages()[slug]
    frozen = copy.deepcopy(before)
    after = writer.build_child(slug, before)
    assert before == frozen
    assert after["parent_traits"] == [writer.IDENTIFIER]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["discussions"][1:] == before["discussions"][1:]
    assert after["discussions"][0]["status"] == "OPEN"
    assert "parent gap is resolved" in after["discussions"][0]["rationale"]
    for k in before.keys() - {"parent_traits", "discussions", "curation_history"}:
        assert after[k] == before[k]


def test_proposal_has_real_parent_and_preserves_child_ids():
    records = {"automixis": writer.build_record()}
    records.update({s: writer.build_child(s, r) for s, r in writer.preimages().items()})
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(records)), delimiter="\t"))
    assert len(rows) == 6 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    for row, (slug, record) in zip(rows[2:], records.items(), strict=True):
        assert row[0] == (writer.METPO_ID if slug == "automixis" else writer.CHILD_IDS[slug])
        assert row[1:3] == [record["label"], record["definition"]]
        assert row[4] == ("METPO:1000059" if slug == "automixis" else writer.METPO_ID)
        assert row[5] == ("pedogamy" if slug == "paedogamy" else "")
        assert row[10] == record["identifier"]


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load((isolated / "automixis.yaml").read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("slug", ["automixis", *writer.CHILD_IDS])
@pytest.mark.parametrize("after_apply", [False, True])
def test_record_drift_refused_before_any_write(isolated, monkeypatch, slug, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = isolated / f"{slug}.yaml"
    record = yaml.safe_load(path.read_text()) if path.exists() else writer.build_record()
    record["label"] = "unreviewed drift"
    writer.write_validated_trait(record, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", list(writer.CHILD_IDS))
def test_missing_preimage_refused(isolated, monkeypatch, slug):
    (isolated / f"{slug}.yaml").unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_proposal_drift_refused_before_writes(isolated, monkeypatch):
    writer.PROPOSAL.parent.mkdir()
    writer.PROPOSAL.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="proposal differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_empty_existing_target_refused(isolated, monkeypatch):
    (isolated / "automixis.yaml").touch()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
