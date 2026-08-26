#!/usr/bin/env python3
"""Fetch ontology snapshots from the exact-synonym review lock manifest.

The manifest is the lock: every source URL is paired with an expected filename,
byte count, and SHA-256 digest. Existing verified files are reused. Existing
mismatched files are never overwritten, and downloaded bytes are installed only
after both checks pass.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import os
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "reports" / "ontology_snapshot_manifest.tsv"


@dataclass(frozen=True)
class LockedSnapshot:
    ontology: str
    version: str
    size: int
    sha256: str
    filename: str
    source_url: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_manifest(path: Path) -> list[LockedSnapshot]:
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    snapshots: list[LockedSnapshot] = []
    seen_files: set[str] = set()
    for line_number, row in enumerate(rows, 2):
        filename = str(row.get("file") or "")
        digest = str(row.get("sha256") or "").lower()
        if not filename or Path(filename).name != filename:
            raise ValueError(f"{path}:{line_number}: unsafe or missing filename {filename!r}")
        if filename in seen_files:
            raise ValueError(f"{path}:{line_number}: duplicate filename {filename!r}")
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise ValueError(f"{path}:{line_number}: invalid SHA-256 {digest!r}")
        try:
            size = int(str(row.get("bytes") or ""))
        except ValueError as error:
            raise ValueError(f"{path}:{line_number}: invalid byte count") from error
        if size < 0:
            raise ValueError(f"{path}:{line_number}: negative byte count")
        source_url = str(row.get("source_url") or "")
        if not source_url:
            raise ValueError(f"{path}:{line_number}: missing source_url")
        seen_files.add(filename)
        snapshots.append(
            LockedSnapshot(
                ontology=str(row.get("ontology") or ""),
                version=str(row.get("version") or ""),
                size=size,
                sha256=digest,
                filename=filename,
                source_url=source_url,
            )
        )
    if not snapshots:
        raise ValueError(f"{path}: manifest contains no snapshots")
    return snapshots


def verify(path: Path, locked: LockedSnapshot) -> tuple[bool, str]:
    actual_size = path.stat().st_size
    if actual_size != locked.size:
        return False, f"size {actual_size}, expected {locked.size}"
    actual_sha = sha256(path)
    if actual_sha != locked.sha256:
        return False, f"sha256 {actual_sha}, expected {locked.sha256}"
    return True, "verified"


def fetch_one(locked: LockedSnapshot, out_dir: Path, verify_only: bool) -> tuple[bool, str]:
    target = out_dir / locked.filename
    if target.exists():
        ok, detail = verify(target, locked)
        return ok, f"REUSED {detail}" if ok else f"MISMATCH {detail}"
    if verify_only:
        return False, "MISSING"

    temporary = out_dir / f".{locked.filename}.{os.getpid()}.part"
    try:
        digest = hashlib.sha256()
        size = 0
        with urllib.request.urlopen(locked.source_url, timeout=60) as response, temporary.open(
            "wb"
        ) as stream:
            while block := response.read(1024 * 1024):
                stream.write(block)
                digest.update(block)
                size += len(block)
        if size != locked.size:
            return False, f"DOWNLOAD_MISMATCH size {size}, expected {locked.size}"
        actual_sha = digest.hexdigest()
        if actual_sha != locked.sha256:
            return False, f"DOWNLOAD_MISMATCH sha256 {actual_sha}, expected {locked.sha256}"
        temporary.replace(target)
        return True, "DOWNLOADED verified"
    except Exception as error:
        return False, f"DOWNLOAD_FAILED {error}"
    finally:
        temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify locked files already in --out-dir without network access",
    )
    args = parser.parse_args(argv)

    try:
        snapshots = read_manifest(args.manifest)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    args.out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for locked in snapshots:
        ok, detail = fetch_one(locked, args.out_dir, args.verify_only)
        print(f"{locked.ontology}\t{locked.filename}\t{detail}")
        failures += not ok
    if failures:
        print(f"ERROR: {failures} snapshot(s) did not match the lock", file=sys.stderr)
        return 1
    print(f"All {len(snapshots)} snapshot(s) match {args.manifest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
