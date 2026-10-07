"""Add synnema formation with source-bounded developmental scope."""

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
SLUG = "synnema_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v532/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000656"
METPO_ID = "METPO:1060900"
MORPHOLOGY = "DOI:10.1016/j.simyco.2017.09.001"
PERTURBATION = "DOI:10.3390/ijms21186660"
DEVELOPMENT = "DOI:10.1099/00221287-87-2-292"
TIMESTAMP = "2026-10-07T02:43:42Z"
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
    "label": "synnema formation",
    "definition": (
        "A morphological phenotype in which fungal hyphae aggregate into an "
        "erect, stalk-like asexual reproductive structure, with conidiogenous "
        "elements borne from the stalk in its fertile form."
    ),
    "definition_source": MORPHOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MORPHOLOGY,
            "snippet": (
                "Hyphae of stipe parallel, 2\u20132.5 \u03bcm wide, pale-brown, "
                "slightly thick-walled."
            ),
            "notes": (
                "Woudenberg et al. (2017), PMID:29158610, PMC5679026. "
                "Direct full-text Taxonomy, Cephalotrichum lignatile description; "
                "the snippet describes this species, not universal dimensions "
                "or pigmentation. Actual Figure 7D-F shows synnemata, G the "
                "stalk apex, and H-I conidiophores and conidiogenous cells. "
                "Methods describes microscopic structures from SNA cultures "
                "after 14 days at 25 C in darkness; Figure 7A-C instead shows "
                "colonies on OA, MEA and DG18. The paper also reports loosely "
                "attached stipe hyphae in C. domesticum, so tight fusion is "
                "not imposed on the class."
            ),
        },
        {
            "reference": PERTURBATION,
            "snippet": (
                "deletion of the brlA gene blocked conidiation but not the "
                "formation of synnemata formed by aggregation of hyphal mycelia."
            ),
            "notes": (
                "Zetina-Serrano et al. (2020), PMID:32932988, PMC7555563, "
                "Introduction's summary of the authors' experiment. Direct "
                "Results 2.2.3 and actual Figure 4 were also inspected: after "
                "30 days on apples at 25 C in darkness, the engineered "
                "Penicillium expansum brlA-null strain formed sporeless "
                "hyphal stalks lacking mature conidiophores; the wild-type "
                "strain formed conidiophores in coremia. This supports "
                "separating stalk formation from completed conidiation, "
                "not a universal BrlA requirement for synnemata. The mutant "
                "is qualified evidence, not a natural canonical example."
            ),
        },
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "Coremia of Penicillium claviforme develop in three stages; "
                "primordium formation, elongation, and sporulation."
            ),
            "notes": (
                "Watkinson (1975), PMID:1141857, scientific abstract retrieved "
                "directly from Europe PMC. The publisher abstract agrees on "
                "the three stages but uses a colon where this indexed version "
                "has a semicolon. Only abstract-level developmental evidence "
                "is used; full text and figures were not inspected. Nutrient "
                "responses in this study do not define all synnemata. The "
                "historical species name is retained without a new taxon "
                "mapping or exact coremium/synnema synonym assertion."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2041050",
            "taxon_label": "Cephalotrichum lignatile",
            "reference": MORPHOLOGY,
            "note": (
                "Ex-type culture CBS 209.63. The primary taxonomic description "
                "and Figure 7 directly document synnemata; microscopic "
                "descriptions use SNA after 14 days at 25 C in darkness. "
                "Specimen examined and Table 1 at "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC5679026/ identify "
                "Hennebert's 1959 isolate from timber in a cave at "
                "Han-sur-Lesse, Belgium. This is primary isolate provenance, "
                "not an inferred wild-type or GMO status. Synnemata production "
                "can vary with culture history; it is not asserted for every "
                "life stage or growth condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "synnema-formation-scope-and-hierarchy",
            "prompt": "Review a fungal reproductive morphology parent and terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Sporulation METPO:1000870 "
                "and spore forming METPO:1000871 explicitly concern bacterial "
                "endospores; mycelial growth traitmech:000074 explicitly "
                "concerns bacterial hyphae. Hyphal anastomosis "
                "traitmech:000605 requires cytoplasmic continuity, not mere "
                "bundling. Pseudohyphal growth traitmech:000653 concerns "
                "chains of budding yeast cells. None is an exact duplicate "
                "or appropriate parent. Zetina-Serrano uses coremia for "
                "conidiophore clusters and synnemata for sporeless hyphal "
                "stalks; Watkinson uses coremia across developmental stages. "
                "Do not force these usages into an exact synonym. No exact "
                "external mapping or organism-level disjointness is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "synnema-formation-development-and-mechanism",
            "prompt": "Resolve stage-specific mechanisms before adding a causal graph.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The fertile-form qualifier preserves the documented "
                "sporeless synnemata of the brlA-null P. expansum strain. "
                "Formation does not require already mature conidiophores "
                "or conidia, a universal shape, size, color, spore wetness, "
                "growth medium or nutritional trigger. BrlA perturbation "
                "separates developmental stages in that experiment; it does "
                "not establish a universal stalk-formation gene or a "
                "mechanism in Cephalotrichum. Defer a causal graph pending "
                "organism-specific perturbations and accession-level review. "
                "Gene possession alone does not establish this phenotype. "
                "Use the 2017 paper's directly examined CBS 209.63 material, "
                "not older sequences attributed to CBS 159.66 that the "
                "authors identify as erroneous."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added synnema formation with three DOI-backed snippets, a "
            "qualified Cephalotrichum lignatile example and developmental "
            "scope boundaries. Ignored-and-hidden searches and structured "
            "METPO review found no exact record. Reserved METPO:1060900 "
            "in v532; existing records unchanged."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Fungal stalk aggregation; includes documented sporeless developmental forms.",
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
