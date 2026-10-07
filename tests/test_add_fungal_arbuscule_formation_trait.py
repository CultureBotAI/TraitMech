"""Protect arbuscule scope, linked-discussion provenance and mutation guards."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_arbuscule_formation_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for name, filename in [
        ("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"),
        ("HAUSTORIUM_PATH", "haustorium.yaml"), ("PROPOSAL", "proposal/template.tsv"),
    ]:
        monkeypatch.setattr(writer, name, tmp_path / filename)
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    before = dict(writer.PARENT, identifier="traitmech:000663", label="fixture haustorium",
                  mapping_status="PROPOSED", trait_category="MORPHOLOGY",
                  discussions=[{
                      "discussion_id": writer.BOUNDARY_ID, "prompt": "Fixture boundary?",
                      "kind": "CURATION_TODO", "status": "OPEN", "rationale": "Fixture scope.",
                  }])
    writer.record_curation_event(
        before, curator="fixture", action="CREATE", timestamp="2026-10-01T00:00:00Z",
    )
    writer.write_validated_trait(before, writer.HAUSTORIUM_PATH)
    monkeypatch.setattr(writer, "HAUSTORIUM_PREIMAGE", writer.digest(before))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_record_scope_and_independent_builds():
    record = writer.build_record()
    assert (record["identifier"], record["label"]) == (
        "traitmech:000664", "fungal arbuscule formation",
    )
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "living plant cells" in record["definition"]
    assert "highly branched hyphal structures" in record["definition"]
    assert not any(s in record["definition"] for s in [
        "root", "nutrient", "obligate", "pathogen", "benefit",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 2


def test_evidence_and_culture_qualifications():
    record = writer.build_record()
    assert record["definition_source"] == writer.THALLUS_STUDY
    root, thallus = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.ROOT_STUDY, writer.THALLUS_STUDY,
    }
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [19, 12]
    assert "transgenic Medicago" in root["notes"]
    assert "not fungal protein anchors" in root["notes"]
    assert "S2B arbuscules at 28 dps" in thallus["notes"]
    assert "Onset remains unresolved" in thallus["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:937382", "Entrophospora etunicata",
    )
    assert example["reference"] == writer.THALLUS_STUDY
    assert all(s in example["note"] for s in [
        "MAFF520053 (H1-1)", "Claroideoglomus etunicatum", "Figure S1",
        "homotypic synonym", "not independent reidentification", "maff=520053",
    ])
    hierarchy, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert all(s in hierarchy["rationale"] for s in [
        "traitmech:000663", "traitmech:000041", "METPO:1000198", "GO:0085041",
        "not asserted equivalent, disjoint or in a subclass relation",
    ])
    assert "deferred, not claimed absent" in mechanism["rationale"]


def test_template_identity_and_shape():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1061700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/morphology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
    }


def test_dry_run_apply_replay_and_exact_link(isolated, monkeypatch):
    before = snapshot(isolated)
    source = yaml.safe_load(writer.HAUSTORIUM_PATH.read_text())
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    linked = yaml.safe_load(writer.HAUSTORIUM_PATH.read_text())
    assert linked["discussions"][0]["status"] == "OPEN"
    assert linked["curation_history"] == source["curation_history"] + [writer.link_event()]
    restored = copy.deepcopy(linked)
    restored["curation_history"].pop()
    restored["discussions"][0]["rationale"] = "Fixture scope."
    assert restored == source
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "HAUSTORIUM_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", list(writer.PARENT))
def test_parent_projection_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", ["status", "rationale", "discussion_id"])
def test_linked_discussion_drift_refused(isolated, monkeypatch, field):
    run(monkeypatch, True)
    record = yaml.safe_load(writer.HAUSTORIUM_PATH.read_text())
    record["discussions"][0][field] = "changed"
    writer.HAUSTORIUM_PATH.write_text(yaml.safe_dump(record))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL", "HAUSTORIUM_PATH"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("builder", ["build_record", "build_haustorium"])
def test_prevalidation_failure_writes_nothing(isolated, monkeypatch, builder):
    original = getattr(writer, builder)

    def invalid(*args):
        record = original(*args)
        record["unrecognized_field"] = "must not be written"
        return record

    monkeypatch.setattr(writer, builder, invalid)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
