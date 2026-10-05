"""Add fungal heterothallism as partner-dependent sexual reproduction."""

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

IDENTIFIER = "traitmech:000610"
TARGET = ROOT / "data/traits/physiology/heterothallism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v487"
OGORMAN = "DOI:10.1038/nature07528"
KIM = "DOI:10.1534/genetics.111.136358"
YUN = "DOI:10.1371/journal.pgen.1006981"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "heterothallism",
    "definition": (
        "A fungal phenotype in which sexual reproduction requires a separate, "
        "compatible mating partner."
    ),
    "definition_source": OGORMAN,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": OGORMAN,
            "snippet": (
                "The species has a heterothallic breeding system; isolates of "
                "complementary mating types are required for sex to occur."
            ),
            "notes": (
                "O'Gorman et al. (2009), PMID:19043401. Exact scientific-abstract "
                "sentence retrieved from Europe PMC core metadata; the publisher "
                "abstract was also read. Aspergillus fumigatus produced "
                "cleistothecia and ascospores, with recombination between mating "
                "type and DNA fingerprint markers in progeny from an Irish "
                "environmental subpopulation. This is observed sexual-cycle "
                "evidence, not an inference from MAT genes alone. Full methods, "
                "figures, supplements and individual isolate provenance remain "
                "uninspected; no canonical strain or universal compatibility "
                "is asserted. The historical teleomorph name in this abstract "
                "is not used as a current taxonomy mapping."
            ),
        },
        {
            "reference": KIM,
            "snippet": (
                "Coexpression of pre-2 and ccg-4 in the mat A background leads "
                "to self-attraction and development of barren perithecia "
                "without ascospores."
            ),
            "notes": (
                "Kim et al. (2012), PMID:22298702. Exact scientific-abstract "
                "sentence directly retrieved from Europe PMC core metadata. "
                "Neurospora crassa experiments distinguish receptor/pheromone "
                "identity from completion of sexual reproduction. The quoted "
                "engineered coexpression phenotype is not self-fertility; "
                "attraction and fruiting-body initiation alone are insufficient "
                "readouts. Forced heterokaryon experiments require mating-type "
                "genes in different nuclei for meiosis and sexual sporulation "
                "in this study, not a universal fungal architecture. Full text, "
                "figures, strain provenance and supplements remain uninspected "
                "after PMC access challenges and a full-text API error. This "
                "citation supports readout limits, not an independent natural "
                "canonical example or a protein-resolved causal graph."
            ),
        },
        {
            "reference": YUN,
            "snippet": (
                "Heterothallic progeny can mate only with homothallic strains, "
                "and progeny also segregate 50% homothallic, 50% heterothallic."
            ),
            "notes": (
                "Yun et al. (2017), PMID:28892488. Exact sentence of scientific "
                "abstract abstract1 in PMC5608430 full-text XML, distinct from "
                "the author summary. Chromocrea spinulosa includes self-fertile "
                "and partner-dependent strains: self-sterile here does not "
                "mean unable to reproduce sexually with a compatible partner. "
                "The stated compatibility and segregation are source-specific, "
                "not requirements for all heterothallic fungi. Strain/culture "
                "Methods and Conclusions were also read. Cs23 and Cs27 natural "
                "provenance, most experiments, actual figures and supplements "
                "remain unverified. Nuclear-level heterothallic recognition "
                "within a self-fertile organism is not organism-level partner "
                "dependence. No canonical example is inferred from unstable "
                "Cs27-derived MAT transformants or from reference-strain labels."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "heterothallism-trait-scope",
            "prompt": "Keep partner dependence distinct from sterility and nuclear recognition.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is an organism-level reproductive phenotype, not a "
                "sequence feature or MAT-gene inventory. It requires a "
                "compatible partner, not exactly two mating types throughout "
                "fungi or compatibility with every other isolate. Self-sterility "
                "alone can also denote general infertility; resolve lexical "
                "scope before adding exact synonyms or external xrefs. "
                "Homothallism, heterokaryosis, ploidy, hyphal fusion and "
                "parasexuality are not is-a parents. Nuclear recognition within "
                "a self-fertile individual does not establish partner dependence "
                "at the organism level. PHYSIOLOGY is a filesystem category, "
                "not an ontology parent. Do not infer absence from an "
                "unsuccessful cross under one set of culture conditions."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "heterothallism-examples-and-mechanism",
            "prompt": "Verify natural isolates and complete-cycle evidence before expanding the record.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Read the uninspected methods, figures and supplements and "
                "resolve natural strain provenance and active taxonomy before "
                "adding canonical examples. Separate completed meiosis and "
                "sexual progeny from attraction, hyphal fusion, fruiting-body "
                "initiation and MAT sequence content. Resolve native protein "
                "accessions and experimental dependencies before adding "
                "mechanistic edges; do not use a NONMECHANISTIC graph to "
                "bypass unresolved grounding. Preserve actual abstract-resolver "
                "verdicts separately from manual source-section checks."
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
            "Added heterothallism with three primary DOI-backed sources and "
            "exact scientific-abstract snippets. Separated partner dependence "
            "from general infertility, MAT content and incomplete sexual "
            "readouts. Ignored-and-hidden novelty searches and structured "
            "METPO review found no exact record. Reserved METPO:1056400 in "
            "v487 under released phenotype. Deferred natural canonical "
            "examples, lexical mappings and protein-resolved graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T02:09:00Z",
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
        "METPO:1056400", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/heterothallism.yaml"
        f"|{OGORMAN}|{KIM}|{YUN}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Partner-dependent fungal sex; not general infertility or MAT content.", IDENTIFIER,
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
