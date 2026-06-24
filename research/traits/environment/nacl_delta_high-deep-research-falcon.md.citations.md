# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta high
- **METPO identifier:** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 3 nodes, 2 edges

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
**Generated:** 2026-06-17T23:13:49.438819

1. khanh2024metabolicpathwayengineering pages 1-2
2. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
3. oren2024novelinsightsinto pages 1-2
4. oren2024novelinsightsinto pages 4-5
5. xing2024thepolyextremophilenatranaerobius pages 1-2
6. ionescu2024extremefluctuationsin pages 1-2
7. jurdzinski2023largescalephylogenomicsof pages 1-1
8. rezaei2025innovativeapproachesin pages 7-8
9. zou2024metabolicengineeringof pages 1-2
10. xing2024thepolyextremophilenatranaerobius pages 6-7
11. xing2024thepolyextremophilenatranaerobius pages 19-21
12. xing2024thepolyextremophilenatranaerobius pages 14-17
13. liu2025plantgrowthpromotingrhizobacteria pages 1-2
14. li2025wholegenomeanalysisof pages 1-2
15. strakova2025strategiesofenvironmental pages 7-9
16. xing2024thepolyextremophilenatranaerobius pages 7-10
17. https://doi.org/10.1126/sciadv.adg2059
18. https://doi.org/10.3389/frmbi.2023.1329925
19. https://doi.org/10.1128/aem.00145-24
20. https://doi.org/10.1038/s44185-024-00050-w
21. https://doi.org/10.1038/s41559-024-02505-6
22. https://doi.org/10.1128/aem.01905-23
23. https://doi.org/10.1128/aem.01195-24
24. https://doi.org/10.1186/s12934-025-02817-7
25. https://doi.org/10.1186/s12870-025-06765-7
26. https://doi.org/10.3390/microorganisms13081781
27. https://doi.org/10.1128/aem.01195-24,
28. https://doi.org/10.1038/s41559-024-02505-6,
29. https://doi.org/10.1038/s44185-024-00050-w,
30. https://doi.org/10.1128/aem.00145-24,
31. https://doi.org/10.3389/frmbi.2023.1329925,
32. https://doi.org/10.1126/sciadv.adg2059,
33. https://doi.org/10.1186/s12934-025-02817-7,
34. https://doi.org/10.1128/aem.01905-23,
35. https://doi.org/10.1186/s12870-025-06765-7,
36. https://doi.org/10.3390/microorganisms13081781,
37. https://doi.org/10.3390/microorganisms13040761,