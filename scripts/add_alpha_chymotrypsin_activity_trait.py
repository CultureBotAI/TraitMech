#!/usr/bin/env python3
"""Add alpha-chymotrypsin activity with URL/DOI-backed evidence."""
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
    "alpha_chymotrypsin_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/21/1.html"
AMYGDALOBACTER = "DOI:10.1099/ijsem.0.006017"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T05:29:03Z"

RECORD = {
    "identifier": "traitmech:000159",
    "label": "alpha-chymotrypsin activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active alpha-chymotrypsin enzymes that preferentially cleave peptide "
        "bonds on the carboxyl side of tyrosine, tryptophan, phenylalanine, "
        "or leucine residues."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "alpha-chymotrypsin",
            "synonym_type": "RELATED_SYNONYM",
            "source": AMYGDALOBACTER,
        }
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": "Reaction: Preferential cleavage: Tyr, Trp, Phe, Leu",
            "notes": (
                "The NC-IUBMB EC 3.4.21.1 entry accepts the name "
                "chymotrypsin and marks tyrosine, tryptophan, phenylalanine, "
                "and leucine as preferred cleavage sites in its reaction line."
            ),
        },
        {
            "reference": AMYGDALOBACTER,
            "snippet": (
                "enzymatic activities are present for: α-galactosidase, "
                "N-acetyl-β-glucosaminidase, arginine arylamidase, "
                "proline arylamidase, leucyl glycine arylamidase, "
                "phenylalanine arylamidase, leucine arylamidase, tyrosine "
                "arylamidase, alanine arylamidase, glycine arylamidase, "
                "histidine arylamidase, glutamyl glutamic acid arylamidase, "
                "serine arylamidase, valine arylamidase, cysteine "
                "arylamidase, esterase, esterase lipase, "
                "alpha-chymotrypsin"
            ),
            "notes": (
                "Srinivasan et al. listed alpha-chymotrypsin among enzymatic "
                "activities present in the Amygdalobacter indicium species "
                "description, consistent with the positive API ZYM table row "
                "for both assayed A. indicium strains."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3029272",
            "taxon_label": "Amygdalobacter indicium",
            "note": (
                "Srinivasan et al. reported Amygdalobacter indicium as "
                "positive for alpha-chymotrypsin activity in the API ZYM "
                "enzyme activity panel."
            ),
            "reference": AMYGDALOBACTER,
        }
    ],
    "discussions": [
        {
            "discussion_id": "alpha-chymotrypsin-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "alpha-chymotrypsin activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004263 chymotrypsin activity is obsolete, and its "
                "replacement GO:0004252 denotes broader serine-type "
                "endopeptidase molecular function rather than the organism-level "
                "alpha-chymotrypsin production phenotype. GO:0004252 is "
                "appropriate as a causal-node grounding for generic "
                "serine-type endopeptidase activity, not as an equivalent "
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
            "Minted alpha-chymotrypsin activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact alpha-chymotrypsin "
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
