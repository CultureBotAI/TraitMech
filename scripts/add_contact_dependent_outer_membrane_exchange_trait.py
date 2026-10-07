"""Add contact-dependent outer-membrane exchange with source-bounded evidence."""

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
SLUG = "contact_dependent_outer_membrane_exchange"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v526/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000650"
METPO_ID = "METPO:1060300"
IMAGING = "DOI:10.7554/eLife.00868"
GENETICS = "DOI:10.1371/journal.pgen.1002626"
TUBES = "DOI:10.1128/jb.00850-13"
POPULATION = "DOI:10.1371/journal.pone.0224817"
TIMESTAMP = "2026-10-06T20:54:50Z"
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
    "label": "contact-dependent outer membrane exchange",
    "definition": (
        "A physiological phenotype in which microbial cells exchange "
        "outer-membrane lipids and proteins with other cells through direct "
        "intercellular contact."
    ),
    "definition_source": IMAGING,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": IMAGING,
            "snippet": (
                "transient contacts between two cells are sufficient to transfer "
                "OM materials, proteins and lipids, at high efficiency."
            ),
            "notes": (
                "PMID:23898400, PMC3721248. Scientific Abstract span directly "
                "read in Europe PMC XML, not the eLife digest. Selected Results "
                "s2-1 to s2-4 and Methods s4-1 to s4-4 were read; actual Figures "
                "2 and 4 were visually inspected with their captions. Engineered "
                "Myxococcus xanthus DZ2 reporters and DiO assays distinguish OM "
                "material transfer from inner-membrane reporter exchange. "
                "Contact and traA controls support the observed endpoint. "
                "Dye continuity through some tubes does not establish significant "
                "protein transfer through them, which was not detected. "
                "Membrane fusion is the authors' mechanistic interpretation; "
                "not every contact transfers material. Videos and remaining "
                "supplementary panels were not inspected."
            ),
        },
        {
            "reference": GENETICS,
            "snippet": (
                "By use of a lipophilic fluorescent dye, we also discovered "
                "that OM lipids are exchanged."
            ),
            "notes": (
                "PMID:22511878, PMC3325183. Scientific Abstract directly read "
                "in Europe PMC XML; Results s2c/s2d and Methods s4a/s4e/s4f "
                "also read. Reporter and DiD experiments in M. xanthus support "
                "TraA/TraB dependence in donors and recipients under the tested "
                "surface-growth conditions. Liquid and nonmotile-pair controls "
                "limit inference from dye labeling alone. Similar domain "
                "architecture in mxan_4924 did not yield an overt transfer defect "
                "when disrupted; sequence resemblance is not sufficient "
                "phenotype evidence. Proposed adhesion, fusion and social roles "
                "are not all directly established by this study. Actual panels "
                "and strain-table provenance remain uninspected."
            ),
        },
        {
            "reference": TUBES,
            "snippet": (
                "Thus, genetic and environmental conditions that promote OMT "
                "production are incongruent with OM exchange."
            ),
            "notes": (
                "PMID:24391054, PMC4011004. Scientific abstract directly "
                "retrieved through the Europe PMC core API. Full-text XML "
                "retrieval failed, so no full-text or panel verification is "
                "claimed. The abstract reports abundant OM tubes in traA/traB "
                "mutants and liquid conditions that do not permit transfer. "
                "Tube abundance alone is therefore insufficient for this trait; "
                "this does not negate the specific dye-conducting connections "
                "imaged in 2013. This paper shares investigators with the 2012 "
                "study and is not independent-laboratory replication."
            ),
        },
        {
            "reference": POPULATION,
            "snippet": (
                "Collectively, our results suggest that most mechanisms of "
                "interference competition and inter-colony kin discrimination "
                "in natural populations of myxobacteria do not require OME."
            ),
            "notes": (
                "PMID:31774841, PMC6880969. Scientific Abstract and Results "
                "sec012/sec014 directly read in Europe PMC XML. In the tested "
                "natural-isolate pairs, traA disruption or the A60 deletion "
                "did not remove colony-merger incompatibility. This is a "
                "boundary on ecological-function claims, not evidence that "
                "membrane exchange never occurs. The GJV1 control uses swarm "
                "inhibition as an inferred OME-dependent toxin readout, not "
                "direct fluorescent membrane transfer in every isolate. "
                "The directly read correction DOI:10.1371/journal.pone.0228697 "
                "(PMID:31999808, PMC6991971) concerns Table 3 typesetting; "
                "no Table 3 numerical claim is used here. Actual panels "
                "were not visually inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "outer-membrane-exchange-scope-and-mapping",
            "prompt": "Keep membrane-component exchange distinct from its possible consequences.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The endpoint is contact-dependent exchange of outer-membrane "
                "material between cells. It is not cytoplasmic fusion, "
                "conjugative DNA transfer, all contact-dependent toxin delivery, "
                "or a generic secretion phenotype. Exocytosis traitmech:000637 "
                "concerns intracellular-compartment fusion-pore discharge; "
                "extracellular membrane vesicle production traitmech:000649 "
                "concerns extracellular particles. Neither is an exact parent. "
                "Cell-free vesicle transfer and slime-trail deposition do not "
                "alone demonstrate this contact-qualified class. The traits "
                "may coexist; no organism-level disjointness is asserted. "
                "Do not require equal bidirectional flux, transfer of every "
                "cargo at every contact, cooperation, killing, kin discrimination "
                "or fruiting-body development. Retain phenotype METPO:1000059 "
                "pending human hierarchy and external-mapping review; no "
                "unqualified exact synonym or external equivalence is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "outer-membrane-exchange-strain-and-mechanism-grounding",
            "prompt": "Ground strain-specific transfer machinery beyond sequence predictions.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "TraA/TraB dependence and live material transfer are supported, "
                "but no accession-resolved universal fusogen pathway is asserted. "
                "Before adding causal graphs, resolve protein accessions, "
                "inspect remaining supplements and distinguish measured transfer, "
                "binding and fusion-model steps. PA14/MYXO-CTERM/OmpA-like "
                "sequence features or a traAB annotation alone do not establish "
                "the phenotype. Reporter-bearing and deletion strains remain "
                "qualified evidence, not unqualified natural exemplars. Natural "
                "provenance and direct positive transfer evidence must be paired "
                "before adding canonical examples; the 2019 negative "
                "kin-discrimination result cannot supply that positive anchor. "
                "These are outstanding grounding tasks, not a claim that "
                "no mechanism is known."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added contact-dependent outer membrane exchange with four "
            "DOI-backed snippets and explicit transfer, tube, ecological-function "
            "and sequence-inference boundaries. Ignored-and-hidden duplicate "
            "searches and the pinned METPO audit found no exact record. "
            "Reserved METPO:1060300 in v526. Deferred unresolved strain/protein "
            "grounding; existing records are unchanged."
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
         "Contact-qualified membrane transfer; no universal social function or sequence inference.",
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
