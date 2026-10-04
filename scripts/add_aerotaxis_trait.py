"""Add aerotaxis with directional evidence and a qualified environmental isolate."""

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

IDENTIFIER = "traitmech:000589"
TARGET = ROOT / "data/traits/physiology/aerotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v466"
SHIOI = "DOI:10.1128/jb.169.7.3118-3123.1987"
ZHULIN = "DOI:10.1128/jb.178.17.5199-5204.1996"
BOUVARD = "DOI:10.1103/PhysRevE.106.034404"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "aerotaxis",
    "definition": (
        "A motile phenotype in which active locomotion is directionally biased "
        "along an oxygen concentration gradient toward preferred oxygen conditions."
    ),
    "definition_source": ZHULIN,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": SHIOI,
            "snippet": (
                "at high concentrations, oxygen was a repellent of Salmonella "
                "typhimurium, Escherichia coli, and some bacilli"
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:3036771); full text "
                "not inspected. The study contrasts high-oxygen repulsion with "
                "attraction at lower concentrations and reports temporal assays. "
                "This supports concentration-dependent response direction, not "
                "universal thresholds or a requirement that every organism "
                "exhibit both signs. The abstract's tentative receptor "
                "interpretation is not promoted to an established mechanism."
            ),
        },
        {
            "reference": ZHULIN,
            "snippet": (
                "As a result of aerotaxis, the bacteria were attracted to a "
                "specific low concentration of oxygen (3 to 5 microM)."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:8752338); full text "
                "not inspected. Azospirillum brasilense forms a band in a "
                "spatial oxygen gradient and returns when swimming into higher "
                "or lower oxygen; temporal gradients corroborate the response. "
                "The preferred interval is experiment-specific. Proton motive "
                "force peaks in the same interval, but its proposed signaling "
                "role remains a hypothesis, not a protein-resolved causal edge. "
                "No strain-level canonical example is inferred from the abstract."
            ),
        },
        {
            "reference": BOUVARD,
            "snippet": (
                "runs in the direction of the oxygen source (x < 0) are "
                "longer and more frequent."
            ),
            "notes": (
                "Section II.B, page 3; published 2022-09-15. Published full text "
                "and Appendices A-E read at the author's institutional copy: "
                "https://www.fast.universite-paris-saclay.fr/~moisy/papers/2022_bouvard_pre.pdf. "
                "Figures 1-2 and the typeset x < 0 passage visually checked. "
                "Tracking in an oxygen-gradient capillary shows directional "
                "bias in Burkholderia contaminans; nonmotile cells are excluded "
                "with a 6 micrometre-per-second velocity threshold. The fitted "
                "response model does not identify a molecular receptor."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:488447",
            "taxon_label": "Burkholderia contaminans",
            "reference": BOUVARD,
            "note": (
                "Section II.A describes an unnamed environmental strain, "
                "identified using 16S and recA fragments and selected for strong "
                "aerotaxis. Figure 2 reports the motile subpopulation's bias "
                "toward the oxygen source. NCBI resolved 488447 on 2026-10-04 "
                "at species rank, not as this exact isolate. This is not a "
                "universal strain or cell-level claim."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "aerotaxis-direction-and-mapping-boundaries",
            "prompt": "Preserve oxygen-directed scope and verify external equivalents.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Preferred oxygen need not be the highest available oxygen. "
                "Oxygen-dependent growth, respiration, tolerance and speed "
                "changes alone do not establish directional locomotion. "
                "Aerotaxis is narrower than general chemotaxis, while magnetic "
                "alignment and magnetoaerotaxis are not exact synonyms. The "
                "existing chemotaxis record is flagellar-specific; motile is "
                "the verified broader METPO parent without imposing that "
                "apparatus. No external xref or synonym is asserted before "
                "authority resolution and an organismal-disposition scope check."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "aerotaxis-mechanism-and-isolate-grounding",
            "prompt": "Ground molecular branches and the exact environmental isolate.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "A proton-motive-force correlation or a fitted response law "
                "does not establish a universal oxygen receptor or molecular "
                "pathway. Add causal graphs only after direct primary evidence "
                "and taxon-paired protein accessions have been verified; no "
                "NONMECHANISTIC graph bypasses this requirement. The canonical "
                "example lacks a published strain designation or accession; "
                "retain its species-level and motile-subpopulation qualifiers "
                "until isolate-specific identity can be resolved."
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
            "Added aerotaxis with three primary DOI citations and exact snippets. "
            "Ignored-and-hidden searches found no exact live trait or METPO term. "
            "Reserved METPO:1054300 in v466. Kept attraction and repulsion "
            "within concentration-dependent directional scope, added a qualified "
            "NCBI-resolved environmental-isolate example, and deferred "
            "unverified molecular mechanisms and external mappings."
        ),
        llm_assisted=True, timestamp="2026-10-04T06:09:08Z",
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
        "METPO:1054300", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/aerotaxis.yaml|{ZHULIN}|{SHIOI}|{BOUVARD}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Oxygen-directed locomotion; not necessarily toward higher oxygen.",
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
