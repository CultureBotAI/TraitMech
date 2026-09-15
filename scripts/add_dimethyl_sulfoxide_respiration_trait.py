#!/usr/bin/env python3
"""Add the dimethyl sulfoxide respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "dimethyl_sulfoxide_respiration.yaml"
GRALNICK = "DOI:10.1073/pnas.0505959103"
ROSENBAUM = "DOI:10.1111/1462-2920.15971"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T02:53:12Z"

RECORD = {
    "identifier": "traitmech:000201",
    "label": "dimethyl sulfoxide respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses dimethyl "
        "sulfoxide as the terminal electron acceptor for energy conservation."
    ),
    "definition_source": GRALNICK,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "DMSO respiration",
            "synonym_type": "EXACT_SYNONYM",
        },
    ],
    "evidence": [
        {
            "reference": GRALNICK,
            "snippet": (
                "one (SO1427-SO1432) is required for anaerobic respiration "
                "of DMSO"
            ),
            "notes": (
                "Gralnick et al. identify the SO1427-SO1432 gene cluster "
                "required for Shewanella oneidensis MR-1 anaerobic "
                "respiration of dimethyl sulfoxide."
            ),
        },
        {
            "reference": GRALNICK,
            "snippet": "DMSO respiration is an extracellular respiratory process",
            "notes": (
                "Gralnick et al. support DMSO respiration as a bona fide "
                "respiratory process rather than an isolated reductase assay."
            ),
        },
        {
            "reference": ROSENBAUM,
            "snippet": (
                "M. thermoacetica can also use dimethyl sulfoxide as "
                "terminal electron acceptor"
            ),
            "notes": (
                "Rosenbaum et al. support organism-level use of dimethyl "
                "sulfoxide as an anaerobic terminal electron acceptor."
            ),
        },
        {
            "reference": ROSENBAUM,
            "snippet": "Membranes showed a DMSO reductase activity",
            "notes": (
                "Rosenbaum et al. biochemically support an induced DMSO "
                "reductase activity in Moorella thermoacetica membranes."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:211586",
            "taxon_label": "Shewanella oneidensis MR-1",
            "note": (
                "Gralnick et al. showed that the SO1427-SO1432 gene cluster "
                "is required for anaerobic DMSO respiration in Shewanella "
                "oneidensis MR-1."
            ),
            "reference": GRALNICK,
        },
    ],
    "discussions": [
        {
            "discussion_id": "dimethyl-sulfoxide-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "dimethyl sulfoxide respiration before adding a TraitRecord "
                "xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot has only an obsolete dimethyl "
                "sulfoxide respiration class. Candidate EC, Rhea, KEGG, and "
                "protein-family terms for DMSO reductase or DmsABC are "
                "narrower than the whole-organism anaerobic respiration "
                "phenotype."
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
            "Minted dimethyl sulfoxide respiration as a DOI-backed "
            "anaerobic respiration TraitRecord after a repository-wide "
            "duplicate review covering ignored and hidden files; the local "
            "METPO snapshot has only obsolete sulfoxide respiration classes "
            "and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v78."
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
