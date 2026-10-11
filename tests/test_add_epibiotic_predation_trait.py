"""Guard external feeding scope, parent repair and dry-run-first writes."""

import copy
import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_epibiotic_predation_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    parent = copy.deepcopy(writer.PARENT_PROJECTION)
    parent["curation_history"] = [{
        "timestamp": "2020-01-01T00:00:00Z", "curator": "test",
        "action": "FIXTURE", "changes": "Controlled test preimage.",
    }]
    parent["causal_graphs"] = [{
        "graph_id": "predatory_bacterium_prey_killing",
        "scope_status": "NONMECHANISTIC", "scope_notes": writer.OLD_SCOPE,
        "nodes": [
            {"node_id": "predatory_trait", "label": "predatory bacterium",
             "node_type": "TRAIT", "grounding": writer.PARENT_ID},
            {"node_id": "prey_killing", "label": "prey killing", "node_type": "BIOLOGICAL_PROCESS"},
        ],
        "edges": [{"subject": "predatory_trait", "predicate": "enables", "object": "prey_killing",
                   "description": writer.OLD_EDGE,
                   "evidence": [{"reference": writer.PARENT_PROJECTION["definition_source"]}]}],
    }]
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    controlled_preimage = yaml.safe_load(writer.PARENT_PATH.read_text())
    monkeypatch.setattr(writer, "PARENT_DIGEST", writer.digest(controlled_preimage))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_record_identity_and_evidence():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000697"
    assert record["label"] == "epibiotic bacterial predation"
    assert record["trait_category"] == "ECOLOGY"
    assert record["term_kind"] == "CLASS" and record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000054"]
    assert record["definition"] == (
        "A predatory bacterial phenotype in which a bacterium kills and obtains "
        "nutrients from bacterial prey while attached and growing externally, "
        "without its cell body entering the prey cell."
    )
    assert record["definition_source"] == writer.DEFINITION
    assert [e["reference"] for e in record["evidence"]] == [
        writer.DEFINITION, writer.ISOLATE, writer.LIFECYCLE,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert not any(record.get(k) for k in ["causal_graphs", "synonyms", "xrefs"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_correction_provenance_and_scope_limits():
    record = writer.build_record()
    assert "10.1038/s41467-025-58758-7" in record["evidence"][2]["notes"]
    assert "not another independent experiment" in record["evidence"][2]["notes"]
    assert "Full text, figures and supplement unavailable" in record["evidence"][1]["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:453816"
    assert example["taxon_label"] == "Pseudobdellovibrio exovorus"
    assert example["reference"] == writer.LIFECYCLE
    assert "JSS" in example["note"] and "not every species member" in example["note"]
    assert "https://doi.org/10.1099/ijs.0.039701-0" in example["note"]
    scope, mechanisms = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "METPO:1007093" in scope["rationale"]
    assert "not every use of external killing" in scope["rationale"]
    assert "No organism-level disjointness" in scope["rationale"]
    assert "envelope-crossing feeding structures" in mechanisms["rationale"]
    assert "not direct nutrient tracing" in mechanisms["rationale"]
    assert "deferred, not claimed absent" in mechanisms["rationale"]


def test_proposal_reuses_real_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1007653" and rows[2][4] == "METPO:1000059"
    assert rows[2][1:3] == [writer.PARENT_PROJECTION["label"], writer.PARENT_PROJECTION["definition"]]
    assert rows[3][0] == "METPO:1065000" and rows[3][4] == rows[2][0]
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][5:7] == ["", ""]
    assert rows[3][7] == "metpo_traitmech_2026_10"
    assert rows[3][10] == writer.IDENTIFIER
    assert set(rows[3][3].split("|")) == {
        f"TraitMech:data/traits/ecology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
    }


def test_dry_run_apply_replay_and_bounded_parent_delta(isolated, monkeypatch):
    before = snapshot(isolated)
    parent_before = yaml.safe_load(writer.PARENT_PATH.read_text())
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    assert parent["curation_history"].pop() == writer.scope_correction_event()
    assert parent["curation_history"].pop() == writer.parent_event()
    graph = parent["causal_graphs"][0]
    assert graph["scope_notes"] == writer.NEW_SCOPE
    assert graph["edges"][0]["description"] == writer.NEW_EDGE
    graph["scope_notes"] = writer.OLD_SCOPE
    graph["edges"][0]["description"] = writer.OLD_EDGE
    assert parent == parent_before
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


def test_interim_parent_correction_is_append_only(isolated, monkeypatch):
    original = yaml.safe_load(writer.PARENT_PATH.read_text())
    interim = copy.deepcopy(original)
    interim["causal_graphs"][0]["scope_notes"] = writer.NEW_SCOPE
    interim["causal_graphs"][0]["edges"][0]["description"] = writer.INTERIM_EDGE
    interim["curation_history"].append(writer.parent_event())
    writer.write_validated_trait(interim, writer.PARENT_PATH)
    assert run(monkeypatch, True) == 0
    final = yaml.safe_load(writer.PARENT_PATH.read_text())
    assert final["curation_history"][:-1] == interim["curation_history"]
    assert final == writer.build_parent(original)


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_target_drift_refused_without_writes(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", list(writer.PARENT_PROJECTION))
def test_parent_identity_drift_refused(isolated, monkeypatch, field):
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("after_apply", [False, True])
def test_full_parent_preimage_guard(isolated, monkeypatch, after_apply):
    if after_apply:
        run(monkeypatch, True)
    parent = yaml.safe_load(writer.PARENT_PATH.read_text())
    parent["causal_graphs"][0]["nodes"][1]["label"] = "unreviewed change"
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unrecognized_field"] = "must not be written"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
