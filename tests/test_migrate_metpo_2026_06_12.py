from __future__ import annotations

import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from migrate_metpo_2026_06_12 import MIGRATIONS, migrate_doc  # noqa: E402


def _source() -> dict:
    return {
        "label": "alkaliphilic",
        "definition": MIGRATIONS[0].old_definition,
        "parents": ["METPO:1003000"],
        "deprecated": False,
        "synonyms": [
            {"text": "alkaliphile", "type": "EXACT_SYNONYM"},
            {"text": "alkaliphilic", "type": "EXACT_SYNONYM"},
            {"text": "alkalophilic", "type": "EXACT_SYNONYM"},
        ],
    }


def _doc() -> dict:
    migration = MIGRATIONS[0]
    return {
        "identifier": migration.curie,
        "label": migration.old_label,
        "definition": migration.old_definition,
        "parent_traits": list(migration.old_parents),
        "synonyms": [
            {
                "synonym_text": "alkaliphilic",
                "synonym_type": "EXACT_SYNONYM",
                "source": "metpo.owl",
            },
            {
                "synonym_text": "curator alias",
                "synonym_type": "RELATED_SYNONYM",
                "source": "PMID:1",
            },
        ],
        "causal_graphs": [{
            "graph_id": "alkaphilic_stable_id",
            "nodes": [{
                "node_id": "alkaphilic_stable_id",
                "label": "alkaphilic",
                "grounding": migration.curie,
            }],
            "edges": [],
        }],
        "evidence": [{"reference": "PMID:1", "snippet": "verbatim alkaphilic"}],
    }


def test_migration_updates_labels_but_preserves_stable_ids_and_evidence():
    doc = _doc()
    migrate_doc(doc, _source(), MIGRATIONS[0])
    assert doc["label"] == "alkaliphilic"
    node = doc["causal_graphs"][0]["nodes"][0]
    assert node["label"] == "alkaliphilic"
    assert node["node_id"] == "alkaphilic_stable_id"
    assert doc["causal_graphs"][0]["graph_id"] == "alkaphilic_stable_id"
    assert doc["evidence"][0]["snippet"] == "verbatim alkaphilic"


def test_synonyms_follow_new_source_scope_and_preserve_curator_entries():
    doc = _doc()
    migrate_doc(doc, _source(), MIGRATIONS[0])
    texts = [synonym["synonym_text"] for synonym in doc["synonyms"]]
    assert texts == ["alkaliphile", "alkalophilic", "curator alias"]
    assert "alkaphilic" not in texts, "old canonical spelling is not source-declared"


def test_migration_is_idempotent():
    doc = _doc()
    migrate_doc(doc, _source(), MIGRATIONS[0])
    once = copy.deepcopy(doc)
    assert migrate_doc(doc, _source(), MIGRATIONS[0]) == []
    assert doc == once
