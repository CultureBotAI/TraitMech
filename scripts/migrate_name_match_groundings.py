#!/usr/bin/env python3
"""Repair three wrong CURIEs from the kg-microbe name-match pass (#402).

#402 found `oxygen` (ENVIRONMENTAL_FACTOR) grounded ENVO:01001495, "dioxygen
dissolved in marine water", and asked whether the pass that produced it produced
others. It did. Sweeping the 136 rows in mappings/node_grounding.tsv whose notes
read "exact name match via kg-microbe index (enriched-corpus pass)" on two
heuristics -- the term markedly more specific than the node label, and the term
sharing no content word with it -- surfaced three more, all the SAME SHAPE: a
right-sounding name match onto a term from the wrong organism or mechanism, in a
BACTERIAL trait knowledge base.

    flagellar_motility                soil_dwelling.yaml
        "Flagellum-dependent cell motility"      -> GO:0003341 cilium movement
        Bacteria have flagella, not cilia.

    hydrogen_peroxide_detoxification  aerotolerant.yaml
        "Enzymatic removal of hydrogen peroxide" -> GO:0033355 ascorbate glutathione cycle
        A plant antioxidant pathway; bacteria use catalase/peroxidase.

    plant_tissue_colonization         plant_pathogen.yaml
        "Establishment of microbial growth in plant tissues"
                                                 -> GO:0140649 symbiont-mediated
                                                    cell-to-cell migration by invasive hypha
        Invasive hyphae are fungal.

Every one is skos:exactMatch at confidence=high, so each asserts the node IS
that term. None would be caught by validate-products or label-correspondence:
those check that a CURIE's label matches the TERM, never that the term matches
the NODE -- the gap #391 named.

TWO ARE REPLACED AND ONE IS RETRACTED, and the difference is whether a
replacement could be VERIFIED rather than remembered. GO:0071973 and GO:0042744
were resolved through this repo's own OAK adapter (conf/id_label_targets.yaml,
`GO: sqlite:obo:go`) before being written, and validate-products re-checks both
label pairs in CI. For plant tissue colonization nothing verified fits --
GO:0044409 is "symbiont ENTRY into host", GO:0051701 and GO:0044403 are the
generic interaction parents -- so it is dropped, following #403's precedent with
the ENVO term: guessing a replacement is the very act that produced these.

The mapping ROWS go with the records, in the same pass. docs/GROUNDING_POLICY.md
records why from the #352 retraction: the grounder keys on (label, node_type),
so leaving a row behind means the next `just ground-nodes --apply` restores
exactly what was removed.

Usage:
    python scripts/migrate_name_match_groundings.py [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import emit_trait_yaml  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"
MAPPING = REPO_ROOT / "mappings" / "node_grounding.tsv"
TIMESTAMP = "2026-08-17T06:00:00Z"
ACTION = "REGROUND_CAUSAL_NODES"

# node_id -> (old CURIE, new CURIE or None, new target label or None, why)
FIX: dict[str, tuple[str, str | None, str | None, str]] = {
    "flagellar_motility": (
        "GO:0003341", "GO:0071973", "bacterial-type flagellum-dependent cell motility",
        "Was GO:0003341 'cilium movement'. Bacteria have flagella, not cilia, and the "
        "node says 'Flagellum-dependent cell motility' — the match was on the word "
        "'motility' via the kg-microbe index (#402). Replaced with the term GO actually "
        "provides for this, resolved through the repo's own OAK adapter before being "
        "written rather than recalled.",
    ),
    "hydrogen_peroxide_detoxification": (
        "GO:0033355", "GO:0042744", "hydrogen peroxide catabolic process",
        "Was GO:0033355 'ascorbate glutathione cycle', a plant antioxidant pathway; "
        "bacteria detoxify H2O2 with catalase and peroxidases, which is what this node "
        "describes. Replaced with the generic catabolic term, resolved through the OAK "
        "adapter before being written.",
    ),
    "plant_tissue_colonization": (
        "GO:0140649", None, None,
        "Was GO:0140649 'symbiont-mediated cell-to-cell migration by invasive hypha'. "
        "Invasive hyphae are FUNGAL and this is a bacterial record. RETRACTED RATHER "
        "THAN REPLACED: nothing verified fits — GO:0044409 is 'symbiont entry into "
        "host', which is entry rather than establishment of growth, and GO:0051701 / "
        "GO:0044403 are the generic interaction parents. Guessing a plausible "
        "replacement is precisely the act that produced this grounding (#402, #403).",
    ),
}


def apply(dry_run: bool = False) -> int:
    touched = 0
    for path in sorted(TRAITS.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        rel = str(path.relative_to(TRAITS))
        notes, whys = [], []
        for graph in (doc.get("causal_graphs") or []):
            for node in (graph.get("nodes") or []):
                nid = node.get("node_id")
                if nid not in FIX:
                    continue
                old, new, _lab, why = FIX[nid]
                if node.get("grounding") != old:
                    continue
                if new:
                    node["grounding"] = new
                    notes.append(f"{nid}: {old} -> {new}")
                    print(f"  reground {rel:40s} {nid} {old} -> {new}")
                else:
                    node.pop("grounding", None)
                    notes.append(f"{nid}: {old} retracted")
                    print(f"  retract  {rel:40s} {nid} {old}")
                whys.append(why)
        if notes:
            record_curation_event(
                doc, curator="claude", action=ACTION, llm_assisted=True,
                timestamp=TIMESTAMP, upsert=True,
                changes=("Repaired a wrong CURIE from the kg-microbe name-match pass "
                         f"(issue 402): {'; '.join(notes)}. " + " ".join(whys)),
            )
            touched += len(notes)
            if not dry_run:
                path.write_text(emit_trait_yaml(doc))

    # The mapping rows, in the same pass — see the module docstring.
    rows = list(csv.DictReader(MAPPING.open(), delimiter="\t"))
    fields = rows[0].keys()
    drop_curies = {old for old, new, _l, _w in FIX.values() if new is None}
    remap = {old: (new, lab) for old, new, lab, _w in FIX.values() if new}
    kept = []
    for r in rows:
        cur = (r.get("target_curie") or "").strip()
        if cur in drop_curies:
            print(f"  drop row {r.get('label')!r} -> {cur}")
            continue
        if cur in remap:
            new, lab = remap[cur]
            print(f"  remap row {r.get('label')!r} {cur} -> {new}")
            r["target_curie"], r["target_label"] = new, lab
            r["notes"] = (r.get("notes") or "") + \
                " CORRECTED in TraitMech#405: the kg-microbe name match returned a" \
                " term from the wrong organism; replacement verified via OAK before" \
                " being written (#402)."
        kept.append(r)
    if not dry_run:
        with MAPPING.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(fields), delimiter="\t",
                               lineterminator="\n")
            w.writeheader()
            w.writerows(kept)
    print(f"\n{touched} node(s), {len(rows) - len(kept)} row(s) dropped"
          f"{' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
