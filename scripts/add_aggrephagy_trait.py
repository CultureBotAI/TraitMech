"""Add a source-bounded microbial protein-aggregate autophagy phenotype."""

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
TARGET = ROOT / "data/traits/physiology/aggrephagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v521/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v522/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000646"
METPO_ID = "METPO:1059900"
PARENT_METPO_ID = "METPO:1059100"
TIMESTAMP = "2026-10-06T16:23:31Z"
PARENT_HASH = "f97521b02026c370e138bea96d5ed332316678c01d9f2786ead3d9e5df5ff398"
TEMPLATE_HASH = "2a3ba91a60aa37635ef6461de62eece95cebb8426990e9ff9b7677d1db90f247"
HEAT = "DOI:10.1080/15548627.2026.2724473"
CCT2 = "DOI:10.1038/s44319-024-00275-7"
CUET = "DOI:10.1016/j.cell.2014.05.048"
IBOPHAGY = "DOI:10.1080/27694127.2023.2236407"
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "aggrephagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell selectively degrades "
        "protein aggregates through macroautophagic delivery to lysosomal or vacuolar compartments."
    ),
    "definition_source": HEAT,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000638"],
    "evidence": [
        {
            "reference": HEAT,
            "snippet": (
                "Our findings indicate that heat shock triggers the targeted degradation "
                "of ubiquitinated protein aggregates, mediated by the macroaggrephagy receptor Cue5."
            ),
            "notes": (
                "PMID:42647820. Scientific abstract directly read in DOI-matched "
                "Europe PMC metadata, separately from Abbreviations. Supports "
                "selective macroautophagic aggregate degradation in Saccharomyces "
                "cerevisiae. In the same heat-stress context, Cct2 and polyQ-HTT "
                "vacuolar turnover is reported to be independent of canonical "
                "autophagy; that turnover is not positive aggrephagy evidence. "
                "Publisher full text returned HTTP 403; Methods, actual figures "
                "and strain provenance were not inspected."
            ),
        },
        {
            "reference": CCT2,
            "snippet": (
                "Deficiency in this interaction significantly weakens the "
                "association of Cct2 with Atg8."
            ),
            "notes": (
                "PMID:39322741, PMC11549370. Scientific abstract and XML "
                "Introduction, Results Sec3-Sec7, Discussion Sec9 and yeast "
                "Methods Sec11 and Sec14-Sec16 were read. The quoted interaction "
                "is Atg11-Cct2. Yeast GFP-47Q cleavage and perturbations support "
                "solid-aggregate turnover; Ape1-P22L maturation alone is not "
                "complete cargo destruction. Synopsis S142 differs from "
                "scientific-abstract/Results S412; retain the discrepancy. "
                "Mammalian counterparts and phosphorylation sites are not "
                "interchangeable with yeast. Actual figures, supplements, Table "
                "EV1 and independent strain provenance were not inspected."
            ),
        },
        {
            "reference": CUET,
            "snippet": (
                "We thus propose that CUET proteins play a critical and ancient "
                "role in autophagic clearance of cytotoxic protein aggregates."
            ),
            "notes": (
                "PMID:25042851. Scientific abstract directly read in DOI-matched "
                "Europe PMC metadata. Yeast Cue5/Rsp5 perturbations and polyQ "
                "responses are separate from human Tollip experiments; do not "
                "transfer human rescue to yeast or equate toxicity alone with "
                "flux. Full text, actual figures and strain provenance were "
                "not inspected. Linked Comment-in articles are not counted "
                "as independent primary evidence."
            ),
        },
        {
            "reference": IBOPHAGY,
            "snippet": (
                "Interestingly, Cue5/Tollip, a known autophagy receptor for "
                "aggrephagy, is dispensable for this inclusion body autophagy."
            ),
            "notes": (
                "PMID:37680383, PMC10482306. Scientific abstract directly read "
                "in DOI-matched Europe PMC metadata. Boundary evidence: the "
                "authors distinguish Htt103QP/A-beta42 inclusion-body clearance "
                "in budding yeast as IBophagy. Do not relabel it an unqualified "
                "Cue5-dependent aggrephagy observation. Complete full text and "
                "actual figures were not inspected; XML returned HTTP 500 and "
                "publisher access returned HTTP 403."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "aggrephagy-scope-and-ibophagy",
            "prompt": "Review cargo boundaries and qualified process alignment.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Autophagy traitmech:000638 is the broader phenotype. Protein "
                "aggregation, disaggregation, proteasomal proteolysis, puncta, "
                "toxicity reduction or vacuolar localization alone is not "
                "selective macroautophagic degradation. GO:0035973, directly "
                "resolved at https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035973, "
                "is a nonobsolete biological process for selective "
                "protein-aggregate degradation by macroautophagy, not an exact "
                "organismal phenotype. Retain that route qualifier and omit "
                "exact xrefs and synonyms. The 2023 study explicitly separates "
                "IBophagy from aggrephagy; do not infer an exact synonym, "
                "disjointness or a separate TraitRecord solely from its "
                "receptor differences. Their potential broader/narrower "
                "relationship needs human review. Proteaphagy traitmech:000645 "
                "concerns proteasomes as cargo, not ordinary aggregate proteolysis."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "aggrephagy-context-exemplars-and-mechanisms",
            "prompt": "Resolve conditional mechanisms and natural exemplars.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Do not make Cue5, Cct2, Atg11, ubiquitination, heat shock or "
                "one aggregate reporter universal requirements. The 2026 "
                "autophagy-independent turnover result does not negate the "
                "2024 nutrient-rich solid-aggrephagy assay. Keep experimental "
                "cargo, conditions and readouts distinct. Resolve the 2024 "
                "Synopsis/Results residue discrepancy and inspect actual "
                "panels before accession-level mechanism curation. Canonical "
                "examples remain unset pending independent natural-strain "
                "provenance; engineered cargo and reporter/deletion assays "
                "are not natural exemplars. A protein graph requires native "
                "taxon-paired accessions and functional evidence. Recombinant "
                "E. coli protein production is not an aggrephagy observation, "
                "and human disease outcomes are not microbial trait evidence."
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
            "Added selective macroautophagic protein-aggregate degradation "
            "with four DOI-backed scientific-abstract snippets and explicit "
            "IBophagy, conditional receptor and source-access limits. "
            "Ignored-and-hidden novelty checks, fresh seed and pinned METPO "
            "review found no exact record. Reserved METPO:1059900 in v522 "
            "using unchanged corrected parent context from v521. Deferred "
            "unverified natural exemplars, exact mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict, old_rows: list[list[str]]) -> str:
    parent = next(r for r in old_rows[2:] if r[0] == PARENT_METPO_ID)
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/aggrephagy.yaml",
                  *[e["reference"] for e in record["evidence"]]]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Selective macroautophagic aggregate turnover; retain IBophagy and context limits.",
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
