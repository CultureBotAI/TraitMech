#!/usr/bin/env python3
"""Add arginine arylamidase activity with URL/DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = (
    REPO_ROOT / "data" / "traits" / "physiology" / "arginine_arylamidase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/11/6.html"
HELICOBACTER = "DOI:10.3389/fgene.2023.1240581"
AMYGDALOBACTER = "DOI:10.1099/ijsem.0.006017"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T11:40:11Z"

RECORD = {
    "identifier": "traitmech:000167",
    "label": "arginine arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell exhibits "
        "arginine arylamidase/arginyl aminopeptidase activity, releasing "
        "N-terminal arginine or lysine residues from peptides or hydrolyzing "
        "arginine and lysine arylamides."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "L-arginine arylamidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": HELICOBACTER,
        },
        {
            "synonym_text": "aminopeptidase B",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "arginine aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "arginyl aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "L-arginine aminopeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                "<b>Reaction:</b> Release of N-terminal Arg and Lys from "
                "oligopeptides when P1' is not Pro. Also acts on arylamides "
                "of Arg and Lys"
            ),
            "notes": (
                "The NC-IUBMB EC 3.4.11.6 entry accepts aminopeptidase B, "
                "records arginine aminopeptidase, arginyl aminopeptidase, and "
                "L-arginine aminopeptidase as other names, and includes "
                "arginine and lysine arylamides in the reaction scope."
            ),
        },
        {
            "reference": HELICOBACTER,
            "snippet": (
                "Both of these strains exhibit positive results for oxidase, "
                "gamma-glutamyl transferase, alkaline phosphatase, "
                "pyrrolidonyl arylamidase, L-arginine arylamidase, and "
                "L-aspartate arylamidase"
            ),
            "notes": (
                "Wang et al. reported both Helicobacter zhangjianzhongii "
                "isolates as positive for L-arginine arylamidase in the "
                "formal species description."
            ),
        },
        {
            "reference": AMYGDALOBACTER,
            "snippet": (
                "arginine arylamidase, proline arylamidase, leucyl glycine "
                "arylamidase, phenylalanine arylamidase, leucine arylamidase, "
                "tyrosine arylamidase, alanine arylamidase, glycine "
                "arylamidase, histidine arylamidase"
            ),
            "notes": (
                "Srinivasan et al. listed arginine arylamidase among "
                "enzymatic activities present in the Amygdalobacter indicium "
                "species description, supporting the API arylamidase row as a "
                "directly assayed bacterial enzyme-activity phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2974574",
            "taxon_label": "Helicobacter zhangjianzhongii",
            "note": (
                "Wang et al. reported both Helicobacter zhangjianzhongii "
                "isolates as positive for L-arginine arylamidase in the "
                "formal species description."
            ),
            "reference": HELICOBACTER,
        }
    ],
    "discussions": [
        {
            "discussion_id": "arginine-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for arginine "
                "arylamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004177 denotes broad aminopeptidase molecular function, "
                "and EC 3.4.11.6 denotes the aminopeptidase B/arginyl "
                "aminopeptidase molecular function rather than the "
                "organism-level arginine arylamidase assay phenotype. Both "
                "remain causal-node grounding leads rather than equivalent "
                "TraitRecord xrefs."
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
            "Minted arginine arylamidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact arginine "
            "arylamidase activity class yet and the placeholder is reserved "
            "in proposals/metpo_traitmech_v44."
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
