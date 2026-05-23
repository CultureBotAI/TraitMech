#!/usr/bin/env python3
"""ROBOT + ELK validation for a TraitMech METPO proposal cohort.

Mirrors `kg-microbe/scripts/extract_metpo_proposals.py::validate_with_robot`
(line 1643): compiles each ROBOT-template TSV into OWL, merges them (optionally
with the local METPO snapshot), and runs ELK to detect unsatisfiable classes.

Robot binary discovery (first match wins):

  1. `$ROBOT` or `$ROBOT_BIN` environment variable.
  2. `robot` on PATH (`shutil.which`).
  3. Sibling-repo fallback: `../kg-microbe/data/raw/robot`, then
     `../../kg-microbe/data/raw/robot` relative to this script.

If none resolve, exits 2 with a hint. The fallback covers the canonical
local layout where TraitMech and kg-microbe sit under the same parent.

Usage:
    python scripts/robot_validate_proposal.py <cohort-dir>
    python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v1
    python scripts/robot_validate_proposal.py <cohort> --no-merge-metpo
    python scripts/robot_validate_proposal.py <cohort> --out reports/robot/<cohort>
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_METPO = REPO_ROOT / "data/raw/metpo.owl"

PREFIXES = [
    "--prefix", "METPO: http://purl.obolibrary.org/obo/METPO_",
    "--prefix", "biolink: https://w3id.org/biolink/vocab/",
    "--prefix", "RO: http://purl.obolibrary.org/obo/RO_",
    "--prefix", "rdfs: http://www.w3.org/2000/01/rdf-schema#",
]


def find_robot() -> str | None:
    """Discover the robot executable per the precedence in the module docstring."""
    for var in ("ROBOT", "ROBOT_BIN"):
        v = os.environ.get(var)
        if v and Path(v).exists():
            return v
    on_path = shutil.which("robot")
    if on_path:
        return on_path
    for rel in (
        REPO_ROOT.parent / "kg-microbe/data/raw/robot",
        REPO_ROOT.parent.parent / "kg-microbe/data/raw/robot",
    ):
        if rel.exists():
            return str(rel)
    return None


def run(cmd: list[str]) -> None:
    print(f"  $ {' '.join(cmd)}", file=sys.stderr)
    subprocess.run(cmd, check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cohort_dir", type=Path)
    ap.add_argument("--out", type=Path, default=None,
                    help="Directory for OWL artifacts (default: reports/robot/<cohort>/).")
    ap.add_argument("--no-merge-metpo", action="store_true",
                    help="Skip the merge-with-local-metpo.owl step.")
    ap.add_argument("--metpo", type=Path, default=DEFAULT_METPO,
                    help=f"Path to METPO snapshot (default: {DEFAULT_METPO.relative_to(REPO_ROOT)}).")
    args = ap.parse_args()

    cohort_dir = args.cohort_dir
    if not cohort_dir.is_dir():
        print(f"error: not a directory: {cohort_dir}", file=sys.stderr)
        return 2

    classes_tsv = cohort_dir / "metpo_proposal_classes_robot.tsv"
    props_tsv = cohort_dir / "metpo_proposal_properties_robot.tsv"
    if not classes_tsv.exists() and not props_tsv.exists():
        print(f"error: no proposal TSVs in {cohort_dir}", file=sys.stderr)
        return 2

    robot = find_robot()
    if robot is None:
        print(
            "error: robot binary not found.\n"
            "  Set ROBOT=/path/to/robot, put robot on PATH, or ensure\n"
            "  ../kg-microbe/data/raw/robot exists (canonical local layout).",
            file=sys.stderr,
        )
        return 2

    out_dir = args.out or (REPO_ROOT / "reports/robot" / cohort_dir.name)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Robot:    {robot}", file=sys.stderr)
    print(f"Cohort:   {cohort_dir}", file=sys.stderr)
    print(f"Outputs:  {out_dir}", file=sys.stderr)

    inputs_to_merge: list[Path] = []

    if classes_tsv.exists():
        classes_owl = out_dir / "classes.owl"
        run([robot, "template", "--template", str(classes_tsv), *PREFIXES,
             "--output", str(classes_owl)])
        inputs_to_merge.append(classes_owl)

    if props_tsv.exists():
        props_owl = out_dir / "props.owl"
        run([robot, "template", "--template", str(props_tsv), *PREFIXES,
             "--output", str(props_owl)])
        inputs_to_merge.append(props_owl)

    if not args.no_merge_metpo:
        if not args.metpo.exists():
            print(f"  WARN: --metpo {args.metpo} not found; skipping merge", file=sys.stderr)
        else:
            inputs_to_merge.insert(0, args.metpo)

    merged_owl = out_dir / "merged.owl"
    merge_cmd = [robot, "merge"]
    for inp in inputs_to_merge:
        merge_cmd += ["--input", str(inp)]
    merge_cmd += ["--output", str(merged_owl)]
    run(merge_cmd)

    reasoned_owl = out_dir / "reasoned.owl"
    run([
        robot, "reason",
        "--reasoner", "ELK",
        "--input", str(merged_owl),
        "--axiom-generators", "SubClass EquivalentClass",
        "--output", str(reasoned_owl),
    ])

    merged_lines = sum(1 for _ in merged_owl.open())
    reasoned_lines = sum(1 for _ in reasoned_owl.open())
    delta = reasoned_lines - merged_lines

    print("", file=sys.stderr)
    print("=== robot-validate-proposal summary ===", file=sys.stderr)
    print(f"  merged.owl lines:    {merged_lines}", file=sys.stderr)
    print(f"  reasoned.owl lines:  {reasoned_lines}", file=sys.stderr)
    print(f"  delta:               {delta:+d}", file=sys.stderr)
    if delta > 200:
        print("  WARN: large delta may indicate unintended inferred equivalences", file=sys.stderr)
    print("  status:              PASS (no UNSAT, ELK exited 0)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
