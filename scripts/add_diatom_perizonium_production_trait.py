"""Add source-bounded diatom perizonium production through the validated writer."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "diatom_perizonium_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/biomineralization.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v569/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000693"
METPO_ID = "METPO:1064600"
PARENT_ID = "traitmech:000690"
PARENT_METPO_ID = "METPO:1000059"
BIDDULPHIA = "DOI:10.1371/journal.pone.0272778"
PLAGIOGRAMMACEANS = "DOI:10.1371/journal.pone.0181413"
TABULARIA = "DOI:10.1016/j.ejop.2013.06.002"
TIMESTAMP = "2026-10-10T23:15:32Z"
PARENT = {
    "identifier": PARENT_ID,
    "label": "biomineralization",
    "definition": (
        "A physiological phenotype in which a microbe mediates the formation of mineral phases."
    ),
    "definition_source": "DOI:10.1016/j.crte.2010.09.002",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "diatom perizonium production",
    "definition": (
        "A biomineralization phenotype in which a diatom produces the siliceous "
        "band system called the perizonium in an auxospore wall."
    ),
    "definition_source": BIDDULPHIA,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": BIDDULPHIA,
            "snippet": (
                "The deposition of the primary TP band became evident when the "
                "auxospore center attained a slim and rigid appearance."
            ),
            "notes": (
                "Kaczmarska et al. 2022, PMID:36067191, PMC9447881, Results: "
                "Epizonium and perizonium. TP means transverse perizonium. "
                "Scientific Abstract, Introduction, Methods, early Results, this "
                "subsection and Discussion: Auxospore structure and development "
                "read in official Europe PMC XML on 2026-10-10; actual Figure 11 "
                "inspected. Other actual figures and S1 Appendix unread. "
                "EXT_ID:36067191 AND SRC:MED confirmed ID, title, DOI and "
                "scientific abstract. Clone HK328 (= ECT3902) originated from "
                "Florida Bay material in 2011; atypical morphology and prolonged "
                "cultivation limit canonical assignment. PDMPO labels silica "
                "deposited after addition. SEM resolves inner TP/LP bands apart "
                "from initial valves; fixed images do not establish live "
                "kinetics. Authors leave some epizonium/perizonium layer "
                "boundaries uncertain. Scaly-band architecture and proposed "
                "shape control are not universal or demonstrated necessities."
            ),
        },
        {
            "reference": PLAGIOGRAMMACEANS,
            "snippet": (
                "transverse perizonial bands produced all together or in quick "
                "succession rather than being added to the auxospore apex one at a time"
            ),
            "notes": (
                "Kaczmarska et al. 2017, PMID:28813426, PMC5558960, scientific "
                "Abstract; EXT_ID:28813426 AND SRC:MED confirmed identity. "
                "Abstract, Methods prose, Results: Auxospore wall fine structure, "
                "related Discussion paragraphs and actual Figure 5 read on "
                "2026-10-10. Table 1/2 headers, footnotes and StA:7/8 and "
                "Van5:5/6 rows inspected; other rows not fully interpreted. "
                "Other actual figures and supplements unread. Fixed stages "
                "support the authors' inferred collapsible-cup sequence, not "
                "a live secretion time course. No longitudinal perizonia found "
                "under their structural criterion; initial epivalves must be "
                "distinguished. Discussion retains the Tabularia fasciculata "
                "study (reference 100); reinterpretation targets other papers. "
                "Aged small cultures, original isolates and progeny are distinct; "
                "culture abnormalities do not define canonical morphology."
            ),
        },
        {
            "reference": TABULARIA,
            "snippet": (
                "Silica precipitation began throughout the auxospore at or near "
                "maximal length, but initially was detectable in isolated regions "
                "throughout the structure."
            ),
            "notes": (
                "Mather et al., online 2013-08-22, 2014 issue, PMID:23972513. "
                "Complete scientific Abstract directly read in official Europe "
                "PMC CORE on 2026-10-10 using EXT_ID:23972513 AND SRC:MED; one "
                "exact MED result with matching ID, title and DOI. Tabularia "
                "fasciculata under the source name lacked transverse perizonium; "
                "longitudinal deposition preceded initial valves near maximal "
                "auxospore length. Undetectable silicon by EDS is not absolute "
                "absence. Publisher full text unavailable; Methods, actual "
                "figures and supplements unread. These three primary studies "
                "have overlapping authors, not independent-laboratory replication."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "diatom-perizonium-production-scope-and-mappings",
            "prompt": "Resolve exact mappings without conflating auxospore wall components.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Biomineralization traitmech:000690 is strictly broader. This "
                "is production, not a material band, inherited band possession, "
                "silica uptake, or auxosporulation alone. Incunabular scales, "
                "epizonium, initial valve/girdle frustules and setae are not "
                "automatically this endpoint. Scaly bands in mediophytes do "
                "not justify universal parenting to siliceous scale production. "
                "Existing frustule/seta boundary notes are not unresolved exact "
                "perizonium groundings. No requirement for both transverse and "
                "longitudinal bands, a single geometry, one-at-a-time secretion, "
                "deposition during expansion, or sexual origin is imposed. "
                "No organism-level disjointness or fitness effect is asserted. "
                "Exact synonyms, properizonium terminology and external "
                "phenotype equivalences remain unasserted pending authority "
                "review; structure terms are not automatically phenotype xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "diatom-perizonium-production-exemplars-and-mechanisms",
            "prompt": "Resolve canonical study material and formation-specific causal evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned: source clone origins were "
                "read, but current taxonomy and figure-to-mating-pair attribution "
                "need reconciliation, including atypical or aged cultures. "
                "Keep mineral deposition, band patterning and shape control "
                "separate. Static microscopy, PDMPO/EDS observations and "
                "sequence features alone do not establish a conserved causal "
                "protein mechanism or necessity for shape control. Protein "
                "edges require functional evidence and taxon-paired accessions. "
                "Mechanism is deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added diatom perizonium production beneath biomineralization with "
            "three primary DOI citations and directly checked short snippets. "
            "Ignored-and-hidden main/worktree/open-PR reservation checks support "
            "000693 and v569 block 1064600-1064699. Existing trait records "
            "unchanged; mappings, canonical taxa and mechanisms remain open. "
            "Timestamp records the observed UTC curation decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Local parent biomineralization; request subclass of v566 METPO:1064300 on adoption.",
         IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
