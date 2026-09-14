#!/usr/bin/env python3
"""Add the arsenite oxidation metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "arsenite_oxidation.yaml"
SHI = "DOI:10.3389/fmicb.2020.569282"
SANTINI = "DOI:10.1128/AEM.66.1.92-97.2000"
HOQUE = "DOI:10.1186/s12866-024-03676-9"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T20:30:00Z"

RECORD = {
    "identifier": "traitmech:000189",
    "label": "arsenite oxidation",
    "definition": (
        "A metabolism in which an organism enzymatically oxidizes arsenite to "
        "arsenate as an energy-generating electron donor or detoxification "
        "substrate."
    ),
    "definition_source": SHI,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000060"],
    "synonyms": [
        {
            "synonym_text": "As(III) oxidation",
            "synonym_type": "EXACT_SYNONYM",
            "source": SHI,
        },
        {
            "synonym_text": "microbial arsenite oxidation",
            "synonym_type": "RELATED_SYNONYM",
            "source": SHI,
        },
    ],
    "evidence": [
        {
            "reference": SHI,
            "snippet": (
                "The biological oxidation of arsenite [As(III)] to arsenate "
                "[As(V)] is considered a strategy to reduce arsenic toxicity "
                "and provide energy"
            ),
            "notes": (
                "Shi et al. review biological As(III)-to-As(V) oxidation as "
                "a microbial detoxification and energy-generating metabolism."
            ),
        },
        {
            "reference": SANTINI,
            "snippet": (
                "A facultatively chemolithoautotrophic arsenite oxidizer "
                "(strain NT-26) was isolated from the arsenopyrite-containing "
                "gold mine at Pine Creek, Northern Territory, Australia."
            ),
            "notes": (
                "Santini et al. isolated the aerobic chemolithoautotrophic "
                "arsenite-oxidizing strain NT-26."
            ),
        },
        {
            "reference": HOQUE,
            "snippet": (
                "Both BAW48 and BAS32 isolates demonstrated As(III) oxidation"
            ),
            "notes": (
                "Hoque et al. report As(III)-oxidizing Achromobacter "
                "aegrifaciens isolates from arsenic-contaminated tubewell "
                "water and soil."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "arsenite-oxidation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "arsenite oxidation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only METPO:1000840 "
                "obsolete Arsenite oxidation. Potential external molecular "
                "function terms for arsenite oxidase activity are narrower "
                "than the organism-level As(III)-to-As(V) metabolism, and a "
                "future mechanism graph should distinguish aerobic AioBA "
                "oxidation from anaerobic ArxAB-mediated arsenite oxidation."
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
            "Minted arsenite oxidation as a DOI-backed arsenic metabolism "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has only an "
            "obsolete Arsenite oxidation class and the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v66."
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
