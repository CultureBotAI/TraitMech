from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = REPO_ROOT / "scripts" / "deep_research_provider.py"
CONFIG_PATH = REPO_ROOT / "conf" / "deep_research_provider.yaml"
SPEC = importlib.util.spec_from_file_location("deep_research_provider", MODULE_PATH)
assert SPEC and SPEC.loader
drp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = drp
SPEC.loader.exec_module(drp)


def test_profile_has_domain_specific_default_and_three_stage_triage():
    config = drp.load_config(CONFIG_PATH)
    focus = config["focuses"][config["default_focus"]]

    assert config["mech"].endswith("Mech")
    assert config["target"]
    assert set(focus["stages"]) == {"discovery", "synthesis", "verification"}
    assert focus["source_priorities"]


@pytest.mark.parametrize("alias", ["edison", "futurehouse", "Falcon"])
def test_edison_aliases_resolve_to_falcon(alias):
    assert drp.canonical_provider(alias) == "falcon"


def test_falcon_platform_key_is_recognized_without_exposing_it():
    """The alternate key name is honoured, and its VALUE never reaches the output.

    Status is `configured`, not `available`: this key authenticates and the
    account then returns 402, so presence cannot promise usability (#435).
    """
    status, reason = drp.provider_status(
        "falcon", {"EDISON_PLATFORM_API_KEY": "secret"}
    )
    assert status == drp.CONFIGURED
    assert "secret" not in reason


def test_explicit_empty_environment_does_not_fall_back_to_process_credentials():
    status, reason = drp.provider_status("asta", {})
    assert status == "unavailable"
    assert reason == "set ASTA_API_KEY"


def test_every_focus_ranks_all_real_and_stub_providers():
    """Every focus ranks every provider and routes somewhere.

    Uses an injected environ rather than monkeypatching the process: since #436
    threaded it through build_report, the report no longer depends on whatever
    keys the machine running the tests happens to have set.
    """
    config = drp.load_config(CONFIG_PATH)

    for focus_name in config["focuses"]:
        report = drp.build_report(config, focus_name, environ={"ASTA_API_KEY": "test-only"})
        for stage in report["stages"]:
            names = {row["provider"] for row in stage["ranking"]}
            assert names == set(drp.PROVIDERS)
            assert stage["recommended_available"] is not None
            assert stage["recommended_available"]["status"] in drp.ROUTABLE


def test_unknown_default_focus_is_rejected(tmp_path):
    profile = tmp_path / "bad.yaml"
    profile.write_text("default_focus: absent\nfocuses:\n  present:\n    stages: {}\n")
    with pytest.raises(ValueError, match="default_focus"):
        drp.load_config(profile)


# --- scoring arithmetic (#438) ---
#
# The output of this tool is a decision about what to spend money on, and none of
# the arithmetic behind it had a test. `speed_weight` and `cost_weight` both
# invert their scale (`5 - value`), which is exactly the expression a sign typo
# survives silently while reordering every recommendation.


def _cfg(stage: dict, adjustments: dict | None = None) -> dict:
    focus = {"stages": {"s": stage}}
    if adjustments is not None:
        focus["provider_adjustments"] = adjustments
    return {"default_focus": "f", "focuses": {"f": focus}}


def test_matching_capabilities_add_their_weights():
    asta = drp.PROVIDERS["asta"]
    assert drp._score(asta, {"capabilities": {"academic_search": 5}}, {}) == 5
    assert drp._score(asta, {"capabilities": {"academic_search": 5, "snippets": 2}}, {}) == 7


def test_unmatched_capabilities_contribute_nothing():
    asta = drp.PROVIDERS["asta"]
    assert "synthesis" not in asta.capabilities
    assert drp._score(asta, {"capabilities": {"synthesis": 5}}, {}) == 0


def test_speed_weight_rewards_fast_and_penalises_slow():
    """`5 - TIME_VALUE`, so fast must outscore very_slow -- not the reverse."""
    fast = drp.PROVIDERS["asta"]           # fast
    slow = drp.PROVIDERS["openscientist"]  # very_slow
    stage = {"capabilities": {}, "speed_weight": 1}
    assert drp._score(fast, stage, {}) > drp._score(slow, stage, {})


def test_cost_weight_rewards_cheap_and_penalises_expensive():
    """`5 - COST_VALUE`, so low cost must outscore very_high."""
    cheap = drp.PROVIDERS["asta"]    # low
    dear = drp.PROVIDERS["openai"]   # very_high
    stage = {"capabilities": {}, "cost_weight": 1}
    assert drp._score(cheap, stage, {}) > drp._score(dear, stage, {})


def test_synthesis_weight_orders_none_below_agentic():
    stage = {"capabilities": {}, "synthesis_weight": 1}
    assert drp._score(drp.PROVIDERS["asta"], stage, {}) < drp._score(
        drp.PROVIDERS["openscientist"], stage, {}
    )


def test_provider_adjustment_is_added_verbatim():
    asta = drp.PROVIDERS["asta"]
    base = drp._score(asta, {"capabilities": {}}, {})
    assert drp._score(asta, {"capabilities": {}}, {"asta": 4}) == base + 4
    assert drp._score(asta, {"capabilities": {}}, {"asta": -4}) == base - 4


