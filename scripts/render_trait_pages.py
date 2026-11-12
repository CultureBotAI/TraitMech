#!/usr/bin/env python3
"""Render HTML pages for every TraitMech YAML.

Outputs
-------
  pages/index.html                                 — landing page + per-category tiles
  pages/category/<category>.html                   — tabular trait list per category
  pages/traits/<category>/<slug>.html              — one page per TraitRecord
  pages/assets/style.css                           — copied from templates

Per-trait page surfaces:
  - METPO provenance (label, definition, parents, synonyms, xrefs, creator)
  - kg-microbe match (from data/embeddings/metpo_to_kgm_node.tsv) plus a short
    preview of the deepwalk vector for each matched node.

Inputs
------
  data/traits/<category>/<slug>.yaml
  data/embeddings/deepwalk_traits.tsv.gz   (built by build_embedding_index.py)
  data/embeddings/metpo_to_kgm_node.tsv    (ditto)
"""
from __future__ import annotations

import argparse
import csv
import gzip
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

import yaml
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

from research_trait import is_pipeline_report
from trait_causal_graph import causal_graphs_for_template

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
EMBED_DIR = REPO_ROOT / "data" / "embeddings"
TEMPLATES_DIR = REPO_ROOT / "src" / "traitmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
RAW_OWL = REPO_ROOT / "data" / "raw" / "metpo.owl"
SCHEMA_PATH = REPO_ROOT / "src" / "traitmech" / "schema" / "traitmech.yaml"
UMAP_JSON = EMBED_DIR / "trait_umap.json"
GRAPH_JSON = EMBED_DIR / "trait_graph.json"
CORPUS_MAP_JSON = EMBED_DIR / "corpus_map.json"
SEQUENCE_MAP_JSON = EMBED_DIR / "sequence_map.json"
NN_JSON = EMBED_DIR / "trait_nearest_neighbors.json"

DIM_PREVIEW = 4  # number of dims to show inline next to each kg-microbe node
EMBEDDING_RELEASE = "2026-04-25"

# Provider precedence for the deep-research lookup.
#
# The pipeline writes `<slug>-deep-research-<provider>.md` — the suffix is what
# makes the sweep resumable, since resume detection is file-existence based on
# that exact name. This renderer looked for a bare `<slug>.md` instead, so the
# research block never rendered for any trait (#233).
#
# A trait can carry reports from more than one provider, so the pick has to be
# deterministic (#228 made reproducible output a requirement). Sorting by name
# would be deterministic but wrong: `cellulolysis` has both `-falcon` and
# `-codex` reports, and alphabetical order picks `codex` — the one artifact in
# the tree with no manifest row and no citations sidecar (#245). Rank by the
# provider the tracked sweep actually ran, and fall back to name order so an
# unrecognised provider still renders reproducibly rather than arbitrarily.
#
# `rosalind` (OpenAI GPT-Rosalind, a pipeline provider since the rosalind lane
# landed) ranks after falcon: the tracked sweep corpus is falcon's, so a trait
# with both keeps rendering the report the manifest accounts for, while a trait
# researched only through Rosalind renders that rather than falling to name
# order behind a stray `-codex` file.
RESEARCH_PROVIDERS = ("falcon", "rosalind")

# How much of a report to embed in the page.
#
# Embedding whole reports takes pages/ from 16 MB to 31 MB — mutualism.html
# alone goes 36 KB → 80 KB — to store a second copy of text that #240/#241
# already track under research/. It also makes every future sweep a 353-file
# diff against the pages/ staleness gate (#230).
#
# The card is a scrolling 480px-tall <pre>, so a reader was never going to see a
# 30 KB report on the page anyway; they were going to open the file. Embed
# enough to show what the report covers — scope summary and the start of the
# candidate nodes — and link the rest. Raising this to a large number restores
# the full embed if that trade is ever judged the wrong way round.
RESEARCH_PREVIEW_LINES = 60

# Last line of the rendered prompt. The provider echoes the whole template twice
# before its answer, so previewing the head of the raw file shows YAML front
# matter and the prompt and not one research finding. This marker appears
# exactly twice in all 353 sweep reports, and everything after the second is the
# answer. A report without it — another provider's layout — falls back to
# everything after the YAML front matter.
RESEARCH_PROMPT_TAIL = "Warnings for claims that should not yet be curated into TraitMech"

# GitHub URL bases for the right-rail source-link card.
GH_BLOB_BASE = "https://github.com/CultureBotAI/TraitMech/blob/main"
GH_RAW_BASE = "https://raw.githubusercontent.com/CultureBotAI/TraitMech/main"
GH_EDIT_BASE = "https://github.com/CultureBotAI/TraitMech/edit/main"


