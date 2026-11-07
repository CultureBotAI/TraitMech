"""Pinned exemplar scope must not become strain-assay or causal approval."""

from __future__ import annotations

import copy
import importlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from traitmech import edge_curation as adapter


@pytest.fixture
def native_input(tmp_path):
    if os.environ.get("TRAIT_REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip("kg_microbe_curation.native", reason="optional pinned CLAW contract; required by adapter CI")
    root = tmp_path / "native"
    root.mkdir()
    record = {
        "identifier": "METPO:1000617", "label": "fixture negative phenotype", "mapping_status": "REVIEWED",
        "trait_category": "ENVIRONMENT", "term_kind": "CLASS", "definition": "Synthetic fixture.",
        "canonical_examples": [
            {"taxon_id": "NCBITaxon:1", "taxon_label": "Fixture", "reference": "PMID:1",
             "note": "Qualified source example", "strain": "strain A", "negative": True,
             "conditions": {"temperature": 42, "unit": "Cel"}},
            {"taxon_id": "NCBITaxon:1", "taxon_label": "Fixture", "reference": "PMID:2"},
        ],
        "evidence": [{"reference": "PMID:1", "snippet": "Native evidence retained exactly."}],
        "causal_graphs": [{"graph_id": "mechanism", "edges": [{"subject": "protein", "predicate": "enables", "object": "trait"}]}],
    }
    path = root / "data/traits/environment/fixture.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(record, sort_keys=False))
    schema = root / adapter.SCHEMA
    schema.parent.mkdir(parents=True)
    schema.write_text("id: https://example.org/trait\nprefixes:\n  METPO: https://w3id.org/metpo/\n")
    subprocess.run(["git", "init", "--quiet", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "."], check=True)
    subprocess.run(["git", "-C", str(root), "-c", "user.name=Test Fixture", "-c", "user.email=fixture@example.test",
                    "commit", "--quiet", "-m", "Synthetic native fixture"], check=True)
    commit = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    return root, commit, path.relative_to(root).as_posix(), record


def test_complete_native_scope_and_review_limit(native_input):
    root, commit, path, record = native_input
    assertions = list(adapter.build_native_assertions(root, commit))
    assert len(assertions) == 2
    assert assertions[0]["assertion_id"] != assertions[1]["assertion_id"]
    for index, item in enumerate(assertions):
        assert item["payload"]["native_payload"] == {"owner_record": record, "example_index": index,
                                                    "example": record["canonical_examples"][index]}
        assert item["native_locator"]["path"] == path
        assert item["native_locator"]["commit"] == commit
        assert item["payload"]["subject"] == "NCBITaxon:1"
        assert item["payload"]["predicate"] == "biolink:has_phenotype"
        assert item["payload"]["object"] == record["identifier"]
        assert item["native_review"]["status"] == "unassessed"
        assert item["native_review"]["locator"] is None
        assert item["assurance"] == "unassessed"
        assert item["independent_scientific_review"] is False
    context = assertions[0]["payload"]["context"]
    assert context["native_example"]["strain"] == "strain A"
    assert context["native_example"]["negative"] is True
    assert context["native_example"]["conditions"] == {"temperature": 42, "unit": "Cel"}
    assert context["polarity_inferred_from_label"] is False


def test_working_copy_changes_do_not_change_pinned_assertions(native_input):
    root, commit, path, _ = native_input
    expected = list(adapter.build_native_assertions(root, commit))
    (root / path).write_text("This working copy is deliberately not valid YAML")
    assert list(adapter.build_native_assertions(root, commit)) == expected


def test_real_persisted_export_and_existing_destination(native_input, tmp_path):
    root, commit, path, _ = native_input
    canary = tmp_path / "canary"
    result = adapter.publish(root, commit, canary, records=(path,), example_index=0)
    assert result["rows"] == 1
    assert result["native_status_counts"] == {"unassessed": 1}
    assert result["complete_native_scope"] is False
    assert (canary / "assertions.jsonl").stat().st_size == result["assertions_bytes"] > 0
    assert adapter.verify_export(canary) == result
    with pytest.raises(ValueError, match="existing"):
        adapter.publish(root, commit, canary)
    full = adapter.publish(root, commit, tmp_path / "full")
    assert full["rows"] == 2 and full["complete_native_scope"] is True
    assert full["kg_occurrences_approved"] == full["independent_scientific_reviews"] == 0


def test_default_cli_only_plans(native_input, tmp_path, capsys):
    root, commit, path, _ = native_input
    output = tmp_path / "planned"
    assert adapter.main(["--root", str(root), "--source-commit", commit, "--record", path,
                         "--example-index", "0", "--output", str(output)]) == 0
    assert json.loads(capsys.readouterr().out)["mode"] == "plan"
    assert not output.exists()


@pytest.mark.parametrize("change", ["main", "0" * 40, "../invalid"])
def test_immutable_commit_required(native_input, change):
    with pytest.raises(ValueError):
        list(adapter.build_native_assertions(native_input[0], change))


@pytest.mark.parametrize("selection,index", [(("../outside.yaml",), None), ((), None), (None, -1)])
def test_bad_selection_refused(native_input, selection, index):
    with pytest.raises(ValueError):
        list(adapter.build_native_assertions(native_input[0], native_input[1], records=selection, example_index=index))


def test_source_symlink_is_not_followed(native_input, tmp_path):
    root, commit, _, _ = native_input
    linked = tmp_path / "linked"
    linked.symlink_to(root, target_is_directory=True)
    with pytest.raises(ValueError, match="Symlink"):
        list(adapter.build_native_assertions(linked, commit))


def test_tampered_output_fails(native_input, tmp_path):
    root, commit, _, _ = native_input
    output = tmp_path / "export"
    adapter.publish(root, commit, output)
    with (output / "assertions.jsonl").open("ab") as handle:
        handle.write(b"{}\n")
    with pytest.raises(ValueError):
        adapter.verify_export(output)


def test_payload_evidence_binding_is_not_only_a_record_label(native_input):
    from kg_microbe_curation.native import native_assertion_id, validate_native_assertion

    assertion = next(adapter.build_native_assertions(native_input[0], native_input[1]))
    modified = copy.deepcopy(assertion)
    modified["payload"]["native_payload"]["example"]["conditions"]["temperature"] = 30
    modified["assertion_id"] = native_assertion_id(modified)
    with pytest.raises(ValueError, match="payload binding"):
        validate_native_assertion(modified)


def test_ci_requires_the_optional_shared_runtime():
    root = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((root / ".github/workflows/edge-curation.yaml").read_text())
    steps = workflow["jobs"]["native-contract"]["steps"]
    checkout = next(step for step in steps if step.get("with", {}).get("repository") == "CultureBotAI/culturebotai-claw")
    assert checkout["with"]["ref"] == adapter.CLAW_COMMIT
    test_step = next(step for step in steps if "tests/test_edge_curation.py" in step.get("run", ""))
    assert test_step["env"]["TRAIT_REQUIRE_EDGE_CONTRACT"] == "1"


@pytest.mark.parametrize("field,value", [
    ("source_commit", "f" * 40), ("repository", "Example/OtherMech"),
    ("contract", "wrong/v1"), ("schema_version", True), ("kg_occurrences_approved", 1),
    ("independent_scientific_reviews", False), ("complete_native_scope", False),
    ("source_records", ["data/traits/environment/missing.yaml"]),
    ("source_record_count", 2), ("example_index", 99),
])
def test_manifest_only_tampering_is_rejected(native_input, tmp_path, field, value):
    root, commit, _, _ = native_input
    output = tmp_path / "export"
    adapter.publish(root, commit, output)
    path = output / "manifest.json"
    manifest = json.loads(path.read_bytes())
    manifest[field] = value
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        adapter.verify_export(output)


def test_publication_flushes_payload_before_manifest_and_parent_before_success(native_input, tmp_path, monkeypatch):
    root, commit, _, _ = native_input
    output = tmp_path / "durable"
    events = []
    original_sync, original_link = adapter._sync_directory, adapter.os.link

    def sync(path):
        events.append(("sync", Path(path)))
        original_sync(path)

    def link(source, target):
        events.append(("link", Path(target)))
        original_link(source, target)

    monkeypatch.setattr(adapter, "_sync_directory", sync)
    monkeypatch.setattr(adapter.os, "link", link)
    adapter.publish(root, commit, output)
    payload_position = events.index(("link", output / "assertions.jsonl"))
    manifest_position = events.index(("link", output / "manifest.json"))
    assert ("sync", output) in events[payload_position + 1:manifest_position]
    assert events[-2:] == [("sync", output), ("sync", output.parent)]
    assert ("sync", output.parent) in events[:payload_position]


@pytest.mark.parametrize("changed_loader", [False, True])
def test_runtime_pin_covers_actual_governance_loader(native_input, tmp_path, monkeypatch, changed_loader):
    script = Path(__file__).resolve().parents[1] / "scripts/adhoc/check_edge_contract_pin_20261107.py"
    spec = importlib.util.spec_from_file_location("trait_edge_pin_test", script)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    root = tmp_path / "claw"
    monkeypatch.setattr(checker.native, "__file__", str(root / "src/kg_microbe_curation/native.py"))
    monkeypatch.setattr(checker.inspect, "getsourcefile", lambda _: str(root / "src/kg_microbe_governance/artifacts/scripts/record_review.py"))

    def git(arguments, **kwargs):
        if "rev-parse" in arguments:
            return adapter.CLAW_COMMIT + "\n"
        if "remote" in arguments:
            return "https://github.com/CultureBotAI/culturebotai-claw.git\n"
        if "status" in arguments:
            return " M src/kg_microbe_governance/artifacts/scripts/record_review.py\n" if changed_loader and "src/kg_microbe_governance" in arguments else ""
        raise AssertionError(arguments)

    monkeypatch.setattr(checker.subprocess, "check_output", git)
    monkeypatch.setattr(sys, "argv", [str(script), "--claw-root", str(root)])
    if changed_loader:
        with pytest.raises(ValueError, match="uncommitted changes"):
            checker.main()
    else:
        checker.main()
