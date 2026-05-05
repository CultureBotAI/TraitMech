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
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
EMBED_DIR = REPO_ROOT / "data" / "embeddings"
TEMPLATES_DIR = REPO_ROOT / "src" / "traitmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
RAW_OWL = REPO_ROOT / "data" / "raw" / "metpo.owl"

DIM_PREVIEW = 4  # number of dims to show inline next to each kg-microbe node

# GitHub URL bases for the right-rail source-link card.
GH_BLOB_BASE = "https://github.com/CultureBotAI/TraitMech/blob/main"
GH_RAW_BASE = "https://raw.githubusercontent.com/CultureBotAI/TraitMech/main"
GH_EDIT_BASE = "https://github.com/CultureBotAI/TraitMech/edit/main"


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


def render_pages(args: argparse.Namespace) -> int:
    if not TEMPLATES_DIR.exists():
        print(f"templates missing: {TEMPLATES_DIR}", file=sys.stderr)
        return 2
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    metpo_version = load_metpo_version(RAW_OWL)
    traits = load_traits()
    match_table = load_match_table()

    if args.dry_run:
        print(f"[dry-run] {len(traits)} traits; {sum(1 for v in match_table.values() if v['n_kgm_nodes'] > 0)} matched")
        return 0

    # Wipe output dir for a clean build.
    if PAGES_DIR.exists() and args.clean:
        shutil.rmtree(PAGES_DIR)

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    (PAGES_DIR / "category").mkdir(exist_ok=True)
    (PAGES_DIR / "assets").mkdir(exist_ok=True)
    shutil.copyfile(TEMPLATES_DIR / "style.css", PAGES_DIR / "assets" / "style.css")

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

    # Render per-trait pages.
    written = 0
    for path, doc in traits:
        rel = path.relative_to(TRAITS_DIR)
        category_dir = rel.parts[0]
        slug = path.stem
        page = f"traits/{category_dir}/{slug}.html"
        out_path = PAGES_DIR / "traits" / category_dir / f"{slug}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        curie = doc.get("identifier", "")
        match = match_table.get(curie, {"n_kgm_nodes": 0, "kgm_nodes": [], "match_method": "no_match"})

        parent_pages = {p: page_path.get(p, "") for p in (doc.get("parent_traits") or [])}
        children = sorted(children_by_parent.get(curie, []), key=lambda x: x["label"])

        yaml_rel = f"data/traits/{category_dir}/{slug}.yaml"
        page_html = env.get_template("trait.html").render(
            title=f"{doc.get('label', curie)} — {doc.get('trait_category', '')}",
            root="../../",
            trait=doc,
            kgm_match=match,
            node_dim_preview=node_dim_preview,
            parent_pages=parent_pages,
            parent_labels=parent_labels,
            children=children,
            metpo_version=metpo_version,
            yaml_path=yaml_rel,
            yaml_blob_url=f"{GH_BLOB_BASE}/{yaml_rel}",
            yaml_raw_url=f"{GH_RAW_BASE}/{yaml_rel}",
            yaml_edit_url=f"{GH_EDIT_BASE}/{yaml_rel}",
            generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        out_path.write_text(page_html)
        written += 1

        category_lists[doc.get("trait_category", "OTHER")].append({
            "curie": curie,
            "label": doc.get("label", ""),
            "page": page,
            "term_kind": doc.get("term_kind", ""),
            "n_kgm_nodes": match.get("n_kgm_nodes", 0),
            "synonyms_count": len(doc.get("synonyms") or []),
        })

    # Render category index pages.
    for cat, items in category_lists.items():
        items.sort(key=lambda x: x["label"])
        out_path = PAGES_DIR / "category" / f"{cat.lower()}.html"
        page_html = env.get_template("category.html").render(
            title=cat,
            root="../",
            category=cat,
            traits=items,
            metpo_version=metpo_version,
            generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            total_traits=len(traits),
            embedding_coverage_pct=_coverage_pct(match_table, len(traits)),
        )
        out_path.write_text(page_html)

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
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )
    (PAGES_DIR / "index.html").write_text(landing)

    print(f"Wrote {written} trait pages")
    print(f"Wrote {len(category_lists)} category index pages")
    print(f"Wrote pages/index.html")
    print(f"Coverage: {embedded_count}/{len(traits)} ({_coverage_pct(match_table, len(traits))}%)")
    return 0


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
    return render_pages(ap.parse_args())


if __name__ == "__main__":
    sys.exit(main())
