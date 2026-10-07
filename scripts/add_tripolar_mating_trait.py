"""Add a cross-level tripolar mating phenotype with engineered-source limits."""

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

IDENTIFIER = "traitmech:000618"
TARGET = ROOT / "data/traits/physiology/tripolar_mating_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v495"
HSUEH_2008 = "DOI:10.1128/ec.00271-08"
XIONG_2026 = "DOI:10.1128/mbio.00059-26"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "tripolar mating system",
    "definition": (
        "A fungal mating-system phenotype in which sexual reproduction occurs "
        "between a partner with pheromone/receptor and homeodomain determinants "
        "linked in one mating-type region and a partner with those determinants "
        "in two unlinked regions."
    ),
    "definition_source": HSUEH_2008,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": HSUEH_2008,
            "snippet": (
                "one of the parents has one contiguous MAT locus (one pole) "
                "while the other has two unlinked sex-determining regions "
                "(two poles)."
            ),
            "notes": (
                "Hsueh et al. (2008), PMID:18723606, PMC2568056. Exact clause "
                "in the first tripolar-cross Results subsection, checked "
                "against raw PMC HTML; not an abstract quote. Engineered "
                "Cryptococcus neoformans strains relocate a homeodomain "
                "determinant from MAT to unlinked URA5. Reciprocal crosses "
                "with wild-type partners yielded germinating, segregating "
                "progeny (Tables 2/3). Actual Figures 1/2 were inspected: "
                "Figure 1 shows colony-edge filamentation, whereas Figure 2 "
                "is a genotype model, not an observed segregation ratio. "
                "Methods, relevant Results and Discussion were read; other "
                "actual figures and supplements remain uninspected. These "
                "engineered crosses establish functional feasibility, not "
                "natural prevalence or a proven ancestral intermediate. "
                "The theoretical fertility fractions are not universal "
                "measured rates; JF289 also carries multiple SXI2a copies."
            ),
        },
        {
            "reference": XIONG_2026,
            "snippet": (
                "the MAT-fused strains were able to successfully mate with "
                "the strains in which the P/R and HD are unlinked, "
                "constituting a \u201ctripolar\u201d mating."
            ),
            "notes": (
                "Xiong et al. (2026), PMID:41841731, PMC13059729. Exact "
                "Results s2-2 clause checked against raw Europe PMC "
                "full-text XML; not a scientific-abstract or IMPORTANCE "
                "quote. In Cryptococcus amylolentus, engineered MAT-fused "
                "derivatives of CBS6039 or CBS6273 mate with an opposite "
                "wild-type partner retaining unlinked P/R and HD loci. "
                "Results s2-2 reports sexual structures and genotyped "
                "germinating progeny; s2-4 reports genome-wide meiotic "
                "recombination in 26 tripolar progeny, within a 42-progeny "
                "analysis also containing bipolar progeny. Relevant "
                "construction, mating and sequencing Methods were read. "
                "Figure 2/4 captions were read, but actual figures and "
                "supplements remain uninspected after image access failed. "
                "Other source sections remain unread. Reduced fusion in "
                "bilateral MAT-fused bipolar crosses must not be transferred "
                "to these unilateral tripolar crosses."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "tripolar-mating-scope-and-hierarchy",
            "prompt": "Keep the cross-level mating phenotype distinct from sequence inventory.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The unit is a mating system or cross with differently "
                "organized partners, not a standalone locus or a species-wide "
                "assertion about either parental strain. Three poles across "
                "the pair do not mean three mating types or three independent "
                "factors in each genome. This differs from the uniform "
                "single-factor and two-factor systems in traitmech:000616 "
                "and traitmech:000615, and from recombination-permitting "
                "chromosomal colocation in traitmech:000617. Heterothallic "
                "source framing does not make this a universal separate-partner "
                "dependence subclass of traitmech:000610; progeny can differ "
                "in self-fertility. Use released phenotype METPO:1000059 "
                "in record and proposal pending narrower relational-phenotype "
                "hierarchy review. PHYSIOLOGY is a filesystem category. "
                "No disjointness, fixed fertility ratio, natural prevalence "
                "or mandatory evolutionary trajectory is asserted. Resolve "
                "lexical and external equivalences before synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "tripolar-mating-evidence-and-mechanism",
            "prompt": "Resolve natural examples and source-bounded mechanisms before extension.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Both primary studies use engineered partners, so no natural "
                "canonical taxon is inferred. Keep genotype, filamentation, "
                "spore germination, meiotic segregation and subsequent mating "
                "ability separate. The two studies report different "
                "self-fertility outcomes for progeny carrying compatible "
                "homeodomain determinants; retain strain background and "
                "copy-number context rather than generalize sterility. "
                "Inspect unread figures, supplements and source sections "
                "before more detailed claims or quantitative rates. Resolve "
                "native protein accessions and experimentally tested "
                "dependencies before causal edges; no NONMECHANISTIC graph "
                "bypasses grounding. Manual full-text snippet matches remain "
                "distinct from the abstract resolver's actual verdicts."
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
            "Added tripolar mating system with two primary DOI-backed sources "
            "and verbatim full-text clauses. Kept the cross-level functional "
            "phenotype distinct from sequence inventory, natural prevalence "
            "and fixed fertility ratios. Ignored-and-hidden novelty and "
            "allocation searches found no exact record or ID collision. "
            "Reserved METPO:1057200 in v495 under released phenotype. "
            "Deferred canonical taxa, lexical mappings and protein graphs, "
            "with engineered provenance and unread source material explicit."
        ),
        llm_assisted=True, timestamp="2026-10-05T10:50:00Z",
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
        "METPO:1057200", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/tripolar_mating_system.yaml"
        f"|{HSUEH_2008}|{XIONG_2026}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Cross-level phenotype; engineered demonstrations do not establish natural prevalence.",
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
