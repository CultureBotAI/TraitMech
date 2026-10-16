#!/usr/bin/env python3
"""2-D map of TraitMech-grounded proteins from ESM-2 sequence embeddings -> data/embeddings/sequence_map.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SIBLING_PTM = REPO_ROOT.parent / "ProteinTraitsMech"
CORPUS_DIR = REPO_ROOT / "data" / "traits"
OUT = REPO_ROOT / "data" / "embeddings" / "sequence_map.json"

DEFAULT_MENTIONS = SIBLING_PTM / "data" / "cross_mech" / "protein_mentions.jsonl"
DEFAULT_SEQUENCES = SIBLING_PTM / "data" / "cross_mech" / "protein_sequences.jsonl"
DEFAULT_INVENTORY = SIBLING_PTM / "data" / "cross_mech" / "protein_inventory.jsonl"
SHARED_CACHE_DIR = Path("/tmp/cross-mech-esm2-cache")
DEFAULT_CACHE_DIRS = (
    SIBLING_PTM / "data" / "embeddings" / "esm2",
    SHARED_CACHE_DIR,
)

MODEL = "facebook/esm2_t33_650M_UR50D"
REVISION = "08e4846e537177426273712802403f7ba8261b6c"
MAX_RESIDUES = 1022
OVERLAP = 256
VALID_SEQUENCE = re.compile(r"^[A-Z]+$")


def cache_key(model: str, revision: str, dtype: str) -> str:
    return hashlib.sha256(f"{model}@{revision}@{dtype}".encode()).hexdigest()[:12]


def windows(
    length: int, window: int = MAX_RESIDUES, overlap: int = OVERLAP
) -> list[tuple[int, int]]:
    if length <= window:
        return [(0, length)]
    stride = window - overlap
    out = []
    start = 0
    while True:
        end = min(start + window, length)
        out.append((start, end))
        if end >= length:
            return out
        start += stride


def find_esm2_caches(explicit: Path | None) -> list[tuple[Path, Path]]:
    dirs = [explicit] if explicit else list(DEFAULT_CACHE_DIRS)
    found: list[tuple[Path, Path]] = []
    for d in dirs:
        if not d or not d.exists():
            continue
        for meta_path in sorted(d.glob("cache_*.json")):
            vec_path = meta_path.with_suffix(".f32.npy")
            if vec_path.exists():
                found.append((meta_path, vec_path))
    if not found:
        raise FileNotFoundError(
            "No ESM-2 cache_<key>.{json,f32.npy} found in "
            + ", ".join(str(d) for d in dirs if d)
        )
    return found


def save_cache_dir(
    cache_dir: Path, cache: dict[str, Any], model: str, revision: str, dtype: str
) -> None:
    import numpy as np

    if not cache:
        return
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = cache_key(model, revision, dtype)
    index_p = cache_dir / f"cache_{key}.json"
    vec_p = cache_dir / f"cache_{key}.f32.npy"
    hashes = list(cache.keys())
    vecs = np.stack([cache[k] for k in hashes]).astype(np.float32)
    tmp_v = vec_p.with_name(f"cache_{key}.{os.getpid()}.f32.tmp.npy")
    np.save(tmp_v, vecs)
    tmp_i = index_p.with_name(f"cache_{key}.{os.getpid()}.json.tmp")
    tmp_i.write_text(
        json.dumps(
            {
                "meta": {
                    "model": model,
                    "revision": revision,
                    "dtype": dtype,
                    "dim": int(vecs.shape[1]),
                },
                "hashes": hashes,
            }
        ),
        encoding="utf-8",
    )
    os.replace(tmp_v, vec_p)
    os.replace(tmp_i, index_p)


def embed_missing(
    todo_seqs: dict[str, str], model_name: str, revision: str, dtype_name: str
) -> dict[str, Any]:
    import numpy as np
    import torch
    from transformers import AutoTokenizer, EsmModel

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    dtype = {
        "float32": torch.float32,
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
    }[dtype_name]
    print(
        f"loading {model_name}@{revision[:8]} ({dtype_name}) on {device} for {len(todo_seqs)} sequences",
        file=sys.stderr,
    )
    tok = AutoTokenizer.from_pretrained(model_name, revision=revision)
    model = EsmModel.from_pretrained(
        model_name, revision=revision, dtype=dtype, add_pooling_layer=False
    )
    model.eval().to(device)

    hashes = list(todo_seqs.keys())
    seqs = [todo_seqs[h] for h in hashes]
    order = sorted(range(len(seqs)), key=lambda i: -len(seqs[i]))
    plan = [(i, s, e) for i in order for (s, e) in windows(len(seqs[i]))]
    remaining = {i: len(windows(len(seqs[i]))) for i in order}
    acc_sum: dict[int, np.ndarray] = {}
    acc_cnt: dict[int, np.ndarray] = {}
    out: dict[str, np.ndarray] = {}

    max_tokens = 16384
    max_batch = 64
    pos = 0
    t0 = time.time()
    while pos < len(plan):
        batch = []
        width = 0
        while pos < len(plan) and len(batch) < max_batch:
            i, s, e = plan[pos]
            w = max(width, e - s + 2)
            if batch and w * (len(batch) + 1) > max_tokens:
                break
            width = w
            batch.append(plan[pos])
            pos += 1
        texts = [seqs[i][s:e] for i, s, e in batch]
        enc = tok(texts, padding=True, return_tensors="pt")
        counts = enc["attention_mask"].sum(dim=1).numpy()
        enc = {k: v.to(device) for k, v in enc.items()}
        with torch.inference_mode():
            hid = model(**enc).last_hidden_state
        hid = hid.float().cpu().numpy()
        for row, (i, s, e) in enumerate(batch):
            n = e - s
            if int(counts[row]) != n + 2:
                raise ValueError(
                    f"Unexpected token count {counts[row]} for window length {n}"
                )
            rep = hid[row, 1 : n + 1]
            if i not in acc_sum:
                acc_sum[i] = np.zeros((len(seqs[i]), rep.shape[1]), dtype=np.float32)
                acc_cnt[i] = np.zeros(len(seqs[i]), dtype=np.float32)
            acc_sum[i][s:e] += rep
            acc_cnt[i][s:e] += 1.0
            remaining[i] -= 1
            if remaining[i] == 0:
                per_res = acc_sum.pop(i) / acc_cnt.pop(i)[:, None]
                vec = per_res.mean(axis=0).astype(np.float32)
                out[hashes[i]] = vec
    print(f"embedded {len(out)} sequences in {time.time() - t0:.1f}s", file=sys.stderr)
    return out


def pca_2d(x):
    import numpy as np

    xc = x - x.mean(0)
    cov = (xc.T @ xc) / max(len(xc) - 1, 1)
    evals, evecs = np.linalg.eigh(cov)
    order = evals.argsort()[::-1]
    coords = xc @ evecs[:, order[:2]]
    return coords, (evals[order[:2]] / evals.sum()).tolist()


def load_trait_metadata() -> tuple[dict[str, dict], dict[str, dict]]:
    """Return (by_rel_path_or_id, local_protein_examples_by_pid)."""
    by_key: dict[str, dict] = {}
    local_proteins: dict[str, dict] = defaultdict(
        lambda: {"records": {}, "roles": set(), "labels": [], "taxa": [], "genes": []}
    )
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        try:
            rec = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(rec, dict) or not rec.get("identifier"):
            continue
        rel_traits = path.relative_to(CORPUS_DIR)
        category_dir = rel_traits.parts[0]
        slug = path.stem
        rel_repo = path.relative_to(REPO_ROOT).as_posix()
        cat = str(rec.get("trait_category") or "OTHER")
        info = {
            "id": str(rec["identifier"]),
            "slug": f"{category_dir}/{slug}",
            "href": f"traits/{category_dir}/{slug}.html",
            "label": str(rec.get("label") or rec["identifier"]),
            "category": cat,
            "class": cat,
            "term_kind": str(rec.get("term_kind") or ""),
        }
        by_key[rel_repo] = info
        by_key[str(rec["identifier"])] = info

        for g in rec.get("causal_graphs") or []:
            if not isinstance(g, dict):
                continue
            for node in g.get("nodes") or []:
                if not isinstance(node, dict):
                    continue
                node_label = str(node.get("label") or node.get("node_id") or "")
                for pex in node.get("protein_examples") or []:
                    if not isinstance(pex, dict) or not pex.get("uniprot_id"):
                        continue
                    pid = str(pex["uniprot_id"]).strip()
                    if not pid.startswith("UniProtKB:"):
                        pid = f"UniProtKB:{pid}"
                    pentry = local_proteins[pid]
                    pentry["records"][info["id"]] = info
                    if pex.get("role"):
                        pentry["roles"].add(str(pex["role"]))
                    elif node_label:
                        pentry["roles"].add(node_label)
                    if pex.get("protein_label"):
                        pentry["labels"].append(str(pex["protein_label"]))
                    if pex.get("gene_symbol"):
                        pentry["genes"].append(str(pex["gene_symbol"]))
                    if pex.get("taxon_label"):
                        pentry["taxa"].append(str(pex["taxon_label"]))
    return by_key, local_proteins


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--method", choices=["pacmap", "umap", "pca"], default="pacmap")
    ap.add_argument("--neighbors", type=int, default=15)
    ap.add_argument("--min-dist", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--cache-dir", type=Path, default=None)
    ap.add_argument("--mentions", type=Path, default=DEFAULT_MENTIONS)
    ap.add_argument("--sequences", type=Path, default=DEFAULT_SEQUENCES)
    ap.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    args = ap.parse_args()

    import numpy as np

    try:
        cache_pairs = find_esm2_caches(args.cache_dir)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    hash_to_vec: dict[str, Any] = {}
    pid_to_vec: dict[str, Any] = {}
    cache_meta: dict[str, Any] = {}
    vec_dim = 1280

    for cache_meta_path, cache_vec_path in cache_pairs:
        meta = json.loads(cache_meta_path.read_text(encoding="utf-8"))
        if not cache_meta:
            cache_meta = meta
        vecs = np.load(cache_vec_path).astype(np.float32)
        vec_dim = int(vecs.shape[1])
        for i, h in enumerate(meta.get("hashes") or []):
            if i < vecs.shape[0] and h not in hash_to_vec:
                hash_to_vec[h] = vecs[i]
        for i, pid in enumerate(meta.get("protein_ids") or []):
            if i < vecs.shape[0] and pid not in pid_to_vec:
                pid_to_vec[pid] = vecs[i]

        ids_path = cache_meta_path.parent / "ids.json"
        vecs_f16_path = cache_meta_path.parent / "vectors.f16.npy"
        if ids_path.exists() and vecs_f16_path.exists():
            f16_ids = json.loads(ids_path.read_text(encoding="utf-8"))
            f16_vecs = np.load(vecs_f16_path).astype(np.float32)
            for idx, pid in enumerate(f16_ids):
                if pid not in pid_to_vec and idx < f16_vecs.shape[0]:
                    pid_to_vec[pid] = f16_vecs[idx]

    seq_info: dict[str, dict] = {}
    if args.sequences.exists():
        with args.sequences.open(encoding="utf-8") as fh:
            for line in fh:
                row = json.loads(line)
                seq_info[row["protein_id"]] = row

    inv_info: dict[str, dict] = {}
    if args.inventory.exists():
        with args.inventory.open(encoding="utf-8") as fh:
            for line in fh:
                row = json.loads(line)
                inv_info[row["protein_id"]] = row

    for pid, srow in seq_info.items():
        shash = srow.get("sequence_sha256")
        if shash and shash in hash_to_vec:
            pid_to_vec[pid] = hash_to_vec[shash]
    for pid, irow in inv_info.items():
        if pid not in pid_to_vec:
            skey = irow.get("sequence_key")
            if skey and skey in hash_to_vec:
                pid_to_vec[pid] = hash_to_vec[skey]

    trait_by_key, local_proteins = load_trait_metadata()

    by_protein: dict[str, dict] = defaultdict(
        lambda: {"records": {}, "roles": set(), "relations": set(), "labels": [], "taxa": [], "genes": []}
    )
    for pid, linfo in local_proteins.items():
        entry = by_protein[pid]
        entry["records"].update(linfo["records"])
        entry["roles"].update(linfo["roles"])
        entry["labels"].extend(linfo["labels"])
        entry["taxa"].extend(linfo["taxa"])
        entry["genes"].extend(linfo["genes"])

    if args.mentions.exists():
        with args.mentions.open(encoding="utf-8") as fh:
            for line in fh:
                if "traitmech" not in line:
                    continue
                m = json.loads(line)
                if m.get("mech") != "traitmech":
                    continue
                pid = m["protein_id"]
                entry = by_protein[pid]
                rec_info = trait_by_key.get(m.get("record_path") or "") or trait_by_key.get(
                    m.get("record_id") or ""
                )
                if rec_info:
                    entry["records"][rec_info["id"]] = rec_info
                if m.get("role"):
                    entry["roles"].add(str(m["role"]))
                if m.get("relation"):
                    entry["relations"].add(str(m["relation"]))
                if m.get("sibling_label"):
                    entry["labels"].append(str(m["sibling_label"]))
                if m.get("taxon_label"):
                    entry["taxa"].append(str(m["taxon_label"]))

    todo_seqs: dict[str, str] = {}
    for pid, info in by_protein.items():
        if not info["records"] or pid in pid_to_vec:
            continue
        srow = seq_info.get(pid)
        if not srow:
            continue
        seq = str(srow.get("sequence") or "").strip().upper()
        shash = srow.get("sequence_sha256")
        if seq and shash and VALID_SEQUENCE.match(seq):
            todo_seqs[shash] = seq

    if todo_seqs:
        new_vecs = embed_missing(todo_seqs, MODEL, REVISION, "float16")
        hash_to_vec.update(new_vecs)
        for pid, srow in seq_info.items():
            shash = srow.get("sequence_sha256")
            if shash and shash in new_vecs:
                pid_to_vec[pid] = new_vecs[shash]
        shared_existing: dict[str, Any] = {}
        key = cache_key(MODEL, REVISION, "float16")
        sp_meta = SHARED_CACHE_DIR / f"cache_{key}.json"
        sp_vec = SHARED_CACHE_DIR / f"cache_{key}.f32.npy"
        if sp_meta.exists() and sp_vec.exists():
            m = json.loads(sp_meta.read_text(encoding="utf-8"))
            v = np.load(sp_vec).astype(np.float32)
            for idx, h in enumerate(m.get("hashes") or []):
                if idx < v.shape[0]:
                    shared_existing[h] = v[idx]
        shared_existing.update(new_vecs)
        save_cache_dir(SHARED_CACHE_DIR, shared_existing, MODEL, REVISION, "float16")

    protein_ids = sorted(
        pid for pid, info in by_protein.items() if pid in pid_to_vec and info["records"]
    )
    if not protein_ids:
        print("No TraitMech proteins matched ESM-2 cache.", file=sys.stderr)
        return 2

    sub_vecs = np.stack([pid_to_vec[pid] for pid in protein_ids], axis=0)
    sub_vecs = sub_vecs - sub_vecs.mean(axis=0, keepdims=True)
    norms = np.linalg.norm(sub_vecs, axis=1, keepdims=True)
    sub_vecs = sub_vecs / np.where(norms == 0, 1.0, norms)

    explained = None
    if args.method == "pca":
        coords, explained = pca_2d(sub_vecs)
    elif args.method == "umap":
        import umap

        coords = umap.UMAP(
            n_neighbors=args.neighbors,
            min_dist=args.min_dist,
            metric="cosine",
            random_state=args.seed,
        ).fit_transform(sub_vecs)
    else:
        import pacmap

        coords = pacmap.PaCMAP(
            n_neighbors=min(args.neighbors, max(2, len(protein_ids) - 1)),
            random_state=args.seed,
        ).fit_transform(sub_vecs)
    coords = np.asarray(coords, dtype=np.float32)

    lo, hi = coords.min(0), coords.max(0)
    span = np.where(hi - lo == 0, 1.0, hi - lo)
    unit = (coords - lo) / span

    primary_class_by_pid: dict[str, str] = {}
    for pid in protein_ids:
        recs = list(by_protein[pid]["records"].values())
        counts = Counter(r["class"] for r in recs)
        primary_class_by_pid[pid] = sorted(
            counts.items(), key=lambda kv: (-kv[1], kv[0])
        )[0][0]

    classes = sorted(set(primary_class_by_pid.values()))
    class_idx = {c: i for i, c in enumerate(classes)}

    points = []
    for n, pid in enumerate(protein_ids):
        info = by_protein[pid]
        s = seq_info.get(pid) or {}
        inv = inv_info.get(pid) or {}
        res = inv.get("current_uniprot_resolution") or {}
        recs = sorted(info["records"].values(), key=lambda r: r["label"].lower())
        p_cls = primary_class_by_pid[pid]

        label = (
            (info["labels"][0] if info["labels"] else None)
            or inv.get("protein_label")
            or res.get("protein_name")
            or pid
        )
        gene_symbol = (
            (info["genes"][0] if info["genes"] else None)
            or inv.get("gene_symbol")
            or ""
        )
        organism = (
            (info["taxa"][0] if info["taxa"] else None)
            or inv.get("taxon_label")
            or res.get("organism_name")
            or "Unspecified"
        )
        accession = pid.split(":", 1)[-1]
        seq_len = int(s.get("sequence_length") or s.get("length") or 0)
        points.append(
            {
                "x": round(float(unit[n][0]), 4),
                "y": round(float(unit[n][1]), 4),
                "classIdx": class_idx[p_cls],
                "class": p_cls,
                "primary_category": p_cls,
                "protein_id": pid,
                "uniprot_id": pid,
                "accession": accession,
                "uniprot_url": f"https://www.uniprot.org/uniprotkb/{accession}/entry",
                "label": str(label),
                "protein_label": str(label),
                "gene_symbol": str(gene_symbol),
                "organism": str(organism),
                "taxon_label": str(organism),
                "length": seq_len,
                "seq_len": seq_len,
                "roles": sorted(info["roles"])[:6],
                "relations": sorted(info["relations"]),
                "n_traits": len(recs),
                "primary_href": recs[0]["href"],
                "primary_trait": recs[0]["label"],
                "records": [
                    {
                        "id": r["id"],
                        "label": r["label"],
                        "category": r["category"],
                        "class": r["class"],
                        "href": r["href"],
                    }
                    for r in recs[:12]
                ],
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    meta_info = cache_meta.get("meta") if isinstance(cache_meta.get("meta"), dict) else cache_meta
    payload = {
        "method": args.method,
        "model": meta_info.get("model", "facebook/esm2_t33_650M_UR50D"),
        "dim": int(meta_info.get("dim", vec_dim)),
        "pooling": meta_info.get("pooling", "mean"),
        "max_length": int(meta_info.get("max_length", 1022)),
        "n": len(points),
        "n_traits_covered": len(
            {r["id"] for pid in protein_ids for r in by_protein[pid]["records"].values()}
        ),
        "classes": classes,
        "generated_from": "scripts/build_sequence_map.py",
        "points": points,
    }
    if explained:
        payload["explained"] = [round(e, 4) for e in explained]
    OUT.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
    print(
        f"{len(points):,} proteins across {payload['n_traits_covered']:,} traits "
        f"({args.method}) -> {OUT.relative_to(REPO_ROOT)} ({OUT.stat().st_size / 1024:.1f} KB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
