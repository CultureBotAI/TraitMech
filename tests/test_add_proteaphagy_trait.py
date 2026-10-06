"""Guard proteaphagy cargo, evidence limits and immutable parent context."""

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
import add_proteaphagy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "proteaphagy.yaml")
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
        "METPO:1059700", "lipophagy", "Historical child; not copied.",
        "TraitMech:data/traits/physiology/lipophagy.yaml", writer.PARENT_METPO_ID,
        "", "", "metpo_traitmech_2026_10", "", "Prior child.", "traitmech:000644",
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
    assert record["identifier"] == "traitmech:000645"
    assert record["label"] == "proteaphagy"
    assert record["definition"].startswith("An autophagy phenotype")
    assert "degrades its proteasomes or proteasome subcomplexes" in record["definition"]
    assert "lysosomal or vacuolar compartments" in record["definition"]
    assert not any(word in record["definition"] for word in ["starvation", "ATG", "intact", "macro"])
    assert record["definition_source"] == writer.STARVATION
    assert record["parent_traits"] == ["traitmech:000638"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert all(record.get(k) is None for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs"])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_retains_correction_and_conditional_dependence():
    record = writer.build_record()
    starvation, inactivation, regulation = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 3
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "targeted separately" in starvation["notes"]
    assert "caption conflicts" in starvation["notes"]
    assert "no Rpn10 requirement" in starvation["notes"]
    assert writer.CORRECTION in inactivation["notes"]
    assert "PMID:35294886" in inactivation["notes"]
    assert "not independent trait evidence" in inactivation["notes"]
    assert "ATG17 deletion background" in regulation["notes"]
    assert "ATG11 single deletion" in regulation["notes"]
    assert "detection-limit caveat" in regulation["notes"]
    assert "actual figures" in regulation["notes"]
    scope, mechanism = [d["rationale"] for d in record["discussions"]]
    assert "GO:0061816" in scope and "selective macroautophagy" in scope
    assert "not an exact organismal phenotype" in scope
    assert "not the machinery degrading unrelated substrates" in scope
    assert "traitmech:000641" in scope and "traitmech:000643" in scope
    assert "ATG17 deletion background" in mechanism
    assert writer.CORRECTION in mechanism


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
    assert rows[3][0] == "METPO:1059800"
    assert rows[3][1:3] == [writer.RECORD["label"], writer.RECORD["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][10] == "traitmech:000645"
    assert all(r[0] != "METPO:1059700" for r in rows)
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
