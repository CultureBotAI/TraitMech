"""Add negative autotropism with stage-specific directional-growth evidence."""

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

IDENTIFIER = "traitmech:000603"
TARGET = ROOT / "data/traits/physiology/negative_autotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v480"
MONTIEL_RUBIES = "DOI:10.3390/biomimetics10050287"
ROBINSON = "DOI:10.1093/jxb/19.1.125"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "negative autotropism",
    "definition": (
        "A phenotype in which germ-tube emergence or hyphal extension is "
        "directionally biased away from neighboring cells or hyphae of the same species."
    ),
    "definition_source": MONTIEL_RUBIES,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": MONTIEL_RUBIES,
            "snippet": (
                "the hyphae often diverted their growth from their initial "
                "direction away from each other."
            ),
            "notes": (
                "Montiel-Rubies et al. (2025), Section 3.4.1; exact span in directly "
                "retrieved Europe PMC JATS, PMC12109565 (PMID:40422117). "
                "Methods and Sections 3.2/3.4.1 were read; Figure 5 and Table 2 "
                "were visually inspected in the authors' PDF. This is a "
                "retrospective analysis of earlier microfluidic experiments, "
                "not a new independent replication of those datasets. "
                "Side-by-side Pycnoporus cinnabarinus hyphae redirected "
                "laterally where space allowed. Figure 5B instead shows "
                "head-on arrest and cytoplasm retreat, not growth away. "
                "Armillaria mellea divergence could reflect directional memory. "
                "For Neurospora crassa, Table 2 rates side-by-side avoidance "
                "strong and head-on avoidance not observed; prose calls the "
                "latter extremely rare. These qualitative descriptions are "
                "not counts or replication estimates. Supplementary movies "
                "were not inspected. The definition uses the directional-growth "
                "component of this paper's broader usage."
            ),
        },
        {
            "reference": ROBINSON,
            "snippet": (
                "When germinated on agar surfaces the first three species "
                "exhibited negative autotropism, B. cinerea being neutral "
                "in its autotropic behaviour."
            ),
            "notes": (
                "Robinson, Park and Graham (1968), original publisher abstract "
                "directly retrieved from "
                "https://oup.silverchair-cdn.com/article-minimal/447341. "
                "The first three species are Rhizopus stolonifer, Mucor plumbeus "
                "and Trichoderma viride. Spore-pair assays concern orientation "
                "of germ-tube emergence, not demonstrated subsequent tip bending. "
                "Cellophane increased their negative response; Botrytis cinerea "
                "was neutral on agar and positive on Cellophane, so is not a "
                "negative exemplar here. Germination timing and cis-ness are "
                "separate readouts, not substitutes for orientation. The full "
                "paper, figures, strain provenance and sample sizes were not "
                "retrieved; proposed mechanisms in the abstract are not "
                "established causal pathways."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "negative-autotropism-direction-and-self-scope",
            "prompt": "Retain directional growth and stage-specific self-avoidance boundaries.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The directional phenotype includes initial germ-tube orientation "
                "and later hyphal redirection without requiring both in one "
                "organism. Same-species neighbors can include branches of one "
                "mycelium or separate spores; this does not assert genetic "
                "identity, vegetative incompatibility or a self-recognition "
                "receptor. Positive autotropism and hyphal fusion are not exact "
                "synonyms. Whole-cell taxis, growth inhibition, branching, "
                "passive bending and cytoplasm retreat alone are insufficient. "
                "The 2025 head-on category is broader than this record's "
                "directional scope. Do not infer chemotropism or aerotropism "
                "parentage from proposed inhibitory cues or oxygen depletion. "
                "Resolve external equivalents before adding xrefs or synonyms."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "negative-autotropism-provenance-and-mechanism",
            "prompt": "Resolve natural strain provenance and causal signals before enrichment.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Canonical examples are deferred until the original strain "
                "sources and NCBI identities are verified. The 1968 full paper "
                "remains unread; the 2025 Methods refer strain culture details "
                "to earlier studies and include a ro-1 mutant whose origin "
                "has not been verified here. Mutation alone does not establish "
                "genetic engineering or natural provenance. Inspect the original imaging datasets "
                "and movies before quantitative prevalence claims. Spatial "
                "constraints, directional memory and local resource gradients "
                "remain competing contributors. Neither paper establishes "
                "a universal signal/receptor chain. Resolve direct native "
                "perturbation evidence and taxon-paired protein accessions "
                "before a causal graph; NONMECHANISTIC is not a grounding bypass."
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
            "Added negative autotropism with two directly retrieved DOI-backed "
            "sources and exact snippets. Distinguished germ-tube emergence from "
            "hyphal redirection and excluded head-on arrest/retreat alone. "
            "Ignored-and-hidden searches and structured OWL review found no "
            "exact term. Reserved METPO:1055700 in v480 under released phenotype. "
            "Inspected Figure 5 and Table 2; retained retrospective-data, "
            "qualitative-assay and abstract-only limitations. Deferred "
            "canonical strains, external equivalents and molecular mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-04T20:13:46Z",
    )
    record_curation_event(
        record, curator="codex", action="QUALIFY_STRAIN_PROVENANCE",
        changes=(
            "Issue #1684: removed the unsupported engineered qualifier for "
            "ro-1. The directly read source identifies a mutant but does not "
            "establish its origin; neither engineering nor natural provenance "
            "is inferred from mutation alone. Original mint history is preserved."
        ),
        llm_assisted=True, timestamp="2026-10-04T20:20:10Z",
    )
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
        "METPO:1055700", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/negative_autotropism.yaml|{MONTIEL_RUBIES}|{ROBINSON}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Directional self-avoidance; emergence and extension are distinct readouts.",
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
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
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
