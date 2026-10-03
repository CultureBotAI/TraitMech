"""Add thermotaxis with a source-bounded Tar response graph and METPO proposal."""

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

SLUG = "thermotaxis"
IDENTIFIER = "traitmech:000580"
TARGET = ROOT / "data/traits/physiology/thermotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v457"
PAULICK = "DOI:10.7554/eLife.26607"
PASTER = "DOI:10.1073/pnas.0709903105"
NARA = "DOI:10.1074/jbc.271.30.17932"
NISHIYAMA = "DOI:10.1128/jb.179.21.6573-6580.1997"


def evidence(reference: str, snippet: str, notes: str) -> list[dict]:
    return [{"reference": reference, "snippet": snippet, "notes": notes}]


RECORD = {
    "identifier": IDENTIFIER,
    "label": "thermotaxis",
    "definition": (
        "A motile phenotype in which an organism biases its active movement "
        "in response to a temperature gradient."
    ),
    "definition_source": PAULICK,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        *evidence(
            PAULICK, "detect and follow environmental temperature gradients",
            "Paulick et al., Introduction; version 2, Version of Record dated "
            "2017-08-31, https://cdn.elifesciences.org/articles/26607/elife-26607-v2.pdf. "
            "Figures 1-3 and their figure supplements distinguish behavioral "
            "gradients from FRET reporters and chemical adaptation. "
            "Temperature preference for movement is not a growth-temperature class.",
        ),
        *evidence(
            PASTER, "responds to changes in temperature by modifying its motor behavior",
            "Paster and Ryu, Abstract and Results: thermal pulses changed "
            "tethered-cell motor bias. Their inversion temperatures are "
            "assay-specific, not universal trait thresholds. This assay "
            "measures motor output rather than spatial accumulation.",
        ),
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:83333",
        "taxon_label": "Escherichia coli K-12",
        "reference": PAULICK,
        "note": (
            "AW405, a K-12 derivative carrying a GFP marker, showed thermal "
            "migration in microfluidic gradients (Figures 1C and 2D-E; "
            "Methods: Strains and plasmids). It is not the engineered "
            "VS223 FRET reporter or the MG1655 growth assay."
        ),
    }],
    "causal_graphs": [{
        "graph_id": "thermotaxis_tar_response",
        "title": "Tar-mediated control of thermal migration",
        "description": (
            "A receptor-modification-dependent thermal response changes "
            "swimming bias and realizes thermotaxis."
        ),
        "scope_status": "MECHANISTIC",
        "scope_notes": (
            "The E. coli Tar-mediated arm, not a universal microbial mechanism "
            "or a complete Tar/Tsr accumulation model. Engineered receptor "
            "experiments establish the Tar transitions. Interplay with Tsr "
            "and chemical adaptation changes the intact-cell response."
        ),
        "nodes": [
            {
                "node_id": "thermotaxis_temperature_change",
                "label": "temperature change during movement",
                "node_type": "ENVIRONMENTAL_FACTOR",
                "description": "Temporal thermal stimulus encountered in a spatial gradient.",
            },
            {
                "node_id": "thermotaxis_tar_modification",
                "label": "Tar covalent modification state",
                "node_type": "STATE",
                "description": (
                    "Deamidation and methylation of Tar adaptation sites; "
                    "unprocessed, unmethylated and heavily methylated forms differ."
                ),
            },
            {
                "node_id": "thermotaxis_tar_receptor",
                "label": "Tar aspartate chemoreceptor",
                "node_type": "GENE_OR_PROTEIN",
                "gene_symbols": ["tar"],
                "description": "The full-length Tar receptor, including its thermal signaling role.",
                "grounding_status": "REVIEWED_LABEL_ONLY",
                "grounding_notes": (
                    "InterPro IPR003122 resolves to a Tar-related ligand-binding "
                    "domain, not the full receptor; IPR004090 covers the broader "
                    "MCP family. Neither is an exact whole-Tar grounding. "
                    "The reviewed K-12 protein remains an instance example."
                ),
                "protein_examples": [{
                    "uniprot_id": "UniProtKB:P07017",
                    "protein_label": "Methyl-accepting chemotaxis protein II",
                    "gene_symbol": "tar",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "retrieved_on": "2026-10-03",
                    "entry_version": 208,
                    "sequence_version": 2,
                    "role": "Tar component of the K-12 thermal response; not the entire receptor array.",
                    "evidence": evidence(
                        PAULICK, "both Tar- and Tsr-only cells exhibited thermophilic responses",
                        "Results, Figure 3A and Methods identify K-12 "
                        "Tar-only receptor experiments; UniProt verifies protein identity.",
                    ),
                }],
            },
            {
                "node_id": "thermotaxis_swimming_control",
                "label": "thermal control of run-and-tumble bias",
                "node_type": "BIOLOGICAL_PROCESS",
                "description": (
                    "Receptor signaling changes smooth-swimming versus tumbling; "
                    "this is not merely a change in swimming speed."
                ),
            },
            {
                "node_id": "thermotaxis_migration_process",
                "label": "thermotaxis",
                "node_type": "BIOLOGICAL_PROCESS",
                "grounding": "GO:0043052",
                "description": "Directed migration in response to a temperature gradient.",
            },
            {
                "node_id": "thermotaxis_trait",
                "label": "thermotaxis",
                "node_type": "TRAIT",
                "grounding": IDENTIFIER,
                "description": "Organism-level disposition for temperature-guided active movement.",
            },
        ],
        "edges": [
            {
                "subject": "thermotaxis_temperature_change",
                "predicate": "modulates",
                "predicate_id": "RO:0002211",
                "object": "thermotaxis_tar_receptor",
                "description": "Temperature changes elicit a Tar response when its modification state permits thermosensing.",
                "evidence": evidence(
                    NARA, "Tar comes to function as a thermoreceptor",
                    "Abstract: deamidation enables the thermal response; "
                    "the primary translational product is not a thermoreceptor.",
                ),
            },
            {
                "subject": "thermotaxis_tar_modification",
                "predicate": "modulates",
                "predicate_id": "RO:0002211",
                "object": "thermotaxis_tar_receptor",
                "description": "Covalent modification changes the receptor's warm, cold or null response state.",
                "evidence": evidence(
                    NISHIYAMA,
                    "thermosensing function that is modulated by covalent modification of its four methylation sites",
                    "Abstract: the mutational study distinguishes deamidation "
                    "from methylation and tests receptor thermosensing, not "
                    "a universal preferred temperature.",
                ),
            },
            {
                "subject": "thermotaxis_tar_receptor",
                "predicate": "regulates",
                "predicate_id": "RO:0002211",
                "object": "thermotaxis_swimming_control",
                "description": "Tar-mediated signaling changes swimming bias, with the response sign depending on receptor modification.",
                "evidence": evidence(
                    NARA, "eliciting a smooth-swimming signal upon increase of temperature",
                    "Abstract: this warm response applies to deamidated, "
                    "unmethylated Tar; the heavily methylated form instead "
                    "signals smooth swimming on cooling. Intermediate "
                    "phosphorelay steps are compressed, not bypassed.",
                ),
            },
            {
                "subject": "thermotaxis_swimming_control",
                "predicate": "contributes to",
                "predicate_id": "RO:0002326",
                "object": "thermotaxis_migration_process",
                "description": "Temperature-dependent run-and-tumble statistics bias migration along a thermal gradient.",
                "evidence": evidence(
                    PASTER, "This stochastic strategy biases the cell's random walk",
                    "Introduction: temporal temperature sensing biases runs "
                    "and tumbles, giving net movement along spatial gradients. "
                    "The separate motor assay is not itself a migration measurement.",
                ),
            },
            {
                "subject": "thermotaxis_migration_process",
                "predicate": "confers",
                "predicate_id": "METPO:2007700",
                "object": "thermotaxis_trait",
                "description": "Temperature-guided migration realizes the organismal thermotaxis phenotype.",
                "evidence": evidence(
                    PAULICK, "cells accumulated towards the warmer side of the gradient",
                    "Results, Figure 1C: buffer-adapted swimming cells; "
                    "chemical adaptation can alter the direction (Figure 2).",
                ),
            },
        ],
    }],
    "discussions": [{
        "discussion_id": "thermotaxis-context-and-mapping-boundaries",
        "prompt": "Resolve assay-dependent response inversion without imposing a universal temperature threshold.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "DOI:10.1073/pnas.0709903105 reports thermal-response inversion "
            "under its tethered-cell conditions. DOI:10.7554/eLife.26607 "
            "instead finds continued warm-seeking in buffer under flow; "
            "its Discussion suggests residual chemical stimulation as one "
            "explanation of earlier results, not a proven correction. "
            "Retain medium, adaptation, strain and assay context. Growth "
            "optima, passive thermophoresis and temperature-dependent speed "
            "alone do not establish thermotaxis. GO:0043052 is a biological "
            "process (QuickGO checked 2026-10-03), so it grounds the process "
            "node rather than an equivalent xref on the disposition. "
            "The Tar arm does not describe every thermotactic microbe."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added thermotaxis with four primary DOI sources, exact snippets, "
            "a K-12 behavioral example and a Tar-mediated causal graph. "
            "Verified P07017, NCBITaxon:83333 and GO:0043052 at authorities. "
            "Ignored-and-hidden searches found no exact record or METPO term; "
            "reserved METPO:1053400 in proposal v457. Kept assay-dependent "
            "inversion separate from growth-temperature preference."
        ),
        llm_assisted=True, timestamp="2026-10-03T22:20:00Z",
    )
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
        "METPO:1053400", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/{SLUG}.yaml|{PAULICK}|{PASTER}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Active temperature-guided movement; not a growth-temperature optimum.", IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
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