def test_fit_is_normalised_so_the_best_provider_scores_100():
    rows = drp.rank_stage(_cfg({"capabilities": {"synthesis": 5}}), "f", "s", environ={})
    assert rows[0]["fit"] == 100
    assert rows == sorted(rows, key=lambda r: (-r["fit"], r["provider"]))


def test_degenerate_scores_do_not_produce_negative_fit():
    """All-zero and all-negative weightings must not emit a negative fit."""
    for adj in ({}, {n: -1 for n in drp.PROVIDERS}):
        rows = drp.rank_stage(_cfg({"capabilities": {}}, adj), "f", "s", environ={})
        assert {r["fit"] for r in rows} == {0}


# --- the environ seam reaches the surface (#436) ---


def test_rank_stage_honours_an_injected_environment():
    cfg = _cfg({"capabilities": {"scientific_literature": 5}})
    empty = {r["provider"]: r["status"] for r in drp.rank_stage(cfg, "f", "s", environ={})}
    assert empty["falcon"] == drp.UNAVAILABLE
    keyed = {
        r["provider"]: r["status"]
        for r in drp.rank_stage(cfg, "f", "s", environ={"EDISON_API_KEY": "x"})
    }
    assert keyed["falcon"] == drp.CONFIGURED


def test_build_report_threads_the_environment_to_its_routing_choice():
    """Without threading, the report always read the real os.environ."""
    cfg = _cfg({"capabilities": {"scientific_literature": 5}})
    report = drp.build_report(cfg, "f", environ={})
    routed = report["stages"][0]["recommended_available"]
    assert routed is None or routed["provider"] != "falcon"


# --- a credential is not usability (#435) ---


def test_a_present_credential_is_configured_not_available():
    status, reason = drp.provider_status("falcon", {"EDISON_API_KEY": "x"})
    assert status == drp.CONFIGURED, "a key that 402s must not read as available"
    assert "unverified" in reason
    assert "x" not in reason


def test_locally_checkable_providers_may_be_available():
    """A local binary/package IS checkable without a network call, so `available`."""
    status, _ = drp.provider_status("mock", {"ENABLE_MOCK_PROVIDER": "true"})
    assert status == drp.AVAILABLE


def test_configured_providers_are_still_routable():
    assert drp.CONFIGURED in drp.ROUTABLE
    assert drp.AVAILABLE in drp.ROUTABLE
    assert drp.UNAVAILABLE not in drp.ROUTABLE
    assert drp.STUB not in drp.ROUTABLE


# --- bad input is usage feedback, not a traceback (#437) ---


def test_unknown_focus_exits_two_without_a_traceback(capsys):
    with pytest.raises(SystemExit) as excinfo:
        drp.main(["--config", str(CONFIG_PATH), "--focus", "no_such_focus"])
    assert excinfo.value.code == 2
    assert "Unknown focus" in capsys.readouterr().err


def test_unknown_provider_exits_two_and_lists_the_choices(capsys):
    with pytest.raises(SystemExit) as excinfo:
        drp.main(["--config", str(CONFIG_PATH), "--provider", "bogus"])
    assert excinfo.value.code == 2
    err = capsys.readouterr().err
    assert "Unknown provider" in err and "asta" in err


def test_usage_error_is_still_a_valueerror_for_existing_callers():
    assert issubclass(drp.UsageError, ValueError)


# --- the fit legend (#439) ---


def test_the_report_states_what_fit_measures(capsys):
    drp.main(["--config", str(CONFIG_PATH)])
    out = capsys.readouterr().out
    assert "relative WITHIN this stage" in out
    assert "not an absolute score" in out


# --- single-provider JSON stays internally consistent (#450) ---


def test_provider_json_adds_selected_without_filtering_the_ranking():
    """Filtering `ranking` left `recommended_available` naming an absent provider.

    The routing choice is a property of the stage, not of the query, so the fix
    is an extra key rather than a narrower payload.
    """
    import contextlib
    import io
    import json as _json

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        drp.main(["--config", str(CONFIG_PATH), "--provider", "edison", "--json"])
    report = _json.loads(buf.getvalue())
    for stage in report["stages"]:
        names = [row["provider"] for row in stage["ranking"]]
        assert names == sorted(set(names), key=names.index), "ranking must not be filtered"
        assert len(names) == len(drp.PROVIDERS)
        assert stage["selected"]["provider"] == "falcon", "edison resolves to falcon"
        routed = stage["recommended_available"]
        if routed:
            assert routed["provider"] in names, (
                "the routing choice must be findable in the ranking it came from"
            )

def test_all_negative_scores_keep_their_relative_order():
    """Fit may floor at zero, but routing must still prefer the least-bad score."""
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))
    stage = config["focuses"][focus_name]["stages"][stage_name]
    stage["capabilities"] = {}
    stage["synthesis_weight"] = 0
    stage["speed_weight"] = 0
    stage["cost_weight"] = 0

    # Deliberately make reverse-alphabetical order the raw-score order.  The
    # old fit-only sort returned alphabetical order once every fit floored to 0.
    expected = sorted(drp.PROVIDERS, reverse=True)
    config["focuses"][focus_name]["provider_adjustments"] = {
        provider: -(index + 1) for index, provider in enumerate(expected)
    }

    rows = drp.rank_stage(config, focus_name, stage_name)
    assert all(row["fit"] == 0 for row in rows)
    assert [row["provider"] for row in rows] == expected
