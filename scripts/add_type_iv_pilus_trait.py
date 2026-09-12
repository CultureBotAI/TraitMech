#!/usr/bin/env python3
"""Add type IV pilus with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "type_iv_pilus.yaml"
ELLISON = "DOI:10.1093/femsre/fuab053"
PIEPENBRINK = "DOI:10.1042/BST20160221"
ROBERGE = "DOI:10.1128/jb.00359-24"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T15:35:50Z"

RECORD = {
    "identifier": "traitmech:000175",
    "label": "type IV pilus",
    "definition": (
        "A morphology trait in which a cell produces dynamic extracellular "
        "type-IV-pilin filaments that extend from the cell surface."
    ),
    "definition_source": ELLISON,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "type IV pili",
            "synonym_type": "EXACT_SYNONYM",
            "source": ELLISON,
        },
        {
            "synonym_text": "T4P",
            "synonym_type": "EXACT_SYNONYM",
            "source": ELLISON,
        },
    ],
    "xrefs": ["GO:0044096"],
    "evidence": [
        {
            "reference": ELLISON,
            "snippet": "Bacteria and archaea rely on appendages called type IV pili (T4P)",
            "notes": (
                "Ellison et al. review type IV pili as prokaryotic "
                "appendages that participate in diverse surface-associated "
                "behaviors."
            ),
        },
        {
            "reference": ELLISON,
            "snippet": "T4P are broadly distributed fibers that dynamically extend and retract",
            "notes": (
                "The review supports the record definition's dynamic "
                "extension and retraction qualifier."
            ),
        },
        {
            "reference": PIEPENBRINK,
            "snippet": "Type IV pili are hair-like bacterial surface appendages",
            "notes": (
                "Piepenbrink and Sundberg support type IV pili as bacterial "
                "cell-surface appendages built from pilin proteins."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:208964",
            "taxon_label": "Pseudomonas aeruginosa PAO1",
            "note": (
                "The PAO1 type IV pilus is a canonical model for PilB/PilT-"
                "driven pilus extension and retraction."
            ),
            "reference": ROBERGE,
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
            "Minted type IV pilus as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; METPO has no exact live type IV pilus class yet and "
            "the placeholder is reserved in proposals/metpo_traitmech_v52."
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
