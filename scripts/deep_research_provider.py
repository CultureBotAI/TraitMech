#!/usr/bin/env python3
"""Triage deep-research providers for a Mech-specific research focus.

The provider facts mirror deep-research-client/DisMech, while the YAML profile
keeps each Mech's evidence target, sources, and stage weights local to that KB.
No provider is called and no credential value is read or printed.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Provider:
    name: str
    label: str
    source_scope: str
    synthesis: str
    cost: str
    time: str
    capabilities: frozenset[str]
    best_for: str
    limitation: str


PROVIDERS: dict[str, Provider] = {
    "asta": Provider(
        "asta",
        "Asta",
        "scientific corpus",
        "none",
        "low",
        "fast",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "snippets",
            }
        ),
        "fast paper and passage discovery",
        "retrieval packet only; no narrative synthesis",
    ),
    "falcon": Provider(
        "falcon",
        "Edison / Falcon",
        "scientific literature",
        "deep",
        "high",
        "slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
            }
        ),
        "scientific evidence synthesis",
        "academic sources only; paid and slower",
    ),
    "openscientist": Provider(
        "openscientist",
        "OpenScientist",
        "PubMed and scientific literature",
        "agentic",
        "high",
        "very_slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "hypothesis_tracking",
            }
        ),
        "iterative mechanism and hypothesis research",
        "long-running and PubMed-focused",
    ),
    "claude_code": Provider(
        "claude_code",
        "Claude Code",
        "open web",
        "agentic",
        "medium",
        "slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "structured_databases",
            }
        ),
        "broad web/database source coverage",
        "quality depends on web access and local CLI authentication",
    ),
    "openai": Provider(
        "openai",
        "OpenAI Deep Research",
        "open web",
        "deep",
        "very_high",
        "very_slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "real_time_data",
                "structured_databases",
            }
        ),
        "comprehensive multi-source synthesis",
        "highest cost and long response times",
    ),
    "perplexity": Provider(
        "perplexity",
        "Perplexity",
        "open web",
        "deep",
        "high",
        "slow",
        frozenset(
            {
                "web_search",
                "citation_tracking",
                "synthesis",
                "real_time_data",
                "multi_language",
                "structured_databases",
            }
        ),
        "current web research with source links",
        "less specialized for primary scientific evidence",
    ),
    "consensus": Provider(
        "consensus",
        "Consensus",
        "peer-reviewed literature",
        "summary",
        "low",
        "fast",
        frozenset({"academic_search", "citation_tracking", "scientific_literature"}),
        "quick peer-reviewed evidence checks",
        "limited depth and no general web/database search",
    ),
    "cyberian": Provider(
        "cyberian",
        "Cyberian",
        "agent-selected web and literature",
        "agentic",
        "high",
        "very_slow",
        frozenset(
            {
                "web_search",
                "academic_search",
                "citation_tracking",
                "synthesis",
                "code_interpretation",
                "structured_databases",
            }
        ),
        "custom iterative research workflows",
        "requires local agent tooling and careful authority limits",
    ),
    "cborg": Provider(
        "cborg",
        "CBORG proxy",
        "model-dependent open web",
        "deep",
        "medium",
        "slow",
        frozenset(
            {"web_search", "citation_tracking", "synthesis", "code_interpretation"}
        ),
        "OpenAI-compatible research through the LBL proxy",
        "capabilities depend on the selected proxy model",
    ),
    "mock": Provider(
        "mock",
        "Mock",
        "fixtures",
        "none",
        "low",
        "fast",
        frozenset(),
        "tests and dry runs",
        "never supplies real evidence",
    ),
    "deeper_med": Provider(
        "deeper_med",
        "DeepER-Med",
        "biomedical databases",
        "agentic",
        "high",
        "slow",
        frozenset(
            {
                "academic_search",
                "scientific_literature",
                "citation_tracking",
                "synthesis",
                "structured_databases",
            }
        ),
        "future biomedical evidence workflows",
        "stub: no public API is available",
    ),
}

ALIASES = {"edison": "falcon", "futurehouse": "falcon", "claude-code": "claude_code"}
_ALL_CAPABILITIES = frozenset(
    capability for provider in PROVIDERS.values() for capability in provider.capabilities
)
COST_VALUE = {"low": 1, "medium": 2, "high": 3, "very_high": 4}
TIME_VALUE = {"fast": 1, "medium": 2, "slow": 3, "very_slow": 4}
SYNTHESIS_VALUE = {"none": 0, "summary": 1, "deep": 2, "agentic": 3}


def canonical_provider(name: str) -> str:
    key = name.strip().casefold().replace(" ", "_")
    return ALIASES.get(key, key)


# `configured` is deliberately NOT `available`. A present credential says nothing
# about whether a call will succeed: EDISON_API_KEY authenticates and the account
# then returns 402 Payment Required, so the old wording routed confidently to a
# provider that cannot run. Nothing here probes a provider -- no call is made and
# no credential value is read or printed -- so `configured` is the strongest claim
# this function is entitled to make (#435).
CONFIGURED = "configured"
AVAILABLE = "available"
UNAVAILABLE = "unavailable"
STUB = "stub"

# Statuses that mean "you can try this now", in preference order for routing.
ROUTABLE = (AVAILABLE, CONFIGURED)
PAID_COSTS = frozenset({"high", "very_high"})


def provider_status(
    provider: str, environ: Mapping[str, str] | None = None
) -> tuple[str, str]:
    """Return status and a safe explanation without exposing credential values.

    Returns one of `available` (a local binary or package is present, which is
    checkable without a network call), `configured` (a credential exists but
    usability is unverified), `unavailable`, or `stub`.
    """
    env = os.environ if environ is None else environ
    if provider == "deeper_med":
        return STUB, "no public API"
    if provider == "mock":
        enabled = env.get("ENABLE_MOCK_PROVIDER", "").casefold() in {"1", "true", "yes"}
        return (
            (AVAILABLE, "enabled")
            if enabled
            else (UNAVAILABLE, "set ENABLE_MOCK_PROVIDER=true")
        )
    if provider == "claude_code":
        return (
            (AVAILABLE, "local CLI")
            if shutil.which("claude")
            else (UNAVAILABLE, "claude CLI not found")
        )
    if provider == "cyberian":
        installed = importlib.util.find_spec("cyberian") is not None
        return (
            (AVAILABLE, "local package")
            if installed
            else (UNAVAILABLE, "install the cyberian extra")
        )

    credentials = {
        "asta": ("ASTA_API_KEY",),
        "falcon": ("EDISON_API_KEY", "EDISON_PLATFORM_API_KEY", "FUTUREHOUSE_API_KEY"),
        "openscientist": ("OPENSCIENTIST_API_KEY",),
        "openai": ("OPENAI_API_KEY",),
        "perplexity": ("PERPLEXITY_API_KEY",),
        "consensus": ("CONSENSUS_API_KEY",),
        "cborg": ("CBORG_API_KEY",),
    }
    keys = credentials.get(provider, ())
    if any(env.get(key) for key in keys):
        # Not `available`: see the note above CONFIGURED.
        return CONFIGURED, "credential set; usability unverified"
    return UNAVAILABLE, f"set {' or '.join(keys)}"


def load_config(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Provider profile must be a YAML mapping: {path}")
    focuses = data.get("focuses")
    if not isinstance(focuses, dict) or not focuses:
        raise ValueError("Provider profile requires a non-empty 'focuses' mapping")
    default_focus = data.get("default_focus")
    if default_focus not in focuses:
        raise ValueError(
            f"default_focus {default_focus!r} is not defined under focuses"
        )
    for focus_name, focus in focuses.items():
        if not isinstance(focus, dict) or not isinstance(focus.get("stages"), dict):
            raise ValueError(f"Focus {focus_name!r} requires a 'stages' mapping")
        for stage_name, stage in focus["stages"].items():
            if not isinstance(stage, dict):
                raise ValueError(f"Stage {focus_name}.{stage_name} must be a mapping")
            capabilities = stage.get("capabilities", {})
            if not isinstance(capabilities, dict):
                raise ValueError(
                    f"Stage {focus_name}.{stage_name}.capabilities must be a mapping"
                )
            unknown_caps = {str(cap) for cap in capabilities} - _ALL_CAPABILITIES
            if unknown_caps:
                raise ValueError(
                    f"Stage {focus_name}.{stage_name}.capabilities names unknown "
                    f"capability/ies {sorted(unknown_caps)}; no provider declares them"
                )
            for cap_name, cap_weight in capabilities.items():
                if not isinstance(cap_weight, (int, float)) or isinstance(cap_weight, bool):
                    raise ValueError(
                        f"Stage {focus_name}.{stage_name}.capabilities[{cap_name!r}] "
                        f"must be a number, got {cap_weight!r}"
                    )
            for weight_key in ("synthesis_weight", "speed_weight", "cost_weight"):
                weight = stage.get(weight_key, 0)
                if not isinstance(weight, (int, float)) or isinstance(weight, bool):
                    raise ValueError(
                        f"Stage {focus_name}.{stage_name}.{weight_key} must be a "
                        f"number, got {weight!r}"
                    )
        adjustments = focus.get("provider_adjustments", {})
        if not isinstance(adjustments, dict):
            raise ValueError(
                f"Focus {focus_name!r}.provider_adjustments must be a mapping"
            )
        canonical: dict[str, Any] = {}
        for raw_name, value in adjustments.items():
            name = canonical_provider(str(raw_name))
            if name not in PROVIDERS:
                raise ValueError(
                    f"Focus {focus_name!r}.provider_adjustments names unknown "
                    f"provider {raw_name!r} (resolved to {name!r})"
                )
            if name in canonical:
                raise ValueError(
                    f"Focus {focus_name!r}.provider_adjustments has multiple keys "
                    f"resolving to provider {name!r}"
                )
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValueError(
                    f"Focus {focus_name!r}.provider_adjustments[{raw_name!r}] "
                    f"must be a number, got {value!r}"
                )
            canonical[name] = value
        focus["provider_adjustments"] = canonical
    return data


def _score(
    provider: Provider, stage: Mapping[str, Any], adjustments: Mapping[str, Any]
) -> float:
    capabilities = stage.get("capabilities", {})
    score = sum(
        float(weight)
        for capability, weight in capabilities.items()
        if capability in provider.capabilities
    )
    score += (
        float(stage.get("synthesis_weight", 0)) * SYNTHESIS_VALUE[provider.synthesis]
    )
    score += float(stage.get("speed_weight", 0)) * (5 - TIME_VALUE[provider.time])
    score += float(stage.get("cost_weight", 0)) * (5 - COST_VALUE[provider.cost])
    score += float(adjustments.get(provider.name, 0))
    return score


def rank_stage(
    config: Mapping[str, Any],
    focus_name: str,
    stage_name: str,
    environ: Mapping[str, str] | None = None,
) -> list[dict[str, Any]]:
    focus = config["focuses"][focus_name]
    stage = focus["stages"][stage_name]
    adjustments = focus.get("provider_adjustments", {})
    raw = {
        name: _score(provider, stage, adjustments)
        for name, provider in PROVIDERS.items()
    }
    high = max(raw.values()) or 1.0
    rows = []
    for name, provider in PROVIDERS.items():
        # Threaded, not defaulted: provider_status offers an injectable environ
        # and calling it bare here severed the seam one level below the surface a
        # user sees, so the report's availability column could not be tested
        # deterministically (#436).
        status, reason = provider_status(name, environ)
        rows.append(
            {
                "provider": name,
                "label": provider.label,
                "status": status,
                "status_reason": reason,
                "fit": round(100 * max(0.0, raw[name]) / high),
                "cost": provider.cost,
                "time": provider.time,
                "synthesis": provider.synthesis,
                "source_scope": provider.source_scope,
                "best_for": provider.best_for,
                "limitation": provider.limitation,
            }
        )
    # Preserve relative order when the absolute-zero fit floor collapses
    # several (or all) negative raw scores to fit=0.  The public fit meaning
    # stays unchanged; raw score is only a deterministic tie-breaker.
    return sorted(
        rows,
        key=lambda row: (-row["fit"], -raw[row["provider"]], row["provider"]),
    )


def recommendable(
    rows: list[dict[str, Any]], *, allow: frozenset[str] | None = None,
    no_paid: bool = False,
) -> list[dict[str, Any]]:
    """Return policy-eligible rows while retaining TraitMech status semantics."""
    out = [row for row in rows
           if row["status"] in ROUTABLE and row["provider"] != "mock"]
    if allow is not None:
        out = [row for row in out if row["provider"] in allow]
    if no_paid:
        out = [row for row in out if row["cost"] not in PAID_COSTS]
    return out


def build_report(
    config: Mapping[str, Any],
    focus_name: str,
    environ: Mapping[str, str] | None = None,
    *,
    allow: frozenset[str] | None = None,
    no_paid: bool = False,
) -> dict[str, Any]:
    focus = config["focuses"][focus_name]
    stages = []
    for stage_name, stage in focus["stages"].items():
        ranking = rank_stage(config, focus_name, stage_name, environ)
        routable = recommendable(ranking, allow=allow, no_paid=no_paid)
        stages.append(
            {
                "name": stage_name,
                "objective": stage.get("objective", ""),
                "ranking": ranking,
                "recommended_available": routable[0] if routable else None,
                "fallback_available": routable[1] if len(routable) > 1 else None,
            }
        )
    return {
        "mech": config.get("mech", "Mech"),
        "target": config.get("target", ""),
        "focus": focus_name,
        "focus_label": focus.get("label", focus_name),
        "objective": focus.get("objective", ""),
        "evidence_policy": config.get("evidence_policy", ""),
        "source_priorities": focus.get("source_priorities", []),
        "policy": {
            "allow": sorted(allow) if allow is not None else None,
            "no_paid": no_paid,
        },
        "stages": stages,
    }


FIT_LEGEND = (
    "fit is relative WITHIN this stage: 100 = best of the listed providers for "
    "this stage, not an absolute score. asta scores 100 for discovery while "
    "supplying no synthesis at all."
)


def _table(rows: list[dict[str, Any]]) -> str:
    headers = ("Provider", "Status", "Fit", "Cost", "Time", "Synthesis", "Source scope")
    values = [headers]
    for row in rows:
        values.append(
            (
                row["provider"],
                row["status"],
                str(row["fit"]),
                row["cost"],
                row["time"],
                row["synthesis"],
                row["source_scope"],
            )
        )
    widths = [
        max(len(str(row[index])) for row in values) for index in range(len(headers))
    ]
    lines = [
        "  ".join(
            str(value).ljust(widths[index]) for index, value in enumerate(values[0])
        )
    ]
    lines.append("  ".join("-" * width for width in widths))
    lines.extend(
        "  ".join(str(value).ljust(widths[index]) for index, value in enumerate(row))
        for row in values[1:]
    )
    return "\n".join(lines)


def print_report(report: Mapping[str, Any], provider_name: str | None = None) -> None:
    print(f"{report['mech']} deep-research provider triage")
    print(f"Target: {report['target']}")
    print(f"Focus: {report['focus']} — {report['focus_label']}")
    print(f"Objective: {report['objective']}")
    print(f"Evidence gate: {report['evidence_policy']}")
    print(f"Fit scale: {FIT_LEGEND}")
    if report["source_priorities"]:
        print("Source priorities: " + "; ".join(report["source_priorities"]))

    for stage in report["stages"]:
        print(f"\n[{stage['name']}] {stage['objective']}")
        rows = stage["ranking"]
        if provider_name:
            rows = [row for row in rows if row["provider"] == provider_name]
        print(_table(rows))
        if provider_name and rows:
            row = rows[0]
            print(f"Best for: {row['best_for']}")
            print(f"Limitation: {row['limitation']}")
            print(f"Availability: {row['status_reason']}")
        elif stage["recommended_available"]:
            primary = stage["recommended_available"]
            fallback = stage["fallback_available"]
            message = f"Route now: {primary['provider']} ({primary['best_for']})"
            if fallback:
                message += f"; cross-check/fallback: {fallback['provider']}"
            print(message)
            # Say it out loud rather than leaving the status column to carry it:
            # EDISON_API_KEY authenticates and then 402s, so a routing line that
            # reads as a verified recommendation is the wrong output (#435).
            unverified = [
                row["provider"]
                for row in (primary, fallback)
                if row and row["status"] == CONFIGURED
            ]
            if unverified:
                print(
                    f"  NOTE: {', '.join(unverified)} only has a credential set -- "
                    f"nothing here probed it. A key can authenticate and the "
                    f"account still refuse the call (Edison returns 402 with no "
                    f"credit). Verify before batching."
                )
        elif recommendable(stage["ranking"]):
            print(
                "Route now: no provider passes the current --allow/--no-paid "
                "filters, though at least one is otherwise routable."
            )
        else:
            print(
                "Route now: no real provider is currently available; configure a listed credential or CLI."
            )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", type=Path, required=True, help="Mech provider profile YAML"
    )
    parser.add_argument(
        "--focus", help="Research focus from the profile (default: profile default)"
    )
    parser.add_argument(
        "--provider", help="Show one provider (aliases such as edison are accepted)"
    )
    parser.add_argument(
        "--list-focuses", action="store_true", help="List domain-specific focuses"
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit machine-readable triage JSON"
    )
    parser.add_argument(
        "--allow",
        help="Comma-separated allowlist; only these providers may be recommended",
    )
    parser.add_argument(
        "--no-paid", action="store_true",
        help=f"Never recommend a provider whose cost is {' or '.join(sorted(PAID_COSTS))}",
    )
    return parser



def parse_args(argv: list[str]) -> argparse.Namespace:
    """Kept for callers/tests that parse without going through main()."""
    return _build_parser().parse_args(argv)


class UsageError(ValueError):
    """A bad --focus/--provider: report it as usage, not as a traceback (#437).

    Kept a ValueError subclass so existing callers and tests that expect
    ValueError still pass, while main() can route it through parser.error() for
    a clean exit 2 instead of a stack trace.
    """


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv or sys.argv[1:])
    try:
        return _run(args, parser)
    except UsageError as exc:
        parser.error(str(exc))  # exits 2
        raise  # unreachable; keeps type checkers honest


def _run(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    config = load_config(args.config)
    if args.list_focuses:
        for name, focus in config["focuses"].items():
            marker = " (default)" if name == config["default_focus"] else ""
            print(f"{name}{marker}: {focus.get('label', name)}")
        return 0
    focus_name = args.focus or config["default_focus"]
    if focus_name not in config["focuses"]:
        choices = ", ".join(config["focuses"])
        raise UsageError(f"Unknown focus {focus_name!r}; choose one of: {choices}")
    provider_name = canonical_provider(args.provider) if args.provider else None
    if provider_name and provider_name not in PROVIDERS:
        raise UsageError(
            f"Unknown provider {args.provider!r}; choose one of: {', '.join(PROVIDERS)}"
        )
    allow = (frozenset(canonical_provider(p) for p in args.allow.split(",") if p.strip())
             if args.allow is not None else None)
    if allow is not None:
        if not allow:
            raise UsageError(f"--allow {args.allow!r} did not contain provider names")
        unknown = allow - set(PROVIDERS)
        if unknown:
            raise UsageError(
                f"Unknown provider(s) in --allow: {', '.join(sorted(unknown))}"
            )
        if "mock" in allow:
            raise UsageError("--allow may not include 'mock'")
    report = build_report(config, focus_name, allow=allow, no_paid=args.no_paid)
    if args.json:
        if provider_name:
            # Add `selected`; do NOT filter `ranking`. The routing choice is a
            # property of the STAGE, so filtering the ranking while keeping
            # stage-level `recommended_available` produced a payload naming a
            # provider absent from its own ranking (#450). Keeping the ranking
            # whole also lets a consumer see WHERE the selected provider placed,
            # which is the question a single-provider query is usually asking.
            for stage in report["stages"]:
                stage["selected"] = next(
                    (row for row in stage["ranking"] if row["provider"] == provider_name),
                    None,
                )
        print(json.dumps(report, indent=2))
    else:
        print_report(report, provider_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
