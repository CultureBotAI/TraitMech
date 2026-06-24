# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length medium
- **METPO identifier:** METPO:1000885
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 2 and 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_2_3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports medium cell length as a typical outcome at moderate growth rates.)
- **Existing causal graph summary:** cell_length_medium_growth_rate: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_medium.yaml`.

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
**Generated:** 2026-06-18T06:56:26.937825

1. castanheira2023evidenceoftwo pages 1-2
2. ago2023relationshipbetweenthe pages 1-3
3. lakey2023theroleof pages 16-18
4. lakey2023theroleof pages 1-2
5. costa2024theroleof pages 1-2
6. lakey2023theroleof pages 2-4
7. willdigg2023adecreasein pages 1-3
8. jain2023understandingelongasomeunit pages 2-4
9. willdigg2023adecreasein pages 9-12
10. https://doi.org/10.1128/mbio.00631-23
11. https://doi.org/10.1002/mbo3.1385
12. https://doi.org/10.1038/s42003-023-05308-w
13. https://doi.org/10.1111/mmi.15323
14. https://doi.org/10.1128/mbio.00475-23
15. https://doi.org/10.1128/mbio.03235-23
16. https://doi.org/10.1128/mbio.00631-23,
17. https://doi.org/10.1038/s42003-023-05308-w,
18. https://doi.org/10.1002/mbo3.1385,
19. https://doi.org/10.1111/mmi.15323,
20. https://doi.org/10.1128/mbio.03235-23,
21. https://doi.org/10.1128/mbio.00475-23,
22. https://doi.org/10.33696/signaling.4.101,