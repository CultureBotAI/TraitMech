"""Add the source-bounded microbial-eukaryote axoneme-internalization phenotype."""

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
SLUG = "eukaryotic_flagellar_axoneme_internalization"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v609/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v610/metpo_proposal_classes_robot.tsv"
SOURCE_SHA256 = "ed4a62de23eee33700a4f731cf2068335e715d2c6d5c35d9f63412c20dbe0737"
IDENTIFIER = "traitmech:000734"
METPO_ID = "METPO:1068700"
TIMESTAMP = "2026-10-15T20:08:47.827435+00:00"
RECORD = {
    "identifier": IDENTIFIER,
    "label": "eukaryotic flagellar axoneme internalization",
    "definition": (
        "A physiological phenotype in which a microbial eukaryote internalizes the intact "
        "axoneme of its own cilium or flagellum into its cell body."
    ),
    "definition_source": "DOI:10.1002/cm.21637",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.1002/cm.21637",
            "snippet": "axonemes remain intact during internalization",
            "notes": (
                "Venard et al. 2020, PMID:33103844, PMCID:PMC7944584, Results 2.2, TEM "
                "interpretation paragraph following Figure 2. Contiguous span checked in "
                "direct PMC HTML; native NOT_IN_ABSTRACT retained. Live phase microscopy, "
                "fixed immunofluorescence and TEM concern Rhizoclosmatium globosum JEL800 "
                "and Spizellomyces punctatus DAOM BR117. Internalized cross-sections retain "
                "9+2 architecture without a surrounding ciliary membrane; fixed TEM is not "
                "continuous same-cell tracking. Figure 1's 23 and 32 cells are selected "
                "retraction events, not biological-culture counts. Methods time zero is "
                "plating, whereas Figure 2's TEM caption says post-retraction; retain that "
                "timing discrepancy. Table 1 labels length/diameter with rate units unlike "
                "Table 2; no numerical conversion or rate is asserted here. Main text and "
                "all five actual main figures were inspected. The main PDF and actual "
                "supplemental PDFs/videos remain unread. Subsequent degradation is a "
                "separate phase, not a requirement for this internalization phenotype."
            ),
        },
        {
            "reference": "DOI:10.1083/jcb.201701074",
            "snippet": (
                "Bd zoospores retracting their flagella by coiling the entire axoneme "
                "into the cell body"
            ),
            "notes": (
                "Fritz-Laylin et al. 2017, PMID:28473602, PMCID:PMC5461030.1, Discussion "
                "JATS s11, printed page 1681, PDF page 9. Direct normalized JATS and "
                "typeset passage checked; native NOT_IN_ABSTRACT retained. Bd denotes "
                "Batrachochytrium dendrobatidis, source strain JEL423, with synchronized "
                "zoospores observed under the described confinement preparation. Results "
                "s10, Discussion s11 and Methods s20 were read, along with selected PDF "
                "pages. Video 5 was inspected through 16 sampled frames and one enlarged "
                "frame, not continuous playback or every-frame analysis. File metadata "
                "reports 10.1 seconds at nominal 10 fps, burned-in labels span 0-20 seconds, "
                "and the caption states 0.1-second acquisition with 20-fps playback. These "
                "are not silently reconciled; no retraction rate or replicate count is "
                "inferred. The paper's WASP/SCAR pseudopod experiments do not establish "
                "an axoneme-internalization mechanism."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "eukaryotic-axoneme-internalization-scope",
            "prompt": "Review intact withdrawal separately from later axonemal disassembly.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The defining endpoint is internalization of the cell's own intact "
                "eukaryotic axoneme. Static internal localization, uptake of another cell's "
                "material, external coiling, failed assembly, motor arrest, passive breakage "
                "or shedding alone do not establish it. Venard et al. 2020 place "
                "internalization within a broader cilium-disassembly program while "
                "distinguishing subsequent degradation. The operational resorption record "
                "traitmech:000733 requires shortening through axonemal disassembly, not "
                "intact withdrawal alone. Later degradation can occur after internalization; "
                "no organism-level disjointness or permanently intact internal axoneme is "
                "asserted. Autotomy traitmech:000731 and bacterial polar flagellar ejection "
                "traitmech:000732 have different endpoints; bacterial periplasmic flagella "
                "and type IV pili are different structures. Phenotype METPO:1000059 is a "
                "definition-based parent inference, without a locomotion requirement."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1091/mbc.E24-12-0577",
                    "reference_title": (
                        "Dynamic remodeling of centrioles and the microtubule cytoskeleton "
                        "in the lifecycle of chytrid fungi."
                    ),
                    "supports": "SUPPORT",
                    "evidence_source": "full_text",
                    "snippet": "Centrioles separated from the degrading axoneme and remained parallel",
                    "explanation": (
                        "Supports the later-degradation and centriole-remodeling distinction, "
                        "not an additional definition citation, a universal centriole fate "
                        "or a same-cell kinetic measurement."
                    ),
                    "notes": (
                        "Long et al. 2025, PMID:40833813, PMCID:PMC12659703.2, Results S7, "
                        "Centrioles shorten but are not degraded during ciliary disassembly, "
                        "sentence following the coiled-complex observation; Figure 4C. "
                        "Direct JATS match; native NOT_IN_ABSTRACT retained. R. globosum "
                        "JEL800 fixed U-ExM stages are not longitudinal trajectories. Actual "
                        "Figure 4, all supplement text and visual supplement pages 4, 7 and "
                        "8 were inspected. The main-text S2 pointer concerns a transcriptomic "
                        "figure; the relevant centriole panels are S3F-H. Figure 4's caption "
                        "gives about 4.5-fold expansion, versus 5.5 +/- 0.2 in Methods/S3B; "
                        "no absolute-size conversion is inferred. Figure 4F counts 16, 3, "
                        "26 and 41 sporangia across categories from three to five independent "
                        "experiments, not retraction events. The two-hour timeline is "
                        "attributed to 2020, not a new measurement. Other actual main "
                        "figures, the main PDF and other supplement pages were not visually "
                        "inspected. The preprint is another version, not another study."
                    ),
                },
            ],
        },
        {
            "discussion_id": "eukaryotic-axoneme-internalization-metpo",
            "prompt": "Review microbial-eukaryote scope and the proposed phenotype parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No active exact term was identified in the inspected pinned/current "
                "METPO release, editor and templates. Deprecated METPO:0000089 and "
                "METPO:000090 carry OMO:0001000; METPO:1000381 carries IAO:0000226. Their "
                "active replacement METPO:1000704 denotes locomotory flagellar possession, "
                "not internalization. Deprecated ciliated METPO:0000093 and METPO:000094 "
                "carry OMO:0001000, while METPO:1000385 carries IAO:0000226; no replacement "
                "or consider annotation was observed for those or deprecated flagellum "
                "METPO:1000123 with OMO:0001000. Historical identifiers are not exact xrefs "
                "and are not reactivated. https://github.com/berkeleybop/metpo/issues/521 "
                "leaves reason-code interpretation unresolved. Upstream's bacterial/archaeal "
                "focus requires maintainer review of microbial-eukaryote inclusion. Proposal "
                "v610 reserves METPO:1068700 in 1068700-1068799, not a released identifier "
                "or human-approved mapping. The ontology pin is unchanged."
            ),
        },
        {
            "discussion_id": "eukaryotic-axoneme-internalization-mechanism",
            "prompt": "Keep observable internalization separate from universal molecular mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Do not require a universal reeling, lash-around, membrane-loss, cortical "
                "tethering, actin-dependent, dynein-dependent or proteolytic mechanism. The "
                "2020 latrunculin live-movie analysis selected complete retractions and "
                "excluded cells retaining cilia; its conditional results cannot establish "
                "all-cell retraction probabilities. Do not transfer 2017 pseudopod "
                "perturbations or 2025 transcript/orthology patterns to this phenotype. "
                "A gene, domain, motif or profile alone does not establish intact axoneme "
                "internalization. A protein-resolved graph requires taxon-paired, "
                "authority-checked accessions and edge-specific evidence. No universal "
                "rate, cell-cycle stage, complete degradation, protein recycling, exact "
                "synonym or equivalent external mapping is asserted."
            ),
        },
        {
            "discussion_id": "eukaryotic-axoneme-internalization-provenance",
            "prompt": "Resolve canonical strain provenance while preserving source-access limits.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The named laboratory strains remain qualified life-stage observations, "
                "not authority-verified canonical taxa or proof of natural provenance. "
                "Two distinct supporting publications are not a claim of independent-lab "
                "replication. The 2025 follow-up shares authors with earlier work and is "
                "scope context, not a third definition citation. Qualified MED/Crossref "
                "identities and available notice fields were checked, not comprehensive "
                "correction/retraction clearance. The linked 2017 Comment/Editorial, "
                "DOI:10.1080/15384101.2017.1360655, PMID:28820330, PMC5628642, has no "
                "returned abstract and its content remains unread; it is not counted "
                "evidence. Publisher/PMC access failures remain failures. The 2020 "
                "supplement endpoint returned an API error with HTTP 200, not a ZIP; "
                "no actual supplement contents are inferred. No raw-data reanalysis, "
                "paid research or human scientific sign-off is implied."
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
            "Added the microbial-eukaryote intact-axoneme internalization phenotype with "
            "two primary DOI sources and checked 5/14-word full-text snippets. Kept a "
            "nine-word 2025 later-degradation excerpt in a scope discussion, not definition "
            "evidence. All three retain native NOT_IN_ABSTRACT. Reserved 000734, v610 "
            "and 1068700-1068799 after ignored/hidden current-file, retained-history, "
            "complete-range and open/draft PR checks. Preserved source-access and assay "
            "limitations; no obsolete identifier, canonical taxon, exact mapping or "
            "universal protein mechanism is inferred. The timestamp is the observed "
            "allocation decision, not source acquisition."
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
