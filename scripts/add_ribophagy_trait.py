"""Add selective microbial ribosome turnover as an autophagy phenotype."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/ribophagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v514/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v517/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000641"
METPO_ID = "METPO:1059400"
PARENT_METPO_ID = "METPO:1059100"
ORIGINAL = "DOI:10.1038/ncb1723"
SUBUNIT = "DOI:10.1083/jcb.201308139"
BULK = "DOI:10.15252/embj.201489083"
RSA1 = "DOI:10.1016/j.jbc.2025.108554"
TIMESTAMP = "2026-10-06T11:59:00Z"
PARENT = {
    "identifier": "traitmech:000638",
    "label": "autophagy",
    "definition": (
        "A physiological phenotype in which a microbial cell degrades cytoplasmic "
        "material, including its own constituents or intracellular non-self cargo, "
        "by delivering that material to lysosomal or vacuolar compartments."
    ),
    "definition_source": "DOI:10.1083/jcb.119.2.301",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
}
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
PARENT_ROW = [
    PARENT_METPO_ID, PARENT["label"], PARENT["definition"],
    "|".join([
        "TraitMech:data/traits/physiology/autophagy.yaml",
        "DOI:10.1083/jcb.119.2.301", "DOI:10.1242/jcs.108.1.25",
        "DOI:10.1073/pnas.0813319106", "DOI:10.1371/journal.ppat.1006344",
    ]),
    "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
    "Catabolic phenotype; formation markers alone do not establish degradative flux.",
    PARENT["identifier"],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "ribophagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell selectively degrades "
        "mature ribosomes or their subunits through macroautophagic delivery "
        "to lysosomal or vacuolar compartments."
    ),
    "definition_source": ORIGINAL,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ORIGINAL,
            "snippet": (
                "A genetic screen revealed that selective degradation of "
                "ribosomes requires catalytic activity of the Ubp3p/Bre5p "
                "ubiquitin protease."
            ),
            "notes": (
                "PMID:18391941. Scientific Abstract directly read in Europe PMC "
                "core metadata with matching DOI. Saccharomyces cerevisiae "
                "degrades mature ribosomes during nutrient starvation by both "
                "nonselective autophagy and a selective component named "
                "ribophagy. The deletion phenotype concerns 60S particles "
                "despite retained starvation sensing and general autophagy; "
                "do not transfer the same dependence to 40S subunits. Enriched "
                "ubiquitination suggests direct regulation rather than proving "
                "every substrate or step. Full text, actual figures and natural "
                "strain provenance were not inspected."
            ),
        },
        {
            "reference": SUBUNIT,
            "snippet": (
                "Its ubiquitylation is Ltn1 dependent and Ubp3 reversed, and "
                "mutation of its ubiquitylation site rendered ribophagy less "
                "dependent on Ubp3."
            ),
            "notes": (
                "PMID:24616224, PMC3998797. Scientific Abstract directly read "
                "in Europe PMC core metadata and XML, distinct from the precis. "
                "The quoted substrate is Rpl25. Introduction, the LTN1-deletion "
                "Results and strain/culture Methods were also read. This yeast "
                "study explicitly treats 60S subunit turnover as ribophagy; "
                "Rpl5/Rpl25-GFP processing and vacuolar localization support "
                "degradation. LTN1 deletion rescues the delayed reporter "
                "cleavage in ubp3 mutants, so Ubp3 is not an unconditional "
                "presence criterion. Table 1 identifies the reference as "
                "BY4741 with auxotrophic deletions, not an independently "
                "verified natural exemplar. Figure 1 caption was read; "
                "actual figures, supplements, complete Methods and independent "
                "strain provenance were not inspected."
            ),
        },
        {
            "reference": BULK,
            "snippet": (
                "Under nutrient starvation, a portion of the cytoplasm is "
                "non-selectively sequestered into autophagosomes."
            ),
            "notes": (
                "PMID:25468960, PMC4337068. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. This is "
                "boundary evidence, not a positive selective-ribophagy "
                "observation: the study frames yeast vacuolar RNA catabolism "
                "as bulk nonselective autophagy. Rny1-mediated RNA cleavage, "
                "downstream nucleotide metabolism or ribosome delivery alone "
                "does not establish cargo selectivity. Full-text retrieval "
                "returned HTTP 500; full Methods and actual figures were not "
                "inspected."
            ),
        },
        {
            "reference": RSA1,
            "snippet": (
                "We discovered that most ribosomes are selectively degraded, "
                "whose mechanism differs from the previously reported selective "
                "degradation process called \"ribophagy.\""
            ),
            "notes": (
                "PMID:40294649, PMC12152620. Scientific Abstract directly read "
                "in Europe PMC core metadata and XML. Results sec1.1-sec1.3, "
                "Discussion sec2 and Methods sec3.1/sec3.7-sec3.11/sec3.13 "
                "were read. The authors distinguish Rsa1-dependent turnover "
                "from previously named Ubp3/Ufd3/Cdc48-dependent ribophagy; "
                "this is terminology/mechanism boundary evidence, not an "
                "unqualified canonical ribophagy assignment. Rpl25-GFP "
                "processing, Atg2 controls and rRNA measurements support "
                "degradation; RNA accumulation in rny1 mutants alone does not. "
                "Residual turnover in rsa1 mutants is retained. The Results "
                "support mature rRNA turnover, while the Discussion also "
                "hypothesizes nascent nuclear cargo; that cargo choice is "
                "not established. Rpl8 contact and Atg8-binding motifs are "
                "modeled, not experimentally mapped. Captions were read, "
                "but actual figures, supplements, complete Methods and "
                "independent natural strain provenance were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "ribophagy-selectivity-and-terminology",
            "prompt": "Review cargo selectivity and mechanism-dependent terminology.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Use autophagy traitmech:000638 as the broader phenotype. "
                "The 2008 paper names selective mature-ribosome turnover "
                "ribophagy; the 2014 paper explicitly includes 60S subunits. "
                "Neither ribosome protection in dormancy nor bulk RNA decay, "
                "free ribosomal-protein degradation, ribosome biogenesis, "
                "gene presence or puncta alone establishes this phenotype. "
                "The 2025 Rsa1 paper distinguishes its pathway from known "
                "ribophagy and notes differing mammalian usage. Retain that "
                "source-attributed distinction for human review; do not "
                "silently equate Rsa1-dependent turnover with the historically "
                "named pathway or make Ubp3 universal. GO:0034517, resolved "
                "at https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0034517, "
                "is a nonobsolete biological process for selective mature "
                "ribosome degradation by macroautophagy, not an exact "
                "organismal phenotype. Preserve that route qualifier and "
                "omit exact xrefs and synonyms."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "ribophagy-exemplars-and-native-mechanisms",
            "prompt": "Resolve natural exemplars and subunit-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Canonical examples remain unset: the experiments use "
                "laboratory reporter and perturbation strains, and natural "
                "strain provenance has not been independently verified. "
                "The microbial cell doing the degradation carries the "
                "phenotype, not bacteria expressing purified yeast proteins "
                "or organisms eliciting an animal host response. Require "
                "native taxon-paired protein accessions and functional "
                "evidence before a causal graph; do not impose the 60S "
                "Ubp3/Bre5 mechanism on 40S turnover or all microbial taxa. "
                "Preserve the difference between normal rates, residual "
                "activity and complete absence of degradation. A predicted "
                "binding motif is not a separate trait or a proven causal "
                "contact."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def tsv(rows: list[list[str]]) -> str:
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added ribophagy as selective mature ribosome or subunit "
            "degradation under autophagy, with four DOI-backed snippets "
            "and explicit bulk-turnover, source-access and terminology "
            "limits. Ignored-and-hidden searches and pinned METPO review "
            "found no exact record. Reserved METPO:1059400 in v517 with "
            "v514's unchanged parent context. Deferred unverified examples, "
            "mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/ribophagy.yaml",
                  ORIGINAL, SUBUNIT, BULK, RSA1]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Selective mature ribosome/subunit turnover; mechanism terminology remains under review.",
        IDENTIFIER,
    ]
    return tsv([*HEADERS, PARENT_ROW, child])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    if PARENT_PROPOSAL.read_text() != tsv([*HEADERS, PARENT_ROW]):
        raise SystemExit("Parent proposal differs from reviewed context")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
