"""Add bipolar mating as a compatibility phenotype, not a sequence inventory."""

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

IDENTIFIER = "traitmech:000616"
TARGET = ROOT / "data/traits/physiology/bipolar_mating_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v493"
BAKKEREN = "DOI:10.1073/pnas.91.15.7085"
JAMES = "DOI:10.1534/genetics.105.051128"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "bipolar mating system",
    "definition": (
        "A fungal mating phenotype in which compatibility between partners is "
        "governed by a single segregating mating-type factor."
    ),
    "definition_source": BAKKEREN,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": BAKKEREN,
            "snippet": (
                "A bipolar system is defined by a single genetic locus (MAT) "
                "that can have two or multiple alleles."
            ),
            "notes": (
                "Bakkeren and Kronstad (1994), PMID:7913746, PMC44343. Exact "
                "scientific-abstract sentence directly retrieved from Europe "
                "PMC core metadata. The abstract reports cloning of Ustilago "
                "hordei a1 and physical linkage of a and b into a complex MAT "
                "region, contrasted with genetically unlinked loci in U. maydis. "
                "The compatibility factor is not necessarily one gene. This "
                "supports definition and a reported linkage architecture, not "
                "a fresh verification of native crossing assays. Full text, "
                "figures, methods, supplements and natural strain provenance "
                "remain uninspected; no canonical strain is inferred."
            ),
        },
        {
            "reference": JAMES,
            "snippet": (
                "All of the 24 collections displayed a bipolar mating system "
                "with only two mating types among all progeny of a collection."
            ),
            "notes": (
                "James et al. (2006), PMID:16461425, PMC1456265. Exact sentence "
                "in the first Results subsection on p. 1881, visually checked in the published "
                "PDF at https://public.websites.umich.edu/~mycology/resources/"
                "Publications/james2006.genetics.pdf; not an abstract quote. "
                "Native Coprinellus disseminatus single-spore crosses support "
                "the compatibility phenotype. Two types per collection does "
                "not mean only two across the species. Methods score clamps "
                "and dikaryotization, not automatically completed fertile sex; "
                "poor-mating progeny were excluded when choosing population "
                "testers. Table 3 shows segregation in 13 TJ00/38 progeny: "
                "MIP tracks mating type, whereas CDSTE3.1-.3 do not. Its "
                "plus/minus states are PCR-RFLP genotypes, not gene presence "
                "or absence; CDSTE3.4 lacks segregation data. The abstract "
                "reports heterologous sexual responses, not loss of all "
                "pheromone-receptor function. PDF pp. 1877-1882 and actual "
                "Tables 1-3 were read; pp. 1883-1884 were text-extracted only. "
                "Actual figures, later Results/Discussion and supplements "
                "remain uninspected. Natural North Carolina fruit-body "
                "provenance is described in Methods, but active taxon authority "
                "and the intersterile Japanese group remain unresolved; no "
                "canonical taxon assertion is made."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "bipolar-mating-scope-and-hierarchy",
            "prompt": "Keep genetic compatibility distinct from locus inventory and partner dependence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "A single segregating compatibility factor need not be one "
                "gene, exactly two specificities across a species, or fused "
                "pheromone/receptor and homeodomain loci. Bakkeren describes "
                "recognition in heterothallic basidiomycetes, but its examples "
                "do not establish universal separate-partner dependence under "
                "the organism-level definition of traitmech:000610. The "
                "functional compatibility axis differs from self-fertility "
                "and from tetrapolar mating (traitmech:000615), which requires "
                "differences at two independently segregating factors. Use "
                "released phenotype METPO:1000059 in record and proposal; "
                "do not assert disjointness with homothallism, universal "
                "self-sterility or a sufficient guarantee of fertility. "
                "Resolve unifactorial terminology and external equivalences "
                "before adding synonyms or xrefs. PHYSIOLOGY is a filesystem "
                "category, not a narrower ontology parent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "bipolar-mating-mechanism-and-examples",
            "prompt": "Resolve native mechanisms and taxon authority before adding graphs or examples.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete unread source sections and inspect actual figures "
                "and supplements before extending mechanistic claims. Loss of "
                "mating-type specificity is not absence of receptor genes or "
                "loss of every cellular function. Keep native compatibility "
                "assays, genetic segregation, heterologous responses and "
                "completed fertile reproduction distinct. Resolve NCBI taxon "
                "authority and strain scope before canonical examples, and "
                "native protein accessions plus tested dependencies before "
                "causal edges. No NONMECHANISTIC graph bypasses grounding. "
                "Manual full-text checks do not replace the abstract "
                "resolver's actual verdict."
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
            "Added bipolar mating system with two primary DOI-backed sources "
            "and verbatim snippets. Kept single-factor compatibility distinct "
            "from gene inventory, globally two mating types, one molecular "
            "architecture and partner dependence. Ignored-and-hidden novelty "
            "and allocation searches found no exact record or ID collision. "
            "Reserved METPO:1057000 in v493 under released phenotype. Deferred "
            "canonical taxon assertions, lexical mappings, native protein "
            "graphs and explicitly unread source material."
        ),
        llm_assisted=True, timestamp="2026-10-05T08:34:00Z",
    )
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE_LOCATOR",
        changes=(
            "Corrected the James p. 1881 locator: the verbatim quote is in "
            "the first Results subsection, not its first sentence (#1706). "
            "The quotation and biological interpretation are unchanged."
        ),
        llm_assisted=True, timestamp="2026-10-05T08:39:00Z",
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
        "METPO:1057000", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/bipolar_mating_system.yaml"
        f"|{BAKKEREN}|{JAMES}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Single-factor compatibility; not exactly two species-wide types or one locus architecture.",
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
