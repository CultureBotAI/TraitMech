#!/usr/bin/env python3
"""Fail if the justfile names a Python file that is not tracked in git.

A `just` recipe only fails when someone invokes it, so a recipe pointing at an
untracked script is invisible to every other gate: tests pass, validation
passes, `just qc` passes, and the breakage surfaces only when a colleague on a
clean checkout runs the recipe and gets `can't open file ...`.

This has happened twice, both times from `git add justfile` sweeping up
working-tree edits that belonged to someone else's in-progress branch:

  * three `research-trait-edison*` / `enrich-edison-response` recipes invoking
    scripts that were never committed;
  * `VENDORED_IDLABEL_FILES` listing two files that did not exist in the repo,
    which broke `just refresh-validator-pin` (the pin *verify* recipe reads a
    checksum file, so CI stayed green).

Scope is deliberately narrow: `scripts/**.py` and `tests/**.py` tokens. Those
are the files recipes execute or checksum, and the class of reference that is
load-bearing at run time. It excludes:

  * paths under `../` — sibling Mech repos and other out-of-tree tooling, whose
    presence this repo cannot assert;
  * non-Python data/config/output paths — some are generated (
    `src/traitmech/schema/traitmech_dataclasses.py` is a `gen-schema` output)
    and legitimately absent from git.

Exits 1 and lists every offender, so an accidental sweep fails fast in CI
instead of at a colleague's terminal.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JUSTFILE = REPO_ROOT / "justfile"

# scripts/… or tests/… ending in .py. Any occurrence counts: recipe bodies,
# just variables (VENDORED_IDLABEL_FILES), and comments alike -- a stale path in
# a comment is a documentation bug worth the same one-line fix.
PATH_RE = re.compile(r"(?<![\w./-])((?:scripts|tests)/[\w./-]+\.py)")

# A token preceded by "../" belongs to a sibling repo, not this one.
EXTERNAL_RE = re.compile(r"\.\./[\w./-]*$")


def referenced_paths(text: str) -> set[str]:
    """Every in-repo scripts//tests/ Python path the justfile names."""
    found = set()
    for match in PATH_RE.finditer(text):
        if EXTERNAL_RE.search(text[: match.start()]):
            continue
        found.add(match.group(1))
    return found


def tracked_paths() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "scripts", "tests"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return set(out.split())


def main(argv: list[str] | None = None) -> int:
    # Takes argv explicitly so callers (and tests) never depend on the ambient
    # sys.argv -- under pytest that is the pytest command line.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--justfile", type=Path, default=JUSTFILE)
    args = parser.parse_args(argv)

    referenced = referenced_paths(args.justfile.read_text())
    tracked = tracked_paths()
    untracked = sorted(referenced - tracked)

    print("=== justfile path audit ===")
    print(f"  scripts//tests/ Python paths referenced: {len(referenced)}")
    print(f"  not tracked in git:                     {len(untracked)}")

    if untracked:
        print("\nThe justfile references files that are not committed. On a clean")
        print("checkout every recipe using them fails. Either commit the file or")
        print("remove the reference -- they belong in the same commit.\n")
        for path in untracked:
            exists = (REPO_ROOT / path).exists()
            why = "untracked (present in your working tree only)" if exists else "does not exist"
            print(f"  {path}  --  {why}")
        return 1

    print("\nAll justfile-referenced scripts/tests are tracked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
