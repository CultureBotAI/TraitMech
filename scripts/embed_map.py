#!/usr/bin/env python3
"""2-D map of the TraitMech corpus from record text embeddings -> data/embeddings/corpus_map.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EMB = REPO_ROOT / "data" / "embeddings"
OUT = EMB / "corpus_map.json"


def pca_2d(x):
    import numpy as np

    xc = x - x.mean(0)
    cov = (xc.T @ xc) / (len(xc) - 1)
    evals, evecs = np.linalg.eigh(cov)
    order = evals.argsort()[::-1]
    coords = xc @ evecs[:, order[:2]]
    return coords, (evals[order[:2]] / evals.sum()).tolist()


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--method", choices=["pacmap", "umap", "pca"], default="pacmap")
    ap.add_argument("--neighbors", type=int, default=15)
    ap.add_argument("--min-dist", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    import numpy as np

    vpath = EMB / "vectors.f16.npy"
    if not vpath.exists():
        print("no vectors — run `python scripts/embed_records.py` first")
        return 2
    vectors = np.load(vpath).astype(np.float32)
    ids = json.loads((EMB / "ids.json").read_text(encoding="utf-8"))
    meta = json.loads((EMB / "records.json").read_text(encoding="utf-8"))
    by_id = {m["id"]: m for m in meta}
    if len(ids) != vectors.shape[0]:
        print(f"ids ({len(ids)}) and vectors ({vectors.shape[0]}) disagree")
        return 2

    explained = None
    if args.method == "pca":
        coords, explained = pca_2d(vectors)
    elif args.method == "umap":
        import umap

        coords = umap.UMAP(
            n_neighbors=args.neighbors,
            min_dist=args.min_dist,
            metric="cosine",
            random_state=args.seed,
        ).fit_transform(vectors)
    else:
        import pacmap

        coords = pacmap.PaCMAP(
            n_neighbors=args.neighbors, random_state=args.seed
        ).fit_transform(vectors)
    coords = np.asarray(coords, dtype=np.float32)

    lo, hi = coords.min(0), coords.max(0)
    span = np.where(hi - lo == 0, 1.0, hi - lo)
    unit = (coords - lo) / span

    classes = sorted({(by_id.get(i) or {}).get("class") or "OTHER" for i in ids})
    index = {c: n for n, c in enumerate(classes)}
    points = []
    hrefs: dict[str, str] = {}
    for n, identifier in enumerate(ids):
        m = by_id.get(identifier) or {}
        cls_name = m.get("class") or "OTHER"
        href = m.get("href") or f"traits/{m.get('slug', identifier)}.html"
        hrefs[identifier] = href
        points.append(
            {
                "x": round(float(unit[n][0]), 4),
                "y": round(float(unit[n][1]), 4),
                "classIdx": index[cls_name],
                "class": cls_name,
                "category": cls_name,
                "id": identifier,
                "label": m.get("label") or identifier,
                "term_kind": m.get("term_kind") or cls_name,
                "taxon": m.get("taxon") or "Multiple / unspecified",
                "href": href,
            }
        )

    emb_meta = json.loads((EMB / "meta.json").read_text(encoding="utf-8"))
    model = emb_meta.get("model", "")
    payload = {
        "method": args.method,
        "model": model,
        "n": len(points),
        "corpus_fingerprint": emb_meta.get("corpus_fingerprint"),
        "classes": classes,
        "generated_from": "scripts/embed_map.py",
        "hrefs": hrefs,
        "points": points,
    }
    if explained:
        payload["explained"] = [round(e, 4) for e in explained]
    OUT.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
    print(
        f"{len(points):,} points ({args.method}) -> {OUT.relative_to(REPO_ROOT)} "
        f"({OUT.stat().st_size / 1024:.1f} KB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
