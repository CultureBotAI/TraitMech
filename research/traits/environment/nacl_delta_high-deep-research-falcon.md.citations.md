# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_high.yaml`.

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
**Generated:** 2026-08-04T01:34:03.385367

1. xing2024thepolyextremophilenatranaerobius pages 1-2
2. xing2024thepolyextremophilenatranaerobius pages 14-17
3. hobmeier2022adaptationtovarying pages 1-2
4. zajc2014osmoadaptationstrategyof pages 1-2
5. hobmeier2022adaptationtovarying pages 14-16
6. zeaiter2019phenomicsandgenomics pages 1-2
7. lee2022accumulationpatternsof pages 1-2
8. dogan2023profilingthegenes pages 1-3
9. dindhoria2024metagenomicassembledgenomes pages 1-2
10. oren2008microbiallifeat pages 1-2
11. jimenezgomez2022survivinginthe pages 8-9
12. jimenezgomez2022survivinginthe pages 1-2
13. oren2008microbiallifeat pages 10-11
14. 10.1128/aem.00145-24
15. 10.1186/1746-1448-4-2
16. 10.3389/fmicb.2022.846677
17. 10.1128/AEM.02702-13
18. 10.3389/fmicb.2022.840408
19. 10.3389/fmicb.2019.01304
20. 10.3389/fmicb.2022.960621
21. 10.1128/msystems.01050-23
22. 10.53447/communc.1206230
23. https://doi.org/10.1128/aem.00145-24
24. https://doi.org/10.1186/1746-1448-4-2
25. https://doi.org/10.3389/fmicb.2022.846677
26. https://doi.org/10.1128/AEM.02702-13
27. https://doi.org/10.3389/fmicb.2022.840408
28. https://doi.org/10.3389/fmicb.2019.01304
29. https://doi.org/10.3389/fmicb.2022.960621
30. https://doi.org/10.1128/msystems.01050-23
31. https://doi.org/10.53447/communc.1206230
32. https://doi.org/10.1128/aem.02702-13,
33. https://doi.org/10.3389/fmicb.2022.840408,
34. https://doi.org/10.1186/1746-1448-4-2,
35. https://doi.org/10.1128/aem.00145-24,
36. https://doi.org/10.3389/fmicb.2022.846677,
37. https://doi.org/10.3389/fmicb.2019.01304,
38. https://doi.org/10.3389/fmicb.2022.960621,
39. https://doi.org/10.53447/communc.1206230,
40. https://doi.org/10.1128/msystems.01050-23,