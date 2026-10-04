"""Add chemical-gradient-directed polarized growth with bounded fungal evidence."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000597"
TARGET = ROOT / "data/traits/physiology/chemotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v474"
YAMAMOTO = "DOI:10.1371/journal.pbio.3002726"
SRIDHAR = "DOI:10.1038/s41598-020-67597-z"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "chemotropism",
    "definition": (
        "A phenotype in which polarized growth is directionally biased "
        "in response to a spatial chemical gradient."
    ),
    "definition_source": YAMAMOTO,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": YAMAMOTO,
            "snippet": (
                "Notably, many hyphae changed direction near the boundary, "
                "opting to remain in the pH 6.5 layer (Fig 3B)."
            ),
            "notes": (
                "Results, Chemotropism to low pH; exact span in Europe PMC "
                "full text PMC11288418 (PMID:39078817), published 2024-07-30. "
                "The compared layers are pH 6.5 and 8. Figure 3 was visually "
                "inspected: tip trajectories support directional growth, "
                "not only greater biomass. Main Results and the primary "
                "abstract describe lower-pH preference in these comparisons; "
                "the separate summary abstract's acidic-pH avoidance wording "
                "conflicts with them. Growth inhibition at pH 3 and carbon-source "
                "growth differences confound those comparisons. The nitrogen "
                "Results separately report negative chemotropism. S1 Table "
                "(10.1371/journal.pbio.3002726.s002), inspected as PDF text "
                "and image, lists engineered backgrounds including TH122; "
                "no natural canonical strain is inferred. Other supplements "
                "and movies were not inspected."
            ),
        },
        {
            "reference": SRIDHAR,
            "snippet": (
                "They respond to changes in their environment by directing "
                "hyphal growth towards or away from a range of chemical stimuli."
            ),
            "notes": (
                "Introduction, first paragraph; They refers to filamentous "
                "fungi. Exact span in Europe PMC full text PMC7329813 "
                "(PMID:32612109). This supports the polarity-neutral growth "
                "definition. The first Results subsection reports directional "
                "growth of Fusarium graminearum towards methionine, while "
                "rapid growth with other tested nitrogen compounds was not "
                "significantly directional. Table 1 identifies GZ-3639 as "
                "wild type, but natural provenance and an exact NCBI identity "
                "were not independently verified. Figures and supplements "
                "were not visually inspected. The paper's receptor and "
                "infection findings are not transferred into a universal "
                "chemotropism mechanism or canonical example."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "chemotropism-growth-and-source-boundaries",
            "prompt": "Preserve direction, growth-rate and source-summary distinctions.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This class covers positive and negative chemical-gradient "
                "responses of polarized growth, not whole-cell locomotion. "
                "Use phenotype rather than motile as the parent. Neither "
                "increased biomass, faster extension nor asymmetric branching "
                "alone establishes directed growth. Keep chemotaxis, contact "
                "guidance and electric-field growth distinct. The Yamamoto "
                "summary abstract conflicts with the main Results on the "
                "pH-response direction; retain the inspected Results and "
                "Figure 3 context rather than silently harmonizing them. "
                "External equivalences and lexical variants require separate "
                "authority and scope checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "chemotropism-strain-and-mechanism-grounding",
            "prompt": "Resolve natural strain provenance and accession-level mechanism evidence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Keep laboratory-strain observations as qualified evidence. "
                "Verify natural provenance and NCBI identities before adding "
                "canonical examples; wild-type labels and no-auxotrophy "
                "controls do not establish an unengineered strain. The "
                "Aspergillus PmaA perturbation also affects growth and acid "
                "tolerance, so it does not isolate a dedicated chemical "
                "sensor. Inspect remaining figures and supplements and resolve "
                "taxon-paired protein accessions before adding a causal graph. "
                "Do not generalize stimulus-specific perturbations into a "
                "universal pathway or use a NONMECHANISTIC graph to bypass "
                "missing molecular evidence."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added chemotropism with two primary DOI citations and exact "
            "full-text snippets. Ignored-and-hidden novelty searches and "
            "structured OWL review found no exact record or METPO term. "
            "Reserved METPO:1055100 in v474. Distinguished polarized growth "
            "from locomotion and growth-rate changes; retained both gradient "
            "directions and documented conflicting summary wording. Inspected "
            "Aspergillus Figure 3 and S1 strain table. Deferred natural "
            "canonical examples and accession-level causal mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-04T13:41:09Z",
    )
    record_curation_event(
        record, curator="codex", action="CORRECT_EVIDENCE_SNIPPET",
        changes=(
            "Raw JATS matching caught a dropped figure pointer in the "
            "uncommitted Yamamoto draft quote. Restored (Fig 3B) before "
            "the sentence-ending period to preserve the contiguous source span."
        ),
        llm_assisted=True, timestamp="2026-10-04T13:44:00Z",
    )
    return record


def initial_draft() -> dict:
    """Accept only the exact locally written draft when repairing its quote."""
    record = build_record()
    record["curation_history"].pop()
    record["evidence"][0]["snippet"] = record["evidence"][0]["snippet"].replace(" (Fig 3B)", "")
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1055100", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/chemotropism.yaml|{YAMAMOTO}|{SRIDHAR}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Chemical-gradient-directed polarized growth; polarity-neutral, not locomotion.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (record, initial_draft()):
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
