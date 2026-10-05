"""Keep zygote, parent and sperm panel roles separate (#1713)."""

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_oogamy_panel_evidence as writer  # noqa: E402


def test_correction_preserves_other_claims_and_provenance():
    before = writer.original.build_record()
    after = writer.build_record()
    for key in before.keys() - {"evidence", "curation_history"}:
        assert before[key] == after[key]
    assert before["evidence"][:3] == after["evidence"][:3]
    assert before["evidence"][3]["snippet"] == after["evidence"][3]["snippet"]
    notes = after["evidence"][3]["notes"]
    assert writer.NEW in notes and writer.OLD not in notes
    assert "D/G/I" in notes and "Panel E shows a mature zygote" in notes
    assert after["curation_history"][:-1] == before["curation_history"]
    assert "#1713" in after["curation_history"][-1]["changes"]


def test_dry_run_apply_replay_and_drift(tmp_path, monkeypatch):
    target = tmp_path / "oogamy.yaml"
    monkeypatch.setattr(writer, "TARGET", target)
    writer.write_validated_trait(writer.original.build_record(), target)
    before = target.read_bytes()
    monkeypatch.setattr(sys, "argv", ["writer"])
    assert writer.main() == 0
    assert target.read_bytes() == before
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    after = target.read_bytes()
    assert writer.main() == 0 and target.read_bytes() == after
    record = yaml.safe_load(target.read_text())
    record["parent_traits"] = ["METPO:1000059"]
    writer.write_validated_trait(record, target)
    drift = target.read_bytes()
    with pytest.raises(SystemExit, match="differs"):
        writer.main()
    assert target.read_bytes() == drift


def test_invalid_correction_does_not_overwrite(tmp_path, monkeypatch):
    target = tmp_path / "oogamy.yaml"
    monkeypatch.setattr(writer, "TARGET", target)
    before = writer.original.build_record()
    writer.write_validated_trait(before, target)
    content = target.read_bytes()
    invalid = writer.build_record()
    invalid["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: invalid)
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    with pytest.raises(Exception, match="unknown_slot"):
        writer.main()
    assert target.read_bytes() == content
