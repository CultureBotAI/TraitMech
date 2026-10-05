"""Add the source-qualified nutritional sense of bacterial cannibalism."""

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
TARGET = ROOT / "data/traits/ecology/bacterial_cannibalism.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/predatory_bacterium.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v502/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000626"
METPO_ID = "METPO:1057900"
ORIGINAL = "DOI:10.1126/science.1086462"
BIOFILM = "DOI:10.1111/j.1365-2958.2009.06882.x"
REASSESSMENT = "DOI:10.1128/mbio.00525-26"
TIMESTAMP = "2026-10-05T19:21:00Z"
PARENT = {
    "identifier": "traitmech:000054",
    "label": "predatory bacterium",
    "definition": (
        "A trophic-ecology lifestyle in which a bacterium actively kills and consumes "
        "other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus."
    ),
    "definition_source": "DOI:10.1146/annurev.micro.091208.073346",
    "parent_traits": ["METPO:1000059"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "bacterial cannibalism",
    "definition": (
        "A predatory bacterial phenotype in which cells kill susceptible conspecific "
        "cells and obtain nutrients from the killed cells."
    ),
    "definition_source": ORIGINAL,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ORIGINAL,
            "snippet": (
                "The sporulating cells feed on the nutrients thereby released, "
                "which allows them to keep growing rather than to complete morphogenesis."
            ),
            "notes": (
                "Gonzalez-Pastor et al. (2003), PMID:12817086, scientific abstract "
                "directly retrieved from Europe PMC. The author-posted main text at "
                "https://www.researchgate.net/publication/10699307_Cannibalism_by_Sporulating_Bacteria "
                "was also read. It reports sibling killing in the PY79 laboratory "
                "background, while the nutritional explanation is proposed from "
                "killing and sporulation phenotypes, not traced nutrient uptake. "
                "The snippet preserves the abstract's stronger wording without "
                "upgrading that inference. Actual figures and supplements were "
                "not inspected; no numerical or protein-resolved claim is imported."
            ),
        },
        {
            "reference": BIOFILM,
            "snippet": (
                "Cannibal cells express the skf and sdp toxin systems to lyse "
                "a fraction of their sensitive siblings."
            ),
            "notes": (
                "Lopez et al. (2009), PMID:19775247, PMC2983100, scientific "
                "Summary, directly checked in NCBI BioC full text at "
                "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2983100/unicode. "
                "Results, Discussion and Experimental Procedures were read. "
                "NCIB3610 is the wild-type background; prominent hypercannibal "
                "phenotypes concern engineered derivatives. Nutrient-mediated "
                "sporulation delay remains an interpretation, not a nutrient-flux "
                "measurement. Actual figures and supplements were not inspected."
            ),
        },
        {
            "reference": REASSESSMENT,
            "snippet": (
                "our data challenge the established role of cannibalism-dependent "
                "killing as the mechanism behind this sporulation delay."
            ),
            "notes": (
                "Friebel et al. (2026), PMID:42294941, PMC13343845.1, published "
                "2026-06-15, IMPORTANCE section, not the scientific Abstract. "
                "Directly checked against Europe PMC full-text XML and "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC13343845.1/. Results, "
                "Discussion and Methods were read; actual figures and supplements "
                "were not inspected. DK1042 is an NCIB3610-derived laboratory "
                "background. Biofilm differentiation and membrane-integrity "
                "readouts do not directly establish nutrient transfer. This is "
                "counterevidence to a universal killing-based explanation, not "
                "a new positive demonstration of the nutritional phenotype."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "bacterial-cannibalism-operational-scope",
            "prompt": "Distinguish nutritional cannibalism from broader developmental usage.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This class retains the classical killing-and-feeding sense. "
                "Friebel et al. 2026 also calls the wider toxin-dependent biofilm "
                "differentiation program cannibalism; that usage need not satisfy "
                "this narrower nutritional definition. The predatory bacterium "
                "parent traitmech:000054 fits this operational scope, not every "
                "phenotype assigned that name in the literature. Bacteriocin "
                "production traitmech:000183 requires neither conspecific killing "
                "nor feeding. Saprotrophy traitmech:000055 does not require "
                "killing the food source; natural competence traitmech:000087 "
                "concerns DNA uptake. Fratricide, programmed cell death, biofilm "
                "formation and sporulation delay are not exact synonyms. "
                "Resolve broader terminology and external mappings before "
                "adding xrefs; do not assume species-level disjointness."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "bacterial-cannibalism-feeding-evidence",
            "prompt": "Resolve direct feeding evidence and strain provenance before exemplar curation.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The cited studies support the term and sibling-killing biology "
                "but do not justify treating every toxin-positive population "
                "as a demonstrated nutritional cannibal. Obtain direct "
                "conspecific nutrient-use evidence, inspect the supplements "
                "and verify natural strain provenance before adding canonical "
                "examples. Gene presence, expression, inhibition zones, "
                "membrane damage and delayed sporulation alone are insufficient. "
                "Do not infer a protein-resolved causal graph from toxin names "
                "or sequence profiles. Mechanistic edges, protein accessions "
                "and canonical taxa are deliberately deferred."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added bacterial cannibalism in the classical nutritional sense, "
            "with three DOI-backed snippets and explicit contrary evidence. "
            "Ignored-and-hidden novelty searches and current METPO review found "
            "no exact record. Reserved METPO:1057900 in v502, reusing the "
            "predatory bacterium parent. Deferred exemplars, mappings and "
            "mechanistic graphs pending direct feeding and provenance review."
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
        ["METPO:1007653", PARENT["label"], PARENT["definition"],
         "TraitMech:data/traits/ecology/predatory_bacterium.yaml|" + PARENT["definition_source"],
         "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
         "Existing v5 parent ID and meaning; included for standalone hierarchy.", PARENT["identifier"]],
        [METPO_ID, record["label"], record["definition"],
         "|".join(["TraitMech:data/traits/ecology/bacterial_cannibalism.yaml",
                   ORIGINAL, BIOFILM, REASSESSMENT]),
         "METPO:1007653", "", "", "metpo_traitmech_2026_10", "",
         "Classical nutritional scope; broader developmental usage and feeding inference qualified.",
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
    if any(parent.get(k) != v for k, v in PARENT.items()):
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
