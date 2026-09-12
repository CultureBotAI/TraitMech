#!/usr/bin/env python3
"""Add prolyl aminopeptidase activity with URL/DOI-backed evidence."""
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
    "prolyl_aminopeptidase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/11/5.html"
PIP = "DOI:10.1111/j.1365-2958.1993.tb01249.x"
AMYGDALOBACTER = "DOI:10.1099/ijsem.0.006017"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T11:07:00Z"

RECORD = {
    "identifier": "traitmech:000166",
    "label": "prolyl aminopeptidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active prolyl aminopeptidases that release N-terminal proline "
        "residues from peptides."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "proline aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "Pro-X aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "proline iminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "proline arylamidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": AMYGDALOBACTER,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": "<b>Reaction:</b> Release of N-terminal proline from a peptide",
            "notes": (
                "The NC-IUBMB EC 3.4.11.5 entry accepts prolyl "
                "aminopeptidase, gives the N-terminal-proline release "
                "reaction, and records proline aminopeptidase, Pro-X "
                "aminopeptidase, and proline iminopeptidase as other names."
            ),
        },
        {
            "reference": PIP,
            "snippet": (
                "Proline iminopeptidase (Pip) is a hydrolase elaborated by "
                "virtually all strains of Neisseria gonorrhoeae that "
                "selectively removes N-terminal proline residues from peptides."
            ),
            "notes": (
                "Albertson and Koomey cloned the gonococcal pip gene and "
                "confirmed that the encoded enzyme can release biologically "
                "active proline from peptides."
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
                "Srinivasan et al. listed proline arylamidase among "
                "enzymatic activities present in the Amygdalobacter indicium "
                "species description, supporting the API proline arylamidase "
                "row as a directly assayed bacterial enzyme-activity "
                "phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:485",
            "taxon_label": "Neisseria gonorrhoeae",
            "note": (
                "Albertson and Koomey cloned the Neisseria gonorrhoeae "
                "proline iminopeptidase gene and confirmed that the encoded "
                "Pip enzyme releases proline from peptides."
            ),
            "reference": PIP,
        }
    ],
    "discussions": [
        {
            "discussion_id": "prolyl-aminopeptidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for prolyl "
                "aminopeptidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004177 denotes broad aminopeptidase molecular function "
                "and EC 3.4.11.5 denotes a prolyl aminopeptidase molecular "
                "function; both are scope-shifted relative to the "
                "organism-level prolyl aminopeptidase production phenotype, "
                "so they remain causal-node grounding leads rather than "
                "equivalent TraitRecord xrefs."
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
            "Minted prolyl aminopeptidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact prolyl "
            "aminopeptidase activity class yet."
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
