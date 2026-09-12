#!/usr/bin/env python3
"""Add gamma-glutamyltransferase activity with URL/DOI-backed evidence."""
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
    REPO_ROOT
    / "data"
    / "traits"
    / "physiology"
    / "gamma_glutamyltransferase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/4/19/13.html"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T06:47:37Z"

RECORD = {
    "identifier": "traitmech:000160",
    "label": "gamma-glutamyltransferase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell exhibits "
        "gamma-glutamyltransferase/glutathione-hydrolase activity, processing "
        "glutathione, glutathione-S-conjugates, or other N-terminal "
        "L-gamma-glutamyl substrates through a gamma-glutamyl-enzyme "
        "intermediate."
    ),
    "definition_source": IUBMB,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "gamma-glutamyl transferase",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.3389/fgene.2023.1240581",
        },
        {
            "synonym_text": "gamma-glutamyl transpeptidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "glutathione gamma-glutamate hydrolase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                "The enzyme then reacts with either a water molecule or a "
                "different acceptor substrate (usually an <small>L</small>-amino "
                "acid or a dipeptide) to form <small>L</small>-glutamate or a "
                "product containing a new &gamma;-glutamyl isopeptide bond, "
                "respectively. The enzyme acts on glutathione, "
                "glutathione-<i>S</i>-conjugates, and, at a lower level, on "
                "other substrates with an N-terminal <small>L</small>-&gamma;"
                "-glutamyl residue."
            ),
            "notes": (
                "The NC-IUBMB EC 3.4.19.13 entry scopes the bifunctional "
                "glutathione gamma-glutamate hydrolase/gamma-glutamyltransferase "
                "enzyme across water- and acceptor-mediated reactions."
            ),
        },
        {
            "reference": "DOI:10.3389/fgene.2023.1240581",
            "snippet": (
                "Like Helicobacter canis, these two putative isolates are "
                "positive for oxidase, gamma-glutamyl transferase, and "
                "alkaline phosphatase and negative for catalase and urease "
                "activities."
            ),
            "notes": (
                "Wang et al. detected gamma-glutamyltransferase activity in "
                "two Helicobacter zhangjianzhongii isolates with the API Campy "
                "biochemical panel."
            ),
        },
        {
            "reference": "DOI:10.3389/fgene.2023.1240581",
            "snippet": (
                "Both of these strains exhibit positive results for oxidase, "
                "gamma-glutamyl transferase, alkaline phosphatase, pyrrolidonyl "
                "arylamidase, L-arginine arylamidase, and L-aspartate "
                "arylamidase"
            ),
            "notes": (
                "The formal species description reports the same "
                "gamma-glutamyltransferase-positive phenotype in both "
                "H. zhangjianzhongii strains."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2974574",
            "taxon_label": "Helicobacter zhangjianzhongii",
            "note": (
                "Wang et al. reported both Helicobacter zhangjianzhongii "
                "isolates as positive for gamma-glutamyltransferase activity "
                "in the API Campy biochemical panel."
            ),
            "reference": "DOI:10.3389/fgene.2023.1240581",
        }
    ],
    "discussions": [
        {
            "discussion_id": "gamma-glutamyltransferase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "gamma-glutamyltransferase activity before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0003840 gamma-glutamyltransferase activity is obsolete, "
                "and its replacement GO:0036374 glutathione hydrolase activity "
                "denotes a glutathione-hydrolysis molecular function rather "
                "than the organism-level gamma-glutamyltransferase/glutathione-"
                "hydrolase phenotype. GO:0036374 is appropriate as a "
                "causal-node grounding when a graph needs that hydrolysis "
                "half-reaction, not as an equivalent TraitRecord xref."
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
            "Minted gamma-glutamyltransferase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact "
            "gamma-glutamyltransferase activity class yet and the placeholder "
            "is reserved in proposals/metpo_traitmech_v37."
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
