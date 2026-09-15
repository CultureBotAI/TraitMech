"""Omitted records cannot shift the per-point graph node provenance."""

import sys
import types

import numpy as np

from scripts.build_embedding_index import compute_umap_and_neighbors


def test_missing_first_trait_does_not_shift_proxy_or_point_source_nodes(monkeypatch):
    class Reducer:
        def __init__(self, **kwargs):
            self.n_neighbors, self.n_MN, self.n_FP = 1, 0, 1

        def fit_transform(self, values, **kwargs):
            return values[:, :2]

    monkeypatch.setitem(sys.modules, "pacmap", types.SimpleNamespace(PaCMAP=Reducer))
    records = [("METPO:missing", "Missing", [], "fixture", [])]
    records.extend((f"METPO:{i}", f"Trait {i}", [], "fixture", []) for i in range(6))
    records.append(("METPO:proxy", "Proxy", [], "fixture", ["METPO:1"]))
    matches = [
        {
            "metpo_curie": curie,
            "kgm_nodes": ""
            if curie == "METPO:missing"
            else "METPO:1"
            if curie == "METPO:proxy"
            else curie,
            "match_method": "parent_proxy" if curie == "METPO:proxy" else "direct_metpo",
        }
        for curie, *_ in records
    ]
    vectors = {f"METPO:{i}": np.array([i + 1, 2, 3.0]) for i in range(6)}
    details = {}
    points, neighbors = compute_umap_and_neighbors(
        records, matches, vectors, receipt_details=details
    )
    by_id = {row["id"]: row for row in points}
    assert by_id["METPO:0"]["kgm_nodes"] == ["METPO:0"]
    assert by_id["METPO:proxy"]["kgm_nodes"] == ["METPO:1"]
    assert by_id["METPO:proxy"]["match_method"] == "parent_proxy"
    assert neighbors["METPO:missing"] == []
    assert len(details["ledger"]) == 8 and len(points) == 7
    assert details["ledger"][0]["status"] == "no_vectors"
    for curie, rows in neighbors.items():
        assert all(row["id"] != curie for row in rows)
