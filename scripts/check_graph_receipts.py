#!/usr/bin/env python3
"""Check current trait graph publication inputs without inference or source vectors."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from traitmech.graph_publication import check_graph_receipts  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        result = check_graph_receipts(args.root)
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"graph publication refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"verified_graphs": result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
