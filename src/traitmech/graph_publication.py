"""Verify current trait-YAML binding before rendering specialty graph views.

Only current YAML and the committed slim graph generation are read. No model,
reducer or original multi-gigabyte embedding source is needed for publication.
"""

from __future__ import annotations

import csv
import json
import math
import os
from pathlib import Path

import yaml

from traitmech.graph_embedding_receipts import corpus_receipt, load_receipt

SHARED_OUTPUTS = {"trait_nearest_neighbors.json", "deepwalk_traits.tsv.gz", "metpo_to_kgm_node.tsv"}
PROJECTIONS = {"trait_umap.json": {"pacmap", "umap"}, "trait_graph.json": {"sfdp"}}
MATCH_METHODS = {"direct_metpo", "alias_table", "label_match", "parent_proxy", "no_match"}


def current_traits(directory: Path) -> tuple[dict, dict]:
    """Include ignored YAML and reject symlinked subtrees instead of omitting them."""
    if not directory.is_dir() or directory.is_symlink() or directory.parent.is_symlink():
        raise ValueError("missing real trait corpus")
    paths = []
    for parent, subdirs, files in os.walk(directory, followlinks=False):
        for name in subdirs + files:
            path = Path(parent) / name
            if path.is_symlink():
                raise ValueError(f"trait corpus symlink refused: {path}")
            if name in files and path.suffix == ".yaml":
                paths.append(path)
    corpus = corpus_receipt(paths, directory)
    records = {}
    for path in sorted(paths):
        doc = yaml.safe_load(path.read_text())
        if not isinstance(doc, dict) or not isinstance(doc.get("identifier"), str):
            raise ValueError(f"trait has no identifier: {path}")
        identifier = doc["identifier"].strip()
        if not identifier or identifier in records:
            raise ValueError("blank or duplicate current trait identifier")
        records[identifier] = {
            "label": (doc.get("label") or "").strip(),
            "category": path.parent.name,
        }
    if corpus_receipt(paths, directory) != corpus:
        raise ValueError("trait corpus changed while checking publication")
    return corpus, records


def _finite(value) -> bool:
    return type(value) in (int, float) and math.isfinite(value)


def _match_rows(path: Path, records: dict) -> dict:
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if set(reader.fieldnames or ()) != {
            "metpo_curie",
            "label",
            "category",
            "match_method",
            "n_kgm_nodes",
            "kgm_nodes",
        }:
            raise ValueError("unexpected trait match-table columns")
        rows = {}
        for row in reader:
            identifier = row["metpo_curie"]
            if identifier in rows or identifier not in records:
                raise ValueError("duplicate or unknown match-table trait")
            if any(row[key] != value for key, value in records[identifier].items()):
                raise ValueError("match-table metadata differs from current trait")
            nodes = [node.strip() for node in row["kgm_nodes"].split(";") if node.strip()]
            if (
                row["match_method"] not in MATCH_METHODS
                or int(row["n_kgm_nodes"]) != len(nodes)
                or len(set(nodes)) != len(nodes)
            ):
                raise ValueError("invalid trait match method or source-node count")
            rows[identifier] = row | {"nodes": nodes}
    if set(rows) != set(records):
        raise ValueError("match table does not cover all current traits")
    return rows


