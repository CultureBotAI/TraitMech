#!/usr/bin/env python3
"""Add magnetotaxis with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "magnetotaxis.yaml"
MULLER = "DOI:10.1128/JB.00398-20"
LIN = "DOI:10.1038/s41396-018-0098-9"
AWAL = "DOI:10.1128/mbio.01649-23"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T16:17:24Z"

RECORD = {
    "identifier": "traitmech:000176",
    "label": "magnetotaxis",
    "definition": (
        "A behavioral physiology in which magnetosome-bearing motile cells "
        "align with geomagnetic field lines and navigate along that axis."
    ),
    "definition_source": MULLER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": MULLER,
            "snippet": (
                "Magnetotactic bacteria are aquatic or sediment-dwelling "
                "microorganisms able to take advantage of the Earth's magnetic "
                "field for directed motility"
            ),
            "notes": (
                "Muller et al. review bacterial magnetotaxis as directed "
                "motility aligned to Earth's magnetic field."
            ),
        },
        {
            "reference": LIN,
            "snippet": (
                "The origin and evolution of magnetoreception, which in diverse "
                "prokaryotes and protozoa is known as magnetotaxis and enables "
                "these microorganisms to detect Earth's magnetic field for "
                "orientation and navigation"
            ),
            "notes": (
                "Lin et al. define magnetotaxis as the magnetoreceptive "
                "orientation and navigation behavior of magnetotactic "
                "microorganisms."
            ),
        },
        {
            "reference": AWAL,
            "snippet": (
                "To efficiently navigate within the geomagnetic field, "
                "magnetotactic bacteria (MTB) align their magnetosome "
                "organelles into chains"
            ),
            "notes": (
                "Awal et al. support the mechanism-level distinction that "
                "magnetosome chain alignment underlies geomagnetic navigation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:431944",
            "taxon_label": "Magnetospirillum gryphiswaldense MSR-1",
            "note": (
                "Awal et al. used Magnetospirillum gryphiswaldense as the "
                "genetically tractable host for functional expression of "
                "magnetotaxis-associated MamK-family magnetoskeleton proteins."
            ),
            "reference": AWAL,
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
            "Minted magnetotaxis as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; METPO has only an obsolete magnetotaxis class in the local "
            "snapshot and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v53."
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
