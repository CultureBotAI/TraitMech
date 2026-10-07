"""Add fungal conidiation with qualified terminology and primary observations."""

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
SLUG = "fungal_conidiation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v533/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000657"
METPO_ID = "METPO:1061000"
TERMINOLOGY = "DOI:10.2336/nishinihonhifu.40.1083"
DEVELOPMENT = "DOI:10.1101/gad.3.4.559"
MORPHOLOGY = "DOI:10.1016/j.simyco.2017.09.001"
BOUNDARY = "PMID:9199700"
TIMESTAMP = "2026-10-07T03:28:58Z"
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
    "label": "fungal conidiation",
    "definition": (
        "A reproductive phenotype in which a fungus produces nonmotile asexual "
        "propagules called conidia through outgrowth from conidiogenous cells "
        "or conversion of pre-existing hyphal cells."
    ),
    "definition_source": TERMINOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "produce asexual, nonmotile and usually deciduous propagules "
                "(conidia) by de novo growth from, or conversion of a fertile "
                "hypha (conidiogenous cell)."
            ),
            "notes": (
                "Cole (1978), publisher abstract directly retrieved at "
                "https://www.jstage.jst.go.jp/article/nishinihonhifu/40/6/"
                "40_6_1083/_article/-char/en. The article is labeled Mini "
                "Review and supports terminology, not independent experimental "
                "replication. Its historical Deuteromycetes classification "
                "is not imposed on the trait. Both new outgrowth and conversion "
                "of existing cells are retained; detached spores, an aerial "
                "stalk and one spore shape are not universal requirements. "
                "The exact DOI query returned no Europe PMC records. Full "
                "text and figures were not inspected."
            ),
        },
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "The filamentous fungus Neurospora crassa responds to nutrient "
                "deprivation and dessication by producing asexual spores, or conidia."
            ),
            "notes": (
                "Springer and Yanofsky (1989), PMID:2524423, scientific "
                "abstract retrieved directly from Europe PMC. The source "
                "spelling dessication is preserved. Primary scanning-electron "
                "microscopy and fluorescent-probe study of wild-type and "
                "morphological mutants: the abstract describes apical "
                "proconidial budding, septation and disarticulation. Early "
                "chains can return to hyphal growth; later chains are committed. "
                "These are source-reported observations, not personally "
                "inspected figures. Full Methods, figures and independent "
                "strain provenance were not read, so no canonical Neurospora "
                "strain or universal nutrient/stress requirement is asserted."
            ),
        },
        {
            "reference": MORPHOLOGY,
            "snippet": "H\u2013I. Conidiophores, conidiogenous cells and conidia.",
            "notes": (
                "Woudenberg et al. (2017), PMID:29158610, PMC5679026, "
                "Figure 7 caption, Cephalotrichum lignatile CBS 209.63. "
                "The actual panels were inspected together with Taxonomy "
                "and Methods. H-I show the named structures; J shows conidia. "
                "The description reports conidia in basipetal chains. "
                "Microscopic descriptions use SNA cultures after 14 days "
                "at 25 C in darkness; A-C instead show OA, MEA and DG18 "
                "colonies. These are descriptive morphology observations, "
                "not time-lapse proof of each developmental transition."
            ),
        },
        {
            "reference": BOUNDARY,
            "snippet": (
                "The developmental cycle of S. griseus starts and ends as a conidium."
            ),
            "notes": (
                "Szabo et al. (1997), Phenotypic heterogeneity of the progeny "
                "of Streptomyces griseus conidia; scientific abstract retrieved "
                "directly from Europe PMC by PMID. This is terminology boundary "
                "evidence, not a fungal observation: the paper uses conidium "
                "for a bacterial reproductive cell. It motivates the fungal "
                "label qualifier without equating bacterial and fungal "
                "developmental mechanisms. No taxon mapping, full-text "
                "inspection or bacterial canonical example is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2041050",
            "taxon_label": "Cephalotrichum lignatile",
            "reference": MORPHOLOGY,
            "note": (
                "Ex-type culture CBS 209.63. Figure 7H-J and the primary "
                "taxonomic description document conidiogenous structures "
                "and conidia in basipetal chains. Microscopic descriptions "
                "use SNA after 14 days at 25 C in darkness. Specimen examined "
                "and Table 1 at https://pmc.ncbi.nlm.nih.gov/articles/PMC5679026/ "
                "identify Hennebert's 1959 isolate from timber in a cave "
                "at Han-sur-Lesse, Belgium. This is primary isolate provenance, "
                "not an inferred wild-type or GMO status. The observation "
                "does not imply production at every life stage or condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-conidiation-scope-and-hierarchy",
            "prompt": "Review a reproductive phenotype parent and qualified mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Sporulation METPO:1000870 "
                "and spore forming METPO:1000871 concern endospores, whereas "
                "mycelial growth traitmech:000074 concerns bacterial hyphae. "
                "The four obsolete METPO conidium/conidia classes denote "
                "material entities, not an active organismal phenotype. "
                "PMID:9199700 documents bacterial conidium usage, so the "
                "fungal qualifier is intentional. Synnema formation "
                "traitmech:000656 is stalk aggregation and includes sporeless "
                "forms; neither trait is imposed as the other's is-a parent. "
                "Pseudohyphal growth traitmech:000653 is a cell arrangement, "
                "not equivalent to conidial production. Leave exact synonyms "
                "and xrefs unset pending authority and scope review; process "
                "ontology classes need not be exact organismal phenotypes."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-conidiation-development-and-mechanism",
            "prompt": "Separate developmental routes and organism-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The class covers outgrowth and conversion of existing hyphal "
                "cells, rather than only one Aspergillus-like conidiophore "
                "architecture. Do not require an aerial stalk, a synnema, "
                "one cell or nucleus per conidium, a particular pigment, "
                "immediate detachment, dormancy or a universal nutritional "
                "trigger. Early proconidial chains alone need not establish "
                "committed development. Distinguish production from conidial "
                "germination, sexual spore formation and spores formed by "
                "cleavage within a sporangium. Do not infer the trait from "
                "a gene inventory or ordinary yeast budding without source "
                "identification of conidial production. A causal graph is "
                "deferred pending direct perturbation details, natural-strain "
                "provenance and taxon-paired protein accessions; no universal "
                "BrlA, WetA or autophagy dependence is asserted."
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
            "Added fungal conidiation with four source-backed snippets, a "
            "qualified Cephalotrichum lignatile example and explicit bacterial "
            "terminology and developmental boundaries. Ignored-and-hidden "
            "searches and structured METPO review found no exact live record. "
            "Reserved METPO:1061000 in v533; existing records unchanged."
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
         "Fungal conidial production; not bacterial endospores or stalk aggregation alone.",
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
