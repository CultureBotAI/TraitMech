"""Protect stalk-extension scope, source roles and fail-closed coupled writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_stalk_contraction_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    source = writer.SOURCE_PROPOSAL.read_bytes()
    for name, relative in [("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"),
                           ("SOURCE_PROPOSAL", "historical.tsv"), ("PROPOSAL", "new/template.tsv")]:
        monkeypatch.setattr(writer, name, tmp_path / relative)
    writer.SOURCE_PROPOSAL.write_bytes(source)
    row = next(r for r in csv.reader(io.StringIO(source.decode()), delimiter="\t")
               if r[0] == writer.PARENT_METPO)
    parent = {
        "identifier": writer.PARENT_ID, "label": row[1], "definition": row[2],
        "definition_source": "DOI:10.1242/jeb.189.1.163",
        "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
        "parent_traits": [row[4]],
        "evidence": [{"reference": writer.RYU, "snippet": "Preserve controlled parent evidence."}],
        "discussions": [
            {"discussion_id": writer.ANCHOR, "kind": "CURATION_TODO", "status": "OPEN",
             "prompt": "Review scope.", "rationale": "Keep this. " + writer.OLD_SENTENCE + " Keep that."},
            {"discussion_id": "independent-question", "kind": "KNOWLEDGE_GAP", "status": "OPEN",
             "prompt": "Resolve mechanisms.", "rationale": "Unresolved independent question."},
        ],
    }
    writer.event(parent, "PRIOR_EVENT", "Preserve this earlier event.")
    monkeypatch.setattr(writer, "PARENT_DIGEST", writer.digest(parent))
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_source_roles_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000730"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == [writer.PARENT_ID]
    assert "end-to-end extension" in record["definition"]
    assert record["definition_source"] == writer.KAMIGURI
    assert [e["reference"] for e in record["evidence"]] == [writer.KAMIGURI, writer.RYU]
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [19, 14]
    assert all("NOT_IN_ABSTRACT" in e["notes"] for e in record["evidence"])
    assert "contour length does not change" in record["evidence"][0]["notes"]
    assert "not independent cells" in record["evidence"][1]["notes"]
    context = record["discussions"][0]["evidence"][0]
    assert context["reference"] == writer.AMOS and context["supports"] == "NO_EVIDENCE"
    assert len(context["snippet"].split()) == 17 and "UNRESOLVED" in context["notes"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert not any(record.get(k) for k in ("canonical_examples", "causal_graphs", "synonyms", "xrefs"))
    record["evidence"][0]["notes"] = "Mutated"
    assert writer.build_record()["evidence"][0]["notes"] != "Mutated"


def test_proposal_copies_existing_parent_and_allocates_one_child(isolated):
    record = writer.build_record()
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record, parent)), delimiter="\t"))
    old = list(csv.reader(io.StringIO(writer.SOURCE_PROPOSAL.read_text()), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == old[:2] and rows[1][-3:] == ["", "", ""]
    assert rows[2] == next(r for r in old if r[0] == writer.PARENT_METPO)
    assert rows[3][0] == writer.METPO_ID and rows[3][-1] == writer.IDENTIFIER
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][4] == writer.PARENT_METPO and rows[3][5:7] == ["", ""]
    assert rows[3][3].split("|") == ["TraitMech:data/traits/physiology/stalk_contraction.yaml", writer.KAMIGURI]
    assert writer.AMOS not in rows[3][3] and writer.RYU not in rows[3][3]


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = snapshot(isolated)
    original = yaml.safe_load(writer.PARENT_PATH.read_text())
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    assert all(d["status"] == "OPEN" for d in parent["discussions"])
    parent["discussions"][0]["rationale"] = parent["discussions"][0]["rationale"].replace(
        writer.NEW_SENTENCE, writer.OLD_SENTENCE)
    added = parent["curation_history"].pop()
    assert added["llm_assisted"] and added["timestamp"] == writer.TIMESTAMP
    assert parent == original
    assert writer.SOURCE_PROPOSAL.read_bytes() == before["historical.tsv"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("field", ["identifier", "label", "definition", "mapping_status",
                                  "parent_traits", "evidence", "curation_history",
                                  "status", "rationale", "discussion_id"])
def test_parent_drift_refused_before_writes(isolated, monkeypatch, field):
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    owner = parent if field in parent else parent["discussions"][0]
    owner[field] = [] if isinstance(owner[field], list) else "Changed"
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", ["evidence", "history", "rationale", "independent_question"])
def test_successor_drift_refused(isolated, monkeypatch, field):
    run(monkeypatch, True)
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    if field == "evidence":
        parent["evidence"][0]["notes"] = "Later evidence."
    elif field == "history":
        writer.event(parent, "LATER_EVENT", "Preserve later curation.")
    elif field == "rationale":
        parent["discussions"][0]["rationale"] += " Later scope."
    else:
        parent["discussions"][1]["status"] = "RESOLVED"
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("name", ["TARGET", "PROPOSAL", "SOURCE_PROPOSAL"])
def test_conflicting_output_or_dependency_refused(isolated, monkeypatch, name):
    path = getattr(writer, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("conflicting: content\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["record", "parent"])
def test_results_prevalidated_before_any_write(isolated, monkeypatch, target):
    function = writer.build_record if target == "record" else writer.build_parent
    def invalid(*args):
        record = copy.deepcopy(function(*args))
        record["unknown_field"] = "invalid"
        return record
    monkeypatch.setattr(writer, "build_record" if target == "record" else "build_parent", invalid)
    before = snapshot(isolated)
    with pytest.raises(Exception):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
