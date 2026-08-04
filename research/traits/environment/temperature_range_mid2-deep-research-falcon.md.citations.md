# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000451
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 27–30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 27–30 °C range as a typical mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid2_baseline_mesophile: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid2.yaml`.

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
**Generated:** 2026-08-04T04:30:37.524619

1. mendoza2014temperaturesensingby pages 5-6
2. mendoza2014temperaturesensingby pages 2-4
3. mendoza2014temperaturesensingby pages 4-5
4. dessenne2024lipidomicanalysesreveal pages 8-12
5. moon2023temperaturemattersbacterial pages 7-9
6. barbotin2026twotemperaturedependentmembrane pages 1-2
7. maiti2024extrememakeoverthe pages 4-5
8. wu2023molecularmechanismsof pages 3-5
9. moon2023temperaturemattersbacterial pages 10-11
10. moon2023temperaturemattersbacterial pages 11-12
11. moon2023temperaturemattersbacterial pages 13-14
12. moon2023temperaturemattersbacterial pages 12-13
13. wu2023molecularmechanismsof pages 16-17
14. 10.1007/s12275-023-00031-x
15. 10.3390/cells12101353
16. 10.1128/spectrum.00757-24
17. 10.1039/D4CC03114H
18. 10.1146/annurev-micro-091313-103612
19. 10.1128/msphere.00095-26
20. https://doi.org/10.1007/s12275-023-00031-x
21. https://doi.org/10.3390/cells12101353
22. https://doi.org/10.1128/spectrum.00757-24
23. https://doi.org/10.1039/D4CC03114H
24. https://doi.org/10.1146/annurev-micro-091313-103612
25. https://doi.org/10.1128/msphere.00095-26
26. https://doi.org/10.1146/annurev-micro-091313-103612,
27. https://doi.org/10.1007/s12275-023-00031-x,
28. https://doi.org/10.1128/spectrum.00757-24,
29. https://doi.org/10.1128/msphere.00095-26,
30. https://doi.org/10.3390/cells12101353,
31. https://doi.org/10.1039/d4cc03114h,