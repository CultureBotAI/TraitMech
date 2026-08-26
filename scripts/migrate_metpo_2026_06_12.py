#!/usr/bin/env python3
"""Migrate the three active METPO label changes in the 2026-06-12 release.

Safe by default: without ``--apply`` this validates the locked source and
reports the three records that would change. Stable identifiers, filenames,
graph ids, node ids, evidence snippets, and earlier curation history are never
rewritten. Only source-owned labels/synonyms plus the one upstream definition
and parent change are migrated.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from fetch_exact_synonym_snapshots import LockedSnapshot, read_manifest, verify
from seed_from_metpo import OWL_PATH, parse_owl
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import ValidationFailedError, write_validated_trait

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "reports" / "ontology_snapshot_manifest.tsv"
SCHEMA = REPO_ROOT / "src" / "traitmech" / "schema" / "traitmech.yaml"
MIGRATION_TIMESTAMP = "2026-08-26T07:35:00Z"


@dataclass(frozen=True)
class Migration:
    path: str
    curie: str
    old_label: str
    old_definition: str
    old_parents: tuple[str, ...]


MIGRATIONS = (
    Migration(
        "data/traits/environment/alkaphilic.yaml",
        "METPO:1003002",
        "alkaphilic",
        "A pH growth preference in which an organism grows optimally at pH values "
        "above 9.",
        ("METPO:1003000",),
    ),
    Migration(
        "data/traits/environment/obligately_alkaphilic.yaml",
        "METPO:1003004",
        "obligately alkaphilic",
        "A pH growth preference in which an organism requires alkaline conditions "
        "(typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.",
        ("METPO:1003000",),
    ),
    Migration(
        "data/traits/environment/facultatively_alkaphilic.yaml",
        "METPO:1003005",
        "facultatively alkaphilic",
        "A pH growth preference in which an organism can grow at alkaline pH but "
        "does not require it.",
        ("METPO:1003000",),
    ),
)


def _locked_metpo() -> LockedSnapshot:
    matches = [row for row in read_manifest(MANIFEST) if row.ontology == "METPO"]
    if len(matches) != 1:
        raise ValueError("snapshot manifest must contain exactly one METPO row")
    ok, detail = verify(OWL_PATH, matches[0])
    if not ok:
        raise ValueError(f"data/raw/metpo.owl does not match the lock: {detail}")
    return matches[0]


def _source_synonyms(source: dict[str, Any]) -> list[dict[str, str]]:
    label = str(source.get("label") or "").strip().casefold()
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for synonym in source.get("synonyms") or []:
        text = str(synonym.get("text") or "").strip()
        key = text.casefold()
        if not text or key == label or key in seen:
            continue
        seen.add(key)
        out.append({
            "synonym_text": text,
            "synonym_type": str(synonym["type"]),
            "source": "metpo.owl",
        })
    return out


def migrate_doc(
    doc: dict[str, Any], source: dict[str, Any], migration: Migration
) -> list[str]:
    """Apply one guarded three-way migration in memory and return changes."""
    if doc.get("identifier") != migration.curie:
        raise ValueError(f"{migration.path}: expected identifier {migration.curie}")
    new_label = str(source.get("label") or "")
    if not new_label or source.get("deprecated"):
        raise ValueError(f"{migration.curie}: new source term is missing or deprecated")
    if doc.get("label") not in {migration.old_label, new_label}:
        raise ValueError(
            f"{migration.curie}: record label {doc.get('label')!r} is neither the old "
            f"nor new canonical label"
        )

    changes: list[str] = []
    if doc.get("label") == migration.old_label:
        doc["label"] = new_label
        changes.append(f"label {migration.old_label!r} -> {new_label!r}")

    new_definition = source.get("definition")
    if doc.get("definition") == migration.old_definition and new_definition != migration.old_definition:
        doc["definition"] = new_definition
        changes.append("definition synchronized to METPO 2026-06-12")

    old_parents = tuple(sorted(migration.old_parents))
    new_parents = tuple(sorted(source.get("parents") or []))
    current_parents = tuple(sorted(doc.get("parent_traits") or []))
    if current_parents == old_parents and new_parents != old_parents:
        if new_parents:
            doc["parent_traits"] = list(new_parents)
        else:
            doc.pop("parent_traits", None)
        changes.append(f"parent_traits {old_parents!r} -> {new_parents!r}")

    retained = [
        synonym
        for synonym in (doc.get("synonyms") or [])
        if synonym.get("source") != "metpo.owl"
    ]
    desired_synonyms = _source_synonyms(source) + retained
    if desired_synonyms != (doc.get("synonyms") or []):
        doc["synonyms"] = desired_synonyms
        changes.append("synonyms synchronized at ontology-declared scope")

    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            if (
                node.get("grounding") == migration.curie
                and node.get("label") == migration.old_label
            ):
                node["label"] = new_label
                changes.append(f"grounded node {node.get('node_id')} label synchronized")

    if changes:
        record_curation_event(
            doc,
            curator="migrate_metpo_2026_06_12",
            action="MIGRATE_METPO_RELEASE",
            changes=(
                "Migrated source-owned fields to locked METPO 2026-06-12: "
                + "; ".join(changes)
            ),
            timestamp=MIGRATION_TIMESTAMP,
            upsert=True,
        )
    return changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write validated YAML")
    args = parser.parse_args(argv)
    try:
        locked = _locked_metpo()
        source = parse_owl(OWL_PATH)
        changed = 0
        for migration in MIGRATIONS:
            path = REPO_ROOT / migration.path
            doc = yaml.safe_load(path.read_text())
            changes = migrate_doc(doc, source[migration.curie], migration)
            if not changes:
                print(f"UNCHANGED\t{migration.path}")
                continue
            changed += 1
            if args.apply:
                write_validated_trait(doc, path, target_class="TraitRecord", schema_path=SCHEMA)
            verb = "UPDATED" if args.apply else "WOULD_UPDATE"
            print(f"{verb}\t{migration.path}\t" + "; ".join(changes))
    except (
        KeyError,
        OSError,
        ValidationFailedError,
        ValueError,
        yaml.YAMLError,
    ) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(
        f"METPO {locked.version}: {changed} record(s) "
        + ("updated" if args.apply else "would update; re-run with --apply")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
