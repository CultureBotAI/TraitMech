"""Add evidence-backed rapid axopodial contraction."""

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
SLUG = "rapid_axopodial_contraction"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v558/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000682"
METPO_ID = "METPO:1063500"
STIMULATION = "DOI:10.2108/zsj.20.1367"
FOOD_UPTAKE = "DOI:10.1111/j.1550-7408.2001.tb00187.x"
TIMESTAMP = "2026-10-08T14:52:39Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "rapid axopodial contraction",
    "definition": (
        "A physiological phenotype in which a microbial cell rapidly shortens "
        "its microtubule-supported axopodia in response to stimulation or prey uptake."
    ),
    "definition_source": STIMULATION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": STIMULATION,
            "snippet": (
                "Axopodial contraction of the centrohelid heliozoon Raphidiophrys "
                "contractilis was induced by mechanical or electrical stimulation."
            ),
            "notes": (
                "Khan et al. (2003), scientific Abstract, directly retrieved from "
                "Europe PMC for PMID:14624035 at https://www.ebi.ac.uk/europepmc/"
                "webservices/rest/search?query=EXT_ID:14624035&resultType=core&format=json. "
                "Abstract-only access; full Methods and figures were not inspected. "
                "The study reports contraction faster than 3.0 mm/sec, followed by "
                "re-elongation initially about 0.30 microm/sec, and a microtubule "
                "bundle in each axopodium. Extracellular calcium dependence is "
                "restricted to this stimulation assay, not a universal defining "
                "threshold. Failure to detect other filaments with the reported "
                "fixation method does not prove their biological absence. "
                "Source taxon spelling is retained; natural culture provenance "
                "and current taxonomic identity are not established here."
            ),
        },
        {
            "reference": FOOD_UPTAKE,
            "snippet": (
                "Upon food uptake, the tubules shorten and transform into a mass "
                "of small granules when rapid axopodial contraction occurs"
            ),
            "notes": (
                "Kinoshita et al. (2001), scientific Abstract, directly read at "
                "https://pubmed.ncbi.nlm.nih.gov/11596916/ and cross-checked against "
                "Europe PMC's scientific abstract. Abstract-only access; full "
                "Methods and figures were not inspected. The study concerns "
                "Actinophrys sol. Contractile-tubule shortening and granulation "
                "accompany the food-uptake response; the authors suggest, rather "
                "than prove, a causal role. Cold and colchicine both induce "
                "microtubule disassembly, but only cold induces tubule granulation "
                "in the reported comparison. Neither intervention alone defines "
                "the natural rapid-contraction phenotype. No protein identity, "
                "effect size or strain provenance is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "axopodial-contraction-scope-and-parent",
            "prompt": "Resolve a closer cellular-contractility parent and assay boundaries.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059 is a broad parent. Existing motile "
                "METPO:1000702 is curated around organismal locomotion; rapid "
                "shortening of a cellular projection does not alone establish "
                "whole-cell locomotion. Keep axopodial contraction separate from "
                "ordinary pseudopod extension, re-elongation, slow structural "
                "loss, stalk or whole-cell contraction, and drug-induced "
                "microtubule disassembly. The reported speed is an observation, "
                "not a universal cutoff. No exact synonyms, xrefs, SSSOM "
                "equivalences or organism-level disjointness are asserted. "
                "Closer hierarchy and comparable time-resolved assays remain open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "axopodial-contraction-provenance-and-mechanism",
            "prompt": "Resolve culture provenance and taxon-specific contraction mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The directly read abstracts do not establish natural strain "
                "provenance or accession-level identities for canonical examples. "
                "Retain the source-named organisms as qualified evidence, not "
                "universal taxon assertions; resolve their current taxonomy and "
                "original culture descriptions before adding exemplars. Calcium "
                "dependence, microtubule disassembly and contractile-tubule "
                "observations must not be combined into one universal heliozoan "
                "mechanism. A protein-resolved graph requires direct perturbation "
                "evidence and taxon-paired accessions. Mechanism is deferred, not "
                "claimed absent; tubulin sequence features alone do not establish "
                "this response."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added rapid axopodial contraction with two primary DOI sources and "
            "contiguous scientific-abstract snippets checked directly. "
            "Ignored-and-hidden main/worktree/open-PR checks support 000682 "
            "and v558 block 1063500-1063599. Kept natural culture provenance, "
            "closer hierarchy and protein mechanism unresolved. Distinguished "
            "rapid response from locomotion and induced structural breakdown. "
            "Existing records unchanged. Timestamp is observed UTC."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record

def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Rapid axopodial shortening; no universal calcium threshold or protein mechanism.",
         IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
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
