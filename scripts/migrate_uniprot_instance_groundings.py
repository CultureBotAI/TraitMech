#!/usr/bin/env python3
"""Replace organism-specific UniProt graph groundings with semantic terms.

The historical UniProt matching pass selected one protein accession by label.
That made taxon-agnostic causal nodes denote arbitrary protein instances, often
from organisms unrelated to the record's canonical examples.  The current
schema cannot pair a protein instance with its source taxon, so this curated
pass uses exact GO/InterPro terms where available and otherwise restores the
node to label-only status.

Default is a dry run. Pass ``--apply`` to update trait YAML files.
"""

from __future__ import annotations

import argparse
import csv
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
CANDIDATES = REPO_ROOT / "mappings/uniprot_regrounding_candidates.tsv"
CURATION_ACTION = "REVIEW_UNIPROT_INSTANCE_GROUNDINGS"
PREFIX = "UniProtKB:"

# Curator-verified against current UniProt cross-references and the named
# InterPro/GO records. These identify a family, complex, or molecular function
# rather than one organism's protein instance.
REPLACEMENTS = {
    "cote": "InterPro:IPR018901",
    "diviva": "InterPro:IPR007793",
    "flab": "InterPro:IPR001492",
    "flhg": "InterPro:IPR033875",
    "flif": "InterPro:IPR000067",
    "ftsa": "InterPro:IPR020823",
    "ftsh protease": "InterPro:IPR005936",
    "ftsz": "InterPro:IPR000158",
    "k+/h+ antiporters": "GO:0015386",
    "roda": "InterPro:IPR001182",
    "rodz": "InterPro:IPR023690",
    "scy": "InterPro:IPR048240",
    "spoiim": "InterPro:IPR002798",
    "spovm": "InterPro:IPR012609",
    "sula": "InterPro:IPR004596",
    "cation/proton antiporter": "GO:0051139",
    "cytochrome c oxidase": "GO:0045277",
    "cytochrome cd1 nitrite reductase nirs": "GO:0050421",
    "methyl-coenzyme m reductase": "GO:0044674",
    "multicopper oxidase": "InterPro:IPR045087",
    "nitrogenase": "GO:0016610",
    "nitrous oxide reductase nosz": "GO:0050304",
    "phytoene desaturase": "InterPro:IPR014102",
    "polyketide synthase (pks)": "GO:0016218",
    "proteorhodopsin": "InterPro:IPR017402",
    "rhodopsin": "InterPro:IPR001425",
}

# These labels are too broad, denote a complex whose subunits vary, or lack an
# exact whole-protein/family term. Label-only is preferable to a false instance.
RETRACT_ONLY = {
    "cooa",
    "glms",
    "perr",
    "spovid",
    "acetyl-coa/propionyl-coa carboxylase",
    "cytochrome bd oxidase",
    "ferredoxin:nad+ oxidoreductase",
    "hydrogenase",
    "malonyl-coa reductase",
    "methyltransferase",
    "quorum-quenching enzyme",
    "sigma e",
    "terminal oxidase",
}


def gene_nodes(doc: dict):
    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            if node.get("node_type") == "GENE_OR_PROTEIN":
                yield node


def unhandled_labels(docs: dict[Path, dict]) -> set[str]:
    handled = set(REPLACEMENTS) | RETRACT_ONLY
    return {
        str(node.get("label", "")).casefold()
        for doc in docs.values()
        for node in gene_nodes(doc)
        if str(node.get("grounding", "")).startswith(PREFIX)
        and str(node.get("label", "")).casefold() not in handled
    }


def migrate_doc(doc: dict) -> list[tuple[str, str, str | None]]:
    """Mutate one document and return (node_id, old, new) changes."""
    changes = []
    for node in gene_nodes(doc):
        old = str(node.get("grounding", ""))
        if not old.startswith(PREFIX):
            continue
        label = str(node.get("label", "")).casefold()
        new = REPLACEMENTS.get(label)
        if new:
            node["grounding"] = new
        else:
            del node["grounding"]
        changes.append((str(node.get("node_id", "?")), old, new))
    return changes


