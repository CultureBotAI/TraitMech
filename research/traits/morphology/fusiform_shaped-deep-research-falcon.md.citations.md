# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** fusiform shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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
**Generated:** 2026-08-04T08:36:49.797138

1. randich2015molecularmechanismsfor pages 7-9
2. bansil2023motilityofdifferent pages 1-2
3. egan2020regulationofpeptidoglycan pages 8-9
4. posch2012glycobiologyaspectsof pages 1-3
5. britton2024therespiratoryenzyme pages 5-7
6. veith2015tannerellaforsythiaouter pages 1-2
7. britton2024therespiratoryenzyme pages 2-5
8. britton2024therespiratoryenzyme pages 1-2
9. britton2024therespiratoryenzyme pages 10-12
10. uncertain; geometry-component mapping
11. uncertain final trait mapping
12. 10.1128/mbio.01751-23
13. 10.3390/microorganisms11030634
14. 10.1038/s41579-020-0366-3
15. 10.3389/fmicb.2015.00580
16. 10.1021/acs.jproteome.5b00878
17. 10.3390/biom2040467
18. 10.1111/j.1365-2958.2011.07698.x
19. https://doi.org/10.1128/mbio.01751-23
20. https://doi.org/10.3390/microorganisms11030634
21. https://doi.org/10.1038/s41579-020-0366-3
22. https://doi.org/10.3389/fmicb.2015.00580
23. https://doi.org/10.1021/acs.jproteome.5b00878
24. https://doi.org/10.3390/biom2040467
25. https://doi.org/10.1111/j.1365-2958.2011.07698.x
26. https://doi.org/10.3389/fmicb.2015.00580,
27. https://doi.org/10.1128/mbio.01751-23,
28. https://doi.org/10.3390/microorganisms11030634,
29. https://doi.org/10.3390/biom2040467,
30. https://doi.org/10.1021/acs.jproteome.5b00878,
31. https://doi.org/10.1038/s41579-020-0366-3,