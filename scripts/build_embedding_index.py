#!/usr/bin/env python3
"""Vendor a slim trait subset of kg-microbe's deepwalk embeddings + build a
METPO CURIE ↔ kg-microbe-node match table.

Source selection
----------------
Explicit ``--src`` or ``KG_MICROBE_EMBEDDINGS`` takes precedence, then a local
v3 2026-06-26 artifact, then the configured/sibling CommunityMech artifact.
A missing selected source fails; legacy releases require an explicit path.
No source/reducer provenance is inferred for old point arrays.

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
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

from traitmech.graph_embedding_receipts import (
    GraphSource,
    corpus_receipt,
    make_receipt,
    matrix_receipt,
    projection_receipt,
    publish_artifacts,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

# Newest available kg-microbe-derived deepwalk: 512-D, 2026-06-26 (v3),
# includes METPO CURIEs directly. Source-of-truth for direct-METPO matching.
EMBEDDINGS_FILENAME = (
    "DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz"
)


def default_deepwalk() -> Path:
    override = os.environ.get("KG_MICROBE_EMBEDDINGS")
    if override:
        return Path(override).expanduser()
    local = REPO_ROOT / "data" / "embeddings" / EMBEDDINGS_FILENAME
    if local.is_file():
        return local
    community = Path(os.environ.get("COMMUNITYMECH_ROOT") or REPO_ROOT.parent / "CommunityMech")
    return community / "data" / "embeddings" / EMBEDDINGS_FILENAME


DEFAULT_KGM_DEEPWALK = default_deepwalk()
DEFAULT_KGM_ALIASES = (
    REPO_ROOT.parent / "kg-microbe" / "mappings" / "canonical" / "metpo_alias_mappings.tsv"
)

# Trait-relevant CURIE prefixes worth carrying into the slim subset. METPO is
# the new authoritative anchor; the legacy `cell_shape:*` etc. prefixes are
# kept for older embeddings but not present in the 2026-04-25 file.
_TRAIT_PREFIXES: tuple[str, ...] = (
    "METPO:",  # primary anchor in 2026-04-25 file
    "cell_shape:",
    "cell_length:",
    "cell_width:",
    "gram_stain:",
    "motility:",
    "gc:",
    "NaCl_opt:",
    "NaCl_range:",
    "NaCl_delta:",
    "pH_opt:",
    "pH_range:",
    "pH_delta:",
    "temp_opt:",
    "temp_range:",
    "temp_delta:",
    "temperature:",
    "oxygen:",
    "trophic_type:",
    "salinity:",
    "pathogen:",
    "pigment:",
    "production:",
    "carbon_substrates:",
    "isolation_source:",
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


def vendor_slim_deepwalk(src: Path, dst: Path, *, node_filter=None, return_receipt=False):
    """Parse source bytes and retain only requested trait/proxy candidates."""
    source = GraphSource(
        src,
        _TRAIT_PREFIXES,
        node_filter=node_filter,
        filter_name="trait-record-parent-alias-label-candidates-v1" if node_filter else None,
    )
    dst.parent.mkdir(parents=True, exist_ok=True)
    nodes = set()
    with dst.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as output:
        for node, vector in source:
            if not nodes:
                output.write(
                    ("node_id\t" + "\t".join(f"d{i}" for i in range(len(vector))) + "\n").encode()
                )
            output.write((node + "\t" + "\t".join(repr(value) for value in vector) + "\n").encode())
            nodes.add(node)
    result = (len(nodes), nodes)
    return (*result, source.receipt) if return_receipt else result


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
    list (used by the parent-proxy match tier). Invalid records fail generation."""
    import yaml  # lazy import; only this script needs it

    out: list[tuple[str, str, list[str], str, list[str]]] = []
    seen = set()
    for path in sorted(traits_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except (OSError, yaml.YAMLError) as error:
            raise ValueError(f"Unable to read trait record: {path}") from error
        if not isinstance(doc, dict):
            raise TypeError(f"Trait record is not a mapping: {path}")
        curie = (doc.get("identifier") or "").strip()
        label = (doc.get("label") or "").strip()
        if not curie:
            raise ValueError(f"Trait record has no identifier: {path}")
        if curie in seen:
            raise ValueError(f"Duplicate trait identifier: {curie}")
        seen.add(curie)
        synonyms = []
        for s in doc.get("synonyms") or []:
            txt = (s.get("synonym_text") or "").strip()
            if txt:
                synonyms.append(txt)
        parents = [
            p.strip() for p in (doc.get("parent_traits") or []) if isinstance(p, str) and p.strip()
        ]
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
    parent_map: dict[str, list[str]] = {curie: parents for curie, _, _, _, parents in metpo_records}

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

        rows.append(
            {
                "metpo_curie": curie,
                "label": label,
                "category": category,
                "match_method": method or "no_match",
                "kgm_nodes": ";".join(sorted(candidates)),
                "n_kgm_nodes": str(len(candidates)),
            }
        )
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
    metpo_records, match_rows, vectors, method="pacmap", *, receipt_details=None
):
    """Keep the matched/proxy graph construction; receipt the actual reducer inputs."""
    import numpy as np
    from sklearn import config_context
    from sklearn.neighbors import NearestNeighbors
    from sklearn.preprocessing import normalize

    match_by_curie = {row["metpo_curie"]: row for row in match_rows}
    record_by_curie = {
        curie: (label, synonyms, category) for curie, label, synonyms, category, _ in metpo_records
    }
    curies, matrix, ledger = [], [], []
    for row in match_rows:
        curie = row["metpo_curie"]
        if curie not in record_by_curie:
            raise ValueError(f"Matched trait is outside the corpus: {curie}")
        nodes = [node.strip() for node in row["kgm_nodes"].split(";") if node.strip()]
        found = [node for node in nodes if node in vectors]
        ledger.append(
            {
                "identifier": curie,
                "source_nodes": found,
                "missing_nodes": [node for node in nodes if node not in vectors],
                "status": "projected" if found else "no_vectors",
                "match_method": row["match_method"],
                "aggregation_method": "mean",
                "weight_per_source": 1 / len(found) if found else 0,
            }
        )
        if found:
            matrix.append(np.mean([vectors[node] for node in found], axis=0))
            curies.append(curie)
    if len(matrix) < 5:
        raise ValueError(
            f"Only {len(matrix)} matched embeddings; trait projection requires at least five"
        )
    arr = np.asarray(matrix, dtype=np.float64)
    if method == "pacmap":
        import pacmap

        parameters = {
            "n_components": 2,
            "random_state": 42,
            "n_neighbors": None,
            "MN_ratio": 0.5,
            "FP_ratio": 2.0,
            "distance": "euclidean",
            "lr": 1.0,
            "num_iters": (100, 100, 250),
            "apply_pca": True,
            "knn_backend": "faiss",
        }
        actual = normalize(arr.astype("float32"))
        vectors_receipt = matrix_receipt(actual, curies)
        reducer = pacmap.PaCMAP(**parameters)
        coords = reducer.fit_transform(actual, init="pca")
        projection = projection_receipt(
            method, parameters, reducer=reducer, normalization="l2", initialization="pca"
        )
    elif method == "umap":
        import umap

        parameters = {
            "n_components": 2,
            "n_neighbors": min(15, len(matrix) - 1),
            "random_state": 42,
            "metric": "euclidean",
        }
        vectors_receipt = matrix_receipt(arr, curies, dtype="float64-le")
        reducer = umap.UMAP(**parameters)
        coords = reducer.fit_transform(arr)
        projection = projection_receipt(method, parameters, reducer=reducer, normalization="none")
    elif method == "sfdp":
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from sfdp_layout import sfdp_layout

        coords, graph = sfdp_layout(arr, k=15, seed=42, return_receipt=True, record_ids=curies)
        vectors_receipt = graph.pop("matrix")
        projection = projection_receipt(
            method, {"k": 15, "seed": 42}, normalization="l2", graph=graph
        )
    else:
        raise ValueError(f"Unknown trait projection: {method}")
    if np.asarray(coords).shape != (len(curies), 2) or not np.isfinite(coords).all():
        raise ValueError(
            "Trait projection did not return finite coordinates for every selected record"
        )
    # Chunked exact cosine neighbors avoid an all-pairs matrix, including for
    # future corpus growth. Self is excluded explicitly even among proxy ties.
    normed = normalize(arr)
    nearest_matrix = matrix_receipt(normed, curies, dtype="float64-le")
    k = min(UMAP_NEAREST_K, len(curies) - 1)
    with config_context(working_memory=64):
        distances, indices = (
            NearestNeighbors(n_neighbors=k + 1, metric="cosine", algorithm="brute")
            .fit(normed)
            .kneighbors(normed)
        )
    ledger_by_curie = {row["identifier"]: row for row in ledger}
    points, neighbors = [], {}
    for i, curie in enumerate(curies):
        label, _, category = record_by_curie[curie]
        points.append(
            {
                "id": curie,
                "label": label,
                "category": category,
                "match_method": match_by_curie[curie]["match_method"],
                "kgm_nodes": ledger_by_curie[curie]["source_nodes"],
                "umap_x": float(coords[i, 0]),
                "umap_y": float(coords[i, 1]),
            }
        )
        neighbors[curie] = []
        for distance, j in zip(distances[i], indices[i], strict=True):
            if j == i:
                continue
            other = curies[j]
            neighbors[curie].append(
                {
                    "id": other,
                    "label": record_by_curie[other][0],
                    "category": record_by_curie[other][2],
                    "similarity": float(1 - distance),
                    "match_method": match_by_curie[other]["match_method"],
                    "kgm_nodes": [
                        node
                        for node in match_by_curie[other]["kgm_nodes"].split(";")
                        if node in vectors
                    ],
                }
            )
            if len(neighbors[curie]) == k:
                break
    for curie in record_by_curie:
        neighbors.setdefault(curie, [])
    if receipt_details is not None:
        receipt_details.update(
            matrix=vectors_receipt,
            projection=projection,
            ledger=ledger,
            nearest_neighbors={
                "metric": "cosine",
                "k": k,
                "implementation": "sklearn.neighbors.NearestNeighbors",
                "working_memory_mib": 64,
                "matrix": nearest_matrix,
            },
        )
    return points, neighbors


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))


