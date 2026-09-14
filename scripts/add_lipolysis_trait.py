#!/usr/bin/env python3
"""Add lipolysis as a DOI-backed metabolism trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "lipolysis.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T21:00:00Z"

RECORD = {
    "identifier": "traitmech:000190",
    "label": "lipolysis",
    "definition": (
        "A metabolism in which a microorganism hydrolyzes triacylglycerols into "
        "fatty acids and glycerol through lipase-catalyzed ester cleavage."
    ),
    "definition_source": "DOI:10.1186/s12934-020-01428-8",
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000060"],
    "evidence": [
        {
            "reference": "DOI:10.1186/s12934-020-01428-8",
            "snippet": (
                "Microbial lipases (EC 3.1.1.3) catalyze the hydrolysis "
                "of long chain triglycerides"
            ),
            "notes": (
                "Chandra et al. review microbial lipases and their use in "
                "long-chain triglyceride hydrolysis."
            ),
        },
        {
            "reference": "DOI:10.1007/s00253-004-1568-8",
            "snippet": (
                "Lipases, triacylglycerol hydrolases, are an important group "
                "of biotechnologically relevant enzymes"
            ),
            "notes": (
                "Gupta et al. review bacterial lipases as microbial enzymes "
                "for triacylglycerol hydrolysis."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "lipolysis-xref-gap",
            "prompt": (
                "Resolve an exact external ontology xref for organism-level "
                "microbial lipolysis before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only obsolete METPO:1000175 "
                "lipolysis, and GO:0016298 denotes the lipase molecular function "
                "rather than the organism-level lipid-hydrolysis trait. GO lipid "
                "catabolic process classes also include downstream fatty-acid "
                "catabolism and are broader than lipase-driven triacylglycerol "
                "hydrolysis."
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
            "Minted lipolysis as a DOI-backed metabolism TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has only an obsolete lipolysis class."
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
