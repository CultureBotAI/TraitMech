"""Evidence inventory must not promote broad reviews or infer assay semantics."""

import hashlib

import pytest
import yaml

from traitmech import edge_evidence as audit


@pytest.fixture
def inventory(tmp_path, monkeypatch):
    record_path = "data/traits/physiology/example.yaml"
    review_path = "reviews/structured/20261107T000000Z-example/review.yaml"
    example = {"taxon_id": "NCBITaxon:1", "taxon_label": "Example strain",
               "note": "No growth at 40 degrees C; medium and strain qualifiers remain local.",
               "reference": "DOI:10.example/source"}
    documents = {
        audit.SCHEMA: {"classes": {
            "CanonicalExample": {"attributes": {key: {} for key in example}},
            "TraitRecord": {"attributes": {"canonical_examples": {},
                                            "observation_count": {"description": "Aggregate ranking count"}}},
        }},
        audit.REVIEW_SCHEMA: {"classes": {"ReviewTarget": {"attributes": {"path": {}, "selector": {}}}}},
        record_path: {"identifier": "traitmech:000001", "mapping_status": "REVIEWED",
                      "canonical_examples": [example], "observation_count": 500},
        review_path: {"review_id": "example", "kind": "record", "completion": "completed",
                      "verdict": "pass", "scientific_review": True,
                      "source": {"git_revision": "b" * 40},
                      "targets": [{"target_id": "example", "path": record_path,
                                   "selector": "canonical_examples[0]", "kind": "record"}]},
    }
    monkeypatch.setattr(audit, "record_paths", lambda root, commit: [record_path])
    monkeypatch.setattr(audit, "_read", lambda root, commit, path: yaml.safe_dump(documents[path]).encode())

    def git(root, *args):
        if args[:2] == ("remote", "get-url"):
            return b"https://github.com/CultureBotAI/TraitMech.git\n"
        directory = args[-1]
        return "\n".join(path for path in documents if path.startswith(directory + "/")).encode()

    monkeypatch.setattr(audit, "_git", git)
    return tmp_path, documents, record_path, review_path


def test_completed_selector_review_is_only_an_unadjudicated_candidate(inventory):
    root, _, _, _ = inventory
    report = audit.inspect_inventory(root, "a" * 40)
    assert report["counts"]["canonical_examples"] == 1
    assert report["records"][0]["observation_count"] == 500
    assert report["structured_reviews"]["selector_candidates"][0]["exact_example_locator_syntax"]
    assert not report["structured_reviews"]["selector_candidates"][0]["scope_adjudicated"]
    assert not report["structured_reviews"]["inventory"][0]["validated_as_assertion_review"]
    assert report["scientific_reviews_created"] == report["inherited_approvals_created"] == 0
    assert report["native_export_changed"] is False


def test_complete_native_qualifier_and_source_hash_are_preserved(inventory):
    root, documents, record_path, _ = inventory
    report = audit.inspect_inventory(root, "a" * 40)
    assert report["records"][0]["canonical_examples"][0]["native_payload"] == documents[record_path]["canonical_examples"][0]
    assert report["inputs"][record_path]["sha256"] == hashlib.sha256(yaml.safe_dump(documents[record_path]).encode()).hexdigest()
    assert "conditions" in report["schema"]["missing_structured_example_fields"]
    assert "polarity" in report["schema"]["missing_structured_example_fields"]


def test_ignored_surface_files_are_discovered_but_never_used_as_pinned_evidence(inventory):
    root, _, record_path, _ = inventory
    (root / "data").mkdir()
    (root / "data" / ".ignored-observation.yaml").write_text("unreviewed: true\n")
    (root / ".gitignore").write_text("data/.ignored-observation.yaml\n")
    report = audit.inspect_inventory(root, "a" * 40, records=(record_path,))
    assert report["complete_record_scope"] is False
    assert report["local_discovery"]["ignored_files_included"]
    assert report["local_discovery"]["paths_not_in_source_commit"] == ["data/.ignored-observation.yaml"]
    assert "data/.ignored-observation.yaml" not in report["inputs"]


@pytest.mark.parametrize("records", [(), ("missing",), ("data/traits/physiology/example.yaml",) * 2])
def test_invalid_selection_fails(inventory, records):
    root, _, _, _ = inventory
    with pytest.raises(ValueError, match="selection"):
        audit.inspect_inventory(root, "a" * 40, records=records)


def test_new_example_fields_require_explicit_inventory_support(inventory):
    root, documents, record_path, _ = inventory
    documents[record_path]["canonical_examples"][0]["invented_approval"] = True
    with pytest.raises(ValueError, match="outside the pinned native schema"):
        audit.inspect_inventory(root, "a" * 40)
