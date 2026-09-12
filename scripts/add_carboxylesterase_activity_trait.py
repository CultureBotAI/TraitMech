#!/usr/bin/env python3
"""Add carboxylesterase activity with URL/DOI-backed evidence."""
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
    "carboxylesterase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T03:42:43Z"

RECORD = {
    "identifier": "traitmech:000156",
    "label": "carboxylesterase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active carboxylesterase enzymes that hydrolyze carboxylic esters to "
        "alcohols and carboxylates."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC3/1/1/1.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "carboxylic-ester hydrolase activity",
            "synonym_type": "EXACT_SYNONYM",
            "source": "https://iubmb.qmul.ac.uk/enzyme/EC3/1/1/1.html",
        }
    ],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC3/1/1/1.html",
            "snippet": (
                "Reaction: A carboxylic ester + H_{2}O = an alcohol + "
                "a carboxylate"
            ),
            "notes": (
                "The NC-IUBMB EC 3.1.1.1 entry defines carboxylesterase "
                "by its accepted reaction, grounding the ester-hydrolase "
                "activity named by the organism-level carboxylesterase "
                "phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/JCM.43.8.3713-3717.2005",
            "snippet": (
                "Alkaline phosphatase, esterase (C4), esterase lipase "
                "(C8), leucine arylamidase, acid phosphatase, and "
                "naphthol-AS-BI-phosphohydrolase were clearly positive"
            ),
            "notes": (
                "Otsuka et al. detected clear esterase (C4) and esterase "
                "lipase (C8) API ZYM reactions in the five Corynebacterium "
                "resistens isolates they characterized, supporting this "
                "as a directly assayed bacterial carboxylesterase "
                "activity phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:258224",
            "taxon_label": "Corynebacterium resistens",
            "note": (
                "Otsuka et al. detected clear esterase (C4) and esterase "
                "lipase (C8) API ZYM reactions in Corynebacterium "
                "resistens isolates."
            ),
            "reference": "DOI:10.1128/JCM.43.8.3713-3717.2005",
        }
    ],
    "discussions": [
        {
            "discussion_id": "carboxylesterase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "carboxylesterase activity before adding a TraitRecord "
                "xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0106435 denotes carboxylesterase molecular function "
                "rather than the organism-level carboxylesterase "
                "production phenotype, so it is appropriate as a "
                "causal-node grounding rather than an equivalent "
                "TraitRecord xref."
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
            "Minted carboxylesterase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact carboxylesterase "
            "activity class yet."
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
