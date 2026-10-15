"""Add the source-bounded microbial eukaryotic flagellar-resorption phenotype."""

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
TARGET = ROOT / "data/traits/physiology/eukaryotic_flagellar_resorption.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v608/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v609/metpo_proposal_classes_robot.tsv"
SOURCE_SHA256 = "24a186fd10b1bd4c4729e86197cc7b5ab4824df57422912fce0bb8e55ca1f529"
IDENTIFIER = "traitmech:000733"
METPO_ID = "METPO:1068600"
TIMESTAMP = "2026-10-15T16:01:11Z"
REPLICATION_CORRECTION_TIMESTAMP = "2026-10-15T17:05:25Z"
RECORD = {
    "identifier": IDENTIFIER,
    "label": "eukaryotic flagellar resorption",
    "definition": (
        "A physiological phenotype in which a microbial eukaryote shortens previously "
        "assembled cilia or flagella through disassembly of their axonemes."
    ),
    "definition_source": "DOI:10.1083/jcb.100.2.457",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1083/jcb.100.2.457",
            "snippet": "Cells under resorption-inducing conditions rapidly shortened their flagella",
            "notes": (
                "L'Hernault and Rosenbaum 1985, PMID:3968171, PMCID:PMC2113451.1, printed page "
                "458, Results, Monitoring of Flagellar Length during In Vivo Labeling, sole "
                "paragraph; Figure 2 on page 459. Contiguous typeset and whitespace-normalized "
                "OCR match; native NOT_IN_ABSTRACT retained. The XML body is a single OCR "
                "preformat block, not a section-structured JATS paragraph. Source-designated "
                "wild-type Chlamydomonas reinhardtii 21gr was mechanically deflagellated and "
                "pulse-chase labelled during regeneration before resorption was induced with "
                "15 mM sodium pyrophosphate at pH 7.5 plus cycloheximide; HEPES was the control. "
                "The shortening concerns regenerated flagella, not failed assembly. Apparent "
                "flagellalessness after 90 minutes still permits the reported short stubs. "
                "Protein fractionation supports transfer to the cell body, not complete "
                "recycling. All six main PDF pages, three figures and Table I were inspected; "
                "raw data were not reanalyzed. Figure 1's two determinations and Table I's two "
                "gels per sample are not established biological-replicate counts."
            ),
        },
        {
            "reference": "DOI:10.1186/1471-2121-4-11",
            "snippet": "Acid shock causes resorption of mutants unable to deflagellate.",
            "notes": (
                "Parker and Quarmby 2003, PMID:12930563, PMCID:PMC194436, Figure 7 caption, "
                "first sentence, page 9 of 12; JATS F7 under sec9/sec5. Direct caption and "
                "typeset match; native NOT_IN_ABSTRACT retained. The acid-shock experiments "
                "concern Chlamydomonas fa1, fa2 and adf1 mutants, with coiling and incomplete "
                "resorption described; wild-type cells instead shed and regrow their flagella "
                "in this comparison. Figure 7 scores the fraction of cells with flagella "
                "longer than 7 micrometers, not a resorption rate or count of released "
                "organelles. The separate fla10 temperature experiments must not be merged "
                "with this assay. Low-calcium HEPES is not calcium-free: Methods retain trace "
                "calcium and do not add chelators. The main length measurements count at least "
                "70 cells per time point and use at least three independent cultures. All twelve main "
                "PDF pages and eight figures were inspected. Proposed basal disassembly and "
                "shared severing machinery are not universal requirements of this class."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "eukaryotic-flagellar-resorption-scope",
            "prompt": "Review shortening through disassembly without requiring complete disappearance.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This physiological phenotype concerns shortening of a previously assembled "
                "eukaryotic axoneme. Static short flagella, failed assembly, nonmotility, "
                "bending or coiling, passive breakage, or shedding a largely intact organelle "
                "alone do not establish it. Neither complete structural disappearance nor "
                "complete protein recycling is required. Basal severing and residual transition "
                "zones can accompany resorption; the class does not require an intact base or "
                "the absence of severing. Eukaryotic flagellar autotomy traitmech:000731 and "
                "bacterial polar flagellar ejection traitmech:000732 have different endpoints. "
                "Bacterial periplasmic resorption involves a different apparatus. No "
                "organism-level disjointness is asserted. Phenotype METPO:1000059 is the "
                "definition-based parent; locomotion is not required. Palmelloid formation "
                "traitmech:000654 does not require flagellar loss."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1002/cm.20454",
                    "reference_title": "Centrioles are freed from cilia by severing prior to mitosis.",
                    "supports": "SUPPORT",
                    "evidence_source": "abstract",
                    "snippet": (
                        "resorbing flagella of Chlamydomonas leave remnants associated with "
                        "the mother cell wall."
                    ),
                    "explanation": (
                        "Supports the remnant/scope limitation, not an additional definition "
                        "citation, a universal severing mechanism or complete recycling."
                    ),
                    "notes": (
                        "Parker et al. 2010, PMID:20506243, PMCID:PMC2897710.1, scientific "
                        "abstract, JATS paragraph P2, third sentence. Direct JATS and MED "
                        "scientific-abstract matches; native VERIFIED retained. Main text, "
                        "Methods, Results, Discussion, Conclusions and three captions were "
                        "read, not the actual figures, PDF, supplementary video, supplementary "
                        "legend or raw data. Live pf6 CC1029 observations and wild-type 137c "
                        "mt- CC124 electron microscopy concern different preparations. Paired "
                        "spots in daughter-cell clusters are not a flagellar-resorption rate. "
                        "Remnants may remain in the wall or be expelled; do not universalize "
                        "this premitotic context to every resorption stimulus."
                    ),
                },
            ],
        },
        {
            "discussion_id": "eukaryotic-flagellar-resorption-metpo",
            "prompt": "Review microbial-eukaryote scope without reviving obsolete morphology identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The inspected pinned/current METPO releases, editor and templates have no "
                "active exact resorption class. Historical METPO:0000089 and METPO:000090 "
                "carry OMO:0001000; METPO:1000381 carries IAO:0000226. All are deprecated and "
                "point to active METPO:1000704, which denotes locomotory flagellar possession, "
                "not resorption. Deprecated ciliated METPO:0000093 and METPO:000094 carry "
                "OMO:0001000, while METPO:1000385 carries IAO:0000226; no replacement or "
                "consider annotation was observed for those or deprecated flagellum "
                "METPO:1000123, whose reason is OMO:0001000. Historical terms are not exact "
                "xrefs and are not reactivated. https://github.com/berkeleybop/metpo/issues/521 "
                "records unresolved reason-code interpretation. Upstream's bacterial/archaeal "
                "focus requires maintainer review of this microbial-eukaryote proposal. The "
                "ontology pin stays unchanged. Proposal v609 reserves METPO:1068600 in "
                "1068600-1068699; neither upstream release nor human sign-off is implied."
            ),
        },
        {
            "discussion_id": "eukaryotic-flagellar-resorption-mechanism",
            "prompt": "Keep the phenotype separate from universal disassembly or sequence-based mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The studies discuss different models of axonemal disassembly. Do not require "
                "a universal tip-to-base direction, basal severing site, tubulin modification, "
                "IFT defect, calcium threshold, stimulus or cell-cycle transition. Induced "
                "and mutant observations support the phenotype without becoming natural "
                "canonical exemplars. A protein-resolved graph requires taxon-paired "
                "authority-checked accessions and edge-specific experiments. A gene, domain, "
                "motif or sequence profile alone does not establish organelle resorption. "
                "Mechanisms are deferred, not claimed absent. No exact synonyms or mappings "
                "are asserted."
            ),
        },
        {
            "discussion_id": "eukaryotic-flagellar-resorption-provenance",
            "prompt": "Resolve strain provenance and preserve source-access limits before adding canonical taxa.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Source-designated strain names remain qualified observations; laboratory "
                "wild type is not proof of natural provenance, and a mutant label alone does "
                "not establish genetic engineering. Two distinct supporting publications are "
                "not a claim of independent-laboratory replication. The 2010 context paper "
                "shares authors with the 2003 study and is not a third definition citation. "
                "MED/Crossref identities and available publisher/PubMed notice fields were "
                "checked; this is not comprehensive correction/retraction clearance. Some "
                "publisher, PMC and PubMed attempts failed or returned challenge pages. "
                "Public PMC cloud assets and the directly retrieved 2003 PDF/XML retain "
                "their own successful provenance; failed requests are not relabeled as "
                "successful source checks. No raw-data reanalysis, paid research or human "
                "scientific sign-off is implied."
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
            "Added the microbial eukaryotic axonemal-resorption phenotype with two primary "
            "DOI sources and directly checked 8/9-word full-text snippets, both retaining "
            "native NOT_IN_ABSTRACT. Kept the 12-word remnant-limitation scientific-abstract "
            "excerpt with native VERIFIED in a discussion, not definition evidence. Reserved "
            "000733, v609 and 1068600-1068699 after ignored/hidden current-file, retained-history, "
            "complete-range and open/draft PR checks. No obsolete identifier, canonical taxon, "
            "exact mapping or universal protein mechanism is inferred. The timestamp records "
            "the observed allocation decision after the fresh guard, not source acquisition."
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
        "TraitMech:data/traits/physiology/eukaryotic_flagellar_resorption.yaml|"
        + record["definition_source"],
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "MEDIUM", "", IDENTIFIER,
    ]]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def correct_replication_bound(current: dict) -> dict:
    expected = build_record()
    original = copy.deepcopy(expected)
    original["evidence"][1]["notes"] = original["evidence"][1]["notes"].replace(
        "use at least three independent cultures.", "use three independent cultures."
    )
    corrected = copy.deepcopy(expected)
    record_curation_event(
        corrected, curator="codex", action="CORRECT_EVIDENCE_QUANTITY",
        changes=(
            "Retained at least three independent cultures as the replication lower bound "
            "reported in the 2003 Methods, Timecourses and flagella length measurements, "
            "page 11 of 12. Source XML and the typeset page were rechecked for issue #1948. "
            "Preserved definition, snippets, references, other evidence and prior history."
        ),
        llm_assisted=True, timestamp=REPLICATION_CORRECTION_TIMESTAMP,
    )
    if current == expected or current == corrected:
        return copy.deepcopy(current)
    if current != original:
        raise SystemExit("Existing target differs from reviewed replication-repair input")
    return corrected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--correct-replication-bound", action="store_true")
    args = parser.parse_args()
    if args.correct_replication_bound:
        if not TARGET.is_file():
            raise SystemExit("Replication repair requires the existing target")
        current = yaml.safe_load(TARGET.read_text())
        record = correct_replication_bound(current)
        with tempfile.TemporaryDirectory() as temporary:
            write_validated_trait(record, Path(temporary) / TARGET.name)
        if args.apply and record != current:
            write_validated_trait(record, TARGET)
        print("Applied replication repair" if args.apply else "Validated replication repair dry run")
        return 0
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