def _check_points(points, receipt, records, matches):
    ledger = {row["identifier"]: row for row in receipt["matching"]["rows"]}
    coverage = receipt["coverage"]
    if (
        set(ledger) != set(records)
        or coverage["eligible"] != len(records)
        or coverage.get("neighbor_records") != len(records)
        or coverage.get("omitted") != len(records) - coverage["projected"]
    ):
        raise ValueError("graph matching/coverage does not cover the current trait corpus")
    if (
        not isinstance(points, list)
        or any(not isinstance(row, dict) for row in points)
        or [row.get("id") for row in points] != receipt["matrix"]["row_ids"]
        or len(points) != coverage["projected"]
    ):
        raise ValueError("graph point identities differ from the ordered receipt")
    for identifier, row in ledger.items():
        found, missing = row["source_nodes"], row.get("missing_nodes")
        match = matches[identifier]
        if (
            not isinstance(missing, list)
            or len(set(found + missing)) != len(found + missing)
            or set(found + missing) != set(match["nodes"])
            or row.get("match_method") != match["match_method"]
            or row["status"] != ("projected" if found else "no_vectors")
        ):
            raise ValueError("graph ledger differs from the complete match table")
    by_id = {}
    for point in points:
        identifier = point["id"]
        if (
            any(not _finite(point.get(axis)) for axis in ("umap_x", "umap_y"))
            or any(point.get(key) != value for key, value in records[identifier].items())
            or point.get("match_method") != ledger[identifier]["match_method"]
            or point.get("kgm_nodes") != ledger[identifier]["source_nodes"]
        ):
            raise ValueError("graph point coordinates or metadata differ from current matching")
        by_id[identifier] = point
    return by_id


def _check_neighbors(neighbors, receipt, records, points):
    k = receipt.get("nearest_neighbors", {}).get("k")
    if (
        type(k) is not int
        or k < 1
        or not isinstance(neighbors, dict)
        or set(neighbors) != set(records)
    ):
        raise ValueError("neighbor coverage differs from current traits")
    for identifier, rows in neighbors.items():
        expected = min(k, len(points) - 1) if identifier in points else 0
        if not isinstance(rows, list) or len(rows) != expected:
            raise ValueError("neighbor count differs from the declared generation")
        seen, scores = set(), []
        for row in rows:
            if not isinstance(row, dict) or row.get("id") not in points:
                raise ValueError("neighbor target is outside the projected traits")
            target, score = row["id"], row.get("similarity")
            if (
                target == identifier
                or target in seen
                or not _finite(score)
                or not -1.000001 <= score <= 1.000001
                or any(
                    row.get(key) != points[target][key]
                    for key in ("label", "category", "match_method", "kgm_nodes")
                )
            ):
                raise ValueError("neighbor identity or metadata differs from graph points")
            seen.add(target)
            scores.append(score)
        if scores != sorted(scores, reverse=True):
            raise ValueError("neighbor similarities are not ordered")


def check_graph_receipts(root: Path) -> list[dict]:
    """Require both complete current generations before any page writer runs."""
    root = root.resolve()
    corpus, records = current_traits(root / "data/traits")
    directory = root / "data/embeddings"
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("missing real graph output directory")
    checked, previous = [], None
    for name, methods in PROJECTIONS.items():
        metadata = directory / name.replace(".json", ".metadata.json")
        receipt = load_receipt(metadata)
        if set(receipt["outputs"]) != SHARED_OUTPUTS | {name}:
            raise ValueError(
                "graph receipt must bind exactly the map, match, slim vectors and neighbors"
            )
        if receipt["projection"]["method"] not in methods:
            raise ValueError("unexpected graph projection method")
        if receipt["corpus"] != corpus:
            raise ValueError("graph corpus changed since generation; refresh both specialty maps")
        if previous is not None and (
            receipt["source"] != previous["source"]
            or receipt["matching"] != previous["matching"]
            or receipt.get("nearest_neighbors") != previous.get("nearest_neighbors")
            or any(
                receipt["outputs"][shared] != previous["outputs"][shared]
                for shared in SHARED_OUTPUTS
            )
        ):
            raise ValueError("paired graphs do not share one source and matching generation")
        matches = _match_rows(directory / "metpo_to_kgm_node.tsv", records)
        points = _check_points(
            json.loads((directory / name).read_text()), receipt, records, matches
        )
        _check_neighbors(
            json.loads((directory / "trait_nearest_neighbors.json").read_text()),
            receipt,
            records,
            points,
        )
        checked.append(
            {
                "map": name,
                "traits": len(records),
                "points": len(points),
                "corpus_sha256": corpus["sha256"],
                "source_sha256": receipt["source"]["sha256"],
            }
        )
        previous = receipt
    return checked
