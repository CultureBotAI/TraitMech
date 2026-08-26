#!/usr/bin/env python3
"""Install the hash-locked METPO snapshot into ``data/raw/metpo.owl``.

The old ``just refresh-metpo`` copied an unversioned sibling checkout that is
still on METPO 2025-11-25. This command uses the repository's snapshot manifest,
verifies bytes and SHA-256 before installation, and is dry-run by default.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

from fetch_exact_synonym_snapshots import LockedSnapshot, fetch_one, read_manifest, verify

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "reports" / "ontology_snapshot_manifest.tsv"
DESTINATION = ROOT / "data" / "raw" / "metpo.owl"


def install_verified_snapshot(
    snapshot: Path, destination: Path, locked: LockedSnapshot, *, apply: bool
) -> str:
    ok, detail = verify(snapshot, locked)
    if not ok:
        raise ValueError(f"candidate snapshot does not match lock: {detail}")
    if destination.exists():
        current, _ = verify(destination, locked)
        if current:
            return "CURRENT"
    if not apply:
        return "WOULD_INSTALL"

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        prefix=f".{destination.name}.", suffix=".part", dir=destination.parent,
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        with snapshot.open("rb") as source:
            shutil.copyfileobj(source, stream)
    try:
        ok, detail = verify(temporary, locked)
        if not ok:
            raise ValueError(f"staged snapshot does not match lock: {detail}")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return "INSTALLED"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="replace data/raw/metpo.owl")
    parser.add_argument(
        "--snapshot", type=Path,
        help="use an already downloaded candidate (still hash-verified)",
    )
    args = parser.parse_args(argv)
    try:
        rows = [row for row in read_manifest(MANIFEST) if row.ontology == "METPO"]
        if len(rows) != 1:
            raise ValueError("snapshot manifest must contain exactly one METPO row")
        locked = rows[0]
        if DESTINATION.exists() and verify(DESTINATION, locked)[0]:
            print(f"CURRENT\tMETPO {locked.version}\t{DESTINATION}")
            return 0

        if args.snapshot:
            snapshot = args.snapshot
            result = install_verified_snapshot(snapshot, DESTINATION, locked, apply=args.apply)
        else:
            with tempfile.TemporaryDirectory(prefix="traitmech-metpo-") as directory:
                downloaded = Path(directory) / locked.filename
                ok, detail = fetch_one(locked, Path(directory), verify_only=False)
                if not ok:
                    raise ValueError(detail)
                result = install_verified_snapshot(
                    downloaded, DESTINATION, locked, apply=args.apply
                )
        print(f"{result}\tMETPO {locked.version}\t{DESTINATION}")
        if result == "WOULD_INSTALL":
            print("Re-run with --apply to install the verified snapshot")
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
