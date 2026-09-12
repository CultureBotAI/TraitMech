#!/usr/bin/env python3
"""Add trypsin activity with URL/DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "trypsin_activity.yaml"
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/21/4.html"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T04:36:25Z"

RECORD = {
    "identifier": "traitmech:000158",
    "label": "trypsin activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active trypsin enzymes that preferentially cleave peptide bonds on "
        "the carboxyl side of arginine or lysine residues."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "trypsin",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        }
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": "Reaction: Preferential cleavage: Arg, Lys",
            "notes": (
                "The NC-IUBMB EC 3.4.21.4 entry accepts the name trypsin "
                "and marks the cleavage sites after arginine and lysine "
                "residues in its reaction line."
            ),
        },
        {
            "reference": IUBMB,
            "snippet": (
                "Isolated as multiple cationic and anionic trypsins [5] "
                "from the pancreas of many vertebrates and from lower "
                "species including crayfish, insects (cocoonase) and "
                "microorganisms"
            ),
            "notes": (
                "The NC-IUBMB EC 3.4.21.4 comments note that trypsins have "
                "also been isolated from microorganisms."
            ),
        },
        {
            "reference": "DOI:10.1371/journal.pone.0322500",
            "snippet": (
                "Enzyme activities of acid- and alkaline-phosphatases, "
                "esterase, esterase lipase, leucine arylamidase, trypsin, "
                "naphthol-AS-BI phosphohydrolase, and alpha-glucosidase are "
                "present when assayed with API ZYM system."
            ),
            "notes": (
                "Park et al. treated trypsin as a positive API ZYM "
                "enzyme-activity phenotype in the Flexibacterium corallicola "
                "type species description."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3037259",
            "taxon_label": "Flexibacterium corallicola",
            "note": (
                "Park et al. reported Flexibacterium corallicola as positive "
                "for trypsin activity in the API ZYM enzyme activity panel."
            ),
            "reference": "DOI:10.1371/journal.pone.0322500",
        }
    ],
    "discussions": [
        {
            "discussion_id": "trypsin-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for trypsin "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004295 trypsin activity is obsolete, and its replacement "
                "GO:0004252 denotes broader serine-type endopeptidase "
                "molecular function rather than the organism-level trypsin "
                "production phenotype. GO:0004252 is appropriate as a "
                "causal-node grounding for generic serine endopeptidase "
                "activity, not as an equivalent TraitRecord xref."
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
            "Minted trypsin activity as a URL/DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; METPO has no exact trypsin activity class yet."
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
