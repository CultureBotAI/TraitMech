"""Add the source-bounded bacterial own-flagellar-filament internalization phenotype."""

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
SLUG = "bacterial_flagellar_filament_internalization"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v610/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v611/metpo_proposal_classes_robot.tsv"
SOURCE_SHA256 = "77d0147f395fe730a2830a0e73a470f7e0cde0d27bc730fa2c7ac5434fc3d7f7"
IDENTIFIER = "traitmech:000735"
METPO_ID = "METPO:1068800"
TIMESTAMP = "2026-10-16T01:41:19.482095+00:00"
RECORD = {
    "label": "bacterial flagellar filament internalization",
    "definition": (
        "A physiological phenotype in which a bacterium withdraws an assembled portion "
        "of its own flagellar filament from outside its cell body into its cell-body periplasm."
    ),
    "definition_source": "DOI:10.1038/s41564-023-01401-2",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1038/s41564-023-01401-2",
            "snippet": "most or all of the filament was internalized to the periplasm",
            "notes": (
                "Kaplan et al. 2023, PMID:37349588, PMC11061892.1, Results S3, Attachment "
                "of B. bacteriovorus to prey, paragraph beginning In cells with larger "
                "portions. Direct manuscript JATS match; native NOT_IN_ABSTRACT retained. "
                "Source strain HD100 and frozen cryo-ET stages support partial through "
                "nearly complete withdrawal into the predator's own periplasm, not the "
                "prey's. Methods S8-S12 qualify minicell enrichment and possible physiology "
                "effects; the images contain no same-cell temporal information. Main "
                "Figure 3 and supplement PDF pages 1, 22-35, 66-67 were visually inspected. "
                "S20-S21 distinguish external and internal filament portions; S22 is a "
                "schematic, not a tracked trajectory. Table S2's 8/4/30 early/intermediate/late "
                "absorbed-flagellum observations are not culture replicates or a prevalence "
                "denominator. Publisher Figure 3's main scale bar is 100 nm, versus 50 nm "
                "in the manuscript caption; no dimension or rate is inferred. Main PDF, "
                "other actual main figures, unselected supplemental images and movies "
                "remain unread. Later breakage or degradation is not required by the definition."
            ),
        },
        {
            "reference": "DOI:10.1063/pt.nkma.bqid",
            "snippet": (
                "B. bacteriovorus retracts its extracellular hook and filament into its "
                "own periplasmic space"
            ),
            "notes": (
                "Kaplan 2024, Physics Today, Figure 5 caption; contiguous span checked "
                "in directly retrieved publisher HTML. Disassembly processes and reference "
                "16 were read, and actual Figure 5 was inspected. This is a distinct "
                "author-perspective publication describing the same 2023 experiment, "
                "not independent experimental replication. The colored segmentation is "
                "not another experiment. Native UNRESOLVED means no usable abstract was "
                "returned, not that the DOI is invalid; Crossref identity and direct "
                "publisher wording were checked separately. Presumed digestion and the "
                "hypothesized evolutionary connection to spirochaete endoflagella are "
                "not defining requirements or established consequences."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "bacterial-flagellar-internalization-scope",
            "prompt": "Review the withdrawal endpoint without making universal entry-time claims.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Cell-body periplasm distinguishes withdrawal from an external flagellar "
                "sheath lumen, static endoflagella, abnormal assembly, import of free "
                "flagellin, uptake of another cell's material and predator entry into the "
                "prey's periplasm. Partial withdrawal counts; permanent intactness and "
                "complete withdrawal are not required. Bacterial polar ejection "
                "traitmech:000732 releases structures externally; eukaryotic axoneme "
                "internalization traitmech:000734 involves a different apparatus. These "
                "distinctions do not imply disjoint organisms. Earlier 109J observations "
                "of externally retained filaments constrain universal early-entry claims "
                "but neither demonstrate own-periplasmic withdrawal nor establish its "
                "absence. Different strains and preparations are not pooled into one time series."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1111/j.1365-2958.2006.05081.x",
                    "reference_title": (
                        "Characterizing the flagellar filament and the role of motility "
                        "in bacterial prey-penetration by Bdellovibrio bacteriovorus."
                    ),
                    "supports": "NO_EVIDENCE",
                    "evidence_source": "full_text",
                    "snippet": (
                        "In our experiments unshed flagella were seen early during the "
                        "establishment of an infection."
                    ),
                    "explanation": (
                        "Comparison context, not positive support for internalization or "
                        "a third supporting definition citation. External retention alone "
                        "does not measure subsequent or partial internalization."
                    ),
                    "notes": (
                        "Lambert et al. 2006, PMID:16573680, PMC1453311.1, Results, "
                        "Flagella are not always shed upon prey entry. Direct JATS match; "
                        "native NOT_IN_ABSTRACT retained. 109J predators were examined "
                        "with flagella-minus E. coli DFB225 prey. The approximately 80% "
                        "of more than 100 assessable early bdelloplasts excludes aggregates "
                        "and may overestimate the whole-population proportion; its "
                        "complement is not an internalization frequency. Actual Figure 1 "
                        "was viewed at 456 by 390 pixels. Its 20-minute time is after "
                        "mixing, not an invasion or withdrawal duration; 1% PTA staining "
                        "differs from the 2023 cryo-ET preparation. Other actual figures, "
                        "supplementary figures and main PDF remain unread."
                    ),
                },
            ],
        },
        {
            "discussion_id": "bacterial-flagellar-internalization-metpo",
            "prompt": "Review the proposed phenotype parent and unresolved ontology equivalence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059, below quality METPO:1000188, is a broader "
                "definition-based parent inference, not an assertion of locomotion. "
                "No active exact withdrawal term was identified in the inspected pinned "
                "and current METPO release/templates. Axially filamented METPO:1000705 "
                "describes static periplasmic location under motile; flagellated "
                "METPO:1000704 describes locomotory possession. Neither is equivalent "
                "to withdrawal. Deprecated METPO:0000089 and METPO:000090 carry "
                "OMO:0001000; METPO:1000381 carries IAO:0000226. Their replacement is "
                "METPO:1000704. Deprecated flagellum METPO:1000123 carries OMO:0001000 "
                "with no observed replacement or consider annotation. These historical "
                "identifiers are not revived or asserted as exact xrefs. The ontology "
                "pin is unchanged; no upstream acceptance or human sign-off is implied."
            ),
        },
        {
            "discussion_id": "bacterial-flagellar-internalization-mechanism",
            "prompt": "Separate observed internalization from universal molecular mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Motor displacement and P/L-ring separation are structural observations, "
                "not universal requirements. Sheath/outer-membrane zippering and lipid "
                "effects are hypotheses. A missing motor can reflect the cryo-ET missing "
                "wedge; vesicles may reflect sample preparation. No universal force, "
                "protease, complete digestion, recycling, rate or order of events is "
                "asserted. A sequence feature or flagellin expression alone does not "
                "establish this phenotype. A protein-resolved causal graph requires "
                "edge-specific evidence and authority-checked, taxon-paired accessions; "
                "mechanism curation is deferred, not claimed absent."
            ),
        },
        {
            "discussion_id": "bacterial-flagellar-internalization-provenance",
            "prompt": "Preserve transient-state, source-version and replication limits.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "HD100 is a qualified experimental observation, not an unqualified "
                "archetypal taxon assertion. Canonical examples remain omitted pending "
                "strain-provenance and representative-state review. The 2024 perspective "
                "and 2023 study satisfy two distinct supporting citations, not two "
                "independent experiments; supplements are part of the same study. "
                "Crossref and qualified MED identities and returned notice fields "
                "were checked, not comprehensive correction/retraction clearance. "
                "The 2023 linked post-publication review remains unread; unsuccessful "
                "publisher/PubMed access does not prove that no notice exists. Source "
                "scale-bar and preparation discrepancies are retained rather than "
                "silently harmonized. No raw-data reanalysis, exact synonym, equivalent "
                "external mapping, paid research or human scientific approval is implied."
            ),
        },
    ],
}


def build_record() -> dict:
    record = {"identifier": IDENTIFIER, **copy.deepcopy(RECORD)}
    for discussion in record["discussions"]:
        discussion.update(posed_by="codex", posed_date=TIMESTAMP[:10])
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added own-flagellar-filament withdrawal into the bacterial cell-body "
            "periplasm with two supporting DOI citations and checked 11/13-word "
            "full-text snippets. The author perspective concerns the same primary "
            "experiment, not independent replication. Kept the 14-word 2006 retained-"
            "flagella excerpt as comparison context, not definition evidence. Native "
            "NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT outcomes are preserved. "
            "Reserved 000735, v611 and 1068800-1068899 after ignored/hidden current-file, "
            "retained-history, complete-range and open/draft PR checks. Preserved "
            "partial-withdrawal, frozen-stage, source-version and preparation limits. "
            "No obsolete ID, canonical taxon, exact mapping or universal protein "
            "mechanism is inferred. Timestamp records observed allocation, not acquisition."
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
        f"TraitMech:data/traits/physiology/{SLUG}.yaml|" + record["definition_source"],
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
