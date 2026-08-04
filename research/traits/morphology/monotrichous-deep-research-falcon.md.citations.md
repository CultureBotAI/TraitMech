# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** monotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 10 nodes, 8 edges

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
**Generated:** 2026-08-04T09:08:31.747316

1. terashima2020assemblymechanismof pages 2-4
2. arroyoperez2024aconservedcellpole pages 1-2
3. arroyoperez2024aconservedcellpole pages 2-3
4. dornes2024polarconfinementof pages 1-2
5. zhang2020flhfregulatesthe pages 1-2
6. arroyoperez2024aconservedcellpole pages 14-15
7. dornes2024polarconfinementof pages 4-6
8. dornes2024polarconfinementof pages 2-4
9. terashima2020assemblymechanismof pages 4-6
10. terashima2020assemblymechanismof pages 1-2
11. dornes2024polarconfinementof pages 6-7
12. arroyoperez2024aconservedcellpole pages 12-14
13. 10.7554/eLife.93004
14. 10.1038/s41467-024-50274-4
15. 10.1128/JB.00236-20
16. which
17. 10.1111/mmi.14482
18. 10.1093/femsre/fuv034
19. 10.3390/biom9070279
20. https://doi.org/10.7554/eLife.93004
21. https://doi.org/10.1038/s41467-024-50274-4
22. https://doi.org/10.1128/JB.00236-20
23. https://doi.org/10.1111/mmi.14482
24. https://doi.org/10.1093/femsre/fuv034
25. https://doi.org/10.3390/biom9070279
26. https://doi.org/10.1128/jb.00236-20,
27. https://doi.org/10.7554/elife.93004.3,
28. https://doi.org/10.1038/s41467-024-50274-4,
29. https://doi.org/10.1111/mmi.14482,