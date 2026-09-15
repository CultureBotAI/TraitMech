#!/usr/bin/env python3
"""Add the iodate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "iodate_respiration.yaml"
AMACHI = "DOI:10.1128/AEM.00241-07"
REYES_UMANA_2021 = "DOI:10.1038/s41396-021-01034-5"
REYES_UMANA_2022 = "DOI:10.3389/fmicb.2021.804181"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T03:53:45Z"

RECORD = {
    "identifier": "traitmech:000203",
    "label": "iodate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses iodate as the "
        "terminal electron acceptor for energy conservation."
    ),
    "definition_source": AMACHI,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "dissimilatory iodate reduction",
            "synonym_type": "EXACT_SYNONYM",
        },
    ],
    "evidence": [
        {
            "reference": AMACHI,
            "snippet": (
                "SCT was capable of anaerobic growth with 3 mM iodate as the "
                "sole electron acceptor"
            ),
            "notes": (
                "Amachi et al. isolated Pseudomonas sp. strain SCT from "
                "marine sediment slurry and showed anaerobic growth with "
                "iodate as sole electron acceptor."
            ),
        },
        {
            "reference": AMACHI,
            "snippet": "SCT is a dissimilatory iodate-reducing bacterium",
            "notes": (
                "Amachi et al. support the dissimilatory iodate reduction "
                "synonym and organism-level phenotype scope."
            ),
        },
        {
            "reference": REYES_UMANA_2021,
            "snippet": (
                "dissimilatory IO3\u2212 reduction to iodide (I\u2212) by a novel "
                "estuarine bacterium, Denitromonas sp. IR-12"
            ),
            "notes": (
                "Reyes-Umana et al. show that iodate respiration recurs in an "
                "estuarine Denitromonas isolate."
            ),
        },
        {
            "reference": REYES_UMANA_2022,
            "snippet": (
                "A. toluclasticum sp. TC-10 couples acetate oxidation to "
                "iodate reduction with a concomitant increase in the OD600."
            ),
            "notes": (
                "Reyes-Umana et al. extend the dissimilatory iodate-reducing "
                "phenotype to the freshwater isolate Aromatoleum "
                "toluclasticum sp. TC-10."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:412955",
            "taxon_label": "Pseudomonas sp. SCT",
            "note": (
                "Amachi et al. isolated Pseudomonas sp. strain SCT from "
                "marine sediment slurry and showed anaerobic growth with "
                "iodate as the sole electron acceptor."
            ),
            "reference": AMACHI,
        },
    ],
    "discussions": [
        {
            "discussion_id": "iodate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "iodate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Candidate Idr, DmsAB, EC, Rhea, and protein-family terms "
                "describe narrower iodate reductase activities, reactions, "
                "or enzymes rather than the whole-organism anaerobic "
                "respiration phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted iodate respiration as a DOI-backed anaerobic respiration "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has no exact "
            "iodate respiration class and the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v80."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