def reconcile_candidate_rows(rows: list[dict], node_counts: Counter) -> int:
    """Update the historical candidate table with final curator decisions."""
    changed = 0
    handled = set(REPLACEMENTS) | RETRACT_ONLY
    for row in rows:
        label = str(row.get("label", "")).casefold()
        if label not in handled:
            continue
        target = REPLACEMENTS.get(label, "")
        route = (
            "CURATED_GO"
            if target.startswith("GO:")
            else "CURATED_INTERPRO"
            if target.startswith("InterPro:")
            else "CURATED_LABEL_ONLY"
        )
        updates = {
            "n_nodes": str(node_counts[label]),
            "current_grounding": target,
            "current_status": "",
            "route": route,
            "target": target,
            "curator_decision": "APPLIED" if target else "RETRACTED",
            "note": (
                "curator-reviewed replacement; taxon-agnostic semantic grounding"
                if target
                else "curator-reviewed retraction; no exact whole-protein, family, complex, or activity term"
            ),
        }
        if any(row.get(key, "") != value for key, value in updates.items()):
            row.update(updates)
            changed += 1
    return changed


def sync_candidate_inventory(docs: dict[Path, dict], apply: bool) -> int:
    node_counts = Counter(
        str(node.get("label", "")).casefold()
        for doc in docs.values()
        for node in gene_nodes(doc)
    )
    with CANDIDATES.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        fieldnames = reader.fieldnames
    changed = reconcile_candidate_rows(rows, node_counts)
    if apply and changed:
        with CANDIDATES.open("w", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=fieldnames,
                delimiter="\t",
                lineterminator="\r\n",
            )
            writer.writeheader()
            writer.writerows(rows)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write changes to disk")
    args = parser.parse_args()

    docs = {
        path: yaml.safe_load(path.read_text()) or {}
        for path in sorted(TRAITS_DIR.glob("*/*.yaml"))
    }
    unknown = unhandled_labels(docs)
    if unknown:
        print("ERROR: unreviewed UniProt-grounded labels: " + ", ".join(sorted(unknown)))
        return 1

    candidate_rows = sync_candidate_inventory(docs, args.apply)

    tally = Counter()
    changed_files = 0
    for path, doc in docs.items():
        changes = migrate_doc(doc)
        if not changes:
            continue
        changed_files += 1
        replaced = sum(new is not None for _, _, new in changes)
        retracted = len(changes) - replaced
        tally["nodes"] += len(changes)
        tally["replaced"] += replaced
        tally["retracted"] += retracted
        print(path.relative_to(REPO_ROOT))
        for node_id, old, new in changes:
            print(f"    - {node_id}: {old} -> {new or '(label only)'}")

        if args.apply:
            record_curation_event(
                doc,
                curator="codex",
                action=CURATION_ACTION,
                changes=(
                    f"Reviewed {len(changes)} organism-specific UniProtKB grounding(s): "
                    f"replaced {replaced} with taxon-agnostic GO/InterPro terms and "
                    f"retracted {retracted} to label-only where no exact semantic term "
                    "was supported (docs/GROUNDING_POLICY.md)."
                ),
                llm_assisted=True,
            )
            try:
                write_validated_trait(doc, path)
            except ValidationFailedError as exc:
                print(exc.summary())
                return 1

    verb = "updated" if args.apply else "would update"
    print(
        f"\n{verb} {tally['nodes']} grounding(s) across {changed_files} files "
        f"({tally['replaced']} replacements, {tally['retracted']} retractions)"
    )
    print(f"{'updated' if args.apply else 'would update'} {candidate_rows} candidate inventory row(s)")
    if not args.apply:
        print("dry-run - pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
