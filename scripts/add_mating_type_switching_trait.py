"""Add fungal mating-type switching without restricting it to reversible yeast switching."""

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

IDENTIFIER = "traitmech:000611"
TARGET = ROOT / "data/traits/physiology/mating_type_switching.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v488"
REVIEW = "DOI:10.5598/imafungus.2015.06.01.13"
YAMADA = "DOI:10.1534/genetics.107.076315"
YUN = "DOI:10.1371/journal.pgen.1006981"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "mating-type switching",
    "definition": (
        "A fungal phenotype enabling conversion from one mating type to "
        "another, either reversibly or irreversibly."
    ),
    "definition_source": REVIEW,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": REVIEW,
            "snippet": (
                "In this mating strategy, an individual of one mating type can "
                "undergo a switch to the opposite mating type, either "
                "bidirectionally (reversibly) or unidirectionally (irreversibly)."
            ),
            "notes": (
                "2015 terminology review, PMID:26203424, PMC4500084. Exact "
                "sentence from the directly retrieved full-text XML section "
                "MATING TYPE SWITCHING (s3), including both subsections read "
                "end-to-end. This is definition authority, not experimental "
                "replication or an abstract quote. The umbrella includes "
                "reversible yeast switching and irreversible mating-type "
                "alteration in filamentous fungi. A single founder can yield "
                "a mixed-mating-type colony; cellular mating identity and "
                "colony-level self-fertility are distinct. The record does not "
                "universalize the review's yeast MAT architecture or require "
                "a particular endonuclease. Figure 1 and the other mechanism "
                "category sections remain uninspected."
            ),
        },
        {
            "reference": YAMADA,
            "snippet": (
                "Schizosaccharomyces pombe cells can switch between two mating "
                "types, plus (P) and minus (M)."
            ),
            "notes": (
                "Yamada-Inagawa et al. (2007), PMID:17660548. Exact first "
                "sentence of the scientific abstract directly retrieved from "
                "Europe PMC core metadata. The study tests synthesis-dependent "
                "strand annealing using strains with two engineered mutant "
                "P donor cassettes and recovery of wild-type P information "
                "at mat1 through heteroduplex formation and repair. This is "
                "an in-vivo mechanistic test, not natural-isolate provenance. "
                "Do not require this cassette arrangement, exactly two mating "
                "types, or the S. pombe replication program for all fungi. "
                "Full text, figures, supplements and original strain provenance "
                "remain uninspected: the full-text XML endpoint returned HTTP "
                "500 and the PDF mirror returned HTTP 403. The authoritative "
                "abstract is indexed and readable despite those access failures."
            ),
        },
        {
            "reference": YUN,
            "snippet": (
                "a chromosomal looping out-based mechanism underpins "
                "irreversible unidirectional mating-type alteration in "
                "filamentous fungi."
            ),
            "notes": (
                "Yun et al. (2017), PMID:28892488, PMC5608430. Exact contiguous "
                "clause from Conclusions (sec017), not the scientific abstract "
                "or author summary. Scientific abstract, strain/culture Methods, "
                "Results sec005-sec007 and Discussion sec013/sec015 were read. "
                "Actual Figures 3 and 4 and their captions were inspected. "
                "Results and Figure 3 identify DR2 deletion in Cs23-derived "
                "T10; Discussion sec013 instead says DR1. Retain the figure-"
                "supported DR2 identity, not that conflicting wording. Figure "
                "4 separates fertile Cs23 from T10 aggregates and Cs27-derived "
                "transformants that can form perithecia without ascospores. "
                "The authors support irreversible MAT loss in C. spinulosa; "
                "the detailed nuclear-recognition mechanism remains a model. "
                "Original natural provenance, other figures, supplements and "
                "unread experimental sections remain unverified. Neither "
                "reference-strain labels nor transgenic constructs establish "
                "natural canonical examples."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "mating-type-switching-scope",
            "prompt": "Preserve reversible and irreversible switching without equating it with self-fertility.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a fungal switching capability, not a literal MAT "
                "locus, HO gene, donor cassette, direct repeat or static "
                "sequence feature. A mating-type change within a cell or "
                "developing lineage is distinct from ordinary segregation "
                "of mating types among sexual progeny. Resolve cellular, "
                "nuclear and colony-level assay scope before assigning the "
                "trait to an organism. Switching can contribute to "
                "homothallism but is not identical to it; a switched nucleus "
                "need not make the whole colony uniformly another mating "
                "type. Homothallism, heterothallism, ploidy, heterokaryosis "
                "and parasexuality are not is-a parents. PHYSIOLOGY is a "
                "filesystem category. Do not require reversibility, one "
                "cassette architecture or a universal cell-cycle stage. "
                "Resolve external phenotype/process mappings and the scope "
                "of mating-type alteration or interconversion before adding "
                "exact synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "mating-type-switching-examples-and-mechanism",
            "prompt": "Ground native switching mechanisms and natural strain examples before expanding the record.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete uninspected primary experiments and supplements, "
                "verify natural strain provenance and resolve active taxonomy "
                "before adding canonical examples. Distinguish sequence "
                "rearrangement, expressed mating identity, compatibility and "
                "completed sexual reproduction; no one readout establishes "
                "all the others. An engineered perturbation supports its "
                "specific experimental dependency, not a universal native "
                "mechanism. Resolve native protein accessions and source-"
                "bounded causal claims before adding a graph; do not use "
                "NONMECHANISTIC to bypass unresolved grounding. Keep actual "
                "abstract-verifier outcomes distinct from manual full-text "
                "checks. Source figure/Results evidence takes precedence "
                "over the conflicting repeat label noted in the evidence."
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
            "Added mating-type switching with a DOI-backed terminology review "
            "and two primary studies, each with an exact source snippet. "
            "Included reversible and irreversible scope, separated switching "
            "from MAT content and sexual-cycle readouts, and inspected primary "
            "Figures 3 and 4 to retain a source DR1/DR2 discrepancy. Ignored-"
            "and-hidden novelty searches and structured METPO review found "
            "no exact record. Reserved METPO:1056500 in v488 under released "
            "phenotype. Deferred canonical examples, lexical mappings and "
            "protein-resolved graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T02:54:00Z",
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
        "METPO:1056500", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/mating_type_switching.yaml"
        f"|{REVIEW}|{YAMADA}|{YUN}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Reversible or irreversible fungal mating-type conversion; not static MAT content.",
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
