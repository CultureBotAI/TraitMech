#!/usr/bin/env python3
"""Add 2,3-butanediol fermentation with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / (
    "butanediol_fermentation.yaml"
)
LI = "DOI:10.1186/s12934-023-02163-6"
CHEN = "DOI:10.1007/s00253-014-5526-9"
ASM_MR_VP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-14T03:36:23Z"

RECORD = {
    "identifier": "traitmech:000181",
    "label": "2,3-butanediol fermentation",
    "definition": (
        "A fermentation in which microorganisms convert sugars to acetoin and "
        "2,3-butanediol neutral end products through the butanediol pathway."
    ),
    "definition_source": LI,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1002005"],
    "evidence": [
        {
            "reference": LI,
            "snippet": (
                "3-Hydroxybutanone (Acetoin, AC) and 2,3-butanediol (BD) "
                "are two essential four-carbon platform compounds with "
                "numerous pharmaceutical and chemical synthesis "
                "applications. AC and BD have two and three stereoisomers, "
                "respectively, while the application of the single isomer "
                "product in chemical synthesis is superior. AC and BD are "
                "glucose overflow metabolites produced by biological "
                "fermentation from a variety of microorganisms."
            ),
            "notes": (
                "Li et al. define acetoin and 2,3-butanediol as microbial "
                "glucose-overflow fermentation products and review the "
                "enzymology of their stereoisomer formation."
            ),
        },
        {
            "reference": ASM_MR_VP,
            "snippet": (
                "Bacteria fermenting sugars via the butanediol pathway "
                "produce acetoin (i.e., acetyl methyl carbinol or "
                "3-hydroxybutanone) as an intermediate which can be further "
                "reduced to 2,3-butanediol."
            ),
            "notes": (
                "The ASM methyl-red/Voges-Proskauer protocol distinguishes "
                "the butanediol fermentation pathway by acetoin formation "
                "with further reduction to 2,3-butanediol."
            ),
        },
        {
            "reference": CHEN,
            "snippet": (
                "Klebsiella pneumoniae is known to produce "
                "meso-2,3-butanediol and 2S,3S-butanediol, whereas "
                "2R,3R-butanediol was detected in the culture broth of K. "
                "pneumoniae CGMCC 1.6366."
            ),
            "notes": (
                "Chen et al. directly studied 2,3-butanediol stereoisomer "
                "formation by K. pneumoniae, supporting this species as a "
                "canonical 2,3-butanediol fermenter."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:573",
            "taxon_label": "Klebsiella pneumoniae",
            "note": (
                "K. pneumoniae CGMCC 1.6366 produced multiple "
                "2,3-butanediol stereoisomers in culture."
            ),
            "reference": CHEN,
        },
    ],
    "discussions": [
        {
            "discussion_id": "butanediol-fermentation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "2,3-butanediol fermentation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact GO or external metabolism class was resolved for "
                "the organism-level 2,3-butanediol fermentation phenotype; "
                "Voges-Proskauer assay terms, acetoin or butanediol chemical "
                "production reactions, and individual dehydrogenase "
                "molecular functions are shifted relative to this "
                "product-specific fermentation class."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
        },
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
            "Minted 2,3-butanediol fermentation as a DOI- and stable-URL-backed "
            "product-specific fermentation TraitRecord after a repository-wide "
            "duplicate review covering ignored and hidden files; METPO has no "
            "exact 2,3-butanediol fermentation class yet and the placeholder is "
            "reserved in proposals/metpo_traitmech_v58."
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
