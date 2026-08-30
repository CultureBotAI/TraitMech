"""Tests for the #478 most-specific canonical-example move."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from move_nacl_optimum_exemplar import (  # noqa: E402
    ACTION,
    BIN_EXAMPLE,
    SOURCE_EXAMPLE,
    transform,
)


def _records():
    return (
        {
            "identifier": "METPO:1000333",
            "canonical_examples": [copy.deepcopy(SOURCE_EXAMPLE)],
        },
        {"identifier": "METPO:1000468", "evidence": []},
    )


def test_moves_the_exact_example_without_parent_bin_duplication():
    parent, bin_record = _records()

    assert transform(parent, bin_record)

    assert "canonical_examples" not in parent
    assert bin_record["canonical_examples"] == [BIN_EXAMPLE]
    assert parent["curation_history"][-1]["action"] == ACTION
    assert bin_record["curation_history"][-1]["action"] == ACTION


def test_is_idempotent_after_the_move():
    parent, bin_record = _records()
    assert transform(parent, bin_record)

    assert not transform(parent, bin_record)


def test_refuses_to_overwrite_a_changed_source_claim():
    parent, bin_record = _records()
    parent["canonical_examples"][0]["reference"] = "DOI:changed"

    with pytest.raises(ValueError, match="exact source exemplar"):
        transform(parent, bin_record)
