"""Tests for TraitMech deep research command wiring."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_trait import (  # noqa: E402
    DEFAULT_PROVIDER,
    build_command,
    load_trait,
    parse_args,
    provider_args,
    research_env,
    resolve_provider,
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
    assert "NCBITaxon:" in variables["canonical_examples_summary"]
    assert "[" in variables["protein_node_summary"]


def test_provider_args_mirror_dismech_cborg_shortcut():
    assert provider_args("falcon") == ["--provider", "falcon"]
    assert provider_args("cborg") == ["--use-cborg"]


def test_build_command_for_falcon_research():
    command = build_command(
        provider="falcon",
        template=Path("templates/trait_causal_graph_research.md"),
        output_file=Path("research/traits/physiology/autotrophic-deep-research-falcon.md"),
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
    # No --separate-citations: the client's sidecar was a broken regex over
    # the report prose and is no longer requested (#249).
    assert "--separate-citations" not in command
    assert command[-2:] == ["--max-cost", "1"]


def test_build_command_makes_an_absolute_template_repo_relative():
    """#248: deep-research-client copies --template verbatim into every
    report's `template_file:` front matter, so an absolute path baked one
    machine's home directory into 342 tracked reports."""
    from research_trait import REPO_ROOT

    command = build_command(
        provider="falcon",
        template=REPO_ROOT / "templates" / "trait_causal_graph_research.md",
        output_file=Path("out.md"),
        variables={},
        passthrough_args=[],
    )
    assert command[3] == "templates/trait_causal_graph_research.md"
    assert not command[3].startswith("/")


def test_build_command_keeps_a_template_outside_the_repo_absolute():
    """There is no repo-relative form to record, so the absolute path stands."""
    command = build_command(
        provider="falcon",
        template=Path("/tmp/elsewhere/custom.md"),
        output_file=Path("out.md"),
        variables={},
        passthrough_args=[],
    )
    # .resolve() so the assertion holds on macOS, where /tmp is a symlink.
    assert command[3] == str(Path("/tmp/elsewhere/custom.md").resolve())
    assert command[3].startswith("/")


def test_a_relative_template_outside_the_repo_is_resolved(monkeypatch, tmp_path):
    """The child runs at REPO_ROOT, so handing it back the caller's relative
    string would re-anchor `../elsewhere/x.md` to the repo root and read the
    wrong file. Resolution happens against the parent's cwd (#248 review)."""
    outside = tmp_path / "elsewhere"
    outside.mkdir()
    (outside / "custom.md").write_text("x")
    monkeypatch.chdir(outside)

    command = build_command(
        provider="falcon",
        template=Path("custom.md"),
        output_file=Path("out.md"),
        variables={},
        passthrough_args=[],
    )
    assert command[3] == str((outside / "custom.md").resolve())


def test_output_paths_are_resolved_against_the_callers_cwd(monkeypatch, tmp_path):
    """Same hazard: a relative --research-dir would have the parent create one
    directory and the child, running at REPO_ROOT, write into another."""
    monkeypatch.chdir(tmp_path)
    command = build_command(
        provider="falcon",
        template=Path("templates/trait_causal_graph_research.md"),
        output_file=Path("out/report.md"),
        variables={},
        passthrough_args=[],
    )
    assert str(tmp_path.resolve() / "out/report.md") in command


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


def test_edison_alias_resolves_to_falcon():
    """"Edison" is the platform; `falcon` is the agent name the client accepts.

    deep-research-client has no provider literally named `edison`, so the alias
    must resolve before the name reaches the client.
    """
    assert resolve_provider("edison") == "falcon"
    assert resolve_provider("Edison") == "falcon"


def test_resolve_provider_passes_through_real_provider_names():
    for name in ("falcon", "openai", "cyberian", "perplexity"):
        assert resolve_provider(name) == name


def test_provider_defaults_to_edison():
    args = parse_args(["--category", "physiology", "--slug", "autotrophic"])
    assert args.provider == DEFAULT_PROVIDER == "edison"


