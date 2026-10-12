"""Qualify the historical reporter readout without rewriting earlier observations."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import tempfile
from pathlib import Path

import yaml

import add_unequal_protein_aggregate_inheritance_trait as initial
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / f"data/traits/physiology/{initial.SLUG}.yaml"
SIDECAR = ROOT / f"research/traits/physiology/{initial.SLUG}-source-verification.json"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv"
TIMESTAMP = "2026-10-12T18:24:02Z"
ISSUE = "https://github.com/CultureBotAI/TraitMech/issues/1896"
EXPECTED_SOURCE_HASH = "6a258129cd8b2248432cfa02af1e65158891b34c4cd4b5474b9f6b11841561dd"
SOURCE = "DOI:10.1371/journal.pbio.2003853"
SOURCE_HASH = "f5e8ed02e307d9153f512ea747a9a0c109eb9ac4b7bc4070a68cb7aba82cdd91"
OLD = (
    "The observations support inheritance and eventual older-pole accumulation; "
    "they do not establish active transport, universal aggregate toxicity or a "
    "natural canonical exemplar."
)
NEW = (
    "These observations describe reporter-focus inheritance and eventual older-pole "
    "accumulation. Govers et al. 2018 (DOI:10.1371/journal.pbio.2003853) subsequently "
    "demonstrated label-induced clustering with IbpA-YFP. The older readout is not "
    "independent proof of endogenous unstressed aggregation; naming the engineered "
    "strain alone does not resolve this assay bias. Neither active transport, "
    "universal aggregate toxicity nor a natural canonical exemplar is established."
)
ADDED_EVIDENCE = {
    "reference": SOURCE,
    "snippet": (
        "the polarly deposited PA was subjected to limited disaggregation and "
        "therefore became asymmetrically inherited for a large number of generations"
    ),
    "notes": (
        "Govers et al. 2018, PMID:30153247, PMC6112618; scientific abstract, "
        "directly matched in primary XML and source-qualified MED. Results on "
        "reporter validation and post-stress inheritance, relevant Methods and "
        "actual Figures 1 and 3 were inspected. Figure 1 shows reporter-dependent "
        "clustering; Figure 3 separately follows engineered MG1655 IbpA-msfGFP "
        "lineages after 47 C for 15 minutes, with microscopy at 37 C. Focus "
        "inheritance is distinct from the fluorescence concentration and growth "
        "readouts. This does not validate unstressed IbpA-YFP foci as endogenous "
        "aggregates or imply universal harm, benefit, aging or rejuvenation. "
        "Supplementary controls were read only where described in Results; their "
        "images, raw data and independent strain provenance were not assessed."
    ),
}


def digest(document: dict) -> str:
    serialized = json.dumps(document, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def build_record() -> dict:
    record = initial.build_record()
    notes = record["evidence"][0]["notes"]
    assert notes.count(OLD) == 1
    record["evidence"][0]["notes"] = notes.replace(OLD, NEW)
    record["evidence"].append(copy.deepcopy(ADDED_EVIDENCE))
    record["discussions"][1]["rationale"] += (
        " Reporter-focus inheritance must be separated from endogenous aggregation: "
        "the later Govers study identifies IbpA-YFP label-induced clustering, while "
        "its separate post-heat-shock IbpA-msfGFP lineages support inheritance. "
        "Monomeric labels also require validation of expression level and assay "
        "conditions; no reporter is declared universally artifact-free."
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_REPORTER_EVIDENCE",
        changes=(
            "Addressed issue #1896 by qualifying the Lindner reporter-focus "
            "readout against later primary evidence of IbpA-YFP label-induced "
            "clustering. Added Govers 2018 with a checked abstract snippet and "
            "separate post-stress inheritance context. Preserved identity, "
            "definition, parent, PROPOSED status, original event and source "
            "assessment; appended the correction and updated the proposal sources. "
            "Timestamp is the observed UTC correction decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def corrected_sidecar(document: dict) -> dict:
    if not isinstance(document, dict):
        raise SystemExit("Source sidecar differs from reviewed preimage")
    base = copy.deepcopy(document)
    prior = base.pop("assessment_corrections", None)
    if digest(base) != EXPECTED_SOURCE_HASH:
        raise SystemExit("Source sidecar differs from reviewed preimage")
    correction = {
        "timestamp": TIMESTAMP, "issue": ISSUE,
        "supersedes_fields": ["evidence_assessment.rows[0].notes", "curation_decision"],
        "scope": "Supersedes the earlier unqualified role of Lindner reporter foci, not the trait identity or historical access record.",
        "corrected_lindner_notes": build_record()["evidence"][0]["notes"],
        "added_evidence": copy.deepcopy(ADDED_EVIDENCE),
        "source_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6112618/fullTextXML",
        "source_sha256": SOURCE_HASH,
        "snippet_locator": "article/front/article-meta/abstract/p",
        "exact_contiguous_span": True,
        "source_identity_verified": True,
        "source_read_scope": "Scientific abstract; Results sec003, sec004 and sec006; Methods sec014, sec017, sec018 and sec021; actual Figures 1 and 3.",
        "asset_sha256": {
            "govers2018-fig1.jpg": "99fdddddb8373d93b160592c81bcd434671c58f59b7cf384ef9d550ccaf84049",
            "govers2018-fig3.jpg": "e0a41254543cb169e496e0cc8c574a3121ea5267c7c1568ee47164f2d4546923",
            "govers2018-med.json": "a8f643fb6d29621b0a2a59701628aaab28e03b4ddb60302b088f3a2c0b8085b5",
            "govers2018-crossref.json": "901023743207950e794835b377cf0e30994c84171659e38e0ad550c71e4e1525",
        },
        "asset_root": "/tmp/traitmech-aggregate-inheritance-reporter-review-20261012",
        "notice_scope": "Source-qualified MED and Crossref identity/notice fields plus accessible publisher article checked on 2026-10-12; no linked correction/retraction exposed by these bounded checks. This is not an exhaustive notice search or a retraction claim about Lindner.",
        "limits": "Supplementary images/movies, numerical data, independent strain provenance and all unlisted figures were not assessed; no universal reporter validity, harm or benefit claim.",
    }
    if prior is not None and prior != [correction]:
        raise SystemExit("Existing sidecar correction differs from reviewed result")
    base["assessment_corrections"] = [correction]
    return base


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    current = yaml.safe_load(TARGET.read_text())
    record = build_record()
    if current != initial.build_record() and current != record:
        raise SystemExit("Existing trait differs from reviewed preimage or result")
    sidecar = corrected_sidecar(json.loads(SIDECAR.read_text()))
    proposal = initial.proposal_tsv(record)
    if PROPOSAL.read_text() not in (initial.proposal_tsv(initial.build_record()), proposal):
        raise SystemExit("Existing proposal differs from reviewed preimage or result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        SIDECAR.write_text(json.dumps(sidecar, indent=2) + "\n")
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
