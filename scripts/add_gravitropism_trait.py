"""Add gravity-directed growth with bounded fungal evidence."""

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

IDENTIFIER = "traitmech:000599"
TARGET = ROOT / "data/traits/physiology/gravitropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v476"
ZIVANOVIC = "DOI:10.4161/cib.22291"
GALLAND = "DOI:10.1078/0176-1617-01082"
BRAUN = "DOI:10.1007/s004250050744"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "gravitropism",
    "definition": (
        "A phenotype in which growth is directionally oriented or reoriented "
        "in response to gravity."
    ),
    "definition_source": ZIVANOVIC,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": ZIVANOVIC,
            "snippet": (
                "Phycomyces sporangiophores grow in the air and display negative "
                "gravitropic bending upon displacement from vertical position."
            ),
            "notes": (
                "Intracellular Reorganization upon Gravistimulation; exact "
                "contiguous Europe PMC full-text XML (PMID:23650568; PMC3642927). "
                "The full article and all three figure images were inspected. "
                "Figure 1 shows bending growth of an intact wild-type stage I "
                "sporangiophore after a 45-degree tilt; no strain identifier "
                "is given. Figure 2 concerns intracellular reorganization, "
                "and Figure 3 measures touch-induced ion fluxes, not a gravity "
                "assay. The author explicitly leaves open whether vacuolization "
                "reflects gravity signaling or coincident development. The "
                "article declares no supplement; the Europe PMC supplementaryFiles "
                "download contained ordinary figure assets."
            ),
        },
        {
            "reference": GALLAND,
            "snippet": (
                "The threshold for the polar angle of the wild type NRRL 1555 "
                "(with crystals) is near 8 x 10(-2) x g."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:15266721). "
                "A clinostat centrifuge measures negative gravitropic bending "
                "of Phycomyces blakesleeanus sporangiophores. Polar angle and "
                "aiming-error angle are distinct readouts; the quoted value "
                "belongs to the wild-type polar angle, not the mutant strains "
                "or aiming error. It is assay-specific, not a universal "
                "threshold. Subscription full text and figures were not inspected."
            ),
        },
        {
            "reference": BRAUN,
            "snippet": (
                "In rhizoids, positive gravitropic curvature is caused by "
                "differential growth limited to the opposite subapical flanks "
                "of the apical dome"
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:10550622). "
                "The primary Chara study describes downward-positive rhizoid "
                "growth and upward-negative protonematal growth. This supports "
                "polarity-neutral terminology, not positive gravitropism in "
                "Phycomyces. The remainder of the quoted sentence excludes "
                "displacement of the rhizoid growth centre, calcium gradient "
                "or channels. No Chara mechanism or canonical taxon is "
                "transferred to the fungus; full text and figures were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:763407",
            "taxon_label": "Phycomyces blakesleeanus NRRL 1555(-)",
            "reference": GALLAND,
            "note": (
                "Wild-type sporangiophore negative gravitropic bending in "
                "the clinostat-centrifuge study, with a source-qualified polar-angle "
                "threshold. This is not a mutant example and is not assigned "
                "the unnamed 2013 study's stage I observations. Natural-isolate "
                "provenance: DOI:10.1128/EC.00203-13, Materials and Methods, "
                "Strains and growth conditions "
                "(https://pmc.ncbi.nlm.nih.gov/articles/PMC3910969/); NRRL1555 "
                "is distinguished from backcrossed A56. Exact strain name and "
                "rank resolved directly at NCBI Taxonomy on 2026-10-04."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "gravitropism-growth-and-direction-boundaries",
            "prompt": "Keep gravity-guided growth separate from swimming and passive motion.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The class includes positive or negative directional growth "
                "without requiring both in one organism or condition. It is "
                "not gravitaxis (swimming orientation), gravikinesis "
                "(propulsion-speed change), passive settling, flotation or "
                "sagging, or gravity-dependent growth rate alone. The "
                "Phycomyces evidence here is negative. Resolve phenotype-level "
                "external equivalences before adding xrefs or synonyms."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "gravitropism-native-mechanism-grounding",
            "prompt": "Discriminate gravity signaling from touch and coincident development.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Bending observations do not resolve a complete molecular "
                "mechanism. Vacuolization can coincide with development; "
                "touch-induced ion fluxes do not establish gravity-triggered "
                "channel activity. The 2004 abstract compares strains with "
                "and without crystals but does not identify a universal "
                "sole gravity sensor. Inspect its full text and resolve "
                "eligible taxon-paired protein accessions before adding a "
                "mechanistic graph. Do not use NONMECHANISTIC to bypass "
                "grounding requirements or transfer Chara signaling to fungi."
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
            "Added gravitropism with two primary fungal studies, a primary "
            "direction-terminology source and exact snippets. Ignored-and-hidden "
            "novelty searches and structured OWL review found no exact record "
            "or METPO term. Reserved METPO:1055300 in v476. Kept growth "
            "distinct from locomotion and passive motion; inspected the 2013 "
            "full text and figures. Added a natural NRRL1555 exemplar tied "
            "only to the 2004 assay, and deferred unresolved mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-04T15:37:17Z",
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
        "METPO:1055300", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/gravitropism.yaml|{ZIVANOVIC}|{GALLAND}|{BRAUN}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Gravity-directed growth; polarity-neutral, not swimming or passive displacement.",
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
