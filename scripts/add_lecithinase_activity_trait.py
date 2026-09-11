#!/usr/bin/env python3
"""Add lecithinase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "lecithinase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "traitmech:000140",
    "label": "lecithinase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active lecithinases that hydrolyze lecithin or phosphatidylcholine."
    ),
    "definition_source": "DOI:10.2147/IDR.S365254",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "lecithinase production",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1128/jb.81.6.939-945.1961",
        },
        {
            "synonym_text": "lecithinase reaction",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.2147/IDR.S365254",
        },
    ],
    "evidence": [
        {
            "reference": "DOI:10.2147/IDR.S365254",
            "snippet": (
                "all tested isolates were positive for lecithinase reaction "
                "and showed opaque zone around colonies on egg yolk agar"
            ),
            "notes": (
                "Algammal et al. used an egg-yolk agar lecithinase reaction to "
                "phenotype Bacillus cereus isolates."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.81.6.939-945.1961",
            "snippet": "egg yolk were used for the demonstration of lecithinase activity",
            "notes": (
                "Esselmann and Liu surveyed lecithinase production by "
                "Gram-negative bacteria on egg-yolk agar."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "note": (
                "Bacillus cereus isolates from diseased Mugil seheli were "
                "positive for lecithinase reaction on egg-yolk agar."
            ),
            "reference": "DOI:10.2147/IDR.S365254",
        }
    ],
    "discussions": [
        {
            "discussion_id": "lecithinase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for lecithinase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004629 denotes C-type glycerophospholipase molecular "
                "function rather than the organism-level lecithinase "
                "production phenotype, so it is too scope-shifted for an "
                "equivalent TraitRecord xref."
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
            "Minted lecithinase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has no exact lecithinase activity class yet."
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
