#!/usr/bin/env python3
"""Apply the reviewed pathway context manifest; dry-run unless --apply is given."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.pathway_links import load_index, pathway_link_errors  # noqa: E402
from traitmech.validation.write_validated import validate_trait, write_validated_trait  # noqa: E402


def proposed_changes(root: Path = ROOT) -> dict[Path, dict]:
    manifest = yaml.safe_load((root / "conf" / "pathway_context_links.yaml").read_text())
    protected = (root / "DO_NOT_WORK.md").read_text()
    version, records = load_index(root)
    changed = {}
    for target in manifest["targets"]:
        relative = target["path"]
        path = root / relative
        if not path.resolve().is_relative_to((root / "data" / "traits").resolve()):
            raise ValueError(f"target outside trait corpus: {relative}")
        if relative in protected or path.stem in protected:
            raise ValueError(f"protected trait: {relative}")
        original = yaml.safe_load(path.read_text())
        if original["identifier"] != target["identifier"]:
            raise ValueError(f"trait identifier changed: {relative}")
        doc = copy.deepcopy(original)
        for addition in target.get("links", []):
            nodes = [node for graph in doc.get("causal_graphs", [])
                     if graph["graph_id"] == addition["graph_id"]
                     for node in graph["nodes"] if node["node_id"] == addition["node_id"]]
            if len(nodes) != 1 or nodes[0]["label"] != addition["node_label"]:
                raise ValueError(f"node identity changed: {relative}/{addition['node_id']}")
            node = nodes[0]
            link = {"corpus": "PathwayMech", "identifier": addition["pathway"],
                    "relation": "PATHWAY_CONTEXT", "basis": addition["basis"],
                    "source_version": version}
            links = node.setdefault("related_records", [])
            matching = [old for old in links if old.get("corpus") == "PathwayMech"
                        and old.get("identifier") == link["identifier"]]
            if matching and matching != [link]:
                raise ValueError(f"existing pathway link differs: {relative}/{addition['node_id']}")
            if not matching:
                links.append(link)
        example = target.get("protein_example")
        if example:
            nodes = [node for graph in doc["causal_graphs"]
                     if graph["graph_id"] == example["graph_id"]
                     for node in graph["nodes"] if node["node_id"] == example["node_id"]]
            if len(nodes) != 1 or nodes[0].get("grounding") != example["expected_grounding"]:
                raise ValueError("protein node grounding changed")
            node = nodes[0]
            examples = node.setdefault("protein_examples", [])
            matching = [old for old in examples
                        if old["uniprot_id"] == example["value"]["uniprot_id"]]
            if matching and matching != [example["value"]]:
                raise ValueError("existing protein example differs")
            if not matching:
                examples.append(example["value"])
        if doc == original:
            continue
        record_curation_event(doc, curator="codex", action="ADD_PATHWAY_CONTEXT",
                              changes=target["changes"], llm_assisted=True)
        failures = pathway_link_errors(doc, version, records)
        failures.extend(str(error) for error in validate_trait(doc))
        if failures:
            raise ValueError(f"{relative}: {failures}")
        changed[path] = doc
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write validated trait changes")
    args = parser.parse_args(argv)
    changed = proposed_changes()
    for path, doc in changed.items():
        print(f"{'write' if args.apply else 'would write'} {path.relative_to(ROOT)}")
        if args.apply:
            write_validated_trait(doc, path)
    print(f"{len(changed)} trait record(s) {'written' if args.apply else 'proposed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
