"""Current YAML, not an unchanged common text map, controls graph publication."""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

import pytest
import yaml

from traitmech import graph_embedding_receipts as receipts
from traitmech.graph_publication import check_graph_receipts
from traitmech.text_map_inputs import iter_inputs

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def builder(monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(
        "trait_current_graph_builder", ROOT / "scripts/build_embedding_index.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def generation(tmp_path, builder):
    corpus = tmp_path / "data/traits/ecology"
    corpus.mkdir(parents=True)
    for name, doc in {
        "child": {
            "identifier": "traitmech:000001",
            "label": "Fixture phenotype",
            "trait_category": "ECOLOGY",
            "parent_traits": ["METPO:1", "METPO:2"],
        },
        "parent1": {"identifier": "METPO:1", "label": "First parent", "trait_category": "ECOLOGY"},
        "parent2": {"identifier": "METPO:2", "label": "Second parent", "trait_category": "ECOLOGY"},
        "unmatched": {
            "identifier": "traitmech:000002",
            "label": "Unmatched",
            "trait_category": "ECOLOGY",
        },
    }.items():
        (corpus / (name + ".yaml")).write_text(yaml.safe_dump(doc))
    directory = tmp_path / "data/embeddings"
    directory.mkdir()
    raw = tmp_path / "tiny-source.tsv.gz"
    raw.write_bytes(gzip.compress(b"node\td1\td2\nMETPO:1\t1\t0\nMETPO:2\t0\t1\n", mtime=0))
    source = receipts.GraphSource(raw, ["METPO"])
    vectors = dict(source)
    records = builder.load_metpo_records(tmp_path / "data/traits")
    matches = builder.build_match_table(records, set(vectors), {})
    ledger, points, matrix = [], [], []
    for match in matches:
        nodes = [n for n in match["kgm_nodes"].split(";") if n]
        identifier = match["metpo_curie"]
        ledger.append(
            {
                "identifier": identifier,
                "source_nodes": nodes,
                "missing_nodes": [],
                "status": "projected" if nodes else "no_vectors",
                "match_method": match["match_method"],
            }
        )
        if nodes:
            points.append(
                {
                    "id": identifier,
                    "label": match["label"],
                    "category": match["category"],
                    "match_method": match["match_method"],
                    "kgm_nodes": nodes,
                    "umap_x": float(len(points)),
                    "umap_y": 0.0,
                }
            )
            matrix.append(vectors[nodes[0]])
    neighbors = {row["metpo_curie"]: [] for row in matches}
    for point in points:
        neighbors[point["id"]] = [
            {key: target[key] for key in ("id", "label", "category", "match_method", "kgm_nodes")}
            | {"similarity": 0.5}
            for target in points
            if target != point
        ]
    stage = tmp_path / "stage"
    stage.mkdir()
    (stage / "deepwalk_traits.tsv.gz").write_bytes(raw.read_bytes())
    builder.write_match_table(matches, stage / "metpo_to_kgm_node.tsv")
    (stage / "trait_nearest_neighbors.json").write_text(json.dumps(neighbors))
    for name, method in (("trait_umap.json", "pacmap"), ("trait_graph.json", "sfdp")):
        (stage / name).write_text(json.dumps(points))
        projection = {
            "method": method,
            "parameters": {},
            "normalization": "none",
            "initialization": "pca",
            "library_versions": {"synthetic_fixture": "1"},
            "implementation": "pacmap.PaCMAP",
            "effective_pairs": {"neighbors": 1, "mid_near": 0, "further": 1},
        }
        if method == "sfdp":
            projection.update(
                implementation="graphviz.sfdp",
                graph={
                    "construction": "symmetric_union_knn",
                    "dot_sha256": "a" * 64,
                    "graphviz_version": "synthetic-fixture",
                    "arguments": ["fixture"],
                    "effective_k": 1,
                    "edges": 2,
                },
            )
        receipt = receipts.make_receipt(
            source=source.receipt,
            corpus=receipts.corpus_receipt(sorted(corpus.glob("*.yaml")), tmp_path / "data/traits"),
            ledger=ledger,
            matrix=receipts.matrix_receipt(matrix, [p["id"] for p in points]),
            projection=projection,
            coverage={"eligible": 4, "projected": 3, "omitted": 1, "neighbor_records": 4},
        )
        receipt["nearest_neighbors"] = {"k": 2, "metric": "cosine"}
        files = {
            directory / member: stage / member
            for member in (
                name,
                "trait_nearest_neighbors.json",
                "deepwalk_traits.tsv.gz",
                "metpo_to_kgm_node.tsv",
            )
        }
        receipts.publish_artifacts(
            files, directory / name.replace(".json", ".metadata.json"), receipt
        )
    return tmp_path


def rebind_output(root, filename):
    """Keep fixture receipts internally consistent to exercise stronger publication checks."""
    directory = root / "data/embeddings"
    for metadata in directory.glob("*.metadata.json"):
        receipt = json.loads(metadata.read_text())
        if filename in receipt["outputs"]:
            receipt["outputs"][filename] = hashlib.sha256(
                (directory / filename).read_bytes()
            ).hexdigest()
            metadata.write_text(json.dumps(receipt))


def test_complete_current_generations_and_actual_cli_pass(generation):
    result = check_graph_receipts(generation)
    assert [row["points"] for row in result] == [3, 3]
    assert all(row["traits"] == 4 for row in result)  # omitted trait remains accounted for
    command = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_graph_receipts.py"), "--root", str(generation)],
        capture_output=True,
        text=True,
    )
    assert command.returncode == 0, command.stderr
    assert len(json.loads(command.stdout)["verified_graphs"]) == 2


def test_parent_order_changes_proxy_with_identical_complete_common_text(generation, builder):
    before = list(iter_inputs(generation))
    directory = generation / "data/traits"
    previous = builder.build_match_table(
        builder.load_metpo_records(directory), {"METPO:1", "METPO:2"}, {}
    )
    child = directory / "ecology/child.yaml"
    value = yaml.safe_load(child.read_text())
    value["parent_traits"].reverse()
    child.write_text(yaml.safe_dump(value))
    current = builder.build_match_table(
        builder.load_metpo_records(directory), {"METPO:1", "METPO:2"}, {}
    )
    assert list(iter_inputs(generation)) == before
    assert previous[0]["kgm_nodes"] == "METPO:1" and current[0]["kgm_nodes"] == "METPO:2"
    with pytest.raises(ValueError, match="corpus changed"):
        check_graph_receipts(generation)


@pytest.mark.parametrize("change", ["add", "remove", "symlink"])
def test_complete_ignored_inclusive_corpus_membership(generation, change):
    directory = generation / "data/traits/ecology"
    if change == "add":
        (generation / ".gitignore").write_text("data/traits/ecology/ignored.yaml\n")
        (directory / "ignored.yaml").write_text("identifier: METPO:99\nlabel: Added trait\n")
    elif change == "remove":
        (directory / "unmatched.yaml").unlink()
    else:
        (directory / "alias").symlink_to(directory, target_is_directory=True)
    with pytest.raises(ValueError, match="corpus changed|symlink"):
        check_graph_receipts(generation)


@pytest.mark.parametrize(
    "name",
    [
        "trait_umap.metadata.json",
        "trait_graph.metadata.json",
        "deepwalk_traits.tsv.gz",
        "metpo_to_kgm_node.tsv",
        "trait_nearest_neighbors.json",
        "trait_umap.json",
        "trait_graph.json",
    ],
)
def test_missing_receipts_or_changed_generation_bytes_fail(generation, name):
    path = generation / "data/embeddings" / name
    if name.endswith("metadata.json"):
        path.unlink()
    else:
        path.write_bytes(b"altered bytes")
    with pytest.raises((ValueError, OSError)):
        check_graph_receipts(generation)


def test_receipt_output_set_is_closed(generation):
    path = generation / "data/embeddings/trait_umap.metadata.json"
    receipt = json.loads(path.read_text())
    receipt["outputs"].pop("metpo_to_kgm_node.tsv")
    path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="exactly the map"):
        check_graph_receipts(generation)


