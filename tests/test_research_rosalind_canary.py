"""The GPT-Rosalind canary: every check is exercised with injected seams.

No network, no credential. The canary's whole job is to distinguish "a key is
set" from "this key may call this model", so each way that distinction can
fail gets a test.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import research_rosalind_canary as rc  # noqa: E402
from research_trait import DEFAULT_ROSALIND_MODEL  # noqa: E402


def _ok_client(command, env):
    assert command[-2:] == ["--provider", "openai"]
    assert env.get("OPENAI_API_KEY"), "the client must be probed with the key a run gets"
    return 0, "Provider: openai - Available\n"


def _checks(report):
    return {c["check"]: c["ok"] for c in report["checks"]}


def test_missing_credential_fails_first_and_makes_no_call():
    calls = []
    report = rc.canary({}, list_models=lambda key: calls.append(key) or [],
                       run_client=_ok_client)
    assert report["ok"] is False
    assert _checks(report) == {"credential": False}
    assert calls == []
    assert "ROSALIND_API_KEY" in report["checks"][0]["detail"]


def test_dedicated_key_is_the_one_probed():
    seen = []
    report = rc.canary(
        {"OPENAI_API_KEY": "general", "ROSALIND_API_KEY": "rosalind"},
        list_models=lambda key: seen.append(key) or [DEFAULT_ROSALIND_MODEL],
        run_client=_ok_client,
    )
    assert seen == ["rosalind"]
    assert report["credential"] == "ROSALIND_API_KEY"
    assert report["ok"] is True


def test_a_bare_openai_key_is_not_a_rosalind_credential():
    """#641: the canary must not pass on a key the lane itself will not use."""
    calls = []
    report = rc.canary({"OPENAI_API_KEY": "general"},
                       list_models=lambda key: calls.append(key) or [DEFAULT_ROSALIND_MODEL],
                       run_client=_ok_client)
    assert report["ok"] is False
    assert _checks(report) == {"credential": False}
    assert calls == []


def test_allow_unlisted_turns_the_model_check_into_a_warning():
    """#645: for a key known to be entitled, when the listing may not
    enumerate the gated preview at all."""
    report = rc.canary({"ROSALIND_API_KEY": "k"}, list_models=lambda key: ["gpt-5"],
                       run_client=_ok_client, allow_unlisted=True)
    assert report["ok"] is True
    assert _checks(report)["model"] is True
    assert "WARNING" in next(c for c in report["checks"] if c["check"] == "model")["detail"]


def test_authentication_failure_is_reported_without_the_key():
    def boom(key):
        raise RuntimeError(f"401 for {key}")

    report = rc.canary({"ROSALIND_API_KEY": "sk-secret-value"}, list_models=boom,
                       run_client=_ok_client)
    assert _checks(report) == {"credential": True, "authenticate": False}
    assert "sk-secret-value" not in json.dumps(report)
    assert "<redacted>" in report["checks"][-1]["detail"]


def test_model_absent_is_the_trusted_access_finding():
    report = rc.canary({"ROSALIND_API_KEY": "k"},
                       list_models=lambda key: ["gpt-5", "o3-deep-research-2025-06-26"],
                       run_client=_ok_client)
    assert _checks(report) == {"credential": True, "authenticate": True, "model": False}
    assert "trusted access" in report["checks"][-1]["detail"]
    assert report["rosalind_models_visible"] == []


def test_a_renamed_preview_id_is_surfaced_for_rosalind_model():
    report = rc.canary({"ROSALIND_API_KEY": "k"},
                       list_models=lambda key: ["gpt-rosalind-2026-08-01"],
                       run_client=_ok_client)
    assert _checks(report)["model"] is False
    assert report["rosalind_models_visible"] == ["gpt-rosalind-2026-08-01"]
    assert "ROSALIND_MODEL" in report["checks"][-1]["detail"]


def test_rosalind_model_override_is_what_gets_checked():
    report = rc.canary({"ROSALIND_API_KEY": "k", "ROSALIND_MODEL": "gpt-rosalind-2026-08-01"},
                       list_models=lambda key: ["gpt-rosalind-2026-08-01"],
                       run_client=_ok_client)
    assert report["model"] == "gpt-rosalind-2026-08-01"
    assert report["model_source"] == "ROSALIND_MODEL"
    assert report["ok"] is True


def test_client_not_discovering_openai_fails_the_canary():
    report = rc.canary({"ROSALIND_API_KEY": "k"},
                       list_models=lambda key: [DEFAULT_ROSALIND_MODEL],
                       run_client=lambda cmd, env: (0, "Provider: openai - Not available\n"))
    assert _checks(report)["client"] is False
    assert report["ok"] is False


def test_client_command_is_split_like_a_shell_would():
    seen = []

    def spy(command, env):
        seen.append(command)
        return 0, "Available"

    rc.canary({"ROSALIND_API_KEY": "k"}, list_models=lambda key: [DEFAULT_ROSALIND_MODEL],
              run_client=spy, client_command="uv run deep-research-client")
    assert seen == [["uv", "run", "deep-research-client", "providers", "--provider", "openai"]]


def test_main_exit_code_follows_the_verdict(monkeypatch, capsys):
    monkeypatch.setattr(rc, "canary", lambda env, client_command, allow_unlisted: {
        "provider": "rosalind", "client_provider": "openai", "model": "m",
        "model_source": "default", "credential": None, "checks": [
            {"check": "credential", "ok": False, "detail": "set it"}],
        "rosalind_models_visible": [], "ok": False})
    assert rc.main([]) == 1
    assert "NOT READY" in capsys.readouterr().out
    monkeypatch.setattr(rc, "canary", lambda env, client_command, allow_unlisted: {
        "provider": "rosalind", "client_provider": "openai", "model": "m",
        "model_source": "default", "credential": "OPENAI_API_KEY", "checks": [],
        "rosalind_models_visible": ["m"], "ok": True})
    assert rc.main(["--json"]) == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True
