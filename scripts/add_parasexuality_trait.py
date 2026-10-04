"""Add the parasexuality phenotype without conflating ploidy or meiotic genes."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000607"
TARGET = ROOT / "data/traits/physiology/parasexuality.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v484"
BENNETT = "DOI:10.1093/emboj/cdg235"
SEERVAI = "DOI:10.1128/ec.00128-13"
ANDERSON = "DOI:10.1038/s41467-019-12376-2"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "parasexuality",
    "definition": (
        "A fungal phenotype enabling genetic reassortment through nuclear fusion "
        "followed by chromosome-loss-mediated ploidy reduction instead of "
        "conventional meiosis."
    ),
    "definition_source": BENNETT,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": BENNETT,
            "snippet": (
                "Thus, an efficient parasexual cycle can be performed in "
                "C.albicans, one that leads to the reassortment of genetic "
                "material in this organism."
            ),
            "notes": (
                "Bennett and Johnson (2003), PMID:12743044. The snippet is an "
                "exact span of the directly retrieved Europe PMC abstract. "
                "Main-text experiments and Figures 1-9 were inspected in the "
                "author-hosted PDF: "
                "https://static1.squarespace.com/static/56463117e4b0770d2cd2d163/"
                "t/564e4d55e4b04412d33a3036/1447972181154/"
                "the%2Bembo%2Bjournal%2B2003%2Bbennett.pdf. "
                "Marked CAI4-derived Candida albicans strains formed tetraploid "
                "mating products; chromosome loss yielded diploid or near-diploid "
                "progeny that could mate again. Flow cytometry and multiple "
                "marker/MTL readouts support ploidy reduction; marker loss alone "
                "can also arise by recombination. The cycle need not reach "
                "haploidy. The paper leaves conventional meiosis possible under "
                "untested conditions. Its supplementary media, mating and PCR "
                "details remain unread, and its unpublished meiotic-gene "
                "deletion observations are not used as mechanistic proof."
            ),
        },
        {
            "reference": SEERVAI,
            "snippet": (
                "The diploid products are themselves mating competent, thereby "
                "establishing a parasexual cycle in this species for the first time."
            ),
            "notes": (
                "Seervai et al. (2013), PMID:24123269. The snippet exact-matches "
                "the directly retrieved Europe PMC abstract. Publisher Methods, "
                "Results, Discussion and strain tables were read, and Figures "
                "3 and 4 were visually inspected. Marked Candida tropicalis "
                "tetraploids produced near-diploid progeny on sorbose; "
                "remating, MTL genotyping and DNA-content measurements support "
                "a repeatable cycle. 2-DOG resistance selects GAL1 loss, not "
                "necessarily chromosome loss. The Figure 4 caption's wild-type "
                "wording does not erase the CAY2060 arg4/arg4 tester genotype "
                "reported in Table 1 and Methods. The response to "
                "presporulation medium differs from C. albicans. The "
                "supplementary Figure S1 caption and labels were read as PDF "
                "text, but the actual supplemental plot was not visually "
                "inspected. No natural canonical example is inferred from "
                "these marker-strain experiments."
            ),
        },
        {
            "reference": ANDERSON,
            "snippet": (
                "These results indicate that C. albicans CCL represents a "
                "'parameiosis' that blurs the conventional boundaries between "
                "mitosis and meiosis."
            ),
            "notes": (
                "Anderson et al. (2019), PMID:31558727. The snippet is an exact "
                "span of the directly retrieved Europe PMC abstract. Publisher "
                "Introduction and Results were read, but full Methods, actual "
                "figures and supplements were not inspected. Concerted "
                "chromosome loss (CCL) in C. albicans includes high "
                "inter-homolog recombination and functions of Spo11 and Rec8. "
                "Their effects on chromosome stability and recombination are "
                "different endpoints: loss of SPO11 increases marker loss while "
                "reducing recombination, whereas loss of REC8 reduces both in "
                "the tested CCL assays. Absence of conventional meiosis does "
                "not mean absence of meiosis-associated proteins. Neither "
                "homologue presence alone nor these assays establish a "
                "conventional meiotic cycle. Protein identities, native strain "
                "provenance and assay-specific causal edges remain uncurated."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "parasexuality-trait-scope",
            "prompt": "Preserve the complete reproductive capability rather than an isolated readout.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The record denotes an organismal phenotype, not a locus, "
                "protein, ploidy measurement or individual mating experiment. "
                "Nuclear fusion followed by nonmeiotic chromosome loss permits "
                "genetic reassortment; mating can be part of this cycle. Do not "
                "define parasexuality as absence of all mating, sexual programs "
                "or meiosis-associated genes. It does not require haploid "
                "progeny, obligate asexuality, identical ploidy in every product "
                "or successful cycling in every isolate. Hyphal fusion, "
                "heterokaryosis, marker loss, aneuploidy, ploidy change and "
                "horizontal gene transfer alone are insufficient. The existing "
                "ploidy trait describes genome-copy number, not this capability. "
                "Ploidy and hyphal anastomosis are not is-a parents. The fungal "
                "scope reflects the cited evidence; broader uses of parasexual "
                "terminology require separate interpretation. Resolve external "
                "phenotype/process mappings and exact synonyms at their "
                "authorities before adding them."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "parasexuality-mechanism-and-strain-provenance",
            "prompt": "Resolve native strain provenance and stage-specific mechanisms before enrichment.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The cited laboratory cycles use marked or engineered strains; "
                "retain those qualifiers rather than promoting a tester or "
                "deletion strain to a natural canonical example. Complete the "
                "unread supplementary methods and figures, current NCBI "
                "identities, original strain provenance and native protein "
                "anchors before adding examples or a mechanistic graph. "
                "Distinguish chromosome loss, DNA-content reduction, "
                "inter-homolog recombination and renewed mating as separate "
                "readouts. A flow-cytometry peak near a diploid control does "
                "not resolve every chromosome's copy number. The 2019 "
                "parameiosis evidence prevents treating nonmeiotic as "
                "independent of all meiotic proteins or simply equating it "
                "with ordinary mitosis. Do not transfer medium responses or "
                "protein dependencies across species, and do not use a "
                "NONMECHANISTIC graph to bypass unresolved molecular grounding."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added parasexuality as a fungal reproductive phenotype with three "
            "primary DOI-backed references and exact abstract snippets. "
            "Separated nuclear-fusion/chromosome-loss cycling from isolated "
            "ploidy measurements and sequence features; retained laboratory "
            "strain and source-access limits. Ignored-and-hidden repository "
            "searches and structured METPO review found no exact record. "
            "Reserved METPO:1056100 in v484 under released phenotype. "
            "Deferred external mappings, canonical examples and protein graph "
            "pending provenance and assay-specific grounding."
        ),
        llm_assisted=True, timestamp="2026-10-04T23:44:20Z",
    )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1056100", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/parasexuality.yaml"
        f"|{BENNETT}|{SEERVAI}|{ANDERSON}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Nuclear fusion and chromosome loss; neither ploidy nor meiotic genes alone.", IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
