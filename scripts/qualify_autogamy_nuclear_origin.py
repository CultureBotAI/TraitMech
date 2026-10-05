"""Preserve same-cell nuclear origin in the #1719 boundary repair (#1720)."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

import yaml

import add_paedogamy_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.NEIGHBOR
PROPOSAL = original.NEIGHBOR_PROPOSAL


def build_record() -> dict:
    record = original.build_neighbor(original.neighbor_preimage())
    record["definition"] = (
        "A sexual-reproduction phenotype in which two meiotically derived "
        "gametic nuclei formed within one unpaired, undivided cell fuse with "
        "each other, without fusion of separate gametes."
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_NUCLEAR_ORIGIN",
        changes=(
            "Addressed #1720: retained the original same-cell origin of both "
            "gametic nuclei alongside the #1719 undivided-cell and "
            "no-separate-gamete-fusion boundary. Fusion location alone does "
            "not establish self-fertilization. Preserved evidence, example, "
            "discussions, parent and all prior history."
        ),
        llm_assisted=True, timestamp="2026-10-05T17:18:00Z",
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not TARGET.exists() or not PROPOSAL.exists():
        raise SystemExit("Missing reviewed record or proposal preimage")
    before = original.build_neighbor(original.neighbor_preimage())
    after = build_record()
    if yaml.safe_load(TARGET.read_text()) not in (before, after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    proposal = original.autogamy_writer.proposal_tsv(after)
    if PROPOSAL.read_text() not in (original.autogamy_writer.proposal_tsv(before), proposal):
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
