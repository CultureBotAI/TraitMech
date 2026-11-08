#!/usr/bin/env python3
"""Inventory pinned Trait native evidence for #2083; 2026-11-07.

Inputs: repository, exact source commit, one record or complete record scope.
Output: exclusive JSON report; no exporter or curated-record mutations.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path

from traitmech.edge_evidence import inspect_inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--record")
    selection.add_argument("--all", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if not args.write:
        print(json.dumps({"plan": True, "source_commit": args.source_commit,
                          "record": args.record, "all": args.all,
                          "writes": "one new inventory report with --write --output"}))
        return
    if args.output is None:
        parser.error("--write requires --output")
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("Inventory output must be new")
    report = inspect_inventory(args.root, args.source_commit,
                               records=(args.record,) if args.record else None)
    raw = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    if args.output.read_bytes() != raw:
        raise ValueError("Persisted inventory differs")
    print(json.dumps({"output": str(args.output), "sha256": hashlib.sha256(raw).hexdigest(),
                      "counts": report["counts"], "review_documents": report["structured_reviews"]["documents"],
                      "approvals_created": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
