"""Add pallium-mediated feeding without asserting a universal membrane topology."""

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
TARGET = ROOT / "data/traits/physiology/pallium_feeding.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v508/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000632"
METPO_ID = "METPO:1058500"
DEFINITION = "DOI:10.1111/j.1529-8817.1986.tb00021.x"
ULTRASTRUCTURE = "DOI:10.1111/j.0022-3646.1992.00069.x"
GROWTH = "DOI:10.4319/lo.1993.38.5.0965"
PROVENANCE = "https://www.whoi.edu/cms/files/Jacobson_%26_Anderson_1986_JP_feeding_30828.pdf"
STRUCTURE_URL = (
    "https://www.whoi.edu/cms/files/"
    "Jacobson%26Anderson_1992_Proto-ultrastructrure_31161.pdf"
)
TIMESTAMP = "2026-10-06T01:50:09Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "pallium feeding",
    "definition": (
        "A physiological phenotype in which a microbial organism feeds by "
        "enveloping all or part of particulate food in an extruded membranous "
        "pallium, digesting it outside the main cell body, and taking up "
        "released nutrients."
    ),
    "definition_source": DEFINITION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": (
                "The contents of the phytoplankton prey are liquified and "
                "transported through the pallium"
            ),
            "notes": (
                "Direct scientific Abstract quote, printed p. 249; original "
                "spelling retained. Institutional scan: " + PROVENANCE + ". "
                "All seven available pages (249-252, 256-258), Table 1 and "
                "actual Figures 1, 2 and 23 were inspected. Pages 253-255 "
                "and Figures 3-22 are missing from this copy and were not "
                "audited. Figure 2B shows Oblea rotunda feeding on "
                "Pyramimonas sp. Discussion p. 256 distinguishes complete "
                "from partial enclosure; Table 1 also lists detrital food. "
                "Neither living prey nor a particular prey size, taxon, "
                "capture filament or digestion time is a universal requirement."
            ),
        },
        {
            "reference": ULTRASTRUCTURE,
            "snippet": "the prey cytoplasm is liquified within the pallium",
            "notes": (
                "Direct Introduction quote, printed p. 69, not an abstract "
                "quote. Complete 14-page institutional scan and actual "
                "Figures 1-46 inspected at " + STRUCTURE_URL + ". "
                "Results describe five feeding cells named Protoperidinium "
                "spinulosum by the authors. Figures 9-12 show the pallium "
                "and degraded diatom contents outside the main cell body; "
                "Figures 1 and 46 are reconstructions. Discussion p. 81 "
                "leaves inner-membrane loss during fixation versus in vivo "
                "reorganization unresolved. Morphology does not demonstrate "
                "specific digestive proteins or a complete transport mechanism. "
                "No canonical taxon assignment is made from this culture."
            ),
        },
        {
            "reference": GROWTH,
            "snippet": (
                "Laboratory experiments were performed to determine the growth "
                "and grazing capabilities of Oblea rotunda, a pallium-feeding "
                "dinoflagellate."
            ),
            "notes": (
                "Direct scientific Abstract from the publisher page at "
                "https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.1993.38.5.0965. "
                "Supports the feeding-mode name and growth on several "
                "phytoplankton foods. Only the abstract was inspected; "
                "Methods, figures and culture provenance were not audited. "
                "The laboratory culture is not equated with the field "
                "specimens in the 1986 canonical example. Behavioral "
                "responses do not identify a molecular receptor."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:402581",
            "taxon_label": "Oblea rotunda",
            "reference": DEFINITION,
            "note": (
                "Qualified example: naturally collected specimens in the "
                "1986 study, Table 1 and Figure 2B, not all isolates. "
                "Methods p. 249 at " + PROVENANCE + " report net tows from "
                "Perch Pond or Vineyard Sound, Massachusetts, followed by "
                "short laboratory incubation and microscopy. No strain "
                "identifier or single collection site is assigned to this "
                "example. Figure 2B depicts pallium deployment around "
                "Pyramimonas sp. NCBI ESearch and EFetch verified the species "
                "name, rank and Peridiniopsis rotunda synonym on 2026-10-06."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pallium-feeding-topology-and-parent",
            "prompt": "Reconcile feeding-mode terminology and membrane topology.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This is an organismal feeding phenotype, not the pallium "
                "structure or a sequence feature. The 1986 Discussion p. 256 "
                "calls complete enclosure intracellular digestion in a "
                "vacuole outside the theca, but partial enclosure "
                "extracellular digestion, and questions that terminological "
                "division. Its engulfment wording need not mean whole "
                "particles enter the main cell body. Local phagocytosis "
                "traitmech:000627 requires enclosure and internalization; "
                "phagotrophy traitmech:000628 requires particulate ingestion "
                "and nutrient assimilation. Myzocytosis traitmech:000631 "
                "denotes prey-content aspiration through a localized "
                "connection, not an enveloping feeding veil. Retain "
                "phenotype METPO:1000059 pending a closer feeding hierarchy. "
                "Do not assert universal extracellular membrane topology "
                "or disjoint organismal feeding capabilities. Ordinary "
                "extracellular digestion or attachment alone is insufficient. "
                "No unverified synonym or ontology equivalence is asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "pallium-feeding-native-mechanism",
            "prompt": "Resolve membrane dynamics and native protein functions.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The 1992 Discussion proposes digestive-granule functions, "
                "membrane storage and transport routes from ultrastructure. "
                "It explicitly leaves fixation artifacts versus biological "
                "inner-membrane reorganization unresolved and requests "
                "time-course evidence. Apparatus similarity to peduncles "
                "does not prove identical feeding mechanics or protein "
                "function. Obtain taxon-paired functional and accession "
                "evidence before adding protein examples or a causal graph. "
                "No actin, centrin or enzyme accession is inferred from "
                "micrographs, and no gene or profile is treated as proof "
                "of this feeding phenotype."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added pallium feeding with three DOI-backed snippets and a "
            "natural-specimen-qualified Oblea example. Ignored-and-hidden "
            "searches and pinned METPO review found no exact record. "
            "Reserved METPO:1058500 in v508. Preserved partial-enclosure "
            "scope, source access limits and unresolved membrane topology; "
            "deferred unsupported protein mechanisms and sequence inference."
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
         "|".join(["TraitMech:data/traits/physiology/pallium_feeding.yaml",
                   DEFINITION, ULTRASTRUCTURE, GROWTH]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Enveloping pallium; outside main cell body, not universal extracellular topology.",
         IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if any(parent.get(k) != v for k, v in PARENT.items()):
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
