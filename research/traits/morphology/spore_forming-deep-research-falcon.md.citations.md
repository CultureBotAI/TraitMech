# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spore forming
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.

**Provider:** falcon
**Generated:** 2026-08-04T10:06:09.552292

1. galperin2022conservationandevolution pages 18-20
2. nerber2024thesmallacidsoluble pages 1-2
3. setlow2023newthoughtson pages 1-2
4. nerber2024thesmallacidsoluble pages 27-28
5. cassona2024sporesofclostridioides pages 1-2
6. setlow2023newthoughtson pages 2-4
7. setlow2023newthoughtson pages 14-16
8. 10.1371/journal.ppat.1012507
9. 10.1128/mmbr.00080-22
10. 10.1038/s42003-024-06521-x
11. 10.1128/jb.00079-22
12. 10.3389/fmicb.2021.630573
13. https://doi.org/10.1371/journal.ppat.1012507
14. https://doi.org/10.1128/mmbr.00080-22
15. https://doi.org/10.1038/s42003-024-06521-x
16. https://doi.org/10.1128/jb.00079-22
17. https://doi.org/10.3389/fmicb.2021.630573
18. https://doi.org/10.1371/journal.ppat.1012507,
19. https://doi.org/10.1038/s42003-024-06521-x,
20. https://doi.org/10.1128/jb.00079-22,
21. https://doi.org/10.1128/mmbr.00080-22,