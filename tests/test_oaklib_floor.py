"""Keep `sqlite:obo:` off the retiring semantic-sql S3 bucket (#562, #568).

At oaklib 0.7.1 and below, `sqlite:obo:` selectors resolve against
``https://s3.amazonaws.com/bbop-sqlite``, whose public access INCATools is
retiring. 0.7.2 moved the default to ``SEMSQL_SQLITE_URL_BASE``. This repo
reaches OAK from `just validate-products` (a blocking CI gate) and from
`scripts/audit_canonical_examples.py`, so anything that puts those back on the
bucket breaks both the moment it goes away.

The reversion is invisible until it is catastrophic: on 0.6.23 every lookup
still succeeds today, so nothing distinguishes a correct pin from a reverted
one right up until every lookup fails at once.

Two layers, because each covers what the other cannot:

* **Declaration** (`test_oaklib_floor_*`, `test_the_lock_*`) — the floor in
  pyproject.toml and the lock agreeing with it. This is what we control, and
  what a routine "relax the constraints" edit would quietly undo. Asserting
  the declared floor rather than the installed version is deliberate: the lock
  is regenerable, and the declaration is what binds a fresh install.
* **Runtime** (`test_the_resolved_default_*`, `test_the_download_path_*`) —
  the value oaklib will actually resolve against, and that its downloader
  still reads that value. This is what we care about, and it survives upstream
  renaming the constant, re-defaulting it, or shipping a version whose number
  implies a fix it does not contain (#568).

A version number is a proxy; the resolved URL is the property.
"""

from __future__ import annotations

import ast
import importlib
import inspect
import re
from pathlib import Path

from packaging.requirements import Requirement
from packaging.version import Version

REPO_ROOT = Path(__file__).resolve().parent.parent

# The first release carrying the CDN default. Anything below reintroduces #562.
CDN_DEFAULT_FIRST_RELEASE = Version("0.7.2")

# Match the whole domain, not one host spelling: a virtual-hosted, region
# qualified URL such as https://bbop-sqlite.s3.us-east-1.amazonaws.com is the
# same bucket and would slip past a check for "s3.amazonaws.com" alone.
S3_DOMAIN = ".amazonaws.com"
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


def _string_literals(module) -> set[str]:
    """Return the string literals in ``module``'s live code.

    Parsed rather than grepped, because a substring search cannot tell live
    code from a comment. oaklib's constants.py names the override variable
    twice — once in live code and once in a prose comment above it — so an
    upstream rename that left the comment stale would satisfy a text search
    while breaking the thing being asserted (#576).
    """
    tree = ast.parse(inspect.getsource(module))
    return {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }


def _calls_named(module, name: str) -> list[str]:
    """Return live call sites of ``name`` in ``module``, ignoring comments.

    The previous line-scan treated every non-``#`` line as live code, so a
    docstring merely MENTIONING the call failed the test, while a call
    assembled through getattr slipped past it (#576).
    """
    tree = ast.parse(inspect.getsource(module))
    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr == name:
            found.append(f"attribute access at line {node.lineno}")
        elif isinstance(node, ast.Name) and node.id == name:
            found.append(f"name reference at line {node.lineno}")
    return found


def _shipped_default(monkeypatch) -> str:
    """Return the URL base oaklib ships, ignoring any local override.

    ``SEMSQL_SQLITE_URL_BASE`` is ``os.environ.get(OVERRIDE_ENV, CDN)`` evaluated
    at import time, so a developer or CI job that sets a mirror would otherwise
    have this test assert their override instead of the shipped default — and a
    reverted default would pass unnoticed behind it (#568).

    The reload leaves ``oaklib.constants`` holding the un-overridden value for
    the rest of the session. Nothing in this repo reads that attribute under
    pytest, and oaklib's downloader binds its own copy at import, so this is
    inert today — but it is why the helper stays confined to these tests.
    """
    monkeypatch.delenv(OVERRIDE_ENV, raising=False)
    constants = importlib.import_module("oaklib.constants")
    assert OVERRIDE_ENV in _string_literals(constants), (
        f"oaklib no longer reads {OVERRIDE_ENV} in live code; clearing it "
        "above is now a no-op, so this test would silently assert the ambient "
        "environment rather than the shipped default"
    )
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
    assert S3_DOMAIN not in shipped, (
        f"oaklib resolves sqlite:obo: against {shipped}, the raw S3 bucket "
        "INCATools/semantic-sql is retiring (semantic-sql#112, #562)"
    )
    assert shipped.startswith("https://"), shipped


def test_the_download_path_actually_uses_the_constant():
    """A correct constant is worthless if the downloader stopped reading it.

    oaklib builds the URL as f"{SEMSQL_SQLITE_URL_BASE}/{prefix}.db.gz". If a
    future release inlined a host there instead, every assertion above would
    still pass while `sqlite:obo:` went back to the bucket.

    This asserts the constant is INTERPOLATED, not merely imported. oaklib's
    source carries the pre-0.7.2 call commented out beside the current one
    (``ensure_from_s3(s3_bucket="bbop-sqlite", ...)``, labelled "Option 2"), so
    the cheapest possible revert is a two-line comment swap that leaves the now
    unused import in place — which a mention-only check would wave through.
    """
    module = importlib.import_module(
        "oaklib.implementations.sqldb.sql_implementation"
    )
    source = inspect.getsource(module)

    assert "{SEMSQL_SQLITE_URL_BASE}/" in source, (
        "oaklib's sqlite implementation no longer interpolates "
        "SEMSQL_SQLITE_URL_BASE into the download URL. The likely cause is a "
        "BENIGN upstream refactor — urljoin(), or binding the base to a local "
        "first — which still resolves against the CDN. Before relaxing this "
        "assertion, check the value the other tests here assert and confirm "
        "the resolved URL: the failure this guards is the pre-0.7.2 S3 call "
        "being re-enabled, which looks the same from here (#577)."
    )

    # Not a substring scan: a docstring merely mentioning the call used to fail
    # this, and a getattr-assembled call used to pass it (#576).
    live = _calls_named(module, "ensure_from_s3")
    assert not live, (
        "oaklib's sqlite implementation references ensure_from_s3 in live "
        f"code; the pre-0.7.2 raw-bucket path appears to be re-enabled: {live}"
    )

    # Restored: 8cc97120 dropped this while its message described the change as
    # a widening. Without it, ADDING an inlined S3 URL below the interpolated
    # line passes every other assertion here, because the constant is still
    # present — just dead (#575).
    assert S3_DOMAIN not in source, (
        f"oaklib's sqlite implementation names {S3_DOMAIN} directly; an S3 URL "
        "may have been added alongside the CDN interpolation rather than "
        "replacing it"
    )
