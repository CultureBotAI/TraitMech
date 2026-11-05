"""label-correspondence.yaml calls claw at the governance pin (#2067).

The workflow says to keep its claw ref at scripts/.vendored_canon_ref, and the
ref drifted once with nothing to notice: the pin moved and this call did not.
A re-pin that leaves a claw ref behind now fails here. claw's
`kg-microbe-governance pin-coupling` also reports the outgoing pin in this
file, so the re-pin commit knows to change both.

The workflow is parsed as YAML, not matched line by line, so quoting a call or
commenting it neither hides a stale ref nor breaks the check (#2077). GitHub
resolves a call's owner and repository case-insensitively, so they are compared
that way; the path and ref are compared exactly (#2078).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CLAW = "CultureBotAI/culturebotai-claw/"
REUSABLE = CLAW + ".github/workflows/label-correspondence-reusable.yaml"


def _canonical(uses: str) -> str:
    """`uses` with its owner and repository in one case, as GitHub resolves them."""
    parts = uses.split("/", 2)
    if len(parts) < 3:
        return uses
    owner, repository, rest = parts
    return f"{owner.lower()}/{repository.lower()}/{rest}"


def claw_calls(workflow_text: str) -> list[str]:
    """Every job- or step-level `uses` naming culturebotai-claw, as written."""
    document = yaml.safe_load(workflow_text)
    calls = []
    for job in (document.get("jobs") or {}).values():
        if not isinstance(job, dict):
            continue
        for uses in [job.get("uses")] + [step.get("uses") for step in job.get("steps") or []
                                         if isinstance(step, dict)]:
            if isinstance(uses, str) and _canonical(uses).startswith(_canonical(CLAW)):
                calls.append(uses)
    return calls


def problems(workflow_text: str, pin: str) -> list[str]:
    calls = claw_calls(workflow_text)
    found = [f"{call} is not at the pin {pin}" for call in calls if call.rpartition("@")[2] != pin]
    reusable = [call for call in calls if _canonical(call).rpartition("@")[0] == _canonical(REUSABLE)]
    if len(reusable) != 1:
        found.append(f"expected one call to {REUSABLE}, found {len(reusable)}")
    return found


def test_the_reusable_workflow_is_called_at_the_governance_pin() -> None:
    workflow = (ROOT / ".github/workflows/label-correspondence.yaml").read_text(encoding="utf-8")
    pin = (ROOT / "scripts/.vendored_canon_ref").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"[0-9a-f]{40}", pin), pin
    assert problems(workflow, pin) == []


PIN = "a" * 40
OLD = "b" * 40
GOOD = f"""
jobs:
  label-correspondence:
    uses: {REUSABLE}@{PIN}
"""


@pytest.mark.parametrize("text,expected", [
    (GOOD, []),
    # Quoted, or carrying a comment, the one correct call still counts (#2077).
    (GOOD.replace(f"{REUSABLE}@{PIN}", f'"{REUSABLE}@{PIN}"'), []),
    (GOOD.replace(f"{REUSABLE}@{PIN}", f"{REUSABLE}@{PIN}  # the pin"), []),
    # A stale second call is found however it is written (#2077).
    (GOOD + f'  second:\n    uses: "{REUSABLE}@{OLD}"\n',
     [f"{REUSABLE}@{OLD} is not at the pin {PIN}", f"expected one call to {REUSABLE}, found 2"]),
    (GOOD + f"  second:\n    uses: {REUSABLE}@{OLD}  # old\n",
     [f"{REUSABLE}@{OLD} is not at the pin {PIN}", f"expected one call to {REUSABLE}, found 2"]),
    # GitHub resolves the owner and repository case-insensitively (#2078).
    (GOOD + f"  second:\n    uses: {REUSABLE.lower()}@{OLD}\n",
     [f"{REUSABLE.lower()}@{OLD} is not at the pin {PIN}", f"expected one call to {REUSABLE}, found 2"]),
    (GOOD.replace("CultureBotAI/culturebotai-claw", "CULTUREBOTAI/CultureBotAI-Claw"), []),
    # Another claw file called at a stale ref, in a step, is a coupling too.
    (GOOD + f"  other:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: {CLAW}.github/actions/x@{OLD}\n",
     [f"{CLAW}.github/actions/x@{OLD} is not at the pin {PIN}"]),
    ("jobs: {}\n", [f"expected one call to {REUSABLE}, found 0"]),
])
def test_every_claw_call_is_found_however_it_is_written(text: str, expected: list[str]) -> None:
    assert problems(text, PIN) == expected
