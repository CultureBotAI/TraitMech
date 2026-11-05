"""label-correspondence.yaml calls claw at the governance pin (#2067).

The workflow says to keep its claw ref at scripts/.vendored_canon_ref, and the
ref drifted once with nothing to notice: the pin moved and this call did not.
A re-pin that leaves this ref behind now fails here. claw's
`kg-microbe-governance pin-coupling` also reports the outgoing pin in this
file, so the re-pin commit knows to change both.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CALL = re.compile(
    r"^\s*uses:\s*CultureBotAI/culturebotai-claw/\.github/workflows/"
    r"label-correspondence-reusable\.yaml@(\S+)\s*$",
    re.MULTILINE,
)


def test_the_reusable_workflow_is_called_at_the_governance_pin() -> None:
    workflow = (ROOT / ".github/workflows/label-correspondence.yaml").read_text(encoding="utf-8")
    pin = (ROOT / "scripts/.vendored_canon_ref").read_text(encoding="utf-8").strip()
    refs = CALL.findall(workflow)
    assert len(refs) == 1, f"expected one call to the reusable workflow, found {refs}"
    assert re.fullmatch(r"[0-9a-f]{40}", pin), pin
    assert refs[0] == pin, f"label-correspondence calls claw at {refs[0]}, but the pin is {pin}"
