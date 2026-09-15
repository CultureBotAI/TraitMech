#!/usr/bin/env python3
"""Add the arsenate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "arsenate_respiration.yaml"
SALTIKOV_PNAS = "DOI:10.1073/pnas.1834303100"
SALTIKOV_AEM = "DOI:10.1128/AEM.69.5.2800-2809.2003"
MALASARN = "DOI:10.1128/JB.01110-07"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T23:52:00Z"
REVIEW_TIMESTAMP = "2026-09-15T00:08:31Z"

RECORD = {
    "identifier": "traitmech:000195",
    "label": "arsenate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses arsenate as the "
        "terminal electron acceptor and reduces it to arsenite for energy "
        "conservation."
    ),
    "definition_source": SALTIKOV_PNAS,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "As(V) respiration",
            "synonym_type": "EXACT_SYNONYM",
            "source": SALTIKOV_PNAS,
        },
        {
            "synonym_text": "respiratory As(V) reduction",
            "synonym_type": "RELATED_SYNONYM",
            "source": SALTIKOV_PNAS,
        },
    ],
    "evidence": [
        {
            "reference": SALTIKOV_PNAS,
            "snippet": (
                "can be used by microorganisms as a terminal electron "
                "acceptor in anaerobic respiration"
            ),
            "notes": (
                "Saltikov and Newman define the organism-level scope as "
                "microbial anaerobic respiration using arsenate, As(V), as a "
                "terminal electron acceptor."
            ),
        },
        {
            "reference": SALTIKOV_AEM,
            "snippet": (
                "This gram-negative strain stoichiometrically couples the "
                "oxidation of lactate to acetate with the reduction of As(V) "
                "to arsenite"
            ),
            "notes": (
                "Saltikov et al. isolated and characterized ANA-3 as a "
                "facultatively anaerobic As(V)-respiring Shewanella strain."
            ),
        },
        {
            "reference": MALASARN,
            "snippet": (
                "the Shewanella sp. strain ANA-3 arsenate respiratory "
                "reductase (ARR), the key enzyme involved in this metabolism"
            ),
            "notes": (
                "Malasarn et al. biochemically characterize ARR as the "
                "arsenate respiratory reductase for ANA-3 arsenate respiration."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:94122",
            "taxon_label": "Shewanella sp. ANA-3",
            "note": (
                "Facultatively anaerobic Shewanella isolate characterized for "
                "arsenate-respiration studies."
            ),
            "reference": SALTIKOV_AEM,
        },
    ],
    "discussions": [
        {
            "discussion_id": "arsenate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "arsenate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains obsolete arsenate "
                "reduction and arsenate-reducing classes but no active "
                "organism-level arsenate respiration class. Potential GO, "
                "Rhea, EC, and protein-family terms for respiratory arsenate "
                "reductase are narrower than the whole-organism anaerobic "
                "respiration phenotype, and future groundings must keep ArrAB "
                "respiratory reduction separate from ArsC cytosolic "
                "detoxification."
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
            "Minted arsenate respiration as a DOI-backed anaerobic "
            "respiration TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; the local METPO "
            "snapshot has only obsolete arsenate-reduction classes and the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v72."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="TIGHTENED_CANONICAL_EXAMPLE",
        changes=(
            "Tightened the ANA-3 canonical example note to the DOI-backed "
            "isolation and facultative arsenate-respiration evidence without "
            "making a broader genetic-tractability claim."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
