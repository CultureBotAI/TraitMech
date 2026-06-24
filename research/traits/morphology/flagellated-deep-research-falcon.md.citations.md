# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellated
- **METPO identifier:** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **flagellated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellated.yaml`.

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
**Generated:** 2026-06-18T07:58:50.045207

1. minamino2023structureassemblyand pages 1-3
2. marvaud2024clostridioidesdifficileflagella pages 2-5
3. xiong2023lossofflagellarelated pages 1-2
4. nakamura2024structureanddynamics pages 1-3
5. nakamura2024structureanddynamics pages 6-8
6. minamino2023structureassemblyand pages 4-6
7. johnson2024structuralbasisof pages 1-5
8. halte2024flhefunctionsas pages 1-2
9. wu2024torquespeedrelationshipof pages 1-2
10. wu2024torquespeedrelationshipof pages 17-19
11. minamino2023structureassemblyand pages 3-4
12. kinosita2023flagellarpolymorphismdependentbacterial pages 7-8
13. minamino2023structureassemblyand pages 16-18
14. wu2024torquespeedrelationshipof pages 2-5
15. marvaud2024clostridioidesdifficileflagella pages 1-2
16. s
17. https://doi.org/10.1128/ecosalplus.esp-0011-2023
18. https://doi.org/10.1128/spectrum.04149-22
19. https://doi.org/10.3390/biom14121488
20. https://doi.org/10.1128/mbio.00745-24
21. https://doi.org/10.1038/s41564-024-01630-z
22. https://doi.org/10.3390/ijms25042202
23. https://doi.org/10.1038/s41467-024-53986-9
24. https://doi.org/10.1038/s41467-024-50278-0
25. https://doi.org/10.2142/biophysico.bppb-v20.0024
26. https://doi.org/10.1128/ecosalplus.esp-0011-2023,
27. https://doi.org/10.3390/ijms25042202,
28. https://doi.org/10.1128/spectrum.04149-22,
29. https://doi.org/10.3390/biom14121488,
30. https://doi.org/10.1038/s41564-024-01630-z,
31. https://doi.org/10.1128/mbio.00745-24,
32. https://doi.org/10.1038/s41467-024-50278-0,
33. https://doi.org/10.2142/biophysico.bppb-v20.0024,