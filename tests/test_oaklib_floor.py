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

import importlib
import re
from pathlib import Path

from packaging.requirements import Requirement
from packaging.version import Version

REPO_ROOT = Path(__file__).resolve().parent.parent

# The first release carrying the CDN default. Anything below reintroduces #562.
CDN_DEFAULT_FIRST_RELEASE = Version("0.7.2")

S3_HOST = "s3.amazonaws.com"
OVERRIDE_ENV = "OAKLIB_SEMSQL_SQLITE_URL_BASE"


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


def _shipped_default(monkeypatch) -> str:
    """Return the URL base oaklib ships, ignoring any local override.

    ``SEMSQL_SQLITE_URL_BASE`` is ``os.environ.get(OVERRIDE_ENV, CDN)`` evaluated
    at import time, so a developer or CI job that sets a mirror would otherwise
    have this test assert their override instead of the shipped default — and a
    reverted default would pass unnoticed behind it (#568).
    """
    monkeypatch.delenv(OVERRIDE_ENV, raising=False)
    constants = importlib.import_module("oaklib.constants")
    return importlib.reload(constants).SEMSQL_SQLITE_URL_BASE


def test_the_resolved_default_is_not_the_retiring_bucket(monkeypatch):
    """Pin the property, not a proxy for it (#568).

    The two tests above track a version number, which is what we control but not
    what we care about. This reads the value oaklib will actually resolve
    `sqlite:obo:` against, so it keeps working if upstream renames the constant,
    changes its default again, or ships a version whose number implies a fix it
    does not contain.
    """
    shipped = _shipped_default(monkeypatch)
    assert S3_HOST not in shipped, (
        f"oaklib resolves sqlite:obo: against {shipped}, the raw S3 bucket "
        "INCATools/semantic-sql is retiring (semantic-sql#112, #562)"
    )
    assert shipped.startswith("https://"), shipped


def test_the_download_path_actually_uses_the_constant(monkeypatch):
    """A correct constant is worthless if the downloader stopped reading it.

    oaklib builds the URL as f"{SEMSQL_SQLITE_URL_BASE}/{prefix}.db.gz". If a
    future release inlined a host there instead, every assertion above would
    still pass while `sqlite:obo:` went back to the bucket.
    """
    import inspect

    module = importlib.import_module(
        "oaklib.implementations.sqldb.sql_implementation"
    )
    source = inspect.getsource(module)
    assert "SEMSQL_SQLITE_URL_BASE" in source, (
        "oaklib's sqlite implementation no longer references "
        "SEMSQL_SQLITE_URL_BASE; the download host may be hardcoded again"
    )
    assert S3_HOST not in source, (
        f"oaklib's sqlite implementation mentions {S3_HOST} directly"
    )
