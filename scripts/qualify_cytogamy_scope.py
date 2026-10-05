"""Exclude one-way nuclear transfer from the cytogamy definition (#1717)."""

from __future__ import annotations

import argparse
import csv
import io
import tempfile
from pathlib import Path

import yaml

import add_cytogamy_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.TARGET
PROPOSAL = original.PROPOSAL


def build_record() -> dict:
    record = original.build_record()
    record["definition"] = (
        "A sexual-reproduction phenotype in which a paired cell self-fertilizes "
        "by fusion of its own gametic nuclei without exchanging gametic nuclei "
        "with its partner."
    )
    scope = record["discussions"][0]
    scope["rationale"] = scope["rationale"].replace(
        "Pairing with internal gametic-nuclear fusion and no reciprocal exchange",
        "Pairing with internal gametic-nuclear fusion and no gametic-nuclear exchange",
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_TRAIT_SCOPE",
        changes=(
            "Addressed #1717: replaced without reciprocal exchange with no "
            "gametic-nuclear exchange with the partner, excluding one-way "
            "transfer as well. Used an individual paired-cell formulation "
            "without requiring the same outcome in both partners. Preserved "
            "all evidence, source qualifiers and the phenotype parent."
        ),
        llm_assisted=True, timestamp="2026-10-05T16:19:43Z",
    )
    return record


def proposal_tsv() -> str:
    rows = list(csv.reader(io.StringIO(original.proposal_tsv(build_record())), delimiter="\t"))
    rows[2][9] = "Paired-cell internal self-fertilization without gametic-nuclear exchange; not unpaired autogamy."
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not TARGET.exists() or not PROPOSAL.exists():
        raise SystemExit("Missing reviewed record or proposal preimage")
    before = yaml.safe_load(TARGET.read_text())
    after = build_record()
    if before not in (original.build_record(), after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    proposal = proposal_tsv()
    if PROPOSAL.read_text() not in (original.proposal_tsv(original.build_record()), proposal):
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
