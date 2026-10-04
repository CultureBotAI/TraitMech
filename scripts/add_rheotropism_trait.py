"""Add flow-directed growth with source-qualified fungal evidence."""

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

IDENTIFIER = "traitmech:000600"
TARGET = ROOT / "data/traits/physiology/rheotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v477"
MULLER = "DOI:10.1016/S0006-3495(65)86719-4"
OH = "DOI:10.1016/S0168-1656(97)00147-8"
METRAUX = "DOI:10.1007/BF00397538"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "rheotropism",
    "definition": (
        "A phenotype in which growth is directionally oriented or reoriented "
        "in response to fluid flow."
    ),
    "definition_source": MULLER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": MULLER,
            "snippet": (
                "Sparsely sowed, hence independent Botrytis spores, which are "
                "fixed to the wall of a laminar flow chamber, tend to germinate downstream."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:19431336). "
                "The author-hosted full text was inspected at "
                "https://mterasaki.us/cellbio/lfjaffe/reprints/65bj2.pdf. "
                "Methods identify Botrytis cinerea without a strain accession. "
                "Figures 3 and 4 (pages 322 and 324) measure downstream "
                "outgrowth orientation, not simply germination rate. Tables VI "
                "and VII (page 329) test viscosity and rotation confounds; "
                "these figures and tables were visually checked. The proposed "
                "self-emitted diffusible stimulator is an indirect mechanistic "
                "inference, not an identified molecule or receptor. Initial "
                "outgrowth localization is not evidence of later tip reorientation."
            ),
        },
        {
            "reference": OH,
            "snippet": (
                "Hyphal tips quickly reoriented towards the upstream of the "
                "flowing medium and became aligned parallel to the flow axis "
                "as they grew larger."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:9470224). "
                "Attached Aspergillus niger hyphae were tested in flowing liquid "
                "medium. Other tested fungi showed upstream hyphal and branch "
                "growth without polarized germ-tube emergence. The inlet/outlet "
                "pH and oxygen measurements do not exclude every local chemical "
                "gradient or identify a flow receptor. Strain identity, full "
                "text and figures were not verified; claims are abstract-limited."
            ),
        },
        {
            "reference": METRAUX,
            "snippet": (
                "When the spph was placed in a laminar flow of air, it grew "
                "into the wind within 2-4 min."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:24258181). "
                "The sporangiophore (spph) of Phycomyces blakesleeanus "
                "exhibits upstream growth in air, establishing that this "
                "usage of rheotropism is not limited to liquid currents. "
                "Added ethylene did not remove the response; that result "
                "does not identify its mediator or establish a universal "
                "ethylene-independent mechanism. The barrier-avoidance assay "
                "is distinct from the wind assay. Strain identity, full text "
                "and figures were not verified; claims are abstract-limited."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "rheotropism-growth-flow-and-direction-boundaries",
            "prompt": "Keep flow-directed growth distinct from swimming and passive transport.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The class includes upstream or downstream growth in liquid "
                "or gas without requiring both directions or media in one "
                "organism. Rheotaxis concerns self-propelled movement, not "
                "growth orientation. Passive bending, advection, alignment "
                "and growth-rate changes alone are insufficient. Initiation "
                "of polarized growth and subsequent tip reorientation are "
                "different readouts. Resolve external phenotype equivalences "
                "and the scope of wind-response labels before adding xrefs "
                "or synonyms; do not split a lexical variant into another trait."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "rheotropism-native-mechanism-and-exemplars",
            "prompt": "Resolve strain provenance and discriminate mechanical from chemical cues.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Flow can redistribute chemical signals as well as impose "
                "mechanical forces. Do not require a direct mechanoreceptor "
                "or transfer a mechanism across species, growth stages or "
                "fluid media. Inspect the remaining full texts and establish "
                "natural strain provenance and NCBI identity before adding "
                "canonical examples. Resolve native causal evidence and "
                "taxon-paired protein accessions before a mechanistic graph; "
                "do not use NONMECHANISTIC to bypass grounding requirements."
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
            "Added polarity-neutral rheotropism with three primary fungal "
            "citations and exact abstract snippets. Ignored-and-hidden novelty "
            "searches and structured OWL review found no exact term. Reserved "
            "METPO:1055400 in v477. Inspected the 1965 full text and orientation "
            "figures and controls; retained abstract-only access limits for "
            "the other studies. Deferred unresolved canonical strains and "
            "molecular mechanisms, and distinguished growth from rheotaxis."
        ),
        llm_assisted=True, timestamp="2026-10-04T16:43:59Z",
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
        "METPO:1055400", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/rheotropism.yaml|{MULLER}|{OH}|{METRAUX}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Flow-directed growth; either polarity in liquid or gas, not swimming or passive motion.",
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
