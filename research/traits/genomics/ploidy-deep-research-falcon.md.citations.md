# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ploidy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000100
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the number of complete genome copies per cell; many bacteria and archaea are polyploid, maintaining many chromosome copies that support survival, repair, and large cell size.
- **Parent traits:** METPO:1000188
- **Synonyms:** polyploidy
- **Existing evidence:** DOI:10.1159/000368855:  (Soppa reviews polyploidy in archaea and bacteria and its links to desiccation resistance, giant cell size, and long-term survival.) | DOI:10.1073/pnas.0707522105:  (Mendell et al. document extreme polyploidy (tens of thousands of genome copies) in the large bacterium Epulopiscium.)
- **Existing causal graph summary:** ploidy_repair_survival: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **ploidy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/ploidy.yaml`.

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
**Generated:** 2026-08-04T05:24:06.655815

1. breuert2006regulatedpolyploidyin pages 1-2
2. bruck2023ploidyinvibrio pages 1-2
3. nagy2021comparisonofalternative pages 1-2
4. bruck2023oneadvantageof pages 1-2
5. misra2023effectivegenesilencing pages 1-2
6. maurya2019paraproteinsof pages 1-4
7. bruck2023oneadvantageof pages 6-8
8. maurya2021characterizationofori pages 1-2
9. slade2009recombinationandreplication pages 1-2
10. bruck2023oneadvantageof pages 10-13
11. bruck2023oneadvantageof pages 15-16
12. bruck2023oneadvantageof pages 2-3
13. maurya2021characterizationofori pages 9-10
14. 10.3390/microorganisms11092267
15. 10.1371/journal.pone.0000092
16. 10.3390/genes14071437
17. 10.26508/lsa.202000856
18. 10.1042/BCJ20180799
19. 10.1016/j.cell.2009.01.018
20. 10.1371/journal.pgen.1000552
21. 10.1186/s12934-021-01622-2
22. 10.1128/spectrum.05204-22
23. 10.1159/000368855
24. 10.1073/pnas.0707522105
25. https://doi.org/10.3390/microorganisms11092267
26. https://doi.org/10.1371/journal.pone.0000092
27. https://doi.org/10.3390/genes14071437
28. https://doi.org/10.26508/lsa.202000856
29. https://doi.org/10.1042/BCJ20180799
30. https://doi.org/10.1016/j.cell.2009.01.018
31. https://doi.org/10.1371/journal.pgen.1000552
32. https://doi.org/10.1186/s12934-021-01622-2
33. https://doi.org/10.1128/spectrum.05204-22
34. https://doi.org/10.1159/000368855
35. https://doi.org/10.1073/pnas.0707522105
36. https://doi.org/10.3390/genes14071437,
37. https://doi.org/10.3390/microorganisms11092267,
38. https://doi.org/10.1371/journal.pone.0000092,
39. https://doi.org/10.26508/lsa.202000856,
40. https://doi.org/10.1186/s12934-021-01622-2,
41. https://doi.org/10.1016/j.cell.2009.01.018,
42. https://doi.org/10.1371/journal.pgen.1000552,
43. https://doi.org/10.1128/spectrum.05204-22,
44. https://doi.org/10.1042/bcj20180799,