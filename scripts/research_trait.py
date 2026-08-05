#!/usr/bin/env python3
"""Run deep research for TraitMech records via deep-research-client."""
from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

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
# client's surface and nothing more — one research call, a markdown answer, and a
# citations sidecar. It exposes no Edison job selection (PaperQA3 vs its
# high-read variant vs precedent vs synthesis) and captures no run provenance
# (task id, cost, status, agent state). Driving the edison-client SDK directly is
# a separate concern and belongs in its own entry point; do not grow those
# features here, because they do not exist in deep-research-client to pass
# through.
PROVIDER_ALIASES = {"edison": "falcon"}


def resolve_provider(provider: str) -> str:
    """Map a user-facing provider name to a deep-research-client provider.

    Canonicalises to lower case on both hit and miss. Returning the caller's
    original casing on a miss would send `Falcon` to a client that only accepts
    `falcon`, and — because run_trait_graph_audit builds output filenames from
    this result — would look for `-deep-research-Falcon.md`, re-queueing (and
    re-paying for) every trait on a case-sensitive filesystem.
    """
    key = provider.lower()
    return PROVIDER_ALIASES.get(key, key)


def provider_args(provider: str) -> list[str]:
    """Mirror DisMech's cborg shortcut while allowing named providers such as falcon."""
    if provider == "cborg":
        return ["--use-cborg"]
    return ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    """Build subprocess environment, aliasing Edison / Falcon keys to EDISON_API_KEY.

    This script and the deep-research-client read ``EDISON_API_KEY``, but the
    Edison platform credential is provisioned in the environment under
    ``EDISON_PLATFORM_API_KEY`` (the name the ``edison_client`` SDK reads by
    default) — and this script has no ``load_dotenv``, so a run outside ``just``
    (whose ``dotenv-load`` injects the per-repo ``.env``) would otherwise see no
    ``EDISON_API_KEY`` at all. Alias the platform key so research works on every
    invocation path. FutureHouse Falcon uses its own key.
    """
    env = os.environ.copy()
    if not env.get("EDISON_API_KEY") and env.get("EDISON_PLATFORM_API_KEY"):
        env["EDISON_API_KEY"] = env["EDISON_PLATFORM_API_KEY"]
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


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
    citations_file: Path,
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
            "--separate-citations",
            str(citations_file.resolve()),
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
             "agent, which resolves to deep-research-client's `falcon`)",
    )
    parser.add_argument("--category", required=True, help="Trait category directory, e.g. physiology")
    parser.add_argument("--slug", required=True, help="Trait YAML slug without .yaml")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it.",
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
    citations_file = output_file.with_suffix(output_file.suffix + ".citations.md")
    variables = template_vars(doc, category_slug, args.slug)
    command = build_command(
        provider=provider,
        template=args.template,
        output_file=output_file,
        citations_file=citations_file,
        variables=variables,
        passthrough_args=args.passthrough_args,
        client_command=args.client_command,
    )

    print(f"Researching: {variables['trait_label']} ({provider}) -> {output_file}")
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