def reference_url(reference: object) -> str | None:
    """Resolve citation identifiers without turning arbitrary text into links."""
    if not isinstance(reference, str):
        return None
    if any(ord(char) < 32 or ord(char) == 127 for char in reference):
        return None
    value = reference.strip()
    if re.fullmatch(r"DOI:10\.[0-9]{4,9}/\S+", value, re.IGNORECASE):
        return "https://doi.org/" + quote(value[4:], safe="/():;")
    if re.fullmatch(r"PMID:[0-9]+", value, re.IGNORECASE):
        return f"https://pubmed.ncbi.nlm.nih.gov/{value[5:]}/"
    if any(char.isspace() or char in '\\<>"' for char in value):
        return None
    try:
        parsed = urlsplit(value)
        if (parsed.scheme.lower() in {"http", "https"} and parsed.hostname
                and parsed.username is None and parsed.password is None):
            # Accessing port also rejects malformed/non-numeric authority ports.
            _ = parsed.port
            return value
    except ValueError:
        pass
    return None


PREFIX_URL = {
    "GO": "https://amigo.geneontology.org/amigo/term/{curie}",
    "CHEBI": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId={curie}",
    "METPO": "https://w3id.org/metpo/{local}",
    "EC": "https://www.ExplorEnz.info/search2.php?ec_no={local}",
    "KEGG": "https://www.kegg.jp/entry/{local}",
    "RHEA": "https://www.rhea-db.org/rhea/{local}",
    "UniProtKB": "https://www.uniprot.org/uniprotkb/{local}/entry",
    "Pfam": "https://www.ebi.ac.uk/interpro/entry/pfam/{local}/",
    "InterPro": "https://www.ebi.ac.uk/interpro/entry/InterPro/{local}/",
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_{local}",
    "PATO": "http://purl.obolibrary.org/obo/PATO_{local}",
    "RO": "http://purl.obolibrary.org/obo/RO_{local}",
    "BFO": "http://purl.obolibrary.org/obo/BFO_{local}",
    "UO": "http://purl.obolibrary.org/obo/UO_{local}",
    "SO": "http://purl.obolibrary.org/obo/SO_{local}",
    "CL": "http://purl.obolibrary.org/obo/CL_{local}",
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_{local}",
    "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={local}",
    "biolink": "https://w3id.org/biolink/vocab/{local}",
    "Reactome": "https://reactome.org/content/detail/{local}",
    "MetaCyc": "https://metacyc.org/META/NEW-IMAGE?object={local}",
    "MICRO": "http://purl.obolibrary.org/obo/MICRO_{local}",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#{local}",
}

# This repository's own namespace. No registry resolves it, so a traitmech:
# CURIE is linkable only through the record page it names; one with no page is
# a dangling reference, and a registry fallback would just invent a 404.
LOCAL_PREFIX = "traitmech"
CURIE_SHAPE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'\\]+")


def curie_url(curie: object) -> str | None:
    """Resolve ontology/database CURIEs to canonical external URLs.

    Known prefixes use PREFIX_URL. Any other well-formed CURIE falls back to
    bioregistry.io, which resolves or explains every registered prefix, so a
    displayed identifier is never a dead end (the fleet's term_links rule).
    """
    if not isinstance(curie, str) or ":" not in curie:
        return None
    ref = reference_url(curie)
    if ref:
        return ref
    value = curie.strip()
    if not CURIE_SHAPE.fullmatch(value):
        return None
    prefix, local = value.split(":", 1)
    tmpl = PREFIX_URL.get(prefix)
    if tmpl:
        return tmpl.format(curie=value, local=local)
    if prefix == LOCAL_PREFIX:
        return None
    return "https://bioregistry.io/" + quote(value, safe=":/")


@pass_context
def term_link(context, curie: object, label: object = None) -> Markup:
    """Render a displayed CURIE as a readable link.

    A CURIE that names one of this corpus's records links to that record's
    page, which is where a reader learns what it means. The page's own
    identifier is the exception: a link back to the same page goes nowhere, so
    it resolves the way the Identifier card does (METPO to w3id, a local id to
    its YAML). Everything else goes through curie_url().
    """
    if not isinstance(curie, str) or not curie.strip():
        return Markup("")
    value = curie.strip()
    code = Markup("<code>{}</code>").format(value)
    text = Markup("{} {}").format(label, code) if label else code
    trait = context.get("trait")
    own = trait.get("identifier") if isinstance(trait, dict) else None
    page_path = context.get("page_path") or {}
    if value != own and value in page_path:
        return Markup('<a href="{}{}">{}</a>').format(
            context.get("root") or "", page_path[value], text)
    if value == own and value.startswith(LOCAL_PREFIX + ":"):
        url = context.get("yaml_blob_url")
    else:
        url = curie_url(value)
    if url:
        return Markup('<a href="{}" rel="nofollow noreferrer">{}</a>').format(url, text)
    return text


# Reference tokens inside free text. URLs come first so a DOI or PMCID inside a
# URL stays part of that URL. Matching runs on the raw string and every piece is
# escaped on the way out, so record text can never become markup.
#
# Research previews are Markdown, so a token also ends at "]": in
# "[10.1038/x](https://doi.org/10.1038/x)" the parentheses balance, and without
# the stop the DOI swallowed "](https://...)" into its href (#2022). No DOI or
# URL in the corpus contains a bracket.
AUTOLINK_TOKEN = re.compile(
    r"(?P<url>\b(?i:https?)://[^\s<>\"\\\]]+)"
    r"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{4,9}/[^\s<>\"\\\]]+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
)
CLOSING = {")": "(", "]": "[", "}": "{"}
# Sentence punctuation, plus the Markdown emphasis and code marks that close a
# token written as **10.x/y** or `10.x/y`.
TRAILING = ".,;:!?'\"*`"


