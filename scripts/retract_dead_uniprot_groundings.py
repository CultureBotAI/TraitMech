#!/usr/bin/env python3
"""Retract UniProtKB groundings whose accessions no longer exist in UniProt.

`scripts/audit_uniprot_grounding.py` found that most `UniProtKB:` groundings
on `GENE_OR_PROTEIN` causal nodes point at accessions UniProt has since
deleted. A CURIE that resolves to nothing is worse than no CURIE at all: it
looks grounded to every downstream consumer. This script demotes those nodes
back to label-only by removing the `grounding` key.

Deleted accessions are **not** recoverable automatically — UniProt ID-mapping
returns them unchanged with `obsoleteCount`, and UniParc keeps the sequence
but no live cross-references — so re-grounding is a separate curation pass
(see `mappings/uniprot_regrounding_candidates.tsv` and
`docs/GROUNDING_POLICY.md`).

Only accessions UniProt reports as `Inactive` are touched. Live entries are
left alone even when unreviewed, because deciding whether a TrEMBL accession
is the right *kind* of identifier for a node is a curation judgement, not a
resolvability fact.

Default is **dry-run**; pass `--apply` to write.

Usage:
    python scripts/retract_dead_uniprot_groundings.py            # dry-run
    python scripts/retract_dead_uniprot_groundings.py --apply
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import (
    ValidationFailedError,
    write_validated_trait,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data/traits"
API = "https://rest.uniprot.org/uniprotkb/{acc}.json"
CURATION_ACTION = "RETRACT_DEAD_UNIPROT_GROUNDINGS"
PREFIX = "UniProtKB:"


def classify(accession: str, delay: float) -> tuple[str, str]:
    """Return (status, replacement) for one accession.

    UniProt marks BOTH deleted and merged accessions `Inactive`, so entryType
    alone is not enough: a merged entry carries `mergeDemergeTo`, the live
    replacement. Retracting those would throw away information UniProt hands us
    directly, so only DELETED is retractable here.

    status is one of: live, deleted, merged, error.
    """
    time.sleep(delay)
    try:
        with urllib.request.urlopen(API.format(acc=accession), timeout=30) as resp:
            data = json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"  WARN: could not resolve {accession}: {exc}", file=sys.stderr)
        return "error", ""
    if data.get("entryType") != "Inactive":
        return "live", ""
    reason = data.get("inactiveReason", {}) or {}
    replacement = ",".join(reason.get("mergeDemergeTo", []) or [])
    kind = (reason.get("inactiveReasonType") or "").upper()
    return ("merged", replacement) if kind == "MERGED" else ("deleted", replacement)


def gene_nodes(doc: dict):
    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            if node.get("node_type") == "GENE_OR_PROTEIN":
                yield node


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write changes to disk")
    parser.add_argument("--delay", type=float, default=0.1)
    args = parser.parse_args()

    paths = sorted(TRAITS_DIR.glob("*/*.yaml"))
    docs = {}
    accessions = set()
    for path in paths:
        try:
            doc = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: unparseable {path}: {exc}", file=sys.stderr)
            continue
        docs[path] = doc
        for node in gene_nodes(doc):
            grounding = node.get("grounding") or ""
            if grounding.startswith(PREFIX):
                accessions.add(grounding[len(PREFIX):])

    print(f"resolving {len(accessions)} distinct accessions against UniProt ...")
    status = {acc: classify(acc, args.delay) for acc in sorted(accessions)}
    dead = {acc for acc, (kind, _) in status.items() if kind == "deleted"}
    merged = {acc: repl for acc, (kind, repl) in status.items() if kind == "merged"}
    errors = sorted(acc for acc, (kind, _) in status.items() if kind == "error")
    live = len(accessions) - len(dead) - len(merged) - len(errors)
    print(f"  {len(dead)} deleted, {len(merged)} merged, {live} live, "
          f"{len(errors)} unresolved\n")
    for acc, repl in sorted(merged.items()):
        print(f"  MERGED (left in place, needs curator): {acc} -> {repl or '?'}")
    if merged:
        print()

    tally = Counter()
    changed_files = 0
    for path, doc in docs.items():
        retracted = []
        for node in gene_nodes(doc):
            grounding = node.get("grounding") or ""
            if grounding.startswith(PREFIX) and grounding[len(PREFIX):] in dead:
                retracted.append((node.get("node_id", "?"), grounding))
                del node["grounding"]
        if not retracted:
            continue
        changed_files += 1
        tally["nodes"] += len(retracted)
        rel = path.relative_to(REPO_ROOT)
        print(f"{rel}")
        for node_id, grounding in retracted:
            print(f"    - {node_id}: {grounding} (deleted from UniProt)")

        if args.apply:
            record_curation_event(
                doc,
                curator="claude",
                action=CURATION_ACTION,
                changes=(
                    f"Retracted {len(retracted)} UniProtKB grounding(s) whose "
                    "accessions are deleted from UniProt; nodes demoted to "
                    "label-only pending re-grounding (docs/GROUNDING_POLICY.md)"
                ),
                llm_assisted=True,
            )
            try:
                write_validated_trait(doc, path)
            except ValidationFailedError as exc:
                print(exc.summary(), file=sys.stderr)
                return 1

    verb = "retracted" if args.apply else "would retract"
    print(f"\n{verb} {tally['nodes']} grounding(s) across {changed_files} file(s)")
    if not args.apply:
        print("dry-run — pass --apply to write")
    if errors:
        # Exiting 0 here would make a UniProt outage look identical to a clean
        # pass: "0 deleted", nothing retracted, success.
        print(f"\nERROR: {len(errors)} accession(s) could not be resolved "
              f"({', '.join(errors[:5])}{'...' if len(errors) > 5 else ''}); "
              "results are incomplete.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
