from __future__ import annotations

import json
from pathlib import Path

import yaml

from scripts import audit_discussions_data as audit


def _fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    config_dir = tmp_path / "conf"
    trait_dir = tmp_path / "data" / "traits" / "ecology"
    config_dir.mkdir()
    trait_dir.mkdir(parents=True)
    config = config_dir / "discussions_config.yaml"
    config.write_text(
        yaml.safe_dump(
            {
                "repo_name": "Fixture",
                "record_glob": "../data/traits/**/*.yaml",
                "name_fields": ["label"],
                "id_field": "identifier",
                "discussions_field": "discussions",
                "page_url_template": "../../pages/traits/{category}/{stem}.html#{discussion_id}",
            },
            sort_keys=False,
        )
    )
    trait = trait_dir / "biofilm.yaml"
    trait.write_text(
        yaml.safe_dump(
            {
                "identifier": "traitmech:1",
                "label": "biofilm",
                "discussions": [
                    {
                        "discussion_id": "gap-1",
                        "prompt": "What is missing?",
                        "kind": "HUMAN_MODEL_MISMATCH",
                        "status": "OPEN",
                        "attaches_to": ["causal_graphs#trait"],
                        "rationale": "A rationale",
                        "posed_by": "curator",
                        "proposed_experiments": [{"experiment_id": "x1"}],
                        "evidence": [{"reference": "PMID:1"}, {"notes": "no ref"}],
                    }
                ],
            },
            sort_keys=False,
        )
    )
    data = tmp_path / "app" / "discussions" / "data.js"
    data.parent.mkdir(parents=True)
    records, metrics, repo = audit.build_expected(config)
    data.write_text(
        f"window.searchData = {json.dumps(records)};\n"
        f"window.searchMetrics = {json.dumps(metrics)};\n"
        f"window.repoName = {json.dumps(repo)};\n"
    )
    return config, trait, data


def test_current_semantic_projection_passes(tmp_path: Path) -> None:
    config, _, data = _fixture(tmp_path)
    assert audit.audit(config, data) == []


def test_yaml_edit_makes_search_data_stale(tmp_path: Path) -> None:
    config, trait, data = _fixture(tmp_path)
    document = yaml.safe_load(trait.read_text())
    document["discussions"][0]["prompt"] = "A corrected question?"
    trait.write_text(yaml.safe_dump(document, sort_keys=False))
    assert audit.audit(config, data) == ["searchData"]


def test_added_discussion_makes_rows_and_metrics_stale(tmp_path: Path) -> None:
    config, trait, data = _fixture(tmp_path)
    document = yaml.safe_load(trait.read_text())
    document["discussions"].append(
        {"discussion_id": "todo-2", "prompt": "Curate this", "kind": "CURATION_TODO"}
    )
    trait.write_text(yaml.safe_dump(document, sort_keys=False))
    assert audit.audit(config, data) == ["searchData", "searchMetrics"]


def test_missing_assignment_fails_closed(tmp_path: Path) -> None:
    config, _, data = _fixture(tmp_path)
    data.write_text("window.searchData = [];\n")
    try:
        audit.audit(config, data)
    except ValueError as exc:
        assert "searchMetrics" in str(exc)
    else:
        raise AssertionError("missing assignment passed the audit")


def test_repository_artifact_is_current() -> None:
    assert audit.audit(
        Path("conf/discussions_config.yaml"), Path("app/discussions/data.js")
    ) == []
