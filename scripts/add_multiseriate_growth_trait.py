"""Add evidence-backed cyanobacterial multiseriate trichome formation."""

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
SLUG = "cyanobacterial_multiseriate_trichome_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v552/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000676"
METPO_ID = "METPO:1062900"
CYTOSKELETON = "DOI:10.1002/2211-5463.13016"
PLASTICITY = "DOI:10.1186/s12862-017-1053-5"
FIELD = "DOI:10.3126/on.v14i1.16445"
TIMESTAMP = "2026-10-08T07:45:42Z"
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
    "label": "cyanobacterial multiseriate trichome formation",
    "definition": (
        "A morphological phenotype in which a cyanobacterium develops a trichome "
        "containing more than one adjacent row of cells through cell division "
        "in multiple planes."
    ),
    "definition_source": CYTOSKELETON,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": CYTOSKELETON,
            "snippet": (
                "cells divide at a right angle to the longitudinal filament axis "
                "and in planes parallel or oblique to the primary trichomes."
            ),
            "notes": (
                "Springstein et al. (2020), Introduction; primary full-text XML "
                "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7714070/fullTextXML "
                "and actual Figure 2E inspected. The text links multiplanar "
                "division to multiseriate Chlorogloeopsis fritschii PCC 6912 "
                "trichomes, contrasting them with lateral Fischerella branches. "
                "Figure 2E shows a mature multiseriate stage, distinct from the "
                "linear hormogonium in 2D. Methods describe stock cultures at "
                "37 degrees C in BG11 or BG11(0), with an 18:6 light-dark cycle; "
                "Van-FL microscopy follows a one-hour stain. This morphology "
                "evidence is not the separate FtsZ-overexpression phenotype."
            ),
        },
        {
            "reference": PLASTICITY,
            "snippet": "When grown in BG11, C. fritschii developed multi-seriate filaments.",
            "notes": (
                "Koch et al. (2017), Additional file 1, Figure S6A caption, "
                "PDF page 8; actual S6 and S1 images and supplementary text "
                "pages 1-2 inspected at https://media.springernature.com/original/"
                "springer-static/esm/art%3A10.1186%2Fs12862-017-1053-5/"
                "MediaObjects/12862_2017_1053_MOESM1_ESM.pdf. S6B instead shows "
                "aseriate clusters with 100 mM NaCl; loose clusters are not "
                "automatically multiseriate trichomes. Main Results and S1 "
                "report salt-associated multiseriate main filaments in "
                "Fischerella, showing that branching and multiseriality can "
                "coexist and that salt responses are taxon-specific. "
                "Transcript correlations do not establish a universal mechanism."
            ),
        },
        {
            "reference": FIELD,
            "snippet": (
                "The present algal taxon exhibited vertical and horizontal "
                "divisions of cells and has a tendency to form filamentous structure."
            ),
            "notes": (
                "Halder (2016), Results and discussion, article page 95, "
                "https://www.nepjol.info/index.php/ON/article/view/16445/13360. "
                "Methods, description and actual Figure 1A-D on page 96 "
                "inspected. The description records cell rows and Conclusions "
                "describe progression from uniseriate to multiseriate filaments. "
                "This is light-microscopy-based identification of field material, "
                "not sequence-confirmed identity, a controlled time-lapse lineage "
                "experiment, or proof of the paper's suggested fertilizer benefit."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1124",
            "taxon_label": "Chlorogloeopsis fritschii",
            "reference": FIELD,
            "note": (
                "Restricted to the multiseriate stage described for field "
                "collection NH-1260, sampled on 18 March 2013 in a rice field "
                "at Balagarh, Hooghly, West Bengal, India. Provenance and "
                "herbarium deposition are reported in Methods/Results at "
                "https://www.nepjol.info/index.php/ON/article/view/16445/13360. "
                "The source identifies the material morphologically; it is not "
                "assigned a PCC strain identity. Live NCBI efetch "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=1124 confirms the current species name and "
                "rank species, not an NH-1260 accession or independent phenotype "
                "evidence. Not every cell, stage or condition is multiseriate."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "multiseriate-trichome-scope",
            "prompt": "Review the closer multicellular morphology parent and terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059 below quality METPO:1000188. "
                "The definition concerns adjacent cell rows in a trichome, "
                "including two rows, not multiple independent uniseriate "
                "trichomes merely bundled in a common sheath. It is not a "
                "synonym of branched shaped METPO:1000687, generic filament "
                "shaped morphology, hormogonium formation traitmech:000651, "
                "or cyanobacterial false branching traitmech:000675. "
                "Cell-shape parents do not unambiguously capture this "
                "multicellular organization; obsolete cell-arrangement terms "
                "redirect to flagellar arrangement and are unsuitable. "
                "Springstein's parenthetical description speaks of multiple "
                "trichomes in a row, whereas its division context and the "
                "other inspected sources support adjacent cell rows. Keep "
                "that wording distinction explicit. The qualified label "
                "does not cover every multiseriate algal or plant structure. "
                "No exact synonyms, xrefs, SSSOM mappings, mandatory branching "
                "or organism-level disjointness are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "multiseriate-trichome-mechanism",
            "prompt": "Resolve native division-plane control without conflating experimental states.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The cited studies distinguish natural developmental states, "
                "environment-associated changes and engineered protein "
                "overexpression. Do not transfer an engineered phenotype to "
                "a natural canonical example or infer a gene mechanism from "
                "transcript correlations. Neither salt exposure, a fixed "
                "row number, a persistent filament length nor a fitness "
                "benefit defines the whole class. No causal graph is proposed "
                "pending a protein-resolved native mechanism with verified "
                "accessions; mechanism is deferred, not claimed absent."
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
            "Added cyanobacterial multiseriate trichome formation with three "
            "DOI sources, source-checked snippets and a qualified field "
            "example. Ignored-and-hidden main/worktree/open-PR checks support "
            "000676 and v552 block 1062900-1062999. Kept branching, loose "
            "clusters, bundled trichomes and engineered morphotypes distinct. "
            "Existing records unchanged; timestamp is observed UTC."
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
         "Adjacent cell rows; not loose clusters or independent bundled trichomes; no universal salt or protein requirement.",
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
