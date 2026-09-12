#!/usr/bin/env python3
"""Add arginine dihydrolase activity with URL/DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / (
    "arginine_dihydrolase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/5/3/6.html"
RIMAUX_2011 = "DOI:10.1016/j.fm.2010.11.016"
RIMAUX_2012 = "DOI:10.1128/aem.07724-11"
RIMAUX_2013 = "DOI:10.1016/j.resmic.2012.11.004"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T09:44:56Z"

RECORD = {
    "identifier": "traitmech:000164",
    "label": "arginine dihydrolase activity",
    "definition": (
        "A physiological pathway-activity phenotype in which a cell converts "
        "L-arginine through the arginine deiminase pathway to generate ATP."
    ),
    "definition_source": RIMAUX_2012,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "arginine deiminase pathway activity",
            "synonym_type": "EXACT_SYNONYM",
            "source": RIMAUX_2013,
        },
        {
            "synonym_text": "ADI pathway activity",
            "synonym_type": "EXACT_SYNONYM",
            "source": RIMAUX_2013,
        },
        {
            "synonym_text": "arginine dihydrolase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "arginine deiminase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                "<b>Reaction:</b> <small>L</small>-arginine + "
                "H<small><sub>2</sub></small>O = <small>L</small>-"
                "citrulline + NH<small><sub>3</sub></small>"
            ),
            "notes": (
                "The NC-IUBMB EC 3.5.3.6 entry grounds the first "
                "arginine-deiminase step of the arginine deiminase pathway "
                "and records arginine dihydrolase as another name for that "
                "molecular function."
            ),
        },
        {
            "reference": RIMAUX_2011,
            "snippet": (
                "Arginine conversion through the ADI pathway, which was "
                "activated from the stationary growth phase on, resulted in "
                "the production of both citrulline and ornithine for all pH "
                "conditions tested."
            ),
            "notes": (
                "Rimaux et al. directly assayed pH-dependent L-arginine "
                "conversion through the ADI pathway in Lactobacillus sakei "
                "CTC 494."
            ),
        },
        {
            "reference": RIMAUX_2012,
            "snippet": (
                "For instance, the ability to utilize arginine through the "
                "arginine deiminase (ADI) pathway, resulting in additional "
                "ATP, represents a competitive benefit."
            ),
            "notes": (
                "Rimaux et al. frame arginine utilization through the ADI "
                "pathway as an ATP-yielding metabolic capability and show "
                "that arc gene expression is strain- and pH-dependent in "
                "Lactobacillus sakei."
            ),
        },
        {
            "reference": RIMAUX_2013,
            "snippet": (
                "Arginine conversion through the arginine deiminase (ADI) "
                "pathway is a common metabolic trait of Lactobacillus sakei "
                "which is ascribed to an arc operon and which inquisitively "
                "involves citrulline excretion and re-uptake."
            ),
            "notes": (
                "Rimaux et al. use the pathway-activity phrasing while "
                "studying the transporter coupled to citrulline and "
                "ornithine exchange during L. sakei ADI pathway activity."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1599",
            "taxon_label": "Latilactobacillus sakei",
            "note": (
                "Rimaux et al. assayed arginine conversion through the ADI "
                "pathway in Lactobacillus sakei CTC 494 and observed "
                "citrulline and ornithine production across the tested pH "
                "series."
            ),
            "reference": RIMAUX_2011,
        }
    ],
    "discussions": [
        {
            "discussion_id": "arginine-dihydrolase-activity-xref-gap",
            "prompt": (
                "Resolve exact external ontology mappings for arginine "
                "dihydrolase activity before adding TraitRecord xrefs."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016990 arginine deiminase activity and EC 3.5.3.6 "
                "denote the first-step molecular function in the arginine "
                "deiminase pathway rather than the full organism-level "
                "pathway-activity phenotype, so GO:0016990 is a close "
                "mechanism grounding for the source node and not an "
                "equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
        }
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
            "Minted arginine dihydrolase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact arginine "
            "deiminase pathway activity class yet."
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
