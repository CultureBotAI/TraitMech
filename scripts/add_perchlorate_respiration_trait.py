#!/usr/bin/env python3
"""Add the perchlorate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "perchlorate_respiration.yaml"
COATES = "DOI:10.1038/nrmicro926"
MELNYK_BMC = "DOI:10.1186/s12864-015-2011-5"
MELNYK_AEM = "DOI:10.1128/AEM.05758-11"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T00:56:27Z"

RECORD = {
    "identifier": "traitmech:000197",
    "label": "perchlorate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses perchlorate as "
        "the terminal electron acceptor and reduces it to chloride for "
        "energy conservation."
    ),
    "definition_source": COATES,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "dissimilatory perchlorate reduction",
            "synonym_type": "RELATED_SYNONYM",
            "source": MELNYK_BMC,
        },
    ],
    "evidence": [
        {
            "reference": MELNYK_BMC,
            "snippet": (
                "reduction to chlorite (ClO2-) in the bacterial periplasm by "
                "perchlorate reductase, and the dismutation of chlorite to "
                "chloride and molecular oxygen"
            ),
            "notes": (
                "Melnyk et al. describe the canonical perchlorate-to-chloride "
                "respiratory pathway through perchlorate reductase and "
                "chlorite dismutase."
            ),
        },
        {
            "reference": MELNYK_AEM,
            "snippet": (
                "perchlorate reductase and chlorite dismutase, which are "
                "encoded by the pcrABCD and cld genes"
            ),
            "notes": (
                "Melnyk et al. support the PcrABCD and Cld gene modules as "
                "the two pathway-specific enzyme systems for perchlorate "
                "reduction to chloride."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "perchlorate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "perchlorate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only obsolete "
                "(Per)chlorate respiration, Perchlorate respiration, and "
                "Perchlorate-reducing classes. Candidate GO, EC, and "
                "protein-family terms for perchlorate reductase and chlorite "
                "dismutase are narrower than the whole-organism anaerobic "
                "respiration phenotype and should be checked separately "
                "before grounding PcrABCD- or Cld-level causal nodes."
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
            "Minted perchlorate respiration as a DOI-backed anaerobic "
            "respiration TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; the local METPO "
            "snapshot has only obsolete perchlorate respiration classes and "
            "the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v74."
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
