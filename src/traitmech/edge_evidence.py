"""Inventory pinned native observation/review coverage for TraitMech #2083.

This is a source inventory, not a scientific review or an assertion exporter.
It never turns record status, free text or a selector match into approval.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from pathlib import Path

import yaml

from traitmech.edge_curation import REPOSITORY, SCHEMA, _git, _read, record_paths

REVIEW_SCHEMA = "schema/record_review.yaml"
OBSERVATION_FIELDS = (
    "observation_id", "experiment_id", "strain_id", "conditions", "measurement",
    "unit", "polarity", "review_id",
)


def _document(raw: bytes) -> dict:
    value = yaml.load(raw, Loader=yaml.CSafeLoader)
    if not isinstance(value, dict):
        raise ValueError("Native inventory inputs must be YAML mappings")
    return value


def _paths(root: Path, commit: str, directory: str) -> list[str]:
    paths = _git(root, "ls-tree", "-r", "--name-only", commit, "--", directory)
    return sorted(paths.decode().splitlines())


def inspect_inventory(root: Path, commit: str, *, records: tuple[str, ...] | None = None) -> dict:
    """Inspect immutable native blobs and record exact evidence limitations.

    Working-tree data/review paths are inventoried without gitignore filtering,
    but their contents do not override the explicit source commit. Review
    document hashes are inventoried; scientific review validity, historical
    input freshness and scope still require a separate adjudication.
    """
    root = Path(root).absolute()
    origin = _git(root, "remote", "get-url", "origin").decode().strip()
    if origin not in {
        f"https://github.com/{REPOSITORY}", f"https://github.com/{REPOSITORY}.git",
        f"git@github.com:{REPOSITORY}.git",
    }:
        raise ValueError("Native inventory repository identity mismatch")
    population = record_paths(root, commit)
    selected = population if records is None else list(records)
    if not selected or len(set(selected)) != len(selected) or not set(selected).issubset(population):
        raise ValueError("Inventory selection must name unique pinned trait records")
    inputs = {}

    def read(path):
        raw = _read(root, commit, path)
        inputs[path] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
        return _document(raw)

    schema, review_schema = read(SCHEMA), read(REVIEW_SCHEMA)
    example_slots = sorted(schema["classes"]["CanonicalExample"]["attributes"])
    record_slots = sorted(schema["classes"]["TraitRecord"]["attributes"])
    rows, counts = [], Counter()
    for path in selected:
        record = read(path)
        examples = record.get("canonical_examples") or []
        if not isinstance(examples, list) or any(not isinstance(item, dict) for item in examples):
            raise ValueError("Canonical examples must be native mappings")
        counts["records"] += 1
        counts["records_with_examples"] += bool(examples)
        counts["canonical_examples"] += len(examples)
        counts["records_with_observation_count"] += "observation_count" in record
        counts["records_with_dataset_references"] += bool(record.get("datasets"))
        counts["causal_graphs"] += len(record.get("causal_graphs") or [])
        for example in examples:
            counts["examples_with_reference"] += bool(example.get("reference"))
            counts["examples_with_note"] += bool(example.get("note"))
            if set(example) - set(example_slots):
                raise ValueError("Example contains fields outside the pinned native schema")
        rows.append({
            "path": path, "sha256": inputs[path]["sha256"],
            "identifier": record["identifier"], "mapping_status": record.get("mapping_status"),
            "canonical_examples": [
                {"index": index, "native_payload": example} for index, example in enumerate(examples)
            ],
            "observation_count": record.get("observation_count"),
            "dataset_references": record.get("datasets") or [],
        })
    review_paths = [path for path in _paths(root, commit, "reviews/structured")
                    if path.endswith("/review.yaml")]
    review_counts, target_counts, inventory = Counter(), Counter(), []
    selectors = []
    for path in review_paths:
        review = read(path)
        targets = review.get("targets") or []
        if not isinstance(targets, list) or any(not isinstance(item, dict) for item in targets):
            raise ValueError("Review targets must be mappings")
        review_counts[str(review.get("kind"))] += 1
        target_counts.update(str(target.get("kind")) for target in targets)
        relevant = []
        for target in targets:
            if target.get("path") not in selected:
                continue
            relevant.append({key: target.get(key) for key in (
                "target_id", "path", "selector", "kind", "record_class", "semantic_digest",
            )})
            if target.get("selector"):
                selector = target["selector"]
                selectors.append({
                    "review_path": path, "review_sha256": inputs[path]["sha256"],
                    "target_id": target.get("target_id"), "path": target["path"],
                    "selector": selector,
                    "exact_example_locator_syntax": bool(
                        isinstance(selector, str) and re.fullmatch(r"canonical_examples\[[0-9]+\]", selector)
                    ),
                    "scope_adjudicated": False,
                })
        inventory.append({
            "path": path, "sha256": inputs[path]["sha256"],
            "review_id": review.get("review_id"), "kind": review.get("kind"),
            "completion": review.get("completion"), "verdict": review.get("verdict"),
            "scientific_review_declared": review.get("scientific_review"),
            "source_revision": (review.get("source") or {}).get("git_revision"),
            "relevant_targets": relevant, "validated_as_assertion_review": False,
        })
    tracked_surface = set(_paths(root, commit, "data") + _paths(root, commit, "reviews"))
    local_surface = {
        path.relative_to(root).as_posix()
        for directory in (root / "data", root / "reviews")
        if directory.is_dir()
        for path in directory.rglob("*")
        if path.is_file() or path.is_symlink()
    }
    return {
        "format": "traitmech-native-evidence-inventory/v1", "repository": REPOSITORY,
        "source_commit": commit, "complete_record_scope": records is None,
        "record_population": len(population), "counts": dict(sorted(counts.items())),
        "schema": {
            "record_attributes": record_slots, "canonical_example_attributes": example_slots,
            "missing_structured_example_fields": [name for name in OBSERVATION_FIELDS if name not in example_slots],
            "observation_count_definition": schema["classes"]["TraitRecord"]["attributes"]["observation_count"]["description"],
            "review_target_attributes": sorted(review_schema["classes"]["ReviewTarget"]["attributes"]),
        },
        "structured_reviews": {"documents": len(review_paths), "by_kind": dict(review_counts),
                               "targets_by_kind": dict(target_counts), "selector_candidates": selectors,
                               "inventory": inventory},
        "records": rows, "inputs": inputs,
        "local_discovery": {"scope": ["data", "reviews"], "ignored_files_included": True,
                            "paths_not_in_source_commit": sorted(local_surface - tracked_surface),
                            "uncommitted_contents_used_as_evidence": False},
        "blockers": [
            "CanonicalExample stores reference taxa and free-text notes/citations; dedicated assay identity, conditions, units, polarity and review bindings are not represented by these fields.",
            "observation_count is an aggregate ranking signal, not a set of independently identified observations or experiments.",
            "Record and corpus reviews cannot be promoted to exact example approval by target path or record status. Selector candidates require source-byte, scope and evidence adjudication.",
            "External dataset references and quoted assay narratives require native observation extraction and review; they are not fetched or converted into assertions by this inventory.",
        ],
        "scientific_reviews_created": 0, "inherited_approvals_created": 0,
        "native_export_changed": False,
    }
