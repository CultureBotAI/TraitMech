"""Protect the shortening endpoint and the coupled, fail-closed parent repair."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_cellular_contraction_trait as writer  # noqa: E402


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
    for slug, (identifier, anchor) in writer.CHILDREN.items():
        child = {
            "identifier": identifier, "label": slug.replace("_", " "),
            "definition": "Controlled child phenotype; retain its definition.",
            "definition_source": writer.KHAN,
            "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
            "parent_traits": [writer.PARENT["identifier"]],
            "evidence": [{"reference": writer.KHAN, "snippet": "Preserve this controlled excerpt.",
                          "notes": "Preserve qualifiers. " + writer.OLD_KHAN_URL}],
            "discussions": [
                {"discussion_id": anchor, "kind": "CURATION_TODO", "status": "OPEN",
                 "prompt": "Review parent and assays.", "rationale": "Historical rationale."},
                {"discussion_id": "independent-gap", "kind": "KNOWLEDGE_GAP", "status": "OPEN",
                 "prompt": "Preserve independent uncertainty.", "rationale": "Mechanism remains open."},
            ],
        }
        writer.event(child, "PRIOR_EVENT", "Retain the prior event.")
        writer.PREIMAGE_SHA256[slug] = writer.digest(child)
        writer.write_validated_trait(child, writer.CHILD_PATHS[slug])
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_record_scope_and_sources():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000729"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "body or cytoplasmic projection shortening" in record["label"]
    assert "reducing its length or extension" in record["definition"]
    assert record["definition_source"] == record["evidence"][0]["reference"] == writer.KATOH
    assert {e["reference"] for e in record["evidence"]} == {writer.KATOH, writer.KHAN, writer.FEBVRE}
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [19, 15, 15]
    assert "Triton-extracted" in record["evidence"][0]["notes"]
    assert "access challenge" in record["evidence"][1]["notes"]
    assert "head top to stalk base" in record["evidence"][2]["notes"]
    assert "NOT_IN_ABSTRACT" in record["evidence"][2]["notes"]
    assert "does not establish force" in record["evidence"][2]["notes"]
    assert not any(record.get(k) for k in ("canonical_examples", "causal_graphs", "synonyms", "xrefs"))
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    record["evidence"][0]["notes"] = "Mutated"
    assert writer.build_record()["evidence"][0]["notes"] != "Mutated"


def test_proposal_allocates_only_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1068200"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == "METPO:1000059" and rows[2][5:7] == ["", ""]
    assert rows[2][3].split("|") == [f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml", writer.KATOH]
    assert rows[2][-1] == writer.IDENTIFIER


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = snapshot(isolated)
    old = {slug: yaml.safe_load(p.read_text()) for slug, p in writer.CHILD_PATHS.items()}
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    for slug, path in writer.CHILD_PATHS.items():
        child = yaml.safe_load(path.read_text())
        assert child["parent_traits"] == [writer.IDENTIFIER]
        assert child["curation_history"][:-1] == old[slug]["curation_history"]
        assert child["discussions"][1] == old[slug]["discussions"][1]
        assert child["discussions"][0]["rationale"] == old[slug]["discussions"][0]["rationale"]
        assert child["discussions"][0]["status"] == "RESOLVED"
        child["discussions"][0].pop("resolution_note")
        child["discussions"][0].pop("resolved_date")
        child["discussions"][0]["status"] = "OPEN"
        child["parent_traits"] = old[slug]["parent_traits"]
        child["curation_history"].pop()
        if slug == "rapid_axopodial_contraction":
            assert child["discussions"].pop() == writer.ASSAY_DISCUSSION
            assert writer.ASSAY_DISCUSSION["status"] == "OPEN"
            child["evidence"][0]["notes"] = child["evidence"][0]["notes"].replace(writer.NEW_KHAN_URL, writer.OLD_KHAN_URL)
        assert child == old[slug]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("slug", writer.CHILDREN)
@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "changed"), ("definition", "changed"),
    ("mapping_status", "REVIEWED"), ("parent_traits", ["METPO:1000188"]),
    ("status", "RESOLVED"), ("rationale", "changed"), ("discussion_id", "changed"),
    ("kind", "KNOWLEDGE_GAP"), ("resolved_date", "2026-10-13"),
])
def test_child_drift_refused_before_any_write(isolated, monkeypatch, slug, field, value):
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    (child if field in child else child["discussions"][0])[field] = value
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("change", ["assay", "evidence", "history", "rationale", "resolution"])
def test_successor_drift_refused(isolated, monkeypatch, change):
    run(monkeypatch, True)
    path = writer.CHILD_PATHS["rapid_axopodial_contraction"]
    child = yaml.safe_load(path.read_text())
    if change == "assay":
        child["discussions"][-1]["status"] = "RESOLVED"
    elif change == "evidence":
        child["evidence"][0]["notes"] += " New interpretation."
    elif change == "history":
        writer.event(child, "LATER_CURATION", "Preserve future curation.")
    elif change == "rationale":
        child["discussions"][0]["rationale"] += " New scope."
    else:
        child["discussions"][0]["resolution_note"] = "Changed"
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
def test_conflicts_refused(isolated, monkeypatch, target):
    run(monkeypatch, True)
    path = getattr(writer, target)
    if target == "PROPOSAL":
        path.write_text(path.read_text() + "drift\n")
    else:
        value = yaml.safe_load(path.read_text())
        value["label"] = "changed"
        writer.write_validated_trait(value, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_new_record_cannot_partially_write(isolated, monkeypatch):
    monkeypatch.setitem(writer.RECORD, "unknown_field", "invalid")
    before = snapshot(isolated)
    with pytest.raises(Exception):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_source_receipt():
    path = writer.ROOT / "research/traits/physiology/cellular_contraction-source-verification.json"
    receipt = json.loads(path.read_text())
    assert receipt["trait_id"] == writer.IDENTIFIER
    assert receipt["accepted_at"] == writer.TIMESTAMP
    evidence = writer.build_record()["evidence"]
    assert [(r["reference"], r["snippet"]) for r in receipt["rows"]] == [(e["reference"], e["snippet"]) for e in evidence]
    assert [r["native_verdict"] for r in receipt["rows"]] == ["VERIFIED", "VERIFIED", "NOT_IN_ABSTRACT"]
    assert all(r["direct_source_match"] for r in receipt["rows"])
