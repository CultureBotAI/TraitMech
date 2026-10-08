"""Check cyanophycin evidence grain, proposal context and fail-closed writing."""

import collections
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_cyanophycin_granule_trait as writer  # noqa: E402


def tsv(rows):
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PARENT_PROPOSAL", tmp_path / "parent.tsv")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    writer.PARENT_PROPOSAL.write_text(tsv([*writer.HEADERS, writer.PARENT_ROW]))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def evidence_items(record):
    yield from record["evidence"]
    for graph in record["causal_graphs"]:
        for edge in graph["edges"]:
            yield from edge["evidence"]
        for node in graph["nodes"]:
            for example in node.get("protein_examples", []):
                yield from example["evidence"]


def test_identity_scope_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000673"
    assert record["label"] == "cyanophycin granule"
    assert record["definition_source"] == writer.CELL_BIOLOGY
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["traitmech:000066"]
    assert "intracellular storage inclusion" in record["definition"]
    assert "nonribosomal" in record["definition"]
    assert not any(t in record["definition"] for t in ["spherical", "cphA", "equimolar"])
    assert all(record.get(k) is None for k in ["xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["causal_graphs"][0]["nodes"].clear()
    assert len(writer.build_record()["causal_graphs"][0]["nodes"]) == 5


def test_snippet_budget_and_direct_source_limits():
    record = writer.build_record()
    words = collections.Counter()
    for evidence in evidence_items(record):
        assert evidence["snippet"] and evidence["notes"]
        assert "..." not in evidence["snippet"]
        words[evidence["reference"]] += len(evidence["snippet"].split())
    assert set(words) == {
        writer.ACCUMULATION, writer.CELL_BIOLOGY, writer.PURIFICATION, writer.EXPRESSION,
    }
    assert max(words.values()) <= 25
    assert "Full text and figures were not accessible" in record["evidence"][0]["notes"]
    graph, = record["causal_graphs"]
    assert "actual figure images were not inspected" in graph["edges"][2]["evidence"][0]["notes"]
    assert "data not shown" in graph["edges"][3]["evidence"][0]["notes"]


def test_canonical_example_is_not_the_protein_source_or_expression_host():
    record = writer.build_record()
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:43989", "Crocosphaera subtropica ATCC 51142",
    )
    assert example["reference"] == writer.ACCUMULATION
    assert all(t in example["note"] for t in [
        "BH68", "rank no rank", "Texas Gulf coast", "10.1128/jb.175.5.1284-1292.1993",
        "not an independent cyanophycin assay",
    ])
    graph, = record["causal_graphs"]
    protein = graph["nodes"][0]
    assert protein["grounding"] == "InterPro:IPR011810"
    instance, = protein["protein_examples"]
    assert instance["uniprot_id"] == "UniProtKB:P56947"
    assert instance["taxon_id"] == "NCBITaxon:113355"
    assert instance["taxon_label"] == "Geminocystis herdmanii PCC 6308"
    assert instance["entry_status"] == "REVIEWED"
    assert instance["entry_version"] == 91 and instance["sequence_version"] == 2
    assert "proteome_id" not in instance
    assert "recombinant E. coli" in instance["role"]
    assert "AAF43647.2" in instance["evidence"][0]["notes"]
    assert "not one experiment" in graph["scope_notes"]
    assert "Kazusa-specific" in record["discussions"][1]["rationale"]


def test_graph_is_connected_and_semantically_typed():
    graph, = writer.build_record()["causal_graphs"]
    assert graph["scope_status"] == "MECHANISTIC"
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert len(nodes) == 5 and len(graph["edges"]) == 4
    trait = nodes["cyanophycin_granule_trait"]
    assert (trait["node_type"], trait["grounding"]) == ("TRAIT", writer.IDENTIFIER)
    assert nodes["cyanophycin_macromolecule"]["grounding"] == "CHEBI:65318"
    assert [(e["predicate_id"], nodes[e["subject"]]["node_type"],
             nodes[e["object"]]["node_type"]) for e in graph["edges"]] == [
        ("RO:0002327", "GENE_OR_PROTEIN", "BIOLOGICAL_PROCESS"),
        ("RO:0002234", "BIOLOGICAL_PROCESS", "CHEMICAL"),
        ("biolink:located_in", "CHEMICAL", "TRAIT"),
        ("RO:0002326", "TRAIT", "BIOLOGICAL_PROCESS"),
    ]
    visited = {trait["node_id"]}
    for _ in nodes:
        for edge in graph["edges"]:
            endpoints = {edge["subject"], edge["object"]}
            if endpoints & visited:
                visited.update(endpoints)
    assert visited == set(nodes)


def test_proposal_preserves_parent_semantics_and_matches_child():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == writer.HEADERS
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][:7] == writer.PARENT_ROW[:7]
    assert rows[2][8:] == writer.PARENT_ROW[8:]
    assert rows[2][7] == rows[3][7] == "metpo_traitmech_2026_10"
    assert writer.PARENT_ROW[7] == "metpo_traitmech_2026_06"
    assert rows[3][0] == writer.METPO_ID == "METPO:1062600"
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][4] == writer.PARENT_METPO_ID
    assert rows[3][5:7] == ["", ""]
    assert rows[3][10] == writer.IDENTIFIER
    assert set(rows[3][3].split("|")) == {
        f"TraitMech:data/traits/morphology/{writer.SLUG}.yaml",
        *(e["reference"] for e in evidence_items(record)),
    }


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    assert writer.PARENT_PROPOSAL.read_bytes() == before["parent.tsv"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


def test_timestamp_correction_preserves_original_event(isolated, monkeypatch):
    original = writer.build_record(corrected=False)
    writer.write_validated_trait(original, writer.TARGET)
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    corrected = yaml.safe_load(writer.TARGET.read_text())
    assert corrected["curation_history"][:-1] == original["curation_history"]
    assert {k: v for k, v in corrected.items() if k != "curation_history"} == {
        k: v for k, v in original.items() if k != "curation_history"
    }
    event = corrected["curation_history"][-1]
    assert event["action"] == "CORRECT_CURATION_PROVENANCE"
    assert event["timestamp"] == writer.CORRECTION_TIMESTAMP
    assert "#1816" in event["changes"]
    assert "upper bound" in event["changes"]
    assert "not an exact reconstructed write time" in event["changes"]


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_existing_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", list(writer.PARENT))
def test_parent_projection_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("column", range(11))
def test_parent_proposal_cell_drift_refused(isolated, monkeypatch, column):
    row = writer.PARENT_ROW.copy()
    row[column] = "drift"
    writer.PARENT_PROPOSAL.write_text(tsv([*writer.HEADERS, row]))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent proposal differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_duplicate_parent_proposal_row_refused(isolated, monkeypatch):
    writer.PARENT_PROPOSAL.write_text(tsv([
        *writer.HEADERS, writer.PARENT_ROW, writer.PARENT_ROW,
    ]))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent proposal differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL", "PARENT_PROPOSAL"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unrecognized_field"] = "must not be written"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
