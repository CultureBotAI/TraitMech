"""Unit tests for the biolink CURIE resolution gate (#342).

The defect it replaces was not that `biolink:encodes` is a coinage -- coinages
are legitimate when nothing upstream fits -- but that the row CLAIMED biolink
provenance for a term the pinned model does not contain, and the one report that
recorded this was read by nobody.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_biolink_curies import curie_to_slot, unbacked  # noqa: E402

HEADER = ("label\ttarget_curie\ttarget_label\tpredicate_id\tsource\tconfidence\t"
          "subject_types\tobject_types\tnotes\n")
MODEL = "slots:\n  produces: {}\n  has gene product: {}\n"


def _files(tmp_path, rows):
    m = tmp_path / "m.tsv"
    m.write_text(HEADER + "".join(rows))
    b = tmp_path / "b.yaml"
    b.write_text(MODEL)
    return m, b


def _row(label, curie, source):
    return f"{label}\t{curie}\tx\tskos:exactMatch\t{source}\thigh\t*\t*\tn\n"


def test_curie_to_slot_matches_how_the_model_spells_it():
    assert curie_to_slot("biolink:has_gene_product") == "has gene product"


def test_a_resolving_curie_passes(tmp_path):
    m, b = _files(tmp_path, [_row("generates", "biolink:produces", "biolink")])
    assert unbacked(m, b) == []


def test_a_synonym_label_is_not_required_to_match_a_slot(tmp_path):
    """Most labels are synonyms: generates/yields/forms all ground to produces.
    Requiring the LABEL to be a slot name would flag correct rows."""
    m, b = _files(tmp_path, [_row("drives synthesis of", "biolink:produces", "biolink")])
    assert unbacked(m, b) == []


def test_a_curie_with_no_slot_is_flagged(tmp_path):
    m, b = _files(tmp_path, [_row("encodes", "biolink:encodes", "biolink")])
    got = unbacked(m, b)
    assert [r["curie"] for r in got] == ["biolink:encodes"]


def test_a_local_coinage_is_exempt(tmp_path):
    """The coinage stays legitimate; claiming biolink provenance does not."""
    m, b = _files(tmp_path, [_row("encodes", "biolink:encodes", "local")])
    assert unbacked(m, b) == []


def test_non_biolink_curies_are_ignored(tmp_path):
    m, b = _files(tmp_path, [_row("reduces", "METPO:2007802", "METPO"),
                             _row("has output", "RO:0002234", "RO")])
    assert unbacked(m, b) == []
