"""Add energy taxis with source-bounded electron-transport sensing evidence."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000590"
TARGET = ROOT / "data/traits/physiology/energy_taxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v467"
ALEXANDRE = "DOI:10.1128/jb.182.21.6042-6048.2000"
GREER = "DOI:10.1128/jb.186.19.6595-6604.2004"
ATCC = "https://www.atcc.org/products/29145"

# Exact original evidence preimage, accepted only for the reviewed #1660 migration.
LEGACY_ATCC_EVIDENCE = {
    "reference": ATCC,
    "snippet": (
        "Isolation source Digitaria decumbens roots, plant "
        "Geographical isolation Brazil"
    ),
    "notes": (
        "ATCC 29145 culture-collection entry, accessed 2026-10-04. "
        "Two adjacent provenance fields, exact-matched after HTML "
        "whitespace normalization. The entry identifies a type strain "
        "and traces custody through J Dobereiner to Sp. 7. This "
        "supports environmental strain provenance, not an independent "
        "measurement of energy taxis or identity of every laboratory "
        "descendant's genome."
    ),
}

RECORD = {
    "identifier": IDENTIFIER,
    "label": "energy taxis",
    "definition": (
        "A motile phenotype in which directional locomotion is regulated by "
        "sensing changes in the electron transport system associated with "
        "cellular energy generation."
    ),
    "definition_source": GREER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": ALEXANDRE,
            "snippet": (
                "behavioral responses to most stimuli in A. brasilense are "
                "triggered by changes in the electron transport system."
            ),
            "notes": (
                "Abstract exact-matched at Europe PMC (PMID:11029423). Publisher "
                "Methods, Results and Discussion also inspected. Sp7 (ATCC "
                "29145), wild type for chemotaxis, is distinguished from the "
                "cytN mutant FAJ851. Spatial and temporal assays, metabolic "
                "inhibition and electron-donor bypass support the sensing "
                "interpretation beyond growth correlation. Nitrate and DMSO "
                "taxis are reported under anaerobic conditions. The study "
                "does not decide whether redox state or ion motive force is "
                "the sensed signal; capillary aerotaxis can confound apparent "
                "substrate chemotaxis. No universal substrate range is inferred."
            ),
        },
        {
            "reference": GREER,
            "snippet": (
                "Motility responses triggered by changes in the electron "
                "transport system are collectively known as energy taxis."
            ),
            "notes": (
                "Abstract exact-matched at Europe PMC (PMID:15375141); full text "
                "not fully inspected. The tlp1 mutant is deficient in responses "
                "to oxidizable substrates, terminal electron acceptors and "
                "redox conditions. The proposed sensory domain's function "
                "remains unknown in this source. Root-colonization impairment "
                "supports an ecological hypothesis, not universal host "
                "specificity or an identified direct ligand. No complete "
                "protein-resolved pathway is inferred from the abstract."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:192",
            "taxon_label": "Azospirillum brasilense",
            "reference": ALEXANDRE,
            "note": (
                "Sp7 (ATCC 29145), the study's wild type for chemotaxis, not "
                "the cytN mutant FAJ851. Observed substrate, electron-acceptor "
                "and repellent responses support energy taxis under the "
                "reported conditions. Environmental provenance is independently "
                "documented at https://www.atcc.org/products/29145. NCBI "
                "resolved 192 on 2026-10-04 at species rank; it is not an "
                "exact strain accession or a claim about all strains."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "energy-taxis-stimulus-and-mapping-boundaries",
            "prompt": "Keep energy sensing distinct from stimulus-defined taxis classes.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This entry follows the electron-transport-based usage in "
                "the cited primary studies. Energy generation powering motility "
                "alone is insufficient: changes must inform locomotor control. "
                "Aerotaxis, phototaxis and chemotaxis can involve other sensing "
                "mechanisms and are not automatically children or exact "
                "synonyms. Metabolism-dependent chemotaxis can instead sense "
                "intracellular intermediates, so that broader phrase is not "
                "an exact synonym. The existing flagellar-specific chemotaxis "
                "record is not used as a universal parent. Resolve external "
                "mappings at their authorities and compare process versus "
                "organismal-disposition scope before adding xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "energy-taxis-signal-and-protein-grounding",
            "prompt": "Verify the sensed signal and taxon-paired molecular branches.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Electron-transport perturbations support energy-dependent "
                "locomotor control without identifying one universal receptor "
                "or deciding redox-state versus ion-motive-force sensing. "
                "Inspect full mutant, complementation and domain-function "
                "evidence and resolve taxon-paired protein accessions before "
                "adding causal edges. Do not substitute a protein/domain "
                "sequence feature for this organismal phenotype or use a "
                "NONMECHANISTIC graph to bypass molecular grounding."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added energy taxis with two primary DOI studies, an ATCC provenance "
            "URL and exact snippets. Ignored-and-hidden searches found no exact "
            "record or METPO term. Reserved METPO:1054400 in v467. Verified "
            "Sp7 collection provenance and NCBITaxon:192 species identity. "
            "Kept stimulus-defined taxis classes separate and deferred "
            "unverified molecular branches and external mappings."
        ),
        llm_assisted=True, timestamp="2026-10-04T06:51:06Z",
    )
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE",
        changes=(
            "Addressed review issue #1660: removed ATCC provenance fields "
            "from trait evidence and retained the stable strain-provenance "
            "URL in the canonical example note. Both primary DOI studies "
            "and their verified abstract snippets remain."
        ),
        llm_assisted=True, timestamp="2026-10-04T07:25:57Z",
    )
    return record


def build_pre_review_record() -> dict:
    record = build_record()
    record["evidence"].append(copy.deepcopy(LEGACY_ATCC_EVIDENCE))
    record["curation_history"].pop()
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1054400", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/energy_taxis.yaml|{GREER}|{ALEXANDRE}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Electron-transport sensing controls locomotion; not energy supply alone.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists():
        existing = yaml.safe_load(TARGET.read_text())
        if existing not in (record, build_pre_review_record()):
            raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
