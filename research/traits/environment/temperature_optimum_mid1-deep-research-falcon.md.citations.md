# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000443
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 22 and 27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate-temperature optima matched by homoviscous lipid composition as the mesophile setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid1_lower_mesophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid1.yaml`.

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
**Generated:** 2026-08-04T03:59:16.918259

1. lehmann2023adaptivelaboratoryevolution pages 3-4
2. mairet2021optimalproteomeallocation pages 1-2
3. lehmann2023adaptivelaboratoryevolution pages 6-7
4. hoogerland2024atemperaturesensitivemetabolic pages 3-4
5. gohrbandt2022lowmembranefluidity pages 1-2
6. mendoza2014temperaturesensingby pages 1-2
7. hoogerland2024atemperaturesensitivemetabolic pages 5-6
8. lehmann2023adaptivelaboratoryevolution pages 1-2
9. gohrbandt2022lowmembranefluidity pages 10-11
10. gohrbandt2022lowmembranefluidity pages 12-14
11. dessenne2024lipidomicanalysesreveal pages 1-2
12. dessenne2024lipidomicanalysesreveal pages 2-4
13. hoogerland2024atemperaturesensitivemetabolic pages 1-2
14. hoogerland2024atemperaturesensitivemetabolic pages 6-7
15. s
16. 10.1038/s41467-024-53677-5
17. 10.1128/spectrum.00757-24
18. 10.3389/fmicb.2023.1265216
19. 10.15252/embj.2021109800
20. 10.1038/s41540-021-00172-y
21. 10.1146/annurev-micro-091313-103612
22. https://doi.org/10.1038/s41467-024-53677-5
23. https://doi.org/10.1128/spectrum.00757-24
24. https://doi.org/10.3389/fmicb.2023.1265216
25. https://doi.org/10.15252/embj.2021109800
26. https://doi.org/10.1038/s41540-021-00172-y
27. https://doi.org/10.1146/annurev-micro-091313-103612
28. https://doi.org/10.1038/s41467-024-53677-5,
29. https://doi.org/10.3389/fmicb.2023.1265216,
30. https://doi.org/10.1146/annurev-micro-091313-103612,
31. https://doi.org/10.15252/embj.2021109800,
32. https://doi.org/10.1038/s41540-021-00172-y,
33. https://doi.org/10.1128/spectrum.00757-24,