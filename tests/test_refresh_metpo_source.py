from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from fetch_exact_synonym_snapshots import LockedSnapshot  # noqa: E402
from refresh_metpo_source import install_verified_snapshot  # noqa: E402


def _locked(payload: bytes) -> LockedSnapshot:
    return LockedSnapshot(
        ontology="METPO",
        version="test",
        size=len(payload),
        sha256=hashlib.sha256(payload).hexdigest(),
        filename="metpo.owl",
        source_url="https://example.invalid/metpo.owl",
    )


def test_refresh_is_dry_run_by_default(tmp_path):
    snapshot = tmp_path / "snapshot.owl"
    destination = tmp_path / "raw" / "metpo.owl"
    snapshot.write_bytes(b"new")
    destination.parent.mkdir()
    destination.write_bytes(b"old")
    result = install_verified_snapshot(snapshot, destination, _locked(b"new"), apply=False)
    assert result == "WOULD_INSTALL"
    assert destination.read_bytes() == b"old"


def test_refresh_atomically_installs_only_verified_bytes(tmp_path):
    snapshot = tmp_path / "snapshot.owl"
    destination = tmp_path / "raw" / "metpo.owl"
    snapshot.write_bytes(b"new")
    result = install_verified_snapshot(snapshot, destination, _locked(b"new"), apply=True)
    assert result == "INSTALLED"
    assert destination.read_bytes() == b"new"
    assert list(destination.parent.iterdir()) == [destination]


def test_refresh_rejects_an_unlocked_candidate(tmp_path):
    snapshot = tmp_path / "snapshot.owl"
    snapshot.write_bytes(b"wrong")
    with pytest.raises(ValueError, match="does not match lock"):
        install_verified_snapshot(
            snapshot, tmp_path / "metpo.owl", _locked(b"expected"), apply=True
        )
