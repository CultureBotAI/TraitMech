"""Add tetrapolar mating as a functional phenotype, not a MAT-locus inventory."""

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

IDENTIFIER = "traitmech:000615"
TARGET = ROOT / "data/traits/physiology/tetrapolar_mating_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v492"
FINDLEY = "DOI:10.1371/journal.pgen.1002528"
MAIA = "DOI:10.1534/genetics.115.177717"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "tetrapolar mating system",
    "definition": (
        "A fungal mating phenotype in which compatibility between partners is "
        "governed by two independently segregating mating-type factors and "
        "requires different specificities at both factors."
    ),
    "definition_source": FINDLEY,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": FINDLEY,
            "snippet": (
                "None of these MAT recombinant progeny mated with either parent, "
                "further confirming that C. amylolentus possesses a tetrapolar mating system"
            ),
            "notes": (
                "Findley et al. (2012), PMID:22359516, PMC3280970. Exact Results "
                "s2g clause, not an abstract quote. The preceding sentences "
                "report interfertility of complementary recombinants; parent "
                "sterility alone is insufficient. Introduction defines the two "
                "unlinked factors and differences at both. Actual Figures 8/9 "
                "were inspected: sexual structures and the mating matrix support "
                "the functional phenotype. Figure 9A is a conceptual model, not "
                "an observed equal-ratio result. Results s2b/s2e, direct prose "
                "of s2f/s2g and Methods s4a/s4m were read. Mixed F1 progeny "
                "include blastospores; frequent infertility and biased mating "
                "types make this a modified tetrapolar cycle. Complete Text S1 "
                "was text-extracted, not page-rendered: filamentation is not "
                "successful mating. Its description of F1S2 #16 as sterile "
                "must not override s2g's successful crosses with some partners. "
                "Tables 1/2, other figures and other supplements remain "
                "uninspected. Physical MAT separation alone in T. wingfieldii "
                "does not establish its reproductive phenotype."
            ),
        },
        {
            "reference": MAIA,
            "snippet": (
                "independent assortment of MAT alleles was observed in the "
                "meiotic progeny of a test cross."
            ),
            "notes": (
                "Maia et al. (2015), PMID:26178967, PMC4566278. Exact scientific "
                "abstract clause, directly retrieved from Europe PMC core "
                "metadata and checked against NCBI efetch front matter. "
                "Leucosporidium scottii has physically unlinked HD and P/R "
                "regions; the reported meiotic segregation supports functional "
                "tetrapolarity independently of sequence annotation. Natural "
                "population linkage disequilibrium does not contradict the "
                "test-cross result. The abstract reports fertile progeny of "
                "four mating types but approximately two thirds nonhaploid; "
                "do not impose universal haploidy or equal ratios. Full-text "
                "XML/PDF endpoints failed with HTTP 500/403 and NCBI returned "
                "no body. Methods, figures, supplements and natural strain "
                "provenance remain uninspected; no canonical example is inferred."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:104669",
            "taxon_label": "Cryptococcus amylolentus",
            "reference": FINDLEY,
            "note": (
                "Qualified to the CBS6039 x CBS6273 cross, not every strain "
                "or laboratory-derived progeny. Natural provenance: Methods "
                "Strains and media at https://journals.plos.org/plosgenetics/"
                "article?id=10.1371/journal.pgen.1002528 reports both isolates "
                "from insect frass in South Africa. Mating used V8 pH 5 in the "
                "dark at 24 C; actual Figure 8 shows two-week sexual structures "
                "and Figure 9 compares complementary mating combinations. "
                "Recombinant fertility, not hyphae alone, supports the modified "
                "tetrapolar classification. NCBI taxonomy 104669 resolves to "
                "this species on 2026-10-05."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "tetrapolar-mating-scope-and-hierarchy",
            "prompt": "Keep mating compatibility separate from partner dependence and MAT inventory.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a functional compatibility phenotype, not possession "
                "of two loci or exactly four mating types throughout a species. "
                "Factors can be multiallelic; different specificities are "
                "necessary, not a guarantee of fertile progeny in every cross. "
                "Findley describes the observed C. amylolentus cycle as "
                "heterothallic, but that example does not make the broader "
                "compatibility axis equivalent to obligatory separate-partner "
                "dependence in traitmech:000610. The latter already separates "
                "nuclear recognition from organism-level self-fertility. "
                "Use released phenotype METPO:1000059 in both record and "
                "proposal rather than infer universal self-sterility. Do not "
                "assert disjointness with homothallism, fixed segregation "
                "ratios, universal A/B naming or identical recognition "
                "architectures. Resolve bifactorial terminology and external "
                "mappings before adding synonyms or xrefs. PHYSIOLOGY is a "
                "filesystem category, not a narrower ontology parent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "tetrapolar-mating-mechanism-and-readouts",
            "prompt": "Resolve native mechanisms and unread experiments before extending the graph.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete the unread Maia full text and Findley tables and "
                "supplements before finer mechanistic or strain claims. "
                "Distinguish MAT-locus separation, genetic segregation, "
                "compatibility, filamentation and fertile sexual progeny. "
                "An unsuccessful cross alone does not establish trait absence; "
                "source-specific sterility can be relative to particular "
                "partners. Resolve native protein accessions and experimentally "
                "tested dependencies before causal edges. No NONMECHANISTIC "
                "graph is used to bypass protein grounding. Manual full-text "
                "matches do not replace the abstract resolver's actual verdict."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added tetrapolar mating system with two independent DOI-backed "
            "sources and verbatim snippets, a qualified natural CBS6039 x "
            "CBS6273 example and verified NCBI taxonomy. Kept mating evidence "
            "distinct from MAT sequence inventory, universal fertility and "
            "partner dependence. Ignored-and-hidden novelty and allocation "
            "searches found no exact record or ID collision. Reserved "
            "METPO:1056900 in v492 under released phenotype. Deferred lexical "
            "mappings, protein mechanisms and explicitly unread source material."
        ),
        llm_assisted=True, timestamp="2026-10-05T07:16:00Z",
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
        "METPO:1056900", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/tetrapolar_mating_system.yaml"
        f"|{FINDLEY}|{MAIA}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Two independently segregating compatibility factors; not a sequence-inventory assertion.",
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
