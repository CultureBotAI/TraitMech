#!/usr/bin/env python3
"""Vendor a slim trait subset of kg-microbe's deepwalk embeddings + build a
METPO CURIE ↔ kg-microbe-node match table.

Source priority
---------------
1. ``../CommunityMech/CommunityMech/data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v2_2026-04-25_*.tsv.gz``
   (5.7 GB, 512-D, latest; carries 380 METPO CURIEs DIRECTLY plus the legacy
   pre-METPO trait nodes for backward compatibility).
2. Fallback to the 2024-09-25 200-D file if the 2026-04-25 one isn't present.

The 2026-04-25 file is the first kg-microbe-derived embedding that ingests
METPO. Direct CURIE lookup (METPO:1000602 → that row's 512 floats) is the
primary match path; the alias-table + label-match fallback covers METPO
classes whose CURIEs the embedding doesn't have but whose label does.

Bridge
------
``../kg-microbe/mappings/canonical/metpo_alias_mappings.tsv`` (~66 rows)
maps text labels → METPO CURIEs ("rod-shaped" → METPO:1000681). Used as a
secondary match path for labels that match a kg-microbe legacy node (e.g.
the 2024-09-25 file's `cell_shape:bacillus`).

Outputs
-------
1. ``data/embeddings/deepwalk_traits.tsv.gz``
   Slim copy of the source: METPO:* rows + trait-relevant legacy prefixes.
   1MB-class, gzipped.
2. ``data/embeddings/metpo_to_kgm_node.tsv``
   Per-METPO match table with method tag (``direct_metpo`` /
   ``alias_table`` / ``label_match`` / ``no_match``) and node id list.

Usage
-----
    just build-embeddings       # uses defaults
    python3 scripts/build_embedding_index.py --src <path>
"""
from __future__ import annotations

import argparse
import csv
import gzip
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Newest available kg-microbe-derived deepwalk: 512-D, 2026-06-26 (v3),
# includes METPO CURIEs directly. Source-of-truth for direct-METPO matching.
DEFAULT_KGM_DEEPWALK = (
    REPO_ROOT.parent / "CommunityMech" / "CommunityMech" / "data" / "embeddings"
    / "DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz"
)
# Fallback: 2024-09-25 200-D file (pre-METPO; only useful for legacy-prefix
# trait nodes like `cell_shape:bacillus`).
FALLBACK_KGM_DEEPWALK = (
    REPO_ROOT.parent / "kg-microbe-projects" / "taxa_media"
    / "DeepWalkSkipGramEnsmallen_degreenorm_embedding_200_1_wouniprot__2024-09-25_03_07_47.tsv.gz"
)
DEFAULT_KGM_ALIASES = (
    REPO_ROOT.parent / "kg-microbe" / "mappings" / "canonical" / "metpo_alias_mappings.tsv"
)

# Trait-relevant CURIE prefixes worth carrying into the slim subset. METPO is
# the new authoritative anchor; the legacy `cell_shape:*` etc. prefixes are
# kept for older embeddings but not present in the 2026-04-25 file.
_TRAIT_PREFIXES: tuple[str, ...] = (
    "METPO:",  # primary anchor in 2026-04-25 file
    "cell_shape:", "cell_length:", "cell_width:",
    "gram_stain:", "motility:",
    "gc:", "NaCl_opt:", "NaCl_range:", "NaCl_delta:",
    "pH_opt:", "pH_range:", "pH_delta:",
    "temp_opt:", "temp_range:", "temp_delta:", "temperature:",
    "oxygen:", "trophic_type:", "salinity:",
    "pathogen:", "pigment:", "production:",
    "carbon_substrates:", "isolation_source:",
    "assay:",
    "BSL:",
    "PATO:",
)

OUT_DIR = REPO_ROOT / "data" / "embeddings"
OUT_DEEPWALK = OUT_DIR / "deepwalk_traits.tsv.gz"
OUT_MATCH = OUT_DIR / "metpo_to_kgm_node.tsv"
OUT_UMAP_JSON = OUT_DIR / "trait_umap.json"
OUT_NN_JSON = OUT_DIR / "trait_nearest_neighbors.json"
TRAITS_DIR = REPO_ROOT / "data" / "traits"

UMAP_NEAREST_K = 8


