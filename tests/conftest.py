"""Shared pytest fixtures for TraitMech.

The credential isolation below exists because a test that reads a credential
variable is only testing the developer's shell otherwise: the same test passes on
a clean machine and fails on a provisioned one, or vice versa, and the failure
output prints the real secret into the terminal and CI log.
"""

from __future__ import annotations

import pytest

# Every variable that any code path consults when resolving a research
# credential. Kept together so adding a provider means adding one entry here.
CREDENTIAL_ENV_VARS = (
    "EDISON_API_KEY",
    "EDISON_PLATFORM_API_KEY",
    "FUTUREHOUSE_API_KEY",
    "CBORG_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENAI_API_KEY",
    "ROSALIND_API_KEY",
    # Not a credential, but it selects the GPT-Rosalind model id and a
    # developer's override must not leak into command-shape assertions.
    "ROSALIND_MODEL",
)


@pytest.fixture(autouse=True)
def isolate_credential_env(monkeypatch):
    """Clear provider credentials so tests never inherit the ambient shell.

    Autouse and unconditional: a test that needs one sets it explicitly, which
    also documents which credential that test is actually about. Without this,
    ``research_env`` tests silently depended on whether the developer happened to
    have ``EDISON_PLATFORM_API_KEY`` exported — which is exactly how the
    provider-aware fallback bug stayed hidden.
    """
    for name in CREDENTIAL_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
