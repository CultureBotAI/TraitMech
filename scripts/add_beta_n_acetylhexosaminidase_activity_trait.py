#!/usr/bin/env python3
"""Add beta-N-acetylhexosaminidase activity with URL/DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / (
    "beta_n_acetylhexosaminidase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/52.html"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T04:12:07Z"

RECORD = {
    "identifier": "traitmech:000157",
    "label": "beta-N-acetylhexosaminidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active beta-N-acetylhexosaminidase enzymes that hydrolyze terminal, "
        "non-reducing N-acetyl-D-hexosamine residues in "
        "N-acetyl-beta-D-hexosaminides."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": (
                "beta-N-acetyl-D-hexosaminide "
                "N-acetylhexosaminohydrolase activity"
            ),
            "synonym_type": "EXACT_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "N-acetylhexosaminidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1021/jf020965x",
        },
        {
            "synonym_text": "beta-N-acetylglucosaminidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "N-acetyl-beta-glucosaminidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "TraitMech#453",
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                "Reaction: Hydrolysis of terminal non-reducing "
                "N-acetyl-D-hexosamine residues in "
                "N-acetyl-β-D-hexosaminides"
            ),
            "notes": (
                "The NC-IUBMB EC 3.2.1.52 entry defines "
                "beta-N-acetylhexosaminidase by its accepted reaction, "
                "grounding the glycosidase activity named by the "
                "organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1021/jf020965x",
            "snippet": (
                "Serratia marcescens YS-1, a chitin-degrading "
                "microorganism, produced mainly N-acetylhexosaminidase"
            ),
            "notes": (
                "Kurakake et al. reported production of "
                "N-acetylhexosaminidase by Serratia marcescens YS-1, "
                "supporting this as a bacterial beta-N-acetylhexosaminidase "
                "activity phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:615",
            "taxon_label": "Serratia marcescens",
            "note": (
                "Kurakake et al. reported Serratia marcescens YS-1 as mainly "
                "producing N-acetylhexosaminidase."
            ),
            "reference": "DOI:10.1021/jf020965x",
        }
    ],
    "discussions": [
        {
            "discussion_id": "beta-n-acetylhexosaminidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "beta-N-acetylhexosaminidase activity before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004563 denotes beta-N-acetylhexosaminidase molecular "
                "function rather than the organism-level "
                "beta-N-acetylhexosaminidase production phenotype, so it is "
                "appropriate as a causal-node grounding rather than an "
                "equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
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
            "Minted beta-N-acetylhexosaminidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact "
            "beta-N-acetylhexosaminidase activity class yet."
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
