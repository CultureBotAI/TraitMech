#!/usr/bin/env python3
"""Add seeded METPO Voges-Proskauer-test-positive with stable evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "voges_proskauer_test_positive.yaml"

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)
HANSEN = "DOI:10.1128/JCM.42.8.3665-3669.2004"

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T19:49:19Z"
TIMESTAMP = "2026-09-12T19:50:21Z"

SEED_RECORD = {
    "identifier": "METPO:1005017",
    "label": "Voges-Proskauer test positive",
    "definition": (
        "A phenotype in which an organism tests positive in the "
        "Voges-Proskauer test, indicating acetoin production."
    ),
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1005016"],
    "synonyms": [
        {
            "synonym_text": "voges-proskauer test",
            "synonym_type": "RELATED_SYNONYM",
            "source": "metpo.owl",
        }
    ],
    "curation_history": [
        {
            "timestamp": SEED_TIMESTAMP,
            "curator": "seed_from_metpo",
            "action": "SEEDED_FROM_METPO",
            "changes": "imported from data/raw/metpo.owl (CLASS)",
        }
    ],
}

UPDATES = {
    "parent_traits": ["METPO:1000059"],
    "definition_source": ASM_MRVP,
    "evidence": [
        {
            "reference": ASM_MRVP,
            "snippet": (
                "In the presence of KOH the intermediate acetoin is oxidized "
                "to diacetyl, a reaction which is catalyzed by a-naphthol "
                "(2). Diacetyl reacts with the guanidine group associated "
                "with molecules contributed by peptone in the medium, to "
                "form a pinkish-red-colored product (Fig. 2A)."
            ),
            "notes": (
                "The ASM protocol PDF explains that the Voges-Proskauer "
                "reaction detects acetoin through Barritt chemistry that "
                "forms a pinkish-red product."
            ),
        },
        {
            "reference": HANSEN,
            "snippet": (
                "In the ASM Manual of Clinical Microbiology, only 6 of the "
                "18 biochemical tests used in the present investigation are "
                "listed for Klebsiella species: indole, MR, VP, LDC, ODC, "
                "and malonate"
            ),
            "notes": (
                "Hansen et al. evaluated Voges-Proskauer as a conventional "
                "Klebsiella biochemical test listed in the ASM Manual of "
                "Clinical Microbiology."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:571",
            "taxon_label": "Klebsiella oxytoca",
            "note": (
                "Hansen et al. Table 2 reported 100.0% "
                "Voges-Proskauer-positive results for K. oxytoca across "
                "the CPHL, NRL, and SSI reference laboratories."
            ),
            "reference": HANSEN,
        }
    ],
    "discussions": [
        {
            "discussion_id": "voges-proskauer-test-positive-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for positive Voges-Proskauer-test "
                "phenotypes before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005016 is the seeded superclass of METPO:1005017, "
                "but METPO:1005016 defines an assay rather than a broader "
                "microbial trait class, so this record is temporarily "
                "parented directly to METPO:1000059 phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
        }
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO Voges-Proskauer-test-positive phenotype with "
            "stable-URL and DOI-backed acetoin-production evidence after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = build_record()
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
