#!/usr/bin/env python3
"""Add beta-glucosidase activity with DOI-backed evidence."""
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
    "beta_glucosidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T17:57:39Z"

RECORD = {
    "identifier": "traitmech:000146",
    "label": "beta-glucosidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active beta-glucosidase enzymes that hydrolyze beta-D-glucosidic "
        "bonds in beta-D-glucosides."
    ),
    "definition_source": "DOI:10.1007/s13205-015-0328-z",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1007/s13205-015-0328-z",
            "snippet": (
                "β-Glucosidases (β-d-glucopyrranoside glucohydrolase) "
                "[E.C.3.2.1.21] are the enzymes which hydrolyze the "
                "glycosidic bond of a carbohydrate moiety to release "
                "nonreducing terminal glycosyl residues, glycoside and "
                "oligosaccharides"
            ),
            "notes": (
                "The review defines beta-glucosidases as EC 3.2.1.21 "
                "glycoside hydrolases, grounding the enzyme activity named by "
                "the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.2323/jgam.60.59",
            "snippet": (
                "In API ZYM, activities are positive for alkaline phosphatase, "
                "esterase (C4), leucine arylamidase, valine arylamidase, "
                "cystine arylamidase, acid phosphatase, "
                "naphthol-AS-BI-phosphohydrolase, α-glucosidase, "
                "β-glucosidase"
            ),
            "notes": (
                "The Flavobacterium panaciterrae species description reports "
                "beta-glucosidase among positive API ZYM activities for the "
                "DCY69T type strain."
            ),
        },
        {
            "reference": "DOI:10.3390/microorganisms12040776",
            "snippet": (
                "Although both strains showed positive results for "
                "α-glucosidase activity, β-glucosidase activity was only "
                "observed in L. mucosae NK41."
            ),
            "notes": (
                "Ma et al. detected beta-glucosidase activity in "
                "Limosilactobacillus mucosae NK41 with the API ZYM enzyme "
                "activity panel."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1222002",
            "taxon_label": "Flavobacterium panaciterrae",
            "note": (
                "An et al. reported Flavobacterium panaciterrae DCY69T as "
                "positive for beta-glucosidase in the API ZYM enzyme activity "
                "panel."
            ),
            "reference": "DOI:10.2323/jgam.60.59",
        }
    ],
    "discussions": [
        {
            "discussion_id": "beta-glucosidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "beta-glucosidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0008422 denotes the beta-D-glucosidase molecular function "
                "rather than the organism-level beta-glucosidase production "
                "phenotype, so it belongs as a causal-node grounding when a "
                "mechanistic graph needs the catalytic activity but not as an "
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
            "Minted beta-glucosidase activity as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact beta-glucosidase activity class "
            "yet."
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
