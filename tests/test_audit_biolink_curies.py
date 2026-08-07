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


def test_source_local_alone_does_not_exempt(tmp_path):
    """#350 review: the escape must not be a free-text cell.

    Exempting on `source=local` meant a future unbacked CURIE could be silenced
    by typing five characters into a TSV -- the failure this gate exists to
    catch, one level up.
    """
    m, b = _files(tmp_path, [_row("encodes", "biolink:encodes", "local")])
    assert [r["curie"] for r in unbacked(m, b)] == ["biolink:encodes"]


def test_an_explicitly_allowed_curie_is_exempt(tmp_path, monkeypatch):
    """The escape exists, but adding to it is a code change, not a cell edit."""
    import audit_biolink_curies as mod
    monkeypatch.setattr(mod, "ALLOWED_UNBACKED", frozenset({"biolink:encodes"}))
    m, b = _files(tmp_path, [_row("encodes", "biolink:encodes", "biolink")])
    assert mod.unbacked(m, b) == []


def test_non_biolink_curies_are_ignored(tmp_path):
    m, b = _files(tmp_path, [_row("reduces", "METPO:2007802", "METPO"),
                             _row("has output", "RO:0002234", "RO")])
    assert unbacked(m, b) == []


# --- the corpus half (#350 review) -------------------------------------------
#
# The mapping table is not the only way a CURIE reaches a record: a curator can
# type a predicate_id directly, and #342's point is that the CURIE in the RECORD
# is what a reader believes.

from audit_biolink_curies import corpus_biolink_curies  # noqa: E402


def _traits(tmp_path, *predicate_ids):
    """A record in the real shape: causal_graphs[].edges[].predicate_id.

    Deliberately the real structure -- the sweep parses rather than regexes, so a
    flat `edges:` fixture would pass through it unseen and prove nothing.
    """
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    edges = "\n".join(f"  - subject: a\n    object: b\n    predicate_id: {p}"
                      for p in predicate_ids)
    (d / "t.yaml").write_text(
        "identifier: traitmech:000001\ncausal_graphs:\n- graph_id: g\n  edges:\n" + edges + "\n")
    return d


def test_a_curie_typed_into_a_record_is_found(tmp_path):
    d = _traits(tmp_path, "biolink:not_a_slot")
    assert set(corpus_biolink_curies(d)) == {"biolink:not_a_slot"}


def test_non_biolink_predicate_ids_are_ignored(tmp_path):
    d = _traits(tmp_path, "METPO:2007813", "RO:0002234")
    assert corpus_biolink_curies(d) == {}


def test_the_example_file_is_reported_so_it_can_be_found(tmp_path):
    d = _traits(tmp_path, "biolink:produces")
    assert corpus_biolink_curies(d)["biolink:produces"].endswith("t.yaml")


def test_a_curie_only_mentioned_in_prose_is_not_flagged(tmp_path):
    """Why parsing beats a text scan: several records now DESCRIBE this issue in
    their curation_history, and a regex would flag those as live groundings."""
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    (d / "t.yaml").write_text(
        "identifier: traitmech:000002\n"
        "curation_history:\n"
        "- changes: 'Re-grounded off predicate_id: biolink:encodes to METPO:2007813.'\n")
    assert corpus_biolink_curies(d) == {}