def _trim_token(token: str) -> str:
    """Cut a token at a closing parenthesis it never opened, then drop the
    punctuation, Markdown marks and unbalanced closers that end it.

    "(10.1016/0005-2744(70)90044-4)" keeps the DOI's own parentheses, while in
    "(https://a.org/x)-(https://b.org/y)" the first ")" closes the sentence's
    parenthesis, so the token ends there and the second URL is its own (#2033).
    """
    depth = 0
    for index, char in enumerate(token):
        depth += {"(": 1, ")": -1}.get(char, 0)
        if depth < 0:
            token = token[:index]
            break
    while token:
        last = token[-1]
        if last in TRAILING or (last in CLOSING and token.count(last) > token.count(CLOSING[last])):
            token = token[:-1]
            continue
        break
    return token


def _token_url(kind: str, token: str, match: re.Match[str]) -> str | None:
    if kind == "url":
        return reference_url(token)
    if kind == "doi":
        return reference_url("DOI:" + token[token.index("10."):])
    if kind == "pmid":
        return f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"


def autolink(value: object) -> Markup:
    """Escape free text and link the PMID, PMCID, DOI and http(s) URL tokens in it.

    Applied wherever record prose can carry a reference -- notes, snippets,
    rationale, change summaries, graph descriptions -- so a citation is
    followable wherever it appears, not only in the structured ``reference``
    slots the citation() macro handles. Surrounding text, including directive
    debris such as ``:ref{doi=...}``, is kept verbatim; only the token itself
    becomes the anchor, and only after reference_url() accepts its target.
    """
    if value is None:
        return Markup("")
    if isinstance(value, Markup):
        return value
    text = str(value)
    out: list[str] = []
    position = scan = 0
    while match := AUTOLINK_TOKEN.search(text, scan):
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind in {"url", "doi"}:
            token = _trim_token(token)
        url = _token_url(kind, token, match) if token else None
        if not url:
            scan = match.end()
            continue
        out.append(escape(text[position:match.start()]))
        out.append(Markup('<a href="{}" rel="nofollow noreferrer">{}</a>').format(url, token))
        # Resume after the token, not the match: what trimming cut off may hold
        # the next citation, as in "(https://a.org/x)-(https://b.org/y)".
        position = scan = match.start() + len(token)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def template_environment() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["reference_url"] = reference_url
    env.filters["curie_url"] = curie_url
    env.filters["term_link"] = term_link
    env.filters["autolink"] = autolink
    return env


def slugify(label: str | None, fallback: str) -> str:
    if not label:
        return fallback
    s = label.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_") or fallback


def load_metpo_version(owl_path: Path) -> str:
    if not owl_path.exists():
        return "unknown"
    head = owl_path.read_text()[:4000]
    m = re.search(r"<owl:versionInfo>([^<]+)</owl:versionInfo>", head)
    return m.group(1).strip() if m else "unknown"


