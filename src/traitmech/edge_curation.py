"""Pinned native reference-taxon assertions for EdgeMech (CLAW #767).

Canonical examples remain reference examples, not strain assays. Whole-record
review labels and taxon-agnostic mechanisms do not approve these assertions.
The optional CLAW contract runtime is checked by the dedicated adapter CI job.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

REPOSITORY = "CultureBotAI/TraitMech"
CLAW_COMMIT = "6141da81dc521d776e1ebcff1c4e63824313a9a1"
SCHEMA = "src/traitmech/schema/traitmech.yaml"
MAX_INPUT_BYTES = 16 * 1024 * 1024
NORMALIZATION = {
    "name": "traitmech-reference-example/v1",
    "subject": "exact native canonical_examples[index].taxon_id; no lineage expansion",
    "predicate": "biolink:has_phenotype",
    "object": "exact owning trait identifier; no label or polarity normalization",
    "payload": "complete owning record and selected example with zero-based position",
    "review": "unassessed; whole-record review never approves organism observations",
}


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _durable_parents(path: Path) -> None:
    missing = []
    candidate = path
    while not candidate.exists():
        missing.append(candidate)
        candidate = candidate.parent
    for candidate in reversed(missing):
        candidate.mkdir(exist_ok=False)
        _sync_directory(candidate.parent)


def _safe_path(path: Path, *, exists=True) -> Path:
    path = Path(path).absolute()
    if ".." in path.parts or any(part.is_symlink() for part in (path, *path.parents)):
        raise ValueError("Symlink or traversal is not allowed")
    if exists and not path.exists():
        raise ValueError(f"Missing path: {path}")
    return path


def _git(root: Path, *arguments: str) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True, check=False)
    if result.returncode:
        raise ValueError("Pinned native Git input is unavailable: " + result.stderr.decode(errors="replace"))
    return result.stdout


def _commit(root: Path, source_commit: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", source_commit):
        raise ValueError("A full immutable source commit is required")
    if _git(root, "rev-parse", source_commit + "^{commit}").decode().strip() != source_commit:
        raise ValueError("Source commit does not identify the pinned commit object")


def _read(root: Path, source_commit: str, path: str) -> bytes:
    from kg_microbe_curation.artifact import validate_relative_path

    validate_relative_path(path)
    entries = _git(root, "ls-tree", "-z", source_commit, "--", path).split(b"\0")
    entries = [entry for entry in entries if entry]
    if len(entries) != 1:
        raise ValueError(f"Missing pinned native file: {path}")
    metadata, actual = entries[0].split(b"\t", 1)
    mode, kind, object_id = metadata.split()
    if actual.decode() != path or kind != b"blob" or mode not in {b"100644", b"100755"}:
        raise ValueError("Native input must be a regular tracked blob")
    size = int(_git(root, "cat-file", "-s", object_id.decode()))
    if size > MAX_INPUT_BYTES:
        raise ValueError("Native input exceeds the 16 MiB bound")
    return _git(root, "cat-file", "blob", object_id.decode())


def record_paths(root: Path, source_commit: str) -> list[str]:
    root = _safe_path(root)
    _commit(root, source_commit)
    result = []
    for entry in _git(root, "ls-tree", "-rz", source_commit, "--", "data/traits").split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        path = raw_path.decode()
        if not path.endswith(".yaml"):
            continue
        mode, kind, _ = metadata.split()
        if kind != b"blob" or mode not in {b"100644", b"100755"}:
            raise ValueError("Trait corpus contains a nonregular tracked YAML input")
        result.append(path)
    return sorted(result)


def build_native_assertions(
    root: Path, source_commit: str, *, records: tuple[str, ...] | None = None,
    example_index: int | None = None,
):
    """Yield canonical envelopes from immutable Git blobs, never the working copy.

    Complete native records preserve evidence, conditions, units and any stated
    polarity. No taxon-agnostic causal edge is projected onto an example organism.
    """
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import (
        NATIVE_CONTRACT,
        native_assertion_id,
        validate_native_assertion,
    )
    from kg_microbe_reviews import load_document

    root = _safe_path(root)
    paths = record_paths(root, source_commit)
    if records is not None:
        if len(set(records)) != len(records) or not records or not set(records).issubset(paths):
            raise ValueError("Record selection is duplicate, empty or outside the pinned trait corpus")
        paths = list(records)
    if example_index is not None and (
        type(example_index) is not int or example_index < 0 or len(paths) != 1
    ):
        raise ValueError("An example index requires exactly one selected record")
    schema_bytes = _read(root, source_commit, SCHEMA)
    schema = load_document(schema_bytes)
    interpretation = {
        "normalization_contract": NORMALIZATION["name"],
        "normalizer_contract_sha256": sha256_json(NORMALIZATION),
        "schema_sha256": _sha(schema_bytes), "prefix_map_sha256": sha256_json(schema["prefixes"]),
    }
    for path in paths:
        raw = _read(root, source_commit, path)
        record = load_document(raw)
        identifier = record.get("identifier")
        if not isinstance(identifier, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+", identifier):
            raise ValueError("Owning trait must have its exact native CURIE")
        examples = record.get("canonical_examples") or []
        if not isinstance(examples, list):
            raise TypeError("canonical_examples must be a list")
        if example_index is not None and example_index >= len(examples):
            raise ValueError("Selected example does not exist")
        for index, example in enumerate(examples):
            if example_index is not None and index != example_index:
                continue
            if not isinstance(example, dict) or not re.fullmatch(r"NCBITaxon:[0-9]+", str(example.get("taxon_id", ""))):
                raise ValueError("Canonical example requires an exact native NCBITaxon CURIE")
            native_payload = {"owner_record": record, "example_index": index, "example": example}
            locator = {"repository": REPOSITORY, "commit": source_commit, "path": path,
                       "selector": {"record_identifier": identifier, "slot": "canonical_examples", "index": index}}
            review = {"record_mapping_status": record.get("mapping_status"),
                      "statement_review": None, "scope": "reference_taxon_example_only"}
            assertion = {
                "contract": NATIVE_CONTRACT,
                "native_locator": {**locator, "source_sha256": _sha(raw),
                                   "payload_sha256": sha256_json(native_payload)},
                "payload": {"subject": example["taxon_id"], "predicate": "biolink:has_phenotype",
                            "object": identifier, "interpretation": interpretation,
                            "context": {"scope": "reference_taxon_example_not_strain_assay",
                                        "native_example": example, "native_trait_identifier": identifier,
                                        "assay_conditions_inferred": False, "descendant_taxa_inferred": False,
                                        "polarity_inferred_from_label": False},
                            "native_payload": native_payload},
                "evidence": [{"evidence_id": "native-record", "locator": locator, "sha256": _sha(raw),
                              "ancestry": [], "payload": {"example_reference": example.get("reference"),
                                                           "record_evidence": record.get("evidence", [])}},
                             {"evidence_id": "native-schema",
                              "locator": {"repository": REPOSITORY, "commit": source_commit, "path": SCHEMA,
                                          "selector": {"class": "CanonicalExample"}},
                              "sha256": _sha(schema_bytes), "ancestry": []}],
                "native_review": {"status": "unassessed", "locator": None, "sha256": None,
                                  "payload": review, "payload_sha256": sha256_json(review),
                                  "rationale": "No statement-scoped assay review is imported. Whole-record mapping status and mechanism review do not approve this organism assertion."},
                "assurance": "unassessed", "independent_scientific_review": False,
                "limitations": [
                    "Canonical examples describe reference taxa and do not supply strain-specific assay observations.",
                    "Native evidence and free-text qualifiers are retained without inferring conditions, units or polarity.",
                    "Taxon-agnostic causal mechanisms are retained as native context and confer no organism-edge approval.",
                    "Whole-record and corpus reviews are not imported as per-example scientific decisions.",
                ],
            }
            assertion["assertion_id"] = native_assertion_id(assertion)
            validate_native_assertion(assertion)
            yield assertion


def verify_export(output: Path) -> dict:
    from kg_microbe_curation.artifact import validate_relative_path
    from kg_microbe_curation.identity import canonical_json
    from kg_microbe_curation.native import NATIVE_CONTRACT, validate_native_assertion

    output = _safe_path(output)
    manifest_path = _safe_path(output / "manifest.json")
    if manifest_path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError("Export manifest exceeds the byte bound")
    manifest = json.loads(manifest_path.read_bytes())
    fixed = {"schema_version": 1, "contract": NATIVE_CONTRACT, "repository": REPOSITORY,
             "shared_contract_commit": CLAW_COMMIT, "scope": "canonical_examples_only",
             "kg_occurrences_approved": 0, "independent_scientific_reviews": 0}
    if any(type(manifest.get(key)) is not type(value) or manifest[key] != value for key, value in fixed.items()):
        raise ValueError("Export manifest contract, repository or approval invariant differs")
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", str(manifest.get("source_commit", ""))):
        raise ValueError("Export source commit must be immutable")
    for field in ("adapter_sha256", "assertions_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(manifest.get(field, ""))):
            raise ValueError("Export manifest requires exact SHA256 digests")
    for field in ("rows", "assertions_bytes", "source_record_count", "source_corpus_record_count"):
        if type(manifest.get(field)) is not int or manifest[field] < 0:
            raise ValueError("Export counts must be nonnegative integers")
    selected = manifest.get("source_records")
    if not isinstance(selected, list) or not all(isinstance(path, str) for path in selected):
        raise ValueError("Export must declare its selected native record inventory")
    for source_path in selected:
        validate_relative_path(source_path)
        if not source_path.startswith("data/traits/") or not source_path.endswith(".yaml"):
            raise ValueError("Selected source is outside the trait corpus")
    if (len(set(selected)) != len(selected) or len(selected) != manifest["source_record_count"]
            or len(selected) > manifest["source_corpus_record_count"]):
        raise ValueError("Selected source inventory does not reconcile")
    example_index = manifest.get("example_index")
    if example_index is not None and (type(example_index) is not int or example_index < 0 or len(selected) != 1):
        raise ValueError("Export example selection is inconsistent")
    complete = len(selected) == manifest["source_corpus_record_count"] and example_index is None
    if type(manifest.get("complete_native_scope")) is not bool or manifest["complete_native_scope"] != complete:
        raise ValueError("Export completeness differs from declared native selection")
    path = _safe_path(output / "assertions.jsonl")
    checksum, counts, identifiers, positions, size = hashlib.sha256(), Counter(), set(), set(), 0
    with path.open("rb") as handle:
        while line := handle.readline(MAX_INPUT_BYTES + 1):
            if len(line) > MAX_INPUT_BYTES:
                raise ValueError("Native assertion line exceeds the byte bound")
            item = json.loads(line)
            validate_native_assertion(item)
            locator = item["native_locator"]
            if (locator["repository"] != manifest["repository"] or locator["commit"] != manifest["source_commit"]
                    or locator["path"] not in selected
                    or any(evidence["locator"]["repository"] != manifest["repository"]
                           or evidence["locator"]["commit"] != manifest["source_commit"] for evidence in item["evidence"])):
                raise ValueError("Native envelope differs from the declared source pin or selected records")
            if (item["native_review"]["status"] != "unassessed" or item["assurance"] != "unassessed"
                    or item["native_review"]["locator"] is not None or item["native_review"]["sha256"] is not None
                    or item["independent_scientific_review"] is not False):
                raise ValueError("Trait reference examples must remain unassessed without imported review")
            selector = locator["selector"]
            index = selector.get("index")
            if (selector.get("slot") != "canonical_examples" or type(index) is not int or index < 0
                    or (example_index is not None and index != example_index)):
                raise ValueError("Native example position differs from the selected scope")
            position = (locator["path"], index)
            if position in positions:
                raise ValueError("Duplicate native example position")
            positions.add(position)
            native_payload = item["payload"]["native_payload"]
            owner, example = native_payload["owner_record"], native_payload["example"]
            if (index != native_payload["example_index"] or index >= len(owner["canonical_examples"])
                    or example != owner["canonical_examples"][index]
                    or selector.get("record_identifier") != owner["identifier"]
                    or item["payload"]["subject"] != example["taxon_id"]
                    or item["payload"]["object"] != owner["identifier"]
                    or item["payload"]["predicate"] != "biolink:has_phenotype"
                    or item["payload"]["context"]["scope"] != "reference_taxon_example_not_strain_assay"):
                raise ValueError("Trait exemplar projection differs from its native payload")
            if line != canonical_json(item) + b"\n" or item["assertion_id"] in identifiers:
                raise ValueError("Noncanonical or duplicate persisted assertion")
            identifiers.add(item["assertion_id"])
            checksum.update(line)
            size += len(line)
            counts[item["native_review"]["status"]] += 1
    if (checksum.hexdigest() != manifest["assertions_sha256"] or size != manifest["assertions_bytes"]
            or len(identifiers) != manifest["rows"] or dict(counts) != manifest["native_status_counts"]):
        raise ValueError("Persisted assertion hashes or counters differ")
    return manifest


def publish(root: Path, source_commit: str, output: Path, *, records=None, example_index=None) -> dict:
    """Publish a new export with the verified manifest as the final atomic marker."""
    from kg_microbe_curation.identity import canonical_json
    from kg_microbe_curation.native import NATIVE_CONTRACT

    output = _safe_path(output, exists=False)
    if output.exists():
        raise ValueError("Refusing to replace an existing native export")
    paths = record_paths(root, source_commit)
    selected = tuple(paths) if records is None else records
    _durable_parents(output.parent)
    output.mkdir(exist_ok=False)
    _sync_directory(output.parent)
    with tempfile.TemporaryDirectory(prefix=".trait-native-stage-", dir=output) as temporary:
        stage = Path(temporary)
        checksum, counts, count, size = hashlib.sha256(), Counter(), 0, 0
        with (stage / "assertions.jsonl").open("xb") as handle:
            for assertion in build_native_assertions(root, source_commit, records=selected, example_index=example_index):
                line = canonical_json(assertion) + b"\n"
                handle.write(line)
                checksum.update(line)
                count += 1
                size += len(line)
                counts[assertion["native_review"]["status"]] += 1
            handle.flush()
            os.fsync(handle.fileno())
        manifest = {
            "schema_version": 1, "contract": NATIVE_CONTRACT, "repository": REPOSITORY,
            "source_commit": source_commit, "shared_contract_commit": CLAW_COMMIT,
            "adapter_sha256": _sha(Path(__file__).read_bytes()), "scope": "canonical_examples_only",
            "source_records": list(selected), "source_record_count": len(selected),
            "source_corpus_record_count": len(paths), "example_index": example_index,
            "complete_native_scope": set(selected) == set(paths) and example_index is None,
            "rows": count, "native_status_counts": dict(counts),
            "assertions_sha256": checksum.hexdigest(), "assertions_bytes": size,
            "independent_scientific_reviews": 0, "kg_occurrences_approved": 0,
        }
        with (stage / "manifest.json").open("xb") as handle:
            handle.write(canonical_json(manifest) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        verify_export(stage)
        _sync_directory(stage)
        os.link(stage / "assertions.jsonl", output / "assertions.jsonl")
        _sync_directory(output)
        os.link(stage / "manifest.json", output / "manifest.json")
        _sync_directory(output)
        _sync_directory(output.parent)
    return verify_export(output)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--record", action="append")
    selection.add_argument("--all", action="store_true")
    parser.add_argument("--example-index", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Publish; the default only plans immutable inputs")
    args = parser.parse_args(argv)
    records = tuple(args.record) if args.record else None
    if not args.write:
        paths = record_paths(args.root, args.source_commit)
        if records and not set(records).issubset(paths):
            parser.error("Selected record is outside the pinned corpus")
        print(json.dumps({"mode": "plan", "source_commit": args.source_commit,
                          "record_count": len(records) if records else len(paths),
                          "example_index": args.example_index, "output": str(args.output)}, sort_keys=True))
        return 0
    if args.output is None:
        parser.error("--write requires --output")
    print(json.dumps(publish(args.root, args.source_commit, args.output, records=records,
                             example_index=args.example_index), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
