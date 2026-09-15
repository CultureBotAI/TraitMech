"""The rendered source claim covers the whole graph output generation."""
from __future__ import annotations

import gzip
import importlib.util
import json
from pathlib import Path

import pytest
from traitmech import graph_embedding_receipts as receipts


@pytest.fixture
def renderer(monkeypatch):
    script = Path(__file__).resolve().parents[1] / "scripts/render_trait_pages.py"
    monkeypatch.syspath_prepend(str(script.parent))
    spec = importlib.util.spec_from_file_location("trait_receipt_renderer_review", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def generation(tmp_path):
    raw = tmp_path / "graph.tsv.gz"
    raw.write_bytes(gzip.compress(b"node\td1\td2\nMETPO:1\t1\t0\nMETPO:2\t0\t1\nMETPO:3\t1\t1\n", mtime=0))
    reader = receipts.GraphSource(raw, ["METPO"])
    vectors = dict(reader)
    corpus = tmp_path / "trait.yaml"
    corpus.write_text("identifier: METPO:1\nlabel: fixture\n")
    metadata = receipts.make_receipt(
        source=reader.receipt, corpus=receipts.corpus_receipt([corpus], tmp_path),
        ledger=[{"identifier": identifier, "source_nodes": [identifier], "status": "projected"}
                for identifier in vectors],
        matrix=receipts.matrix_receipt(vectors.values(), vectors),
        projection={"method": "pacmap", "parameters": {"n_components": 2},
                    "normalization": "none", "initialization": "pca",
                    "implementation": "pacmap.PaCMAP", "library_versions": {"fixture": "1"},
                    "effective_pairs": {"neighbors": 1, "mid_near": 0, "further": 1}},
        coverage={"eligible": 3, "projected": 3},
    )
    staged = tmp_path / "staged"
    staged.mkdir()
    contents = {"deepwalk_traits.tsv.gz": raw.read_bytes(),
                "metpo_to_kgm_node.tsv": b"metpo_id\tkgm_node\nMETPO:1\tMETPO:1\n",
                "trait_umap.json": b'[{"id":"METPO:1","x":0,"y":0}]',
                "trait_nearest_neighbors.json": b'{"METPO:1": []}'}
    for name, value in contents.items():
        (staged / name).write_bytes(value)
    projection = tmp_path / "trait_umap.json"
    receipts.publish_artifacts({tmp_path / name: staged / name for name in contents},
                               projection.with_suffix(".metadata.json"), metadata)
    return projection, contents


def test_renderer_accepts_complete_current_graph_receipt(renderer, generation):
    projection, _ = generation
    result = renderer.load_projection_receipt(projection)
    assert result["verified"] is True
    assert result["label"] == "PaCMAP" and result["source"] == "graph.tsv.gz"
    assert result["dimensions"] == 2


@pytest.mark.parametrize("name", ["deepwalk_traits.tsv.gz", "metpo_to_kgm_node.tsv",
                                  "trait_umap.json", "trait_nearest_neighbors.json"])
def test_changed_generation_member_cannot_borrow_old_source_claim(renderer, generation, name):
    projection, _ = generation
    (projection.parent / name).write_bytes(b"a later generation")
    assert renderer.load_projection_receipt(projection)["verified"] is False


def test_receipt_cannot_omit_a_required_generation_member(renderer, generation):
    projection, _ = generation
    sidecar = projection.with_suffix(".metadata.json")
    metadata = json.loads(sidecar.read_text())
    metadata["outputs"].pop("metpo_to_kgm_node.tsv")
    sidecar.write_text(json.dumps(metadata))
    assert renderer.load_projection_receipt(projection)["verified"] is False
