"""Add microbial autophagic glycogen degradation with explicit endpoint limits."""

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
TARGET = ROOT / "data/traits/physiology/autophagic_glycogen_degradation.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v522/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v523/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000647"
METPO_ID = "METPO:1060000"
PARENT_METPO_ID = "METPO:1059100"
TIMESTAMP = "2026-10-06T17:24:49Z"
PARENT_HASH = "f97521b02026c370e138bea96d5ed332316678c01d9f2786ead3d9e5df5ff398"
TEMPLATE_HASH = "c90d78e62a73e8d14cf6bbdf071337c00e05342fc0dc7272bb56925335e80e2f"
SGA1 = "DOI:10.4161/auto.6.4.11736"
GLG1 = "DOI:10.3390/cells13060467"
REPORTERS = "DOI:10.3390/ijms252111772"
ATG45 = "DOI:10.1016/j.isci.2024.109810"
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "autophagic glycogen degradation",
    "definition": (
        "An autophagy phenotype in which a microbial cell degrades intracellular "
        "glycogen by delivering it to lysosomal or vacuolar compartments."
    ),
    "definition_source": SGA1,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000638"],
    "evidence": [
        {
            "reference": SGA1,
            "snippet": (
                "Our results indicate that autophagy and Sga1 act cooperatively "
                "in vacuolar glycogen breakdown"
            ),
            "notes": (
                "PMID:20383057. DOI-matched scientific abstract directly read "
                "in Europe PMC metadata. Supports autophagy-associated vacuolar "
                "glycogen hydrolysis in Magnaporthe oryzae during asexual "
                "development. The reported breakdown supports conidia formation "
                "but is dispensable for pathogenicity. Cytoplasmic "
                "retargeting of GFP-Sga1 is an engineered rescue, not a natural "
                "vacuolar-flux exemplar. Full Methods, actual figures and "
                "independent strain provenance were not inspected."
            ),
        },
        {
            "reference": GLG1,
            "snippet": (
                "vacuolar delivery of Glg1-GFP and its processing to free GFP "
                "were strictly dependent on autophagic machinery and vacuolar proteolysis."
            ),
            "notes": (
                "PMID:38534311, PMC10969688. Scientific abstract, XML Methods "
                "2.1, Results 3.2-3.4 and Discussion were read. The authors "
                "conclude nonselective glycogen autophagy in nitrogen-starved "
                "Komagataella phaffii using glycogen-bound, nonbinding and "
                "cytosolic reporters. Atg11 independence alone is not the "
                "selectivity argument. TCA extraction under-recovers the bound "
                "reporter; raw free-GFP/total-fusion ratios are unreliable. "
                "Reporter proteolysis is not a direct polymer-hydrolysis assay. "
                "Actual panels and independent strain provenance remain uninspected."
            ),
        },
        {
            "reference": REPORTERS,
            "snippet": (
                "The K. phaffii Gsy1-GFP marked the GGs and reported on their "
                "autophagic degradation during nitrogen starvation, as expected."
            ),
            "notes": (
                "PMID:39519320, PMC11546884. DOI-matched scientific abstract "
                "and XML Results 2.2-2.3 and Discussion were read. GGs means "
                "glycogen granules. This follow-up uses Gsy1 and CBM20 reporters "
                "to support neutral cargo behavior in nitrogen-starved K. phaffii; "
                "it is not independent-laboratory replication. Early Gsy1-GFP "
                "dot disappearance is autophagy-independent and is not positive "
                "flux evidence. A human STBD1 domain used as a reporter does "
                "not establish a native human mechanism in yeast. Complete "
                "Methods, actual panels and strain provenance were not inspected."
            ),
        },
        {
            "reference": ATG45,
            "snippet": (
                "glycophagy may play a role in the suppression of glycogen "
                "consumption, rather than enhancing degradation."
            ),
            "notes": (
                "PMID:38832010, PMC11145338. Exact XML Results sec2.7 span, "
                "not an abstract quote. Scientific Summary, Results, Discussion, "
                "Limitations and selected yeast, GFP-cleavage and glycogen-assay "
                "Methods were read. Boundary evidence: Atg45-dependent vacuolar "
                "delivery during Saccharomyces cerevisiae sporulation can preserve "
                "glycogen. Do not score that delivery alone as degradation. "
                "Receptor recruitment and prolonged-starvation reporter turnover "
                "do not make storage and hydrolysis interchangeable. Actual "
                "panels, supplements and independent strain provenance remain unread."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "autophagic-glycogen-degradation-scope",
            "prompt": "Distinguish degradation from broader glycophagy usage.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The explicit degradative endpoint narrows autophagy "
                "traitmech:000638 without changing that parent's identity. "
                "This is intracellular cargo recycling, not growth on glycogen, "
                "extracellular amylolysis, granule possession or a gene inventory. "
                "The Cells paper introduces glycophagy as selective but reports "
                "nonselective K. phaffii turnover; the iScience paper also uses "
                "glycophagy for vacuolar preservation during sporulation. "
                "Those source-attributed usages are not exact synonyms of this "
                "endpoint-defined record. GO:0061723 was directly resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061723 "
                "as a nonobsolete biological process for selective glycogen "
                "degradation by macroautophagy. It is narrower on selectivity "
                "and route, and is not an exact organismal phenotype. Omit "
                "exact xrefs and synonyms. Broader delivery/storage and selective "
                "subtype relationships require human review, not silent "
                "normalization of conflicting terminology."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "autophagic-glycogen-degradation-assays-and-exemplars",
            "prompt": "Resolve polymer turnover, natural exemplars and mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Keep glycogen-bound reporter cleavage, vacuolar localization, "
                "glycogen content and polymer hydrolysis as distinct readouts. "
                "Do not impose universal Sga1, Atg45, Atg11, starvation, "
                "sporulation, selectivity or a macroautophagic route. Yeast "
                "species and nutrient conditions can differ. The Atg45 storage "
                "result is a boundary, not positive evidence of this endpoint. "
                "Canonical examples remain unset pending independent natural-"
                "strain provenance and direct endpoint support; reporter and "
                "deletion strains are qualified evidence, not natural exemplars. "
                "Protein graphs require native taxon-paired accessions and "
                "functional evidence. Human disease models and an Aspergillus "
                "enzyme used as an assay reagent are not microbial observations "
                "of this trait. Inspect actual panels before protein-level curation."
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
            "Added autophagic glycogen degradation with four DOI-backed "
            "source-matched snippets and explicit storage, selectivity and "
            "reporter limits. Fresh ignored-and-hidden searches, seed and "
            "METPO inventories found no exact record. Reserved METPO:1060000 "
            "in v523 with unchanged corrected autophagy parent context. "
            "Deferred broad glycophagy equivalence, natural exemplars and "
            "protein mechanisms."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict, old_rows: list[list[str]]) -> str:
    parent = next(r for r in old_rows[2:] if r[0] == PARENT_METPO_ID)
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/autophagic_glycogen_degradation.yaml",
                  *[e["reference"] for e in record["evidence"]]]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Degradation endpoint; retain glycophagy storage, selectivity and reporter limits.",
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
