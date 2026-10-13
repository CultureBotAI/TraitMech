"""Protect the morphological umbrella and the five narrowly coupled edits."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_nematode_trap_formation_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for attr, name in [("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"),
                       ("PROPOSAL", "proposal/template.tsv")]:
        monkeypatch.setattr(writer, attr, tmp_path / name)
    monkeypatch.setattr(writer, "CHILD_PATHS", {
        slug: tmp_path / f"{slug}.yaml" for slug in writer.CHILDREN
    })
    monkeypatch.setattr(writer, "PREIMAGE_SHA256", {})
    writer.write_validated_trait(copy.deepcopy(writer.PARENT), writer.PARENT_PATH)
    for slug, (identifier, discussion_id, _) in writer.CHILDREN.items():
        child = {
            "identifier": identifier, "label": slug.replace("_", " "),
            "definition": "A controlled narrower trap-formation phenotype.",
            "definition_source": writer.JI, "trait_category": "MORPHOLOGY",
            "term_kind": "CLASS", "mapping_status": "PROPOSED",
            "parent_traits": [writer.PARENT["identifier"]],
            "evidence": [{"reference": writer.JI, "notes": "Keep evidence unchanged."}],
            "discussions": [
                {"discussion_id": discussion_id, "kind": "CURATION_TODO",
                 "status": "OPEN", "prompt": "Find the morphological parent.",
                 "rationale": f"Controlled historical rationale for {slug}."},
                {"discussion_id": "independent-gap", "kind": "KNOWLEDGE_GAP",
                 "status": "OPEN", "prompt": "Preserve the mechanism question.",
                 "rationale": "Independent uncertainty."},
            ],
        }
        writer.event(child, "PRIOR_EVENT", "Keep earlier history.")
        writer.PREIMAGE_SHA256[slug] = writer.digest(child)
        writer.write_validated_trait(child, writer.CHILD_PATHS[slug])
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_source_limits():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000718"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A morphological phenotype in which a fungus differentiates hyphae into "
        "specialized nematode-capturing structures."
    )
    assert not any(record.get(k) for k in [
        "canonical_examples", "causal_graphs", "protein_examples", "xrefs", "synonyms",
    ])
    evidence = record["evidence"]
    assert [e["reference"] for e in evidence] == [writer.JI, writer.YANG, writer.CHEN, writer.SAIKAWA]
    assert record["definition_source"] == writer.JI
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in evidence)
    assert "scientific Summary" in evidence[0]["notes"]
    assert "Author Summary, not the scientific abstract" in evidence[1]["notes"]
    assert "NOT_IN_ABSTRACT" in evidence[1]["notes"]
    assert "immature-ring escape" in evidence[2]["notes"]
    assert "incomplete supplementary ZIP is not evidence" in evidence[2]["notes"]
    assert "UNRESOLVED" in evidence[3]["notes"]
    assert "unindexed everywhere" in evidence[3]["notes"]
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    assert "Morphologically complete immature traps are included" in scope["rationale"]
    assert "not exhaust the class" in scope["rationale"]
    assert "0000261, 000262 and 1000125" in scope["rationale"]
    assert "do not validate sequence-only phenotype predictions" in mechanism["rationale"]
    evidence[0]["notes"] = "Mutation must not escape."
    assert writer.build_record()["evidence"][0]["notes"] != evidence[0]["notes"]


def test_proposal_reserves_only_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067100"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == "METPO:1000059"
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == record["identifier"]
    assert all(reference in rows[2][3] for reference in [writer.JI, writer.YANG, writer.CHEN, writer.SAIKAWA])


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
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
        assert child["curation_history"][-1] == writer.child_event(slug)
        child["curation_history"].pop()
        discussion = child["discussions"][0]
        assert discussion.pop("resolved_date") == writer.DATE
        assert discussion.pop("resolution_note") == writer.resolution(slug)
        assert discussion["status"] == "RESOLVED"
        discussion["status"] = "OPEN"
        if slug == writer.COLUMN:
            assert child["discussions"].pop() == writer.COLUMN_GAP
        child["parent_traits"] = old[slug]["parent_traits"]
        assert child == old[slug]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_output_drift_refused(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    if target == "PARENT_PATH":
        record = yaml.safe_load(path.read_text())
        record["definition"] = "Unreviewed parent scope."
        writer.write_validated_trait(record, path)
    else:
        path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", list(writer.CHILDREN))
@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "Changed label"),
    ("definition", "Changed scope"), ("mapping_status", "REVIEWED"),
    ("parent_traits", ["METPO:1000188"]),
])
def test_child_drift_refused(isolated, monkeypatch, slug, field, value):
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    child[field] = value
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", list(writer.CHILDREN))
@pytest.mark.parametrize("drift", ["rationale", "status", "missing", "duplicate"])
def test_discussion_drift_refused(isolated, monkeypatch, slug, drift):
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    discussion = child["discussions"][0]
    if drift == "missing":
        child["discussions"].pop(0)
    elif drift == "duplicate":
        child["discussions"].append(copy.deepcopy(discussion))
    else:
        discussion[drift] = {"rationale": "Independent curation", "status": "RESOLVED"}[drift]
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", list(writer.CHILDREN))
@pytest.mark.parametrize("drift", ["status", "resolved_date", "resolution_note", "history", "evidence"])
def test_replay_drift_refused(isolated, monkeypatch, slug, drift):
    run(monkeypatch, True)
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    if drift == "history":
        child["curation_history"].pop()
    elif drift == "evidence":
        child["evidence"][0]["notes"] = "Independent evidence edit."
    else:
        child["discussions"][0][drift] = {
            "status": "OPEN", "resolved_date": "2026-10-14",
            "resolution_note": "Independent resolution",
        }[drift]
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_column_followup_drift_refused(isolated, monkeypatch):
    run(monkeypatch, True)
    path = writer.CHILD_PATHS[writer.COLUMN]
    child = yaml.safe_load(path.read_text())
    child["discussions"][-1]["status"] = "RESOLVED"
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="column discussion replay differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_all_six_prevalidated_before_writing(isolated, monkeypatch):
    real_writer = writer.write_validated_trait

    def reject_last(record, path):
        if record["identifier"] == writer.CHILDREN[writer.COLUMN][0]:
            raise ValueError("Controlled final-child validation failure")
        return real_writer(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", reject_last)
    before = snapshot(isolated)
    with pytest.raises(ValueError, match="Controlled final-child"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
