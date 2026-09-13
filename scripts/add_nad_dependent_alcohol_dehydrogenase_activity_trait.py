#!/usr/bin/env python3
"""Add NAD-dependent alcohol dehydrogenase activity with URL/DOI-backed evidence."""
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
    "nad_dependent_alcohol_dehydrogenase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T10:11:31Z"

RECORD = {
    "identifier": "traitmech:000165",
    "label": "NAD-dependent alcohol dehydrogenase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active NAD-dependent alcohol dehydrogenases that interconvert "
        "primary or secondary alcohols with aldehydes or ketones."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC1/1/1/1.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "alcohol dehydrogenase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "https://iubmb.qmul.ac.uk/enzyme/EC1/1/1/1.html",
        },
        {
            "synonym_text": "ethanol dehydrogenase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "https://iubmb.qmul.ac.uk/enzyme/EC1/1/1/1.html",
        },
        {
            "synonym_text": "NAD-dependent alcohol dehydrogenase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "https://iubmb.qmul.ac.uk/enzyme/EC1/1/1/1.html",
        },
    ],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC1/1/1/1.html",
            "snippet": (
                "<b>Reaction:</b> (1) a primary alcohol + "
                "NAD<small><sup>+</sup></small> = an aldehyde + NADH + "
                "H<small><sup>+</sup></small><br>\n\n"
                "(2) a secondary alcohol + NAD<small><sup>+</sup></small> = "
                "a ketone + NADH + H<small><sup>+</sup></small>"
            ),
            "notes": (
                "The NC-IUBMB EC 1.1.1.1 entry names alcohol dehydrogenase "
                "as alcohol:NAD+ oxidoreductase and defines the "
                "NAD-dependent primary-alcohol-to-aldehyde and "
                "secondary-alcohol-to-ketone reactions."
            ),
        },
        {
            "reference": "DOI:10.1111/j.1432-1033.1986.tb09366.x",
            "snippet": (
                "The two alcohol dehydrogenases found in Zymomonas mobilis "
                "have each been purified using dye-ligand chromatography and "
                "affinity elution with nucleotides."
            ),
            "notes": (
                "Neale et al. purified the ZADH-1 and ZADH-2 isoenzymes from "
                "Zymomonas mobilis and characterized their ethanol-oxidizing "
                "and acetaldehyde-reducing activities."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.169.6.2591-2597.1987",
            "snippet": (
                "The gene which encodes alcohol dehydrogenase II (adhB) from "
                "Zymomonas mobilis was cloned in Escherichia coli"
            ),
            "notes": (
                "Conway et al. cloned the Z. mobilis adhB gene, connected it "
                "to the purified alcohol dehydrogenase II protein, and used "
                "an indicator plate that detected recombinant ADH activity."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:542",
            "taxon_label": "Zymomonas mobilis",
            "note": (
                "Neale et al. purified and characterized the two native "
                "alcohol dehydrogenase isoenzymes from Zymomonas mobilis."
            ),
            "reference": "DOI:10.1111/j.1432-1033.1986.tb09366.x",
        }
    ],
    "discussions": [
        {
            "discussion_id": "nad-dependent-alcohol-dehydrogenase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for NAD-dependent "
                "alcohol dehydrogenase activity before adding a TraitRecord "
                "xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004022 and EC 1.1.1.1 denote the NAD-dependent "
                "molecular function rather than the organism-level "
                "NAD-dependent alcohol dehydrogenase production phenotype; "
                "the GO term remains an appropriate causal-node grounding "
                "lead but not an equivalent TraitRecord xref."
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
            "Minted NAD-dependent alcohol dehydrogenase activity as a "
            "URL/DOI-backed TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; METPO has no exact "
            "NAD-dependent alcohol dehydrogenase activity class yet."
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
