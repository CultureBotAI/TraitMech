#!/usr/bin/env python3
"""Add the bacterial siderophore production physiology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "siderophore_production.yaml"
SCHALK = "DOI:10.1111/1462-2920.14937"
RINGEL = "DOI:10.15698/mic2018.10.649"
IMPERI = "DOI:10.1073/pnas.0908760106"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T18:32:00Z"

RECORD = {
    "identifier": "traitmech:000186",
    "label": "siderophore production",
    "definition": (
        "A physiological trait in which bacteria biosynthesize and release "
        "siderophores that scavenge extracellular iron for uptake."
    ),
    "definition_source": SCHALK,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": SCHALK,
            "snippet": (
                "Siderophores are iron-chelating molecules produced by "
                "bacteria to access iron, a key nutrient."
            ),
            "notes": (
                "Schalk et al. define bacterial siderophores as produced "
                "iron-chelating molecules that enable iron access."
            ),
        },
        {
            "reference": SCHALK,
            "snippet": (
                "They are released by bacteria into their environment to "
                "scavenge iron and bring it back into the cells."
            ),
            "notes": (
                "The same review supports the release, extracellular "
                "scavenging, and uptake clauses in the local definition."
            ),
        },
        {
            "reference": RINGEL,
            "snippet": (
                "Pyoverdines are fluorescent siderophores of pseudomonads "
                "that play important roles for growth under iron-limiting "
                "conditions."
            ),
            "notes": (
                "Ringel and Bruser support pyoverdine production as a "
                "fluorescent-pseudomonad siderophore-production subtype."
            ),
        },
        {
            "reference": IMPERI,
            "snippet": (
                "The siderophore pyoverdine (PVD) is a primary virulence "
                "factor of the human pathogenic bacterium Pseudomonas "
                "aeruginosa"
            ),
            "notes": (
                "Imperi et al. support Pseudomonas aeruginosa as a "
                "pyoverdine-producing bacterium."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Pseudomonas aeruginosa is used as a canonical "
                "pyoverdine-producing bacterium."
            ),
            "reference": IMPERI,
        },
    ],
    "discussions": [
        {
            "discussion_id": "siderophore-production-xref-gap",
            "prompt": (
                "Resolve exact external ontology xrefs for the bacterial "
                "siderophore production phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only METPO:1000277 "
                "obsolete siderophore. GO:0019290 is limited to the "
                "siderophore biosynthetic process, GO:0015891 is a "
                "siderophore transport process, and CHEBI:26672 denotes the "
                "siderophore molecule rather than the organism-level "
                "biosynthesis-and-release trait."
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
            "Minted siderophore production as a DOI-backed TraitRecord after "
            "a repository-wide duplicate review covering ignored and hidden "
            "files; METPO has only an obsolete siderophore class in the "
            "local snapshot and the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v63."
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
