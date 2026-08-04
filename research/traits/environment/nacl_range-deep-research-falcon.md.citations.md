# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000334
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that bounds the minimum and maximum NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl concentrations supporting growth as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic-tolerance breadth as the basis of the NaCl-range phenotype.)
- **Existing causal graph summary:** nacl_range_tolerance_breadth: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range.yaml`.

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
**Generated:** 2026-08-04T01:57:03.770027

1. li2024integratedgenomicsand pages 1-2
2. oren2008microbiallifeat pages 2-4
3. oren2008microbiallifeat pages 10-11
4. rath2020managementofosmoprotectant pages 1-2
5. khanh2024metabolicpathwayengineering pages 1-2
6. khanh2024metabolicpathwayengineering pages 6-9
7. rath2020managementofosmoprotectant pages 12-14
8. xing2024thepolyextremophilenatranaerobius pages 6-7
9. li2024integratedgenomicsand pages 5-8
10. nguyen2023draftgenomesequencing pages 1-2
11. khanh2024metabolicpathwayengineering pages 15-17
12. park2023onlineomicsplatform pages 6-7
13. xing2024thepolyextremophilenatranaerobius pages 1-2
14. park2023onlineomicsplatform pages 1-2
15. nguyen2023draftgenomesequencing pages 4-5
16. xing2024thepolyextremophilenatranaerobius pages 10-14
17. 10.1128/aem.01195-24
18. 10.3389/fmicb.2020.00622
19. 10.1128/aem.00145-24
20. 10.3390/microorganisms12020285
21. 10.1177/11779322231171779
22. 10.1186/1746-1448-4-2
23. 10.1007/s13205-023-03833-3
24. 10.1093/femsre/fuy009
25. https://doi.org/10.1128/aem.01195-24
26. https://doi.org/10.3389/fmicb.2020.00622
27. https://doi.org/10.1128/aem.00145-24
28. https://doi.org/10.3390/microorganisms12020285
29. https://doi.org/10.1177/11779322231171779
30. https://doi.org/10.1186/1746-1448-4-2
31. https://doi.org/10.1007/s13205-023-03833-3
32. https://doi.org/10.1093/femsre/fuy009
33. https://doi.org/10.1128/aem.01195-24,
34. https://doi.org/10.1007/s13205-023-03833-3,
35. https://doi.org/10.1128/aem.00145-24,
36. https://doi.org/10.3390/microorganisms12020285,
37. https://doi.org/10.1186/1746-1448-4-2,
38. https://doi.org/10.3389/fmicb.2020.00622,
39. https://doi.org/10.1177/11779322231171779,