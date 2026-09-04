#!/usr/bin/env python3
"""Non-billing canary for the GPT-Rosalind deep-research lane.

GPT-Rosalind is OpenAI's life-sciences reasoning model, served as a research
preview to organisations in OpenAI's trusted-access program. TraitMech reaches
it through deep-research-client's `openai` provider with an explicit model id
(see ``research_trait.provider_args``). Two things can therefore be wrong while
every generic check still looks green:

* the credential belongs to an organisation WITHOUT trusted access, so the key
  authenticates and the model call is refused; or
* the model id TraitMech requests is not the id OpenAI currently serves, because
  the preview name was snapshotted or renamed.

This canary answers both without spending anything. Listing models is an
authenticated call that OpenAI does not bill, and it returns exactly the ids the
credential is entitled to use. It then confirms deep-research-client discovers
its `openai` provider under the same environment a real run would get from
``research_trait.research_env``.

It does NOT prove a research call will succeed: quota, rate limits, and the
request shape the lane actually sends (a `developer` message plus the
`web_search_preview` tool) only show up on the first real run, which is why
the docs require one canary trait before any batch. Nor is it settled that a
gated research-preview id appears in the model listing at all (#645); if a key
known to be entitled fails only the `model` check, `--allow-unlisted` turns
that check into a warning so the single real trait can settle it.

No credential value is ever printed; only the NAME of the variable that was
used.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from collections.abc import Callable, Mapping
from typing import Any

from research_trait import (
    ROSALIND_CLIENT_PROVIDER,
    ROSALIND_CREDENTIALS,
    ROSALIND_MODEL_ENV,
    ROSALIND_PROVIDER,
    research_env,
    rosalind_model,
)

ListModels = Callable[[str], list[str]]
RunClient = Callable[[list[str], Mapping[str, str]], tuple[int, str]]


def credential_name(environ: Mapping[str, str]) -> str | None:
    """The first Rosalind credential variable that is set, by name only."""
    for name in ROSALIND_CREDENTIALS:
        if environ.get(name):
            return name
    return None


def _list_models_openai(api_key: str) -> list[str]:
    """Authenticated, unbilled: the ids this key may call."""
    from openai import OpenAI  # deep-research-client dependency; dev extra only

    client = OpenAI(api_key=api_key)
    try:
        return sorted(model.id for model in client.models.list())
    finally:
        client.close()


def _run_client(command: list[str], env: Mapping[str, str]) -> tuple[int, str]:
    completed = subprocess.run(
        command, env=dict(env), capture_output=True, text=True, timeout=120
    )
    return completed.returncode, completed.stdout + completed.stderr


def canary(
    environ: Mapping[str, str],
    *,
    list_models: ListModels = _list_models_openai,
    run_client: RunClient = _run_client,
    client_command: str = "deep-research-client",
    allow_unlisted: bool = False,
) -> dict[str, Any]:
    """Run every check and return a report; ``ok`` is the overall verdict."""
    model = rosalind_model(environ)
    report: dict[str, Any] = {
        "provider": ROSALIND_PROVIDER,
        "client_provider": ROSALIND_CLIENT_PROVIDER,
        "model": model,
        "model_source": ROSALIND_MODEL_ENV if environ.get(ROSALIND_MODEL_ENV) else "default",
        "credential": None,
        "checks": [],
        "rosalind_models_visible": [],
        "ok": False,
    }
    checks = report["checks"]

    name = credential_name(environ)
    report["credential"] = name
    if name is None:
        checks.append(
            {"check": "credential", "ok": False,
             "detail": f"set {' or '.join(ROSALIND_CREDENTIALS)}"}
        )
        return report
    checks.append({"check": "credential", "ok": True, "detail": f"{name} is set"})

    # research_env() is the path a real run takes; probing with anything else
    # would repeat the falcon lesson (preflight green, run unauthenticated).
    run_env = research_env(ROSALIND_PROVIDER, environ)
    api_key = run_env.get("OPENAI_API_KEY", "")

    try:
        ids = list_models(api_key)
    except Exception as exc:  # noqa: BLE001 - any SDK/network failure is the finding
        checks.append({"check": "authenticate", "ok": False,
                       "detail": f"{type(exc).__name__}: {_scrub(str(exc), api_key)}"})
        return report
    checks.append({"check": "authenticate", "ok": True,
                   "detail": f"{len(ids)} model ids visible (unbilled call)"})

    visible = [i for i in ids if "rosalind" in i.lower()]
    report["rosalind_models_visible"] = visible
    if model in ids:
        checks.append({"check": "model", "ok": True, "detail": f"{model} is listed"})
    else:
        hint = (
            f"credential sees {', '.join(visible)}; set {ROSALIND_MODEL_ENV} to one of them"
            if visible
            else "no Rosalind id is visible: this credential's organisation has no "
                 "trusted access, or the key is not the Rosalind key"
        )
        detail = f"{model} is not listed for this credential; {hint}"
        if not allow_unlisted:
            checks.append({"check": "model", "ok": False, "detail": detail})
            return report
        checks.append({"check": "model", "ok": True,
                       "detail": f"WARNING (--allow-unlisted): {detail}"})

    command = [*shlex.split(client_command), "providers", "--provider",
               ROSALIND_CLIENT_PROVIDER]
    try:
        code, output = run_client(command, run_env)
    except Exception as exc:  # noqa: BLE001
        checks.append({"check": "client", "ok": False,
                       "detail": f"could not run {command[0]}: {exc}"})
        return report
    if code or "not available" in output.casefold():
        checks.append({"check": "client", "ok": False,
                       "detail": f"{command[0]} does not report {ROSALIND_CLIENT_PROVIDER} "
                                 "as available under research_env()"})
        return report
    checks.append({"check": "client", "ok": True,
                   "detail": f"{command[0]} discovers {ROSALIND_CLIENT_PROVIDER} under research_env()"})
    report["ok"] = True
    return report


# OpenAI's 401 body echoes the key MASKED -- `at-Jk6S****zMaI` -- which still
# leaks its prefix and suffix. Seen live on the first real canary (#647).
_MASKED_KEY_RE = re.compile(r"\S*\*{3,}\S*")
_KEY_ECHO_RE = re.compile(r"(Incorrect API key provided:)\s*\S+")


def _scrub(text: str, secret: str) -> str:
    """Belt and braces: an SDK message must never carry the key into a log.

    Removes the full key, any masked rendering of it, and the fragment OpenAI
    places after "Incorrect API key provided:".
    """
    if secret:
        text = text.replace(secret, "<redacted>")
    text = _KEY_ECHO_RE.sub(r"\1 <redacted>", text)
    return _MASKED_KEY_RE.sub("<redacted>", text)


def print_report(report: Mapping[str, Any]) -> None:
    print(f"GPT-Rosalind canary: provider `{report['provider']}` -> "
          f"deep-research-client `{report['client_provider']}` --model {report['model']} "
          f"({report['model_source']})")
    for check in report["checks"]:
        label = "PASS" if check["ok"] else "FAIL"
        print(f"  {label} {check['check']}: {check['detail']}")
    if report["rosalind_models_visible"]:
        print(f"  Rosalind ids visible to this credential: "
              f"{', '.join(report['rosalind_models_visible'])}")
    if report["ok"]:
        print("  OK: credential, model, and client all agree. Nothing here was billed; "
              "run ONE trait before any batch.")
    else:
        print("  NOT READY: fix the first FAIL above before running any trait.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    parser.add_argument(
        "--allow-unlisted", action="store_true",
        help="Warn instead of failing when the model id is absent from the "
             "listing; for a key known to be entitled (#645)",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])
    report = canary(os.environ, client_command=args.client_command,
                    allow_unlisted=args.allow_unlisted)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
