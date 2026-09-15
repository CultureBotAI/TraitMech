"""Publication requires an explicit switch and current validated full inputs."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest
from jinja2 import Environment, FileSystemLoader

from traitmech import text_map_site as site


def configure(root: Path, value="false"):
    config = root / "conf" / "text_map.yaml"
    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text(f"enabled: {value}\n")


def fake_pipeline():
    calls = []
    profile = {
        "model": "BAAI/bge-large-en-v1.5",
        "revision": "d4aa6901d3a41ba39fb536a557fa166f842b0e09",
        "dimension": 1024,
        "max_seq_length": 512,
    }
    manifest = {"encoder": profile, "projection": {"implementation": "pacmap.PaCMAP"}}

    def validate(bundle, *, input_path):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("validate", bundle, input_path))
        return manifest

    def stage(output, published_dir, *, input_path, expected_bundle):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("stage", output, published_dir, expected_bundle))
        return manifest

    pipeline = SimpleNamespace(
        MODEL=profile["model"],
        MODEL_REVISION=profile["revision"],
        MODEL_DIMENSION=1024,
        MAX_SEQ_LENGTH=512,
        current_bundle=lambda output: output / ("a" * 64),
        validate_bundle=validate,
        stage_map=stage,
    )
    return pipeline, calls, manifest


def enable_fixture(root, monkeypatch):
    configure(root, "true")
    source = root / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    pipeline, calls, manifest = fake_pipeline()
    monkeypatch.setattr(site, "load_pipeline", lambda _root: pipeline)

    def export(actual_root, output, **kwargs):
        assert actual_root == root
        assert not kwargs, "publication cannot request a canary or limited input set"
        output.write_text(json.dumps({"test": "fresh full inputs"}))
        return {"scope": "full"}

    monkeypatch.setattr(site, "export_inputs", export)
    return pipeline, calls, manifest


def test_disabled_map_requires_no_runtime_or_artifact(tmp_path, monkeypatch):
    configure(tmp_path)
    monkeypatch.setattr(site, "load_pipeline", lambda _root: pytest.fail("disabled map loaded runtime"))
    with site.prepare_text_map(tmp_path) as ready:
        assert ready is None


def test_enabled_map_missing_bundle_fails(tmp_path):
    configure(tmp_path, "true")
    with pytest.raises(ValueError, match="current.json"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_missing_shared_runtime_fails(tmp_path):
    configure(tmp_path, "true")
    source = tmp_path / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    with pytest.raises(ValueError, match="CLAW-governed"), site.prepare_text_map(tmp_path):
        pass


@pytest.mark.parametrize("value", ["1", "'true'", "null", "[]"])
def test_enablement_requires_an_actual_boolean(tmp_path, value):
    configure(tmp_path, value)
    with pytest.raises(ValueError, match="enabled boolean"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_uses_fresh_full_inputs_and_canonical_stage(tmp_path, monkeypatch):
    _, calls, _ = enable_fixture(tmp_path, monkeypatch)
    with site.prepare_text_map(tmp_path) as ready:
        inputs = ready.inputs
        ready.stage(tmp_path / "published")
        assert calls[-1] == (
            "stage",
            tmp_path / "data" / "text_map",
            tmp_path / "published" / "text-map",
            "a" * 64,
        )
    assert not inputs.exists()
    assert calls[0][0] == "validate"


def test_legacy_encoder_cannot_be_published_as_the_common_space(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["encoder"] = {"model": "MiniLM", "revision": "0" * 40, "dimension": 384}
    with pytest.raises(ValueError, match="pinned fleet BGE"), site.prepare_text_map(tmp_path):
        pass


def test_injected_projector_cannot_reach_the_site_build(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["projection"]["implementation"] = "injected-projector"
    with pytest.raises(ValueError, match="actual PaCMAP"), site.prepare_text_map(tmp_path):
        pass


def test_subset_receipt_cannot_reach_publication(tmp_path, monkeypatch):
    enable_fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(site, "export_inputs", lambda _root, _output: {"scope": "subset"})
    with pytest.raises(ValueError, match="full-corpus"), site.prepare_text_map(tmp_path):
        pass


def test_navigation_is_conditional_and_retains_specialty_maps():
    templates = Path(__file__).resolve().parents[1] / "src" / "traitmech" / "templates"
    env = Environment(loader=FileSystemLoader(str(templates)))
    template = env.get_template("index.html")
    context = {"root": "", "category_counts": {}, "projection_label": "PaCMAP"}
    disabled = template.render(text_map_enabled=False, **context)
    enabled = template.render(text_map_enabled=True, **context)
    assert "Explore shared BGE map" not in disabled
    assert 'href="text-map/"' in enabled
    assert 'href="umap.html"' in enabled and 'href="graph.html"' in enabled


def test_invalid_map_preflight_preserves_existing_pages_before_clean(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "scripts"))
    import render_trait_pages as render

    configure(tmp_path, "true")
    published = tmp_path / "published"
    published.mkdir()
    old = published / "index.html"
    old.write_text("existing published site")
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    with pytest.raises(ValueError, match="current.json"):
        render.render_pages(SimpleNamespace(out=published, clean=True, dry_run=False))
    assert old.read_text() == "existing published site"


def test_staging_failure_precedes_renderer_mutation(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "scripts"))
    import render_trait_pages as render

    pipeline, _, _ = enable_fixture(tmp_path, monkeypatch)
    def refuse(*args, **kwargs):
        raise ValueError("generation changed")
    monkeypatch.setattr(pipeline, "stage_map", refuse)
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(render, "_render_pages", lambda *a, **kw: pytest.fail("renderer wrote too early"))
    with pytest.raises(ValueError, match="generation changed"):
        render.render_pages(SimpleNamespace(out=tmp_path / "pages", clean=True, dry_run=False))
    assert not (tmp_path / "pages").exists()


def test_pointer_change_does_not_replace_the_preflight_generation(tmp_path, monkeypatch):
    pipeline, _, _ = enable_fixture(tmp_path, monkeypatch)
    published = tmp_path / "published" / "text-map"
    published.mkdir(parents=True)
    old = published / "index.html"
    old.write_text("previously published map")
    seen = []

    def checked_stage(output, published_dir, *, input_path, expected_bundle):
        seen.append(expected_bundle)
        if pipeline.current_bundle(output).name != expected_bundle:
            raise ValueError("current map differs from preflight generation")
        (published_dir / "index.html").write_text("replacement map")

    monkeypatch.setattr(pipeline, "stage_map", checked_stage)
    with site.prepare_text_map(tmp_path) as ready:
        monkeypatch.setattr(pipeline, "current_bundle", lambda output: output / ("b" * 64))
        with pytest.raises(ValueError, match="preflight generation"):
            ready.stage(tmp_path / "published")
    assert seen == ["a" * 64]
    assert old.read_text() == "previously published map"


def test_common_map_rejects_an_alternate_window_with_other_bge_fields_valid(tmp_path, monkeypatch):
    _, calls, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["encoder"]["max_seq_length"] = 256
    with pytest.raises(ValueError, match="pinned fleet BGE"), site.prepare_text_map(tmp_path):
        pytest.fail("different input window was approved as the common BGE map")
    assert not any(call[0] == "stage" for call in calls)
