#!/usr/bin/env python3
"""Add the cyanobacterial akinete morphology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "akinete.yaml"
GARG = "DOI:10.1159/000517443"
RIOS_HENRIQUEZ = "DOI:10.3389/fmicb.2025.1677844"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T15:47:55Z"

RECORD = {
    "identifier": "traitmech:000185",
    "label": "akinete",
    "definition": (
        "A morphology trait in which a filamentous cyanobacterium "
        "differentiates enlarged, thick-coated, spore-like dormant cells "
        "called akinetes that can germinate into vegetative cells."
    ),
    "definition_source": GARG,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": GARG,
            "snippet": (
                "Some cyanobacteria of the order Nostocales can form "
                "akinetes, spore-like dormant cells resistant to various "
                "unfavorable environmental fluctuations."
            ),
            "notes": (
                "Garg and Maldener support akinetes as spore-like dormant "
                "cells formed by Nostocales cyanobacteria under unfavorable "
                "environmental conditions."
            ),
        },
        {
            "reference": GARG,
            "snippet": (
                "Akinetes are enveloped in a thick protective coat containing "
                "a multilayered structure and are able to germinate into new "
                "vegetative cells under suitable growth conditions."
            ),
            "notes": (
                "The source supports the thick protective coat and "
                "vegetative-cell germination clauses in the local definition."
            ),
        },
        {
            "reference": RIOS_HENRIQUEZ,
            "snippet": (
                "Raphidiopsis raciborskii (Nostocales) is a successful "
                "invader of temperate ecosystems originating from the "
                "tropics that forms akinetes in their new habitats to "
                "overcome unfavorable winter conditions."
            ),
            "notes": (
                "Rios-Henriquez and Weithoff provide a second Nostocales "
                "cyanobacterium study supporting akinete formation as an "
                "unfavorable-condition dormancy trait."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:240292",
            "taxon_label": "Trichormus variabilis ATCC 29413",
            "note": (
                "Model Nostocales strain still cited in the akinete "
                "literature as Anabaena variabilis ATCC 29413; the NCBI "
                "Taxonomy record lists that name as an equivalent name."
            ),
            "reference": GARG,
        }
    ],
    "discussions": [
        {
            "discussion_id": "akinete-exact-xref-gap",
            "prompt": (
                "Resolve exact external ontology xrefs for the cyanobacterial "
                "akinete morphology trait."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only deprecated "
                "akinete classes, including METPO:1000012 obsolete akinete; "
                "no active METPO, GO, or OBO class was accepted as an exact "
                "equivalent for this cyanobacterial dormant-cell trait."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
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
            "Minted akinete as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; live METPO has no active exact akinete class and the "
            "placeholder is reserved in proposals/metpo_traitmech_v62."
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
