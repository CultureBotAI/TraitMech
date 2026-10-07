"""Add anisogamy with explicit size-based scope and qualified strain evidence."""

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

IDENTIFIER = "traitmech:000620"
TARGET = ROOT / "data/traits/physiology/anisogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v497"
HAMAJI_2018 = "DOI:10.1038/s42003-018-0019-5"
NOZAKI_2014 = "DOI:10.1186/1471-2148-14-37"
LINDSEY_2024 = "DOI:10.1186/s12915-024-01878-1"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "anisogamy",
    "definition": (
        "A sexual-reproduction phenotype in which the fusing gametes belong to "
        "two types that differ in size, with smaller male and larger female gametes."
    ),
    "definition_source": HAMAJI_2018,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": HAMAJI_2018,
            "snippet": (
                "Male and female gametes differing in size\u2014anisogamy\u2014emerged "
                "independently from isogamous ancestors in various eukaryotic lineages"
            ),
            "notes": (
                "Hamaji et al. (2018), PMID:30271904, PMC6123790. Exact opening "
                "scientific-abstract clause checked in raw XML, not the separate "
                "editorial summary. Size dimorphism defines the phenotype; evolutionary "
                "origin is not part of this definition. Main text, Methods and captions "
                "were read and actual Figure 3 inspected: Eudorina gametes provide "
                "independent phenotype observations. Comparative MT architecture and "
                "RT-PCR expression do not demonstrate a gamete-size causal pathway. "
                "Results associate genomes with NIES-4100/4018, whereas Methods name "
                "NIES-3985/3984 for sequencing and the former sibling strains for other "
                "experiments. This unresolved discrepancy prevents strain-to-assembly "
                "inference here. Other actual figures and supplements remain unread."
            ),
        },
        {
            "reference": NOZAKI_2014,
            "snippet": (
                "Obligately anisogamous conjugation between male and female motile "
                "gametes occurred outside the female colony (external fertilization "
                "during anisogamy)."
            ),
            "notes": (
                "Nozaki et al. (2014), PMID:24589311, PMC4015742. Exact scientific-"
                "abstract Results sentence verified in raw XML. Main text and captions, "
                "actual Figure 3, and Additional file 2 Information S1/Table S1 were "
                "inspected. Sexual reproduction was observed in C. charkowiensis, "
                "not C. angeleri. Male length was 5-10 micrometers; female diameter "
                "13-17 micrometers. These different measurements do not establish a "
                "volume ratio. Other actual figures, Additional file 1 and the remainder "
                "of Additional file 2 remain uninspected. Proposed evolutionary "
                "intermediacy is not demonstrated ancestry."
            ),
        },
        {
            "reference": LINDSEY_2024,
            "snippet": (
                "Oogamy constitutes a specialized form of anisogamy wherein small "
                "male gametes are motile and large female gametes are not"
            ),
            "notes": (
                "Lindsey et al. (2024), PMID:38600528, PMC11007952. Exact Background "
                "Sec1 clause before the parenthetical, checked in raw XML and publisher "
                "HTML. This supports broad terminology including oogamy, not a new "
                "gamete-fusion experiment. The scientific abstract and this scope "
                "paragraph were inspected; remaining analyses, actual figures and "
                "supplements were not audited. The quoted motility formulation is "
                "not imposed on all microbial anisogamy."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:51706",
            "taxon_label": "Colemanosphaera charkowiensis",
            "reference": NOZAKI_2014,
            "note": (
                "Source-observed reference example, not a claim about every strain. "
                "Figure 3 shows mixed 2013-0615-IC-3/4/7 cultures and male "
                "2010-0713-E5; mating generally occurred after two days in "
                "nitrogen-deficient medium. Table S1 traces IC-3/4/7 to a natural "
                "water sample near Lake Isanuma. Collection provenance was checked "
                "at https://mcc.nbrp.jp/strainList.do?strainNumber=NIES-3388 "
                "(IC-7), https://mcc.nbrp.jp/strainList.do?strainNumber=NIES-3386 "
                "(IC-3) and https://mcc.nbrp.jp/strainList.do?strainNumber=NIES-3387 "
                "(IC-4). IC-3/4 collection and isolation dates conflict; no date is "
                "silently corrected. IC-7's 2018 axenic status is not projected onto "
                "2014. Taxon label verified at https://www.ncbi.nlm.nih.gov/Taxonomy/"
                "Browser/wwwtax.cgi?id=51706 on 2026-10-05. Collection fields support "
                "provenance, not independent experimental replication."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "anisogamy-scope-and-hierarchy",
            "prompt": "Preserve broad size-dimorphism scope and distinguish motility conventions.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use anisogamy in the broad size-dimorphism sense, including oogamy, "
                "as explicitly stated by Lindsey et al. (2024). Nozaki et al. (2014) "
                "instead distinguish anisogamy with flagellated female gametes from "
                "oogamy in their four-type classification. This is a terminology "
                "difference, not evidence that the phenotypes are disjoint. Motility "
                "of both gametes and external fertilization describe the canonical "
                "example, not universal requirements. The definition compares gamete "
                "types, not incidental size variation within a type, vegetative-versus-"
                "gamete size, or mating compatibility. Isogamy traitmech:000619, "
                "unisexual reproduction traitmech:000613 and fungal mating systems "
                "traitmech:000615 through traitmech:000618 describe distinct scopes. "
                "No numerical threshold or organism-level disjointness is asserted. "
                "Use phenotype METPO:1000059 pending a narrower reproductive-phenotype "
                "hierarchy; PHYSIOLOGY is a filesystem category. Verify any future "
                "oogamy child and lexical/external mappings before adding them."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "anisogamy-mechanism-and-provenance",
            "prompt": "Resolve size-control mechanisms and strain discrepancies before extension.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The observed gamete phenotype is not a literal MID locus, a sequence "
                "profile, an expanded mating-type region, or an expression signature. "
                "Comparative genomic associations and the proposed evolutionary role "
                "of MID do not justify causal edges for size dimorphism. Resolve "
                "native protein accessions and perturbation evidence before a causal "
                "graph; no NONMECHANISTIC graph bypasses this gap. Keep the 2018 "
                "Results/Methods strain mismatch unresolved until primary metadata "
                "reconciles it. Collection date conflicts do not invalidate the "
                "directly observed 2014 phenotype, but constrain strain-history claims. "
                "A collection's blank mutation field is not proof of an unmutated "
                "genome. Read remaining source material before quantitative or "
                "evolutionary extensions; preserve actual abstract-resolver verdicts "
                "separately from manual full-text checks."
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
            "Added anisogamy with three DOI-backed sources and verbatim snippets, "
            "broad size-dimorphism scope, and a provenance-qualified canonical "
            "Colemanosphaera charkowiensis example. Ignored-and-hidden novelty and "
            "allocation searches found no exact record or collision. Reserved "
            "METPO:1057400 in v497 under phenotype. Retained motility conventions "
            "and strain discrepancies explicitly; deferred lexical mappings, "
            "a narrower parent and unproven causal mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-05T12:52:28Z",
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
        "METPO:1057400", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/anisogamy.yaml|{HAMAJI_2018}|{NOZAKI_2014}|{LINDSEY_2024}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Gamete-type size dimorphism including oogamy; not universal motility or a sequence feature.",
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
