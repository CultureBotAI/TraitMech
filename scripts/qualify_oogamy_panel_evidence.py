"""Distinguish a cross-derived zygote from its engineered parent (#1713)."""

import argparse
import tempfile
from pathlib import Path

import yaml

import add_oogamy_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.TARGET
OLD = "Figure 2B/C/F/H show wild-type egg/sperm controls; D/E/G/I are engineered pseudo-males."
NEW = (
    "Figure 2B/C/F/H show wild-type egg/sperm controls; D/G/I show the "
    "engineered pseudo-male spheroid, its sperm packet and an aberrant sperm "
    "cell, respectively. Panel E shows a mature zygote from an Eve::VcMID-BH "
    "x Eve cross, not the engineered parent."
)


def build_record() -> dict:
    record = original.build_record()
    evidence = record["evidence"][3]
    if evidence["reference"] != original.GENG_2014 or evidence["notes"].count(OLD) != 1:
        raise SystemExit("Evidence differs from reviewed preimage")
    evidence["notes"] = evidence["notes"].replace(OLD, NEW)
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE_PANEL",
        changes=(
            "Addressed #1713: Figure 2E in Geng et al. (2014) is a cross-derived "
            "mature zygote, not an engineered pseudo-male. Distinguished its "
            "role from D/G/I using the directly inspected caption and actual "
            "figure. Definition, verbatim snippet, natural canonical example "
            "and proposal hierarchy remain unchanged."
        ),
        llm_assisted=True, timestamp="2026-10-05T14:24:04Z",
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not TARGET.exists():
        raise SystemExit("Missing reviewed preimage")
    before = yaml.safe_load(TARGET.read_text())
    after = build_record()
    if before not in (original.build_record(), after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(after, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(after, TARGET)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
