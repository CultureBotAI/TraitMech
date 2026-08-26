from __future__ import annotations

import csv
import hashlib
import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_exact_synonym_snapshots.py"
SPEC = importlib.util.spec_from_file_location("fetch_exact_synonym_snapshots_test", SCRIPT)
assert SPEC and SPEC.loader
fetch = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fetch
SPEC.loader.exec_module(fetch)


def write_manifest(path: Path, source: Path, payload: bytes) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "ontology", "version", "bytes", "sha256", "file", "source_url", "status"
            ],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(
            {
                "ontology": "TEST",
                "version": "1",
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "file": "test.obo",
                "source_url": source.as_uri(),
                "status": "LOADED",
            }
        )


def test_downloads_and_reuses_verified_snapshot(tmp_path) -> None:
    payload = b"format-version: 1.2\n"
    source = tmp_path / "source.obo"
    source.write_bytes(payload)
    manifest = tmp_path / "manifest.tsv"
    write_manifest(manifest, source, payload)
    out_dir = tmp_path / "snapshots"

    assert fetch.main(["--manifest", str(manifest), "--out-dir", str(out_dir)]) == 0
    assert (out_dir / "test.obo").read_bytes() == payload
    assert fetch.main(
        ["--manifest", str(manifest), "--out-dir", str(out_dir), "--verify-only"]
    ) == 0


def test_mismatched_existing_snapshot_is_not_overwritten(tmp_path) -> None:
    payload = b"expected"
    source = tmp_path / "source.obo"
    source.write_bytes(payload)
    manifest = tmp_path / "manifest.tsv"
    write_manifest(manifest, source, payload)
    out_dir = tmp_path / "snapshots"
    out_dir.mkdir()
    target = out_dir / "test.obo"
    target.write_bytes(b"wrong")

    assert fetch.main(["--manifest", str(manifest), "--out-dir", str(out_dir)]) == 1
    assert target.read_bytes() == b"wrong"


def test_verify_only_reports_missing_snapshot(tmp_path) -> None:
    payload = b"expected"
    source = tmp_path / "source.obo"
    source.write_bytes(payload)
    manifest = tmp_path / "manifest.tsv"
    write_manifest(manifest, source, payload)

    assert fetch.main(
        [
            "--manifest", str(manifest),
            "--out-dir", str(tmp_path / "missing"),
            "--verify-only",
        ]
    ) == 1


def test_missing_download_source_fails_without_installing_snapshot(tmp_path) -> None:
    payload = b"expected"
    source = tmp_path / "source.obo"
    source.write_bytes(payload)
    manifest = tmp_path / "manifest.tsv"
    write_manifest(manifest, source, payload)
    source.unlink()
    out_dir = tmp_path / "snapshots"

    assert fetch.main(["--manifest", str(manifest), "--out-dir", str(out_dir)]) == 1
    assert not (out_dir / "test.obo").exists()
    assert not list(out_dir.glob("*.part"))
