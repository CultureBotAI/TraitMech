# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000034
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy to fix CO2, oxidizing water as the electron donor and releasing molecular oxygen. It uses two linked photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant chloroplasts).
- **Parent traits:** traitmech:000038
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a distinct, cyanobacterial innovation.)
- **Existing causal graph summary:** oxygenic_photosynthesis_water_splitting: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **oxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxygenic_photosynthesis.yaml`.

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
**Generated:** 2026-08-04T06:47:47.857556

1. shevela2023solarenergyconversion pages 1-2
2. tian2024photosystemia pages 1-2
3. shevela2023solarenergyconversion pages 4-5
4. milrad2024regulationofmicroalgal pages 1-3
5. moore2024functionalconsequencesof pages 1-2
6. moore2024functionalconsequencesof pages 13-15
7. shevela2023solarenergyconversion pages 9-10
8. moore2024functionalconsequencesof pages 7-9
9. moore2024functionalconsequencesof pages 12-13
10. moore2024functionalconsequencesof pages 18-20
11. 10.1007/s11120-022-00991-y
12. 10.3390/plants13152103
13. 10.3390/ijms25168767
14. 10.1128/jb.00454-23
15. 10.32615/ps.2023.021
16. 10.1016/j.tim.2006.09.001
17. 10.1146/annurev-earth-060313-054810
18. https://doi.org/10.1007/s11120-022-00991-y
19. https://doi.org/10.3390/plants13152103
20. https://doi.org/10.3390/ijms25168767
21. https://doi.org/10.1128/jb.00454-23
22. https://doi.org/10.32615/ps.2023.021
23. https://doi.org/10.1016/j.tim.2006.09.001
24. https://doi.org/10.1146/annurev-earth-060313-054810
25. https://doi.org/10.1007/s11120-022-00991-y,
26. https://doi.org/10.3390/ijms25168767,
27. https://doi.org/10.1128/jb.00454-23,
28. https://doi.org/10.3390/plants13152103,