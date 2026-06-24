# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteorhodopsin phototrophy
- **METPO identifier:** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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
**Generated:** 2026-06-18T06:01:30.906554

1. zambrano2024enlightenedbymicrobial pages 1-4
2. oh2024effectoflight pages 13-14
3. delgadillonuno2024coastalupwellingsystems pages 7-9
4. oh2024effectoflight pages 1-2
5. lee2024effectsoflight pages 1-2
6. hirschi2024structuralinsightsinto pages 8-9
7. hasegawatakano2024cyanorhodopsiniirepresentsa pages 9-10
8. hirschi2024structuralinsightsinto pages 5-6
9. mao2024molecularmechanismsand pages 1-2
10. delgadillonuno2024coastalupwellingsystems pages 13-14
11. mao2024molecularmechanismsand pages 2-3
12. hirschi2024structuralinsightsinto pages 1-2
13. tu2024engineeringrhodopsinbasedartificial pages 102-105
14. hirschi2024structuralinsightsinto pages 6-8
15. oh2024effectoflight pages 2-3
16. zambrano2024enlightenedbymicrobial pages 4-4
17. https://doi.org/10.4014/jmb.2410.10034
18. https://doi.org/10.1007/s12275-024-00125-0
19. https://doi.org/10.1126/sciadv.adj0384
20. https://doi.org/10.1038/s41467-024-50960-3
21. https://doi.org/10.34133/2022/9782712
22. https://doi.org/10.3389/fmars.2023.1259783
23. https://doi.org/10.5287/ora-8jgz2nrvd
24. https://doi.org/10.4014/jmb.2410.10034,
25. https://doi.org/10.3389/fmars.2023.1259783,
26. https://doi.org/10.1007/s12275-024-00125-0,
27. https://doi.org/10.1038/s41467-024-50960-3,
28. https://doi.org/10.34133/2022/9782712,
29. https://doi.org/10.1093/ismejo/wrae175,
30. https://doi.org/10.1126/sciadv.adj0384,