#!/usr/bin/env python3
"""Add alanine arylamidase activity with URL/DOI-backed evidence."""
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
    "alanine_arylamidase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/11/2.html"
AMYGDALOBACTER = "DOI:10.1099/ijsem.0.006017"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T07:32:57Z"

RECORD = {
    "identifier": "traitmech:000161",
    "label": "alanine arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell exhibits "
        "alanine arylamidase/alanyl aminopeptidase activity, releasing "
        "N-terminal residues from peptide, amide, or arylamide substrates "
        "with preference for alanine."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "alanyl aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "alanine aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "L-alanine aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                '<b>Reaction:</b> Release of an N-terminal amino acid, '
                'Xaa<img src="../../../EZgif/FISS.GIF" align=top>Yaa- from '
                "a peptide, amide or arylamide. Xaa is preferably Ala, but "
                "may be most amino acids including Pro (slow action)."
            ),
            "notes": (
                "The NC-IUBMB EC 3.4.11.2 entry accepts membrane alanyl "
                "aminopeptidase and places the scissile-bond FISS.GIF image "
                "between Xaa and Yaa in a reaction line that includes "
                "arylamide substrates and preferential N-terminal alanine."
            ),
        },
        {
            "reference": AMYGDALOBACTER,
            "snippet": (
                "enzymatic activities are present for: α-galactosidase, "
                "N-acetyl-β-glucosaminidase, arginine arylamidase, proline "
                "arylamidase, leucyl glycine arylamidase, phenylalanine "
                "arylamidase, leucine arylamidase, tyrosine arylamidase, "
                "alanine arylamidase, glycine arylamidase, histidine "
                "arylamidase, glutamyl glutamic acid arylamidase, serine "
                "arylamidase, valine arylamidase, cysteine arylamidase, "
                "esterase, esterase lipase, alpha-chymotrypsin"
            ),
            "notes": (
                "Srinivasan et al. listed alanine arylamidase among "
                "enzymatic activities present in the Amygdalobacter indicium "
                "species description, supporting the API arylamidase row as "
                "a bacterial enzyme-activity phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3029272",
            "taxon_label": "Amygdalobacter indicium",
            "note": (
                "Srinivasan et al. reported Amygdalobacter indicium as "
                "positive for alanine arylamidase activity in an enzyme "
                "activity panel."
            ),
            "reference": AMYGDALOBACTER,
        }
    ],
    "discussions": [
        {
            "discussion_id": "alanine-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for alanine "
                "arylamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016285 alanyl aminopeptidase activity denotes the "
                "catalytic molecular function rather than the organism-level "
                "alanine arylamidase/alanyl aminopeptidase phenotype, so it "
                "is appropriate as a causal-node grounding for that enzyme "
                "activity and not as an equivalent TraitRecord xref."
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
            "Minted alanine arylamidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact alanine "
            "arylamidase activity class yet."
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
