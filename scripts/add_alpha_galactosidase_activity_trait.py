#!/usr/bin/env python3
"""Add alpha-galactosidase activity with DOI-backed evidence."""
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
    "alpha_galactosidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T23:46:20Z"

RECORD = {
    "identifier": "traitmech:000149",
    "label": "alpha-galactosidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active alpha-galactosidase enzymes that hydrolyze alpha-1,6-linked "
        "galactose residues in oligosaccharides and polymeric galactomannans."
    ),
    "definition_source": "DOI:10.3109/07388551.2013.794124",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.3109/07388551.2013.794124",
            "snippet": (
                "The enzyme α-galactosidase (α-D-galactoside "
                "galactohydrolase; EC 3.2.1.22) catalyzes the hydrolysis of "
                "α-1,6-linked galactose residues in oligosaccharides and "
                "polymeric galactomannan."
            ),
            "notes": (
                "Katrolia et al. define alpha-galactosidase as EC 3.2.1.22, "
                "an enzyme that hydrolyzes alpha-1,6-linked galactose "
                "residues, grounding the enzyme activity named by the "
                "organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/jcm.22.3.333-335.1985",
            "snippet": (
                "Selenomonas sputigena was positive for α-galactosidase, "
                "β-galactosidase, and α-glucosidase (API ZYM strip) and for "
                "α-glucosidase, β-glucosidase, and α-galactosidase (API "
                "An-Ident strip)."
            ),
            "notes": (
                "Tanner et al. detected alpha-galactosidase in Selenomonas "
                "sputigena with the API ZYM enzyme activity panel and the "
                "API An-Ident strip."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:69823",
            "taxon_label": "Selenomonas sputigena",
            "note": (
                "Tanner et al. reported Selenomonas sputigena as positive for "
                "alpha-galactosidase in API ZYM and API An-Ident enzyme "
                "activity panels."
            ),
            "reference": "DOI:10.1128/jcm.22.3.333-335.1985",
        }
    ],
    "discussions": [
        {
            "discussion_id": "alpha-galactosidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "alpha-galactosidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004557 denotes the alpha-galactosidase/melibiase "
                "molecular function rather than the organism-level "
                "alpha-galactosidase production phenotype, so it is "
                "appropriate as a causal-node grounding rather than an "
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
            "Minted alpha-galactosidase activity as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact alpha-galactosidase activity "
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
