#!/usr/bin/env python3
"""Add lipase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "lipase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "traitmech:000139",
    "label": "lipase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active lipases that hydrolyze triglycerides at lipid-water interfaces."
    ),
    "definition_source": "DOI:10.22207/JPAM.16.4.27",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "lipase production",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.22207/JPAM.16.4.27",
        },
        {
            "synonym_text": "lipolytic activity",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1016/j.mex.2018.01.004",
        },
    ],
    "evidence": [
        {
            "reference": "DOI:10.22207/JPAM.16.4.27",
            "snippet": (
                "Lipase-producing bacteria were isolated using tributyrin agar "
                "as a selective medium"
            ),
            "notes": (
                "Savalia and Dungrechiya used tributyrin agar to isolate "
                "lipase-producing bacteria from waste samples."
            ),
        },
        {
            "reference": "DOI:10.1016/j.mex.2018.01.004",
            "snippet": (
                "to identify lipase producers. The addition of calcium and "
                "magnesium ions can provide an easier screening procedure for "
                "selection of lipolytic bacterial strains"
            ),
            "notes": (
                "Carrazco-Palafox et al. optimized modified tributyrin agar as "
                "a microbial lipolytic-activity screen."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1408",
            "taxon_label": "Bacillus pumilus",
            "note": (
                "Bacillus pumilus S113 was isolated as the strongest lipase "
                "producer in a tributyrin-agar screen."
            ),
            "reference": "DOI:10.22207/JPAM.16.4.27",
        }
    ],
    "discussions": [
        {
            "discussion_id": "lipase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for lipase activity "
                "before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016298 denotes the lipase molecular function rather than "
                "the organism-level lipase production phenotype, so it is too "
                "scope-shifted for an equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-11",
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
            "Minted lipase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has no exact lipase activity class yet."
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
