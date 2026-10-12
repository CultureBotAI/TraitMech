"""Require environment-independent state interconversion in bet hedging (#1888)."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

import yaml

import add_diversifying_bet_hedging_trait as original
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = original.TARGET
PROPOSAL = original.PROPOSAL
PARENT_PATH = original.PARENT_PATH


def build_record() -> dict:
    record = original.build_record()
    record["definition"] = (
        "A physiological phenotype in which a clonal microbial lineage reversibly "
        "interconverts between alternative cell states independently of the "
        "prevailing environment and before environmental change, spreading risk "
        "across unpredictable environmental changes through state-specific "
        "survival or reproductive trade-offs."
    )
    record["discussions"][0]["rationale"] += (
        " Following Levy et al. Box 1, the relevant state interconversion must "
        "be independent of the prevailing environment; temporal precedence "
        "alone does not establish this criterion. Cue-triggered preparation "
        "before a later change is not sufficient. Deterministic age-related "
        "variation can qualify, so environmental independence is not a "
        "requirement for a purely stochastic switching mechanism."
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_TRAIT_SCOPE",
        changes=(
            "Addressed #1888: made reversible environment-independent state "
            "interconversion explicit in the definition and scope discussion, "
            "following Levy et al. Box 1. Temporal precedence alone is "
            "insufficient; purely stochastic or binary switching is not "
            "required. Preserved evidence and original provenance. Timestamp "
            "is the observed UTC correction decision."
        ),
        llm_assisted=True, timestamp="2026-10-12T07:04:27Z",
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
