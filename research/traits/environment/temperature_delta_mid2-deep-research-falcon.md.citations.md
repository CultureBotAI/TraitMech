# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid2
- **METPO identifier:** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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
**Generated:** 2026-06-18T02:04:56.355198

1. yang2023insightintothe pages 1-2
2. sidarta2024lipidphaseseparation pages 14-16
3. safronova2023fromhotto pages 8-10
4. halamka2023productionofdiverse pages 5-6
5. chiu2023membranelipidand pages 5-6
6. sidarta2024lipidphaseseparation pages 1-2
7. moon2023temperaturemattersbacterial pages 9-10
8. chiu2023membranelipidand pages 7-9
9. yang2023insightintothe pages 10-12
10. chiu2023membranelipidand pages 14-15
11. lehmann2023adaptivelaboratoryevolution pages 1-2
12. maiti2024extrememakeoverthe pages 4-5
13. moon2023temperaturemattersbacterial pages 1-3
14. halamka2023productionofdiverse pages 1-2
15. chiu2023membranelipidand pages 13-14
16. halamka2023productionofdiverse pages 10-11
17. chiu2023membranelipidand pages 1-2
18. halamka2023productionofdiverse pages 8-9
19. safronova2023fromhotto pages 10-12
20. stonik2024structurediversityand pages 17-19
21. safronova2023fromhotto pages 1-3
22. chiu2023membranelipidand pages 15-16
23. lehmann2023adaptivelaboratoryevolution pages 6-7
24. https://doi.org/10.1128/spectrum.03925-23
25. https://doi.org/10.1007/s12275-023-00031-x
26. https://doi.org/10.1101/2023.11.10.566608
27. https://doi.org/10.1111/gbi.12525
28. https://doi.org/10.3389/fmicb.2023.1219779
29. https://doi.org/10.1128/aem.01928-22
30. https://doi.org/10.3389/fmicb.2023.1265216
31. https://doi.org/10.1039/d4cc03114h
32. https://doi.org/10.1007/s12275-023-00031-x,
33. https://doi.org/10.1128/aem.01928-22,
34. https://doi.org/10.1111/gbi.12525,
35. https://doi.org/10.1128/spectrum.03925-23,
36. https://doi.org/10.1039/d4cc03114h,
37. https://doi.org/10.1101/2023.11.10.566608,
38. https://doi.org/10.3389/fmicb.2023.1219779,
39. https://doi.org/10.3390/md23010003,
40. https://doi.org/10.3389/fmicb.2023.1265216,