"""Add source-qualified cyanobacterial necridium formation."""

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
SLUG = "necridium_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v550/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000674"
METPO_ID = "METPO:1062700"
NECRIDIA = "DOI:10.1127/1864-1318/2005/0117-0239"
MASTIGOCLADUS = "DOI:10.1111/mmi.12506"
MICROCOLEUS = "DOI:10.3389/fmicb.2015.00278"
TIMESTAMP = "2026-10-08T05:29:42Z"
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
    "label": "necridium formation",
    "definition": (
        "A morphological phenotype in which a filamentous cyanobacterium forms "
        "degenerating separation cells called necridia whose disintegration "
        "permits trichome fragmentation."
    ),
    "definition_source": NECRIDIA,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": NECRIDIA,
            "snippet": (
                "Trichome breakage and hormogonia liberation were caused by "
                "the disintegration of such necridia"
            ),
            "notes": (
                "Hernandez-Marine and Roldan (2005), scientific abstract on "
                "article page 239, visually checked in the published article "
                "reproduced in Roldan's university thesis: "
                "https://diposit.ub.edu/server/api/core/bitstreams/"
                "6ce8a85f-d68f-402d-8c13-882f128e4a7f/content "
                "(PDF page 106). Article pages 239-247, including Methods, "
                "Results, Discussion and actual Figures 1-4, were inspected. "
                "Natural cave/catacomb biofilms contain Leptolyngbya and "
                "Scytonema; microscopy associates cell degeneration with "
                "fragmentation and terminal polysaccharide pads. The proposed "
                "adhesive function is not a demonstrated universal requirement. "
                "No exact strain exemplar is assigned from these mixed samples."
            ),
        },
        {
            "reference": MASTIGOCLADUS,
            "snippet": (
                "Necridia formation inhibits further molecular exchange, "
                "determining the fate of a branch likely to become a hormogonium."
            ),
            "notes": (
                "Nurnberg et al. (2014), scientific abstract directly retrieved "
                "from DOI-matched Europe PMC record PMID:24383541. Publisher "
                "full-text Results and Methods were read; actual Figures 5-6 "
                "were inspected in the accepted manuscript at "
                "https://idus.us.es/bitstreams/"
                "05b873c9-9775-45f4-a6d6-2b6c54f97978/download "
                "(PDF pages 41-42), with final publisher captions cross-checked. "
                "Figure 5 follows 5-CFDA fluorescence for 24 seconds across a "
                "necridium; this is not proof of permanent exclusion of every "
                "molecule. Figure 6 shows terminal cell remnants and sealed "
                "neighboring membranes. Supplements were not inspected."
            ),
        },
        {
            "reference": MICROCOLEUS,
            "snippet": "necridic (dead) cells are SYTOX Green-positive and CTC-negative",
            "notes": (
                "Publisher full-text Methods, Results, Figure 2 caption and "
                "actual panels A-I were inspected. The quoted caption identifies "
                "dead cells operationally by membrane permeability and lack of "
                "CTC reduction. Panels D-F concern Microcoleus vaginatus 858 "
                "CCALA after a week at 4 degrees C, before desiccation; Results "
                "report frequent necridia and trichome splitting in cold "
                "cultures. Injured double-positive cells and nitrogen-starved "
                "bleached but active cells are distinguished. Neither cold "
                "exposure nor this stain combination defines the entire class. "
                "Supplements and strain provenance were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:447715",
            "taxon_label": "Mastigocladus laminosus SAG 4.84",
            "reference": MASTIGOCLADUS,
            "note": (
                "Necridium-forming stage of the study strain, not a claim that "
                "every cell is a necridium. Methods report Castenholz D liquid "
                "culture at 40 degrees C under constant white light and fresh "
                "medium growth before communication assays. Natural origin "
                "from an Icelandic thermal spring in 1967 is independently "
                "confirmed by the culture collection at "
                "https://sagdb.uni-goettingen.de/detailedList.php?str_number=4.84. "
                "NCBI Taxonomy efetch for 447715 confirms this current name "
                "and rank strain. These authorities support identity/provenance, "
                "not additional phenotype experiments."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "necridium-formation-scope",
            "prompt": "Review a closer parent and separation-cell terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 below quality METPO:1000188. "
                "Hormogonium formation traitmech:000651 denotes production of "
                "short dispersal filaments, not the degenerating separation "
                "cell. The 2005 Introduction describes additional fragmentation "
                "routes, so neither trait is asserted a subclass or exact "
                "synonym of the other. Filament-shaped morphology concerns "
                "elongated cell shape, not this multicellular separation stage. "
                "Do not equate all dead cells, all trichome fragmentation or "
                "all hormogonium formation with necridia. No exact synonyms, "
                "xrefs, SSSOM equivalences or organism-level disjointness are "
                "asserted pending review of historical separation-disc usages."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "necridium-formation-mechanism",
            "prompt": "Resolve the formation mechanism without inferring protein causality.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cell degeneration, communication loss and fragmentation are "
                "observed, but the inspected evidence does not establish a "
                "protein-resolved necridium-formation mechanism. SepJ sequence "
                "similarity and septal localization in the 2014 paper do not "
                "establish its causal role in necridium formation. Programmed "
                "cell death is an interpretation, not proof of conserved "
                "apoptosis machinery. Do not impose a fixed cell shape, spacing, "
                "cold trigger, adhesion function or fitness benefit. A causal "
                "graph is deferred pending direct mechanism evidence and "
                "authority-verified protein examples; the mechanism is not "
                "claimed biologically absent."
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
            "Added necridium formation with three primary DOI references, three "
            "verbatim snippets and a source-qualified SAG 4.84 example. Ignored-"
            "and-hidden novelty and current-main/worktree/complete-open-PR "
            "reservation checks support 000674 and v550 block 1062700-1062799. "
            "Kept separation-cell morphology distinct from hormogonium formation, "
            "generic cell death and inferred protein mechanisms; existing "
            "records unchanged. Timestamp is observed UTC curation time."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Cyanobacterial separation-cell formation; no universal trigger or protein mechanism asserted.",
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
