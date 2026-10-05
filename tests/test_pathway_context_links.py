"""Pathway links retain source context and reject stale or malformed targets."""

from __future__ import annotations

import copy
import shutil
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from add_pathway_context_links import proposed_changes  # noqa: E402
from render_trait_pages import template_environment  # noqa: E402
from trait_causal_graph import causal_graphs_for_template  # noqa: E402

from traitmech.validation.pathway_links import load_index, pathway_link_errors  # noqa: E402
from traitmech.validation.write_validated import validate_trait, write_validated_trait  # noqa: E402


def sample():
    version, records = load_index()
    doc = yaml.safe_load((ROOT / "data/traits/physiology/heterotrophic.yaml").read_text())
    node = doc["causal_graphs"][0]["nodes"][0]
    node["related_records"] = [{
        "corpus": "PathwayMech", "identifier": "MetaCyc:GLYOXYLATE-BYPASS",
        "relation": "PATHWAY_CONTEXT", "basis": "M. tuberculosis pathway example <not exact>.",
        "source_version": version,
    }]
    return doc, node["related_records"][0], version, records


@pytest.mark.parametrize("field", ["corpus", "identifier", "relation", "basis", "source_version"])
def test_shared_required_fields_are_enforced(field):
    doc, link, _, _ = sample()
    del link[field]
    assert validate_trait(doc)


@pytest.mark.parametrize("field,value", [
    ("corpus", "OtherMech"), ("relation", "EXACT_MATCH"), ("source_version", "main"),
])
def test_local_schema_rejects_unsupported_link_semantics(field, value):
    doc, link, _, _ = sample()
    link[field] = value
    assert validate_trait(doc)


def test_checker_rejects_unknown_target_stale_pin_and_duplicate():
    doc, link, version, records = sample()
    assert pathway_link_errors(doc, version, records) == []
    link["identifier"] = "MetaCyc:DOES-NOT-EXIST"
    link["source_version"] = "0" * 40
    errors = pathway_link_errors(doc, version, records)
    assert any("unknown PathwayMech record" in error for error in errors)
    assert any("source_version" in error for error in errors)
    doc["causal_graphs"][0]["nodes"][0]["related_records"].append(copy.deepcopy(link))
    assert any("duplicate" in error for error in pathway_link_errors(doc, version, records))


def test_rendering_preserves_node_basis_source_pin_and_escapes_text():
    doc, link, _, _ = sample()
    graphs = causal_graphs_for_template(doc)
    page = template_environment().get_template("trait.html").render(
        trait=doc, causal_graphs=graphs, kgm_match={"n_kgm_nodes": 0},
        parent_pages={}, parent_labels={},
    )
    assert "https://culturebotai.github.io/PathwayMech/pages/records/MetaCyc_GLYOXYLATE-BYPASS.html" in page
    assert "M. tuberculosis pathway example &lt;not exact&gt;." in page
    assert link["source_version"] in page


def test_manifest_is_idempotent_and_respects_protected_records(tmp_path):
    shutil.copytree(ROOT / "conf", tmp_path / "conf")
    shutil.copy(ROOT / "DO_NOT_WORK.md", tmp_path / "DO_NOT_WORK.md")
    manifest = yaml.safe_load((tmp_path / "conf/pathway_context_links.yaml").read_text())
    for target in manifest["targets"]:
        path = tmp_path / target["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        doc = yaml.safe_load((ROOT / target["path"]).read_text())
        for graph in doc["causal_graphs"]:
            for node in graph["nodes"]:
                node.pop("related_records", None)
                node["protein_examples"] = [example for example in node.get("protein_examples", [])
                                            if example["uniprot_id"] != "UniProtKB:P06115"]
        write_validated_trait(doc, path)
    before = {path: path.read_bytes() for path in (tmp_path / "data").rglob("*.yaml")}
    proposed = proposed_changes(tmp_path)
    assert proposed and all(path.read_bytes() == content for path, content in before.items())
    for path, doc in proposed.items():
        assert doc["curation_history"][-1]["curator"] == "codex"
        write_validated_trait(doc, path)
    assert proposed_changes(tmp_path) == {}
    (tmp_path / "DO_NOT_WORK.md").write_text(manifest["targets"][0]["path"])
    with pytest.raises(ValueError, match="protected trait"):
        proposed_changes(tmp_path)


def test_pinned_index_tampering_fails_closed(tmp_path):
    shutil.copytree(ROOT / "conf", tmp_path / "conf")
    path = tmp_path / "conf/pathwaymech_index.json"
    path.write_text(path.read_text() + " ")
    with pytest.raises(ValueError, match="SHA-256"):
        load_index(tmp_path)
