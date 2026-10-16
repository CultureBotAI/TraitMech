#!/usr/bin/env python3
"""Text-embed every TraitMech trait record into a dense vector with a LOCAL model.

Output (data/embeddings/, vectors gitignored — large and rebuildable):
  vectors.f16.npy   float16 [N, dim], L2-normalized, row i <-> ids[i]
  ids.json          the N record identifiers, in row order
  records.json      light metadata per record (id, slug, href, label, category, class, term_kind, taxon)
  meta.json         {model, dim, count, normalized, excluded_fields, corpus_fingerprint}
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "traits"
OUT = REPO_ROOT / "data" / "embeddings"

EXCLUDED = (
    "curation_history",
    "created_by",
    "definition_source",
)


def humanize(value: str) -> str:
    return (value or "").replace("_", " ").replace("-", " ").strip()


def extract_taxa(record: dict) -> list[str]:
    taxa: list[str] = []
    for ex in record.get("canonical_examples") or []:
        if isinstance(ex, dict):
            lbl = ex.get("taxon_label") or ex.get("taxon_id")
            if lbl:
                taxa.append(str(lbl))
    for g in record.get("causal_graphs") or []:
        if not isinstance(g, dict):
            continue
        for node in g.get("nodes") or []:
            if not isinstance(node, dict):
                continue
            for pex in node.get("protein_examples") or []:
                if isinstance(pex, dict):
                    tl = pex.get("taxon_label") or pex.get("taxon_id")
                    if tl:
                        taxa.append(str(tl))
    return list(dict.fromkeys(taxa))


def build_document(record: dict) -> str:
    """One document per trait record, ordered most discriminative first."""
    parts: list[str] = [str(record.get("label") or record.get("identifier"))]

    cat = humanize(str(record.get("trait_category") or ""))
    kind = humanize(str(record.get("term_kind") or ""))
    if cat or kind:
        parts.append(f"trait category: {cat} ({kind})".strip())

    if record.get("definition"):
        parts.append(str(record["definition"]))

    syns = [
        str(s.get("synonym_text") if isinstance(s, dict) else s)
        for s in (record.get("synonyms") or [])
        if isinstance(s, (dict, str))
    ]
    syns = [s for s in dict.fromkeys(syns) if s]
    if syns:
        parts.append("synonyms: " + ", ".join(syns[:12]))

    taxa = extract_taxa(record)
    if taxa:
        parts.append("canonical organisms: " + ", ".join(taxa[:8]))

    graph_nodes: list[str] = []
    proteins: list[str] = []
    for g in record.get("causal_graphs") or []:
        if not isinstance(g, dict):
            continue
        if g.get("title"):
            graph_nodes.append(str(g["title"]))
        for node in g.get("nodes") or []:
            if not isinstance(node, dict):
                continue
            nlbl = node.get("label") or node.get("node_id")
            if nlbl:
                graph_nodes.append(str(nlbl))
            for pex in node.get("protein_examples") or []:
                if isinstance(pex, dict):
                    plbl = pex.get("protein_label") or pex.get("gene_symbol") or pex.get("uniprot_id")
                    if plbl:
                        proteins.append(str(plbl))
    if graph_nodes:
        parts.append("mechanisms and causal graph nodes: " + ", ".join(list(dict.fromkeys(graph_nodes))[:18]))
    if proteins:
        parts.append("proteins and genes: " + ", ".join(list(dict.fromkeys(proteins))[:14]))

    ground = [str(record.get("identifier") or "")]
    for x in record.get("xrefs") or []:
        if x:
            ground.append(str(x))
    for p in record.get("parent_traits") or []:
        if p:
            ground.append(str(p))
    ground = list(dict.fromkeys(g for g in ground if g))[:12]
    if ground:
        parts.append("identifiers: " + ", ".join(ground))

    return ". ".join(p.rstrip().rstrip(".") for p in parts if p and p.strip())


def corpus_fingerprint(docs: list[str]) -> str:
    return hashlib.sha256("\x1f".join(docs).encode("utf-8")).hexdigest()[:16]


def load_corpus() -> tuple[list[str], list[str], list[dict]]:
    rows: list[tuple[Path, dict]] = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(record, dict) or not record.get("identifier"):
            continue
        rows.append((path, record))
    rows.sort(key=lambda item: str(item[1]["identifier"]))
    ids = [str(r["identifier"]) for _, r in rows]
    docs = [build_document(r) for _, r in rows]
    meta = []
    for path, r in rows:
        rel = path.relative_to(CORPUS_DIR)
        category_dir = rel.parts[0]
        slug = path.stem
        cat = str(r.get("trait_category") or "OTHER")
        taxa = extract_taxa(r)
        meta.append(
            {
                "id": str(r["identifier"]),
                "slug": f"{category_dir}/{slug}",
                "href": f"traits/{category_dir}/{slug}.html",
                "label": str(r.get("label") or r["identifier"]),
                "category": cat,
                "class": cat,
                "term_kind": str(r.get("term_kind") or ""),
                "mapping_status": str(r.get("mapping_status") or ""),
                "taxon": ", ".join(taxa[:4]) if taxa else "Multiple / unspecified",
            }
        )
    return ids, docs, meta


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--model", default="BAAI/bge-large-en-v1.5")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--device", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ids, docs, meta = load_corpus()
    if not ids:
        print("no records found under data/traits/", file=sys.stderr)
        return 2
    if args.limit:
        ids, docs, meta = ids[: args.limit], docs[: args.limit], meta[: args.limit]

    if args.dry_run:
        print(f"{len(ids):,} records would be embedded with {args.model}\n")
        for i, d in zip(ids[:3], docs[:3], strict=True):
            print(f"--- {i} ---\n{d}\n")
        return 0

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = args.device or (
        "mps"
        if torch.backends.mps.is_available()
        else "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )
    print(f"{len(ids):,} records -> embedding with {args.model} on {device}")
    model = SentenceTransformer(args.model, device=device)
    vectors = model.encode(
        docs,
        batch_size=args.batch,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    OUT.mkdir(parents=True, exist_ok=True)
    np.save(OUT / "vectors.f16.npy", vectors.astype(np.float16))
    (OUT / "ids.json").write_text(json.dumps(ids), encoding="utf-8")
    (OUT / "records.json").write_text(json.dumps(meta), encoding="utf-8")
    (OUT / "meta.json").write_text(
        json.dumps(
            {
                "model": args.model,
                "dim": int(vectors.shape[1]),
                "count": len(ids),
                "normalized": True,
                "excluded_fields": list(EXCLUDED),
                "corpus_fingerprint": corpus_fingerprint(docs),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(
        f"wrote {vectors.shape[0]:,} x {vectors.shape[1]} vectors to "
        f"{OUT.relative_to(REPO_ROOT)}/"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