def test_edison_output_filename_stays_in_falcon_namespace(tmp_path, capsys):
    """Resolving the alias late would strand results in a new filename namespace
    and make the 10 already-researched traits look pending again.

    Asserts on the emitted path, not the return code: --dry-run returns 0 no
    matter which filename was built, so a return-code check cannot detect the
    regression this test exists to catch.
    """
    from research_trait import main as research_main

    rc = research_main([
        "--provider", "edison", "--category", "physiology", "--slug", "autotrophic",
        "--research-dir", str(tmp_path), "--dry-run",
    ])
    assert rc == 0
    out = capsys.readouterr().out
    assert "autotrophic-deep-research-falcon.md" in out
    assert "-deep-research-edison.md" not in out


# --- the GPT-Rosalind lane ---
#
# `rosalind` is a TraitMech provider NAME served through the client's `openai`
# provider with an explicit model. The three things that must hold together:
# the alias resolves to `rosalind` (not `openai`), the client is told `openai`
# plus a model, and the output filename stays in the `-rosalind` namespace.

from research_trait import (  # noqa: E402
    DEFAULT_ROSALIND_MODEL,
    ROSALIND_CREDENTIALS,
    rosalind_model,
)


def test_rosalind_aliases_resolve_to_the_traitmech_name_not_to_openai():
    for alias in ("rosalind", "Rosalind", "gpt-rosalind", "GPT-Rosalind", "gpt_rosalind"):
        assert resolve_provider(alias) == "rosalind"


def test_rosalind_is_sent_to_the_client_as_openai_with_an_explicit_model():
    assert provider_args("rosalind", {}) == [
        "--provider", "openai", "--model", DEFAULT_ROSALIND_MODEL,
    ]


def test_rosalind_model_can_be_overridden_without_editing_code():
    """The preview id can be snapshotted or renamed; the canary tells you the
    new name and ROSALIND_MODEL is where it goes."""
    assert rosalind_model({}) == DEFAULT_ROSALIND_MODEL
    assert rosalind_model({"ROSALIND_MODEL": "gpt-rosalind-2026-08-01"}) == "gpt-rosalind-2026-08-01"
    assert provider_args("rosalind", {"ROSALIND_MODEL": "x"})[-1] == "x"


def test_plain_openai_is_still_plain_openai():
    """Adding the lane must not touch the documented `--provider openai` path."""
    assert provider_args("openai", {}) == ["--provider", "openai"]


def test_rosalind_output_stays_in_its_own_namespace(tmp_path, capsys):
    """An o3-deep-research report and a GPT-Rosalind report are different
    evidence; neither may satisfy the other's resume check."""
    from research_trait import main as research_main

    rc = research_main([
        "--provider", "gpt-rosalind", "--category", "ecology", "--slug", "gut_associated",
        "--research-dir", str(tmp_path), "--dry-run",
    ])
    assert rc == 0
    out = capsys.readouterr().out
    assert "gut_associated-deep-research-rosalind.md" in out
    assert "-deep-research-openai.md" not in out
    assert "--provider openai --model" in out


def test_dedicated_rosalind_key_overrides_a_general_openai_key():
    """A general-purpose OPENAI_API_KEY in the shell belongs to whatever org the
    developer uses day to day; it must not silently take a Rosalind call."""
    env = research_env("rosalind", {"OPENAI_API_KEY": "general", "ROSALIND_API_KEY": "rosalind"})
    assert env["OPENAI_API_KEY"] == "rosalind"


def test_a_bare_openai_key_still_serves_rosalind():
    env = research_env("rosalind", {"OPENAI_API_KEY": "general"})
    assert env["OPENAI_API_KEY"] == "general"


def test_rosalind_key_does_not_leak_into_other_providers():
    env = research_env("openai", {"OPENAI_API_KEY": "general", "ROSALIND_API_KEY": "rosalind"})
    assert env["OPENAI_API_KEY"] == "general"
    env = research_env("falcon", {"ROSALIND_API_KEY": "rosalind"})
    assert "OPENAI_API_KEY" not in env


def test_research_env_still_reads_the_process_environment_by_default(monkeypatch):
    monkeypatch.setenv("ROSALIND_API_KEY", "from-process")
    assert research_env("rosalind")["OPENAI_API_KEY"] == "from-process"


def test_rosalind_credential_order_prefers_the_dedicated_name():
    assert ROSALIND_CREDENTIALS[0] == "ROSALIND_API_KEY"
    assert "OPENAI_API_KEY" in ROSALIND_CREDENTIALS
