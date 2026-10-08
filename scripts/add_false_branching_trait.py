"""Add source-qualified cyanobacterial false branching."""

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
SLUG = "false_branching"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v551/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000675"
METPO_ID = "METPO:1062800"
DEVELOPMENT = "DOI:10.1127/algol_stud/83/1996/303"
SCYTONEMA = "DOI:10.5507/fot.2021.017"
RHIZONEMA = "DOI:10.1111/jpy.13256"
TIMESTAMP = "2026-10-08T06:28:38Z"
CORRECTION_TIMESTAMP = "2026-10-08T06:50:15Z"
BOUNDARY_NOTE = (
    " The label is qualified as cyanobacterial false branching because the "
    "directly read English scientific abstract of Nesterenko et al. (1980), "
    "PMID:6782438 (https://pubmed.ncbi.nlm.nih.gov/6782438/), uses false "
    "branching for growth of separated cell ends in the organism historically "
    "named Brevibacterium helvolum ATCC 19239. That distinct usage is not "
    "evidence for cyanobacterial trichome development. Its full text and "
    "modern taxonomic identity were not inspected. No unqualified exact "
    "synonym or cross-taxon mechanism is asserted. See review issue #1821."
)
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
    "label": "false branching",
    "definition": (
        "A morphological phenotype in which a filamentous cyanobacterium forms "
        "an apparent branch by trichome-bundle partitioning or lateral trichome "
        "protrusion without generating a branch-point cell connecting at least "
        "three neighboring cells at that junction."
    ),
    "definition_source": DEVELOPMENT,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "Two basic types of false branching (by bundle partitioning and "
                "by lateral trichome protrusion)"
            ),
            "notes": (
                "Golubic et al. (1996), scientific abstract directly read on the "
                "publisher page https://www.schweizerbart.de/papers/algol_stud/"
                "detail/83/91090/Developmental_aspects_of_branching_in_filamentous_. "
                "Crossref confirms DOI, title and authors. The developmental "
                "analysis distinguishes false from true branching by branch-point "
                "cells contacting at least three neighbors. This terminology "
                "authority supports both listed modes, not only sheath rupture "
                "following necridium formation. Full article and figures were "
                "not inspected; no new experimental replication or universal "
                "molecular mechanism is inferred from the abstract."
            ),
        },
        {
            "reference": SCYTONEMA,
            "snippet": (
                "initiation of branching after disintegrating of sheath at the "
                "site of a necridia cell"
            ),
            "notes": (
                "Tawong et al. (2022), Figure 1k caption, article page 82 in "
                "https://fottea.czechphycology.cz/pdfs/fot/2022/01/05.pdf "
                "(PDF page 5); actual Figure 1 panels and Methods/Results read. "
                "Source grammar is retained. Results page 81 points to Figs 2e-k "
                "for false branching, but the microscopy is Figure 1e-k; Figure "
                "2 is phylogeny. NUACC05/06 show single and binary false branches "
                "associated with separation, heterocytes and loop rupture. "
                "The captioned necridium route is not required for every branch "
                "or for bundle partitioning."
            ),
        },
        {
            "reference": RHIZONEMA,
            "snippet": (
                "False branches developed adjacent to necridic cells or "
                "heterocytes, or by separation of vegetative cells at compression "
                "folds in the trichome."
            ),
            "notes": (
                "Masumoto and Sanders (2022), scientific abstract directly read "
                "at https://onlinelibrary.wiley.com/doi/abs/10.1111/jpy.13256. "
                "Microscopy of lichen cyanobionts reports multiple branching "
                "modes within a strain, so false and true branching are not "
                "disjoint organism-level traits. Secondary attachment of freed "
                "apical segments is separately described as pseudo-branching; "
                "that term is not imported as an exact synonym. Full text, "
                "figures and supplements were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2929979",
            "taxon_label": "Scytonema foetidum",
            "reference": SCYTONEMA,
            "note": (
                "Example restricted to false-branched filaments of natural "
                "isolate NUACC06, not every cell or stage. Methods describe "
                "single-filament isolation from wet Khek River bank soil, "
                "Thailand, April 2019, followed by CT/2 liquid culture at "
                "25 degrees C with a 12:12 light-dark cycle. Live NCBI Taxonomy "
                "efetch https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=2929979 confirms this current species name, "
                "rank species and NUACC06 type material; it is not a strain-rank "
                "accession. Taxonomy supports identity, not independent "
                "phenotype evidence."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "false-branching-scope",
            "prompt": "Review a closer multicellular morphology parent and branching terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059 below quality METPO:1000188. "
                "Branched shaped METPO:1000687 concerns lateral branches in "
                "cell shape, not necessarily this arrangement of trichomes; "
                "no subclass or equivalence is asserted. The Golubic 1996 "
                "definition authority includes bundle partitioning as well as "
                "lateral protrusion. The Scytonema example demonstrates the "
                "latter and must not narrow the whole class. Necridium "
                "formation traitmech:000674 describes a separation cell, not "
                "all false branches. Hormogonium formation traitmech:000651 "
                "describes dispersal filaments, not the branching topology. "
                "Obsolete cell-arrangement METPO terms redirect to flagellar "
                "arrangement, which is not a suitable parent here. No exact "
                "synonyms, xrefs, SSSOM mappings or organism-level disjointness "
                "are asserted; historical pseudo-branch usages need review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "false-branching-mechanism",
            "prompt": "Resolve mechanisms separately for each developmental mode.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The inspected microscopy supports a phenotype and cellular "
                "developmental routes, not an accession-resolved protein "
                "mechanism. Taxonomic sequence markers do not establish "
                "causality. Do not require necridia, heterocytes, a fixed "
                "branch count, one division plane, a universal trigger or a "
                "fitness benefit. No causal graph is proposed pending direct "
                "mechanistic evidence and verified protein examples; a "
                "mechanism is not claimed biologically absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cyanobacterial false branching with three DOI sources, "
            "verbatim snippets and a source-qualified NUACC06 example. "
            "Ignored-and-hidden searches of current main, worktrees and "
            "complete open-PR curation snapshots support 000675 and v551 block "
            "1062800-1062899. Preserved both developmental modes, local "
            "branch-point scope and uncertainty about protein mechanisms. "
            "Existing traits unchanged. Timestamp is observed UTC curation time."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    record["label"] = "cyanobacterial false branching"
    record["discussions"][0]["rationale"] += BOUNDARY_NOTE
    record_curation_event(
        record, curator="codex", action="QUALIFY_TRAIT_LABEL",
        changes=(
            "Addressed #1821: qualified the label to its cyanobacterial scope "
            "after directly checking the non-cyanobacterial usage in "
            "PMID:6782438. Preserved definition, evidence, example, identifier, "
            "proposal block and original curation event. Added source-qualified "
            "terminology discussion without an unqualified exact synonym."
        ),
        llm_assisted=True, timestamp=CORRECTION_TIMESTAMP,
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
         "Includes bundle partitioning and lateral protrusion; no universal necridium or protein requirement.",
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
    initial = build_initial_record()
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (initial, record):
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (proposal_tsv(initial), proposal):
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
