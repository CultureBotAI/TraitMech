"""Add pH taxis as an external-gradient-directed motility phenotype."""

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

IDENTIFIER = "traitmech:000591"
TARGET = ROOT / "data/traits/physiology/ph_taxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v468"
TOHIDIFAR = "DOI:10.1128/jb.00491-19"
CROXEN = "DOI:10.1128/jb.188.7.2656-2665.2006"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "pH taxis",
    "definition": (
        "A motile phenotype in which active locomotion is directionally biased "
        "in response to an external pH gradient."
    ),
    "definition_source": TOHIDIFAR,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": TOHIDIFAR,
            "snippet": (
                "This bacterium was found to perform bidirectional taxis in "
                "response to external pH gradients, enabling it to preferentially "
                "migrate to neutral environments."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:31685537). "
                "The antecedent is Bacillus subtilis. This observation supports "
                "external-gradient-directed movement, including responses from "
                "both acidic and alkaline environments in this study. It does "
                "not establish neutral pH as a universal preferred destination. "
                "Full text was not systematically inspected; receptor-chimera "
                "findings in the abstract are not converted into a molecular "
                "causal graph or an unqualified natural-strain example."
            ),
        },
        {
            "reference": CROXEN,
            "snippet": (
                "Bacteria in more-alkaline regions did not swim toward the acid, "
                "suggesting the pH taxis is a form of negative chemotaxis."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:16547053); full "
                "text not inspected. The preceding observation describes "
                "Helicobacter pylori moving away from strong acid in a "
                "microscope-slide pH gradient. This supports an acid-avoidance "
                "response without requiring every pH-tactic organism to show "
                "bidirectional attraction to a neutral optimum. Strain-specific "
                "mutant, receptor and host-colonization findings are not "
                "generalized into the trait definition or mechanism."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "ph-taxis-scope-and-mapping-boundaries",
            "prompt": "Preserve directional scope and verify external equivalents.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Growth pH preference, acid or alkali tolerance, intracellular "
                "pH homeostasis and changes in speed alone do not establish "
                "pH-directed locomotion. Neither neutral-pH attraction nor "
                "bidirectional response is required universally. The local "
                "chemotaxis definition specifies flagellar motor switching; "
                "motile is the verified broader METPO parent without imposing "
                "that apparatus. No external xref or exact synonym is asserted "
                "before authority resolution and organismal-scope comparison."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "ph-taxis-mechanism-and-canonical-strains",
            "prompt": "Verify natural strain provenance and protein-resolved mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The primary abstracts establish pH-tactic behavior, not a "
                "single universal receptor mechanism. Before adding canonical "
                "examples, verify the unperturbed reference strains against "
                "primary strain-provenance sources and resolve their NCBI "
                "taxon identities. Before adding a causal graph, inspect the "
                "full studies and relevant supplements, distinguish observed "
                "perturbation effects from proposed sensing models, and "
                "resolve taxon-paired protein accessions. A NONMECHANISTIC "
                "graph must not bypass those requirements."
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
            "Added pH taxis with two primary DOI citations and exact abstract "
            "snippets. Ignored-and-hidden searches and structured OWL review "
            "found no exact live record or METPO term. Reserved METPO:1054500 "
            "in v468. Deferred unverified strain examples, molecular graph "
            "grounding and external equivalents; retained directional scope "
            "without universal neutral-pH or bidirectionality requirements."
        ),
        llm_assisted=True, timestamp="2026-10-04T08:03:18Z",
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
        "METPO:1054500", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/ph_taxis.yaml|{TOHIDIFAR}|{CROXEN}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Directional response to external pH; not pH tolerance or speed alone.",
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
