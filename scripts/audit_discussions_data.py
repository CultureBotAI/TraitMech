#!/usr/bin/env python3
"""Fail when the tracked discussions browser data is stale (#409).

The browser generator lives in culturebotai-claw, which is not checked out by
TraitMech's ordinary QC workflow.  This audit independently projects the small,
documented browser record shape from the authoritative trait YAML and compares
that semantic payload with ``app/discussions/data.js``.  It therefore catches
the failure that matters without rewriting the artifact it is judging.
"""

from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path
from typing import Any

import yaml

GAP_KINDS = {"KNOWLEDGE_GAP", "HUMAN_MODEL_MISMATCH"}


def _load_config(path: Path) -> dict[str, Any]:
    config = yaml.safe_load(path.read_text())
    if not isinstance(config, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    if not isinstance(config.get("record_glob"), str):
        raise ValueError(f"{path}: record_glob must be a string")
    return config


def _first_string(document: dict[str, Any], fields: list[str]) -> str:
    for field in fields:
        value = document.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _evidence_refs(discussion: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for evidence in discussion.get("evidence") or []:
        if isinstance(evidence, dict) and evidence.get("reference"):
            refs.append(str(evidence["reference"]))
    return refs


def build_expected(config_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any], str]:
    config = _load_config(config_path)
    config_dir = config_path.resolve().parent
    pattern = str(config_dir / config["record_glob"])
    name_fields = config.get("name_fields", ["name", "label", "preferred_term"])
    if not isinstance(name_fields, list) or not all(isinstance(x, str) for x in name_fields):
        raise ValueError(f"{config_path}: name_fields must be a list of strings")
    id_field = config.get("id_field")
    id_fields = [id_field] if isinstance(id_field, str) and id_field else ["identifier", "id"]
    discussions_field = config.get("discussions_field", "discussions")
    page_template = config.get("page_url_template", "")

    records: list[dict[str, Any]] = []
    for filename in sorted(glob.glob(pattern, recursive=True)):
        path = Path(filename)
        document = yaml.safe_load(path.read_text())
        if not isinstance(document, dict):
            continue
        discussions = document.get(discussions_field) or []
        source_name = _first_string(document, name_fields)
        source_id = _first_string(document, id_fields)
        for discussion in discussions:
            if not isinstance(discussion, dict):
                continue
            kind = discussion.get("kind", "")
            refs = _evidence_refs(discussion)
            discussion_id = discussion.get("discussion_id", "")
            page_url = ""
            if page_template:
                page_url = page_template.format(
                    stem=path.stem,
                    category=path.parent.name,
                    discussion_id=discussion_id,
                )
            records.append(
                {
                    "discussion_id": discussion_id,
                    "prompt": discussion.get("prompt", ""),
                    "kind": kind or "UNSPECIFIED",
                    "status": discussion.get("status", "") or "UNSPECIFIED",
                    "is_gap": "Knowledge gap" if kind in GAP_KINDS else "Other discussion",
                    "source_name": source_name,
                    "source_id": source_id,
                    "source_file": path.name,
                    "attaches_to": list(discussion.get("attaches_to") or []),
                    "rationale": discussion.get("rationale", ""),
                    "num_experiments": len(discussion.get("proposed_experiments") or []),
                    "num_evidence": len(refs),
                    "evidence_refs": refs,
                    "posed_by": discussion.get("posed_by", ""),
                    "page_url": page_url,
                }
            )

    metrics = {
        "total_discussions": len(records),
        "total_knowledge_gaps": sum(r["is_gap"] == "Knowledge gap" for r in records),
        "total_source_entries": len({r["source_id"] or r["source_file"] for r in records}),
        "kinds": sorted({r["kind"] for r in records}),
    }
    return records, metrics, str(config.get("repo_name", ""))


def _assignment(text: str, name: str) -> Any:
    marker = f"window.{name} = "
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"missing {marker.strip()!r} assignment")
    value, _ = json.JSONDecoder().raw_decode(text, start + len(marker))
    return value


def load_actual(path: Path) -> tuple[Any, Any, Any]:
    text = path.read_text()
    return (
        _assignment(text, "searchData"),
        _assignment(text, "searchMetrics"),
        _assignment(text, "repoName"),
    )


def audit(config_path: Path, data_path: Path) -> list[str]:
    expected = build_expected(config_path)
    actual = load_actual(data_path)
    names = ("searchData", "searchMetrics", "repoName")
    return [name for name, wanted, found in zip(names, expected, actual, strict=True) if wanted != found]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("conf/discussions_config.yaml"))
    parser.add_argument("--data", type=Path, default=Path("app/discussions/data.js"))
    args = parser.parse_args()

    try:
        stale = audit(args.config, args.data)
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"ERROR: discussions data staleness was not checked: {exc}")
        return 1
    if stale:
        print(f"STALE {args.data}: {', '.join(stale)} differs from trait YAML")
        print("Regenerate and commit it with: just gen-discussions-data")
        return 1
    records, metrics, _ = load_actual(args.data)
    print(
        f"discussions data current: {len(records)} discussion(s), "
        f"{metrics['total_source_entries']} source record(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
