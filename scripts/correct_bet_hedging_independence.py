"""Correct the inverted independence/stochasticity implication (#1890)."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

import yaml

import qualify_bet_hedging_scope as previous
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = previous.TARGET
PROPOSAL = previous.PROPOSAL
PARENT_PATH = previous.PARENT_PATH
OLD_CLAUSE = "environmental independence is not a requirement for a purely stochastic switching mechanism."
NEW_CLAUSE = "environmental independence does not require a purely stochastic switching mechanism."


def build_record() -> dict:
    record = previous.build_record()
    rationale = record["discussions"][0]["rationale"]
    if rationale.count(OLD_CLAUSE) != 1:
        raise ValueError("Expected exactly one reviewed inverted clause")
    record["discussions"][0]["rationale"] = rationale.replace(OLD_CLAUSE, NEW_CLAUSE)
    record_curation_event(
        record, curator="codex", action="CORRECTED_SCOPE_WORDING",
        changes=(
            "Addressed external review #1890: corrected the inverted implication "
            "in the first scope discussion. Environment-independent "
            "interconversion remains required; a purely stochastic mechanism "
            "is not required, consistent with Levy et al. Box 1. Preserved the "
            "definition, evidence, proposal definition and both previous events. "
            "Timestamp is the observed UTC correction decision."
        ),
        llm_assisted=True, timestamp="2026-10-12T08:09:20Z",
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in previous.original.PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    if not TARGET.exists() or not PROPOSAL.exists():
        raise SystemExit("Missing reviewed record or proposal preimage")
    before = yaml.safe_load(TARGET.read_text())
    after = build_record()
    if before not in (previous.build_record(), after):
        raise SystemExit("Existing record differs from reviewed preimage or result")
    if PROPOSAL.read_text() != previous.original.proposal_tsv(after):
        raise SystemExit("Existing proposal differs from reviewed definition")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(after, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(after, TARGET)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
