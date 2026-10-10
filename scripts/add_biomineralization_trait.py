"""Add biomineralization and resolve two mineral-production parent gaps."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "biomineralization"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v566/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000690"
METPO_ID = "METPO:1064300"
TIMESTAMP = "2026-10-10T08:03:12Z"
TERMINOLOGY = "DOI:10.1016/j.crte.2010.09.002"
PRECIPITATION = "DOI:10.1128/AEM.07044-11"
COCCOLITH = "DOI:10.1038/ncomms11228"
SCALE = "DOI:10.1016/j.protis.2016.05.002"
PARENT = {
    "identifier": "METPO:1000059", "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER", "term_kind": "CLASS", "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
CHILDREN = {
    "coccolith_production": {
        "identifier": "traitmech:000689", "label": "coccolith production",
        "definition": (
            "A physiological phenotype in which a microbial cell produces the calcitic "
            "cell-covering elements known as coccoliths."
        ),
        "definition_source": COCCOLITH,
        "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    },
    "siliceous_scale_production": {
        "identifier": "traitmech:000688", "label": "siliceous scale production",
        "definition": (
            "A physiological phenotype in which a microbial cell produces siliceous scales."
        ),
        "definition_source": SCALE,
        "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    },
}
CHILD_PATHS = {slug: ROOT / f"data/traits/physiology/{slug}.yaml" for slug in CHILDREN}
RATIONALE_SHA256 = {
    "coccolith_production": "701bcbc1c3391ae7014cff5f6cddf0f73f3b32d2b23ea26141d151fb1c4d11e0",
    "siliceous_scale_production": "12e1bad3e0530ccc80a37540d9d86ae676e089d18de1a38fb276851f6f01dd35",
}
RESOLUTION = (
    "Added biomineralization traitmech:000690 as the direct broader phenotype. "
    "Production of the mineral elements specified by this record entails mineral "
    "formation; this is a definition-based hierarchy inference, not a new child "
    "experiment. Phenotype METPO:1000059 remains an ancestor. The historical "
    "rationale and endpoint distinctions are preserved; the separate exemplar "
    "and mechanism gap remains OPEN. The v566 proposal requests the additional "
    "child axiom without rewriting the historical proposal cohort."
)
CHILD_CHANGE = (
    "Refined the direct parent to biomineralization traitmech:000690 and resolved "
    "the temporary parent gap by definition-based inference. Preserved the "
    "definition, evidence, historical rationale, independent mechanism gap and "
    "prior curation history. No organism or molecular mechanism was added."
)
RECORD = {
    "identifier": IDENTIFIER,
    "label": "biomineralization",
    "definition": (
        "A physiological phenotype in which a microbe mediates the formation of mineral phases."
    ),
    "definition_source": TERMINOLOGY,
    "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "Microorganisms can mediate the formation of minerals by a process "
                "called biomineralization."
            ),
            "notes": (
                "Benzerara et al. 2011, scientific Abstract, directly checked in "
                "publisher HTML on 2026-10-10. Definition terminology, not an "
                "independent experimental replication: this is a review. Its "
                "Introduction and section 2 distinguish controlled, induced and "
                "biologically influenced formation, including organic-matrix effects. "
                "TraitMech represents the microbial phenotype rather than equating "
                "it with a process or material entity. The source cautions that "
                "association with pre-existing minerals does not establish formation. "
                "The remainder and actual figures were not audited for this record."
            ),
        },
        {
            "reference": PRECIPITATION,
            "snippet": (
                "All bacteria tested induce the precipitation of a significant amount "
                "of calcium carbonate when cultured in M-3P medium."
            ),
            "notes": (
                "Rodriguez-Navarro et al. 2012, PMID:22447589, PMC3346411, Discussion, "
                "Bacterial carbonatogenesis. Publisher scientific Abstract, Introduction, "
                "Methods, Results and relevant Discussion directly read on 2026-10-10; "
                "actual Figures 1 and 6 inspected, other figures not visually audited. "
                "Inoculated assays produced carbonates whereas uninoculated substrate "
                "controls did not. Tested M. xanthus strain 422, B. diminuta SJ 63 and "
                "a stone bacterial community are assay labels, not verified canonical "
                "taxa here. Polymorph selection depends on the stated substrate/medium "
                "conditions, not a universal strain rule. The proposed amorphous "
                "precursor is not established by morphology alone. No universal "
                "urease requirement or functional protein mechanism is inferred."
            ),
        },
        {
            "reference": COCCOLITH,
            "snippet": (
                "Coccoliths are calcitic particles produced inside the cells of "
                "unicellular marine algae known as coccolithophores."
            ),
            "notes": (
                "Sviben et al. 2016, PMID:27075521, PMC4834641. Scientific Abstract "
                "directly checked in Europe PMC full-text XML on 2026-10-10; "
                "Introduction, calcite-resupply Results and Discussion also inspected. "
                "This supports controlled mineral production and the coccolith "
                "child's placement. Historical E. huxleyi AWI1516 observations do not "
                "establish every strain's current phenotype. A separate calcium-rich "
                "compartment is not proven to be a necessary direct precursor or "
                "bulk-transfer route. No new figure or supplement audit is claimed "
                "for this parent; the child's more detailed provenance is retained."
            ),
        },
        {
            "reference": SCALE,
            "snippet": "Scales were formed one by one in silica deposition vesicles (SDVs)",
            "notes": (
                "Nomura and Ishida 2016, PMID:27348459. Scientific abstract directly "
                "read on 2026-10-10 at https://rrc.nbrp.jp/references/56432?lang=en. "
                "Scale formation and silicon detection in immature-scale vesicles "
                "support mineral production beyond carbonates and the siliceous-scale "
                "child's placement. Historical Paulinella chromatophora naming does "
                "not establish current strain taxonomy. Full Methods and figures "
                "remain unread; proposed microtubule involvement is not molecular "
                "necessity. Scale production is distinct from subsequent shell assembly."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "biomineralization-scope-and-mappings",
            "prompt": "Keep mineral formation distinct from association and process-level mappings.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The definition includes controlled, induced and matrix-mediated "
                "formation when microbial mediation is demonstrated; it is not "
                "restricted to carbonate, intracellular deposition or a crystalline "
                "end product. Benzerara et al. DOI:10.1016/j.crte.2010.09.002 "
                "section 2 includes passive organic-matter effects under biologically "
                "influenced biomineralization. This broad terminology is retained, "
                "but precipitation near a cell, isolated nonliving-matrix activity, "
                "mineral adhesion, uptake of preformed particles or ion adsorption "
                "alone does not establish that organism's formation phenotype. "
                "Organic-substrate mineralization, mineral dissolution, metal "
                "tolerance and mineral use as an electron donor are not equivalent. "
                "Coccolith and siliceous-scale production are narrower endpoints. "
                "Magnetosome and ferrosome organelle records retain their structural "
                "parents; no automatic cross-axis reparenting or disjointness is "
                "asserted. The magnetosome graph's similarly named node has narrower "
                "scope and is not exactly grounded to this umbrella. No synonyms "
                "or xrefs are asserted pending authority-backed phenotype mapping."
            ),
            "posed_by": "codex", "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "biomineralization-exemplars-and-mechanisms",
            "prompt": "Resolve assay-specific exemplars and distinct mineral-forming mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned before strain provenance and "
                "current taxonomy are reconciled with the original assays. A "
                "community precipitation assay cannot be assigned wholesale to "
                "each community member. Substrate, medium, mineral phase, location "
                "and life stage qualify observations. No universal benefit, growth "
                "dependence, genetic control, obligatory enzyme or shared protein "
                "pathway follows from this umbrella. Separate controlled deposition "
                "from metabolically induced precipitation and organic-matrix effects "
                "when adding mechanisms. Functional evidence and taxon-paired "
                "accessions are required for protein edges; sequence features or "
                "mineral co-localization alone are insufficient. Mechanism is "
                "deferred, not claimed absent."
            ),
            "posed_by": "codex", "posed_date": "2026-10-10",
        },
    ],
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(record, curator="codex", action=action, changes=changes,
                         llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(record, "MINTED_TRAITMECH_ID", (
        "Added biomineralization with source-backed terminology, three primary "
        "studies and directly checked short snippets. Reserved 000690 and v566 "
        "block 1064300-1064399 after ignored-and-hidden main/worktree/open-PR "
        "checks. Resolved the coccolith and siliceous-scale production parent "
        "gaps without claiming common mechanisms or canonical taxa. Timestamp "
        "records the observed UTC curation decision."
    ))
    return record


def build_child(slug: str, record: dict) -> dict:
    record = copy.deepcopy(record)
    if not isinstance(record, dict) or any(record.get(k) != v for k, v in CHILDREN[slug].items()):
        raise SystemExit(f"{slug} identity or scope differs from reviewed preimage")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == slug.replace("_", "-") + "-scope-and-parent"]
    if len(matches) != 1:
        raise SystemExit(f"{slug} discussion identity differs")
    discussion = matches[0]
    if (discussion.get("kind") != "CURATION_TODO"
            or hashlib.sha256(discussion.get("rationale", "").encode()).hexdigest()
            != RATIONALE_SHA256[slug]):
        raise SystemExit(f"{slug} discussion scope differs")
    expected = {}
    event(expected, "REFINE_BIOMINERALIZATION_PARENT", CHILD_CHANGE)
    expected_event = expected["curation_history"][0]
    history = record.get("curation_history", [])
    if record.get("parent_traits") == [IDENTIFIER]:
        if (discussion.get("status") != "RESOLVED"
                or discussion.get("resolved_date") != "2026-10-10"
                or discussion.get("resolution_note") != RESOLUTION
                or not history or history[-1] != expected_event):
            raise SystemExit(f"{slug} replay differs from reviewed result")
        return record
    if (record.get("parent_traits") != [PARENT["identifier"]]
            or discussion.get("status") != "OPEN"
            or "resolved_date" in discussion or "resolution_note" in discussion
            or expected_event in history):
        raise SystemExit(f"{slug} hierarchy or discussion state differs")
    record["parent_traits"] = [IDENTIFIER]
    discussion.update(status="RESOLVED", resolved_date="2026-10-10", resolution_note=RESOLUTION)
    event(record, "REFINE_BIOMINERALIZATION_PARENT", CHILD_CHANGE)
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
         "Microbial formation phenotype; add v564/v565 child axioms documented in proposal.md.",
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
    children = {slug: build_child(slug, yaml.safe_load(path.read_text()))
                for slug, path in CHILD_PATHS.items()}
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    # Validate the complete coupled change before writing any production file.
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        for slug, child in children.items():
            write_validated_trait(child, Path(tmp) / CHILD_PATHS[slug].name)
    if args.apply:
        write_validated_trait(record, TARGET)
        for slug, child in children.items():
            write_validated_trait(child, CHILD_PATHS[slug])
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
