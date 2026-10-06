"""Add a source-bounded microbial lipid-droplet autophagy phenotype."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/lipophagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v519/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v520/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000644"
METPO_ID = "METPO:1059700"
PARENT_METPO_ID = "METPO:1059100"
TIMESTAMP = "2026-10-06T14:27:56Z"
PARENT_HASH = "f97521b02026c370e138bea96d5ed332316678c01d9f2786ead3d9e5df5ff398"
TEMPLATE_HASH = "34c3fcd948812542d3f16ccaea326fb0e07f2663d9fcd691f7a773690954b2fc"
TURNOVER = "DOI:10.1091/mbc.e13-08-0448"
CONTACT = "DOI:10.1016/j.devcel.2024.01.014"
READOUT = "DOI:10.1080/15548627.2024.2325297"
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "lipophagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell degrades its lipid "
        "droplets by delivering them to lysosomal or vacuolar compartments."
    ),
    "definition_source": TURNOVER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000638"],
    "evidence": [
        {
            "reference": TURNOVER,
            "snippet": (
                "LDs can also be turned over in vacuoles/lysosomes by a process "
                "that morphologically resembles microautophagy."
            ),
            "notes": (
                "PMID:24258026, PMC3890349. Scientific abstract directly read in "
                "DOI-matched Europe PMC metadata and XML abstract2, not the precis. "
                "Results sec9 and Methods sec12-sec15 were read. Purified, "
                "trypsin-treated vacuoles, lipid analysis and TAG-lipase assays "
                "separate uptake from breakdown in Saccharomyces cerevisiae. "
                "The atg1/atg15 comparisons distinguish delivery, vacuolar "
                "catabolism and compensating cytosolic lipolysis. BY4742-derived "
                "reporter/mutant hosts are not verified natural exemplars. "
                "Actual figures and supplements were not inspected."
            ),
        },
        {
            "reference": CONTACT,
            "snippet": (
                "Upon nutrient exhaustion, cells consume LDs via gradual "
                "lipolysis or via lipophagy, the en bloc uptake of LDs into "
                "the vacuole."
            ),
            "notes": (
                "PMID:38354739. Scientific abstract directly read in Europe PMC "
                "with matching DOI. The LDO/Vac8 vCLIP contact site supports "
                "starvation-induced yeast uptake. This source operationally "
                "calls en bloc uptake lipophagy; docking or uptake alone is "
                "not direct proof of completed lipid degradation. Shared Vac8 "
                "use links this route to nuclear microautophagy without "
                "equating the cargo phenotypes. Full text, Methods, actual "
                "figures and strain provenance were not inspected."
            ),
        },
        {
            "reference": READOUT,
            "snippet": (
                "We find that the degradation of LD surface proteins relies "
                "on autophagy and can occur independently of lipophagy."
            ),
            "notes": (
                "PMID:38425021, PMC11210923. Scientific ABSTRACT paragraph "
                "directly read and exact-matched in DOI-matched NCBI PMC XML at "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11210923&retmode=xml. "
                "Europe PMC and PubMed abstract fields return only abbreviations; "
                "they do not verify this quote. The retrieved XML has no body. "
                "The yeast study separates engulfment from surface-protein "
                "processing and reports glucose-concentration-dependent, "
                "ATG1-independent uptake. This does not establish lipid "
                "catabolism from a protein marker alone. Full Methods, "
                "figures and supplements were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "lipophagy-scope-and-go-alignment",
            "prompt": "Review cargo-defined scope against source and GO conventions.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The 2014 study supports vacuolar lipid-droplet catabolism via "
                "a microautophagy-like route. The two 2024 abstracts also use "
                "lipophagy operationally for uptake; the present phenotype "
                "retains the autophagy parent's degradative endpoint, not "
                "uptake alone. Current GO:0061724 "
                "(https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061724) "
                "restricts lipophagy to selective macroautophagy. GO:0140504 "
                "(https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140504) "
                "separately denotes microlipophagy. Both are nonobsolete "
                "biological processes, not exact organismal-phenotype xrefs. "
                "Preserve this source-attributed scope difference for human "
                "review; no universal macro/micro route, selectivity mechanism, "
                "starvation trigger or ATG inventory is asserted. Lipolysis "
                "traitmech:000190 concerns triacylglycerol hydrolysis: it can "
                "overlap lipophagy but is neither an exact synonym nor a "
                "necessary broader parent for all droplet cargo. Lipid storage, "
                "PHA granules and pigment sequestration are not equivalent "
                "degradation phenotypes. No exact synonyms or mappings are added."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "lipophagy-flux-exemplars-and-mechanism",
            "prompt": "Resolve route-specific flux assays and native exemplars.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The phenotype belongs to the microbial cell performing "
                "autophagic degradation. Droplet docking, uptake, abundance "
                "changes and surface-protein processing are distinct readouts; "
                "none alone establishes completed lipid breakdown. Cytosolic "
                "lipases can also consume stored lipids. The condition-specific "
                "ATG dependence in these studies is not a universal sequence "
                "signature. Canonical examples remain unset pending independent "
                "natural-strain provenance; do not infer natural or engineered "
                "origin merely from a mutant label. Native taxon-paired protein "
                "accessions and direct functional support are needed before a "
                "causal graph is added. Shared contact machinery with nucleophagy "
                "traitmech:000643 does not make their cargo phenotypes equivalent. "
                "The third quote is directly source-matched despite the abstract "
                "API's abbreviation-only field; retain the resolver's actual "
                "inconclusive verdict rather than calling it VERIFIED."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def fingerprint(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added lipid-droplet autophagy with three DOI-backed source-matched "
            "snippets, explicit uptake/flux limits and GO-scope differences. "
            "Ignored-and-hidden novelty checks, fresh seed and pinned METPO "
            "review found no exact record. Reserved METPO:1059700 in v520 "
            "using unchanged corrected v519 parent context. Deferred "
            "unverified exemplars, mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict, old_rows: list[list[str]]) -> str:
    parent = next(r for r in old_rows[2:] if r[0] == PARENT_METPO_ID)
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/lipophagy.yaml",
                  *[e["reference"] for e in record["evidence"]]]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Droplet degradation, not uptake alone; GO and assay scope differences remain explicit.",
        IDENTIFIER,
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows([*HEADERS, parent, child])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or fingerprint(parent) != PARENT_HASH:
        raise SystemExit("Parent differs from reviewed context")
    template = PARENT_PROPOSAL.read_bytes()
    if hashlib.sha256(template).hexdigest() != TEMPLATE_HASH:
        raise SystemExit("Parent proposal differs from reviewed context")
    old_rows = list(csv.reader(io.StringIO(template.decode()), delimiter="\t"))
    record = build_record()
    proposal = proposal_tsv(record, old_rows)
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