@pytest.mark.parametrize(
    "change",
    ["point_order", "point_metadata", "neighbor_coverage", "match_coverage", "paired_source"],
)
def test_self_consistent_but_mismatched_output_identities_fail(generation, change):
    directory = generation / "data/embeddings"
    if change.startswith("point_"):
        name = "trait_umap.json"
        value = json.loads((directory / name).read_text())
        if change == "point_order":
            value.reverse()
        else:
            value[0]["kgm_nodes"] = ["METPO:2"]
        (directory / name).write_text(json.dumps(value))
    elif change == "neighbor_coverage":
        name = "trait_nearest_neighbors.json"
        value = json.loads((directory / name).read_text())
        value.pop("traitmech:000002")
        (directory / name).write_text(json.dumps(value))
    elif change == "match_coverage":
        name = "metpo_to_kgm_node.tsv"
        lines = (directory / name).read_text().splitlines()
        (directory / name).write_text("\n".join(lines[:-1]) + "\n")
    else:
        path = directory / "trait_graph.metadata.json"
        value = json.loads(path.read_text())
        value["source"]["filename"] = "another-historical-source.tsv.gz"
        path.write_text(json.dumps(value))
        name = "trait_graph.json"
    rebind_output(generation, name)
    with pytest.raises(ValueError):
        check_graph_receipts(generation)


def test_actual_render_preflight_preserves_pages_when_graph_is_stale(generation, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    import render_trait_pages as renderer

    config = generation / "conf/text_map.yaml"
    config.parent.mkdir()
    config.write_text("enabled: false\n")
    pages = generation / "pages"
    pages.mkdir()
    old = pages / "index.html"
    old.write_text("prior published site")
    (generation / "data/traits/ecology/unmatched.yaml").unlink()
    monkeypatch.setattr(renderer, "REPO_ROOT", generation)
    monkeypatch.setattr(
        renderer,
        "load_traits",
        lambda: pytest.fail("renderer reached data loading before graph preflight"),
    )
    with pytest.raises(ValueError, match="corpus changed"):
        renderer.render_pages(SimpleNamespace(out=pages, clean=True, dry_run=False))
    assert old.read_text() == "prior published site"


def test_required_qc_and_artifact_only_pushes_cover_publication_gate():
    workflows = ROOT / ".github/workflows"
    qc = yaml.load((workflows / "qc.yaml").read_text(), Loader=yaml.BaseLoader)
    assert {"pull_request", "merge_group", "push"} <= set(qc["on"])
    assert set(qc["on"]["push"]) == {"branches"}  # no source/artifact path filter skips qc
    assert any(step.get("run") == "just qc" for step in qc["jobs"]["qc"]["steps"])
    tests = yaml.load((workflows / "pytest.yaml").read_text(), Loader=yaml.BaseLoader)
    assert "data/embeddings/**" in tests["on"]["push"]["paths"]
    recipes = (ROOT / "justfile").read_text()
    assert "audit-embedding-publication:" in recipes
    assert "uv run python scripts/check_graph_receipts.py" in recipes
