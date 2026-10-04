"""Add osmotaxis while separating migration from uniform-shock motility data."""

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

IDENTIFIER = "traitmech:000592"
TARGET = ROOT / "data/traits/physiology/osmotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v469"
LESLIE = "DOI:10.1016/s0014-4894(03)00031-6"
BARROS = "DOI:10.1016/j.exppara.2005.10.005"
ROSKO = "DOI:10.1073/pnas.1620945114"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "osmotaxis",
    "definition": (
        "A motile phenotype in which active locomotion produces net migration "
        "in response to a spatial gradient in external osmotic conditions."
    ),
    "definition_source": LESLIE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": LESLIE,
            "snippet": (
                "We find that promastigotes move towards concentrations of all "
                "substances tested and that this taxis requires the presence "
                "of an osmotic gradient."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:12706748); full "
                "text not inspected. The study concerns Leishmania mexicana "
                "promastigotes and supports migration requiring an osmotic "
                "gradient under the tested conditions. The authors reinterpret "
                "those responses as osmotaxis; this is not evidence that all "
                "chemical-gradient responses in Leishmania are osmotic, or "
                "that every substance or life stage elicits this behavior. "
                "No universal preferred osmolarity or natural-strain example "
                "is inferred from the abstract."
            ),
        },
        {
            "reference": BARROS,
            "snippet": (
                "These were able to respond to chemotaxic as well as to "
                "osmotaxic stimuli."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:16313904); full "
                "text not inspected. The antecedent is Leishmania promastigotes; "
                "the article identifies Leishmania amazonensis. The authors "
                "report distinguishing chemical from osmotic responses, "
                "supporting osmotaxis without collapsing all chemotaxis into "
                "it. Their receptor model and possible vector-development "
                "role are not established as universal mechanisms or required "
                "trait consequences."
            ),
        },
        {
            "reference": ROSKO,
            "snippet": (
                "We discuss how the speed changes we observe can lead to "
                "steady-state bacterial accumulation."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:28874571); full "
                "text and supplement not systematically inspected. Escherichia "
                "coli motor and population-swimming measurements concern "
                "stepwise osmotic changes. The snippet states a proposed link "
                "from measured speed changes to accumulation, not a direct "
                "spatial-gradient migration result from those measurements. "
                "Osmokinesis and motor bias may contribute to osmotaxis but "
                "are not exact synonyms or sufficient evidence of net migration "
                "on their own; no molecular causal edge is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "osmotaxis-spatial-and-chemical-boundaries",
            "prompt": "Separate osmotic migration from tolerance, kinesis and chemical specificity.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Osmotic stress survival, growth salinity preference, water "
                "balance, and speed or tumbling changes after a uniform shock "
                "do not alone establish net migration through a spatial "
                "gradient. Exclude passive transport, osmotic water movement "
                "and differential growth as sole evidence. Osmokinesis is "
                "not an exact synonym, even when it contributes to spatial "
                "redistribution. Solute-specific chemotaxis can coexist with "
                "osmotaxis, as the Barros study reports; the Leslie result "
                "does not negate it universally. The local chemotaxis record "
                "imposes flagellar motor switching, so motile is used as the "
                "verified broader parent. External equivalents remain unasserted "
                "pending authority and organismal-scope checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "osmotaxis-mechanism-and-canonical-strains",
            "prompt": "Verify strain and life-stage provenance before adding examples or mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The studies support a microbial osmotic-gradient response "
                "without identifying one universal receptor or movement "
                "apparatus. Inspect full studies and relevant supplements, "
                "distinguish spatial observations from temporal-shock "
                "measurements and model interpretations, and resolve "
                "taxon-paired protein accessions before adding molecular "
                "causal graphs. Verify unperturbed natural strain provenance "
                "and NCBI identity before adding canonical examples; "
                "promastigote observations must retain their life-stage "
                "restriction. A NONMECHANISTIC graph must not bypass those "
                "requirements."
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
            "Added osmotaxis with three primary DOI citations and exact "
            "abstract snippets. Ignored-and-hidden searches and structured "
            "OWL review found no exact live record or METPO term. Reserved "
            "METPO:1054600 in v469. Distinguished spatial migration from "
            "uniform-shock motility measurements, retained coexistence with "
            "solute-specific chemotaxis, and deferred unverified strain "
            "examples, molecular mechanisms and external equivalents."
        ),
        llm_assisted=True, timestamp="2026-10-04T08:45:40Z",
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
        "METPO:1054600", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/osmotaxis.yaml|{LESLIE}|{BARROS}|{ROSKO}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Net osmotic-gradient migration; speed changes alone are insufficient.",
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
