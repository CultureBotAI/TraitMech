# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** monotrichous
- **METPO identifier:** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **monotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/monotrichous.yaml`.

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
**Generated:** 2026-06-18T08:38:07.848054

1. schuhmacher2015howbacteriamaintain pages 4-5
2. gibson2023controlofthe pages 1-2
3. botting2023flagellumassemblyanda pages 138-143
4. dornes2024polarconfinementof pages 1-2
5. dornes2024polarconfinementof pages 2-4
6. schuhmacher2015howbacteriamaintain pages 7-8
7. lozano2025regulatoryplasticityand pages 1-5
8. dornes2024polarconfinementof pages 4-6
9. dornes2024polarconfinementof pages 7-8
10. dornes2024polarconfinementof pages 6-7
11. https://doi.org/10.1128/jb.00110-23
12. https://doi.org/10.1038/s41467-024-50274-4
13. https://doi.org/10.1093/femsre/fuv034
14. https://doi.org/10.1101/2025.07.29.667523
15. https://doi.org/10.1093/femsre/fuv034,
16. https://doi.org/10.1128/jb.00110-23,
17. https://doi.org/10.1038/s41467-024-50274-4,
18. https://doi.org/10.1101/2025.07.29.667523,