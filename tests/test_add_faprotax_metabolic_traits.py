from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import add_faprotax_metabolic_traits as add_faprotax  # noqa: E402


@pytest.fixture()
def metabolism_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    trait_dir = tmp_path / "data" / "traits"
    metabolism = trait_dir / "metabolism"
    metabolism.mkdir(parents=True)
    monkeypatch.setattr(add_faprotax, "TRAIT_DIR", trait_dir)
    monkeypatch.setattr(add_faprotax, "METABOLISM_DIR", metabolism)
    return metabolism


def _write_yaml(path: Path, doc: dict) -> None:
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def test_new_records_skip_existing_same_id_records(metabolism_dir: Path):
    slug, raw = add_faprotax.NEW_RECORDS[0]
    path = metabolism_dir / f"{slug}.yaml"
    record = copy.deepcopy(raw)
    record["mapping_status"] = "REVIEWED"
    record["curation_history"] = [
        {
            "timestamp": "2026-09-09T00:00:00Z",
            "curator": "human",
            "action": "PROMOTE_TO_REVIEWED",
            "changes": "Curated the initial proposal.",
            "llm_assisted": False,
        }
    ]
    _write_yaml(path, record)

    outputs = add_faprotax._new_records()

    assert path not in {output for output, _ in outputs}


def test_replace_parent_removes_old_when_new_is_already_present():
    doc = {"parent_traits": ["METPO:1000802", "traitmech:000121"]}

    assert add_faprotax._replace_parent(doc, "METPO:1000802", "traitmech:000121")
    assert doc["parent_traits"] == ["traitmech:000121"]


def test_dark_sulfur_oxidation_carries_the_v11_go_xref():
    records = dict(add_faprotax.NEW_RECORDS)

    assert records["dark_oxidation_of_sulfur_compounds"]["xrefs"] == ["GO:0019417"]
