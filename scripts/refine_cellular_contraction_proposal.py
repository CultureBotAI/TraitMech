"""Refine the contraction label and emit both existing child subclass axioms."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

import add_cellular_contraction_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "data/traits/physiology/cellular_contraction.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v605/metpo_proposal_classes_robot.tsv"
LABEL = "cell body or cytoplasmic projection contraction"
TIMESTAMP = "2026-10-14T23:56:33Z"
PREIMAGE_SHA256 = "0d8ab72f1786596f59971da34aa8ee9c81ed6f68475171644a2e091640036af1"
CHILD_PROPOSALS = {
    "METPO:1063500": (ROOT / "proposals/metpo_traitmech_v558/metpo_proposal_classes_robot.tsv",
                      "dad8ccb2031b4e7f518efa57ee3094a1137ff60af3fe5de783b0a6d8cd8d5655"),
    "METPO:1068100": (ROOT / "proposals/metpo_traitmech_v604/metpo_proposal_classes_robot.tsv",
                      "d6ff228db4e4814e7f789aff4b5958c0681514792e1f14e8c2cf48c5af293d13"),
}


def build_record() -> dict:
    record = original.build_record()
    if original.digest(record) != PREIMAGE_SHA256:
        raise SystemExit("Original parent definition or evidence changed")
    record["label"] = LABEL
    record_curation_event(record, curator="codex", action="REFINE_CONTRACTION_LABEL",
        changes=(
            "Replaced the parenthetical label cellular contraction (body or cytoplasmic "
            "projection shortening) with cell body or cytoplasmic projection contraction. "
            "Preserved definition, endpoint qualifier, evidence, discussions, identifier "
            "and earlier history. The v605 template also emits the two existing child "
            "subclass axioms without modifying historical v558/v604 cohorts. Addresses "
            "external review issues #1941 and #1942; no new biology or human review "
            "promotion. Timestamp records observed acceptance of the refinements."
        ), llm_assisted=True, timestamp=TIMESTAMP)
    return record


def proposal_tsv(record: dict) -> str:
    rows = list(csv.reader(io.StringIO(original.proposal_tsv(record)), delimiter="\t"))
    rows[2][9] = "Shortening parent; refined parents for existing v558/v604 child IDs."
    for identifier, (path, expected) in CHILD_PROPOSALS.items():
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise SystemExit(f"Historical proposal changed: {path}")
        source = list(csv.reader(io.StringIO(raw.decode()), delimiter="\t"))
        if (len(source) != 3 or source[:2] != rows[:2] or len(source[2]) != 11
                or source[2][0] != identifier or source[2][4] != "METPO:1000059"):
            raise SystemExit(f"Historical proposal shape or identity changed: {path}")
        child = copy.deepcopy(source[2])
        child[4] = original.METPO_ID
        child[9] += " Existing ID; v605 supplies the refined direct parent."
        rows.append(child)
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    old = original.build_record()
    record = build_record()
    proposal = proposal_tsv(record)
    current = yaml.safe_load(TARGET.read_text())
    current_tsv = PROPOSAL.read_text()
    preimage = current == old and current_tsv == original.proposal_tsv(old)
    replay = current == record and current_tsv == proposal
    if not preimage and not replay:
        raise SystemExit("Parent or proposal differs from reviewed preimage/result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply and not replay:
        write_validated_trait(record, TARGET)
        PROPOSAL.write_text(proposal)
    print("Applied or unchanged replay" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
