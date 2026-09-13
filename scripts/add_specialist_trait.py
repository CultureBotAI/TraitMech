#!/usr/bin/env python3
"""Add the specialist niche-breadth phenotype."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "specialist.yaml"

BELL_BACTERIAL_GENERALISM = "DOI:10.1093/femsec/fiaa240"
VON_MEIJENFELDT_NICHE_BREADTH = "DOI:10.1038/s41559-023-02027-7"

CURATOR = "codex"
TIMESTAMP = "2026-09-13T17:05:41Z"

RECORD = {
    "identifier": "traitmech:000177",
    "label": "specialist",
    "definition": (
        "A phenotype describing an organism with a narrow ecological niche, "
        "restricted to a limited range of environments or resources."
    ),
    "definition_source": BELL_BACTERIAL_GENERALISM,
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": BELL_BACTERIAL_GENERALISM,
            "snippet": (
                "Organisms are often categorized as generalists or specialists, "
                "corresponding to broad or narrow niche requirements"
            ),
            "notes": (
                "Bell and Bell frame specialists as organisms with narrow "
                "niche requirements, contrasting them with bacterial "
                "generalists."
            ),
        },
        {
            "reference": VON_MEIJENFELDT_NICHE_BREADTH,
            "snippet": (
                "Generalists can survive in many environments, whereas "
                "specialists are restricted to a single environment."
            ),
            "notes": (
                "The social-niche-breadth study defines specialists as "
                "environmentally restricted prokaryotes while contrasting "
                "them with generalists."
            ),
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
            "Minted specialist as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; the local METPO snapshot has no exact specialist class "
            "and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v54."
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
