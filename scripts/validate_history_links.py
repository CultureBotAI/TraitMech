#!/usr/bin/env python3
"""Reject history link values that are not absolute usable URIs."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from new_history_record import history_link_errors


def record_paths(targets: list[Path]) -> list[Path]:
    paths: list[Path] = []
    for target in targets:
        if target.is_dir():
            paths.extend(sorted(target.rglob("*.yaml")))
        elif target.is_file():
            paths.append(target)
        else:
            raise ValueError(f"target does not exist: {target}")
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="+", type=Path)
    args = parser.parse_args(argv)
    try:
        paths = record_paths(args.targets)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    failures = 0
    for path in paths:
        try:
            instance = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as error:
            print(f"{path}: {type(error).__name__}: {error}", file=sys.stderr)
            failures += 1
            continue
        errors = history_link_errors(instance)
        for error in errors:
            print(f"{path}: {error}", file=sys.stderr)
        failures += bool(errors)
    if failures:
        print(f"ERROR: {failures} history record(s) have invalid links", file=sys.stderr)
        return 1
    print(f"history links: {len(paths)} record(s), 0 invalid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
