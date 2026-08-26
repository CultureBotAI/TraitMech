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

Taxon ids and labels were verified against NCBI taxonomy — which is what the
records store and what `just audit-canonical-examples` checks — and every DOI
was resolved through Crossref, before this script was written. Notes state what
the cited source actually measured: a localization percentage is not a per-cell
count, an overexpression phenotype is not a clean loss of function, and a
protein characterised in a heterologous host is not an in-situ observation.

Usage:
    python scripts/add_morphology_motility_exemplars.py           # dry run
    python scripts/add_morphology_motility_exemplars.py --apply   # write
"""
from __future__ import annotations

import argparse
import sys
import tempfile
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
                "Monotrichous polar flagellation: hooks are monopolar in about 92% "
                "of wild-type cells, and disrupting the FlhF FliG-binding region "
                "redistributes them to subpolar sites. The figure is a localization "
                "percentage, not a per-cell flagellar count. Exemplifies the "
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
            "taxon_id": "NCBITaxon:2242",
            "taxon_label": "Halobacterium salinarum",
            "note": (
                "Gas vesicle: a gas-filled, protein-shelled inclusion built from "
                "this organism's Gvp proteins, where GvpA forms the shell ribs and "
                "GvpC stabilises the exterior. The cited interaction and deletion "
                "analysis was performed on those proteins in a heterologous "
                "haloarchaeal host, so it establishes the protein roles rather than "
                "in-situ assembly. Exemplifies the gas-filled inclusion type only."
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
                "Flagellar swimming: a structural reference for the ion-driven "
                "rotary motor, where MotA-MotB torque generation turns a hook and "
                "filament to propel the cell; the cited review treats this organism "
                "together with Escherichia coli. Exemplifies flagellar propulsion; "
                "its peritrichous run-and-tumble pattern is not universal."
            ),
            "reference": "DOI:10.3390/biom14121488",
        },
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Type IV pilus twitching: PilB-dependent pilus assembly drives "
                "surface twitching, and overexpressing the regulator PlzR abolished "
                "detectable pili and cut the twitching zone by 63% on 1% agar. That "
                "figure comes from a gain-of-function overexpression that also "
                "reduced swimming and swarming, so pleiotropy is possible. "
                "Exemplifies non-flagellar surface motility, a mechanism "
                "independent of the flagellar motor."
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


def _write(doc: dict[str, Any], path: Path, write: bool) -> None:
    """Validate always; write only when applying.

    A dry run that skipped validation would prove nothing about the write it is
    previewing, so the dry run renders through the same closed-schema gate into
    a temporary file and throws the result away.
    """
    if write:
        write_validated_trait(doc, path)
        return
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(doc, Path(tmp) / path.name)


def apply(write: bool = False) -> int:
    failures = 0
    written = 0
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
        # Insert after `evidence` where possible: 250 of the 259 records that
        # carry examples order them that way, and EMIT_OPTS keeps insertion
        # order verbatim, so appending would grow the minority spelling.
        merged = existing + fresh
        if "canonical_examples" in doc:
            doc["canonical_examples"] = merged
        else:
            rebuilt: dict[str, Any] = {}
            for key, value in doc.items():
                rebuilt[key] = value
                if key == "evidence":
                    rebuilt["canonical_examples"] = merged
            if "canonical_examples" not in rebuilt:
                rebuilt["canonical_examples"] = merged
            doc.clear()
            doc.update(rebuilt)
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
        _write(doc, path, write)
        written += len(fresh)

    print(
        f"{written} canonical example(s) added"
        f"{'' if write else ' (dry run)'}; {failures} record(s) skipped on conflict",
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
