"""Add reversible nematode-paralyzing activity through guarded writes."""

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
SLUG = "reversible_nematode_paralyzing_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v598/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000722"
METPO_ID = "METPO:1067500"
TIMESTAMP = "2026-10-14T01:02:02Z"
DEFINITION_SOURCE = "https://journals.flvc.org/nematropica/article/view/64427"
RECOVERY_SOURCE = "https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_5/pt5/nemato/27861.pdf"
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
    "label": "reversible nematode-paralyzing activity",
    "definition": (
        "A physiological capability of a microorganism to induce a loss of active "
        "nematode movement that reverses after exposure to the microorganism or "
        "its products ends."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "Bioassays revealed that filtrates of P. lilacinus and "
                "Paecilomyces marquandii caused reversible paralysis of male "
                "and juvenile R. similis."
            ),
            "notes": (
                "Kilama et al. 2007, English Abstract, printed page 215/PDF page 1. "
                "Direct publisher HTML/PDF and typeset match; native verifier "
                "skips URL references, not VERIFIED. Needle-probed immobilization "
                "at 2 h was followed by rinsing and reassessment labelled 21 h; "
                "Discussion says 21 h after rinsing. Bioassay 2 lacks recovery "
                "testing; bioassay 3 has a high-paralysis pH control and bioassay "
                "5 is null against controls. Actual Figure 1 measures initial "
                "paralysis; Results/Table 2 address recovery. Repeated counts "
                "are not individual trajectories. No universal host/stage "
                "response or dose threshold is inferred."
            ),
        },
        {
            "reference": RECOVERY_SOURCE,
            "snippet": (
                "Secondly, the majority of larvae are able to recover the "
                "mobility in fresh water following all treatment times up to 48 h."
            ),
            "notes": (
                "Cayrol, Djian and Pijarowski 1989, Results, Study of the "
                "reversibility of the toxic effect, printed page 335/PDF page 5; "
                "actual Figure 3 inspected. This recovery result concerns "
                "M. arenaria larvae exposed to Brazilian P. lilacinus culture "
                "filtrate: 10-day motionless, aerated, illuminated malt culture, "
                "15 g/L, undiluted filtrate, varied exposure, then 24 h in water. "
                "Needle probing and water/pH-matched medium controls are described. "
                "Summary says less than 48 h, Results through 48 h; no universal "
                "threshold is adopted. Typeset all is quoted; PDF text extraction "
                "misreads it as dl. Native URL verification is skipped. This is "
                "recovery support, not a standalone producer-identity excerpt "
                "or proof of a neural mechanism."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "reversible-nematode-paralysis-scope-and-hierarchy",
            "prompt": "Refine the hierarchy without losing the microbial actor and recovery requirement.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is the microorganism's capability, not its own nonmotility "
                "or the nematode's susceptibility. Recovery after removal is "
                "required; immobility, reduced speed, reduced egg hatch, population "
                "suppression, trapping or attraction alone is insufficient. "
                "The same producer or product may kill under other conditions; "
                "no organism-level disjointness follows. Phenotype METPO:1000059 "
                "is the conservative parent. Lethal activity, fungal nematophagy, "
                "trap formation and attraction are related, not necessary parents. "
                "No exact active or deprecated METPO counterpart was identified "
                "in the documented pinned/current screen; v598 proposes the class. "
                "Nematostatic terminology, chemical roles and sequence annotations "
                "are not exact synonyms or xrefs. Infection, feeding and a "
                "particular molecular mechanism are not required."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "reversible-nematode-paralysis-source-and-mechanism-limits",
            "prompt": "Resolve source discrepancies and strain provenance before adding taxa or mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kilama assigns 22R5-2 to both species in Methods, versus lilacinus "
                "22R5-1/marquandii 22R5-2 in Results/Figure 1 and marquandii "
                "22R5-1 in Discussion. It also varies 11N4-8/11N8-4 and "
                "23N5-2/23N-5. Upper dose is 375 in Methods/Results but 325 in "
                "Table 2; lower dose is 125 in Methods/Table 2 but 150 in "
                "Results, in microliters/mL. These discrepancies are not "
                "silently corrected. Cayrol's proposed neurotropic action is "
                "unresolved, not a demonstrated target. No common active "
                "chemical, protein, causal graph, canonical taxon, field efficacy "
                "or environmental safety is asserted. Taxonomic authority and "
                "strain provenance remain unchecked for exemplar purposes. "
                "Source hashes, bounded notice checks, URL-verifier skips and "
                "inspection limits are retained in the verification sidecar. "
                "No full raw-data or statistical reanalysis was performed."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added a microbial reversible nematode-paralyzing capability with "
            "two stable-URL primary studies and typeset-verified snippets. "
            "Retained recovery criteria, assay/control and source discrepancies; "
            "native URL references are skipped, not VERIFIED. Reserved 000722, "
            "v598 and 1067500-1067599 after ignored/hidden current-copy, retained "
            "history and open/draft PR checks with numeric false positives "
            "adjudicated. No exact active METPO counterpart identified in the "
            "inspected scope. Other records unchanged. Timestamp records "
            "observed acceptance after assessment, not the later file write."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml", record["definition_source"]]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Microbial paralyzing capability requiring recovery; not mere immobility or killing.",
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
