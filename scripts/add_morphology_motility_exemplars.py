#!/usr/bin/env python3
"""Add canonical examples for three morphology/motility classes (#444).

`flagellar_arrangement`, `intracellular_inclusion`, and `motility` are upper
morphology classes whose graphs are NONMECHANISTIC: each spans alternative
mechanisms rather than one shared protein pathway. That is why they were left
without `canonical_examples` while narrower records were backfilled, and it is
also what makes a single "the" exemplar wrong for them.

Every example below is taken from the record's OWN deep-research artifact under
`research/traits/morphology/`, names an organism the cited source actually
characterizes, and carries a note that scopes the claim to the one arrangement,
inclusion type, or locomotion mechanism the source establishes. Nothing here
asserts that the exemplar realizes the whole class.

Deliberately NOT added:

  - Myxococcus xanthus for gliding motility. The motility artifact lists it as a
    taxon label but retrieves no cited gliding-mechanism claim for it, and the
    report warns against one generic gliding motor. An exemplar with no
    record-local citation is exactly the token entry #526 objects to.
  - Any quantitative-bin record. Those stay deferred under #475/#478.
  - Any gene or operon as a primary entry; genes appear only in graph metadata.

Taxon ids and labels were verified against UniProt/NCBI taxonomy, and every DOI
was resolved through Crossref, before this script was written.

Usage:
    python scripts/add_morphology_motility_exemplars.py           # dry run
    python scripts/add_morphology_motility_exemplars.py --apply   # write
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-26T19:05:00Z"
CURATOR = "claude"
ACTION = "ADD_CANONICAL_EXAMPLES"

TRANCHE: dict[str, list[dict[str, str]]] = {
    "morphology/flagellar_arrangement": [
        {
            "taxon_id": "NCBITaxon:319224",
            "taxon_label": "Shewanella putrefaciens CN-32",
            "note": (
                "Monotrichous polar flagellation: 92% of wild-type cells carry a "
                "single monopolar flagellum, and disrupting the FlhF FliG-binding "
                "region redistributes hooks to subpolar sites. Exemplifies the "
                "monotrichous arrangement class, not every flagellation pattern."
            ),
            "reference": "DOI:10.1038/s41467-024-50274-4",
        },
        {
            "taxon_id": "NCBITaxon:210",
            "taxon_label": "Helicobacter pylori",
            "note": (
                "Multi-flagellate polar tuft: wild-type populations centre on about "
                "four flagella per cell, and flhF/flhG deletions shift number and "
                "polar placement. Exemplifies a lophotrichous arrangement whose "
                "numerical control differs from monotrichous vibrios."
            ),
            "reference": "DOI:10.1128/JB.00110-23",
        },
    ],
    "morphology/intracellular_inclusion": [
        {
            "taxon_id": "NCBITaxon:64091",
            "taxon_label": "Halobacterium salinarum NRC-1",
            "note": (
                "Gas vesicle: a gas-filled, protein-shelled inclusion whose GvpA "
                "ribs and stabilising GvpC were characterised by deletion and "
                "interaction analysis in this organism. Exemplifies the gas-filled "
                "inclusion type only."
            ),
            "reference": "DOI:10.3389/fmicb.2022.971917",
        },
        {
            "taxon_id": "NCBITaxon:381666",
            "taxon_label": "Cupriavidus necator H16",
            "note": (
                "Polyhydroxybutyrate storage granule: the reference PHB-accumulating "
                "organism, whose PhaM activator and PhaP phasins set granule number, "
                "surface properties, and partitioning. Review-level synthesis of "
                "primary studies; exemplifies the storage-granule type only."
            ),
            "reference": "DOI:10.1093/femsre/fuaa058",
        },
        {
            "taxon_id": "NCBITaxon:431944",
            "taxon_label": "Magnetospirillum gryphiswaldense MSR-1",
            "note": (
                "Magnetosome: a membrane-bounded magnetite inclusion; the organism "
                "carries over 30 magnetosome-associated proteins, with the mamAB "
                "operon required for magnetosome membrane formation. Exemplifies the "
                "mineral-bearing organelle type only."
            ),
            "reference": "DOI:10.1111/mmi.15330",
        },
    ],
    "morphology/motility": [
        {
            "taxon_id": "NCBITaxon:90371",
            "taxon_label": "Salmonella enterica subsp. enterica serovar Typhimurium",
            "note": (
                "Flagellar swimming: the structural reference for the ion-driven "
                "rotary motor, where MotA-MotB torque generation turns a hook and "
                "filament to propel the cell. Exemplifies flagellar propulsion; its "
                "peritrichous run-and-tumble pattern is not universal."
            ),
            "reference": "DOI:10.3390/biom14121488",
        },
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Type IV pilus twitching: PilB-driven extension and PilT-driven "
                "retraction pull the cell across a surface, and blocking pilus "
                "assembly cuts the twitching zone by 63%. Exemplifies non-flagellar "
                "surface motility, a mechanism independent of the flagellar motor."
            ),
            "reference": "DOI:10.1038/s41467-024-52732-5",
        },
    ],
}

CHANGES = (
    "Added {n} source-backed canonical example(s) from this record's own "
    "deep-research artifact (issue 444): {taxa}. Each note scopes the exemplar to "
    "the single {kind} the cited source establishes, because this record is an "
    "upper class whose graph is NONMECHANISTIC and spans alternative mechanisms. "
    "Taxon ids and labels were verified against NCBI taxonomy and every DOI "
    "resolved through Crossref. No gene or operon was promoted to a primary entry."
)

KIND = {
    "morphology/flagellar_arrangement": "flagellation pattern",
    "morphology/intracellular_inclusion": "inclusion type",
    "morphology/motility": "locomotion mechanism",
}


def apply(write: bool = False) -> int:
    failures = 0
    for slug, examples in TRANCHE.items():
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        existing = doc.get("canonical_examples") or []
        have = {ex.get("taxon_id") for ex in existing if isinstance(ex, dict)}
        fresh = [ex for ex in examples if ex["taxon_id"] not in have]
        if not fresh:
            print(f"  {path.name}: already carries every exemplar; skipping")
            continue
        if existing and len(fresh) != len(examples):
            print(
                f"  {path.name}: partial overlap with existing examples; "
                "not writing (re-check the tranche by hand)",
                file=sys.stderr,
            )
            failures += 1
            continue
        doc["canonical_examples"] = existing + fresh
        record_curation_event(
            doc,
            curator=CURATOR,
            action=ACTION,
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
            changes=CHANGES.format(
                n=len(fresh),
                taxa=", ".join(f"{ex['taxon_label']} ({ex['taxon_id']})" for ex in fresh),
                kind=KIND[slug],
            ),
        )
        for ex in fresh:
            print(f"  {path.name}: + {ex['taxon_label']} {ex['taxon_id']} {ex['reference']}")
        if write:
            write_validated_trait(doc, path)

    total = sum(len(v) for v in TRANCHE.values())
    print(
        f"{total} canonical example(s) across {len(TRANCHE)} records"
        f"{'' if write else ' (dry run)'}",
        file=sys.stderr,
    )
    return int(failures > 0)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="write (default is a dry run)")
    return apply(ap.parse_args().apply)


if __name__ == "__main__":
    sys.exit(main())
