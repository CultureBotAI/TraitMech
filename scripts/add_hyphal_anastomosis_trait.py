"""Add hyphal anastomosis with source-bounded vegetative fusion evidence."""

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

IDENTIFIER = "traitmech:000605"
TARGET = ROOT / "data/traits/physiology/hyphal_anastomosis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v482"
GIOVANNETTI = "DOI:10.1128/aem.65.12.5571-5575.1999"
CHARLTON = "DOI:10.1128/ec.00191-12"
CROLL = "DOI:10.1111/j.1469-8137.2008.02726.x"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "hyphal anastomosis",
    "definition": (
        "A phenotype in which vegetative fungal hyphae fuse to establish "
        "cytoplasmic continuity."
    ),
    "definition_source": GIOVANNETTI,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [{
        "synonym_text": "vegetative hyphal fusion",
        "synonym_type": "EXACT_SYNONYM",
        "source": CHARLTON,
    }],
    "evidence": [
        {
            "reference": GIOVANNETTI,
            "snippet": (
                "We observed complete fusion of hyphal walls and the migration "
                "of a mass of particles in both directions within the hyphal bridges."
            ),
            "notes": (
                "Giovannetti et al. (1999); snippet exact-matched to the directly "
                "retrieved Europe PMC abstract, PMID:10584019. Publisher Methods, "
                "Results and Discussion were read; actual Figures 1 and 3 were "
                "inspected. Cellophane over water agar supported live observations. "
                "SDH staining visualized active bridges; time-lapse microscopy "
                "showed bidirectional particle passage in Glomus caledonium. "
                "The 0-to-2-second image pairs are representative observations, "
                "not replication counts or identification of each particle as a "
                "nucleus. Same-germling and different-germling/same-isolate "
                "fusion were observed. Tested interspecific failures do not "
                "establish a universal compatibility rule. Nuclear migration "
                "was reported separately; Figure 2 was not visually inspected. "
                "This study did not demonstrate genetic recombination."
            ),
        },
        {
            "reference": CHARLTON,
            "snippet": (
                "Hyphal anastomosis, or vegetative hyphal fusion, establishes "
                "the interconnection of individual hyphal strands into an "
                "integrated network of a fungal mycelium."
            ),
            "notes": (
                "Charlton et al. (2012); snippet exact-matched to the directly "
                "retrieved Europe PMC abstract, PMID:23042130. Publisher Methods "
                "and fusion Results were read; actual Figure 3 was inspected. "
                "This naming sentence supports the exact synonym. Calcofluor "
                "and DIC images compare Epichloe festucae E2368, delta-so268 "
                "and complemented 268C53: connections in wild type and complement, "
                "but separate apposed walls in delta-so268. Static images "
                "indicate apparent cytoplasmic connectivity, not measured flow. "
                "Delta-so238 retained a gene signal and was interpreted as a "
                "heterokaryon/knockdown, not a clean knockout; complementation "
                "of delta-so75 did not restore fusion. Host effects do not "
                "prove that fusion universally causes mutualism. Supplements "
                "were not inspected; no protein-resolved causal chain is asserted."
            ),
        },
        {
            "reference": CROLL,
            "snippet": (
                "We show that genetically distinct AMF, from the same field, "
                "anastomose, resulting in viable cytoplasmic connections through "
                "which genetic exchange could potentially occur."
            ),
            "notes": (
                "Croll et al. (2009); snippet exact-matched to the directly "
                "retrieved Europe PMC abstract, PMID:19140939. Publisher "
                "Experiment 1 methods/results and relevant Discussion were read. "
                "Five Glomus intraradices isolates from one field population "
                "were paired; nine of ten nonself combinations fused, with "
                "subsequent streaming and SDH-positive bridges used to assess "
                "viable continuity. Genetic identity is therefore not required. "
                "The paper separately reports marker transmission to progeny; "
                "its genotyping does not establish nuclear recombination. "
                "Figures and supplementary movies were not visually inspected. "
                "Table 1's PFI/PrFI column-footnote assignments appear transposed "
                "in publisher HTML, so those column-specific rates are not used."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "hyphal-anastomosis-endpoint-and-scope",
            "prompt": "Keep completed vegetative fusion distinct from approach and its consequences.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Directional approach/positive autotropism, contact, adhesion "
                "and branching alone do not establish cytoplasmic continuity. "
                "The definition does not require genetic identity, nuclear "
                "migration, recombination, mating or persistent network viability. "
                "Postfusion incompatibility can follow an actual fusion event. "
                "Unqualified anastomosis also names nonfungal structures and "
                "self-fusion is narrower; neither is an exact synonym here. "
                "The organismal phenotype is not automatically equivalent to "
                "a molecular or cellular process class. Resolve external "
                "equivalents at their authorities before adding xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "hyphal-anastomosis-strains-and-mechanism",
            "prompt": "Resolve modern strain identities and native protein anchors before enrichment.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Canonical examples await modern NCBI identity and original "
                "strain-provenance checks, especially for historical Glomus "
                "names and E2368. Transformed carrot roots in the 2009 culture "
                "method do not establish engineering of the fungi. The 2012 "
                "soft perturbation/rescue supports a native candidate mechanism "
                "but is not a universal dependency. Read its supplements and "
                "resolve taxon-paired protein accessions before adding causal "
                "nodes. Do not infer a ligand/receptor chain from approach or "
                "use NONMECHANISTIC to bypass missing protein grounding."
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
            "Added hyphal anastomosis with three directly retrieved DOI-backed "
            "sources and exact abstract snippets. Distinguished completed "
            "cytoplasmic continuity from approach and downstream genetic effects. "
            "Added source-named vegetative hyphal fusion as an exact synonym. "
            "Ignored-and-hidden repository searches and structured OWL review "
            "found no exact trait. Reserved METPO:1055900 in v482 under released "
            "phenotype. Inspected 1999 Figures 1 and 3 and 2012 Figure 3; kept "
            "unread figures/supplements and mutant limitations explicit. Deferred "
            "canonical strains, external equivalences and protein-resolved graphs."
        ),
        llm_assisted=True, timestamp="2026-10-04T22:09:46Z",
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
        "METPO:1055900", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/hyphal_anastomosis.yaml|{GIOVANNETTI}|{CHARLTON}|{CROLL}",
        "METPO:1000059", "vegetative hyphal fusion", "", "metpo_traitmech_2026_10", "HIGH",
        "Completed vegetative fusion, not approach, mating or recombination.", IDENTIFIER,
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
