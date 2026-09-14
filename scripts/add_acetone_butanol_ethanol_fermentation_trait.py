#!/usr/bin/env python3
"""Add acetone-butanol-ethanol fermentation with DOI-backed evidence."""
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
    "acetone_butanol_ethanol_fermentation.yaml"
)
LIAO = "DOI:10.1073/pnas.1423143112"
LEE = "DOI:10.1002/bit.22003"
JONES_WOODS = "DOI:10.1128/mr.50.4.484-524.1986"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T02:40:39Z"

RECORD = {
    "identifier": "traitmech:000180",
    "label": "acetone-butanol-ethanol fermentation",
    "definition": (
        "A fermentation in which solventogenic bacteria convert organic carbon "
        "sources to organic acids and then reassimilate those acids to produce "
        "acetone, butanol, and ethanol solvents."
    ),
    "definition_source": LIAO,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1002005"],
    "synonyms": [
        {
            "synonym_text": "ABE fermentation",
            "synonym_type": "EXACT_SYNONYM",
            "source": LIAO,
        },
        {
            "synonym_text": "acetone-butanol fermentation",
            "synonym_type": "RELATED_SYNONYM",
            "source": JONES_WOODS,
        },
    ],
    "evidence": [
        {
            "reference": LIAO,
            "snippet": (
                "One canonical example of such processes is "
                "acetone-butanol-ethanol (ABE) fermentation by Clostridium "
                "acetobutylicum, during which cells convert carbon sources to "
                "organic acids that are later reassimilated to produce "
                "solvents as a strategy for cellular survival."
            ),
            "notes": (
                "Liao et al. use the exact acetone-butanol-ethanol (ABE) "
                "fermentation name and describe the acidogenic-to-solventogenic "
                "conversion of carbon sources into solvent end products."
            ),
        },
        {
            "reference": LEE,
            "snippet": (
                "Biological production of butanol (with acetone and ethanol) "
                "was one of the largest industrial fermentation processes early "
                "in the 20th century."
            ),
            "notes": (
                "Lee et al. independently review fermentative butanol "
                "production with acetone and ethanol by Clostridia."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:272562",
            "taxon_label": "Clostridium acetobutylicum ATCC 824",
            "note": (
                "Wild-type ATCC 824 strain whose ABE fermentations were "
                "experimentally reproduced by Liao et al.'s integrated model."
            ),
            "reference": LIAO,
        },
    ],
    "discussions": [
        {
            "discussion_id": "acetone-butanol-ethanol-fermentation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "acetone-butanol-ethanol fermentation before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact GO or external metabolism class was resolved for the "
                "organism-level ABE fermentation phenotype; broader "
                "fermentation classes and individual solvent-production "
                "reactions are shifted relative to this product-specific "
                "fermentation class."
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
            "Minted acetone-butanol-ethanol fermentation as a DOI-backed "
            "solventogenic fermentation TraitRecord after a repository-wide "
            "duplicate review covering ignored and hidden files; METPO has no "
            "exact acetone-butanol-ethanol fermentation class yet and the "
            "placeholder is reserved in proposals/metpo_traitmech_v57."
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
