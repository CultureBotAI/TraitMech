# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gliding
- **METPO identifier:** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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
**Generated:** 2026-06-18T08:19:53.445030

1. vincent2022dynamicprotondependentmotors pages 1-2
2. lauber2024structuralinsightsinto pages 1-2
3. islam2023unmaskingofthe pages 1-2
4. shibata2023filamentousstructuresin pages 1-2
5. paillat2023ajourneywith pages 1-3
6. attia2024amolecularswitch pages 1-1
7. thunes2024glidingmotilityproteins pages 2-5
8. lauber2024structuralinsightsinto pages 5-6
9. lauber2024structuralinsightsinto pages 2-3
10. jolivet2023integrinlikeadhesincgld pages 1-3
11. attia2024amolecularswitch pages 1-3
12. shibata2023filamentousstructuresin pages 5-6
13. islam2023unmaskingofthe pages 3-5
14. thunes2024glidingmotilityproteins pages 1-2
15. https://doi.org/10.1038/s42003-023-04472-3
16. https://doi.org/10.1038/s41564-024-01644-7
17. https://doi.org/10.1126/sciadv.adn2789
18. https://doi.org/10.1128/jb.00068-24
19. https://doi.org/10.1021/acsomega.3c05155
20. https://doi.org/10.1099/mic.0.001320
21. https://doi.org/10.1126/sciadv.abq0619
22. https://doi.org/10.1371/journal.pbio.3001443
23. https://doi.org/10.1371/journal.pbio.3001443,
24. https://doi.org/10.1038/s42003-023-04472-3,
25. https://doi.org/10.1126/sciadv.abq0619,
26. https://doi.org/10.1099/mic.0.001320,
27. https://doi.org/10.1038/s41564-024-01644-7,
28. https://doi.org/10.1126/sciadv.adn2789,
29. https://doi.org/10.1101/2023.10.19.562135,
30. https://doi.org/10.1128/jb.00068-24,
31. https://doi.org/10.1021/acsomega.3c05155,