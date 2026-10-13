"""Guard feeding scope, provenance and fail-closed trait writes."""

import csv
import io
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_nematophagy_trait as writer  # noqa: E402


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


def test_identity_scope_and_history():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000719"
    assert record["label"] == "fungal nematophagy"
    assert record["definition"] == "A nutritional phenotype in which a fungus consumes nematodes as food."
    assert record["trait_category"] == "ECOLOGY"
    assert record["mapping_status"] == "PROPOSED" and record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == "DOI:10.3390/f10050404"
    assert len(record["evidence"]) == 4
    words = Counter()
    for item in record["evidence"]:
        assert item["reference"].startswith(("DOI:", "https://"))
        words[item["reference"]] += len(item["snippet"].split())
    assert len(words) == 3 and max(words.values()) <= 25
    assert not any(record.get(k) for k in ["causal_graphs", "synonyms", "xrefs", "protein_examples"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["canonical_examples"][0]["note"] = "changed"
    assert len(writer.build_record()["evidence"]) == 4
    assert writer.build_record()["canonical_examples"][0]["note"] != "changed"


def test_evidence_and_example_limits():
    record = writer.build_record()
    definition, feeding, modes, digestion = record["evidence"]
    assert "Introduction" in definition["notes"] and "UNRESOLVED" in definition["notes"]
    assert "Figure 2a" in feeding["notes"] and "not measured nutrient flux" in feeding["notes"]
    assert "previously killed" in modes["notes"] and "not run" in modes["notes"]
    for text in ["NOT_IN_ABSTRACT", "TWF3407 is engineered", "12 h", "raw S1"]:
        assert text in digestion["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == ("NCBITaxon:5322", "Pleurotus ostreatus")
    assert example["reference"] == definition["reference"]
    for text in ["grocery-store", "morphologically", "one week", "https://doi.org/"]:
        assert text in example["note"]
    scope, ontology, limits = [d["rationale"] for d in record["discussions"]]
    for text in ["previously dead", "paralysis", "neither necessary nor sufficient", "no universal carbon", "not an exact synonym"]:
        assert text in scope
    for text in ["METPO:0000005", "METPO:000005", "METPO:1000631", "OMO:0001000", "not exact xrefs"]:
        assert text in ontology
    for text in ["not imported", "mep1", "mcp1", "not a correction", "403"]:
        assert text in limits


def test_source_receipt():
    path = writer.ROOT / f"research/traits/ecology/{writer.SLUG}-source-verification.json"
    receipt = json.loads(path.read_text())
    assert receipt["trait_id"] == writer.IDENTIFIER
    assert receipt["decision_timestamp"] == writer.TIMESTAMP
    assert receipt["native_record_verification"]["exit"] == 0
    assert [(r["reference"], r["snippet"]) for r in receipt["rows"]] == [
        (e["reference"], e["snippet"]) for e in writer.build_record()["evidence"]
    ]
    assert [r["native_verdict"] for r in receipt["rows"]] == [
        "UNRESOLVED", "UNRESOLVED", "NOT_RUN_URL_REFERENCE", "NOT_IN_ABSTRACT",
    ]
    for row in receipt["rows"]:
        assert row["exact_contiguous_span"] and row["source_identity_verified"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert len(row["source"]["sha256"]) == 64 and row["source"]["url"].startswith("https://")
        assert row["locator"] and row["inspection_limits"]
    assert receipt["allocation"]["conflicting_reservations"] == []
    assert receipt["novelty"]["ignored_hidden_included"]


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067200"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    citations = rows[2][3].split("|")
    assert len(citations) == len(set(citations)) == 4
    assert set(citations) == {f"TraitMech:data/traits/ecology/{writer.SLUG}.yaml", *(e["reference"] for e in record["evidence"])}


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
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
