# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum low
- **METPO identifier:** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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
**Generated:** 2026-06-18T00:50:05.126694

1. chiu2023membranelipidand pages 15-16
2. chong2024archaeamembranesin pages 2-3
3. atasoy2024exploitationofmicrobial pages 10-11
4. gonzalez2024acidophilicheterotrophsbasic pages 1-2
5. gonzalez2024acidophilicheterotrophsbasic pages 2-3
6. krulwich2011molecularaspectsof pages 3-5
7. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
8. deng2023strategiesofchemolithoautotrophs pages 1-2
9. krulwich2011molecularaspectsof pages 11-12
10. krulwich2011molecularaspectsof pages 17-18
11. dopson2023eurypsychrophilicacidophilesfrom pages 2-4
12. krulwich2011molecularaspectsof pages 5-6
13. chiu2023membranelipidand pages 9-10
14. chong2024archaeamembranesin pages 3-4
15. chiu2023membranelipidand pages 1-2
16. chong2024archaeamembranesin pages 4-6
17. hwangbo2023acidophilicmethanotrophsoccurrence pages 1-2
18. dopson2023eurypsychrophilicacidophilesfrom pages 1-2
19. krulwich2011molecularaspectsof pages 14-15
20. chong2024archaeamembranesin pages 1-2
21. chiu2023membranelipidand pages 2-3
22. chiu2023membranelipidand pages 5-6
23. chiu2023membranelipidand pages 6-7
24. chong2024archaeamembranesin pages 7-7
25. krulwich2011molecularaspectsof pages 15-17
26. watkin2024editorialacidophilemicrobiology pages 1-2
27. s
28. https://doi.org/10.1038/nrmicro2549
29. https://doi.org/10.3389/fmicb.2023.1149903
30. https://doi.org/10.1111/1758-2229.70019
31. https://doi.org/10.3389/frbis.2023.1338019
32. https://doi.org/10.3389/fmicb.2023.1219779
33. https://doi.org/10.1186/s40168-023-01712-w
34. https://doi.org/10.1093/femsre/fuad062
35. https://doi.org/10.3389/fmicb.2024.1374800
36. https://doi.org/10.1111/1758-2229.13156
37. https://doi.org/10.3389/fmicb.2023.1149903,
38. https://doi.org/10.3389/fmicb.2024.1374800,
39. https://doi.org/10.1038/nrmicro2549,
40. https://doi.org/10.1111/1758-2229.70019,
41. https://doi.org/10.1111/1758-2229.13156,
42. https://doi.org/10.3389/fmicb.2023.1219779,
43. https://doi.org/10.3389/frbis.2023.1338019,
44. https://doi.org/10.1093/femsre/fuad062,
45. https://doi.org/10.1186/s40168-023-01712-w,
46. https://doi.org/10.3389/fmicb.2024.1454559,