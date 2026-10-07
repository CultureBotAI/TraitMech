"""Protect membrane-uptake scope and both coupled hierarchy refinements."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_endocytosis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for attr, name in [("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"),
                       ("PROPOSAL", "proposal/template.tsv")]:
        monkeypatch.setattr(writer, attr, tmp_path / name)
    monkeypatch.setattr(writer, "CHILD_PATHS", {
        slug: tmp_path / f"{slug}.yaml" for slug in writer.CHILDREN
    })
    monkeypatch.setattr(writer, "RATIONALE_SHA256", {})
    writer.write_validated_trait(
        {**writer.PARENT, "trait_category": "UPPER", "term_kind": "CLASS"}, writer.PARENT_PATH,
    )
    for slug, scope in writer.CHILDREN.items():
        rationale = f"Controlled {slug} historical preimage. " + writer.OLD_PHAGOCYTOSIS_PARENT
        writer.RATIONALE_SHA256[slug] = hashlib.sha256(rationale.encode()).hexdigest()
        child = {
            **scope, "parent_traits": [writer.PARENT["identifier"]],
            "evidence": [{"reference": scope["definition_source"], "notes": "Keep evidence."}],
            "canonical_examples": [{"taxon_id": "NCBITaxon:44689",
                                    "taxon_label": "Dictyostelium discoideum",
                                    "reference": scope["definition_source"],
                                    "note": "Controlled strain qualification."}],
            "discussions": [
                {"discussion_id": writer.DISCUSSIONS[slug], "kind": "CURATION_TODO",
                 "status": "OPEN", "prompt": "Review scope.", "rationale": rationale},
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


def test_scope_sources_and_deferred_claims():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000636"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "plasma-membrane components" in record["definition"]
    assert "intracellular membrane-bound compartments" in record["definition"]
    assert not any(s in record["definition"] for s in ["clathrin", "actin", "degradation"])
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "xrefs", "synonyms"])
    first, second = record["evidence"]
    assert record["definition_source"] == first["reference"] == writer.FIRST
    assert second["reference"] == writer.SECOND
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "BHY10.5" in first["notes"] and "not the SEY6210 control" in first["notes"]
    assert "not visually audited" in first["notes"]
    assert "Full text and figures were unavailable" in second["notes"]
    scope, mechanism = record["discussions"]
    assert "DOI:10.3390/microorganisms11081945" in scope["rationale"]
    assert "not exclusions or disjointness" in scope["rationale"]
    assert "not independent taxon replication" in mechanism["rationale"]
    first["notes"] = "Mutation must not escape."
    assert writer.build_record()["evidence"][0]["notes"] != first["notes"]


def test_proposal_matches_only_new_reservation():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1058900"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


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
        assert child["curation_history"][:-1] == old[slug]["curation_history"]
        assert child["curation_history"][-1]["action"] == "REFINE_ENDOCYTOSIS_PARENT"
        discussion = child["discussions"][0]
        if slug == "pinocytosis":
            assert discussion.pop("resolved_date") == "2026-10-06"
            assert discussion.pop("resolution_note") == writer.PINOCYTOSIS_RESOLUTION
            assert discussion["status"] == "RESOLVED"
            discussion["status"] = "OPEN"
        else:
            assert discussion["status"] == "OPEN"
            assert writer.NEW_PHAGOCYTOSIS_PARENT in discussion["rationale"]
            discussion["rationale"] = discussion["rationale"].replace(
                writer.NEW_PHAGOCYTOSIS_PARENT, writer.OLD_PHAGOCYTOSIS_PARENT,
            )
        child["parent_traits"] = old[slug]["parent_traits"]
        child["curation_history"].pop()
        assert child == old[slug]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_output_and_parent_drift_refused(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    if target == "PARENT_PATH":
        parent = yaml.safe_load(path.read_text())
        parent["definition"] = "Unreviewed scope change"
        writer.write_validated_trait(parent, path)
    else:
        path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", ["pinocytosis", "phagocytosis"])
@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "other uptake"),
    ("definition", "Unreviewed scope change"), ("mapping_status", "REVIEWED"),
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


@pytest.mark.parametrize("slug", ["pinocytosis", "phagocytosis"])
@pytest.mark.parametrize("drift", ["rationale", "status", "kind", "missing", "duplicate"])
def test_discussion_drift_refused(isolated, monkeypatch, slug, drift):
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    discussion = child["discussions"][0]
    if drift == "missing":
        child["discussions"].pop(0)
    elif drift == "duplicate":
        child["discussions"].append(copy.deepcopy(discussion))
    else:
        discussion[drift] = {"rationale": "Independent curation", "status": "RESOLVED",
                             "kind": "KNOWLEDGE_GAP"}[drift]
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("slug", ["pinocytosis", "phagocytosis"])
@pytest.mark.parametrize("drift", ["status", "resolved_date", "resolution_note", "history", "rationale"])
def test_replay_drift_refused(isolated, monkeypatch, slug, drift):
    run(monkeypatch, True)
    path = writer.CHILD_PATHS[slug]
    child = yaml.safe_load(path.read_text())
    if drift == "history":
        child["curation_history"].pop()
    else:
        discussion = child["discussions"][0]
        discussion[drift] = {
            "status": "OPEN" if slug == "pinocytosis" else "RESOLVED",
            "resolved_date": "2026-10-07", "resolution_note": "Independent resolution",
            "rationale": "Independent scope edit",
        }[drift]
    writer.write_validated_trait(child, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_all_records_prevalidated_before_writing(isolated, monkeypatch):
    real_writer = writer.write_validated_trait

    def reject_last(record, path):
        if record["identifier"] == writer.CHILDREN["phagocytosis"]["identifier"]:
            raise ValueError("Controlled final-child validation failure")
        return real_writer(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", reject_last)
    before = snapshot(isolated)
    with pytest.raises(ValueError, match="Controlled final-child"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
