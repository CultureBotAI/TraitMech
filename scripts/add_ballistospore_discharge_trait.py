"""Add source-bounded ballistospore discharge, distinct from spore formation."""

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
SLUG = "ballistospore_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v537/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000661"
METPO_ID = "METPO:1061400"
BALLISTICS = "DOI:10.1371/journal.pone.0004163"
DEVELOPMENT = "DOI:10.1371/journal.pone.0105147"
MECHANICS = "DOI:10.1242/jeb.029975"
TIMESTAMP = "2026-10-07T08:42:05Z"
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
    "label": "ballistospore discharge",
    "definition": (
        "A physiological phenotype in which a fungus forcibly discharges spores "
        "through coalescence of Buller's drop with liquid on the spore surface."
    ),
    "definition_source": BALLISTICS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": BALLISTICS,
            "snippet": (
                "is achieved by the formation and collapse of the Buller's drop "
                "on the wet spore surface"
            ),
            "notes": (
                "Stolze-Rybczynski et al. (2009), PMID:19129912, PMC2612744; "
                "Results and Discussion, opening sentence, directly retrieved "
                "as publisher HTML and Europe PMC full-text XML. Abstract, "
                "Introduction, Results and Discussion, Table 1 and Methods "
                "were read. Seven basidiomycete species were analyzed by "
                "high-speed video; the yeast Sporobolomyces salmonicolor NPM01 "
                "had a measured mean launch speed of 1.42 +/- 0.12 m/s "
                "(s.e.m., six launches). Its 0.54 +/- 0.04 mm flight range is "
                "calculated, not a directly measured range. Drop geometry and "
                "flight range vary; a prominent lens-shaped adaxial drop is "
                "not universal. Figure captions were read, but image retrieval "
                "failed; actual figures, videos and supplements were not inspected."
            ),
        },
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "Ballistospores can be produced either asexually (ballistoconidia) "
                "or sexually (basidiospores)."
            ),
            "notes": (
                "Ianiri et al. (2014), PMID:25148260, PMC4141788; Introduction "
                "directly retrieved as full-text XML. This quotation supports "
                "terminology, not a new comparison of sexual and asexual "
                "development. Scientific abstract, strain table, mirror-assay "
                "Methods, initial mutant-screen Results and Discussion were "
                "also read. Of 18 mirror mutants, 17 had absent or reduced "
                "spore production; GI277 still formed abundant ballistospores "
                "but failed to release them. A failed mirror assay alone thus "
                "does not distinguish formation from discharge. PHS1 results "
                "concern delayed formation and broader cellular defects, not "
                "a demonstrated universal release motor. Actual figures, "
                "supplements and independent IAM 13481 provenance were not "
                "inspected; no canonical example is inferred from these mutants."
            ),
        },
        {
            "reference": MECHANICS,
            "snippet": (
                "The fusion of the droplet onto the spore creates a momentum "
                "that propels the spore forward."
            ),
            "notes": (
                "Noblin, Yang and Dumais (2009), PMID:19684219; scientific "
                "abstract retrieved directly through Europe PMC. The study "
                "reports high-speed observations in Auricularia auricula and "
                "Sporobolomyces yeasts, mechanical analysis and calibrated "
                "microcantilever measurements of detachment work. The "
                "artificial validation system is not a fungal exemplar. "
                "Predicted and observed velocities are distinct quantities. "
                "Full text, figures, supplements and strain provenance were "
                "not inspected; the abstract is not a complete mechanistic audit."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:5005",
            "taxon_label": "Sporobolomyces salmonicolor",
            "reference": BALLISTICS,
            "note": (
                "Strain NPM01. Table 1 reports high-speed-video launch "
                "measurements from six spores, with mean initial speed "
                "1.42 +/- 0.12 m/s (s.e.m.); the listed flight distance is "
                "modeled, not directly measured. Organisms and culture methods "
                "at https://doi.org/10.1371/journal.pone.0004163 identify NPM01 "
                "as isolated from a contaminated manufacturing facility and "
                "report spore formation on potato dextrose agar within 24 h. "
                "That primary provenance passage was read directly; no "
                "engineered-strain origin is inferred. NCBI Taxonomy resolves "
                "the species ID and label. This example concerns NPM01 under "
                "the reported conditions, not every strain or life stage."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "ballistospore-discharge-scope-and-hierarchy",
            "prompt": "Review dispersal hierarchy without equating formation and discharge.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059. The sporulation and spore-forming "
                "records METPO:1000870 and METPO:1000871 concern endospores. "
                "Fungal conidiation traitmech:000657 concerns production of "
                "asexual propagules, whereas ballistospores include sexual "
                "and asexual forms and formation can persist without release. "
                "Discharge is also distinct from passive shedding, later "
                "wind transport and pressure-driven ascospore or sporangium "
                "ejection. Motility METPO:1000701 emphasizes independent "
                "locomotion; a closer dispersal parent and process-versus-"
                "phenotype mappings need review. Ballistospore and "
                "ballistoconidium name cells, not exact synonyms of this "
                "disposition; no exact synonyms or xrefs are asserted. Do not "
                "require a particular speed, distance, fruiting body or "
                "asexual developmental mode."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "ballistospore-discharge-mechanism-and-readouts",
            "prompt": "Keep measured discharge, formation defects and physical models distinct.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The cited studies support a surface-tension mechanism, not "
                "an unknown-mechanism claim. A causal graph is deferred until "
                "the full mechanical study and supplementary observations "
                "are inspected and the repository's protein-required "
                "MECHANISTIC graph convention is reconciled with a physical "
                "coalescence mechanism. Do not invent a protein motor or "
                "label a physical causal model NONMECHANISTIC merely to pass "
                "the audit. PHS1 possession or expression does not establish "
                "discharge; the 2014 formation-defect experiments do not "
                "isolate a universal ejection pathway. Negative mirror "
                "transfer can reflect impaired production, release or "
                "subsequent growth. The 2017 study at "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC5550963/ remains an "
                "unread research lead: PMC returned a challenge and two "
                "XML requests failed. It is not counted as verified evidence."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added ballistospore discharge with three directly checked DOI-backed "
            "snippets, a provenance-qualified NPM01 example and explicit "
            "formation/discharge and measured/modeled distinctions. Ignored-and-"
            "hidden searches and structured METPO review found no exact record. "
            "Reserved METPO:1061400 in v537; existing records unchanged. "
            "Physical mechanism evidence is retained; graph formalization is deferred."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    evidence = record["evidence"][0]
    evidence["snippet"] = (
        "At the moment of fusion, Buller's drop snaps from the hilar appendix "
        "onto the adjacent spore surface."
    )
    evidence["notes"] = evidence["notes"].replace(
        "Results and Discussion, opening sentence,", "Introduction, first paragraph,",
    )
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE_SNIPPET",
        changes=(
            "Replaced the subjectless Results fragment with a complete, exact "
            "Introduction sentence describing Buller's-drop fusion (#1781). "
            "Updated the section locator; retained the original minting event "
            "and all experimental and source-access qualifications."
        ),
        llm_assisted=True, timestamp="2026-10-07T09:12:00Z",
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
         "Discharge phenotype, distinct from formation and passive dispersal.", IDENTIFIER],
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
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (
        build_initial_record(), record,
    ):
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
