#!/usr/bin/env python3
"""Preserve exact IUBMB scissile-bond tags in serine protease snippets."""
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
TIMESTAMP = "2026-09-12T05:47:58Z"

FIXES = {
    REPO_ROOT / "data/traits/physiology/trypsin_activity.yaml": {
        "old": "Reaction: Preferential cleavage: Arg, Lys",
        "intermediate": (
            'Reaction:</b> Preferential cleavage: Arg<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Lys<img '
            'src="../../../EZgif/FISS.GIF" align=top>'
        ),
        "new": (
            '<b>Reaction:</b> Preferential cleavage: Arg<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Lys<img '
            'src="../../../EZgif/FISS.GIF" align=top>'
        ),
        "notes": (
            "The NC-IUBMB EC 3.4.21.4 entry accepts the name trypsin and its "
            "reaction line places the scissile-bond FISS.GIF image "
            "immediately after Arg and Lys."
        ),
        "changes": (
            "Corrected the IUBMB reaction-line snippet for trypsin activity "
            "so it preserves the scissile-bond image tags from the source "
            "HTML (#819)."
        ),
    },
    REPO_ROOT / "data/traits/physiology/alpha_chymotrypsin_activity.yaml": {
        "old": "Reaction: Preferential cleavage: Tyr, Trp, Phe, Leu",
        "intermediate": (
            'Reaction:</b> Preferential cleavage: Tyr<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Trp<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Phe<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Leu<img '
            'src="../../../EZgif/FISS.GIF" align=top>'
        ),
        "new": (
            '<b>Reaction:</b> Preferential cleavage: Tyr<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Trp<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Phe<img '
            'src="../../../EZgif/FISS.GIF" align=top>, Leu<img '
            'src="../../../EZgif/FISS.GIF" align=top>'
        ),
        "notes": (
            "The NC-IUBMB EC 3.4.21.1 entry accepts the name chymotrypsin and "
            "its reaction line places the scissile-bond FISS.GIF image "
            "immediately after Tyr, Trp, Phe, and Leu."
        ),
        "changes": (
            "Corrected the IUBMB reaction-line snippet for "
            "alpha-chymotrypsin activity so it preserves the scissile-bond "
            "image tags from the source HTML (#819)."
        ),
    },
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML files")
    args = parser.parse_args()

    for path, fix in FIXES.items():
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        evidence = record["evidence"][0]
        if evidence.get("snippet") not in {
            fix["old"],
            fix["intermediate"],
            fix["new"],
        }:
            rel = path.relative_to(REPO_ROOT)
            raise SystemExit(f"{rel}: unexpected IUBMB snippet")

        evidence["snippet"] = fix["new"]
        evidence["notes"] = fix["notes"]
        record_curation_event(
            record,
            curator=CURATOR,
            action="CORRECTED_EVIDENCE_SNIPPET",
            changes=fix["changes"],
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )

        rel = path.relative_to(REPO_ROOT)
        if args.apply:
            write_validated_trait(record, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
