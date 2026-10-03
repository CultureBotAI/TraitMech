"""Guarded citation repair preserves scope and refuses partial/drifted inputs."""

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import repair_legacy_canonical_citations_1626 as repair  # noqa: E402
from render_trait_pages import reference_url  # noqa: E402


def original(spec):
    return {
        **copy.deepcopy(spec["identity"]),
        "term_kind": "CLASS", "mapping_status": "REVIEWED",
        "canonical_examples": [
            {"taxon_id": "NCBITaxon:1", "taxon_label": "root", "note": "Keep this example",
             "reference": "https://example.org/unchanged"},
            copy.deepcopy(spec["before"]),
        ],
        "evidence": [{"reference": "DOI:10.1000/unchanged", "notes": "Preserved evidence"}],
        "synonyms": [{"synonym_text": "Retained alias", "synonym_type": "RELATED_SYNONYM"}],
        "xrefs": ["TEST:123"],
        "curation_history": [{
            "timestamp": "2026-01-01T00:00:00Z", "curator": "test",
            "action": "CREATE", "changes": "Preserve old event", "llm_assisted": False,
        }],
    }


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    monkeypatch.setattr(repair, "TRAITS_DIR", tmp_path)
    for slug, spec in repair.SPECS.items():
        path = tmp_path / f"{slug}.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(original(spec), sort_keys=False))
    return tmp_path


@pytest.mark.parametrize("spec", repair.SPECS.values(), ids=repair.SPECS.keys())
def test_updates_only_target_example_optional_evidence_and_appended_event(spec):
    before = original(spec)
    frozen = copy.deepcopy(before)
    after = repair.build_update(before, spec)
    assert before == frozen
    assert after["canonical_examples"][1] == spec["after"]
    assert reference_url(after["canonical_examples"][1]["reference"])
    assert after["curation_history"][-1] == repair.event(spec["changes"])
    restored = copy.deepcopy(after)
    restored["canonical_examples"][1] = copy.deepcopy(spec["before"])
    restored["curation_history"].pop()
    if spec.get("evidence"):
        assert restored["evidence"].pop() == spec["evidence"]
    assert restored == before
    assert repair.build_update(after, spec) == after


@pytest.mark.parametrize("spec", repair.SPECS.values(), ids=repair.SPECS.keys())
@pytest.mark.parametrize("key", [
    "identifier", "label", "definition", "definition_source", "parent_traits",
    "trait_category", "term_kind", "mapping_status",
])
def test_refuses_identity_and_scope_drift(spec, key):
    doc = original(spec)
    doc[key] = ["METPO:999"] if key == "parent_traits" else "drift"
    with pytest.raises(ValueError, match=f"{key} drifted"):
        repair.build_update(doc, spec)


@pytest.mark.parametrize("key", ["taxon_label", "reference", "note", "unexpected"])
@pytest.mark.parametrize("spec", repair.SPECS.values(), ids=repair.SPECS.keys())
def test_refuses_target_example_drift(spec, key):
    doc = original(spec)
    doc["canonical_examples"][1][key] = "drift"
    with pytest.raises(ValueError, match="example drifted"):
        repair.build_update(doc, spec)


@pytest.mark.parametrize("duplicate", [False, True])
def test_target_must_be_present_exactly_once(duplicate):
    spec = next(iter(repair.SPECS.values()))
    doc = original(spec)
    if duplicate:
        doc["canonical_examples"].append(copy.deepcopy(spec["before"]))
    else:
        doc["canonical_examples"].pop()
    with pytest.raises(ValueError, match="exactly one"):
        repair.build_update(doc, spec)


def test_rejects_partial_updates_and_postimage_provenance_drift():
    spec = repair.SPECS["morphology/lophotrichous"]
    partial = original(spec)
    partial["evidence"].append(copy.deepcopy(spec["evidence"]))
    with pytest.raises(ValueError, match="partial update"):
        repair.build_update(partial, spec)
    for key in ["evidence", "curation_history"]:
        after = repair.build_update(original(spec), spec)
        after[key].pop()
        with pytest.raises(ValueError, match="postimage"):
            repair.build_update(after, spec)


def test_dry_run_and_apply_are_idempotent(corpus):
    before = {path: path.read_bytes() for path in corpus.rglob("*.yaml")}
    assert repair.run() == 3
    assert all(path.read_bytes() == value for path, value in before.items())
    assert repair.run(apply=True) == 3
    applied = {path: path.read_bytes() for path in before}
    assert repair.run(apply=True) == 0
    assert all(path.read_bytes() == value for path, value in applied.items())


def test_last_prevalidation_failure_prevents_every_live_write(corpus, monkeypatch):
    before = {path: path.read_bytes() for path in corpus.rglob("*.yaml")}
    calls = []

    def fail_last(_doc, path):
        assert not path.is_relative_to(corpus)
        calls.append(path)
        if len(calls) == 3:
            raise ValueError("invalid final record")

    monkeypatch.setattr(repair, "write_validated_trait", fail_last)
    with pytest.raises(ValueError, match="invalid final record"):
        repair.run(apply=True)
    assert len(calls) == 3
    assert all(path.read_bytes() == value for path, value in before.items())


def test_last_input_drift_prevents_even_prevalidation(corpus, monkeypatch):
    path = corpus / "environment/halophily_preference.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["definition"] = "Changed by another curator"
    path.write_text(yaml.safe_dump(doc))
    before = {p: p.read_bytes() for p in corpus.rglob("*.yaml")}

    def unexpected_write(*_args):
        pytest.fail("a record was written before all preimages were checked")

    monkeypatch.setattr(repair, "write_validated_trait", unexpected_write)
    with pytest.raises(ValueError, match="definition drifted"):
        repair.run(apply=True)
    assert all(p.read_bytes() == value for p, value in before.items())


def test_source_replacement_is_not_described_as_identity_normalization():
    spec = repair.SPECS["morphology/lophotrichous"]
    assert "Recently divided, naturally unipolar" in spec["after"]["note"]
    assert "older bipolar" in spec["after"]["note"]
    assert "not all cells" in spec["after"]["note"]
    assert "not a PMID-to-DOI normalization" in spec["changes"]
    assert spec["after"]["reference"] == repair.SWAN
    assert "ATCC 19554" in spec["evidence"]["notes"]


def test_salt_examples_retain_same_source_with_strain_and_medium_bounds():
    for slug in ["environment/non_halophilic", "environment/halophily_preference"]:
        spec = repair.SPECS[slug]
        assert spec["after"]["reference"] == repair.LI
        assert spec["before"]["reference"] == "PMC8415458"
        for scope in ["BW25113", "LB", "37 C", "24 h", "3.5%", "not sodium-free"]:
            assert scope in spec["after"]["note"]
    assert repair.LI_EVIDENCE["snippet"].endswith("other tested groups")
