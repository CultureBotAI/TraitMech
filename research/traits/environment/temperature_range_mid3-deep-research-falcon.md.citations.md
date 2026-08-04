# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid3.yaml`.

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
**Generated:** 2026-08-04T04:31:57.069327

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. liang2024interactionsbetweenchaperone pages 1-2
3. mendoza2014temperaturesensingby pages 1-2
4. mendoza2014temperaturesensingby pages 2-4
5. mendoza2014temperaturesensingby pages 5-6
6. dessenne2024lipidomicanalysesreveal pages 8-12
7. sato2024effectsofsmall pages 10-11
8. liang2024interactionsbetweenchaperone pages 16-17
9. mendoza2014temperaturesensingby pages 4-5
10. pollo2015insightsintothermoadaptation pages 7-11
11. dessenne2024lipidomicanalysesreveal pages 1-2
12. liang2024interactionsbetweenchaperone pages 8-10
13. liang2024interactionsbetweenchaperone pages 13-16
14. 10.1128/spectrum.00757-24
15. 10.3389/fmicb.2023.1265216
16. 10.1007/s00792-023-01326-y
17. 10.7717/peerj.17197
18. 10.1146/annurev-micro-091313-103612
19. 10.1139/cjm-2015-0073
20. https://doi.org/10.1128/spectrum.00757-24
21. https://doi.org/10.3389/fmicb.2023.1265216
22. https://doi.org/10.1007/s00792-023-01326-y
23. https://doi.org/10.7717/peerj.17197
24. https://doi.org/10.1146/annurev-micro-091313-103612
25. https://doi.org/10.1139/cjm-2015-0073
26. https://doi.org/10.3389/fmicb.2023.1265216,
27. https://doi.org/10.7717/peerj.17197,
28. https://doi.org/10.1007/s00792-023-01326-y,
29. https://doi.org/10.1146/annurev-micro-091313-103612,
30. https://doi.org/10.1128/spectrum.00757-24,
31. https://doi.org/10.1139/cjm-2015-0073,