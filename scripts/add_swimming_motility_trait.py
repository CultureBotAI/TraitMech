"""Add swimming motility through the guarded validated writer."""

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
SLUG = "swimming_motility"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/morphology/motile.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v578/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000702"
METPO_ID = "METPO:1065500"
IDENTITY = "DOI:10.1038/s41467-020-18253-7"
BOUNDARY = "DOI:10.1038/s41467-018-07802-w"
TIMESTAMP = "2026-10-11T18:17:31Z"
PARENT = {
    "identifier": "METPO:1000702",
    "label": "motile",
    "definition": (
        "A motility in which an organism has the ability to move independently "
        "using metabolic energy."
    ),
    "definition_source": "DOI:10.1038/s41579-021-00626-4",
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000701"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "swimming motility",
    "definition": (
        "A motile phenotype in which an organism propels itself through a liquid medium."
    ),
    "definition_source": IDENTITY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": IDENTITY,
            "snippet": "Their swimming direction is stabilised by their flagella (archaella)",
            "notes": (
                "Thornton et al. 2020, PMID:32901025, PMC7478972, scientific abstract. "
                "Qualified MED identity, title and DOI checked. Results, Swimming "
                "behaviour in three dimensions, and Methods on culture and holographic "
                "reconstruction directly support liquid swimming by environmental "
                "Haloferax sp. Boulby Mine and Haloarcula sp. Great Salt Lake isolates. "
                "Mean-squared displacement separated swimming from diffusion. Figure 2 "
                "was visually inspected; Supplementary Note 1 describes sampling "
                "locations. Methods explicitly leave exact species unresolved. "
                "Cultures were grown in 25% dissolved-salt MGM to early exponential "
                "phase. The measured trajectories, not merely genes or simulations, "
                "support the phenotype. Chemotactic efficiency simulations do not "
                "define swimming or establish a universal speed optimum. Raw movies "
                "were not reanalyzed. MED, Crossref and the retrieved publisher page "
                "exposed no linked correction or retraction at the check. Source: "
                "https://www.nature.com/articles/s41467-020-18253-7."
            ),
        },
        {
            "reference": BOUNDARY,
            "snippet": (
                "However, the free-swimming capability of the different strains did not "
                "correlate well to the spreading capability in soft agar."
            ),
            "notes": (
                "Kuhn et al. 2018, PMID:30560868, PMC6299084, Results, Filament "
                "composition affects flagella-mediated swimming; quote checked directly "
                "in full-text XML, not the abstract. Qualified MED identity and DOI "
                "checked. Figure 3 and Supplementary Table 1 (printed p. 10, PDF "
                "p. 11) were visually inspected. All studied S. putrefaciens CN-32 "
                "backgrounds lack lateral flagellin genes; the paper calls this "
                "delta-flaA2B2 background wild type relative to the polar flagellum. "
                "Methods distinguish three-dimensional cell tracking in regular or "
                "Ficoll-supplemented liquid from soft-agar spreading, and reject "
                "Brownian-only tracks. Thus liquid swimming is observed in engineered "
                "material; it is not inferred from agar halos or a sequence feature. "
                "Filament simulations are separate model evidence. Raw movies were "
                "not reanalyzed. MED, Crossref and the retrieved publisher page exposed "
                "no linked correction or retraction at the check. Source: "
                "https://www.nature.com/articles/s41467-018-07802-w."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "swimming-motility-scope-and-assays",
            "prompt": "Keep liquid propulsion distinct from surface movement and passive displacement.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Motile METPO:1000702 is the broader energy-dependent locomotion "
                "phenotype. Swimming concerns propulsion through liquid, including "
                "near a boundary, not locomotion across a supporting substrate. "
                "Swarming traitmech:000062, twitching traitmech:000061 and gliding "
                "METPO:1000706 are not exact synonyms. Passive advection, settling, "
                "Brownian motion, colony growth and appendage possession alone are "
                "insufficient. Neither a particular speed, solitary behavior, "
                "chemotaxis nor a specified propulsion apparatus is required. "
                "Bacterial flagella and archaeal archaella must not be conflated. "
                "An organism can exhibit swimming and surface motility in different "
                "conditions; no organism-level disjointness is asserted. Existing "
                "flagellar-motility process nodes, swimming-velocity capacities and "
                "taxis discussions are not exact ungrounded instances of this "
                "trait. Upstream METPO issue 271 requests this gap; it does not "
                "supply an accepted identifier. External phenotype equivalences "
                "and lexical variants remain unasserted pending authority checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "swimming-motility-examples-and-mechanisms",
            "prompt": "Resolve taxon-specific examples and mechanisms without inferring motion from sequence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned in this first pass: the "
                "haloarchaeal isolates lack resolved species identities in the "
                "study, and exact taxon anchors for the bacterial experimental "
                "background have not been independently verified here. Engineered "
                "material remains valid qualified phenotype evidence, not an "
                "unmodified natural exemplar. A causal graph is deferred pending "
                "source-bounded branches and eligible taxon-paired protein "
                "examples. Do not impose one lineage's motor or chemotaxis "
                "machinery on all swimming organisms, or use a NONMECHANISTIC "
                "graph to bypass grounding requirements. A flagellin, archaellin, "
                "motor gene or predicted motility system alone does not establish "
                "liquid propulsion under a tested condition. The present evidence "
                "covers bacterial and archaeal cases, not a systematic survey of "
                "eukaryotic propulsion or every swimming mechanism."
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
            "Added liquid swimming motility beneath motile with two DOI-backed "
            "primary studies and checked verbatim abstract/full-text snippets. "
            "Ignored/hidden worktree, live ontology and pending-PR checks support "
            "000702 and v578 block 1065500-1065599. Existing records unchanged. "
            "Assay, strain and sequence-inference limits are explicit. "
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Liquid self-propulsion, not passive displacement or agar spreading alone.", IDENTIFIER],
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
