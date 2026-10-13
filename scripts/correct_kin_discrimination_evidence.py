"""Correct the initial kin-discrimination evidence with guarded provenance (#1909, #1910)."""

from __future__ import annotations

import argparse
import copy
import tempfile
from pathlib import Path

import yaml

import add_kin_discrimination_trait as initial
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = initial.ROOT
TARGET = initial.TARGET
PARENT_PATH = initial.PARENT_PATH
PROPOSAL = initial.PROPOSAL
TIMESTAMP = "2026-10-13T09:17:32Z"
DEFINITION_SOURCE = "DOI:10.1128/mBio.00723-17"


def build_record() -> dict:
    record = copy.deepcopy(initial.build_record())
    record["definition_source"] = DEFINITION_SOURCE
    record["evidence"][1]["reference"] = "DOI:10.1073/pnas.1512671112"
    record["evidence"][1]["snippet"] = (
        "Some swarms did merge, and most interestingly, this behavior was only "
        "seen in the most highly related strain pairs."
    )
    record["evidence"][2]["snippet"] = (
        "The effects of kin discrimination extend to nearby species, as the "
        "other subtilis clade species were treated with the same antagonism "
        "as nonkin."
    )
    record["evidence"][2]["notes"] = (
        "Lyons and Kolter 2017, PMID:28679746, PMC5573675; scientific abstract, "
        "NLM version 1 PDF page 1 and JATS article-meta abstract without "
        "abstract-type. This is not the separate IMPORTANCE summary. "
        "Introduction distinguishes preferential kin association from nonkin "
        "exclusion and supports the definition's two modes; the paper's own "
        "experiments support the nearby-species extension. The comparison "
        "concerns interactions with B. subtilis NCIB3610: nearby species can "
        "be antagonized, while more distant lineages show varied outcomes. "
        "This is not a universal monotonic relation between distance and "
        "antagonism. Relatedness uses type-strain 16S, not whole-genome "
        "identity of every isolate. Swarm, biofilm and halo assays differ "
        "in medium and endpoint. Figure 2A and 2C assign WNC032 to different "
        "species; Data Set S1 identifies it as B. megaterium. No silent "
        "panel correction or taxon anchor is inferred. Actual Figures 2 "
        "and 4 and selected spreadsheet rows/totals were inspected, not "
        "all figures or raw assays. Native abstract verifier: VERIFIED. "
        "Shares an investigator with 2015; not an independent-laboratory "
        "replication."
    )
    old = "the excerpt is from Results, not either abstract."
    new = "the corrected excerpt is from the scientific abstract, not IMPORTANCE."
    rationale = record["discussions"][1]["rationale"]
    assert rationale.count(old) == 1
    record["discussions"][1]["rationale"] = rationale.replace(old, new)
    record_curation_event(
        record, curator="codex", action="EVIDENCE_CORRECTED",
        changes=(
            "Addressed adversarial findings #1909 and #1910: replaced two "
            "source-matching but insufficiently self-contained excerpts with "
            "explicit swarm-merging and antagonism results. Changed sole "
            "definition authority to Lyons 2017 for the attributed nearby-species "
            "extension, preserving the explicit Stefanic 2015 evidence DOI. "
            "Updated section and native-verifier notes. Original event, phenotype "
            "definition, identifiers, parent, PROPOSED status and remaining "
            "source limits are preserved. Timestamp is observed correction "
            "decision time, not an estimated write time."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in initial.PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    before, after = initial.build_record(), build_record()
    if not TARGET.exists() or yaml.safe_load(TARGET.read_text()) not in (before, after):
        raise SystemExit("Existing target differs from reviewed correction preimage")
    expected, proposal = initial.proposal_tsv(before), initial.proposal_tsv(after)
    if not PROPOSAL.exists() or PROPOSAL.read_text() not in (expected, proposal):
        raise SystemExit("Existing proposal differs from reviewed correction preimage")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(after, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(after, TARGET)
        PROPOSAL.write_text(proposal)
    print("Applied correction" if args.apply else "Validated correction dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
