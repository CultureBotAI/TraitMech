#!/usr/bin/env python3
"""Add the fumarate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "fumarate_respiration.yaml"
ITO = "DOI:10.1128/mBio.03238-19"
BUTLER = "DOI:10.1128/JB.00389-22"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T00:25:53Z"

RECORD = {
    "identifier": "traitmech:000196",
    "label": "fumarate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses fumarate as the "
        "terminal electron acceptor and reduces it to succinate for energy "
        "conservation."
    ),
    "definition_source": ITO,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "anaerobic respiration on fumarate",
            "synonym_type": "RELATED_SYNONYM",
            "source": BUTLER,
        },
    ],
    "evidence": [
        {
            "reference": ITO,
            "snippet": (
                "under anaerobic conditions, fumarate can serve as a "
                "terminal electron acceptor, with fumarate reductase (FRD) "
                "transferring electrons from the reduced quinone, producing "
                "succinate"
            ),
            "notes": (
                "Ito et al. summarize Bacteroides anaerobic respiration as "
                "quinone-linked transfer to fumarate through fumarate "
                "reductase, producing succinate."
            ),
        },
        {
            "reference": BUTLER,
            "snippet": (
                "The respiratory chain responsible for anaerobic respiration "
                "(NADH to fumarate) involves two NADH dehydrogenases"
            ),
            "notes": (
                "Butler et al. describe the B. fragilis anaerobic respiratory "
                "chain as an NADH-to-fumarate route."
            ),
        },
        {
            "reference": BUTLER,
            "snippet": (
                "Analysis of fumarate reductase showed that it is synthesized "
                "and active under anaerobic and nanaerobic conditions"
            ),
            "notes": (
                "The 2023 biochemical assay shows fumarate reductase remains "
                "synthesized and active in B. fragilis membranes under "
                "strictly anaerobic growth and under low-oxygen growth."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:817",
            "taxon_label": "Bacteroides fragilis",
            "note": (
                "Gut anaerobe with fumarate-linked anaerobic respiration "
                "characterized in membrane and mutant assays."
            ),
            "reference": ITO,
        },
    ],
    "discussions": [
        {
            "discussion_id": "fumarate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "fumarate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only obsolete Fumarate "
                "respiration and no active organism-level class for "
                "anaerobic respiration using fumarate as the terminal "
                "electron acceptor. Potential GO, Rhea, EC, and "
                "protein-family terms for fumarate reductase or the "
                "fumarate-to-succinate reaction are narrower than the "
                "whole-organism anaerobic respiration phenotype and should "
                "be checked separately before grounding FrdABCD-level "
                "causal nodes."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
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
            "Minted fumarate respiration as a DOI-backed anaerobic "
            "respiration TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; the local METPO "
            "snapshot has only obsolete Fumarate respiration and the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v73."
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
