"""Selected graph sources and published receipts must be literal, not guessed."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest


@pytest.fixture
def builder():
    path = Path(__file__).resolve().parents[1] / "scripts/build_embedding_index.py"
    spec = importlib.util.spec_from_file_location("graph_builder_under_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_explicit_missing_source_fails_without_fallback(builder, tmp_path, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["builder", "--src", str(tmp_path / "typo.gz"), "--out-deepwalk", str(tmp_path / "out.gz")],
    )
    assert builder.main() == 2
    assert not (tmp_path / "out.gz").exists()


def test_configured_source_is_selected_even_if_missing(builder, tmp_path, monkeypatch):
    missing = tmp_path / "selected.gz"
    monkeypatch.setenv("KG_MICROBE_EMBEDDINGS", str(missing))
    assert builder.default_deepwalk() == missing


def test_current_local_and_configured_sibling_layout(builder, tmp_path, monkeypatch):
    monkeypatch.delenv("KG_MICROBE_EMBEDDINGS", raising=False)
    monkeypatch.setattr(builder, "REPO_ROOT", tmp_path / "TraitMech")
    sibling = tmp_path / "CommunityMech"
    monkeypatch.setenv("COMMUNITYMECH_ROOT", str(sibling))
    assert builder.default_deepwalk() == sibling / "data/embeddings" / builder.EMBEDDINGS_FILENAME
    local = builder.REPO_ROOT / "data/embeddings" / builder.EMBEDDINGS_FILENAME
    local.parent.mkdir(parents=True)
    local.write_bytes(b"source")
    assert builder.default_deepwalk() == local


def test_output_only_metadata_cannot_bless_old_coordinates(builder, tmp_path):
    with pytest.raises(ValueError, match="Output-only provenance"):
        builder.write_projection_metadata(
            tmp_path / "old-map.json",
            tmp_path / "new-source.gz",
            {"METPO:1": [1.0] * 200},
            "pacmap",
            tmp_path / "matches.tsv",
            tmp_path / "neighbors.json",
        )


def test_renderer_checks_receipt_and_labels_legacy_without_guessing(builder, tmp_path, monkeypatch):
    import hashlib

    path = Path(__file__).resolve().parents[1] / "scripts/render_trait_pages.py"
    monkeypatch.syspath_prepend(str(path.parent))
    spec = importlib.util.spec_from_file_location("graph_renderer_under_test", path)
    renderer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(renderer)
    projection = tmp_path / "map.json"
    projection.write_text("[]")
    neighbors = tmp_path / "trait_nearest_neighbors.json"
    neighbors.write_text("{}")
    assert renderer.load_projection_receipt(projection)["verified"] is False
    receipt = {
        "schema_version": 1,
        "input_dimensions": 200,
        "source": {"filename": "actual_legacy_source.gz", "sha256": "a" * 64},
        "projection": {"method": "umap"},
        "outputs": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (projection, neighbors)
        },
    }
    projection.with_suffix(".metadata.json").write_text(json.dumps(receipt))
    result = renderer.load_projection_receipt(projection)
    assert result["label"] == "UMAP"
    assert result["dimensions"] == 200
    assert result["source"] == "actual_legacy_source.gz"
    assert result["verified"] is True
    neighbors.write_text('{"changed": []}')
    assert renderer.load_projection_receipt(projection)["verified"] is False
    projection.with_suffix(".metadata.json").write_text("broken")
    assert renderer.load_projection_receipt(projection)["label"] == "Unverified projection"
