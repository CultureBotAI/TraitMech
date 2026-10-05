"""Add pseudohomothallism without universalizing nuclear counts or meiotic programs."""

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

IDENTIFIER = "traitmech:000612"
TARGET = ROOT / "data/traits/physiology/pseudohomothallism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v489"
REVIEW = "DOI:10.5598/imafungus.2015.06.01.13"
MERINO = "DOI:10.1093/genetics/143.2.789"
RAJU = "DOI:10.1002/dvg.1020150111"
MENKIS = "DOI:10.1371/journal.pgen.1000030"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "pseudohomothallism",
    "definition": (
        "A fungal phenotype enabling a sexual spore carrying separate nuclei "
        "of compatible mating types to establish a self-fertile heterokaryotic culture."
    ),
    "definition_source": REVIEW,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000609"],
    "evidence": [
        {
            "reference": REVIEW,
            "snippet": (
                "self-fertility is the result of the packaging of two independent "
                "and opposite mating type nuclei within a single spore"
            ),
            "notes": (
                "2015 terminology review, PMID:26203424, PMC4500084. Exact "
                "contiguous clause from section s2b Pseudohomothallism, read "
                "end-to-end in directly retrieved full-text XML. This supplies "
                "definition and homothallism-parent authority, not experimental "
                "replication or an abstract quote. The review describes "
                "single-spore self-fertility arising from compatible partners packaged "
                "as separate nuclei. Its two-nucleus description is not a "
                "fixed count for every subsequent spore or mycelial stage; "
                "the comparative primary study below documents developmental "
                "variation. Occasional self-sterile propagules allow "
                "outcrossing. Figure 1 remains uninspected."
            ),
        },
        {
            "reference": MERINO,
            "snippet": (
                "Ascospores of Neurospora tetrasperma normally contain nuclei "
                "of both mating-type idiomorphs (a and A), resulting in "
                "self-fertile heterokaryons"
            ),
            "notes": (
                "Merino et al. (1996), PMID:8725227. Exact opening clause of "
                "the scientific abstract directly retrieved from Europe PMC "
                "core metadata. The following parenthesis names this sexual "
                "system pseudohomothallism. The study compares mating-type "
                "chromosome and autosomal sequences from wild-collected "
                "self-fertile strains, while distinguishing occasional "
                "homokaryotic self-sterile strains capable of outcrossing. "
                "Recombination suppression is an evolutionary association "
                "in this system, not the definition of every pseudohomothallic "
                "fungus. Full text, figures, supplements and strain-level "
                "provenance in this paper remain uninspected."
            ),
        },
        {
            "reference": RAJU,
            "snippet": (
                "Two basically different modes underlie the delivery of "
                "opposite mating type nuclei into each of the four ascospores "
                "in the different genera."
            ),
            "notes": (
                "Raju and Perkins (1994), PMID:8187347. Exact sentence of the "
                "directly retrieved Europe PMC scientific abstract, which is "
                "explicitly truncated at 400 words. Comparative cytology covers "
                "N. tetrasperma, G. tetrasperma, P. anserina and P. tetraspora. "
                "First-division segregation in Neurospora differs from the "
                "second-division program in Podospora and Gelasinospora. "
                "The mat-centromere crossover is established for P. anserina "
                "but inferred for the other two latter species. Following "
                "postmeiotic development, germinating P. anserina ascospores "
                "retain three functional nuclei, two of one mating type and "
                "one of the other. Do not require exactly two nuclei, four "
                "spores, a fixed nuclear ratio, suppressed crossing over or "
                "one spindle geometry for the whole trait. Full text, original "
                "methods, actual figures and strain provenance remain unread."
            ),
        },
        {
            "reference": MENKIS,
            "snippet": (
                "recombination was assessed in individual sexual progeny "
                "originating from a selfed cross of the heterokaryotic mycelia."
            ),
            "notes": (
                "Menkis et al. (2008), PMID:18369449, PMC2268244. Exact "
                "contiguous clause of Methods s4d, not an abstract quote. "
                "Scientific abstract, Introduction, Results s2b/s2c, Methods "
                "s4a/s4c/s4d/s4e and Table 1 including footnotes were read in "
                "the full-text XML. Results s2b and Methods s4d assay 152 "
                "heterokaryotic sexual progeny of a selfed P581 cross; that "
                "selected assay denominator is not the frequency of all "
                "heterokaryotic offspring. Table 1 identifies P581 as a wild-type "
                "heterokaryon from Lihue, Hawaii, and its P-prefix footnote "
                "identifies the Perkins collection from nature. FGSC 2508/2509 "
                "are homokaryotic components, not alternative identifiers for "
                "the natural heterokaryon. The separate 83-progeny N. crassa "
                "introgression experiment is not the native P581 selfing assay. "
                "Figures, supplements, Discussion and unread experimental "
                "sections remain uninspected; inferred evolutionary history "
                "is not a demonstrated universal developmental mechanism."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:40127",
            "taxon_label": "Neurospora tetrasperma",
            "reference": MENKIS,
            "note": (
                "Qualified natural example: heterokaryon P581 from Lihue, "
                "Hawaii. Provenance is Table 1 and its Perkins-collection "
                "footnote at https://pmc.ncbi.nlm.nih.gov/articles/PMC2268244/. "
                "Results s2b and Methods s4d analyze 152 heterokaryotic sexual "
                "progeny from selfed P581; this is a selected assay set, not "
                "a claim that every spore is heterokaryotic or self-fertile. "
                "Methods s4a specifies synthetic cross medium at 25 C for "
                "crosses. FGSC 2508 and 2509 are its isolated homokaryotic "
                "components and are not the example. Do not extend this "
                "observation to every strain or life stage. NCBI taxonomy "
                "40127 resolves to the active species name on 2026-10-04."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pseudohomothallism-scope-and-hierarchy",
            "prompt": "Keep single-spore self-fertility distinct from nuclear coexistence and MAT content.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This reproductive phenotype narrows homothallism "
                "(traitmech:000609), not heterothallism or mating-type "
                "switching. Heterokaryosis is relevant cellular context but "
                "does not alone establish self-fertility. A single sexual "
                "spore can carry compatible partners as separate nuclei; "
                "MAT sequences in one assembly or multinucleation alone do "
                "not establish the trait. Do not require exactly two nuclei "
                "throughout development, four spores, one nuclear ratio, "
                "universal self-fertility or absence of outcrossing. Resolve "
                "secondary homothallism and functional heterothallism usage "
                "before assigning exact synonyms, and verify external "
                "phenotype/process mappings before adding xrefs. PHYSIOLOGY "
                "is a filesystem category. The standalone METPO proposal "
                "uses released phenotype, not an unlabeled stub for pending "
                "homothallism METPO:1056300; reconcile the narrower hierarchy "
                "when that v486 parent is accepted upstream."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "pseudohomothallism-mechanism-and-readouts",
            "prompt": "Resolve taxon-specific nuclear packaging before adding protein-level causal edges.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete unread primary experiments, figures and supplements "
                "before expanding mechanistic claims. Spindle arrangement, "
                "mating-type segregation and nuclear elimination vary across "
                "genera and developmental stages; no one meiotic program is "
                "universal. Separate observed cytology from inferred crossover "
                "events, and sequence divergence from a direct reproductive "
                "readout. Keep natural P581 separate from its homokaryotic "
                "components and interspecific introgression derivatives. "
                "Resolve native protein accessions and source-bounded "
                "dependencies before adding a graph; do not use NONMECHANISTIC "
                "to bypass missing grounding. Manual full-text matching is "
                "not an abstract-resolver VERIFIED verdict."
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
            "Added pseudohomothallism with four DOI-backed exact source "
            "snippets and qualified natural P581 after primary selfed-progeny, "
            "strain-table and NCBI checks. Kept local homothallism parent and "
            "reproductive scope separate from MAT content or nuclear count. "
            "Ignored-and-hidden novelty searches and structured METPO review "
            "found no exact record. Reserved METPO:1056600 in v489 under "
            "released phenotype pending acceptance of the narrower parent. "
            "Deferred lexical mappings and protein-resolved causal graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T03:50:00Z",
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
        "METPO:1056600", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/pseudohomothallism.yaml"
        f"|{REVIEW}|{MERINO}|{RAJU}|{MENKIS}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Single-spore self-fertility through compatible nuclei; local homothallism parent pending upstream.",
        IDENTIFIER,
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
