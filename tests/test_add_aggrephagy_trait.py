"""Guard aggregate-cargo scope and the immutable autophagy parent context."""

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
import add_aggrephagy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "aggrephagy.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "autophagy.yaml")
    monkeypatch.setattr(writer, "PARENT_PROPOSAL", tmp_path / "parent.tsv")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    parent = {
        "identifier": "traitmech:000638", "label": "autophagy",
        "definition": "A physiological phenotype of intracellular vacuolar degradation.",
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
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "", "Corrected context.",
        parent["identifier"],
    ], [
        "METPO:1059800", "proteaphagy", "Historical child; not copied.",
        "TraitMech:data/traits/physiology/proteaphagy.yaml", writer.PARENT_METPO_ID,
        "", "", "metpo_traitmech_2026_10", "", "Prior child.", "traitmech:000645",
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


def test_identity_and_cargo_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000646"
    assert record["label"] == "aggrephagy"
    assert record["definition"].startswith("An autophagy phenotype")
    assert "selectively degrades protein aggregates" in record["definition"]
    assert "macroautophagic delivery to lysosomal or vacuolar compartments" in record["definition"]
    assert not any(word in record["definition"] for word in ["heat", "Cue5", "Cct2", "ubiquitin"])
    assert record["definition_source"] == writer.HEAT
    assert record["parent_traits"] == ["traitmech:000638"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert all(record.get(k) is None for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs"])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_retains_context_and_source_boundaries():
    record = writer.build_record()
    heat, cct2, cuet, ibophagy = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 4
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "not positive aggrephagy evidence" in heat["notes"]
    assert "separately from Abbreviations" in heat["notes"]
    assert "Atg11-Cct2" in cct2["notes"]
    assert "GFP-47Q cleavage" in cct2["notes"]
    assert "Synopsis S142" in cct2["notes"] and "Results S412" in cct2["notes"]
    assert "not complete cargo destruction" in cct2["notes"]
    assert "separate from human Tollip" in cuet["notes"]
    assert "not counted as independent primary evidence" in cuet["notes"]
    assert "Boundary evidence" in ibophagy["notes"] and "IBophagy" in ibophagy["notes"]
    scope, mechanism = [d["rationale"] for d in record["discussions"]]
    assert "GO:0035973" in scope and "macroautophagy" in scope
    assert "not an exact organismal phenotype" in scope
    assert "broader/narrower relationship" in scope
    assert "traitmech:000645" in scope
    assert "universal requirements" in mechanism
    assert "natural-strain provenance" in mechanism
    assert "human disease outcomes are not microbial trait evidence" in mechanism


def test_dry_run_apply_replay_and_unchanged_parent(isolated, monkeypatch):
    root, original = isolated
    before = snapshot(root)
    assert run(monkeypatch) == 0
    assert snapshot(root) == before
    assert run(monkeypatch, True) == 0
    assert writer.PARENT_PATH.read_bytes() == before["autophagy.yaml"]
    assert yaml.safe_load(writer.PARENT_PATH.read_text()) == original
    assert writer.PARENT_PROPOSAL.read_bytes() == before["parent.tsv"]
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.PROPOSAL.read_text()), delimiter="\t"))
    old_rows = list(csv.reader(io.StringIO(before["parent.tsv"].decode()), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == writer.HEADERS
    assert rows[2] == old_rows[2]
    assert rows[3][0] == "METPO:1059900"
    assert rows[3][1:3] == [writer.RECORD["label"], writer.RECORD["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][10] == "traitmech:000646"
    assert all(r[0] != "METPO:1059800" for r in rows)
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
@pytest.mark.parametrize("content", ["", "drift"])
def test_empty_or_drifted_files_refused(isolated, monkeypatch, target, after_apply, content):
    root, _ = isolated
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before


def test_record_prevalidated_before_writes(isolated, monkeypatch):
    root, _ = isolated
    bad = copy.deepcopy(writer.build_record())
    bad["unknown_field"] = True
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(root)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(root) == before


def test_fixture_does_not_weaken_production_guard(isolated, monkeypatch):
    root, _ = isolated
    monkeypatch.setattr(writer, "PARENT_HASH", "f97521b02026c370e138bea96d5ed332316678c01d9f2786ead3d9e5df5ff398")
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before
