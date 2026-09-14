#!/usr/bin/env python3
"""Add the anaerobic ammonium oxidation metabolism trait."""
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
    "anaerobic_ammonium_oxidation.yaml"
)
STROUS_NATURE = "DOI:10.1038/22749"
STROUS_AEM = "DOI:10.1128/AEM.65.7.3248-3250.1999"
KARTAL = "DOI:10.1038/nature10453"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T20:06:42Z"

RECORD = {
    "identifier": "traitmech:000188",
    "label": "anaerobic ammonium oxidation",
    "definition": (
        "An anaerobic nitrogen metabolism in which ammonium is oxidized with "
        "nitrite as the electron acceptor to form dinitrogen."
    ),
    "definition_source": STROUS_NATURE,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000121"],
    "synonyms": [
        {
            "synonym_text": "anammox",
            "synonym_type": "EXACT_SYNONYM",
            "source": STROUS_NATURE,
        },
        {
            "synonym_text": "anaerobic ammonia oxidation",
            "synonym_type": "RELATED_SYNONYM",
            "source": STROUS_NATURE,
        },
    ],
    "evidence": [
        {
            "reference": STROUS_NATURE,
            "snippet": (
                "This new process combines ammonia and nitrite directly into "
                "dinitrogen gas"
            ),
            "notes": (
                "Strous et al. identified the anaerobic ammonia oxidation "
                "process and linked ammonia plus nitrite conversion to "
                "dinitrogen formation."
            ),
        },
        {
            "reference": STROUS_AEM,
            "snippet": (
                "The affinity constants for the substrates ammonium and "
                "nitrite were each less than 0.1 mg of nitrogen per liter."
            ),
            "notes": (
                "Strous et al. measured ammonium and nitrite as high-affinity "
                "anammox substrates."
            ),
        },
        {
            "reference": KARTAL,
            "snippet": (
                "anammox converts ammonia and nitrite into dinitrogen (N2) gas"
            ),
            "notes": (
                "Kartal et al. review the pathway scope and support anammox "
                "as the established exact synonym."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "anaerobic-ammonium-oxidation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for anaerobic "
                "ammonium oxidation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only METPO:1000812 "
                "obsolete Anaerobic ammonium oxidation. Candidate GO "
                "classes should be checked against the primary Gene "
                "Ontology release before adding an exact xref because "
                "component ammonium- or nitrite-oxidation processes are "
                "narrower than the whole anammox metabolism."
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
            "Minted anaerobic ammonium oxidation as a DOI-backed nitrogen "
            "respiration TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; the local METPO "
            "snapshot has only obsolete anammox classes and the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v65."
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
