#!/usr/bin/env python3
"""Tighten trypsin/chymotrypsin phenotype definitions."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

CURATOR = "codex"
TIMESTAMP = "2026-09-12T06:00:57Z"

FIXES = {
    REPO_ROOT / "data/traits/physiology/trypsin_activity.yaml": {
        "identifier": "traitmech:000158",
        "discussion_id": "trypsin-activity-xref-gap",
        "old_definition": (
            "A physiological enzyme-activity phenotype in which a cell produces "
            "active trypsin enzymes that preferentially cleave peptide bonds on "
            "the carboxyl side of arginine or lysine residues."
        ),
        "new_definition": (
            "A physiological enzyme-activity phenotype in which a cell exhibits "
            "trypsin-like serine endopeptidase activity, preferentially cleaving "
            "peptide bonds on the carboxyl side of arginine or lysine residues."
        ),
        "old_rationale": (
            "GO:0004295 trypsin activity is obsolete, and its replacement "
            "GO:0004252 denotes broader serine-type endopeptidase molecular "
            "function rather than the organism-level trypsin production "
            "phenotype. GO:0004252 is appropriate as a causal-node grounding "
            "for generic serine endopeptidase activity, not as an equivalent "
            "TraitRecord xref."
        ),
        "new_rationale": (
            "GO:0004295 trypsin activity is obsolete, and its replacement "
            "GO:0004252 denotes broader serine-type endopeptidase molecular "
            "function rather than the organism-level trypsin-like serine "
            "endopeptidase phenotype. GO:0004252 is appropriate as a "
            "causal-node grounding for generic serine endopeptidase activity, "
            "not as an equivalent TraitRecord xref."
        ),
        "changes": (
            "Tightened the trypsin activity definition to describe a "
            "trypsin-like organismal phenotype instead of over-specifying "
            "production of the named vertebrate enzyme (#820)."
        ),
    },
    REPO_ROOT / "data/traits/physiology/alpha_chymotrypsin_activity.yaml": {
        "identifier": "traitmech:000159",
        "discussion_id": "alpha-chymotrypsin-activity-xref-gap",
        "old_definition": (
            "A physiological enzyme-activity phenotype in which a cell produces "
            "active alpha-chymotrypsin enzymes that preferentially cleave "
            "peptide bonds on the carboxyl side of tyrosine, tryptophan, "
            "phenylalanine, or leucine residues."
        ),
        "new_definition": (
            "A physiological enzyme-activity phenotype in which a cell exhibits "
            "chymotrypsin-like serine endopeptidase activity, preferentially "
            "cleaving peptide bonds on the carboxyl side of tyrosine, "
            "tryptophan, phenylalanine, or leucine residues."
        ),
        "old_rationale": (
            "GO:0004263 chymotrypsin activity is obsolete, and its replacement "
            "GO:0004252 denotes broader serine-type endopeptidase molecular "
            "function rather than the organism-level alpha-chymotrypsin "
            "production phenotype. GO:0004252 is appropriate as a causal-node "
            "grounding for generic serine-type endopeptidase activity, not as "
            "an equivalent TraitRecord xref."
        ),
        "new_rationale": (
            "GO:0004263 chymotrypsin activity is obsolete, and its replacement "
            "GO:0004252 denotes broader serine-type endopeptidase molecular "
            "function rather than the organism-level chymotrypsin-like serine "
            "endopeptidase phenotype. GO:0004252 is appropriate as a "
            "causal-node grounding for generic serine-type endopeptidase "
            "activity, not as an equivalent TraitRecord xref."
        ),
        "changes": (
            "Tightened the alpha-chymotrypsin activity definition to describe a "
            "chymotrypsin-like organismal phenotype instead of over-specifying "
            "production of the named vertebrate enzyme (#820)."
        ),
    },
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    for path, fix in FIXES.items():
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        rel = path.relative_to(REPO_ROOT)
        if record.get("identifier") != fix["identifier"]:
            raise SystemExit(f"{rel}: expected {fix['identifier']}")

        if record.get("definition") not in {
            fix["old_definition"],
            fix["new_definition"],
        }:
            raise SystemExit(f"{rel}: unexpected definition")
        record["definition"] = fix["new_definition"]

        discussions = record.get("discussions") or []
        discussion = next(
            (
                item
                for item in discussions
                if item.get("discussion_id") == fix["discussion_id"]
            ),
            None,
        )
        if discussion is None:
            raise SystemExit(f"{rel}: missing {fix['discussion_id']}")
        if discussion.get("rationale") not in {
            fix["old_rationale"],
            fix["new_rationale"],
        }:
            raise SystemExit(f"{rel}: unexpected discussion rationale")
        discussion["rationale"] = fix["new_rationale"]

        record_curation_event(
            record,
            curator=CURATOR,
            action="TIGHTENED_DEFINITION_WORDING",
            changes=fix["changes"],
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )

        if args.apply:
            write_validated_trait(record, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
