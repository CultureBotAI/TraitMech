"""Add pseudobipolar mating with explicit physical/genetic linkage scope."""

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

IDENTIFIER = "traitmech:000617"
TARGET = ROOT / "data/traits/physiology/pseudobipolar_mating_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v494"
COELHO_2010 = "DOI:10.1371/journal.pgen.1001052"
COELHO_2025 = "DOI:10.1371/journal.pbio.3003417"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "pseudobipolar mating system",
    "definition": (
        "A fungal mating-system phenotype in which pheromone/receptor and "
        "homeodomain compatibility loci are physically linked on the same "
        "chromosome but can recombine during meiosis, generating new "
        "mating-type combinations."
    ),
    "definition_source": COELHO_2010,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": COELHO_2010,
            "snippet": (
                "occasional disruptions of the genetic cohesion of the bipolar "
                "MAT locus originate new mating types."
            ),
            "notes": (
                "Coelho et al. (2010), PMID:20700437, PMC2916851. Exact clause "
                "in scientific abstract abstract1, checked against raw Europe "
                "PMC metadata and full-text XML, not the author summary. "
                "Results/Discussion and Methods were read, with actual "
                "Figures 3-5, Figure S5 and both pages of Table S1 inspected. "
                "Sporidiobolus salmonicolor CBS 6832 x ML 2241 yielded the "
                "recombinant T7.1, incompatible with either parent but "
                "compatible with CBS 490 in Figure 4. The scored endpoint is "
                "clamp-bearing mycelium and teliospores after four days on "
                "corn meal agar at 25 C; normal germination after compatible "
                "T7 crosses is reported in prose as results not shown. Eight "
                "teliospores came from one parental cross; colonies from a "
                "teliospore are mostly mitotic clones, and T8 was apparently "
                "diploid. The authors require larger samples for statistically "
                "significant linkage and precise recombination frequencies. "
                "Figure 5 partly assumes S. roseus synteny, not a complete "
                "S. salmonicolor chromosome assembly. Table S1 and Figures "
                "3/4 label CBS 6832 A2-15, whereas the germination and "
                "micromanipulation Methods say A2-6; strain identity is kept "
                "without silently reconciling that discrepancy. Table S1 gives "
                "CBS 6832 a clinical origin but only names ML 2241's isolator, "
                "so full parental provenance and active taxonomy remain "
                "unresolved. Other actual figures and supplements remain "
                "uninspected. This is native crossing evidence, not solely "
                "MAT sequence annotation or a precise population rate."
            ),
        },
        {
            "reference": COELHO_2025,
            "snippet": (
                "In the pseudobipolar configuration, the P/R and HD loci "
                "remained on the same chromosome but genetically unlinked"
            ),
            "notes": (
                "Coelho et al. (2025), PMID:41042803, PMC12510652. Exact "
                "scientific-abstract clause checked against raw Europe PMC "
                "metadata, full-text XML and publisher HTML. Supports the "
                "broader same-chromosome, recombination-permitting usage, "
                "not an independent functional replication in Kwoniella "
                "europaea. Abstract, Introduction, first two Results "
                "subsections, the relevant Discussion paragraph in sec017 "
                "and actual Figure 1 were read. Figure 1B classifies its "
                "breeding system as likely heterothallic; Figure 1E shows "
                "separated loci in PYCC6329. Despite the abstract's declarative "
                "wording, sec017 says crosses have not yielded sexual "
                "reproduction and treats persistent recombination as "
                "conditional. Physical distance alone does not exclude "
                "long-range recombination suppression. Its inferred "
                "configuration therefore does not establish observed mating "
                "or fertility. The C. decagattii and K. mangrovensis sexual "
                "results cannot be transferred to K. europaea. Other Results, "
                "Methods, figures and supplements remain uninspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pseudobipolar-mating-scope-and-hierarchy",
            "prompt": "Keep physical linkage, genetic linkage and observed compatibility distinct.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The 2010 pseudo-bipolar usage emphasizes normally bipolar "
                "behavior with occasional recombination; the 2025 usage also "
                "covers widely separated, potentially genetically unlinked "
                "loci on one chromosome. The definition retains their shared "
                "recombination-permitting organization without requiring a "
                "fixed rate, partial linkage strength, or exactly two "
                "species-wide mating types. A genomic prediction must remain "
                "distinct from an observed mating phenotype. This is not a "
                "literal MAT locus or an individual gene record. It is not "
                "identical to traitmech:000616 bipolar mating, which requires "
                "a single segregating factor, or traitmech:000615 tetrapolar "
                "mating, which requires independent segregation without "
                "specifying chromosome colocation. The 2025 paper explicitly "
                "allows functional resemblance to tetrapolarity, so do not "
                "assert disjointness. Its heterothallic framing also does not "
                "prove universal separate-partner dependence under "
                "traitmech:000610. Use released phenotype METPO:1000059 "
                "in record and proposal pending narrower hierarchy and "
                "lexical review; PHYSIOLOGY is a filesystem category."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "pseudobipolar-mating-evidence-and-mechanism",
            "prompt": "Resolve strain provenance and native dependencies before adding examples or graphs.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Resolve the CBS 6832 allele-designation discrepancy and "
                "ML 2241's original isolation context before canonical "
                "examples, and verify current taxon authority. Laboratory "
                "recombinant T7.1 is not an independently sampled natural "
                "isolate. Distinguish crossovers from gene conversion "
                "and retain the eight-teliospore sampling limitation. Finish "
                "unread source sections, actual figures and supplements "
                "before more detailed claims. Never transfer the confirmed "
                "sexual cycle of one species to another species with a "
                "predicted MAT configuration. Resolve native protein "
                "accessions and experimentally tested dependencies before "
                "causal edges; no NONMECHANISTIC graph bypasses grounding. "
                "Manual source checks remain distinct from actual resolver "
                "verdicts."
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
            "Added pseudobipolar mating system with two primary DOI-backed "
            "sources and exact scientific-abstract clauses. Distinguished "
            "native red-yeast recombination and compatibility from the "
            "broader genome-based terminology, fixed linkage rates and "
            "unverified fertility. Ignored-and-hidden novelty and allocation "
            "searches found no exact record or ID collision. Reserved "
            "METPO:1057100 in v494 under released phenotype. Deferred "
            "canonical taxa, lexical mappings and native protein graphs, "
            "with source limitations and an allele-label discrepancy explicit."
        ),
        llm_assisted=True, timestamp="2026-10-05T09:48:00Z",
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
        "METPO:1057100", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/pseudobipolar_mating_system.yaml"
        f"|{COELHO_2010}|{COELHO_2025}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Physical linkage with meiotic recombination; genomic prediction is not observed fertility.",
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
