# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plant pathogen
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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
**Generated:** 2026-08-03T23:43:47.719851

1. pfeilmeier2016bacterialpathogenesisof pages 7-8
2. leivamora2024uncoveringthemechanisms pages 4-5
3. santosbriones2024algorithmsforeffector pages 1-2
4. leivamora2024uncoveringthemechanisms pages 2-4
5. santosbriones2024algorithmsforeffector pages 2-4
6. leivamora2024uncoveringthemechanisms pages 23-25
7. 10.3390/microorganisms9061227
8. 10.3390/microbiolres15040145
9. 10.1128/iai.00500-23
10. 10.3390/jof10090635
11. 10.1111/mpp.12427
12. https://doi.org/10.3390/microorganisms9061227
13. https://doi.org/10.3390/microbiolres15040145
14. https://doi.org/10.1128/iai.00500-23
15. https://doi.org/10.3390/jof10090635
16. https://doi.org/10.1111/mpp.12427
17. https://doi.org/10.3390/microorganisms9061227,
18. https://doi.org/10.1111/mpp.12427,
19. https://doi.org/10.3390/microbiolres15040145,
20. https://doi.org/10.3390/jof10090635,
21. https://doi.org/10.1128/iai.00500-23,