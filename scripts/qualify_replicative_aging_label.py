"""Qualify the aging label to match the decline-based phenotype (#1891)."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

import yaml

import add_replicative_aging_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.TARGET
PROPOSAL = original.PROPOSAL
PARENT_PATH = original.PARENT_PATH
LABEL = "replicative aging with functional decline"


def build_record() -> dict:
    record = original.build_record()
    record["label"] = LABEL
    scope = record["discussions"][0]
    scope["prompt"] = "Assess remaining upstream terminology for the explicitly decline-qualified phenotype."
    scope["rationale"] = scope["rationale"].replace(
        "Upstream review should assess that label boundary; no exact synonym or external xref is asserted.",
        "The label is now explicitly qualified as replicative aging with functional "
        "decline (#1891); bare replicative aging is not asserted as an exact "
        "synonym. Upstream review should assess remaining terminology and "
        "hierarchy choices; no external xref is asserted.",
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_TRAIT_LABEL",
        changes=(
            "Addressed #1891 by qualifying the record and v585 proposal label "
            "as replicative aging with functional decline. Preserved the "
            "definition, evidence, identifier and original provenance; retained "
            "the broader healthy-aging usage as an attributed distinction, "
            "not an exact synonym. Timestamp is the observed UTC correction decision."
        ),
        llm_assisted=True, timestamp="2026-10-12T10:28:34Z",
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in original.PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    if not TARGET.exists() or not PROPOSAL.exists():
        raise SystemExit("Missing reviewed record or proposal preimage")
    before = yaml.safe_load(TARGET.read_text())
    after = build_record()
    if before not in (original.build_record(), after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    proposal = original.proposal_tsv(after)
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
