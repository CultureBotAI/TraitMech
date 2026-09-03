#!/usr/bin/env python3
"""Run deep research for TraitMech records via deep-research-client."""
from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml

from deep_research_contract import (
    ContractError,
    render_prompt_template,
    run_codex_research,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "trait_causal_graph_research.md"
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research"


def load_trait(path: Path) -> dict[str, Any]:
    """Load a TraitRecord YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Trait file not found: {path}")
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise ValueError(f"Trait file is not a YAML mapping: {path}")
    return doc


def resolve_trait_file(category: str, slug: str) -> Path:
    """Resolve a category/slug pair to a TraitRecord YAML path."""
    category_slug = category.lower()
    candidate = TRAITS_DIR / category_slug / f"{slug}.yaml"
    if candidate.exists():
        return candidate
    available = sorted((TRAITS_DIR / category_slug).glob("*.yaml"))
    hint = ", ".join(path.stem for path in available[:20])
    raise FileNotFoundError(
        f"Trait file not found: {candidate}. "
        f"Available {category_slug} traits include: {hint or 'none'}"
    )


def _join_values(values: Any) -> str:
    if values is None:
        return ""
    if isinstance(values, list):
        return ", ".join(str(value) for value in values)
    return str(values)


def summarize_synonyms(doc: dict[str, Any]) -> str:
    synonyms = []
    for synonym in doc.get("synonyms", []) or []:
        if isinstance(synonym, dict) and synonym.get("synonym_text"):
            synonyms.append(str(synonym["synonym_text"]))
    return ", ".join(synonyms)


def summarize_evidence(doc: dict[str, Any]) -> str:
    rows = []
    for evidence in doc.get("evidence", []) or []:
        if not isinstance(evidence, dict):
            continue
        reference = evidence.get("reference", "")
        snippet = evidence.get("snippet", "")
        notes = evidence.get("notes", "")
        rows.append(f"{reference}: {snippet} ({notes})".strip())
    return " | ".join(rows)


def summarize_causal_graphs(doc: dict[str, Any]) -> str:
    summaries = []
    for graph in doc.get("causal_graphs", []) or []:
        if not isinstance(graph, dict):
            continue
        graph_id = graph.get("graph_id", "")
        title = graph.get("title", "")
        node_count = len(graph.get("nodes", []) or [])
        edge_count = len(graph.get("edges", []) or [])
        summaries.append(f"{graph_id or title}: {node_count} nodes, {edge_count} edges")
    return " | ".join(summaries)


def summarize_canonical_examples(doc: dict[str, Any]) -> str:
    summaries = []
    for example in doc.get("canonical_examples", []) or []:
        if not isinstance(example, dict):
            continue
        label = example.get("taxon_label", "")
        taxon_id = example.get("taxon_id", "")
        reference = example.get("reference", "")
        summaries.append(f"{label} ({taxon_id}; {reference})")
    return " | ".join(summaries)


def summarize_protein_nodes(doc: dict[str, Any]) -> str:
    summaries = []
    for graph in doc.get("causal_graphs", []) or []:
        if not isinstance(graph, dict):
            continue
        graph_id = graph.get("graph_id", "")
        for node in graph.get("nodes", []) or []:
            if not isinstance(node, dict) or node.get("node_type") != "GENE_OR_PROTEIN":
                continue
            grounding = node.get("grounding") or "label-only"
            summaries.append(f"{graph_id}:{node.get('label', '')} [{grounding}]")
    return " | ".join(summaries)


def template_vars(doc: dict[str, Any], category_slug: str, trait_slug: str) -> dict[str, str]:
    return {
        "trait_label": str(doc.get("label", trait_slug)),
        "trait_identifier": str(doc.get("identifier", "")),
        "trait_category": str(doc.get("trait_category", category_slug.upper())),
        "trait_category_slug": category_slug,
        "trait_slug": trait_slug,
        "term_kind": str(doc.get("term_kind", "")),
        "mapping_status": str(doc.get("mapping_status", "")),
        "definition": str(doc.get("definition", "")),
        "parent_traits": _join_values(doc.get("parent_traits")),
        "synonyms": summarize_synonyms(doc),
        "evidence_summary": summarize_evidence(doc),
        "causal_graph_summary": summarize_causal_graphs(doc),
        "canonical_examples_summary": summarize_canonical_examples(doc),
        "protein_node_summary": summarize_protein_nodes(doc),
    }


DEFAULT_PROVIDER = "edison"

# Friendly provider aliases → the name `deep-research-client` actually accepts.
#
# "Edison" is the platform; `falcon` is its research agent, and the agent name is
# what the client exposes (`deep-research-client providers` lists perplexity,
# openai, falcon, asta, consensus, mock, cyberian, openscientist — there is no
# `edison`). The `edison_client` SDK targets api.platform.edisonscientific.com and
# names every job `job-futurehouse-*`, i.e. Edison Scientific and FutureHouse are
# one platform, and the client documents falcon's credential as EDISON_API_KEY.
#
# Aliasing lets callers say "edison" — the platform they think in — without
# teaching the client a provider it does not have. Resolve BEFORE computing output
# filenames so results stay in the established `-deep-research-falcon.md` namespace
# and previously-researched traits still count as done.
#
# SCOPE: this reaches Edison *through deep-research-client*, so it inherits that
# client's surface and nothing more — one research call and a markdown answer.
# (The client can also emit a citations sidecar; #249 stopped requesting it,
# because every one of the 353 it produced was a malformed regex over the report
# prose and the report's own References section is strictly better.) It exposes
# no Edison job selection (PaperQA3 vs its
# high-read variant vs precedent vs synthesis) and captures no run provenance
# (task id, cost, status, agent state). Driving the edison-client SDK directly is
# a separate concern and belongs in its own entry point; do not grow those
# features here, because they do not exist in deep-research-client to pass
# through.
PROVIDER_ALIASES = {
    "edison": "falcon",
    "gpt-rosalind": "rosalind",
    "gpt_rosalind": "rosalind",
}

# GPT-Rosalind is OpenAI's life-sciences reasoning model (research preview,
# trusted-access program). It is not a deep-research-client provider of its own:
# it is served by the same OpenAI Responses API the client's `openai` provider
# already drives, so TraitMech reaches it as `--provider openai --model <id>`.
#
# `rosalind` is nevertheless a TraitMech-level provider NAME, not an alias for
# `openai`, because the two must not share a filename namespace: an
# `o3-deep-research` report and a GPT-Rosalind report are different evidence
# and must never satisfy each other's resume check. resolve_provider() therefore
# returns `rosalind`, the output lands in `-deep-research-rosalind.md` (the
# namespace the two hand-supplied Rosalind artifacts under research/traits/
# ecology/ already use), and only provider_args() translates it for the client.
#
# The model id is an environment override with a default, not a constant: the
# id is a research-preview name that OpenAI can snapshot or rename, and
# `just rosalind-canary` reports which Rosalind ids the credential can actually
# see, so a wrong default is corrected by setting ROSALIND_MODEL rather than by
# editing code.
ROSALIND_PROVIDER = "rosalind"
ROSALIND_CLIENT_PROVIDER = "openai"
ROSALIND_MODEL_ENV = "ROSALIND_MODEL"
DEFAULT_ROSALIND_MODEL = "gpt-rosalind"
# The ONLY credential for this lane, even when it is the same string as
# OPENAI_API_KEY. The model is gated per organisation, so an ordinary OpenAI
# key proves nothing about access; accepting it made the triage route
# causal-mechanism work to a model most keys cannot call (#641). Setting the
# dedicated name is the operator's statement that this key is entitled.
ROSALIND_CREDENTIALS = ("ROSALIND_API_KEY",)


def resolve_provider(provider: str) -> str:
    """Map a user-facing provider name to TraitMech's canonical provider name.

    For most providers the canonical name is the deep-research-client name.
    `rosalind` is the exception: it is canonical here and translated to the
    client's `openai` provider plus a model by provider_args().

    Canonicalises to lower case on both hit and miss. Returning the caller's
    original casing on a miss would send `Falcon` to a client that only accepts
    `falcon`, and — because run_trait_graph_audit builds output filenames from
    this result — would look for `-deep-research-Falcon.md`, re-queueing (and
    re-paying for) every trait on a case-sensitive filesystem.
    """
    key = provider.lower()
    return PROVIDER_ALIASES.get(key, key)


def rosalind_model(environ: Mapping[str, str] | None = None) -> str:
    """The GPT-Rosalind model id to request: ROSALIND_MODEL, else the default."""
    env = os.environ if environ is None else environ
    return env.get(ROSALIND_MODEL_ENV) or DEFAULT_ROSALIND_MODEL


def provider_args(provider: str, environ: Mapping[str, str] | None = None) -> list[str]:
    """Mirror DisMech's cborg shortcut while allowing named providers such as falcon.

    `rosalind` becomes the client's `openai` provider with an explicit model, so
    the client never falls back to its o3-deep-research default under the
    Rosalind name.
    """
    if provider == "cborg":
        return ["--use-cborg"]
    if provider == ROSALIND_PROVIDER:
        return ["--provider", ROSALIND_CLIENT_PROVIDER, "--model", rosalind_model(environ)]
    return ["--provider", provider]


def research_env(provider: str, environ: Mapping[str, str] | None = None) -> dict[str, str]:
    """Build subprocess environment, aliasing Edison / Falcon keys to EDISON_API_KEY.

    This script and the deep-research-client read ``EDISON_API_KEY``, but the
    Edison platform credential is provisioned in the environment under
    ``EDISON_PLATFORM_API_KEY`` (the name the ``edison_client`` SDK reads by
    default) — and this script has no ``load_dotenv``, so a run outside ``just``
    (whose ``dotenv-load`` injects the per-repo ``.env``) would otherwise see no
    ``EDISON_API_KEY`` at all. Alias the platform key so research works on every
    invocation path. FutureHouse Falcon uses its own key.

    For ``rosalind`` the client reads ``OPENAI_API_KEY``, so the dedicated
    ``ROSALIND_API_KEY`` is copied over it -- and when the dedicated key is
    absent, any ``OPENAI_API_KEY`` in the shell is REMOVED rather than used, so
    a general-purpose key cannot silently take the call to an org without
    trusted access (#641). The client then reports a missing credential,
    which is the accurate message.
    """
    env = dict(os.environ if environ is None else environ)
    if not env.get("EDISON_API_KEY") and env.get("EDISON_PLATFORM_API_KEY"):
        env["EDISON_API_KEY"] = env["EDISON_PLATFORM_API_KEY"]
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    if provider == ROSALIND_PROVIDER:
        if env.get("ROSALIND_API_KEY"):
            env["OPENAI_API_KEY"] = env["ROSALIND_API_KEY"]
        else:
            env.pop("OPENAI_API_KEY", None)
    return env


def front_matter(path: Path) -> dict[str, Any]:
    """The YAML front matter of a report, or ``{}`` when it has none.

    Parsed with yaml rather than matched by regex, and over the whole head of
    the file rather than a fixed byte count: the hand-supplied Rosalind
    reports carry front matter longer than 4 KiB, and a curator may spell a
    flag ``False`` or ``no`` (#642). A UTF-8 BOM is tolerated.
    """
    try:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}
    try:
        data = yaml.safe_load(parts[0][3:])
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def is_pipeline_report(path: Path) -> bool:
    """False for a report whose front matter declares ``pipeline_run: false``.

    That flag marks an artifact a maintainer pasted in by hand (the two
    GPT-Rosalind answers under research/traits/ecology/). The sweep, the
    orphan gate, the renderer, and the overwrite guard all consult it, so it
    lives here with the provider table rather than in any one of them.
    """
    return front_matter(path).get("pipeline_run") is not False


def passthrough_model_override(passthrough_args: list[str]) -> bool:
    """True when the caller tried to pass ``--model`` through to the client."""
    return any(arg == "--model" or arg.startswith("--model=") for arg in passthrough_args)


def _repo_relative(path: Path) -> str:
    """Render ``path`` relative to the repo root when it lives inside it.

    deep-research-client copies whatever ``--template`` string it is given
    straight into each report's ``template_file:`` front matter. Passing an
    absolute path baked one machine's home directory into 342 tracked reports
    (#248) — a value that is wrong for every reader but one. The command is run
    with ``cwd=REPO_ROOT`` so the relative form still resolves.

    Falls back to the RESOLVED absolute path for a template outside the repo:
    it has no repo-relative form to record, and returning the caller's relative
    string would be actively wrong now that the child runs at ``REPO_ROOT`` —
    ``../elsewhere/x.md`` would re-anchor to the repo root and read the wrong
    file. Resolving happens against the parent's cwd, which is what the caller
    meant.
    """
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def build_command(
    *,
    provider: str,
    template: Path,
    output_file: Path,
    variables: dict[str, str],
    passthrough_args: list[str],
    client_command: str = "deep-research-client",
) -> list[str]:
    command = [
        client_command,
        "research",
        "--template",
        _repo_relative(template),
    ]
    for key, value in variables.items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(provider_args(provider))
    command.extend(
        [
            # Resolved for the same reason as the template above: the child runs
            # at REPO_ROOT, so a relative --research-dir would have the parent
            # create one directory and the child write into another.
            "--output",
            str(output_file.resolve()),
            # NO --separate-citations. The client's sidecar is a regex over the
            # report prose, and every one of the 353 it produced was malformed:
            # 194 broken markdown-link tails, 2,770 stray trailing commas, and
            # 332 of 353 listing the same reference two or three times over
            # (#249). It also re-emitted the ~55-line rendered prompt, already
            # stored in the report's own `template_variables` front matter.
            #
            # The report's References section maps PaperQA keys to DOIs and is
            # what a curator actually reads, so this drops a broken duplicate
            # rather than a source. Verified before removing: across every
            # sidecar, ZERO CURIE-shaped tokens appear that are not also in
            # their report — so `run_trait_graph_audit --verify`'s malformed-CURIE
            # scan loses no coverage.
        ]
    )
    command.extend(passthrough_args)
    return command


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        default=DEFAULT_PROVIDER,
        help=f"provider or alias (default: {DEFAULT_PROVIDER}, the Edison research "
             "agent, which resolves to deep-research-client's `falcon`); "
             "`rosalind` (alias `gpt-rosalind`) runs OpenAI's GPT-Rosalind through "
             "the client's `openai` provider",
    )
    parser.add_argument("--category", required=True, help="Trait category directory, e.g. physiology")
    parser.add_argument("--slug", required=True, help="Trait YAML slug without .yaml")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--min-chars", type=int, default=1000)
    parser.add_argument("--min-sources", type=int, default=3)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing report at the output path. Without it an "
             "existing report -- the pipeline's own or a hand-supplied one -- "
             "is never replaced (#638).",
    )
    args, passthrough_args = parser.parse_known_args(argv)
    args.passthrough_args = passthrough_args
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    # Resolve "edison" -> "falcon" up front so the client call, the credential
    # lookup, and the output filename all agree on one name.
    provider = resolve_provider(args.provider)
    category_slug = args.category.lower()
    trait_file = resolve_trait_file(category_slug, args.slug)
    doc = load_trait(trait_file)

    output_dir = args.research_dir / "traits" / category_slug
    output_file = output_dir / f"{args.slug}-deep-research-{provider}.md"
    variables = template_vars(doc, category_slug, args.slug)
    print(f"Researching: {variables['trait_label']} ({provider}) -> {output_file}")
    if provider == ROSALIND_PROVIDER and passthrough_model_override(args.passthrough_args):
        # The client keeps the LAST --model, so a passthrough one would write
        # some other model's answer into the rosalind namespace and satisfy its
        # resume check (#640). The model is set through ROSALIND_MODEL only.
        print(
            f"--model is not a passthrough option for {ROSALIND_PROVIDER}; set "
            f"{ROSALIND_MODEL_ENV} instead so the report namespace stays honest",
            file=sys.stderr,
        )
        return 2
    if output_file.exists() and not args.force:
        kind = "the pipeline's own" if is_pipeline_report(output_file) else "a hand-supplied"
        message = (
            f"refusing to overwrite {kind} report at {output_file}; pass --force "
            f"to replace it (#638)"
        )
        if args.dry_run:
            print(f"NOTE: {message}")
        else:
            print(f"ERROR: {message}", file=sys.stderr)
            return 3
    if provider == "codex":
        if args.passthrough_args:
            print(
                "Codex does not accept deep-research-client passthrough arguments",
                file=sys.stderr,
            )
            return 2
        try:
            prompt = render_prompt_template(args.template, variables)
            if args.dry_run:
                print("codex --search --ask-for-approval never exec [schema validated]")
                print(f"prompt: {len(prompt)} characters")
                return 0
            summary = run_codex_research(
                prompt,
                output_file,
                repo_root=REPO_ROOT,
                timeout=args.timeout,
                min_chars=args.min_chars,
                min_sources=args.min_sources,
            )
        except ContractError as exc:
            print(f"Codex research rejected: {exc}", file=sys.stderr)
            return 1
        print(f"Validated {summary.characters} characters and {summary.sources} sources")
        return 0

    command = build_command(
        provider=provider,
        template=args.template,
        output_file=output_file,
        variables=variables,
        passthrough_args=args.passthrough_args,
        client_command=args.client_command,
    )

    if args.dry_run:
        print(shlex.join(command))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    # cwd is pinned so the repo-relative --template above resolves no matter
    # where the script was invoked from.
    subprocess.run(command, check=True, env=research_env(provider), cwd=REPO_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
