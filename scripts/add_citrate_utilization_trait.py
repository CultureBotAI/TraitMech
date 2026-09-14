#!/usr/bin/env python3
"""Add citrate utilization with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "citrate_utilization.yaml"
CHEN = "DOI:10.1186/1471-2180-9-168"
MEYER = "DOI:10.1128/JB.183.18.5248-5256.2001"
ASM_CITRATE = (
    "https://asm.org/ASM/media/Protocol-Images/Citrate-Test-Protocol.pdf?ext=.pdf"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-14T04:09:24Z"

RECORD = {
    "identifier": "traitmech:000182",
    "label": "citrate utilization",
    "definition": (
        "A metabolism in which a microorganism uses citrate as a sole carbon "
        "and energy source."
    ),
    "definition_source": MEYER,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000060"],
    "evidence": [
        {
            "reference": MEYER,
            "snippet": (
                "Klebsiella pneumoniae is able to grow anaerobically with "
                "citrate as a sole carbon and energy source by a fermentative "
                "pathway"
            ),
            "notes": (
                "Meyer et al. provide direct Klebsiella pneumoniae evidence "
                "for growth with citrate as sole carbon and energy source."
            ),
        },
        {
            "reference": CHEN,
            "snippet": (
                "Not all, but nearly half of the K. pneumoniae clinical "
                "isolates carry the genes responsible for anaerobic growth "
                "on citrate."
            ),
            "notes": (
                "Chen et al. found citrate-growth gene clusters in clinical "
                "K. pneumoniae isolates, supporting K. pneumoniae as a "
                "canonical citrate utilizer with strain-level variation."
            ),
        },
        {
            "reference": ASM_CITRATE,
            "snippet": (
                "The citrate test screens a bacterial isolate for the ability "
                "to utilize citrate as its carbon and energy source"
            ),
            "notes": (
                "The ASM citrate-test protocol standardizes citrate "
                "utilization as the ability to use citrate for carbon and "
                "energy in a defined assay medium."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:573",
            "taxon_label": "Klebsiella pneumoniae",
            "note": (
                "Chen et al. and Meyer et al. both studied citrate-positive "
                "K. pneumoniae strains."
            ),
            "reference": CHEN,
        },
    ],
    "discussions": [
        {
            "discussion_id": "citrate-utilization-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for citrate "
                "utilization before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact GO or external metabolism class was resolved for "
                "the organism-level citrate-utilization phenotype; citrate "
                "metabolic process terms, citrate lyase or transporter "
                "molecular functions, carbon-source or energy-source "
                "predicates, and citrate assay terms are shifted relative to "
                "this precomposed microbial citrate-use class."
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
            "Minted citrate utilization as a DOI- and stable-URL-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact citrate "
            "utilization class yet and the placeholder is reserved in "
            "proposals/metpo_traitmech_v59."
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
