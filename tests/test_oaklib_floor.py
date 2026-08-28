"""Keep the oaklib floor above the raw-S3 code path (#562).

At oaklib 0.7.1 and below, `sqlite:obo:` selectors resolve against
``https://s3.amazonaws.com/bbop-sqlite``, whose public access INCATools is
retiring. 0.7.2 moved the default to ``SEMSQL_SQLITE_URL_BASE``. This repo
reaches OAK from `just validate-products` (a blocking CI gate) and from
`scripts/audit_canonical_examples.py`, so a floor that admits <=0.7.1 puts
both back on a bucket that is going away.

Nothing else guards that. The floor lives in one line of pyproject.toml, and
a routine "relax the constraints" edit would silently undo the fix without
failing any other check — the sibling repo added the same guard for the same
reason (CultureMech#365). This asserts the declared floor, not the resolved
version, because the lock can be regenerated while the declaration is what
binds a fresh install.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

from packaging.requirements import Requirement
from packaging.version import Version

REPO_ROOT = Path(__file__).resolve().parent.parent

# The first release carrying the CDN default. Anything below reintroduces #562.
CDN_DEFAULT_FIRST_RELEASE = Version("0.7.2")


def _declared(name: str) -> Requirement:
    data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    for raw in data["project"]["dependencies"]:
        req = Requirement(raw)
        if req.name == name:
            return req
    raise AssertionError(f"{name} is not a declared dependency")


def test_oaklib_floor_excludes_the_raw_s3_code_path():
    req = _declared("oaklib")
    floors = [
        Version(spec.version)
        for spec in req.specifier
        if spec.operator in (">=", "==", "~=")
    ]
    assert floors, (
        f"oaklib is declared as {req!s} with no lower bound; a bare or "
        "upper-bound-only specifier admits 0.7.1 and below, which resolve "
        "sqlite:obo: against the retiring raw S3 bucket (#562)"
    )
    assert min(floors) >= CDN_DEFAULT_FIRST_RELEASE, (
        f"oaklib floor {min(floors)} is below {CDN_DEFAULT_FIRST_RELEASE}, "
        "which reintroduces the raw-S3 resolution path (#562)"
    )


def test_the_lock_satisfies_the_declared_floor():
    req = _declared("oaklib")
    lock = (REPO_ROOT / "uv.lock").read_text()
    match = re.search(r'name = "oaklib"\nversion = "([^"]+)"', lock)
    assert match, "oaklib is not present in uv.lock"
    locked = match.group(1)
    assert req.specifier.contains(locked), (
        f"uv.lock pins oaklib {locked}, which does not satisfy the declared "
        f"{req!s}; the lock and the declaration have drifted"
    )
    assert Version(locked) >= CDN_DEFAULT_FIRST_RELEASE