def file_sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def write_projection_metadata(
    path: Path,
    source=None,
    vectors=None,
    method=None,
    match_table=None,
    neighbors=None,
    *,
    generation_receipt=None,
    staged=None,
):
    """Output-only source labels cannot establish provenance; stage a real generation."""
    if generation_receipt is None or staged is None:
        raise ValueError(
            "Output-only provenance is unsupported; regenerate from the actual graph source"
        )
    return publish_artifacts(staged, path.with_suffix(".metadata.json"), generation_receipt)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--src", type=Path, default=DEFAULT_KGM_DEEPWALK, help="path to the source deepwalk .tsv.gz"
    )
    ap.add_argument("--kgm-aliases", type=Path, default=DEFAULT_KGM_ALIASES)
    ap.add_argument("--out-deepwalk", type=Path, default=OUT_DEEPWALK)
    ap.add_argument("--out-match", type=Path, default=OUT_MATCH)
    ap.add_argument(
        "--umap-out",
        type=Path,
        default=OUT_UMAP_JSON,
        help="output path for the 2-D projection JSON "
        "(default: data/embeddings/trait_umap.json). Use a "
        "separate path (e.g. trait_graph.json) for --method sfdp "
        "so the pacmap default output is not overwritten.",
    )
    ap.add_argument(
        "--method",
        choices=["pacmap", "umap", "sfdp"],
        default="pacmap",
        help="2-D reducer for the trait projection (default: pacmap)",
    )
    ap.add_argument(
        "--out-neighbors",
        type=Path,
        default=OUT_NN_JSON,
        help="Neighbor JSON destination; all graph outputs must share one directory",
    )
    args = ap.parse_args()

    src = args.src
    if not src.is_file():
        print(
            f"Selected deepwalk source missing: {src}; pass --src for another release",
            file=sys.stderr,
        )
        return 2

    destinations = [args.out_deepwalk, args.out_match, args.umap_out, args.out_neighbors]
    if len({path.parent.resolve() for path in destinations}) != 1:
        ap.error("graph outputs must share one directory for complete receipt validation")
    if len({path.name for path in destinations}) != len(destinations):
        ap.error("graph output filenames must be distinct")

    corpus_paths = sorted(TRAITS_DIR.rglob("*.yaml"))
    corpus = corpus_receipt(corpus_paths, TRAITS_DIR)
    records = load_metpo_records(TRAITS_DIR)
    alias_receipt = {
        "filename": args.kgm_aliases.name,
        "sha256": file_sha256(args.kgm_aliases) if args.kgm_aliases.is_file() else None,
    }
    aliases = load_alias_table(args.kgm_aliases)
    curies = {row[0] for row in records}
    direct_candidates = curies | {parent for row in records for parent in row[4]}
    labels = {
        _normalise(label) for _, label, synonyms, _, _ in records for label in [label, *synonyms]
    }
    labels.update(norm for norm, curie in aliases.items() if curie in curies)
    labels.discard("")

    def candidate(node):
        return (
            node in direct_candidates
            or _normalise(node) in labels
            or _normalise(node.split(":", 1)[-1]) in labels
        )

    args.umap_out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".trait-graph-", dir=args.umap_out.parent) as temporary:
        stage = Path(temporary)
        slim, match_path = stage / args.out_deepwalk.name, stage / args.out_match.name
        _, nodes, source_receipt = vendor_slim_deepwalk(
            src, slim, node_filter=candidate, return_receipt=True
        )
        matches = build_match_table(records, nodes, aliases)
        write_match_table(matches, match_path)
        vectors = load_embedding_vectors(slim)
        details = {}
        points, neighbors = compute_umap_and_neighbors(
            records, matches, vectors, method=args.method, receipt_details=details
        )
        staged_map, staged_neighbors = stage / args.umap_out.name, stage / args.out_neighbors.name
        write_json(staged_map, points)
        write_json(staged_neighbors, neighbors)
        receipt = make_receipt(
            source=source_receipt,
            corpus=corpus,
            ledger=details["ledger"],
            matrix=details["matrix"],
            projection=details["projection"],
            coverage={
                "eligible": len(records),
                "projected": len(points),
                "omitted": len(records) - len(points),
                "neighbor_records": len(neighbors),
            },
            auxiliary={"aliases": alias_receipt},
        )
        receipt["nearest_neighbors"] = details["nearest_neighbors"]
        if corpus_receipt(sorted(TRAITS_DIR.rglob("*.yaml")), TRAITS_DIR) != corpus:
            raise ValueError("Trait corpus changed during graph generation")
        if (file_sha256(args.kgm_aliases) if args.kgm_aliases.is_file() else None) != alias_receipt[
            "sha256"
        ]:
            raise ValueError("Alias table changed during graph generation")
        write_projection_metadata(
            args.umap_out,
            generation_receipt=receipt,
            staged={
                args.out_deepwalk: slim,
                args.out_match: match_path,
                args.umap_out: staged_map,
                args.out_neighbors: staged_neighbors,
            },
        )
    print(
        f"{len(points)} verified {args.method} points and {len(neighbors)} neighbor records published"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
