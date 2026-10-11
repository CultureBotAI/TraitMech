"""Add cytoplasmic bacterial predation through the guarded validated writer."""

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
SLUG = "cytoplasmic_bacterial_predation"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/predatory_bacterium.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v576/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000700"
METPO_ID = "METPO:1065300"
PARENT_ID = "traitmech:000054"
PARENT_METPO_ID = "METPO:1007653"
IDENTITY = "DOI:10.1073/pnas.83.7.2138"
TERMINOLOGY = "https://lpsn.dsmz.de/genus/daptobacter"
TIMESTAMP = "2026-10-11T15:30:45Z"
PARENT = {
    "identifier": PARENT_ID,
    "label": "predatory bacterium",
    "definition": (
        "A trophic-ecology lifestyle in which a bacterium actively kills and consumes "
        "other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus."
    ),
    "definition_source": "DOI:10.1146/annurev.micro.091208.073346",
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000059"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "cytoplasmic bacterial predation",
    "definition": (
        "A predatory bacterial phenotype in which a bacterium enters the cytoplasm "
        "of a bacterial prey cell and grows and reproduces there by consuming "
        "and degrading the prey cytoplasm."
    ),
    "definition_source": IDENTITY,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": IDENTITY,
            "snippet": (
                "Daptobacter penetrates both membranes of the prey cell walls "
                "and reproduces in their degrading cytoplasm."
            ),
            "notes": (
                "Guerrero et al. 1986, PMID:11542073, PMC323246, Figure 2E caption "
                "continued on p. 2141. Full five-page primary paper read from the "
                "Europe PMC PDF, including Methods, Results and Discussion, Table 2 "
                "and the note added in proof; actual Figure 2E/F micrographs and "
                "continued caption visually inspected. Enrichment-culture thin "
                "sections support prey-cytoplasmic invasion, degradation and "
                "division; these are not live-cell time courses or nutrient-tracing "
                "experiments. Figure 3 is a schematic, not additional experimental "
                "imaging. The scientific abstract was independently retrieved with "
                "EXT_ID:11542073 AND SRC:MED and title/DOI checked. MED and Crossref "
                "exposed no linked correction/retraction; publisher notice access "
                "returned HTTP 403, so that status is unverified. Source: "
                "https://europepmc.org/articles/PMC323246?pdf=render."
            ),
        },
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "invade their host cells and replicate in the cytoplasm, "
                "consuming their prey from the inside out"
            ),
            "notes": (
                "LPSN genus Daptobacter, Notes, directly retrieved 2026-10-11. "
                "LPSN quotes this description from Madigan et al. 2019; that book "
                "was not independently read. Supports established terminology, "
                "not independent experimental replication of Guerrero et al. "
                "LPSN marks the genus name not validly published and preferred "
                "rather than correct. Its permanent record link is "
                "https://doi.org/10.83108/rn.684. The nomenclatural record is not "
                "evidence for a sequence-defined lineage or an NCBITaxon mapping."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "cytoplasmic-predation-boundaries-and-mappings",
            "prompt": "Keep prey-cytoplasmic feeding distinct from generic intracellular residence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Predatory bacterium traitmech:000054 supplies the broader trophic "
                "phenotype. Periplasmic bacterial predation traitmech:000699 has a "
                "different replication compartment; epibiotic bacterial predation "
                "traitmech:000697 keeps the predator cell body external. Generic "
                "endobiotic or intracellular predation, endoparasitism and "
                "endosymbiosis are not exact synonyms. Guerrero et al. discuss "
                "predator/parasite and primary-consumer terminology on pp. 2141-2142; "
                "the operational feeding/location definition here does not settle "
                "that broader ecological vocabulary. Entry alone or intracellular "
                "growth without destructive prey consumption is insufficient. No "
                "organism-level disjointness, fixed prey range or obligate prey "
                "dependence is asserted. Exact synonyms and authority-backed xrefs "
                "remain unassigned pending scope reconciliation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "cytoplasmic-predation-taxon-and-mechanism",
            "prompt": "Resolve the historical isolate and its mechanism before grounding examples.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The primary study describes Daptobacter in lake-derived enrichment "
                "cultures and reports axenic growth; it does not make cytoplasmic "
                "predation an obligate lifestyle. No exact NCBITaxon identity for "
                "the observed material has been established in this curation, so "
                "canonical_examples is intentionally omitted. LPSN nomenclature "
                "does not supply that missing mapping. The second evidence item "
                "is terminology support, not another experiment. Protein-resolved "
                "mechanism, modern replication and lineage breadth remain open; "
                "do not infer causal machinery from a taxon name, sequence "
                "prediction or the different Bdellovibrio model. No causal graph "
                "or protein examples are proposed."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cytoplasmic bacterial predation beneath predatory bacterium "
            "with primary microscopy and explicitly secondary LPSN terminology "
            "evidence, both carrying checked snippets. Ignored/hidden main/worktree "
            "and pending-PR checks support 000700 and v576 block 1065300-1065399. "
            "Existing records unchanged; taxon identity, mappings and mechanism "
            "remain open. Timestamp records the observed UTC curation decision."
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
        [PARENT_METPO_ID, PARENT["label"], PARENT["definition"],
         "TraitMech:data/traits/ecology/predatory_bacterium.yaml|" + PARENT["definition_source"],
         "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
         "Existing v5 parent ID and meaning; included for standalone hierarchy.", PARENT_ID],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Prey-cytoplasmic invasion with destructive feeding and reproduction; not residence alone.",
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
