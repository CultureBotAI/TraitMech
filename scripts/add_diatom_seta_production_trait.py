"""Add source-bounded diatom seta production through the validated writer."""

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
SLUG = "diatom_seta_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/biomineralization.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v568/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000692"
METPO_ID = "METPO:1064500"
PARENT_ID = "traitmech:000690"
PARENT_METPO_ID = "METPO:1000059"
FORMATION = "DOI:10.1038/s41467-021-24944-6"
SHEATH = "DOI:10.1016/j.jsb.2025.108205"
TIMESTAMP = "2026-10-10T21:53:42Z"
PARENT = {
    "identifier": PARENT_ID,
    "label": "biomineralization",
    "definition": (
        "A physiological phenotype in which a microbe mediates the formation of mineral phases."
    ),
    "definition_source": "DOI:10.1016/j.crte.2010.09.002",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "diatom seta production",
    "definition": (
        "A biomineralization phenotype in which a diatom forms siliceous "
        "whisker-like cell-wall extensions called setae."
    ),
    "definition_source": FORMATION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": FORMATION,
            "snippet": (
                "A striking example for such long elements are whisker-like "
                "extensions, called setae, which characterize the genus Chaetoceros"
            ),
            "notes": (
                "Mayzel et al. 2021, PMID:34330922, PMC8324917, Introduction. "
                "Scientific Abstract, Introduction, Results, Discussion, Methods, "
                "main figure captions and Table 1 read in official Europe PMC "
                "full-text XML on 2026-10-10; actual Figures 2, 3 and 5 inspected. "
                "Other actual figures, supplements and movies remain unread. "
                "EXT_ID:34330922 AND SRC:MED confirmed the scientific abstract, "
                "ID, source, title and DOI. The quote identifies the structures; "
                "Results report seta formation in Chaetoceros tenuissimus under "
                "the source name. Figure 2 PDMPO labeling at growing tips supports "
                "new silica deposition, not only inherited appendage possession. "
                "Figure 3 resolves membrane, silica and an external organic layer; "
                "this supports a proposed extracellular route, not universal "
                "absence of a silica deposition vesicle. Figure 5 scores silicon "
                "limitation per cell, but germanium/PDMPO inhibition per valve; "
                "these denominators are not interchangeable. New valves still "
                "form under the germanium treatment, with altered texture, so "
                "valves are not claimed unaffected. No universal concentration "
                "threshold, growth rate or molecular necessity is inferred."
            ),
        },
        {
            "reference": SHEATH,
            "snippet": (
                "Here, we study a relatively large species, Chaetoceros rostratus, "
                "that forms long and intricate setae."
            ),
            "notes": (
                "Safadi et al. 2025, PMID:40294667, online 2025-04-26, June issue. "
                "Complete scientific Abstract directly read in source-qualified "
                "Europe PMC CORE on 2026-10-10 using EXT_ID:40294667 AND SRC:MED; "
                "one exact MED result with matching ID, title and DOI. The abstract "
                "reports in-cell cryo-electron tomography during seta formation "
                "in Chaetoceros rostratus under the source name and describes "
                "an organic sheath covering newly formed silica outside the "
                "plasma membrane. Structural macromolecules might regulate "
                "architecture; their necessity is not demonstrated by this "
                "abstract. Full Methods, actual figures and supplements were "
                "not inspected. This is a distinct primary study with overlapping "
                "authors, not independent-laboratory replication. No current "
                "taxon or strain provenance is assigned from the abstract alone."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "diatom-seta-production-scope-and-mappings",
            "prompt": "Keep seta formation distinct from possession and other silica endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Biomineralization traitmech:000690 is the broader phenotype: "
                "formation of these siliceous extensions entails mineral "
                "formation. A material seta, inherited appendage, silica uptake "
                "or adsorption is not this production phenotype. Valve/girdle "
                "formation (traitmech:000691), siliceous scales and auxospore "
                "coverings alone do not establish seta production, nor do setae "
                "alone establish those other endpoints. The existing frustule "
                "scope note already distinguishes setae; it is not an unresolved "
                "exact grounding. No organism-level disjointness, universal "
                "seta number, length, geometry, cell-cycle coupling, buoyancy "
                "or fitness effect is asserted. The extracellular route is not "
                "definitional. Exact synonyms and external phenotype mappings "
                "remain unasserted pending authority review; generic bristles, "
                "spines, silica processes and material structures are not "
                "automatically equivalent to this diatom phenotype."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "diatom-seta-production-exemplars-and-mechanisms",
            "prompt": "Resolve study-strain provenance and formation-specific causal evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned before checking collection "
                "provenance and current taxonomy. The two studies support seta "
                "formation, but structural localization alone does not establish "
                "a conserved protein mechanism. Microtubule pushing, a guiding "
                "organic scaffold and a diffusion-based silicon route remain "
                "hypotheses in Mayzel et al.; unobserved vesicle transport is "
                "not proof of its absence. Separate mineral deposition, shape "
                "control and organic-sheath assembly when evaluating functional "
                "perturbations. Protein edges require direct causal evidence "
                "and taxon-paired accessions; sequence features alone are "
                "insufficient. Mechanism is deferred, not claimed absent."
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
            "Added diatom seta production beneath biomineralization with two "
            "primary DOI citations and directly checked short snippets. "
            "Ignored-and-hidden main/worktree/open-PR reservation checks support "
            "000692 and v568 block 1064500-1064599. Existing trait records "
            "unchanged; mappings, canonical taxa and mechanisms remain open. "
            "Timestamp records the observed UTC curation decision."
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
         "Local parent biomineralization; request subclass of v566 METPO:1064300 on adoption.",
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
