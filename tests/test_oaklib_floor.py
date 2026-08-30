"""Keep the oaklib floor at the repository's deliberate policy minimum.

At oaklib 0.7.1 and below, `sqlite:obo:` selectors resolve against
``https://s3.amazonaws.com/bbop-sqlite``, whose public access INCATools is
retiring. 0.7.2 moved the default to ``SEMSQL_SQLITE_URL_BASE``; the repository
deliberately chose 0.7.3 for fleet consistency and wider upstream Python
metadata (#569/#572). This repo
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
from pathlib import Path

from packaging.requirements import Requirement
from packaging.version import Version

REPO_ROOT = Path(__file__).resolve().parent.parent

# 0.7.2 is the first CDN-default release, but 0.7.3 is the declared policy
# floor. Guard the actual decision so lowering the declaration cannot pass by
# satisfying only the narrower raw-S3 invariant (#572).
MIN_OAKLIB = Version("0.7.3")


def _declared(name: str) -> Requirement:
    """Return the declared requirement for ``name``.

    Parsed from the raw text rather than with ``tomllib``, which is stdlib only
    from 3.11 while this project supports 3.10 — the same reason
    ``test_python_support.py`` reads pyproject with a regex.
    """
    text = (REPO_ROOT / "pyproject.toml").read_text()
    body = text.split("dependencies = [", 1)[-1].split("]", 1)[0]
    for raw in re.findall(r'"([^"]+)"', body):
        req = Requirement(raw)
        if req.name == name:
            return req
    raise AssertionError(f"{name} is not a declared dependency")


def test_oaklib_floor_matches_the_declared_policy_minimum():
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
    assert min(floors) >= MIN_OAKLIB, (
        f"oaklib floor {min(floors)} is below the {MIN_OAKLIB} policy floor; "
        "0.7.2 fixes raw-S3 resolution but does not match the fleet decision (#572)"
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
    assert Version(locked) >= MIN_OAKLIB