def load_traits() -> list[tuple[Path, dict]]:
    out: list[tuple[Path, dict]] = []
    for path in sorted(TRAITS_DIR.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except Exception:
            continue
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


def corpus_timestamp(traits: list[tuple[Path, dict]]) -> str:
    """The latest ``curation_history`` timestamp across all records.

    Deliberately NOT ``datetime.now()``. A wall-clock stamp made every page
    differ on every run, so ``pages/`` could not be checked by regenerating and
    diffing — the technique that guards the grounding residuals (#214) and the
    causal-graph audit (#223). With no way to check, it drifted silently: 119
    pages were stale by four weeks before anyone noticed (#228).

    It is also the more useful answer. A reader wants to know "current as of
    what corpus state?", and the wall-clock time of the last ``just gen-pages``
    invocation does not tell them that — a rebuild with no data change moved it
    forward, and a data change with no rebuild did not.

    Falls back to the empty string rather than to the clock: no timestamps means
    no defensible claim about currency, and inventing one would restore exactly
    the nondeterminism this removes.
    """
    latest: datetime | None = None
    for _path, doc in traits:
        for entry in (doc.get("curation_history") or []):
            parsed = _as_utc(entry.get("timestamp"))
            if parsed is None:
                continue
            if latest is None or parsed > latest:
                latest = parsed
    return latest.strftime("%Y-%m-%d %H:%M UTC") if latest else ""


def synonym_search_text(doc: dict) -> str:
    """Index synonym names, never metadata keys or their serialized mappings."""
    return " ".join(value.get("synonym_text", "") if isinstance(value, dict) else value
                    for value in (doc.get("synonyms") or [])
                    if isinstance(value, (dict, str)))


def load_record_sessions(root: Path = REPO_ROOT) -> dict[str, list[dict]]:
    sessions: dict[str, list[dict]] = defaultdict(list)
    for path in sorted((root / "history" / "records").glob("*/*.yaml")):
        entry = yaml.safe_load(path.read_text())
        entry["source_url"] = f"{GH_BLOB_BASE}/{path.relative_to(root).as_posix()}"
        sessions[entry["target"]["path"]].append(entry)
    return dict(sessions)


def record_timestamp(doc: dict, sessions: list[dict] | None = None) -> str:
    """The latest ``curation_history`` timestamp for ONE record.

    Trait pages carry this rather than the corpus-wide stamp (#304). The
    corpus value is genuinely global, so storing 477 copies of it meant every
    PR that appended a curation event — i.e. every data PR, since the playbook
    requires one — rewrote all 477 pages. PR #300 changed 14 trait files and
    produced a 508-file diff, 477 of them nothing but a footer timestamp, which
    buries the real change and makes `pages/` conflict spuriously between
    concurrent data PRs.

    A per-record stamp fixes that without losing information: it changes only
    when that record changes, and "when was THIS trait last curated" is the more
    useful question on a trait page anyway. The corpus-wide stamp still appears
    on the aggregate pages, where it is a property of the thing being shown.
    """
    latest: datetime | None = None
    timestamps = [entry.get("timestamp") for entry in (doc.get("curation_history") or [])]
    timestamps += [entry["session"]["timestamp"] for entry in (sessions or [])]
    for timestamp in timestamps:
        parsed = _as_utc(timestamp)
        if parsed is None:
            continue
        if latest is None or parsed > latest:
            latest = parsed
    return latest.strftime("%Y-%m-%d %H:%M UTC") if latest else ""


def _as_utc(raw: object) -> datetime | None:
    """Coerce a curation_history timestamp to an aware UTC datetime.

    Handles both YAML shapes, which is not optional: PyYAML resolves an
    *unquoted* ISO timestamp to a ``datetime`` and a quoted one to ``str``. All
    3341 timestamps in the corpus are currently quoted, but nothing enforces
    that — so accepting only ``str`` would silently drop any record a curator or
    writer script emitted unquoted, and the page stamp would go stale or
    backwards with no signal. Silent zero is the failure mode this whole thread
    keeps finding (#214, #223, #228).

    Strings mix offsets and the 'Z' suffix ('...+00:00', '...-07:00', '...Z'),
    so they are normalised before parsing. Everything is compared in UTC —
    otherwise "latest" would depend on which offset a curator's machine used.
    Naive values are assumed UTC rather than discarded.
    """
    if isinstance(raw, datetime):
        parsed = raw
    elif isinstance(raw, str):
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return None
    else:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def load_match_table() -> dict[str, dict]:
    """Return {METPO CURIE → match-row dict}."""
    out: dict[str, dict] = {}
    path = EMBED_DIR / "metpo_to_kgm_node.tsv"
    if not path.exists():
        return out
    with path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            curie = (row.get("metpo_curie") or "").strip()
            if not curie:
                continue
            n = int(row.get("n_kgm_nodes") or 0)
            nodes = [n.strip() for n in (row.get("kgm_nodes") or "").split(";") if n.strip()]
            out[curie] = {
                "metpo_curie": curie,
                "label": row.get("label", ""),
                "category": row.get("category", ""),
                "match_method": row.get("match_method", ""),
                "n_kgm_nodes": n,
                "kgm_nodes": nodes,
            }
    return out


def load_node_dim_preview(needed_nodes: set[str]) -> dict[str, str]:
    """Return {kg-microbe node → '[d0, d1, d2, …]' truncated preview} for the
    subset of nodes referenced by any matched TraitRecord."""
    out: dict[str, str] = {}
    if not needed_nodes:
        return out
    path = EMBED_DIR / "deepwalk_traits.tsv.gz"
    if not path.exists():
        return out
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for raw in f:
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            sid = parts[0]
            if sid in needed_nodes:
                dims = parts[1:1 + DIM_PREVIEW]
                if dims and dims[0] in ("0", "0.0", ""):
                    # Header / index column? skip.
                    if all(d.isdigit() for d in dims if d):
                        continue
                preview = ", ".join(f"{float(d):+.3f}" for d in dims if d)
                out[sid] = f"[{preview}, …]"
    return out


def reciprocal_neighbor_edges(
    neighbors: dict[str, list[dict]], point_ids: set[str]
) -> list[dict[str, str]]:
    """Return stable undirected edges where both records name each other.

    ``trait_nearest_neighbors.json`` is the committed similarity input available
    to the page renderer. Requiring reciprocity avoids drawing every one-way
    top-k suggestion as if it were equally strong, while still making the sfdp
    view an actual graph rather than a second edge-free scatterplot (#151).
    """
    directed = {
        source: {
            row.get("id")
            for row in rows
            if isinstance(row, dict) and row.get("id") in point_ids
        }
        for source, rows in neighbors.items()
        if source in point_ids
    }
    pairs = {
        tuple(sorted((source, target)))
        for source, targets in directed.items()
        for target in targets
        if source != target and source in directed.get(target, set())
    }
    return [{"source": source, "target": target} for source, target in sorted(pairs)]


def research_report(category_dir: str, slug: str) -> Path | None:
    """Return this trait's deep-research report, or None if it has none.

    Matches what the pipeline writes — `<slug>-deep-research-<provider>.md` —
    and picks by RESEARCH_PROVIDERS when a trait has more than one.
    """
    candidates = [
        path
        for path in RESEARCH_DIR.glob(f"{category_dir}/{slug}-deep-research-*.md")
        # Sidecars match the same glob and are reference lists, not reports.
        # Both separators, because the tree spells this two ways: the pipeline
        # wrote `<report>.md.citations.md` until #249 stopped requesting it,
        # while _edison_capture bundles use `<stem>-citations.md`. Neither form
        # is produced for these reports today and the 353 dot-form files are
        # deleted, so this exclusion currently matches nothing — it stays
        # because _edison_capture can still emit the hyphen form, which would
        # fail silently rather than loudly: it survives a
        # dot-only exclusion, and for an unrecognised provider sorts ahead of its
        # own report ('-' < '.'), so the page would render the bibliography (#259).
        if not re.search(r"[-.]citations\.md$", path.name)
        # A hand-supplied artifact (`pipeline_run: false`) is not a research
        # report: it answers a discussion hypothesis, echoes no prompt, and has
        # no manifest row. Ranking it as the sweep's own would put an
        # unaccounted-for answer on the page (#643).
        and is_pipeline_report(path)
    ]
    if not candidates:
        return None

    def rank(path: Path) -> tuple[int, str]:
        provider = path.stem[len(f"{slug}-deep-research-"):]
        known = provider in RESEARCH_PROVIDERS
        return (RESEARCH_PROVIDERS.index(provider) if known
                else len(RESEARCH_PROVIDERS), path.name)

    return min(candidates, key=rank)


def research_answer(text: str) -> list[str]:
    """Strip a report's front matter and echoed prompt, leaving the answer."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                lines = lines[i + 1:]
                break
    # The prompt is echoed exactly twice, so the second marker is the boundary.
    # Anchoring on the LAST one instead would be identical today and fails
    # unsafely: a report whose answer quotes the instruction line — reports do
    # discuss what should not be curated — would be cut mid-answer, silently
    # dropping findings. Overshooting the other way only leaves some boilerplate
    # in the preview (#255).
    marks = [i for i, line in enumerate(lines) if RESEARCH_PROMPT_TAIL in line]
    if marks:
        lines = lines[marks[min(1, len(marks) - 1)] + 1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    return lines


def schema_reference(schema_path: Path = SCHEMA_PATH) -> dict:
    """Readable documentation of the record schema, read from the schema itself.

    docs/SCHEMA.md is a hand-written quick reference that has already fallen
    behind the schema it describes, so the site documents what LinkML resolves
    instead: every class with its induced slots (imports and slot_usage
    applied), and every enum with its permissible values. The output follows
    the schema's own declaration order and carries no clock, so an unchanged
    schema renders byte-identically under the pages/ staleness gate.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(schema_path))
    view.imports_closure()
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.exists():
            module_file[schema.id] = source.relative_to(REPO_ROOT).as_posix()
    classes = view.all_classes()
    enums = view.all_enums()
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]

    def range_kind(name: str | None) -> str:
        if name in classes:
            return "class"
        if name in enums:
            return "enum"
        return "type"

    def slot_row(slot) -> dict:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        ranges = names or [slot.range or view.schema.default_range or "string"]
        return {
            "name": slot.name,
            "ranges": [{"name": name, "kind": range_kind(name)} for name in ranges],
            "required": bool(slot.required or slot.identifier),
            "multivalued": bool(slot.multivalued),
            "identifier": bool(slot.identifier),
            "pattern": slot.pattern or "",
            "description": slot.description or "",
        }

    def source_of(element) -> str:
        return module_file.get(element.from_schema, "")

    return {
        "title": view.schema.title or view.schema.name,
        "description": view.schema.description or "",
        "license": view.schema.license or "",
        "source": schema_path.relative_to(REPO_ROOT).as_posix(),
        "modules": sorted(set(module_file.values())),
        "classes": [{
            "name": name,
            "description": classes[name].description or "",
            "is_a": classes[name].is_a or "",
            "source": source_of(classes[name]),
            "slots": [slot_row(slot) for slot in view.class_induced_slots(name)],
        } for name in ordered],
        "enums": [{
            "name": name,
            "description": enum.description or "",
            "source": source_of(enum),
            "permissible": [{"text": text, "description": value.description or "",
                        "meaning": value.meaning or ""}
                       for text, value in (enum.permissible_values or {}).items()],
        } for name, enum in enums.items()],
    }


