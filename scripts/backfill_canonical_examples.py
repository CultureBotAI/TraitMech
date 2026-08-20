#!/usr/bin/env python3
"""Backfill canonical_examples for records whose own artifact names exemplars (#444).

Batch 1, following the single-record canary on `environment/temperature_range_high`.

THE STANDARD, agreed with the maintainer: exemplar organisms come ONLY from the
record's own deep-research artifact, cited to a DOI that appears in that
artifact. No organism and no citation is supplied from memory, so there is no
fabrication surface. Every `taxon_id` below was resolved and label-checked
against the local NCBITaxon build rather than recalled.

WHY THIS IS SEVEN RECORDS AND NOT FIFTEEN. The artifacts name organisms as
CONTRAST CASES at least as often as exemplars, so a screen cannot be trusted and
every candidate needed reading. Excluded after review, all of them suggested by
the screen:

  ph_optimum_high      Bacillus subtilis -- a neutrophile. It appears in an
                       alkaliphile discussion as the comparison, not the example.
  ph_range_low         Escherichia coli -- a neutrophile, same pattern.
  facultative_psychrophilic
                       Escherichia coli -- cold-SHOCK response is not growth at
                       low temperature; the artifact is discussing the response.
  nacl_range_low       Halomonas elongata -- a moderate halophile growing past
                       20% NaCl, in a record whose upper bound is ~3%. The
                       screen's top hit for the record, and the wrong direction
                       entirely.

The canary hit the same thing (Escherichia coli and Pseudomonas putida named in a
>40 C record as mesophile contrasts), so this is the norm rather than bad luck.

TWO TAXA WERE DROPPED BY OFFLINE RESOLUTION, which is the reason for resolving
rather than recalling:

  Bacillus pseudofirmus   the classic alkaliphile, and absent from this
                          NCBITaxon build under any spelling -- it has been moved
                          to Alkalihalobacillus. Dropped rather than guessed.
  Caulobacter crescentus  resolves only as NCBITaxon:155892 `Caulobacter
                          vibrioides`, the current name. Recorded under the
                          current label with the artifact's name in the note, so
                          the id/label audit stays clean.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import yaml  # noqa: E402

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAITS = Path("data/traits")
TIMESTAMP = "2026-08-20T02:40:00Z"
CURATOR = "claude"

# file -> list of (taxon_id, taxon_label, reference, note)
PLAN: dict[str, list[tuple[str, str, str, str]]] = {
    "environment/facultative_oxygen_preference.yaml": [
        (
            "NCBITaxon:562",
            "Escherichia coli",
            "DOI:10.1111/1751-7915.70051",
            "Respires oxygen when it is available and switches to nitrate "
            "respiration or fermentation when it is not, which is the trait as "
            "defined.",
        ),
        (
            "NCBITaxon:1423",
            "Bacillus subtilis",
            "DOI:10.3390/ijms25021277",
            "Grows aerobically and, on oxygen limitation, by nitrate respiration "
            "or fermentation under the regulation described in this record.",
        ),
    ],
    "environment/temperature_optimum_high.yaml": [
        (
            "NCBITaxon:2261",
            "Pyrococcus furiosus",
            "DOI:10.1093/nar/gkab869",
            "Hyperthermophilic archaeon with an optimum near 100 degrees C; the "
            "reverse-gyrase supercoiling evidence in this trait's artifact is "
            "taxon-specific to it.",
        ),
        (
            "NCBITaxon:311400",
            "Thermococcus kodakarensis",
            "DOI:10.1128/JB.186.14.4829-4833.2004",
            "Hyperthermophilic archaeon used in this trait's artifact as the "
            "genetic system for the heat-adaptation mechanism.",
        ),
        (
            "NCBITaxon:43080",
            "Saccharolobus islandicus",
            "DOI:10.1111/1462-2920.16375",
            "Thermoacidophilic archaeon whose membrane-lipid response at its "
            "growth optimum is characterised in this trait's artifact.",
        ),
    ],
    "environment/temperature_optimum_low.yaml": [
        (
            "NCBITaxon:296",
            "Pseudomonas fragi",
            "DOI:10.37256/amtt.5220244537",
            "Cold-adapted organism whose best growth sits at the low end of the "
            "range, cited in this trait's artifact for psychrophilic adaptation.",
        ),
        (
            "NCBITaxon:1880678",
            "Pseudomonas sivasensis",
            "DOI:10.1007/s42770-023-01057-4",
            "Cold-adapted isolate cited in this trait's artifact for growth at "
            "low temperature.",
        ),
    ],
    "environment/facultative_psychrophilic.yaml": [
        (
            "NCBITaxon:334543",
            "Psychrobacter arcticus",
            "DOI:10.37256/amtt.5220244537",
            "Grows at low temperature rather than merely surviving it, which is "
            "the distinction this trait turns on.",
        ),
    ],
    "environment/ph_optimum_high.yaml": [
        (
            "NCBITaxon:1463663",
            "Bacillus aequororis",
            "DOI:10.1155/2024/3087296",
            "Alkaliphilic isolate whose best growth is at high external pH, "
            "cited in this trait's artifact for alkaliphile physiology.",
        ),
    ],
    "environment/ph_range_low.yaml": [
        (
            "NCBITaxon:920",
            "Acidithiobacillus ferrooxidans",
            "DOI:10.3390/fermentation10060298",
            "Acidophile growing in the low-pH range this record bounds, cited in "
            "its artifact for acidophile physiology.",
        ),
    ],
    "morphology/cell_width.yaml": [
        (
            "NCBITaxon:274",
            "Thermus thermophilus",
            "DOI:10.1038/s41467-023-39037-9",
            "Model organism for the RodA/MreB width-determining machinery "
            "described in this record.",
        ),
        (
            "NCBITaxon:155892",
            "Caulobacter vibrioides",
            "DOI:10.1101/197475",
            "Model organism for MreB-dependent width control; the artifact cites "
            "it under the earlier name Caulobacter crescentus, and the reference "
            "is a preprint.",
        ),
        (
            "NCBITaxon:562",
            "Escherichia coli",
            "DOI:10.1002/mbo3.1385",
            "Model rod whose peptidoglycan-synthesis complex sets cell width in "
            "the mechanism this record carries.",
        ),
    ],
}


def main() -> int:
    total = 0
    for rel, examples in sorted(PLAN.items()):
        path = TRAITS / rel
        doc = yaml.safe_load(path.read_text())
        if doc.get("canonical_examples"):
            print(f"SKIP {rel}: already has canonical_examples")
            continue
        doc["canonical_examples"] = [
            {"taxon_id": tid, "taxon_label": label, "reference": ref, "note": note}
            for tid, label, ref, note in examples
        ]
        record_curation_event(
            doc,
            curator=CURATOR,
            action="BACKFILL_CANONICAL_EXAMPLES",
            changes=(
                f"Added {len(examples)} exemplar taxon/taxa. Organisms and "
                "citations come only from this record's own deep-research "
                "artifact; every taxon id was resolved and label-checked against "
                "the local NCBITaxon build rather than recalled. Organisms the "
                "artifact names as contrast cases rather than exemplars were "
                "deliberately excluded."
            ),
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )
        write_validated_trait(doc, path)
        total += len(examples)
        print(f"{rel}: +{len(examples)}")
    print(f"\nadded {total} exemplar(s) across {len(PLAN)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