def _normalise(s: str) -> str:
    """Lowercase + collapse-whitespace + drop punctuation."""
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def vendor_slim_deepwalk(src: Path, dst: Path) -> tuple[int, set[str]]:
    """Copy only trait-relevant rows from ``src`` to ``dst`` (gzipped TSV).
    Returns (n_rows, set of kg-microbe node ids carried)."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    n_rows = 0
    nodes: set[str] = set()
    with gzip.open(src, "rt", encoding="utf-8") as fin, \
         gzip.open(dst, "wt", encoding="utf-8") as fout:
        # Pass-through header.
        header = fin.readline()
        fout.write(header)
        for line in fin:
            tab = line.find("\t")
            sid = line[:tab] if tab > 0 else line.strip()
            if sid.startswith(_TRAIT_PREFIXES):
                fout.write(line)
                n_rows += 1
                nodes.add(sid)
    return n_rows, nodes


def load_alias_table(path: Path) -> dict[str, str]:
    """Return {normalised_label → METPO CURIE} from metpo_alias_mappings.tsv."""
    out: dict[str, str] = {}
    if not path.exists():
        print(f"  alias table missing: {path}", file=sys.stderr)
        return out
    with path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            label = row.get("subject_label_normalized") or row.get("subject_label", "")
            curie = (row.get("object_id") or "").strip()
            if label and curie.startswith("METPO:"):
                out[_normalise(label)] = curie
    return out


def load_metpo_records(traits_dir: Path) -> list[tuple[str, str, list[str], str, list[str]]]:
    """Return list of (curie, label, synonyms, category_dir, parents) tuples for
    every seeded TraitRecord. ``parents`` is the record's ``parent_traits`` CURIE
    list (used by the parent-proxy match tier). Skips files that fail to parse."""
    import yaml  # lazy import; only this script needs it
    out: list[tuple[str, str, list[str], str, list[str]]] = []
    for path in sorted(traits_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        curie = (doc.get("identifier") or "").strip()
        label = (doc.get("label") or "").strip()
        if not curie:
            continue
        synonyms = []
        for s in (doc.get("synonyms") or []):
            txt = (s.get("synonym_text") or "").strip()
            if txt:
                synonyms.append(txt)
        parents = [p.strip() for p in (doc.get("parent_traits") or []) if isinstance(p, str) and p.strip()]
        category_dir = path.parent.name
        out.append((curie, label, synonyms, category_dir, parents))
    return out


def build_match_table(
    metpo_records: list[tuple[str, str, list[str], str, list[str]]],
    deepwalk_nodes: set[str],
    alias_table: dict[str, str],
) -> list[dict[str, str]]:
    """Match each record to ≥0 kg-microbe trait nodes via, in order:
      1. direct_metpo — the record's own CURIE is in the deepwalk.
      2. alias_table  — reverse alias lookup (METPO → known label → node).
      3. label_match  — normalised label / synonym matches a node value-form.
      4. parent_proxy — for records whose own CURIE is absent (synthetic
         ``traitmech:`` traits, or METPO classes minted after the deepwalk
         run), walk ``parent_traits`` transitively to the nearest ancestor
         whose CURIE *is* in the deepwalk and borrow its embedding. The trait
         is positioned with its semantic parent rather than dropped entirely.
    """
    # Parent map for the proxy tier: curie -> list of parent curies (may chain
    # traitmech: -> traitmech: -> METPO:).
    parent_map: dict[str, list[str]] = {
        curie: parents for curie, _, _, _, parents in metpo_records
    }

    def resolve_parent_proxy(curie: str) -> str | None:
        """BFS up the parent chain to the first ancestor CURIE in the deepwalk."""
        seen: set[str] = {curie}
        queue: list[str] = list(parent_map.get(curie, []))
        while queue:
            p = queue.pop(0)
            if p in seen:
                continue
            seen.add(p)
            if p in deepwalk_nodes:
                return p
            queue.extend(parent_map.get(p, []))
        return None
    # Build reverse alias index: METPO CURIE -> set of acceptable normalised labels
    metpo_to_norm_labels: dict[str, set[str]] = {}
    for norm, curie in alias_table.items():
        metpo_to_norm_labels.setdefault(curie, set()).add(norm)

    # Pre-normalise deepwalk node values for fuzzy lookup. Index BOTH the
    # value-only form (`gc:high` → "high") AND the full-id form
    # (`gc:high` → "gc_high"). The full-id form matches METPO labels that
    # carry the prefix in their label (e.g. METPO:1000432 "GC high" →
    # `gc_high`); the value-only form catches METPO labels that drop the
    # prefix (e.g. METPO:1000602 "aerobic" → kg-microbe `oxygen:aerobe`).
    nodes_by_normvalue: dict[str, set[str]] = {}
    for node in deepwalk_nodes:
        if ":" in node:
            value = node.split(":", 1)[1]
            nodes_by_normvalue.setdefault(_normalise(value), set()).add(node)
        nodes_by_normvalue.setdefault(_normalise(node), set()).add(node)

    rows: list[dict[str, str]] = []
    for curie, label, synonyms, category, _parents in metpo_records:
        candidates: set[str] = set()
        method = ""

        # 1. PRIMARY: direct METPO CURIE lookup. The 2026-04-25 deepwalk has
        #    380 METPO CURIEs; if our subject is one of them, that's the
        #    authoritative match — nothing fuzzy needed.
        if curie in deepwalk_nodes:
            candidates.add(curie)
            method = "direct_metpo"

        # 2. Alias-table reverse lookup: METPO → known normalised labels → nodes.
        if not candidates:
            for norm in metpo_to_norm_labels.get(curie, set()):
                if norm in nodes_by_normvalue:
                    candidates.update(nodes_by_normvalue[norm])
                    method = "alias_table"

        # 3. Direct normalised-label match (METPO label or synonyms).
        if not candidates:
            for txt in [label] + synonyms:
                norm = _normalise(txt)
                if norm and norm in nodes_by_normvalue:
                    candidates.update(nodes_by_normvalue[norm])
                    if not method:
                        method = "label_match"

        # 4. Parent proxy: borrow the nearest embedded ancestor's vector.
        if not candidates:
            proxy = resolve_parent_proxy(curie)
            if proxy:
                candidates.add(proxy)
                method = "parent_proxy"

        rows.append({
            "metpo_curie": curie,
            "label": label,
            "category": category,
            "match_method": method or "no_match",
            "kgm_nodes": ";".join(sorted(candidates)),
            "n_kgm_nodes": str(len(candidates)),
        })
    return rows


def write_match_table(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cols = ["metpo_curie", "label", "category", "match_method", "n_kgm_nodes", "kgm_nodes"]
    with path.open("w") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def load_embedding_vectors(slim_deepwalk: Path) -> dict[str, list[float]]:
    """Load the slim deepwalk into {node_id: [float, ...]}."""
    out: dict[str, list[float]] = {}
    with gzip.open(slim_deepwalk, "rt", encoding="utf-8") as f:
        # Skip header
        f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            sid = parts[0]
            try:
                vec = [float(x) for x in parts[1:]]
            except ValueError:
                continue
            out[sid] = vec
    return out


def compute_umap_and_neighbors(
    metpo_records: list[tuple[str, str, list[str], str]],
    match_rows: list[dict[str, str]],
    vectors: dict[str, list[float]],
    method: str = "pacmap",
) -> tuple[list[dict], dict[str, list[dict]]]:
    """Project the matched-record embeddings to 2-D and compute k nearest
    neighbors per record. Returns (umap_points, nn_per_curie).

    ``method`` selects the 2-D reducer: ``"pacmap"`` (default; PCA-init,
    fixed seed, L2-normalised rows to mirror cosine geometry) or ``"umap"``
    (legacy UMAP path). The output JSON keys (umap_x / umap_y) are unchanged
    regardless of reducer.

    Records without an embedding are NOT in the UMAP output (they have no
    coordinates) but still appear in nn_per_curie as []."""
    try:
        import numpy as np
    except ImportError as e:
        print(f"  numpy not available: {e}; skipping projection", file=sys.stderr)
        return [], {}
    if method == "umap":
        try:
            import umap as _umap
        except ImportError as e:
            print(f"  UMAP not available: {e}; skipping projection", file=sys.stderr)
            return [], {}
    elif method == "pacmap":
        try:
            import pacmap  # noqa: F401
            from sklearn.preprocessing import normalize  # noqa: F401
        except ImportError as e:
            print(f"  PaCMAP / scikit-learn not available: {e}; skipping projection",
                  file=sys.stderr)
            return [], {}
    else:
        print(f"  Unknown reducer method {method!r}; skipping projection", file=sys.stderr)
        return [], {}

    # Index match table by curie
    match_by_curie = {r["metpo_curie"]: r for r in match_rows}
    record_by_curie = {c: (lbl, syn, cat) for c, lbl, syn, cat, _par in metpo_records}

    # Build matrix: take ANY matched node's vector for each METPO record;
    # when multiple nodes match, average them.
    curies: list[str] = []
    matrix: list[list[float]] = []
    for r in match_rows:
        nodes = [n.strip() for n in r["kgm_nodes"].split(";") if n.strip()]
        vecs = [vectors[n] for n in nodes if n in vectors]
        if not vecs:
            continue
        n = len(vecs[0])
        avg = [sum(v[i] for v in vecs) / len(vecs) for i in range(n)]
        curies.append(r["metpo_curie"])
        matrix.append(avg)

    if len(matrix) < 5:
        print(f"  Only {len(matrix)} matched embeddings — projection skipped", file=sys.stderr)
        return [], {}

    arr = np.array(matrix, dtype=float)
    if method == "umap":
        print(f"      Running UMAP on {arr.shape[0]} × {arr.shape[1]} matrix")
        reducer = _umap.UMAP(
            n_components=2, n_neighbors=min(15, len(matrix) - 1), random_state=42
        )
        coords = reducer.fit_transform(arr)
    else:  # pacmap (default)
        from sklearn.preprocessing import normalize
        print(f"      Running PaCMAP on {arr.shape[0]} × {arr.shape[1]} matrix")
        X = normalize(arr.astype("float32"))
        coords = pacmap.PaCMAP(n_components=2, random_state=42).fit_transform(X, init="pca")

    # Cosine-style nearest neighbors via L2 normalisation + dot product.
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normed = arr / norms
    sim = normed @ normed.T
    np.fill_diagonal(sim, -1.0)
    k = min(UMAP_NEAREST_K, len(matrix) - 1)
    top_idx = np.argsort(-sim, axis=1)[:, :k]

    umap_points: list[dict] = []
    nn_map: dict[str, list[dict]] = {}
    for i, curie in enumerate(curies):
        lbl, _, cat = record_by_curie.get(curie, ("", [], "OTHER"))
        umap_points.append({
            "id": curie,
            "label": lbl,
            "category": cat,
            "match_method": match_by_curie[curie]["match_method"],
            "umap_x": float(coords[i, 0]),
            "umap_y": float(coords[i, 1]),
        })
        nn_map[curie] = [
            {
                "id": curies[j],
                "label": record_by_curie[curies[j]][0],
                "category": record_by_curie[curies[j]][2],
                "similarity": float(sim[i, j]),
            }
            for j in top_idx[i]
        ]

    # Records without embeddings still get an entry (empty list) so the renderer
    # can distinguish "no embedding" from "no neighbors found".
    for curie, _, _, _, _ in metpo_records:
        nn_map.setdefault(curie, [])
    return umap_points, nn_map


def write_json(path: Path, payload) -> None:
    import json
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=DEFAULT_KGM_DEEPWALK,
                    help="path to the source deepwalk .tsv.gz")
    ap.add_argument("--kgm-aliases", type=Path, default=DEFAULT_KGM_ALIASES)
    ap.add_argument("--out-deepwalk", type=Path, default=OUT_DEEPWALK)
    ap.add_argument("--out-match", type=Path, default=OUT_MATCH)
    ap.add_argument("--method", choices=["pacmap", "umap"], default="pacmap",
                    help="2-D reducer for the trait projection (default: pacmap)")
    args = ap.parse_args()

    src = args.src
    if not src.exists():
        if FALLBACK_KGM_DEEPWALK.exists():
            print(f"  Primary embedding missing ({src}); using fallback {FALLBACK_KGM_DEEPWALK.name}")
            src = FALLBACK_KGM_DEEPWALK
        else:
            print(f"deepwalk source missing: {src}", file=sys.stderr)
            return 2

    print(f"[1/4] Vendoring slim deepwalk subset → {args.out_deepwalk}")
    print(f"      source: {src.name}")
    n_rows, nodes = vendor_slim_deepwalk(src, args.out_deepwalk)
    metpo_count = sum(1 for n in nodes if n.startswith("METPO:"))
    print(f"      {n_rows} trait-relevant rows carried; {len(nodes)} unique node ids "
          f"(METPO:* = {metpo_count})")

    print(f"[2/4] Loading metpo alias table → {args.kgm_aliases}")
    aliases = load_alias_table(args.kgm_aliases)
    print(f"      {len(aliases)} alias rows loaded")

    print(f"[3/4] Building METPO ↔ kg-microbe match table → {args.out_match}")
    metpo_records = load_metpo_records(TRAITS_DIR)
    rows = build_match_table(metpo_records, nodes, aliases)
    write_match_table(rows, args.out_match)

    matched = sum(1 for r in rows if int(r["n_kgm_nodes"]) > 0)
    print(f"      {len(rows)} TraitRecords; {matched} matched ≥1 kg-microbe node "
          f"({matched / max(len(rows), 1) * 100:.1f}% coverage)")
    by_method: dict[str, int] = {}
    for r in rows:
        by_method[r["match_method"]] = by_method.get(r["match_method"], 0) + 1
    for m, n in sorted(by_method.items(), key=lambda x: -x[1]):
        print(f"        {m:<15} {n}")

    print(f"[4/4] 2-D projection ({args.method}) + nearest neighbors")
    vectors = load_embedding_vectors(args.out_deepwalk)
    umap_points, nn_map = compute_umap_and_neighbors(
        metpo_records, rows, vectors, method=args.method
    )
    write_json(OUT_UMAP_JSON, umap_points)
    write_json(OUT_NN_JSON, nn_map)
    print(f"      {len(umap_points)} UMAP points → {OUT_UMAP_JSON.name}")
    nn_with_data = sum(1 for v in nn_map.values() if v)
    print(f"      {nn_with_data} traits with ≥1 nearest neighbor → {OUT_NN_JSON.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
