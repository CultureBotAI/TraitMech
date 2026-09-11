#!/usr/bin/env python3
"""Add alpha-glucosidase activity with DOI-backed evidence."""
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
    "alpha_glucosidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T17:22:13Z"

RECORD = {
    "identifier": "traitmech:000145",
    "label": "alpha-glucosidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active alpha-glucosidase enzymes that hydrolyze alpha-glucosidic "
        "bonds in alpha-D-glucosides."
    ),
    "definition_source": "DOI:10.1371/journal.pone.0322500",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1371/journal.pone.0322500",
            "snippet": (
                "Enzyme activities of acid- and alkaline-phosphatases, "
                "esterase, esterase lipase, leucine arylamidase, trypsin, "
                "naphthol-AS-BI phosphohydrolase, and alpha-glucosidase are "
                "present when assayed with API ZYM system."
            ),
            "notes": (
                "Park et al. treated alpha-glucosidase as a positive API ZYM "
                "enzyme-activity phenotype in the Flexibacterium corallicola "
                "type species description."
            ),
        },
        {
            "reference": "DOI:10.3390/microorganisms13092005",
            "snippet": (
                "alkaline phosphatase, esterase (C4), lipoid esterase (C8), "
                "lipase (C14), leucine arylamines, valine arylamines, "
                "cystine arylaminase, pancreatic coagulase, acid phosphatase, "
                "naphthol-AS-BI-phosphohydrolase, alpha-glucosidase, and "
                "N-acetyl-glucosaminidase were positive"
            ),
            "notes": (
                "Zhang and Liu detected alpha-glucosidase in Microbulbifer "
                "weihaiensis SDUM041083T with the API ZYM enzyme activity "
                "panel."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3037259",
            "taxon_label": "Flexibacterium corallicola",
            "note": (
                "Park et al. reported Flexibacterium corallicola as positive "
                "for alpha-glucosidase in the API ZYM enzyme activity panel."
            ),
            "reference": "DOI:10.1371/journal.pone.0322500",
        }
    ],
    "discussions": [
        {
            "discussion_id": "alpha-glucosidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for alpha-glucosidase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0090599 carries the same alpha-glucosidase activity label "
                "but denotes the enzyme molecular function rather than the "
                "organism-level alpha-glucosidase production phenotype, so it "
                "is appropriate as a causal-node grounding rather than an "
                "equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-11",
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
            "Minted alpha-glucosidase activity as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact alpha-glucosidase activity "
            "class yet."
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
