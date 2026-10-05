"""Qualify size-based anisogamy against behavioural-only usage (#1711)."""

from __future__ import annotations

import argparse
import csv
import io
import tempfile
from pathlib import Path

import yaml

import add_anisogamy_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.TARGET
PROPOSAL = original.PROPOSAL / "metpo_proposal_classes_robot.tsv"
REFERENCE = "DOI:10.1371/journal.pone.0181413"
SCOPE_NOTE = (
    "Kaczmarska et al. (2017), DOI:10.1371/journal.pone.0181413, also use "
    "physiological/behavioural anisogamy for approximately equal-sized gametes "
    "in diatoms. That usage is not equivalent to the size-based sense selected "
    "here: behavioural or physiological differences alone do not establish "
    "gamete-type size dimorphism. Do not map that usage as an exact synonym "
    "or infer organism-level disjointness; its relationship needs separate "
    "scope review. "
)


def build_record() -> dict:
    record = original.build_record()
    record["evidence"].append({
        "reference": REFERENCE,
        "snippet": (
            "physiological and behavioural anisogamy of more or less equal size "
            "gametes, each with sex-specific behaviour and morphology"
        ),
        "notes": (
            "Kaczmarska et al. (2017), Discussion > Sexual reproduction and life "
            "history. This exact contiguous clause was checked in publisher HTML "
            "and manuscript XML. It documents alternative diatom terminology, not "
            "evidence that equal-sized gametes satisfy this record's size-dimorphism "
            "definition. That Discussion passage and the opening live-cell Results "
            "paragraphs were inspected; the latter describe sex-dependent motility. "
            "Remaining Results, actual figures, tables and supplements were not "
            "audited. No diatom canonical example or size measurement is inferred."
        ),
    })
    scope = record["discussions"][0]
    scope["rationale"] += " " + SCOPE_NOTE.rstrip()
    record_curation_event(
        record, curator="codex", action="QUALIFIED_TRAIT_SCOPE",
        changes=(
            "Addressed #1711 by citing directly inspected diatom terminology and "
            "distinguishing behavioural/physiological anisogamy from the selected "
            "size-based sense. Added a verbatim scope snippet and inspection "
            "limits; preserved definition, canonical example and unresolved "
            "mechanism/hierarchy questions."
        ),
        llm_assisted=True, timestamp="2026-10-05T13:15:22Z",
    )
    return record


def proposal_tsv() -> str:
    rows = list(csv.reader(io.StringIO(original.proposal_tsv(original.build_record())),
                           delimiter="\t"))
    rows[2][3] += "|" + REFERENCE
    rows[2][9] += " Behavioural differences alone do not establish this size-based sense."
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = yaml.safe_load(TARGET.read_text())
    after = build_record()
    if before not in (original.build_record(), after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    proposal = proposal_tsv()
    if PROPOSAL.read_text() not in (
        original.proposal_tsv(original.build_record()), proposal,
    ):
        raise SystemExit("Existing proposal differs from reviewed preimage or result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(after, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(after, TARGET)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
