"""Add evidence-backed trichocyst discharge below the proposed exocytosis class."""

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
SLUG = "trichocyst_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/exocytosis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v559/metpo_proposal_classes_robot.tsv"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v513/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000683"
METPO_ID = "METPO:1063600"
PARENT_METPO_ID = "METPO:1059000"
CALCIUM = "DOI:10.1083/jcb.111.6.2527"
RELEASE = "DOI:10.1016/s0143-4160(98)90030-6"
SLOW = "DOI:10.1016/0143-4160(93)90065-e"
TIMESTAMP = "2026-10-08T16:03:03Z"
PARENT = {
    "identifier": "traitmech:000637",
    "label": "exocytosis",
    "definition": (
        "A physiological phenotype in which a microbial cell releases material "
        "from an intracellular membrane-bounded compartment to the cell exterior "
        "through a fusion pore between the compartment membrane and the plasma membrane."
    ),
    "definition_source": "DOI:10.1083/jcb.56.1.153",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "trichocyst discharge",
    "definition": (
        "An exocytotic phenotype in which a microbial cell releases trichocyst "
        "contents to the exterior through fusion of a trichocyst membrane with "
        "the plasma membrane."
    ),
    "definition_source": CALCIUM,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": CALCIUM,
            "snippet": (
                "A Paramecium possesses secretory organelles called trichocysts "
                "which are docked beneath the plasma membrane awaiting an external "
                "stimulus that triggers their exocytosis."
            ),
            "notes": (
                "PMID:1703537, PMC2116420. Scientific Abstract and relevant "
                "Methods/Results OCR read directly in Europe PMC fullTextXML. "
                "The snippet is from the scientific Abstract; figures were not "
                "inspected. AED-triggered release was studied in Paramecium "
                "tetraurelia stock d4-2, a stock 51 derivative, and mutants. "
                "Calcium influx and concentration requirements concern this "
                "assay, not a universal discharge threshold or proven channel "
                "identity. The Methods distinguish low-calcium membrane injury "
                "from secretion; calcium influx alone does not demonstrate release."
            ),
        },
        {
            "reference": RELEASE,
            "snippet": "but only wt cells release trichocysts (t).",
            "notes": (
                "PMID:9681197. Primary PDF at https://d-nb.info/1107191386/34, "
                "Figures 1-4 caption, printed page 351. Pages 351-352 were "
                "visually inspected, including paired fluorescence/transmitted-light "
                "panels and Table 1. Wildtype Paramecium caudatum releases "
                "trichocysts after local AED or caffeine stimulation; tnd1 shows "
                "calcium transients and membrane fusion without contents release. "
                "Most trichocysts remain in wildtype cells during the illustrated "
                "local response, so total emptying is not required. Mutant tnd1 "
                "is boundary evidence, not a positive discharge exemplar. "
                "Reduced calcium binding is a proposed explanation, not a "
                "proven protein lesion. Natural strain provenance is unresolved."
            ),
        },
        {
            "reference": SLOW,
            "snippet": "trichocyst contents were slowly extruded",
            "notes": (
                "PMID:7684653. Scientific Abstract retrieved directly using an "
                "exact quoted DOI query in Europe PMC. Abstract-only access; "
                "full Methods and figures were not inspected. Slow extrusion "
                "under AED and low-calcium conditions shows why rapid expansion "
                "is not mandatory in this definition. The abstract distinguishes "
                "fusion, contents release and resealing; prolonged calcium "
                "removal is followed by cell death. Do not infer calcium "
                "irrelevance to all stages or treat terminal damage as secretion."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "trichocyst-discharge-scope-and-assays",
            "prompt": "Keep cargo release distinct from organelle presence and component steps.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Exocytosis traitmech:000637 is the broader parent; the proposal "
                "depends on its v513 placeholder METPO:1059000. Trichocyst "
                "formation, docking, fusion without cargo release and isolated "
                "matrix expansion do not alone establish completed discharge. "
                "Lysis and preparation artifacts must be excluded from positive "
                "assays. Neither rapid extrusion, total emptying nor a shared "
                "calcium threshold defines this class. The existing myzocytosis "
                "record's warning about fixation-associated discharge and "
                "uncertain prey capture is not resolved by these secretion "
                "experiments. No exact synonyms, xrefs, SSSOM equivalents or "
                "universal prey-capture role are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "trichocyst-discharge-provenance-and-mechanism",
            "prompt": "Resolve natural culture provenance and taxon-specific release mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "These experiments support a secretion phenotype in source-named "
                "Paramecium systems, not every protist bearing an extrusome. "
                "Natural culture provenance and strain-level taxonomy remain "
                "unchecked, so no canonical examples are assigned. A wildtype "
                "designation alone does not establish natural provenance; a "
                "mutant designation alone does not establish engineering. "
                "Keep assay-specific calcium observations separate and obtain "
                "direct functional evidence with taxon-paired accessions before "
                "adding a protein-resolved graph. Mechanism is deferred, not "
                "claimed absent; sequence features alone do not establish discharge."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added trichocyst discharge with three primary DOI sources and "
            "directly checked abstract/caption snippets. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000683 and v559 block "
            "1063600-1063699. Used existing exocytosis parent and its v513 "
            "proposal dependency. Kept calcium conditions, fusion-only mutants, "
            "slow extrusion and provenance qualified; deferred protein mechanism. "
            "Existing records unchanged. Timestamp is observed UTC."
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
         "Depends on v513 exocytosis; contents release, not fusion alone.", IDENTIFIER],
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
    with PARENT_PROPOSAL.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    matches = [r for r in rows if r.get("proposed_id") == PARENT_METPO_ID]
    expected = {
        "label": PARENT["label"], "definition": PARENT["definition"],
        "parent": PARENT["parent_traits"][0], "traits_addressed": PARENT["identifier"],
    }
    if len(matches) != 1 or any(matches[0].get(k) != v for k, v in expected.items()):
        raise SystemExit("Parent proposal differs from reviewed identity or hierarchy")
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
