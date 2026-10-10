"""Protect source scope, coupled hierarchy, dry runs and stale-preimage refusal."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_biomineralization_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for attr, name in [("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"),
                       ("PROPOSAL", "proposal/template.tsv")]:
        monkeypatch.setattr(writer, attr, tmp_path / name)
    monkeypatch.setattr(writer, "CHILD_PATHS", {
        slug: tmp_path / f"{slug}.yaml" for slug in writer.CHILDREN
    })
    monkeypatch.setattr(writer, "RATIONALE_SHA256", {})
    writer.write_validated_trait(copy.deepcopy(writer.PARENT), writer.PARENT_PATH)
    for slug, scope in writer.CHILDREN.items():
        rationale = f"Controlled historical scope for {slug}; preserve this."
        writer.RATIONALE_SHA256[slug] = hashlib.sha256(rationale.encode()).hexdigest()
        child = {
            **scope, "parent_traits": [writer.PARENT["identifier"]],
            "evidence": [{"reference": scope["definition_source"], "notes": "Keep evidence."}],
            "discussions": [
                {"discussion_id": slug.replace("_", "-") + "-scope-and-parent",
                 "kind": "CURATION_TODO", "status": "OPEN", "prompt": "Review parent.",
                 "rationale": rationale},
                {"discussion_id": "independent-gap", "kind": "KNOWLEDGE_GAP",
                 "status": "OPEN", "prompt": "Preserve this independent gap.",
                 "rationale": "Unrelated uncertainty."},
            ],
        }
        writer.event(child, "PRIOR_EVENT", "Keep earlier history.")
        writer.write_validated_trait(child, writer.CHILD_PATHS[slug])
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_source_limits():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000690"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A physiological phenotype in which a microbe mediates the formation of mineral phases."
    )
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "xrefs", "synonyms"])
    evidence = record["evidence"]
    assert len({e["reference"] for e in evidence}) == 4
    assert record["definition_source"] == evidence[0]["reference"] == writer.TERMINOLOGY
    assert "this is a review" in evidence[0]["notes"]
    assert "M-3P medium" in evidence[1]["snippet"]
    assert "uninoculated" in evidence[1]["notes"]
    assert "not a universal strain rule" in evidence[1]["notes"]
    assert "not proven" in evidence[2]["notes"]
    assert "Full Methods and figures remain unread" in evidence[3]["notes"]
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in evidence)
    scope, mechanisms = record["discussions"]
    assert "matrix-mediated" in scope["rationale"]
    assert "mineral dissolution" in scope["rationale"]
    assert "no automatic cross-axis reparenting" in scope["rationale"]
    assert "community member" in mechanisms["rationale"]
    evidence[0]["notes"] = "Changed"
    assert writer.build_record()["evidence"][0]["notes"] != "Changed"


def test_proposal_only_allocates_new_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1064300"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_replay_preserves_children(isolated, monkeypatch):
    before = snapshot(isolated)
    old = {slug: yaml.safe_load(path.read_text()) for slug, path in writer.CHILD_PATHS.items()}
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    for slug, path in writer.CHILD_PATHS.items():
        child = yaml.safe_load(path.read_text())
        assert child["parent_traits"] == [writer.IDENTIFIER]
        assert child["curation_history"][:-1] == old[slug]["curation_history"]
        assert child["curation_history"][-1]["action"] == "REFINE_BIOMINERALIZATION_PARENT"
        d = child["discussions"][0]
        assert d.pop("resolved_date") == "2026-10-10"
        assert d.pop("resolution_note") == writer.RESOLUTION
        assert d["status"] == "RESOLVED"
        d["status"] = "OPEN"
        child["parent_traits"] = old[slug]["parent_traits"]
        child["curation_history"].pop()
        assert child == old[slug]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("slug", writer.CHILDREN)
@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "changed"), ("definition", "changed"),
    ("mapping_status", "REVIEWED"), ("parent_traits", ["METPO:1000188"]),
    ("status", "RESOLVED"), ("rationale", "changed"), ("discussion_id", "changed"),
    ("kind", "KNOWLEDGE_GAP"), ("resolved_date", "2026-10-09"),
])
def test_child_preimage_drift_refused(isolated, monkeypatch, slug, field, value):
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    target = child if field in child else child["discussions"][0]
    target[field] = value
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field,value", [
    ("status", "OPEN"), ("resolution_note", "changed"), ("resolved_date", "2026-10-09"),
])
def test_replay_drift_refused(isolated, monkeypatch, field, value):
    run(monkeypatch, True)
    path = next(iter(writer.CHILD_PATHS.values()))
    child = yaml.safe_load(path.read_text())
    child["discussions"][0][field] = value
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
def test_output_or_parent_conflict_refused(isolated, monkeypatch, target):
    run(monkeypatch, True)
    path = getattr(writer, target)
    if target == "PROPOSAL":
        path.write_text(path.read_text().replace("biomineralization", "changed"))
    else:
        record = yaml.safe_load(path.read_text())
        record["label"] = "changed"
        writer.write_validated_trait(record, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_validation_failure_writes_nothing(isolated, monkeypatch):
    original = writer.write_validated_trait
    last = list(writer.CHILD_PATHS)[-1]

    def reject(record, path):
        if record["identifier"] == writer.CHILDREN[last]["identifier"]:
            raise ValueError("simulated validation failure")
        original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", reject)
    before = snapshot(isolated)
    with pytest.raises(ValueError, match="simulated"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
