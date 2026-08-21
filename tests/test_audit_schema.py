"""Tests for import-aware schema range auditing."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_schema import local_imported_type_names, undefined_range_hits  # noqa: E402


def test_local_imported_classes_are_known_ranges(tmp_path):
    imported_path = tmp_path / "shared.yaml"
    imported_path.write_text("classes:\n  SharedClass:\n    attributes: {}\n")
    root_path = tmp_path / "root.yaml"
    root_path.write_text(
        "imports: [shared]\n"
        "classes:\n"
        "  Root:\n"
        "    attributes:\n"
        "      shared:\n"
        "        range: SharedClass\n"
    )
    schema = yaml.safe_load(root_path.read_text())

    imported = local_imported_type_names(root_path, schema)
    assert "SharedClass" in imported
    assert undefined_range_hits(schema, imported) == []


def test_genuinely_unknown_range_is_still_reported(tmp_path):
    root_path = tmp_path / "root.yaml"
    root_path.write_text(
        "classes:\n"
        "  Root:\n"
        "    attributes:\n"
        "      missing:\n"
        "        range: NotImported\n"
    )
    schema = yaml.safe_load(root_path.read_text())

    assert undefined_range_hits(schema, set()) == [
        ("Root", "missing", "NotImported")
    ]


def test_traitmech_imported_ranges_are_not_false_positives():
    schema_path = REPO_ROOT / "src/traitmech/schema/traitmech.yaml"
    schema = yaml.safe_load(schema_path.read_text())
    imported = local_imported_type_names(schema_path, schema)

    assert {"Discussion", "Dataset"}.issubset(imported)
    assert undefined_range_hits(schema, imported) == []
