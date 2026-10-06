"""Guard nuclear-cargo scope, parent repair, provenance and fail-closed replay."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_nucleophagy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "nucleophagy.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "autophagy.yaml")
    monkeypatch.setattr(writer, "PARENT_PROPOSAL", tmp_path / "parent.tsv")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    parent = {
        "identifier": "traitmech:000638", "label": "autophagy",
        "definition": writer.OLD_DEFINITION,
        "definition_source": "DOI:10.1083/jcb.119.2.301",
        "trait_category": "PHYSIOLOGY", "term_kind": "CLASS",
        "mapping_status": "PROPOSED", "parent_traits": ["METPO:1000059"],
        "evidence": [{"reference": "DOI:10.1083/jcb.119.2.301", "notes": "Fixture evidence."}],
        "discussions": [{
            "discussion_id": "autophagy-scope-and-flux", "prompt": "Fixture scope?",
            "kind": "CURATION_TODO", "status": "OPEN", "rationale": "Fixture scope.",
            "posed_by": "codex", "posed_date": "2026-10-06",
        }],
        "curation_history": [{
            "timestamp": "2026-10-06T09:00:00Z", "curator": "fixture",
            "action": "CURATED_WITH_LITERATURE", "changes": "Fixture only.",
        }],
    }
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    monkeypatch.setattr(writer, "PARENT_HASH", writer.fingerprint(parent))
    rows = [*writer.HEADERS, [
        writer.PARENT_METPO_ID, parent["label"], parent["definition"],
        "TraitMech:data/traits/physiology/autophagy.yaml|" + parent["definition_source"],
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "", "Prior context.",
        parent["identifier"],
    ]]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    writer.PARENT_PROPOSAL.write_text(stream.getvalue())
    monkeypatch.setattr(writer, "TEMPLATE_HASH", hashlib.sha256(stream.getvalue().encode()).hexdigest())
    return tmp_path, parent


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_source_bounded_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000643"
    assert record["label"] == "nucleophagy"
    assert record["definition"].startswith("An autophagy phenotype")
    assert "parts of its nucleus or an entire nucleus" in record["definition"]
    assert "lysosomal or vacuolar compartments" in record["definition"]
    assert not any(word in record["definition"] for word in ["selective", "starvation", "Atg", "macro"])
    assert record["definition_source"] == writer.WHOLE
    assert record["parent_traits"] == ["traitmech:000638"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert all(record.get(k) is None for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs"])
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert len(record["discussions"]) == 2
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 5


def test_evidence_keeps_conflicts_and_readout_limits():
    record = writer.build_record()
    pmn, followup, whole, nonselective, review = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 5
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all("Scientific Abstract directly read" in e["notes"] for e in record["evidence"])
    assert "revised by the 2008 follow-up" in pmn["notes"]
    assert "rarely release vesicles" in followup["notes"]
    assert "sample-preparation proteolysis" in whole["notes"]
    assert "not the phenotype" in whole["notes"]
    assert "complementation was incomplete" in whole["notes"]
    assert "data not shown" in nonselective["notes"]
    assert "not an independent experiment" in review["notes"]
    scope = record["discussions"][0]["rationale"]
    assert "GO:0044804" in scope and "not an exact" in scope
    assert "does not require universal selectivity" in scope
    assert "traitmech:000642" in scope


def test_dry_run_apply_replay_and_proposal_parity(isolated, monkeypatch):
    root, original = isolated
    before = snapshot(root)
    assert run(monkeypatch) == 0
    assert snapshot(root) == before
    assert run(monkeypatch, True) == 0
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    expected = copy.deepcopy(original)
    expected["definition"] = writer.NEW_DEFINITION
    expected["evidence"].append(writer.PARENT_EVIDENCE)
    expected["discussions"][0]["rationale"] += writer.PARENT_SCOPE_ADDITION
    expected["curation_history"].append(writer.parent_event())
    assert parent == expected
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PROPOSAL.read_bytes() == before["parent.tsv"]
    rows = list(csv.reader(io.StringIO(writer.PROPOSAL.read_text()), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == writer.HEADERS
    assert rows[2][0] == "METPO:1059100"
    assert rows[2][2] == parent["definition"]
    assert rows[2][3].endswith("|" + writer.WHOLE)
    assert "supersedes v514-v518" in rows[2][9]
    assert rows[3][0] == "METPO:1059600"
    assert rows[3][1:3] == [writer.RECORD["label"], writer.RECORD["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][10] == "traitmech:000643"
    after = snapshot(root)
    assert run(monkeypatch, True) == 0
    assert snapshot(root) == after


@pytest.mark.parametrize("field", [
    "identifier", "label", "definition", "definition_source", "parent_traits",
    "mapping_status", "trait_category", "term_kind", "evidence", "discussions",
    "curation_history",
])
@pytest.mark.parametrize("after_apply", [False, True])
def test_parent_drift_refused_without_partial_write(isolated, monkeypatch, field, after_apply):
    root, _ = isolated
    if after_apply:
        run(monkeypatch, True)
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_empty_or_drifted_files_refused(isolated, monkeypatch, target, after_apply):
    root, _ = isolated
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before


@pytest.mark.parametrize("target", ["parent", "child"])
def test_all_records_prevalidated_before_writes(isolated, monkeypatch, target):
    root, original = isolated
    if target == "parent":
        bad = writer.prepare_parent(original)
        bad["unknown_field"] = True
        monkeypatch.setattr(writer, "prepare_parent", lambda _: bad)
    else:
        bad = writer.build_record()
        bad["unknown_field"] = True
        monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(root)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(root) == before


def test_test_fixture_does_not_weaken_production_guard(isolated, monkeypatch):
    root, _ = isolated
    monkeypatch.setattr(writer, "PARENT_HASH", "ca93d09966ac81f73c0e02b59209429851989505381eeec97eb3f1c2eebff4bc")
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before
