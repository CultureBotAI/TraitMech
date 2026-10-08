"""Add evidence-backed mucocyst discharge below the proposed exocytosis class."""

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
SLUG = "mucocyst_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/exocytosis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v560/metpo_proposal_classes_robot.tsv"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v513/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000684"
METPO_ID = "METPO:1063700"
PARENT_METPO_ID = "METPO:1059000"
MDL1 = "DOI:10.1371/journal.pgen.1010194"
DIBUCAINE = "DOI:10.1016/0309-1651(77)90012-1"
CTH4 = "DOI:10.1128/ec.00058-15"
TIMESTAMP = "2026-10-08T17:15:26Z"
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
    "label": "mucocyst discharge",
    "definition": (
        "An exocytotic phenotype in which a microbial cell releases mucocyst "
        "contents to the exterior through fusion of a mucocyst membrane with "
        "the plasma membrane."
    ),
    "definition_source": MDL1,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MDL1,
            "snippet": (
                "lysosome-related organelles called mucocysts accumulate at the "
                "cell periphery where they secrete their contents in response "
                "to extracellular events"
            ),
            "notes": (
                "PMID:35587496, PMC9159632. Scientific Abstract, relevant "
                "Results/Methods and Discussion read directly in Europe PMC "
                "fullTextXML and publisher HTML. Figure 1 and its caption were "
                "visually inspected; Figure 4 caption, not image, was read. "
                "The snippet is from the scientific Abstract, not the Author "
                "summary. Dibucaine stimulates release in Tetrahymena thermophila. "
                "Sedimented flocculent volume is a secretion proxy, not a count "
                "of discharged organelles; cells can be trapped in that layer. "
                "The MN175 missense and MDL1 deletion phenotypes differ. "
                "S1 Table DOCX text was inspected, not rendered; laboratory "
                "strain names and genotypes do not establish natural provenance."
            ),
        },
        {
            "reference": DIBUCAINE,
            "snippet": "Synchronous secretion of all available mature mucocysts was induced",
            "notes": (
                "PMID:610868. Scientific Abstract directly retrieved with "
                "EXT_ID:610868 AND SRC:MED in Europe PMC; an unqualified numeric "
                "query also returns an unrelated database record. The correct "
                "MED result matches this DOI and title. Abstract-only access; "
                "full Methods and figures were not inspected. The source names "
                "Tetrahymena thermophilia (B III). Synchrony and complete release "
                "concern late-log cultures treated with dibucaine, not universal "
                "requirements for this trait. Fusion-rosette reappearance and "
                "new mucocyst precursors are temporally associated, not proof "
                "of a universal protein mechanism."
            ),
        },
        {
            "reference": CTH4,
            "snippet": (
                "those cores do not undergo normal directional expansion during "
                "exocytosis, and they thus fail to efficiently extrude from the cells."
            ),
            "notes": (
                "PMID:26092918, PMC4519746. Scientific Abstract directly retrieved "
                "by exact quoted DOI query in Europe PMC. Abstract-only access; "
                "full Methods, figures and supplements were not inspected. "
                "The snippet refers to CTH4-disrupted Tetrahymena thermophila: "
                "crystalline cores assemble but extrusion is inefficient. "
                "It is boundary evidence distinguishing assembly from successful "
                "release, not a positive mutant exemplar or proof that no cargo "
                "is released. CTH4 dependence is not imposed on all mucocysts."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "mucocyst-discharge-scope-and-homology",
            "prompt": "Keep cargo release distinct from organelle presence and homologous types.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Exocytosis traitmech:000637 is the broader parent; the proposal "
                "depends on its v513 placeholder METPO:1059000. Mucocyst "
                "formation, docking and fusion without cargo release do not "
                "alone establish discharge. Lysis and preparation artifacts "
                "must be excluded from positive assays. Neither rapid expansion "
                "nor total emptying defines this class. The 2022 Discussion "
                "calls Paramecium trichocysts mucocyst homologs. This record "
                "preserves the organelle-specific release phenotype rather than "
                "asserting independent origins, exact equivalence to trichocyst "
                "discharge traitmech:000683, or organism-level disjointness. "
                "Resolve historical extrusome terminology before broadening "
                "the definition; not all mucus secretion, cortical granules "
                "or capsule formation are equivalent. No exact synonyms or "
                "xrefs are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "mucocyst-discharge-provenance-and-mechanism",
            "prompt": "Resolve natural culture provenance and taxon-specific release mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "These experiments support a secretion phenotype in source-named "
                "Tetrahymena systems, not every protist bearing an extrusome. "
                "Natural culture provenance and strain-level taxonomy remain "
                "unchecked, so no canonical examples are assigned. A wildtype "
                "designation alone does not establish natural provenance; a "
                "mutant designation alone does not establish engineering. "
                "The MDL1 and CTH4 experiments motivate a future protein-resolved "
                "graph, but require taxon-paired accessions and separation of "
                "maturation, docking, fusion and cargo extrusion. Mechanism is "
                "deferred, not claimed absent; sequence features alone do not "
                "establish discharge. Do not infer a universal ecological role "
                "from induced secretion."
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
            "Added mucocyst discharge with three primary DOI sources and "
            "directly checked scientific-abstract snippets. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000684 and v560 block "
            "1063700-1063799. Used existing exocytosis parent and its v513 "
            "proposal dependency. Qualified assay proxies, organelle homology, "
            "mutant evidence and provenance; deferred protein mechanism. "
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
