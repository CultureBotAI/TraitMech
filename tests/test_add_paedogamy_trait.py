"""Protect the gamete/nucleus distinction and guarded coupled update."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_paedogamy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for name, relative in [
        ("TARGET", "paedogamy.yaml"), ("NEIGHBOR", "autogamy.yaml"),
        ("PROPOSAL", "new/template.tsv"), ("NEIGHBOR_PROPOSAL", "old.tsv"),
    ]:
        monkeypatch.setattr(writer, name, tmp_path / relative)
    writer.write_validated_trait(writer.neighbor_preimage(), writer.NEIGHBOR)
    writer.NEIGHBOR_PROPOSAL.write_text(
        writer.autogamy_writer.proposal_tsv(writer.neighbor_preimage())
    )
    for name in ["NEIGHBOR", "NEIGHBOR_PROPOSAL"]:
        monkeypatch.setattr(writer, name + "_SHA", hashlib.sha256(getattr(writer, name).read_bytes()).hexdigest())
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_evidence_roles():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000624"
    assert record["definition"] == (
        "A sexual-reproduction phenotype in which two gametes produced by "
        "division within a single gametangium fuse with each other."
    )
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY" and record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == writer.TERMINOLOGY
    assert record["synonyms"] == [{
        "synonym_text": "pedogamy", "synonym_type": "EXACT_SYNONYM", "source": writer.BAGMET,
    }]
    assert not any(k in record for k in ["xrefs", "causal_graphs"])
    terminology, microscopy, timing = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.TERMINOLOGY, writer.BAGMET, writer.POULICKOVA,
    }
    assert "not independent experimental replication" in terminology["notes"]
    assert "apparently-qualified" in microscopy["notes"]
    assert "VCA-50 and VCA-52 showed no mating" in microscopy["notes"]
    assert "do not establish absence" in microscopy["notes"]
    assert "after auxospore expansion" in timing["snippet"]
    assert "Preserve cf." in timing["notes"] and "remain unread" in timing["notes"]
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])


def test_qualified_example_and_no_universal_inferences():
    record = writer.build_record()
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:1302829"
    assert example["taxon_label"] == "Nitzschia acidoclinata"
    assert example["reference"] == writer.BAGMET
    for text in ["VCA-7", "not every tested clone", "Gonduras Cave", "2011-02-19",
                 writer.SUPPLEMENT_URL, "does not authenticate a genome"]:
        assert text in example["note"]
    scope, mechanism = record["discussions"]
    for text in ["traitmech:000622", "traitmech:000623", "traitmech:000609",
                 "not an exact synonym", "species-level disjointness", "Broader non-diatom"]:
        assert text in scope["rationale"]
    assert "not a literal locus" in mechanism["rationale"]
    assert "No causal graph" in mechanism["rationale"]


def test_neighbor_repair_preserves_unrelated_facts_and_history():
    before = writer.neighbor_preimage()
    frozen = copy.deepcopy(before)
    after = writer.build_neighbor(before)
    assert before == frozen
    assert "undivided cell, without fusion of separate gametes" in after["definition"]
    assert "meiosis II" not in after["definition"]
    assert after["evidence"][:-1] == before["evidence"]
    assert after["evidence"][-1]["reference"] == writer.TERMINOLOGY
    assert "postmeiotic mitosis" in after["evidence"][-1]["notes"]
    assert after["curation_history"][:-1] == before["curation_history"]
    for key in before.keys() - {"definition", "evidence", "discussions", "curation_history"}:
        assert after[key] == before[key]
    assert "now resolved by direct reading" in after["discussions"][1]["rationale"]
    assert all(d["status"] == "OPEN" for d in after["discussions"])
    quotes = [writer.RECORD["evidence"][0]["snippet"], after["evidence"][-1]["snippet"]]
    assert sum(len(s.split()) for s in quotes) <= 25


@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "drift"),
    ("mapping_status", "REVIEWED"), ("parent_traits", ["METPO:1000188"]),
])
def test_neighbor_semantic_preimage_guards(field, value):
    before = writer.neighbor_preimage()
    before[field] = value
    with pytest.raises(SystemExit, match="differs"):
        writer.build_neighbor(before)


def test_both_proposals_remain_in_parity():
    for record, text, curie, local in [
        (writer.build_record(), writer.proposal_tsv(writer.build_record()), "METPO:1057700", "traitmech:000624"),
        (writer.build_neighbor(writer.neighbor_preimage()),
         writer.autogamy_writer.proposal_tsv(writer.build_neighbor(writer.neighbor_preimage())),
         "METPO:1057500", "traitmech:000622"),
    ]:
        rows = list(csv.reader(io.StringIO(text), delimiter="\t"))
        assert len(rows) == 3 and {len(r) for r in rows} == {11}
        assert rows[1][-3:] == ["", "", ""]
        assert rows[2][0] == curie and rows[2][-1] == local
        assert rows[2][1:3] == [record["label"], record["definition"]]
        assert rows[2][4] == record["parent_traits"][0]
        assert rows[2][5] == ("pedogamy" if local == "traitmech:000624" else "")
        assert rows[2][6] == ""
        assert all(e["reference"] in rows[2][3] for e in record["evidence"])


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("name", ["NEIGHBOR", "NEIGHBOR_PROPOSAL", "TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_all_drift_is_refused_before_writing(isolated, monkeypatch, name, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".yaml":
        record = yaml.safe_load(path.read_text()) if path.exists() else writer.build_record()
        record["label"] = "unexpected drift"
        writer.write_validated_trait(record, path)
    else:
        path.write_text("unexpected drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("name", ["NEIGHBOR", "NEIGHBOR_PROPOSAL"])
def test_missing_preimage_is_refused(isolated, monkeypatch, name):
    getattr(writer, name).unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing reviewed"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_payload_cannot_mutate_any_output(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    before = snapshot(isolated)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
