"""Add galvanotaxis with a scoped flagellar-motility graph and METPO proposal."""

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

SLUG = "galvanotaxis"
IDENTIFIER = "traitmech:000581"
TARGET = ROOT / "data/traits/physiology/galvanotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v458"
ADLER = "DOI:10.1101/sqb.1988.053.01.006"
SHI = "DOI:10.1128/jb.178.4.1113-1119.1996"
SUN = "DOI:10.1038/s41564-024-01778-8"
INTERPRO = "https://www.ebi.ac.uk/interpro/entry/InterPro/IPR001492/"
SALMONELLA = "Salmonella enterica subsp. enterica serovar Typhimurium str. 14028S"
SOURCE_DATA = (
    "https://media.springernature.com/original/springer-static/esm/"
    "art%3A10.1038%2Fs41564-024-01778-8/MediaObjects/41564_2024_1778_MOESM10_ESM.xlsx"
)


def evidence(reference: str, snippet: str, notes: str) -> list[dict]:
    return [{"reference": reference, "snippet": snippet, "notes": notes}]


RECORD = {
    "identifier": IDENTIFIER,
    "label": "galvanotaxis",
    "definition": (
        "A motile phenotype in which an organism biases its active movement "
        "in response to an electric field."
    ),
    "definition_source": ADLER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        *evidence(
            ADLER,
            "movement of a motile organism or cell in direct response to an electric current",
            "Adler and Shi, publisher's freely accessible Excerpt, "
            "https://symposium.cshlp.org/content/53/23.short. "
            "The full paywalled paper was not accessed. The disposition "
            "requires active motility; passive electrophoretic displacement alone is insufficient.",
        ),
        *evidence(
            SHI,
            "motile Escherichia coli K-12 placed in an electric field swims toward the anode",
            "Shi, Stocker and Adler, primary abstract (PMID:8576046), "
            "verified through Europe PMC. Rough K-12 and smooth Salmonella "
            "differ in direction; surface composition and capsules qualify "
            "the response. Only the abstract was accessed, not the full paper.",
        ),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "reference": SHI,
            "note": (
                "The primary abstract reports anode-directed swimming of "
                "motile rough K-12 cells. This is not a claim about every "
                "E. coli strain or an invariant direction across surface compositions."
            ),
        },
        {
            "taxon_id": "NCBITaxon:588858",
            "taxon_label": SALMONELLA,
            "reference": SUN,
            "note": (
                "Figure 5 and Supplementary Table 1: Green ST is IR715, a "
                "nalidixic-acid-resistant 14028S derivative, carrying pGFT/RalFc. "
                "These fluorescent cells migrated toward the cathode at 2 V/cm "
                "in vitro. Do not substitute the SW473 flagellar mutant or "
                "the separate cheB mutant for this behavioral example."
            ),
        },
    ],
    "causal_graphs": [{
        "graph_id": "galvanotaxis_flagellar_motility",
        "title": "Flagellar motility in electric-field-biased migration",
        "description": "Flagellin supports the motility apparatus used for active galvanotaxis.",
        "scope_status": "MECHANISTIC",
        "scope_notes": (
            "The flagellar-motility branch supported in Salmonella 14028S-background "
            "cells, not a complete electrical sensing or orientation mechanism. "
            "The fliC/fljB double mutant establishes dependence on the flagellar "
            "apparatus, not individual FliC necessity or flagellin sufficiency. "
            "Host CFTR is outside this microbial graph."
        ),
        "nodes": [
            {
                "node_id": "galvanotaxis_electric_field",
                "label": "electric field",
                "node_type": "ENVIRONMENTAL_FACTOR",
                "description": "Applied electrical stimulus, 2 V/cm in the Sun et al. in vitro assay.",
            },
            {
                "node_id": "galvanotaxis_flagellin",
                "label": "flagellin",
                "node_type": "GENE_OR_PROTEIN",
                "grounding": "InterPro:IPR001492",
                "gene_symbols": ["fliC", "fljB"],
                "description": (
                    "Flagellin family forming the flagellar filament; not the "
                    "entire flagellum, its rotary motor or an established electrical sensor."
                ),
                "protein_examples": [{
                    "uniprot_id": "UniProtKB:A0A0F6B2U2",
                    "protein_label": "Flagellin",
                    "gene_symbol": "fliC",
                    "taxon_id": "NCBITaxon:588858",
                    "taxon_label": SALMONELLA,
                    "entry_status": "UNREVIEWED",
                    "proteome_id": "UP000002695",
                    "retrieved_on": "2026-10-03",
                    "entry_version": 42,
                    "sequence_version": 1,
                    "role": (
                        "FliC is one of the two alternative flagellins removed "
                        "together in SW473; individual FliC necessity was not established."
                    ),
                    "evidence": evidence(
                        SUN, "Most of these mutants were non-motile",
                        "Results, flagellar-mutant paragraph and Supplementary "
                        "Table 1: SW473 is an IR715 fliC/fljB double mutant. "
                        "The exact 14028S FliC identity, taxon and versions were "
                        "resolved at https://www.ebi.ac.uk/proteins/api/proteins/A0A0F6B2U2; "
                        "https://rest.uniprot.org/proteomes/UP000002695.json "
                        "confirms reference-proteome membership. UniProtKB REST "
                        "protein requests failed during retrieval; the EBI Proteins "
                        "API supplied the metadata. This accession anchors the "
                        "strain background, not an experimentally sequenced SW473 protein.",
                    ),
                }],
            },
            {
                "node_id": "galvanotaxis_flagellar_motility",
                "label": "flagellar motility",
                "node_type": "BIOLOGICAL_PROCESS",
                "grounding": "GO:0071973",
                "description": "Active movement powered by the bacterial flagellar apparatus.",
            },
            {
                "node_id": "galvanotaxis_process",
                "label": "electric-field-biased active migration",
                "node_type": "BIOLOGICAL_PROCESS",
                "description": "Biased active movement, not passive drift of fixed cells.",
            },
            {
                "node_id": "galvanotaxis_trait",
                "label": "galvanotaxis",
                "node_type": "TRAIT",
                "grounding": IDENTIFIER,
                "description": "Organismal disposition for electric-field-guided active movement.",
            },
        ],
        "edges": [
            {
                "subject": "galvanotaxis_electric_field",
                "predicate": "modulates",
                "predicate_id": "RO:0002211",
                "object": "galvanotaxis_process",
                "description": "An applied electric field biases active migration direction.",
                "evidence": evidence(
                    SUN, "robustly biased migration of all cells",
                    "Results and Figure 5c-e compare no-field and 2 V/cm "
                    "conditions. DH5alpha K-12-background cells migrated toward "
                    "the anode and IR715-background cells toward the cathode. "
                    "This edge does not prescribe one direction for every microbe.",
                ),
            },
            {
                "subject": "galvanotaxis_flagellin",
                "predicate": "contributes to",
                "predicate_id": "RO:0002326",
                "object": "galvanotaxis_flagellar_motility",
                "description": "Flagellin supplies the filament component of the motility apparatus.",
                "evidence": evidence(
                    INTERPRO, "Flagellin is the subunit protein that polymerises to form the flagella",
                    "InterPro IPR001492 family description, verified through "
                    "https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001492/ "
                    "on 2026-10-03. This is a family, not merely an N- or "
                    "C-terminal domain. Filament assembly and the motor are "
                    "also required; flagellin alone is not sufficient for movement.",
                ),
            },
            {
                "subject": "galvanotaxis_flagellar_motility",
                "predicate": "contributes to",
                "predicate_id": "RO:0002326",
                "object": "galvanotaxis_process",
                "description": "Flagellar motility enables active electrical-field-guided migration.",
                "evidence": evidence(
                    SUN, "flagella are indeed essential for electrical field-guided galvanotaxis",
                    "Results, flagellar-mutant experiment: SW473 cells were "
                    "mostly non-motile and unresponsive. This establishes a "
                    "motility requirement, not a specific electrical sensor. "
                    "Fixed-cell controls distinguish passive drift from live-cell swimming.",
                ),
            },
            {
                "subject": "galvanotaxis_process",
                "predicate": "confers",
                "predicate_id": "METPO:2007700",
                "object": "galvanotaxis_trait",
                "description": "Electric-field-guided active movement realizes the galvanotaxis phenotype.",
                "evidence": evidence(
                    ADLER, "migration is toward the cathode or the anode",
                    "Publisher's free Excerpt defines galvanotaxis and allows "
                    "either pole. Direction depends on organism and context, "
                    "rather than being a universal part of this trait definition.",
                ),
            },
        ],
    }],
    "discussions": [
        {
            "discussion_id": "galvanotaxis-orientation-and-mapping-boundaries",
            "prompt": "Resolve electrical orientation mechanisms without equating active motility with passive drift.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "DOI:10.1128/jb.178.4.1113-1119.1996 proposes differential "
                "electrophoretic mobility of the body and flagellar filaments "
                "as an orientation model. DOI:10.1038/s41564-024-01778-8 "
                "observes flagellar redistribution and a largely non-motile "
                "double mutant; it does not establish a universal receptor "
                "circuit or separate the individual flagellin contributions. "
                "A cheB mutant retains the electrical response. The source's "
                "weakly biased B. subtilis assay is not a robust canonical "
                "example. Physical orientation can guide powered locomotion, "
                "but fixed-cell drift alone is not this phenotype. QuickGO "
                "searches for galvanotaxis and electrotaxis found no exact "
                "term on 2026-10-03; MeSH Taxis Response is broader and "
                "excluded from xrefs. GO:0071973 grounds only the flagellar process."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        },
        {
            "discussion_id": "galvanotaxis-source-data-coordinate-convention",
            "prompt": "Reconcile directedness signs before importing numerical source-data values.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Sun et al., Figure 5d and Results report negative directedness "
                "for E. coli and positive for Salmonella. The source workbook's "
                "Fig. 5d,e sheet labels Red to anode and Green to cathode but "
                "contains opposite-signed cosine values. Direction labels agree "
                "with Figure 5c and the 1996 primary abstract; the coordinate "
                "conventions need reconciliation. No numerical directedness "
                "values are imported and no correction is inferred. Source: " + SOURCE_DATA
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added galvanotaxis with three primary DOI sources, an InterPro "
            "family source, exact snippets, two strain-qualified examples "
            "and a flagellar-motility graph. Verified NCBI taxa, IPR001492, "
            "GO:0071973, the 14028S FliC accession and its reference proteome. "
            "Ignored-and-hidden searches found no exact trait or METPO class; "
            "reserved METPO:1053500 in proposal v458. Kept electrical "
            "orientation and source-data sign conventions as open questions."
        ),
        llm_assisted=True, timestamp="2026-10-03T23:20:08Z",
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
        "METPO:1053500", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/{SLUG}.yaml|{ADLER}|{SHI}|{SUN}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Active electric-field-guided movement; not passive electrophoretic drift.", IDENTIFIER,
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
