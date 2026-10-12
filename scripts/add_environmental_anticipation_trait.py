"""Add cue-triggered environmental anticipation through the validated writer."""

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
SLUG = "cue_triggered_environmental_anticipation"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v583/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000707"
METPO_ID = "METPO:1066000"
REGULATORY = "DOI:10.1038/nature08112"
METABOLIC = "DOI:10.1038/nmicrobiol.2017.84"
TIMESTAMP = "2026-10-12T05:07:15Z"
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
    "label": "cue-triggered environmental anticipation",
    "definition": (
        "A physiological phenotype in which exposure to an environmental cue "
        "induces changes that prepare a microorganism for a distinct, temporally "
        "associated environmental condition before that condition occurs."
    ),
    "definition_source": REGULATORY,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": REGULATORY,
            "snippet": (
                "early stimuli pre-induce genes that would be needed for later "
                "ones, yet later stimuli only induce genes needed to cope with them."
            ),
            "notes": (
                "Mitchell et al. 2009, PMID:19536156; scientific abstract, checked "
                "against publisher and source-qualified MED text. Main Figures 2-3 "
                "and supplementary Figures 3 and 6 were visually inspected, with "
                "their relevant Methods and control explanations. MG1655 sugar-switch "
                "assays distinguish early induction from subsequent growth; "
                "glycerol normalization and residual-sugar controls matter. Loss "
                "of the association in laboratory-evolved strains concerns selection "
                "across generations, not cognitive learning. Ecological explanations "
                "remain author interpretations. Not all raw data were reanalyzed."
            ),
        },
        {
            "reference": METABOLIC,
            "snippet": (
                "Here, we identify a metabolic adaptation that is triggered upon "
                "entry into hypoxia-induced quiescence but facilitates subsequent "
                "cell cycle re-entry."
            ),
            "notes": (
                "Eoh et al. 2017, PMID:28530656, PMC5540153; scientific abstract, "
                "checked against publisher and source-qualified MED text. The "
                "abstract and qualitative main-text framing support metabolically "
                "encoded preparation, with hypoxia preceding re-aeration in the "
                "studied Mycobacterium tuberculosis system. This is not evidence "
                "for a universal transcriptional mechanism or an in-vivo "
                "demonstration of anticipation. Figures, supplements and raw data "
                "were not independently assessed; no molecular causal edges are asserted."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "anticipation-scope-and-hierarchy",
            "prompt": "Retain cue-dependent preparation without conflating neighboring temporal-response traits.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The cue-triggered qualifier is deliberate: solely clock-driven "
                "preparation or constitutive readiness is insufficient. Evidence "
                "must link the preceding cue to preparation for a different later "
                "condition; correlated expression or cross-protection alone does "
                "not establish that interpretation. Generic stress response, "
                "stochastic bet hedging, carbon-source memory and diauxic growth "
                "are not exact synonyms, although particular observations can "
                "overlap. Neither cognition nor learning within an individual's "
                "lifetime is required; evolutionary regulatory wiring is compatible. "
                "No universal benefit, fixed delay, asymmetric response or single "
                "mechanism is required. METPO:1000731 nutrient adaptation is "
                "locally framed as chronic copiotroph/oligotroph trophic adaptation, "
                "not this cue-to-future-condition phenotype. METPO:1000059 phenotype "
                "is the conservative parent pending upstream hierarchy review. "
                "This is an organismal disposition, not a sequence feature, "
                "regulatory site or precomposed chemical-use assertion."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "anticipation-evidence-and-mechanism-limits",
            "prompt": "Resolve assay-specific mechanisms, natural strain provenance and broader terminology before extending the record.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical_examples, causal_graphs, exact synonyms or xrefs "
                "are asserted. The studies do not establish a uniform species-wide "
                "phenotype or a common protein mechanism; strain provenance and "
                "authority-resolved taxa require further review. Source-qualified "
                "MED, Crossref and visible publisher notice links were checked "
                "on 2026-10-12; their commentary/review links are not corrections "
                "or independent experiments. No correction or retraction was "
                "exposed for the two retained papers in these bounded checks. "
                "The separate Tagkopoulos 2008 lead (DOI:10.1126/science.1154456) "
                "is not counted evidence: its main PMC text was readable, but "
                "the indexed 9 June 2008 supplement correction could not be "
                "directly inspected. Broad environmental anticipation and adaptive "
                "prediction are not assumed exactly equivalent to this qualified "
                "class. No exact candidate was found in the pinned/current METPO "
                "RDF and ignored/hidden novelty searches; the pinned ontology "
                "remains unchanged."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cue-triggered environmental anticipation with two primary "
            "DOI-backed sources and directly checked scientific-abstract snippets. "
            "Reserved 000707, v583 and 1066000-1066099 after ignored/hidden "
            "worktree and pending-PR checks. Scope, mechanism, provenance and "
            "source-access limits are explicit. Existing traits unchanged; "
            "timestamp is the observed UTC curation decision."
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
         "Cue-triggered preparation for a distinct later condition; not a sequence feature.", IDENTIFIER],
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
