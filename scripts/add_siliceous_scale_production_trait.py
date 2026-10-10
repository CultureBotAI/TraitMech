"""Add source-bounded siliceous scale production through the validated writer."""

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
SLUG = "siliceous_scale_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v564/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000688"
METPO_ID = "METPO:1064100"
PARENT_METPO_ID = "METPO:1000059"
ULTRASTRUCTURE = "DOI:10.1016/j.protis.2016.05.002"
RECOVERY = "DOI:10.1111/j.0022-3646.1996.00675.x"
TIMESTAMP = "2026-10-10T05:02:23Z"
PARENT = {
    "identifier": PARENT_METPO_ID,
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
    "label": "siliceous scale production",
    "definition": (
        "A physiological phenotype in which a microbial cell produces siliceous scales."
    ),
    "definition_source": ULTRASTRUCTURE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
    "evidence": [
        {
            "reference": ULTRASTRUCTURE,
            "snippet": "Scales were formed one by one in silica deposition vesicles (SDVs)",
            "notes": (
                "Nomura and Ishida 2016, PMID:27348459. Scientific abstract directly "
                "read on 2026-10-10 at https://rrc.nbrp.jp/references/56432?lang=en "
                "and Europe PMC CORE, using EXT_ID:27348459 AND SRC:MED and checking "
                "the returned source, title and DOI together. The study describes "
                "scale formation in Paulinella chromatophora under its historical "
                "name and detects silicon in vesicles with immature scales. "
                "Microtubule involvement in determining scale geometry is proposed, "
                "not demonstrated molecular necessity. Publisher access returned "
                "403; full Methods and figures were not inspected. Scale production "
                "and subsequent shell assembly are distinct observations."
            ),
        },
        {
            "reference": RECOVERY,
            "snippet": "The first new scales appeared within 2 h after the silica addition",
            "notes": (
                "Sandgren, Hall and Barlow 1996, scientific ABSTRACT directly read "
                "on 2026-10-10 in publisher-deposited Crossref JATS at "
                "https://api.crossref.org/works/10.1111%2Fj.0022-3646.1996.00675.x. "
                "Silica-limited Synura petersenii cultures suppressed scale "
                "deposition, and scale-free cells regenerated scales after dissolved "
                "silica addition. This supports production rather than possession "
                "alone. The quoted recovery timing is specific to that culture "
                "experiment, not a universal threshold or rate. Scale production "
                "could be uncoupled from cell division in this system; no obligatory "
                "growth dependence is inferred. Crossref print date is August 1996; "
                "its June 2008 online date is not a second study. Full Methods and "
                "figures were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "siliceous-scale-production-scope-and-parent",
            "prompt": "Resolve broader biomineralization placement without conflating endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059 pending a source-backed broader "
                "biomineralization phenotype. This is production of scales, not "
                "mere possession, acquisition or reuse of preformed scales, their "
                "extrusion, or their arrangement into a shell or scale layer. "
                "It is not equivalent to general silicification, diatom frustule "
                "formation, magnetosome or ferrosome possession, substrate "
                "adhesion, or growth on a particular chemical. These neighboring "
                "endpoints do not alone demonstrate new-scale production. Do not "
                "infer a universal scale geometry, covering architecture, cell-cycle "
                "coupling or fitness effect. No exact synonyms, xrefs, homology "
                "or organism-level disjointness are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "siliceous-scale-production-exemplars-and-mechanism",
            "prompt": "Verify assay-strain identity and production-specific molecular evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned until primary assay Methods, "
                "strain provenance and current taxonomy are jointly reconciled. "
                "NIES-4060 is currently catalogued as Paulinella micropora (MYN1) "
                "at https://mcc.next.nbrp.jp/strainList.do?strainNumber=NIES-4060; "
                "its reference list links the 2016 historical chromatophora paper, "
                "but this collection association is not an independent production "
                "experiment or authority to rename every historical observation. "
                "The two primary abstracts support a reusable phenotype through "
                "different methods, not one conserved molecular pathway. "
                "Ultrastructure and cytoskeletal association alone cannot establish "
                "causal protein requirements. Separate deposition, vesicle "
                "transport, extrusion and assembly before adding causal edges. "
                "A protein mechanism needs functional evidence and taxon-paired "
                "accessions; sequence features alone cannot supply that support. "
                "Mechanism is deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added siliceous scale production with two primary DOI citations, "
            "directly checked scientific-abstract snippets and explicit access "
            "limits. Ignored-and-hidden main/worktree/open-PR reservation checks "
            "support 000688 and v564 block 1064100-1064199. Broader hierarchy, "
            "canonical exemplars and protein mechanism remain unresolved. "
            "Existing records unchanged. Timestamp records the observed UTC "
            "curation decision."
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
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "New-scale production, not scale possession or shell assembly.", IDENTIFIER],
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
