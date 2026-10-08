"""Add a cyanophycin storage inclusion with source-bounded protein evidence."""

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
SLUG = "cyanophycin_granule"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/morphology/intracellular_inclusion.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v549/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000673"
METPO_ID = "METPO:1062600"
PARENT_METPO_ID = "METPO:1007665"
TIMESTAMP = "2026-10-08T04:30:00Z"
CORRECTION_TIMESTAMP = "2026-10-08T04:29:03Z"
CELL_BIOLOGY = "DOI:10.1128/AEM.01298-18"
ACCUMULATION = "DOI:10.1007/s002030100281"
EXPRESSION = "DOI:10.1007/s002030000206"
PURIFICATION = "DOI:10.1128/AEM.67.5.2176-2182.2001"
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
PARENT = {
    "identifier": "traitmech:000066",
    "label": "intracellular inclusion",
    "definition": (
        "A morphology trait describing a discrete intracellular body \u2014 a storage "
        "granule, gas-filled structure, or protein-bounded microcompartment/organelle "
        "\u2014 that compartmentalizes material or function within a prokaryotic cell."
    ),
    "definition_source": "DOI:10.1038/s41579-020-0413-0",
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000059"],
}
PARENT_ROW = [
    PARENT_METPO_ID, PARENT["label"], PARENT["definition"],
    "TraitMech:data/traits/morphology/intracellular_inclusion.yaml",
    "METPO:1000059", "", "", "metpo_traitmech_2026_06", "", "", PARENT["identifier"],
]
ENZYME_SNIPPET = (
    "which catalyzed the incorporation of arginine and aspartic acid into cyanophycin"
)
RECORD = {
    "identifier": IDENTIFIER,
    "label": "cyanophycin granule",
    "definition": (
        "An intracellular storage inclusion composed of cyanophycin, a nonribosomal "
        "arginine- and aspartate-rich polymer serving as a nitrogen reserve."
    ),
    "definition_source": CELL_BIOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ACCUMULATION,
            "snippet": (
                "Cyanophycin granules reached a maximum after the peak of "
                "nitrogenase activity and eventually were utilized completely."
            ),
            "notes": (
                "Li et al. (2001), publisher scientific abstract directly read at "
                "https://link.springer.com/article/10.1007/s002030100281. "
                "Electron microscopy and biochemistry identified granules in "
                "Cyanothece ATCC 51142 during nitrogen-fixing growth on a "
                "12-hour light/12-hour dark cycle. Full text and figures were "
                "not accessible; timing is condition-specific, not a universal "
                "granule property. The separate PCC 6803 mutant observations "
                "do not establish a universal cyanophycinase requirement."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:43989",
            "taxon_label": "Crocosphaera subtropica ATCC 51142",
            "reference": ACCUMULATION,
            "note": (
                "Historical Cyanothece ATCC 51142: granules observed during "
                "nitrogen-fixing light/dark culture, not constitutively in every "
                "cell. NCBI directly confirms the current strain name, rank no "
                "rank, and BH68/BH68K synonym: "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=43989. "
                "The directly read scientific abstract of the original isolation "
                "paper, https://doi.org/10.1128/jb.175.5.1284-1292.1993, places "
                "BH68 in intertidal sands of the Texas Gulf coast. This is "
                "provenance support, not an independent cyanophycin assay."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "cyanophycin_synthesis_and_storage",
            "title": "CphA supplies polymer for cyanophycin storage granules",
            "scope_status": "MECHANISTIC",
            "description": (
                "A source-bounded synthesis, material-localization and nitrogen-"
                "storage sketch, not a claim that every inclusion shares one regulation."
            ),
            "scope_notes": (
                "Integrates PCC 6308 enzyme expression/purification with PCC 6803 "
                "cell biology. It is not one experiment or a strain-specific "
                "mechanism demonstrated in the ATCC 51142 canonical example. "
                "The sequence-family match establishes identity, not granule "
                "formation. No universal growth benefit, magnesium dependence "
                "in vivo, degradation enzyme, or granule-surface organizer is inferred."
            ),
            "nodes": [
                {
                    "node_id": "cyanophycin_synthetase_cpha",
                    "label": "cyanophycin synthetase CphA",
                    "node_type": "GENE_OR_PROTEIN",
                    "grounding": "InterPro:IPR011810",
                    "gene_symbols": ["cphA"],
                    "description": (
                        "Cyanophycin synthetase family, verified at the InterPro "
                        "authority; not an isolated ATP-grasp domain."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P56947",
                            "protein_label": "Cyanophycin synthetase",
                            "gene_symbol": "cphA",
                            "taxon_id": "NCBITaxon:113355",
                            "taxon_label": "Geminocystis herdmanii PCC 6308",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-10-08",
                            "entry_version": 91,
                            "sequence_version": 2,
                            "role": (
                                "PCC 6308 enzyme catalyzes cyanophycin synthesis; "
                                "functional expression and purification used "
                                "recombinant E. coli, not a natural E. coli phenotype."
                            ),
                            "evidence": [
                                {
                                    "reference": EXPRESSION,
                                    "snippet": (
                                        "The functionality of cphA was proven by "
                                        "heterologous expression of active enzyme and "
                                        "synthesis of cyanophycin in Escherichia coli"
                                    ),
                                    "notes": (
                                        "Aboulmagd et al. (2000), scientific abstract "
                                        "directly read in DOI-matched Europe PMC "
                                        "core metadata (PMID:11131019); full paper "
                                        "not inspected. UniProt REST P56947 links "
                                        "this paper and AF220099/AAF43647.2 to PCC "
                                        "6308; its entry version 91, sequence version "
                                        "2 and NCBITaxon:113355 were checked live. "
                                        "The paper's Synechocystis name is historical. "
                                        "The accession is not PCC 6803 or the "
                                        "heterologous expression host."
                                    ),
                                },
                            ],
                        },
                    ],
                },
                {
                    "node_id": "cyanophycin_synthesis",
                    "label": "cyanophycin synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Nonribosomal polymer synthesis from arginine and aspartate.",
                },
                {
                    "node_id": "cyanophycin_macromolecule",
                    "label": "cyanophycin macromolecule",
                    "node_type": "CHEMICAL",
                    "grounding": "CHEBI:65318",
                    "description": (
                        "Authority-verified aspartate-backbone, arginine-side-group "
                        "polymer; chemical identity is not the granule phenotype."
                    ),
                },
                {
                    "node_id": "cyanophycin_granule_trait",
                    "label": "cyanophycin granule",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                },
                {
                    "node_id": "temporary_nitrogen_storage",
                    "label": "temporary nitrogen storage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Retention of assimilated nitrogen for subsequent utilization.",
                },
            ],
            "edges": [
                {
                    "subject": "cyanophycin_synthetase_cpha",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "cyanophycin_synthesis",
                    "description": "Purified PCC 6308 CphA catalyzes polymer synthesis.",
                    "evidence": [
                        {
                            "reference": PURIFICATION,
                            "snippet": ENZYME_SNIPPET,
                            "notes": (
                                "Aboulmagd et al. (2001), scientific abstract: "
                                "the quoted relative clause describes the native "
                                "enzyme purified from recombinant E. coli. "
                                "Publisher full-text Methods and substrate/primer "
                                "Results were read, including Tables 2 and 3. "
                                "No actual figure images were inspected."
                            ),
                        },
                    ],
                },
                {
                    "subject": "cyanophycin_synthesis",
                    "predicate": "has output",
                    "predicate_id": "RO:0002234",
                    "object": "cyanophycin_macromolecule",
                    "description": "The assayed reaction incorporates amino acids into cyanophycin.",
                    "evidence": [
                        {
                            "reference": PURIFICATION,
                            "snippet": ENZYME_SNIPPET,
                            "notes": (
                                "Same abstract clause supports the product as well "
                                "as catalysis. Radiometric incorporation into "
                                "insoluble polymer is the assay readout. This does "
                                "not equate soluble synthesis or engineered "
                                "amino-acid variants with a cellular granule."
                            ),
                        },
                    ],
                },
                {
                    "subject": "cyanophycin_macromolecule",
                    "predicate": "located in",
                    "predicate_id": "biolink:located_in",
                    "object": "cyanophycin_granule_trait",
                    "description": "Accumulated cyanophycin forms the material of the inclusion.",
                    "evidence": [
                        {
                            "reference": CELL_BIOLOGY,
                            "snippet": (
                                "Cyanophycin accumulates in the form of opaque and "
                                "light-scattering granules in the cell"
                            ),
                            "notes": (
                                "Watzer and Forchhammer (2018), Introduction, "
                                "directly read in publisher HTML. Results report "
                                "microscopy and arginine-specific Sakaguchi "
                                "staining during nitrogen resuscitation in the "
                                "engineered PCC 6803 CphA-eGFP strain. Main text, "
                                "Methods and supplemental captions were read; "
                                "actual figure images were not inspected."
                            ),
                        },
                    ],
                },
                {
                    "subject": "cyanophycin_granule_trait",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "temporary_nitrogen_storage",
                    "description": "The inclusion retains cyanophycin as a temporary nitrogen reserve.",
                    "evidence": [
                        {
                            "reference": CELL_BIOLOGY,
                            "snippet": "cyanophycin can be used as a temporary nitrogen storage",
                            "notes": (
                                "Scientific abstract clause. PCC 6803 wild-type "
                                "versus cphA-deletion comparisons support "
                                "condition-dependent storage during fluctuating "
                                "or limiting nitrogen supply and light/dark cycles, "
                                "not a universal fitness advantage. Granule-loss "
                                "confirmation is reported as data not shown; "
                                "no complementation experiment is claimed."
                            ),
                        },
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "cyanophycin-granule-identity",
            "prompt": "Keep inclusion morphology distinct from polymer and sequence identity.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Uses intracellular inclusion traitmech:000066 like PHA and "
                "polyphosphate granules. CHEBI:65318 is a chemical grounding "
                "only; CphA activity and family membership are not equivalent "
                "traits. CGP names the polymer, not an exact granule synonym. "
                "No trait xrefs, exact synonyms or SSSOM equivalences are "
                "asserted. Do not require spherical shape, fixed size, "
                "constitutive occurrence, or an invariant amino-acid ratio."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "cyanophycin-granule-mechanism-scope",
            "prompt": "Resolve strain-specific assembly and degradation mechanisms separately.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The 2001 enzyme paper calls cyanophycin unique to cyanobacteria, "
                "but the 2018 primary paper also documents its distribution in "
                "heterotrophic bacteria; no cyanobacteria-only restriction is "
                "imposed. Soluble engineered polymers do not alone establish "
                "granules. The graph integrates distinct source taxa rather "
                "than transferring PCC 6308 CphA evidence to the ATCC 51142 "
                "example. PCC 6803 without a substrain designation does not "
                "establish the Kazusa-specific UniProt instance. Surface "
                "localization and magnesium effects in cell extracts do not "
                "prove a universal in-vivo assembly requirement."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_record(*, corrected: bool = True) -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cyanophycin granule with four primary references, bounded "
            "verbatim excerpts, a natural ATCC 51142 example and a five-node "
            "mechanistic graph. Verified PCC 6308 CphA protein/family and polymer "
            "identity separately from morphology. Ignored-and-hidden novelty "
            "and current-main/worktree/complete-open-PR reservation checks "
            "support 000673 and v549 block 1062600-1062699. Existing records unchanged."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    if corrected:
        record_curation_event(
            record, curator="codex", action="CORRECT_CURATION_PROVENANCE",
            changes=(
                "Corrected provenance for #1816 without rewriting the initial event: "
                "its 04:30:00Z timestamp was mistakenly set ahead of execution. "
                "The initial record was already written before the repository CREATE "
                "history timestamp 2026-10-08T04:28:08Z, an observed upper bound, "
                "not an exact reconstructed write time. This correction uses the "
                "directly observed UTC clock; biological content is unchanged."
            ),
            llm_assisted=True, timestamp=CORRECTION_TIMESTAMP,
        )
    return record


def proposal_tsv(record: dict) -> str:
    parent = PARENT_ROW.copy()
    parent[7] = "metpo_traitmech_2026_10"
    rows = [*HEADERS, parent, [
        METPO_ID, record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                  CELL_BIOLOGY, ACCUMULATION, EXPRESSION, PURIFICATION]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Intracellular storage inclusion, not a polymer identity or predicted cphA phenotype.",
        IDENTIFIER,
    ]]
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
    rows = list(csv.reader(io.StringIO(PARENT_PROPOSAL.read_text()), delimiter="\t"))
    matches = [row for row in rows[2:] if row and row[0] == PARENT_METPO_ID]
    if rows[:2] != HEADERS or matches != [PARENT_ROW]:
        raise SystemExit("Parent proposal differs from reviewed context")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists():
        existing = yaml.safe_load(TARGET.read_text())
        if existing not in (record, build_record(corrected=False)):
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
