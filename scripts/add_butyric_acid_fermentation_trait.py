#!/usr/bin/env python3
"""Add butyric acid fermentation with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / (
    "butyric_acid_fermentation.yaml"
)
BUCKEL = "DOI:10.3389/fmicb.2021.703525"
LOUIS_FLINT = "DOI:10.1111/j.1574-6968.2009.01514.x"
BAROI = "DOI:10.1111/1751-7915.12304"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T01:34:38Z"

RECORD = {
    "identifier": "traitmech:000179",
    "label": "butyric acid fermentation",
    "definition": (
        "A fermentation in which anaerobic bacteria convert organic substrates "
        "to butyrate as a major reduced end product, conserving energy through "
        "substrate-level phosphorylation and reduced-ferredoxin-dependent "
        "ion-gradient generation."
    ),
    "definition_source": BUCKEL,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1002005"],
    "synonyms": [
        {
            "synonym_text": "butyrate fermentation",
            "synonym_type": "RELATED_SYNONYM",
            "source": BUCKEL,
        },
    ],
    "evidence": [
        {
            "reference": BUCKEL,
            "snippet": (
                "glutamate to ammonia, CO2, acetate, butyrate and H2 via "
                "3-methylaspartate or via 2-hydroxyglutarate by members of "
                "the Firmicutes"
            ),
            "notes": (
                "Buckel reviews Firmicutes fermentations that form acetate, "
                "butyrate, and H2 while demonstrating redox and "
                "ion-gradient-linked energy conservation in butyrate-forming "
                "anaerobic bacteria."
            ),
        },
        {
            "reference": LOUIS_FLINT,
            "snippet": (
                "butyryl-CoA : acetate CoA-transferase, rather than "
                "butyrate kinase, appears to perform the final step in "
                "butyrate synthesis"
            ),
            "notes": (
                "Louis and Flint review butyrate-producing gut bacteria and "
                "identify butyryl-CoA:acetate CoA-transferase as the common "
                "terminal butyrate-synthesis route."
            ),
        },
        {
            "reference": BAROI,
            "snippet": (
                "Butyric acid fermentation from pretreated and hydrolysed "
                "wheat straw by an adapted Clostridium tyrobutyricum strain"
            ),
            "notes": (
                "Baroi et al. directly studied butyric acid fermentation from "
                "pretreated and hydrolysed wheat straw by an adapted "
                "Clostridium tyrobutyricum strain."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1519",
            "taxon_label": "Clostridium tyrobutyricum",
            "note": (
                "Butyric-acid fermenter used by Baroi et al. for fermentative "
                "conversion of wheat-straw hydrolysate to butyric acid."
            ),
            "reference": BAROI,
        },
    ],
    "discussions": [
        {
            "discussion_id": "butyric-acid-fermentation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for butyric acid "
                "fermentation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact GO or external metabolism class was resolved for the "
                "organism-level butyrate-producing fermentation phenotype; "
                "butyrate-synthesis enzyme molecular functions and chemical "
                "production relations are shifted relative to this "
                "product-specific fermentation class."
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
            "Minted butyric acid fermentation as a DOI-backed product-specific "
            "fermentation TraitRecord after a repository-wide duplicate review "
            "covering ignored and hidden files; METPO has no exact butyric "
            "acid fermentation class yet and the placeholder is reserved in "
            "proposals/metpo_traitmech_v56."
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
