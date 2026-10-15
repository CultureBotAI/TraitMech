"""Add the source-bounded microbial eukaryotic flagellar-autotomy phenotype."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/eukaryotic_flagellar_autotomy.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v606/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v607/metpo_proposal_classes_robot.tsv"
SOURCE_SHA256 = "8ed5281bf51e818afa9a78b24582122b1b67cf85e26cc9e95ab5a6e3ea044609"
IDENTIFIER = "traitmech:000731"
METPO_ID = "METPO:1068400"
TIMESTAMP = "2026-10-15T07:50:51Z"
RECORD = {
    "identifier": "traitmech:000731",
    "label": "eukaryotic flagellar autotomy",
    "definition": (
        "A physiological phenotype in which a microbial eukaryote sheds its cilia or flagella by "
        "regulated severing of their axonemes near the base."
    ),
    "definition_source": "DOI:10.1186/1471-2121-4-11",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [
        "METPO:1000059",
    ],
    "evidence": [
        {
            "reference": "DOI:10.1186/1471-2121-4-11",
            "snippet": "fla10 cells lose flagella by deflagellation at 33 degrees C.",
            "notes": (
                "Parker and Quarmby 2003, PMID:12930563, PMCID:PMC194436, scientific abstract "
                "Results, second sentence. Direct MED text match; native VERIFIED applies to that "
                "text, not the PDF degree-symbol typography. Background distinguishes basal "
                "axonemal severing from resorption. The quoted response concerns source-named "
                "Chlamydomonas fla10 in calcium-containing medium, not reference strain WTB214. "
                "Released flagella were counted per 100 cells, with the initial count subtracted; "
                "lengths are a separate endpoint. Low calcium is not calcium-free, and buffer "
                "exchange is a confound. All twelve main PDF pages and eight figures were "
                "inspected. No universal IFT or calcium requirement follows."
            ),
        },
        {
            "reference": "DOI:10.1534/g3.116.034264",
            "snippet": (
                "Wild-type cells deflagellate completely in response to pH shock or dibucaine, "
                "regardless of the temperature"
            ),
            "notes": (
                "Hilton et al. 2016, PMID:27520959, PMCID:PMC5068960.1, page 3416, Results and "
                "Discussion subsection ADF2 and ADF4 remain unassigned, first paragraph and "
                "Figure 4A. Contiguous JATS and typeset match; native NOT_IN_ABSTRACT retained. "
                "The comparison is 21 versus 33 degrees C after six hours, not every temperature. "
                "The assay scores the control-normalized decrease in biflagellate cells per 100 "
                "cells, not a direct count of released flagella or proof that every responding "
                "cell loses both. Figure 4A reports three independent experiments with SD. All "
                "ten main pages, four figures and three tables were inspected; supplements remain "
                "unread. Phototaxis screening alone is not the shedding endpoint."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "eukaryotic-flagellar-autotomy-scope",
            "prompt": "Review the basal axonemal shedding endpoint and its phenotype parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This organism-level phenotype concerns regulated release of a eukaryotic cilium "
                "or flagellum, not possession, arrangement, assembly failure or nonmotility. "
                "Resorption, retained-organelle disassembly, passive breakage, distal vesicle "
                "release and premitotic basal-body release alone do not establish the endpoint. "
                "Bacterial flagellar ejection or resorption involves a different apparatus and is "
                "outside this qualified class. The phenotype parent METPO:1000059 is a "
                "definition-based inference; motility is not a required parent. Palmelloid "
                "formation traitmech:000654 does not require flagellar loss. No exact synonyms, "
                "organism-level disjointness or universal stimulus threshold are asserted."
            ),
        },
        {
            "discussion_id": "eukaryotic-flagellar-autotomy-metpo",
            "prompt": "Review current ontology scope without reviving obsolete morphology identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The inspected pinned and current METPO release/editor/template scope has no "
                "active exact shedding class. Historical METPO:0000089 and METPO:000090 are "
                "deprecated with OMO:0001000; METPO:1000381 is deprecated with IAO:0000226. All "
                "point to METPO:1000704, which denotes locomotory flagellar possession, not "
                "autotomy. Deprecated ciliated METPO:0000093 and METPO:000094 carry OMO:0001000, "
                "while METPO:1000385 carries IAO:0000226; no replacement or consider annotation "
                "was observed for these or deprecated flagellum METPO:1000123, whose recorded "
                "reason is OMO:0001000. Those historical morphology terms are not exact xrefs and "
                "are not reactivated. METPO issue https://github.com/berkeleybop/metpo/issues/521 "
                "records unresolved reason-code interpretation. Current upstream describes a "
                "bacterial/archaeal focus, so adoption of this microbial-eukaryote proposal "
                "requires maintainer review. The ontology pin stays unchanged. Proposal v607 "
                "reserves METPO:1068400 within 1068400-1068499; no upstream release or human "
                "sign-off is implied."
            ),
        },
        {
            "discussion_id": "eukaryotic-flagellar-autotomy-mechanism",
            "prompt": (
                "Keep the shedding phenotype separate from universal katanin or sequence-based "
                "mechanism claims."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A protein-resolved graph requires taxon-paired authority-checked accessions and "
                "edge-specific experiments. Domain, motif, gene or mutant names alone do not "
                "establish the organismal phenotype. The p60 study constrains a proposed "
                "universal severing mechanism; it does not establish dispensability of every "
                "katanin function. No universal FA1, FA2, TRP15, IFT or calcium requirement is "
                "asserted. Mechanisms are deferred, not claimed absent."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1242/jcs.096941",
                    "reference_title": (
                        "PF19 encodes the p60 catalytic subunit of katanin and is required for "
                        "assembly of the flagellar central apparatus in Chlamydomonas"
                    ),
                    "supports": "SUPPORT",
                    "evidence_source": "full_text",
                    "snippet": "microtubule severing activity of p60 is not required for deflagellation",
                    "explanation": (
                        "Supports the bounded mechanistic limitation, not an additional "
                        "definition citation or a claim that every katanin function is "
                        "dispensable."
                    ),
                    "notes": (
                        "Dymek and Smith 2012, PMID:22467860, PMCID:PMC3516377, Discussion "
                        "subsection Is katanin required for flagellar excision in Chlamydomonas? "
                        "Direct HTML match; native NOT_IN_ABSTRACT retained. Main text and all "
                        "six figures were inspected; supplements were not. Figure 5A assays "
                        "cellular shedding; Figure 2 assays purified protein. Transcript "
                        "knockdown is not verified protein depletion. The reference A54-e18 "
                        "carries listed mutations, and the tested mutants are not nulls."
                    ),
                },
            ],
        },
        {
            "discussion_id": "eukaryotic-flagellar-autotomy-provenance",
            "prompt": "Resolve strain provenance and preserve source-access limits before adding canonical taxa.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Study organism and strain names remain qualified observations, not canonical "
                "taxon assertions. Distinct papers from the Quarmby group are not "
                "independent-laboratory replication. MED/Crossref fields and available "
                "PubMed/publisher records were checked for notices; this is not comprehensive "
                "correction/retraction clearance. Publisher DOI requests failed in the follow-up, "
                "some PMC requests returned challenge pages, and the 2003 PubMed page yielded no "
                "usable text. Those failures do not negate earlier directly retrieved primary "
                "materials, but are not successful source checks. The 2016 supplementary index "
                "digest mismatch remains recorded; nine substantive assets matched supplied "
                "digests. No paid research, human sign-off or raw-data reanalysis is implied."
            ),
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    for discussion in record["discussions"]:
        discussion.update(posed_by="codex", posed_date=TIMESTAMP[:10])
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added the microbial eukaryotic basal-axoneme shedding phenotype with "
            "two primary DOI sources and directly checked 10/15-word snippets. "
            "Retained native VERIFIED and NOT_IN_ABSTRACT outcomes respectively, "
            "plus separate 10-word full-text mechanism-limitation evidence with "
            "native NOT_IN_ABSTRACT. Reserved 000731, v607 and 1068400-1068499 "
            "after ignored/hidden current-file, retained-history, full-range and "
            "open/draft PR checks. No obsolete identifier, canonical taxon, exact "
            "mapping or universal protein requirement is inferred. The timestamp "
            "records observed acceptance, not a reconstructed acquisition time."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    raw = SOURCE_PROPOSAL.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise SystemExit("Historical template dependency differs")
    headers = list(csv.reader(io.StringIO(raw.decode()), delimiter="\t"))[:2]
    if len(headers) != 2 or any(len(row) != 11 for row in headers):
        raise SystemExit("Unexpected class-template layout")
    rows = headers + [[
        METPO_ID, record["label"], record["definition"],
        "TraitMech:data/traits/physiology/eukaryotic_flagellar_autotomy.yaml|"
        + record["definition_source"],
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "MEDIUM", "", IDENTIFIER,
    ]]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as temporary:
        write_validated_trait(record, Path(temporary) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
