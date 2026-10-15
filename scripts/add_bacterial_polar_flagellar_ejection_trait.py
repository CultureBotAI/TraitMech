"""Add the source-bounded bacterial polar flagellar-ejection phenotype."""

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
TARGET = ROOT / "data/traits/physiology/bacterial_polar_flagellar_ejection.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v607/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v608/metpo_proposal_classes_robot.tsv"
SOURCE_SHA256 = "72af61de0c6d741f00271b48d1656ee47c313fbde38ce953b6cfb81c7a76aae3"
IDENTIFIER = "traitmech:000732"
METPO_ID = "METPO:1068500"
TIMESTAMP = "2026-10-15T11:39:29Z"
LOCATOR_CORRECTION_TIMESTAMP = "2026-10-15T13:07:41Z"
OLD_LOCATOR = "third paragraph; Figure 1G"
SOURCE_LOCATOR = "sole paragraph (HTML anchor article1.body1.sec2.sec4.p1; PDF pp. 4-5); Figure 1G"
RECORD = {
    "identifier": "traitmech:000732",
    "label": "bacterial polar flagellar ejection",
    "definition": "A physiological phenotype in which a bacterium actively ejects previously assembled axial structures of a polar flagellum by separation at its base.",
    "definition_source": "DOI:10.1371/journal.pbio.3000165",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [
        "METPO:1000059"
    ],
    "evidence": [
        {
            "reference": "DOI:10.1371/journal.pbio.3000165",
            "snippet": "Plesiomonas cells consistently lose their flagella at the base of the hook",
            "notes": "Ferreira et al. 2019, PMID:30889173, PMC6424402. Results, Shed hook-filament structures accumulate in P. shigelloides supernatant, " + SOURCE_LOCATOR + ". Direct publisher full-text match; native NOT_IN_ABSTRACT. Hook-bearing released structures, population counts and relic/assembly comparisons support ejection rather than daughter-cell dilution or passive midfilament breakage. Nutrient-depletion conditions vary among assays; minimal medium containing glucose is not complete carbon starvation. All 25 main PDF pages and six figures were inspected, not raw supplementary data. Energy conservation and leakage prevention are interpretations."
        },
        {
            "reference": "DOI:10.1111/mmi.14511",
            "snippet": "bacteria can actively abandon flagella after prolonged stationary culturing",
            "notes": "Zhuang et al. 2020, PMID:32259388, scientific abstract, sentence beginning Interestingly. Direct MED/publisher match and native VERIFIED. Main publisher text and six figure captions were subsequently read, not the actual figures or supplement. Sections 2.4-2.7 separate daughter-cell dilution from stationary-phase shedding. OD times flagellated fraction is a population proxy, not a direct cell count. VIO5 and engineered EGFP-FliG strain NMB344 are distinct; red/green panels in Figure 3 are not the same cells. Two-color experiments in Figures 5-6 support basal release, but rod breakage is inferred, not a directly imaged cut. Surface immobilization and medium exchanges constrain the assay."
        },
        {
            "reference": "DOI:10.1038/s41467-026-75593-6",
            "snippet": "Nutrient depletion significantly increases the frequency of flagellar shedding and the accumulation of closed FOMCs",
            "notes": "Guo et al. 2026, PMID:42660870, PMC13521929.1, Results, Two distinct in situ architectures of the flagellar motor in V. cholerae, and Supplementary Figure 4. Direct JATS match; native NOT_IN_ABSTRACT. FOMC denotes the flagellar outer membrane complex. The quoted experiment uses wild-type V. cholerae; delta-flhG structural samples are distinct. All 12 main PDF pages and six main figures were inspected, plus the actual supplementary Figure 4 and supplementary tables. Its 81/273 observations are cells in the figure caption and tomograms in Methods/Table 4, not biological replicates or ejection rates. The main-text Table 3 pointer instead corresponds to Table 4. Other supplements remain incompletely read."
        }
    ],
    "discussions": [
        {
            "discussion_id": "bacterial-polar-flagellar-ejection-scope",
            "prompt": "Review active basal release separately from possession, loss and resorption.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": "This qualified phenotype requires active basal release of previously assembled polar flagellar axial structures. Hook-filament release is an observed endpoint, not a universal component-completeness requirement. Flagellar possession or arrangement, assembly failure, motor arrest, reduced motility, a decreasing flagellated fraction or passive filament breakage alone do not establish it. Periplasmic resorption and microbial-eukaryotic axonemal autotomy are distinct. Phenotype METPO:1000059 is a definition-based parent inference; locomotory possession is not a required parent. The definition does not require every flagellum to be lost, nonmotility, a particular stimulus, exact severing site, relic morphology or universal behavior among polar-flagellated bacteria. No bare shedding or deflagellation exact synonym is asserted."
        },
        {
            "discussion_id": "bacterial-polar-flagellar-ejection-metpo",
            "prompt": "Review the phenotype hierarchy without reviving retired flagellar identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": "Pinned and current METPO release annotations distinguish motility, locomotory flagellar possession and polar arrangement from ejection. Historical METPO:0000089 and METPO:000090 are deprecated with OMO:0001000; METPO:1000381 is deprecated with IAO:0000226. Their replacement METPO:1000704 denotes possession, not shedding. Deprecated flagellum METPO:1000123 has OMO:0001000 and no observed replacement or consider annotation. These are not exact mappings and are not reactivated. The current editor is an import stub, not a full release. The ontology pin remains unchanged. Proposal v608 reserves METPO:1068500 within 1068500-1068599; the local identifier is traitmech:000732. No upstream release or human sign-off is implied."
        },
        {
            "discussion_id": "bacterial-polar-flagellar-ejection-mechanism",
            "prompt": "Keep organismal ejection separate from universal molecular and sequence claims.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": "The 2026 structures assign closure to FlgI conformational changes in V. cholerae; the 2019 interpretation of an unidentified added plug is not imposed as a universal mechanism. Assembly defects in gate-deletion mutants do not by themselves demonstrate failure of ejection. Cryo-ET states are not a longitudinal trajectory of the same motor. A protein-resolved causal graph needs taxon-paired authority-checked accessions and edge-specific evidence. Gene, motif and domain presence alone do not establish this organism-level phenotype. Mechanisms are deferred, not claimed absent."
        },
        {
            "discussion_id": "bacterial-polar-flagellar-ejection-provenance",
            "prompt": "Resolve assay-specific strain provenance before asserting canonical taxa.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": "Source organism names remain qualified observations, not independently resolved canonical taxon assertions. Engineered structural samples and source-designated wild-type nutrient assays must not be conflated. MED metadata and accessible publisher text were checked; unavailable publisher or PubMed pages are access limits, not evidence that no notice exists. This is not comprehensive correction/retraction clearance, raw-data reanalysis, independent replication, paid research or human sign-off."
        }
    ]
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    for discussion in record["discussions"]:
        discussion.update(posed_by="codex", posed_date=TIMESTAMP[:10])
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added active basal release of assembled bacterial polar flagellar structures "
            "with three primary DOI sources and directly checked 12/9/15-word snippets. "
            "Native NOT_IN_ABSTRACT/VERIFIED/NOT_IN_ABSTRACT remain distinct from "
            "direct full-text checks. Reserved 000732, v608 and 1068500-1068599 after "
            "ignored/hidden current-file, retained-history, complete-range and open/draft "
            "PR checks, including the changed CommunityMech PR2018 worktree. No obsolete "
            "identifier, exact mapping, canonical taxon or universal molecular mechanism "
            "is inferred. Timestamp records observed acceptance, not source acquisition."
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
        "TraitMech:data/traits/physiology/bacterial_polar_flagellar_ejection.yaml|"
        + record["definition_source"],
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "MEDIUM", "", IDENTIFIER,
    ]]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def correct_source_locator(current: dict) -> dict:
    expected = build_record()
    original = copy.deepcopy(expected)
    original["evidence"][0]["notes"] = original["evidence"][0]["notes"].replace(
        SOURCE_LOCATOR, OLD_LOCATOR
    )
    corrected = copy.deepcopy(expected)
    record_curation_event(
        corrected, curator="codex", action="CORRECT_EVIDENCE_LOCATOR",
        changes=(
            "Corrected the Ferreira 2019 third-paragraph locator to the sole "
            "subsection paragraph, HTML anchor article1.body1.sec2.sec4.p1, "
            "spanning PDF pages 4-5. Preserved the verbatim excerpt, native "
            "NOT_IN_ABSTRACT outcome, biological claims and prior history. "
            "Source HTML and PDF pages were rechecked for issue #1947."
        ),
        llm_assisted=True, timestamp=LOCATOR_CORRECTION_TIMESTAMP,
    )
    if current == expected or current == corrected:
        return copy.deepcopy(current)
    if current != original:
        raise SystemExit("Existing target differs from reviewed locator-repair input")
    return corrected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--correct-source-locator", action="store_true")
    args = parser.parse_args()
    if args.correct_source_locator:
        if not TARGET.is_file():
            raise SystemExit("Locator repair requires the existing target")
        current = yaml.safe_load(TARGET.read_text())
        record = correct_source_locator(current)
        with tempfile.TemporaryDirectory() as temporary:
            write_validated_trait(record, Path(temporary) / TARGET.name)
        if args.apply and record != current:
            write_validated_trait(record, TARGET)
        print("Applied locator repair" if args.apply else "Validated locator repair dry run")
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
