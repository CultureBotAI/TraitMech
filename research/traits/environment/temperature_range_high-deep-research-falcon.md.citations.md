# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range high
- **METPO identifier:** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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
**Generated:** 2026-06-18T02:38:10.149730

1. valenzuela2024isolationofthermophilic pages 1-2
2. rekadwad2023extremophilesthespecies pages 2-4
3. takemata2024howdothermophiles pages 1-2
4. moon2023temperaturemattersbacterial pages 6-7
5. chong2024archaeamembranesin pages 1-2
6. deng2023strategiesofchemolithoautotrophs pages 1-2
7. lipscomb2023manipulatingfermentationpathways pages 1-2
8. burkhardt2024miningthermophilesfor pages 1-2
9. gallo2024theundeniablepotential pages 4-5
10. maiti2024extrememakeoverthe pages 2-3
11. grunberger2023uncoveringthetemporal pages 24-26
12. grunberger2023uncoveringthetemporal pages 19-21
13. lehmann2023adaptivelaboratoryevolution pages 1-2
14. gallo2024theundeniablepotential pages 1-3
15. valenzuela2024isolationofthermophilic pages 2-4
16. takemata2024howdothermophiles pages 2-3
17. grunberger2023uncoveringthetemporal pages 1-2
18. deng2023strategiesofchemolithoautotrophs pages 20-20
19. grunberger2023uncoveringthetemporal pages 23-24
20. moon2023temperaturemattersbacterial pages 1-3
21. gallo2024theundeniablepotential pages 9-11
22. https://doi.org/10.1264/jsme2.me23087
23. https://doi.org/10.3389/frbis.2023.1338019
24. https://doi.org/10.1039/d4cc03114h
25. https://doi.org/10.1007/s00253-024-13082-w
26. https://doi.org/10.3390/microorganisms12030473
27. https://doi.org/10.1007/s00792-023-01321-3
28. https://doi.org/10.3390/ijms25147685
29. https://doi.org/10.3389/fmicb.2023.1265216
30. https://doi.org/10.1007/s12275-023-00031-x
31. https://doi.org/10.1128/mbio.02174-23
32. https://doi.org/10.1186/s40168-023-01712-w
33. https://doi.org/10.1128/aem.00012-23
34. https://doi.org/10.1007/s13205-023-03733-6
35. https://doi.org/10.3389/fmicb.2023.1265216,
36. https://doi.org/10.1007/s00253-024-13082-w,
37. https://doi.org/10.3390/microorganisms12030473,
38. https://doi.org/10.1007/s13205-023-03733-6,
39. https://doi.org/10.3390/ijms25147685,
40. https://doi.org/10.1264/jsme2.me23087,
41. https://doi.org/10.1007/s12275-023-00031-x,
42. https://doi.org/10.3389/frbis.2023.1338019,
43. https://doi.org/10.1186/s40168-023-01712-w,
44. https://doi.org/10.1128/mbio.02174-23,
45. https://doi.org/10.1128/aem.00012-23,
46. https://doi.org/10.1007/s00792-023-01321-3,
47. https://doi.org/10.1039/d4cc03114h,