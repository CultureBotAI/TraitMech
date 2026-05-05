#!/usr/bin/env python3
"""Vendor a slim trait subset of kg-microbe's deepwalk embeddings + build a
METPO CURIE ↔ kg-microbe trait-node match table.

Source
------
``../kg-microbe-projects/taxa_media/DeepWalkSkipGramEnsmallen_*.tsv.gz``
(1.2 GB, 200-dimensional, ~1M rows). The file predates METPO ingestion in
kg-microbe so it carries 0 METPO CURIEs directly; trait nodes appear under
kg-microbe's pre-METPO prefixes (`cell_shape:bacillus`, `motility:motile`,
`gram_stain:positive`, `assay:API_*`, `isolation_source:*`, etc.).

Bridge
------
``../kg-microbe/mappings/canonical/metpo_alias_mappings.tsv`` (~67 rows)
maps text labels → METPO CURIEs ("rod-shaped" → METPO:1000681). This script
combines that table with normalised-label matching to produce a per-METPO
match table.

Outputs
-------
1. ``data/embeddings/deepwalk_traits.tsv.gz``
   Slim copy of the source deepwalk: only rows whose subject is a
   trait-relevant kg-microbe node. ~899 rows × 200 dims, ≪1MB gzipped.
2. ``data/embeddings/metpo_to_kgm_node.tsv``
   Per-METPO-CURIE match: one row per METPO TraitRecord, with a
   semicolon-delimited list of matching kg-microbe trait-node IDs (may
   be empty when no label match resolves).

Usage
-----
    just build-embeddings       # uses default --kgm path
    python3 scripts/build_embedding_index.py --kgm <path>
"""
from __future__ import annotations

import argparse
import csv
import gzip
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_KGM_DEEPWALK = (
    REPO_ROOT.parent / "kg-microbe-projects" / "taxa_media"
    / "DeepWalkSkipGramEnsmallen_degreenorm_embedding_200_1_wouniprot__2024-09-25_03_07_47.tsv.gz"
)
DEFAULT_KGM_ALIASES = (
    REPO_ROOT.parent / "kg-microbe" / "mappings" / "canonical" / "metpo_alias_mappings.tsv"
)

# kg-microbe pre-METPO trait-node prefixes worth carrying into the slim subset.
# Match the prefix universe surveyed in the deepwalk file (see
# `awk '{split($1,a,":"); print a[1]}' | sort | uniq -c`).
_TRAIT_PREFIXES: tuple[str, ...] = (
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
    # ontology prefixes that may appear (PATO is METPO-overlap territory)
    "PATO:",
)

OUT_DIR = REPO_ROOT / "data" / "embeddings"
OUT_DEEPWALK = OUT_DIR / "deepwalk_traits.tsv.gz"
OUT_MATCH = OUT_DIR / "metpo_to_kgm_node.tsv"
TRAITS_DIR = REPO_ROOT / "data" / "traits"


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


def load_metpo_records(traits_dir: Path) -> list[tuple[str, str, list[str], str]]:
    """Return list of (curie, label, synonyms, category_dir) tuples for every
    seeded TraitRecord. Skips files that fail to parse."""
    import yaml  # lazy import; only this script needs it
    out: list[tuple[str, str, list[str], str]] = []
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
        category_dir = path.parent.name
        out.append((curie, label, synonyms, category_dir))
    return out


def build_match_table(
    metpo_records: list[tuple[str, str, list[str], str]],
    deepwalk_nodes: set[str],
    alias_table: dict[str, str],
) -> list[dict[str, str]]:
    """Match each METPO CURIE to ≥0 kg-microbe trait nodes via:
      1. Direct alias-table lookup on label / synonyms (METPO → kg-microbe text-form).
      2. Normalised-label substring match on the value half of `<prefix>:<value>`
         kg-microbe nodes.
    """
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
    for curie, label, synonyms, category in metpo_records:
        candidates: set[str] = set()
        method = ""

        # 1. Try alias-table reverse: METPO -> known normalised labels -> nodes
        for norm in metpo_to_norm_labels.get(curie, set()):
            if norm in nodes_by_normvalue:
                candidates.update(nodes_by_normvalue[norm])
                method = "alias_table"

        # 2. Direct normalised-label match (METPO label or synonyms)
        if not candidates:
            for txt in [label] + synonyms:
                norm = _normalise(txt)
                if norm and norm in nodes_by_normvalue:
                    candidates.update(nodes_by_normvalue[norm])
                    if not method:
                        method = "label_match"

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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kgm-deepwalk", type=Path, default=DEFAULT_KGM_DEEPWALK)
    ap.add_argument("--kgm-aliases", type=Path, default=DEFAULT_KGM_ALIASES)
    ap.add_argument("--out-deepwalk", type=Path, default=OUT_DEEPWALK)
    ap.add_argument("--out-match", type=Path, default=OUT_MATCH)
    args = ap.parse_args()

    if not args.kgm_deepwalk.exists():
        print(f"deepwalk source missing: {args.kgm_deepwalk}", file=sys.stderr)
        return 2

    print(f"[1/3] Vendoring slim deepwalk subset → {args.out_deepwalk}")
    n_rows, nodes = vendor_slim_deepwalk(args.kgm_deepwalk, args.out_deepwalk)
    print(f"      {n_rows} trait-relevant rows carried; {len(nodes)} unique node ids")

    print(f"[2/3] Loading metpo alias table → {args.kgm_aliases}")
    aliases = load_alias_table(args.kgm_aliases)
    print(f"      {len(aliases)} alias rows loaded")

    print(f"[3/3] Building METPO ↔ kg-microbe match table → {args.out_match}")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
