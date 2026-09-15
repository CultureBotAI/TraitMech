#!/usr/bin/env python3
"""Add the chlorate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "chlorate_respiration.yaml"
DANIELSSON = "DOI:10.1128/AEM.69.9.5585-5592.2003"
HELLBERG_LINDQVIST = "DOI:10.1128/AEM.07303-11"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T01:28:00Z"

RECORD = {
    "identifier": "traitmech:000198",
    "label": "chlorate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses chlorate as the "
        "terminal electron acceptor and reduces it to chloride for energy "
        "conservation."
    ),
    "definition_source": DANIELSSON,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "dissimilatory chlorate reduction",
            "synonym_type": "RELATED_SYNONYM",
            "source": HELLBERG_LINDQVIST,
        },
    ],
    "evidence": [
        {
            "reference": DANIELSSON,
            "snippet": (
                "chlorate ion as the sole electron acceptor for oxidation of "
                "organic matter in a previously unknown mode of respiration"
            ),
            "notes": (
                "Danielsson Thorell et al. support the organism-level "
                "respiratory use of chlorate as the electron acceptor."
            ),
        },
        {
            "reference": DANIELSSON,
            "snippet": (
                "reduction of chlorate occurs in a two-step reaction: "
                "chlorate reduction followed by chlorite decomposition"
            ),
            "notes": (
                "The Ideonella dechloratans chlorate pathway reduces "
                "chlorate and then decomposes the chlorite intermediate."
            ),
        },
        {
            "reference": HELLBERG_LINDQVIST,
            "snippet": (
                "Perchlorate-respiring bacteria (PRB) can use both "
                "perchlorate and chlorate as terminal electron acceptors, "
                "whereas chlorate-respiring bacteria (CRB) use only chlorate"
            ),
            "notes": (
                "Hellberg Lindqvist et al. separate chlorate-respiring "
                "bacteria from broader perchlorate reducers."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:36863",
            "taxon_label": "Ideonella dechloratans",
            "note": (
                "Chlorate-respiring bacterium assayed anaerobically with "
                "acetate as electron donor and sodium chlorate as electron "
                "acceptor."
            ),
            "reference": HELLBERG_LINDQVIST,
        }
    ],
    "discussions": [
        {
            "discussion_id": "chlorate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "chlorate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only the obsolete broad "
                "(Per)chlorate respiration class and no active exact "
                "organism-level chlorate respiration class. Candidate EC, "
                "Rhea, and protein-family terms for chlorate reductase or "
                "chlorite dismutase are narrower than the whole-organism "
                "anaerobic respiration phenotype."
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
            "Minted chlorate respiration as a DOI-backed anaerobic "
            "respiration TraitRecord with a related synonym after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; the local METPO snapshot has only an obsolete broad "
            "(Per)chlorate respiration class and the replacement "
            "placeholder is reserved in "
            "proposals/metpo_traitmech_v75."
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
