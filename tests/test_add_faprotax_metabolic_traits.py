from __future__ import annotations

import copy
import csv
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import add_faprotax_metabolic_traits as add_faprotax  # noqa: E402


@pytest.fixture()
def metabolism_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    trait_dir = tmp_path / "data" / "traits"
    metabolism = trait_dir / "metabolism"
    metabolism.mkdir(parents=True)
    monkeypatch.setattr(add_faprotax, "TRAIT_DIR", trait_dir)
    monkeypatch.setattr(add_faprotax, "METABOLISM_DIR", metabolism)
    return metabolism


def _write_yaml(path: Path, doc: dict) -> None:
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def _v11_proposal_rows() -> list[dict[str, str]]:
    proposal_tsv = REPO_ROOT / "proposals/metpo_traitmech_v11/metpo_proposal_classes_robot.tsv"
    with proposal_tsv.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def _v11_proposal_text() -> str:
    return (
        REPO_ROOT / "proposals/metpo_traitmech_v11/proposal.md"
    ).read_text(encoding="utf-8")


def test_new_records_skip_existing_same_id_records(metabolism_dir: Path):
    slug, raw = add_faprotax.NEW_RECORDS[0]
    path = metabolism_dir / f"{slug}.yaml"
    record = copy.deepcopy(raw)
    record["mapping_status"] = "REVIEWED"
    record["curation_history"] = [
        {
            "timestamp": "2026-09-09T00:00:00Z",
            "curator": "human",
            "action": "PROMOTE_TO_REVIEWED",
            "changes": "Curated the initial proposal.",
            "llm_assisted": False,
        }
    ]
    _write_yaml(path, record)

    outputs = add_faprotax._new_records()

    assert path not in {output for output, _ in outputs}


def test_replace_parent_removes_any_old_when_new_is_already_present():
    doc = {"parent_traits": ["METPO:1000802", "traitmech:000121", "traitmech:000122"]}

    assert add_faprotax._replace_parent(
        doc,
        ("METPO:1000802", "traitmech:000121"),
        "traitmech:000122",
    )
    assert doc["parent_traits"] == ["traitmech:000122"]


def test_canonical_nitrate_reducers_reparent_to_nitrate_respiration():
    reparents = {slug: new for slug, _, new, _ in add_faprotax.REPARENTS}

    assert reparents["denitrification"] == "traitmech:000122"
    assert reparents["dissimilatory_nitrate_reduction_to_ammonium"] == "traitmech:000122"


def test_faprotax_group_key_synonyms_are_related():
    records = dict(add_faprotax.NEW_RECORDS)

    for record in records.values():
        for synonym in record.get("synonyms", []):
            assert synonym["synonym_type"] == "RELATED_SYNONYM"


def test_dark_sulfur_oxidation_refines_sulfur_oxidation_without_go_close_match_xref():
    records = dict(add_faprotax.NEW_RECORDS)
    dark_sulfur_oxidation = records["dark_oxidation_of_sulfur_compounds"]

    assert dark_sulfur_oxidation["parent_traits"] == ["traitmech:000106"]
    assert dark_sulfur_oxidation["definition"].startswith("A sulfur oxidation in which")
    assert "GO:0019417" not in dark_sulfur_oxidation.get("xrefs", [])


def test_hydrogenotrophic_methanogenesis_has_no_broader_go_xref():
    records = dict(add_faprotax.NEW_RECORDS)
    hydrogenotrophic_methanogenesis = records["hydrogenotrophic_methanogenesis"]

    assert "GO:0019386" not in hydrogenotrophic_methanogenesis.get("xrefs", [])


def test_metpo_v11_dark_sulfur_parent_matches_lifted_sulfur_oxidation():
    dark_sulfur_oxidation = next(
        row for row in _v11_proposal_rows() if row["proposed_id"] == "METPO:1008812"
    )

    assert dark_sulfur_oxidation["parent"] == "METPO:1007705"


def test_metpo_v11_skips_duplicate_xylanolysis_class():
    proposed = {
        row["proposed_id"]: row["label"]
        for row in _v11_proposal_rows()
        if row["proposed_id"].startswith("METPO:")
    }

    assert "METPO:1008810" not in proposed
    assert "xylanolysis" not in proposed.values()


def test_metpo_v11_documents_existing_respiration_reparents():
    proposal = _v11_proposal_text()

    assert (
        "| `METPO:1007629` | dissimilatory nitrate reduction to ammonium | "
        "`METPO:1000802` | `METPO:1008801` |"
    ) in proposal
    assert (
        "| `METPO:1007703` | denitrification | `METPO:1000802` | "
        "`METPO:1008801` |"
    ) in proposal
    assert (
        "| `METPO:1007704` | dissimilatory sulfate reduction | "
        "`METPO:1000802` | `METPO:1008803` |"
    ) in proposal


def test_metpo_v11_nitrate_second_parent_note_does_not_claim_nitrite():
    proposal = _v11_proposal_text()

    assert "The same holds for" not in proposal


def test_metpo_v11_documents_scope_a_round_trip_plan():
    proposal = _v11_proposal_text()

    assert (
        "| A — synthetic trait class lift | 14 | every proposed class is now "
        "loaded locally as `traitmech:000121`–`traitmech:000134` |"
    ) in proposal
    assert "## Round-trip plan (Scope A)" in proposal
    assert "## Change log" in proposal
    assert "METPO:1008810` withdrawn" in proposal


def test_metpo_v11_group_keys_are_related_in_robot_template():
    rows = [
        row
        for row in _v11_proposal_rows()
        if row["proposed_id"].startswith("METPO:")
    ]

    for row in rows:
        assert row["exact_synonyms"] == ""
        assert row["related_synonyms"]


def test_metpo_v11_drops_dark_sulfur_go_closematch():
    mapping_tsv = REPO_ROOT / "proposals/metpo_traitmech_v11/metpo_proposal_mappings.sssom.tsv"
    proposal = _v11_proposal_text()

    assert "GO:0019417" not in mapping_tsv.read_text(encoding="utf-8")
    assert "phototrophic sulfur oxidation" not in proposal
