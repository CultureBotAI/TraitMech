#!/usr/bin/env python3
"""Add the selenate respiration metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "selenate_respiration.yaml"
OREMLAND = "DOI:10.1128/aem.60.8.3011-3019.1994"
NARASINGARAO_2006 = "DOI:10.1016/j.syapm.2005.12.011"
NARASINGARAO_2007 = "DOI:10.1128/AEM.02737-06"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T03:22:39Z"

RECORD = {
    "identifier": "traitmech:000202",
    "label": "selenate respiration",
    "definition": (
        "An anaerobic respiration in which an organism uses selenate as the "
        "terminal electron acceptor for energy conservation."
    ),
    "definition_source": OREMLAND,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000802"],
    "synonyms": [
        {
            "synonym_text": "dissimilatory selenate reduction",
            "synonym_type": "EXACT_SYNONYM",
        },
    ],
    "evidence": [
        {
            "reference": OREMLAND,
            "snippet": (
                "A gram-negative, strictly anaerobic, motile vibrio was "
                "isolated from a selenate-respiring enrichment culture"
            ),
            "notes": (
                "Oremland et al. isolated strain SES-3 from a "
                "selenate-respiring enrichment culture and showed anaerobic "
                "growth coupled to selenate reduction."
            ),
        },
        {
            "reference": NARASINGARAO_2007,
            "snippet": "use selenate as a terminal electron acceptor",
            "notes": (
                "Narasingarao and Haggblom define the phenotype as use of "
                "selenate as a terminal electron acceptor in dissimilatory "
                "selenate reduction."
            ),
        },
        {
            "reference": NARASINGARAO_2007,
            "snippet": (
                "four novel anaerobic dissimilatory selenate-respiring "
                "bacteria"
            ),
            "notes": (
                "Narasingarao and Haggblom support selenate respiration as a "
                "repeatedly observed microbial trait across aquatic-sediment "
                "isolates rather than a single strain-specific anomaly."
            ),
        },
        {
            "reference": NARASINGARAO_2006,
            "snippet": (
                "Here we characterize a novel selenate-respiring bacterium, "
                "strain AK4OH1, isolated from an estuarine sediment "
                "enrichment culture"
            ),
            "notes": (
                "Narasingarao and Haggblom described Sedimenticola "
                "selenatireducens AK4OH1 as an anaerobic selenate-respiring "
                "bacterium isolated from estuarine sediment."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1111735",
            "taxon_label": "Sedimenticola selenatireducens DSM 17993",
            "note": (
                "Narasingarao and Haggblom isolated and described "
                "Sedimenticola selenatireducens strain AK4OH1 as an "
                "anaerobic selenate-respiring bacterium."
            ),
            "reference": NARASINGARAO_2006,
        },
    ],
    "discussions": [
        {
            "discussion_id": "selenate-respiration-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "selenate respiration before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Candidate EC, Rhea, and protein-family terms for selenate "
                "reductase describe narrower molecular functions, reactions, "
                "or enzymes rather than the whole-organism anaerobic "
                "respiration phenotype."
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
            "Minted selenate respiration as a DOI-backed anaerobic respiration "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has no exact "
            "selenate respiration class and the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v79."
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
