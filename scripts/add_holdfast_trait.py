#!/usr/bin/env python3
"""Add holdfast with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "holdfast.yaml"
HERSHEY = "DOI:10.1128/jb.00276-19"
CHEPKWONY = "DOI:10.1128/jb.00273-22"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T06:26:17Z"

RECORD = {
    "identifier": "traitmech:000184",
    "label": "holdfast",
    "definition": (
        "A morphology trait in which a bacterial cell produces a localized "
        "polar adhesive matrix called a holdfast that mediates permanent "
        "attachment to surfaces."
    ),
    "definition_source": HERSHEY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "holdfast adhesin",
            "synonym_type": "RELATED_SYNONYM",
            "source": HERSHEY,
        }
    ],
    "evidence": [
        {
            "reference": HERSHEY,
            "snippet": (
                "Caulobacter crescentus synthesizes a polysaccharide-based "
                "adhesin known as the holdfast at one of its cell poles, "
                "which enables tight attachment to exogenous surfaces."
            ),
            "notes": (
                "Hershey et al. support holdfast as a Caulobacter polar "
                "polysaccharide-based adhesin mediating tight surface "
                "attachment."
            ),
        },
        {
            "reference": HERSHEY,
            "snippet": (
                "Glucose, 3-O-methylglucose, mannose, N-acetylglucosamine, "
                "and xylose were detected in our extracts."
            ),
            "notes": (
                "The compositional analysis supports the holdfast matrix as "
                "a bacterial polysaccharide-rich adhesive."
            ),
        },
        {
            "reference": CHEPKWONY,
            "snippet": (
                "Species of the Caulobacterales produce a specialized polar "
                "adhesin, holdfast, which is required for permanent "
                "attachment to surfaces."
            ),
            "notes": (
                "Chepkwony et al. support holdfast as a specialized polar "
                "Caulobacterales adhesin required for permanent attachment."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:155892",
            "taxon_label": "Caulobacter vibrioides",
            "note": (
                "Model freshwater Caulobacter species, long called "
                "Caulobacter crescentus, that produces a polar holdfast."
            ),
            "reference": HERSHEY,
        }
    ],
    "discussions": [
        {
            "discussion_id": "holdfast-exact-xref-gap",
            "prompt": (
                "Resolve exact external ontology xrefs for the bacterial "
                "holdfast morphology trait."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only the deprecated "
                "METPO:1000158 obsolete holdfast class; no active METPO, GO, "
                "or OBO class was accepted as an exact equivalent for this "
                "bacterial adhesive-matrix trait."
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
            "Minted holdfast as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; live METPO has no active exact holdfast class and the "
            "placeholder is reserved in proposals/metpo_traitmech_v61."
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
