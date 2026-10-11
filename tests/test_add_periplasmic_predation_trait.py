"""Protect periplasmic predation scope and fail-closed writer behavior."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_periplasmic_predation_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_evidence_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000699"
    assert record["label"] == "periplasmic bacterial predation"
    assert record["trait_category"] == "ECOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000054"]
    assert record["definition"] == (
        "A predatory bacterial phenotype in which a bacterium enters the periplasm "
        "of a bacterial prey cell and grows and reproduces there using nutrients "
        "obtained by killing and consuming the prey."
    )
    assert record["definition_source"] == writer.IDENTITY
    assert [e["reference"] for e in record["evidence"]] == [
        writer.IDENTITY, writer.GROWTH, writer.STRUCTURE,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all(not record.get(k) for k in ["causal_graphs", "xrefs", "synonyms"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["canonical_examples"][0]["note"] = "mutated"
    assert len(writer.build_record()["evidence"]) == 3
    assert writer.build_record()["canonical_examples"][0]["note"] != "mutated"


def test_taxon_and_inference_limits():
    record = writer.build_record()
    identity, growth, structure = record["evidence"]
    assert "Introduction, second paragraph" in identity["notes"]
    assert "not direct imaging" in identity["notes"]
    assert "single-prey" in growth["notes"]
    assert "remain unread" in growth["notes"]
    assert "not an intact membrane throughout" in structure["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:264462"
    assert example["taxon_label"] == "Bdellovibrio bacteriovorus HD100"
    assert example["reference"] == writer.IDENTITY
    assert "wild-type HD100" in example["note"]
    assert "soil isolate" in example["note"]
    assert "host-independent derivatives" in example["note"]
    scope, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "lifecycle stage, not this whole feeding phenotype" in scope["rationale"]
    assert "cell body external" in scope["rationale"]
    assert "deferred, not claimed absent" in mechanism["rationale"]
    assert "predicted sequence function" in mechanism["rationale"]


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1007653"
    assert rows[2][1:3] == [writer.PARENT["label"], writer.PARENT["definition"]]
    assert rows[2][4] == "METPO:1000059"
    assert rows[2][10] == record["parent_traits"][0]
    assert rows[3][0] == "METPO:1065200"
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][5:7] == ["", ""]
    assert rows[3][7] == rows[2][7] == "metpo_traitmech_2026_10"
    assert rows[3][10] == writer.IDENTIFIER
    assert set(rows[3][3].split("|")) == {
        f"TraitMech:data/traits/ecology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
    }


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_existing_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
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
