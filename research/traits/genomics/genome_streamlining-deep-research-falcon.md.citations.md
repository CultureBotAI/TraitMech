# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genome streamlining
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000099
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing selective reduction of genome size and gene content in free-living microbes with very large effective population sizes, minimizing the cellular cost of replication and biosynthesis.
- **Parent traits:** METPO:1000188
- **Synonyms:** streamlined genome
- **Existing evidence:** DOI:10.1038/ismej.2014.60:  (Giovannoni et al. set out streamlining theory, explaining small streamlined genomes of abundant oligotrophic microbes.) | DOI:10.1038/nrmicro3331:  (Batut et al. compare reductive genome evolution at both ends of the bacterial population-size spectrum.)
- **Existing causal graph summary:** streamlining_oligotrophic_selection: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **genome streamlining** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genome_streamlining.yaml`.

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
**Generated:** 2026-08-04T05:05:52.280632

1. ramoneda2023taxonomicandenvironmental pages 1-2
2. giovannoni2014implicationsofstreamlining pages 4-6
3. morris2012theblackqueen pages 1-2
4. jackrel2023selectionforoligotrophy pages 1-2
5. dong2024ecoevolutionarystrategiesfor pages 1-2
6. giordano2024genomescalecommunitymodelling pages 1-2
7. giovannoni2014implicationsofstreamlining pages 1-2
8. chaudhari2024genomestreamliningin pages 1-2
9. giovannoni2014implicationsofstreamlining pages 3-4
10. giovannoni2014implicationsofstreamlining pages 2-3
11. wong2024ubiquitousgenomestreamlined pages 1-4
12. chaudhari2024genomestreamliningin pages 7-8
13. zhang2024genomereductionoccurred pages 10-14
14. sengupta2024genomestreamliningto pages 1-2
15. fan2024genomestreamliningof pages 1-2
16. giovannoni2014implicationsofstreamlining pages 11-12
17. giovannoni2014implicationsofstreamlining pages 7-8
18. giovannoni2014implicationsofstreamlining pages 8-9
19. 10.1038/ismej.2014.60
20. 10.1128/mbio.00036-12
21. 10.1101/2023.06.25.546417
22. 10.1186/s40793-024-00581-6
23. 10.1038/s41467-024-50368-z
24. 10.1038/s41467-024-46374-w
25. 10.1038/s41467-023-43435-4
26. 10.1128/mbio.01415-23
27. 10.21203/rs.3.rs-4258556/v1
28. 10.1128/mbio.03530-23
29. 10.1128/msystems.00845-24
30. 10.1146/annurev-marine-010814-015934
31. https://doi.org/10.1038/ismej.2014.60
32. https://doi.org/10.1128/mbio.00036-12
33. https://doi.org/10.1101/2023.06.25.546417
34. https://doi.org/10.1186/s40793-024-00581-6
35. https://doi.org/10.1038/s41467-024-50368-z
36. https://doi.org/10.1038/s41467-024-46374-w
37. https://doi.org/10.1038/s41467-023-43435-4
38. https://doi.org/10.1128/mbio.01415-23
39. https://doi.org/10.21203/rs.3.rs-4258556/v1
40. https://doi.org/10.1128/mbio.03530-23
41. https://doi.org/10.1128/msystems.00845-24
42. https://doi.org/10.1146/annurev-marine-010814-015934
43. https://doi.org/10.1038/ismej.2014.60,
44. https://doi.org/10.1128/mbio.00036-12,
45. https://doi.org/10.1038/s41467-023-43435-4,
46. https://doi.org/10.1128/mbio.03530-23,
47. https://doi.org/10.1128/msystems.00845-24,
48. https://doi.org/10.1186/s40793-024-00581-6,
49. https://doi.org/10.1128/mbio.01415-23,
50. https://doi.org/10.21203/rs.3.rs-4258556/v1,
51. https://doi.org/10.1038/s41467-024-46374-w,
52. https://doi.org/10.1146/annurev-marine-010814-015934,
53. https://doi.org/10.1038/s41467-024-50368-z,
54. https://doi.org/10.1101/2023.06.25.546417,