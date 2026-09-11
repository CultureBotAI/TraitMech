#!/usr/bin/env python3
"""Enrich the seeded METPO oxidase-negative record with assay evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

OXIDASE_NEGATIVE = REPO_ROOT / "data" / "traits" / "other" / "oxidase_negative.yaml"

CURATOR = "codex"
TIMESTAMP = "2026-09-11T15:16:21Z"

OMP_OXIDASE_NEGATIVE = "http://purl.obolibrary.org/obo/OMP_0006084"
ASM_OXIDASE_PROTOCOL = "https://asm.org/protocols/oxidase-test-protocol"
HAFEZI_BIOCHEMICAL_TESTS = "DOI:10.5812/chbs-160199"

SEEDED_SYNONYMS = [
    {
        "synonym_text": "oxidase -",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
    {
        "synonym_text": "oxidase test negative",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl",
    },
]

OXIDASE_NEGATIVE_UPDATES = {
    "definition_source": OMP_OXIDASE_NEGATIVE,
    "evidence": [
        {
            "reference": ASM_OXIDASE_PROTOCOL,
            "snippet": (
                "The test can be used to distinguish Neisseria gonorrhoeae "
                "(oxidase positive) from Staphylococcus spp. and Streptococcus "
                "spp. (oxidase negative)"
            ),
            "notes": (
                "The American Society for Microbiology protocol gives "
                "oxidase-negative Staphylococcus and Streptococcus spp. as "
                "contrasts to an oxidase-positive Neisseria gonorrhoeae result."
            ),
        },
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "A positive result from the dry filter paper method is indicated "
                "by the appearance of a dark purple color within 5 to 10 "
                "seconds. A 'delayed positive' result is recognized when a "
                "color change occurs between 10 and 60 seconds, whereas a "
                "negative result is indicated by the paper remaining colorless "
                "or changing color after more than 60 seconds"
            ),
            "notes": (
                "Hafezi and Khamar review the oxidase-test polarity and "
                "interpret a colorless dry filter paper, or a color change only "
                "after the cutoff, as a negative result."
            ),
        },
        {
            "reference": HAFEZI_BIOCHEMICAL_TESTS,
            "snippet": (
                "Bacteria that are classified as oxidase-negative can be "
                "anaerobic, aerobic, or facultative. A negative oxidase result "
                "indicates merely the absence of cytochrome c oxidase, which is "
                "responsible for oxidizing the reactant, while these organisms "
                "may utilize alternative oxidases for electron transfer during "
                "respiration"
            ),
            "notes": (
                "The review constrains interpretation of the negative assay "
                "outcome to cytochrome c oxidase under the oxidase-test readout, "
                "rather than absence of every terminal oxidase."
            ),
        },
    ],
}


def load_record(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        record = yaml.safe_load(fh)
    if not isinstance(record, dict):
        raise TypeError(f"{path} does not contain a mapping")
    return record


def enrich_oxidase_negative(record: dict) -> dict:
    record = copy.deepcopy(record)
    if record.get("identifier") != "METPO:1007086":
        raise ValueError(f"expected METPO:1007086, got {record.get('identifier')!r}")
    if record.get("label") != "oxidase negative":
        raise ValueError(f"expected oxidase negative, got {record.get('label')!r}")
    if record.get("mapping_status") != "SEEDED":
        raise ValueError(f"expected SEEDED, got {record.get('mapping_status')!r}")
    if record.get("trait_category") != "OTHER":
        raise ValueError(f"expected OTHER, got {record.get('trait_category')!r}")
    if record.get("parent_traits") != ["METPO:1007081"]:
        raise ValueError(
            f"expected oxidase-test parent, got {record.get('parent_traits')!r}"
        )
    if record.get("synonyms") != SEEDED_SYNONYMS:
        raise ValueError(f"expected seeded synonyms, got {record.get('synonyms')!r}")

    record.update(copy.deepcopy(OXIDASE_NEGATIVE_UPDATES))
    record.pop("canonical_examples", None)
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Enriched the seeded METPO oxidase-negative test outcome with OMP "
            "definition provenance plus stable-URL and DOI-backed assay "
            "evidence after a repository-wide duplicate review covering "
            "ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    record = enrich_oxidase_negative(load_record(OXIDASE_NEGATIVE))
    rel = OXIDASE_NEGATIVE.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, OXIDASE_NEGATIVE)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
