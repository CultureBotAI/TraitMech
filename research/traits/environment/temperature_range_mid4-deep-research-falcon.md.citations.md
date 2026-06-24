# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid4
- **METPO identifier:** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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
**Generated:** 2026-06-18T03:00:41.808279

1. ramon2023ageneraloverview pages 1-2
2. hua2024regulatorymechanismsof pages 1-3
3. hoogerland2024atemperaturesensitivemetabolic pages 1-2
4. mcguire2023wholegenomesequencinganalysis pages 1-2
5. berdejo2024evolutionarytradeoffbetween pages 1-2
6. hurtadobautista2024thermalplasticityand pages 16-17
7. perezmorales2024simultaneoussaccharificationand pages 2-4
8. hua2024regulatorymechanismsof pages 9-11
9. hoogerland2024atemperaturesensitivemetabolic pages 2-3
10. hoogerland2024atemperaturesensitivemetabolic pages 3-4
11. hoogerland2024atemperaturesensitivemetabolic pages 6-7
12. hoogerland2024atemperaturesensitivemetabolic pages 10-11
13. hurtadobautista2024thermalplasticityand pages 1-2
14. hoogerland2024atemperaturesensitivemetabolic pages 7-8
15. hoogerland2024atemperaturesensitivemetabolic pages 9-10
16. https://doi.org/10.1038/s41467-024-53677-5
17. https://doi.org/10.1186/s12864-023-09266-9
18. https://doi.org/10.1128/mbio.03105-23
19. https://doi.org/10.3390/biology13121088
20. https://doi.org/10.1186/s12934-024-02602-y
21. https://doi.org/10.1186/s13068-024-02579-1
22. https://doi.org/10.1007/s42770-023-01057-4
23. https://doi.org/10.1007/s42770-023-01057-4,
24. https://doi.org/10.1186/s12934-024-02602-y,
25. https://doi.org/10.1038/s41467-024-53677-5,
26. https://doi.org/10.1186/s12864-023-09266-9,
27. https://doi.org/10.1128/mbio.03105-23,
28. https://doi.org/10.3390/biology13121088,
29. https://doi.org/10.1186/s13068-024-02579-1,