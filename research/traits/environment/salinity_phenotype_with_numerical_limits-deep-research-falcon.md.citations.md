# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** salinity phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000532
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific salt concentration values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports quantitative salinity descriptors (optimum, range, delta) as the standard numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009: Hypersaline environments (Osmoadaptation review supports salinity as the physical axis underlying halophily classifications.)
- **Existing causal graph summary:** salinity_phenotype_numerical_axis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **salinity phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.

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
**Generated:** 2026-08-04T03:31:41.721813

1. lee2018naclsaturatedbrinesare pages 1-3
2. bialeckafornal2015therateof pages 1-2
3. dong2023improvedsalttolerance pages 1-2
4. khanh2024metabolicpathwayengineering pages 1-2
5. xamxidin2025metagenomicsassembledgenomesreveal pages 11-12
6. pricewhelan2013transcriptionalprofilingof pages 1-2
7. xing2024thepolyextremophilenatranaerobius pages 1-2
8. michel2022cellularadaptationof pages 2-2
9. herz2003rolesofnhaa pages 1-2
10. kraegeloh2005potassiumtransportin pages 1-2
11. acciarri2023redundantpotassiumtransporter pages 1-2
12. ionescu2024extremefluctuationsin pages 1-2
13. wu2024metagenomicinsightsinto pages 1-2
14. dindhoria2024metagenomicassembledgenomes pages 1-2
15. xing2024thepolyextremophilenatranaerobius pages 7-10
16. xing2024thepolyextremophilenatranaerobius pages 10-14
17. michel2022cellularadaptationof pages 2-3
18. xing2024thepolyextremophilenatranaerobius pages 23-24
19. matarredona2020theroleof pages 3-4
20. wu2024metagenomicinsightsinto pages 17-18
21. dindhoria2024metagenomicassembledgenomes pages 11-13
22. dindhoria2024metagenomicassembledgenomes pages 13-13
23. https://doi.org/10.1128/aem.00145-24.
24. https://doi.org/10.1128/aem.01195-24.
25. https://doi.org/10.1186/s40168-024-01817-w.
26. https://doi.org/10.1128/msystems.01050-23.
27. https://doi.org/10.3389/frmbi.2023.1329925.
28. https://doi.org/10.3389/fmicb.2023.1123081.
29. https://doi.org/10.3389/fmicb.2023.1117684.
30. https://doi.org/10.1111/1462-2920.15925.
31. https://doi.org/10.1093/femsre/fuy009.
32. https://doi.org/10.1093/femsre/fuy026.
33. https://doi.org/10.1128/JB.02175-14.
34. https://doi.org/10.1128/mBio.00407-13.
35. https://doi.org/10.1128/JB.187.3.1036-1043.2005.
36. https://doi.org/10.1128/JB.185.4.1236-1244.2003.
37. https://doi.org/10.1128/aem.00145-24,
38. https://doi.org/10.1093/femsre/fuy026,
39. https://doi.org/10.1128/jb.02175-14,
40. https://doi.org/10.1111/1462-2920.15925,
41. https://doi.org/10.3389/fmicb.2023.1123081,
42. https://doi.org/10.1128/aem.01195-24,
43. https://doi.org/10.1128/mbio.00407-13,
44. https://doi.org/10.3389/fmicb.2023.1117684,
45. https://doi.org/10.3390/biom10101390,
46. https://doi.org/10.1186/s40168-024-01817-w,
47. https://doi.org/10.1128/jb.187.3.1036-1043.2005,
48. https://doi.org/10.1128/jb.185.4.1236-1244.2003,
49. https://doi.org/10.3389/fmicb.2025.1550346,
50. https://doi.org/10.3389/frmbi.2023.1329925,
51. https://doi.org/10.1128/msystems.01050-23,