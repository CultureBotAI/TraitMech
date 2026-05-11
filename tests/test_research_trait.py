"""Tests for TraitMech deep research command wiring."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_trait import (  # noqa: E402
    build_command,
    load_trait,
    parse_args,
    provider_args,
    research_env,
    resolve_trait_file,
    template_vars,
)


def test_resolve_trait_file_finds_category_slug_record():
    path = resolve_trait_file("physiology", "autotrophic")
    assert path == REPO_ROOT / "data" / "traits" / "physiology" / "autotrophic.yaml"


def test_template_vars_include_trait_context():
    path = resolve_trait_file("physiology", "autotrophic")
    variables = template_vars(load_trait(path), "physiology", "autotrophic")
    assert variables["trait_label"] == "autotrophic"
    assert variables["trait_identifier"] == "METPO:1000632"
    assert variables["trait_category_slug"] == "physiology"
    assert "inorganic carbon" in variables["definition"]


def test_provider_args_mirror_dismech_cborg_shortcut():
    assert provider_args("falcon") == ["--provider", "falcon"]
    assert provider_args("cborg") == ["--use-cborg"]


def test_build_command_for_falcon_research():
    command = build_command(
        provider="falcon",
        template=Path("templates/trait_causal_graph_research.md"),
        output_file=Path("research/traits/physiology/autotrophic-deep-research-falcon.md"),
        citations_file=Path("research/traits/physiology/autotrophic-deep-research-falcon.md.citations.md"),
        variables={"trait_label": "autotrophic", "trait_identifier": "METPO:1000632"},
        passthrough_args=["--max-cost", "1"],
    )
    assert command[:4] == [
        "deep-research-client",
        "research",
        "--template",
        "templates/trait_causal_graph_research.md",
    ]
    assert "--provider" in command
    assert "falcon" in command
    assert "--separate-citations" in command
    assert command[-2:] == ["--max-cost", "1"]


def test_research_env_maps_futurehouse_key_to_edison(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "test-key")
    env = research_env("falcon")
    assert env["EDISON_API_KEY"] == "test-key"


def test_parse_args_passes_provider_specific_options_through():
    args = parse_args(
        [
            "--provider",
            "falcon",
            "--category",
            "physiology",
            "--slug",
            "mixotrophic",
            "--param",
            "max_tokens=3500",
        ]
    )
    assert args.passthrough_args == ["--param", "max_tokens=3500"]