def mapping_statuses(schema: dict) -> list[dict]:
    """MappingStatusEnum's values with their descriptions, as the schema states them.

    Pages quote these rather than paraphrase them, so a page cannot claim more
    about a status (who reviewed a record, and how) than the schema does.
    """
    return next(enum["permissible"] for enum in schema["enums"]
                if enum["name"] == "MappingStatusEnum")


# GitHub Pages answers a missing URL at any depth with the publishing root's
# 404.html, served at the address the reader asked for. Relative links would
# resolve against that missing path, so the page uses site-root-absolute ones.
SITE_ROOT = "/TraitMech/"


def render_not_found(env: Environment) -> str:
    """The themed not-found page, independent of corpus state."""
    return env.get_template("404.html").render(
        title="Page not found", root=SITE_ROOT + "pages/")


def render_pages(args: argparse.Namespace) -> int:
    # Output root is a parameter, not the module constant, so the staleness gate
    # can render into a temp dir and diff (#230). Checking must never dirty the
    # tree — that is half of what #214 was about — and this function wipes and
    # recreates its output root, so pointing it at pages/ to verify pages/ would
    # destroy the very thing being compared.
    pages_dir = args.out or PAGES_DIR
    if not TEMPLATES_DIR.exists():
        print(f"templates missing: {TEMPLATES_DIR}", file=sys.stderr)
        return 2
    env = template_environment()
    metpo_version = load_metpo_version(RAW_OWL)
    traits = load_traits()
    match_table = load_match_table()
    # One value for every page in the run, derived from the data (#228).
    corpus_stamp = corpus_timestamp(traits)
    record_sessions = load_record_sessions()
    schema = schema_reference()
    statuses = mapping_statuses(schema)
    status_meanings = {value["text"]: value["description"] for value in statuses}

    if args.dry_run:
        print(f"[dry-run] {len(traits)} traits; {sum(1 for v in match_table.values() if v['n_kgm_nodes'] > 0)} matched")
        return 0

    # Wipe output dir for a clean build.
    if pages_dir.exists() and args.clean:
        shutil.rmtree(pages_dir)

    pages_dir.mkdir(parents=True, exist_ok=True)
    (pages_dir / "category").mkdir(exist_ok=True)
    (pages_dir / "assets").mkdir(exist_ok=True)
    shutil.copyfile(TEMPLATES_DIR / "style.css", pages_dir / "assets" / "style.css")
    shutil.copyfile(TEMPLATES_DIR / "record-browser.js", pages_dir / "assets" / "record-browser.js")

    # Build category, slug, parent indexes.
    by_curie: dict[str, dict] = {curie: doc for path, doc in traits if (curie := doc.get("identifier"))}
    page_path: dict[str, str] = {}
    parent_labels: dict[str, str] = {curie: doc.get("label", "") for curie, doc in by_curie.items()}
    children_by_parent: dict[str, list[dict]] = defaultdict(list)
    category_lists: dict[str, list[dict]] = defaultdict(list)

    for path, doc in traits:
        rel = path.relative_to(TRAITS_DIR)
        category_dir = rel.parts[0]
        slug = path.stem
        page = f"traits/{category_dir}/{slug}.html"
        curie = doc.get("identifier", "")
        if curie:
            page_path[curie] = page
        for p in (doc.get("parent_traits") or []):
            children_by_parent[p].append({
                "curie": curie,
                "label": doc.get("label", ""),
                "page": page,
            })

    # Collect deepwalk preview for the matched nodes only.
    needed_nodes: set[str] = set()
    for v in match_table.values():
        needed_nodes.update(v["kgm_nodes"])
    node_dim_preview = load_node_dim_preview(needed_nodes)

    # Load nearest-neighbors map (built by build_embedding_index.py).
    nn_by_curie: dict[str, list[dict]] = {}
    if NN_JSON.exists():
        import json as _json
        nn_by_curie = _json.loads(NN_JSON.read_text())

    # Render per-trait pages.
    written = 0
    for path, doc in traits:
        rel = path.relative_to(TRAITS_DIR)
        category_dir = rel.parts[0]
        slug = path.stem
        page = f"traits/{category_dir}/{slug}.html"
        out_path = pages_dir / "traits" / category_dir / f"{slug}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        curie = doc.get("identifier", "")
        match = match_table.get(curie, {"n_kgm_nodes": 0, "kgm_nodes": [], "match_method": "no_match"})

        parent_pages = {p: page_path.get(p, "") for p in (doc.get("parent_traits") or [])}
        children = sorted(children_by_parent.get(curie, []), key=lambda x: x["label"])

        yaml_rel = f"data/traits/{category_dir}/{slug}.yaml"

        # Deep-research output. The renderer treats the report as an opaque
        # markdown blob and hands it to the template as a string. No file →
        # research section is hidden entirely.
        research_path = research_report(category_dir, slug)
        research_rel = (
            research_path.relative_to(REPO_ROOT).as_posix() if research_path else ""
        )
        research_lines = (
            research_answer(research_path.read_text()) if research_path else []
        )
        research_md = "\n".join(research_lines[:RESEARCH_PREVIEW_LINES])
        research_total_lines = len(research_lines)
        research_shown_lines = min(research_total_lines, RESEARCH_PREVIEW_LINES)

        # Resolve nearest-neighbor records into renderable rows with page links.
        nn_rows = []
        for nn in nn_by_curie.get(curie, []):
            nn_curie = nn.get("id", "")
            nn_page = page_path.get(nn_curie)
            if not nn_page:
                continue
            nn_rows.append({
                "curie": nn_curie,
                "label": nn.get("label", ""),
                "category": nn.get("category", ""),
                "similarity": nn.get("similarity", 0.0),
                "page": nn_page,
            })

        page_html = env.get_template("trait.html").render(
            title=f"{doc.get('label', curie)} — {doc.get('trait_category', '')}",
            root="../../",
            trait=doc,
            causal_graphs=causal_graphs_for_template(doc),
            kgm_match=match,
            node_dim_preview=node_dim_preview,
            parent_pages=parent_pages,
            parent_labels=parent_labels,
            page_path=page_path,
            status_meanings=status_meanings,
            children=children,
            nearest_neighbors=nn_rows,
            research_md=research_md,
            research_path=research_rel,
            research_total_lines=research_total_lines,
            research_shown_lines=research_shown_lines,
            research_blob_url=(
                f"{GH_BLOB_BASE}/{research_rel}" if research_rel else ""
            ),
            embedding_release=EMBEDDING_RELEASE,
            metpo_version=metpo_version,
            yaml_path=yaml_rel,
            yaml_blob_url=f"{GH_BLOB_BASE}/{yaml_rel}",
            yaml_raw_url=f"{GH_RAW_BASE}/{yaml_rel}",
            yaml_edit_url=f"{GH_EDIT_BASE}/{yaml_rel}",
            generated_at=record_timestamp(doc, record_sessions.get(yaml_rel, [])),
            curation_sessions=record_sessions.get(yaml_rel, []),
            stamp_scope="Record",
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(out_path, page_html)
        written += 1

        category_lists[doc.get("trait_category", "OTHER")].append({
            "curie": curie,
            "label": doc.get("label", ""),
            "page": page,
            "term_kind": doc.get("term_kind", ""),
            "n_kgm_nodes": match.get("n_kgm_nodes", 0),
            "synonyms_count": len(doc.get("synonyms") or []),
            "identifier": curie,
            "definition": doc.get("definition", ""),
            "category": doc.get("trait_category", "OTHER"),
            "kind": doc.get("term_kind", ""),
            "synonyms": synonym_search_text(doc),
        })

    # Render category index pages.
    for cat, items in category_lists.items():
        items.sort(key=lambda x: x["label"])
        out_path = pages_dir / "category" / f"{cat.lower()}.html"
        page_html = env.get_template("category.html").render(
            title=cat,
            root="../",
            category=cat,
            traits=items,
            metpo_version=metpo_version,
            generated_at=corpus_stamp,
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(out_path, page_html)

    # Render UMAP page if data exists.
    if UMAP_JSON.exists():
        umap_data_dst = pages_dir / "data" / "trait_umap.json"
        umap_data_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(UMAP_JSON, umap_data_dst)
        import json as _json
        umap_points = _json.loads(UMAP_JSON.read_text())
        umap_html = env.get_template("umap.html").render(
            title="Trait embedding space",
            root="",
            data_url="data/trait_umap.json",
            href_by_id=_json.dumps({p["id"]: page_path.get(p["id"], "") for p in umap_points}).replace("</", "<\\/"),
            n_points=len(umap_points),
            metpo_version=metpo_version,
            generated_at=corpus_stamp,
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(pages_dir / "umap.html", umap_html)

    # Render sfdp graph-layout page if data exists.
    if GRAPH_JSON.exists():
        graph_data_dst = pages_dir / "data" / "trait_graph.json"
        graph_data_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(GRAPH_JSON, graph_data_dst)
        import json as _json
        graph_points = _json.loads(GRAPH_JSON.read_text())
        graph_edges = reciprocal_neighbor_edges(
            nn_by_curie, {point["id"] for point in graph_points}
        )
        graph_html = env.get_template("graph.html").render(
            title="Trait graph layout (sfdp)",
            root="",
            data_url="data/trait_graph.json",
            href_by_id=_json.dumps({p["id"]: page_path.get(p["id"], "") for p in graph_points}).replace("</", "<\\/"),
            graph_edges=_json.dumps(graph_edges).replace("</", "<\\/"),
            n_points=len(graph_points),
            n_edges=len(graph_edges),
            metpo_version=metpo_version,
            generated_at=corpus_stamp,
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(pages_dir / "graph.html", graph_html)

    # Render full-corpus text embedding map (BGE-large + PaCMAP) if data exists.
    if CORPUS_MAP_JSON.exists():
        corpus_map_dst = pages_dir / "data" / "corpus_map.json"
        corpus_map_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CORPUS_MAP_JSON, corpus_map_dst)
        import json as _json
        corpus_raw = _json.loads(CORPUS_MAP_JSON.read_text())
        corpus_pts = corpus_raw if isinstance(corpus_raw, list) else corpus_raw.get("points", [])
        map_html = env.get_template("map.html").render(
            title="Full-corpus text embedding map",
            root="",
            data_url="data/corpus_map.json",
            n_points=len(corpus_pts),
            metpo_version=metpo_version,
            generated_at=corpus_stamp,
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(pages_dir / "map.html", map_html)

    # Render ESM-2 protein sequence embedding map if data exists.
    if SEQUENCE_MAP_JSON.exists():
        seq_map_dst = pages_dir / "data" / "sequence_map.json"
        seq_map_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SEQUENCE_MAP_JSON, seq_map_dst)
        import json as _json
        seq_raw = _json.loads(SEQUENCE_MAP_JSON.read_text())
        seq_pts = seq_raw if isinstance(seq_raw, list) else seq_raw.get("points", [])
        seq_html = env.get_template("sequence-map.html").render(
            title="Protein sequence embedding map (ESM-2 pLM)",
            root="",
            data_url="data/sequence_map.json",
            n_points=len(seq_pts),
            metpo_version=metpo_version,
            generated_at=corpus_stamp,
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        write_html(pages_dir / "sequence-map.html", seq_html)

    # Render landing page.
    category_counts = {cat: len(items) for cat, items in sorted(category_lists.items(), key=lambda x: -len(x[1]))}
    embedding_per_category: dict[str, int] = defaultdict(int)
    for cat, items in category_lists.items():
        for it in items:
            if it["n_kgm_nodes"] > 0:
                embedding_per_category[cat] += 1
    embedded_count = sum(1 for v in match_table.values() if v["n_kgm_nodes"] > 0)
    landing = env.get_template("index.html").render(
        title="Microbial trait knowledge base",
        root="",
        total_traits=len(traits),
        embedded_count=embedded_count,
        embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        category_counts=category_counts,
        embedding_per_category=dict(embedding_per_category),
        metpo_version=metpo_version,
        generated_at=corpus_stamp,
        statuses=statuses,
        status_counts=Counter(doc.get("mapping_status") for _path, doc in traits),
    )
    write_html(pages_dir / "index.html", landing)

    # Render the searchable catalogue and retain category navigation.
    browse = env.get_template("browse.html").render(
        title="Record browser",
        root="",
        traits=sorted((item for items in category_lists.values() for item in items),
                      key=lambda item: item["label"].lower()),
        total_traits=len(traits),
        embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        category_counts=category_counts,
        embedding_per_category=dict(embedding_per_category),
        metpo_version=metpo_version,
        generated_at=corpus_stamp,
    )
    write_html(pages_dir / "browse.html", browse)

    # Readable schema documentation, generated from the LinkML schema.
    schema_html = env.get_template("schema.html").render(
        title="LinkML schema",
        root="",
        schema=schema,
        gh_blob_base=GH_BLOB_BASE,
        metpo_version=metpo_version,
        generated_at=corpus_stamp,
        total_traits=len(traits),
        embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
    )
    write_html(pages_dir / "schema.html", schema_html)

    # The site's not-found page belongs at the publishing root, which for this
    # branch-built site is the repository root, not pages/. A render into
    # another --out root (the staleness gate's temp dir) leaves it alone;
    # tests/test_unified_site_features.py checks the committed copy instead.
    if pages_dir.resolve() == PAGES_DIR.resolve():
        write_html(REPO_ROOT / "404.html", render_not_found(env))

    # Write bulk corpus JSON export for downstream consumers.
    import json as _json
    traits_json_dst = pages_dir / "data" / "traits.json"
    traits_json_dst.parent.mkdir(parents=True, exist_ok=True)
    traits_json_dst.write_text(
        _json.dumps([doc for _path, doc in traits], indent=2, default=str) + "\n"
    )

    print(f"Wrote {written} trait pages")
    print(f"Wrote {len(category_lists)} category index pages")
    print("Wrote pages/index.html")
    print("Wrote pages/browse.html")
    print("Wrote pages/schema.html")
    if pages_dir.resolve() == PAGES_DIR.resolve():
        print("Wrote 404.html")
    print(f"Coverage: {embedded_count}/{len(traits)} ({_coverage_pct(match_table, len(traits))}%)")
    return 0


def write_html(path: Path, text: str) -> None:
    """Write rendered HTML without invisible line-end drift."""
    path.write_text("\n".join("" if not line.strip() else line.rstrip()
                              for line in text.split("\n")))


def _coverage_pct(match_table: dict[str, dict], n: int) -> str:
    if n == 0:
        return "0.0"
    matched = sum(1 for v in match_table.values() if v["n_kgm_nodes"] > 0)
    return f"{matched / n * 100:.1f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="report counts without writing pages/")
    ap.add_argument("--clean", action="store_true",
                    help="remove pages/ before rendering")
    ap.add_argument("--out", type=Path, default=None,
                    help="output root (default: pages/); used by the staleness "
                         "gate to render into a temp dir")
    return render_pages(ap.parse_args())


if __name__ == "__main__":
    sys.exit(main())
