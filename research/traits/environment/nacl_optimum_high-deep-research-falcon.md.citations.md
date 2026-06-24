# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum high
- **METPO identifier:** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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
**Generated:** 2026-06-17T23:16:45.441389

1. matarredona2024understandingthetolerance pages 1-2
2. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
3. bonnaud2024haloarchaeaaspromising pages 2-4
4. bonnaud2024haloarchaeaaspromising pages 1-2
5. aldaghistani2024microbialcommunitiesin pages 1-3
6. yu2024temporaldynamicsof pages 1-2
7. favreau2023molecularacclimationof pages 1-2
8. lee2018naclsaturatedbrinesare pages 15-17
9. xing2024thepolyextremophilenatranaerobius pages 1-2
10. oren2024novelinsightsinto pages 1-2
11. galisteo2023astepinto pages 1-2
12. cirachavez2019kineticsofhalophilic pages 1-3
13. cirachavez2019kineticsofhalophilic pages 3-6
14. bartha2022investigatingextremotolerantmicrobes pages 21-25
15. bartha2022investigatingextremotolerantmicrobes pages 139-143
16. bartha2022investigatingextremotolerantmicrobes pages 25-28
17. xing2024thepolyextremophilenatranaerobius pages 17-19
18. martinezespinosa2024halophilicarchaeaas pages 1-2
19. martinezespinosa2024halophilicarchaeaas pages 2-4
20. moopantakath2023bioactivemoleculesfrom pages 1-2
21. moopantakath2023bioactivemoleculesfrom pages 4-5
22. xing2024thepolyextremophilenatranaerobius pages 10-14
23. chen2020comparativegenomicsanalysis pages 11-12
24. reang2024extremozymesandcompatible pages 1-2
25. martinezespinosa2024halophilicarchaeaas pages 4-5
26. https://doi.org/10.1038/s41559-024-02505-6
27. https://doi.org/10.1038/s44185-024-00050-w
28. https://doi.org/10.1002/pro.5003
29. https://doi.org/10.3390/microorganisms12081738
30. https://doi.org/10.1007/s00253-024-13241-z
31. https://doi.org/10.1186/s12934-024-02358-5
32. https://doi.org/10.1128/aem.00145-24
33. https://doi.org/10.1111/1758-2229.70039
34. https://doi.org/10.3389/fmicb.2022.1075274
35. https://doi.org/10.3389/fmicb.2023.1113540
36. https://doi.org/10.1080/19420889.2024.2369782
37. https://doi.org/10.3389/fmicb.2020.00324
38. https://doi.org/10.1093/femsre/fuy026
39. https://doi.org/10.5772/intechopen.81100
40. https://doi.org/10.5772/intechopen.81100,
41. https://doi.org/10.3389/fmicb.2020.00324,
42. https://doi.org/10.1111/1758-2229.70039,
43. https://doi.org/10.1093/femsre/fuy026,
44. https://doi.org/10.1038/s41559-024-02505-6,
45. https://doi.org/10.1186/s12934-024-02358-5,
46. https://doi.org/10.1002/pro.5003,
47. https://doi.org/10.3390/microorganisms12081738,
48. https://doi.org/10.1128/aem.00145-24,
49. https://doi.org/10.1007/s00253-024-13241-z,
50. https://doi.org/10.3389/fmicb.2023.1113540,
51. https://doi.org/10.1080/19420889.2024.2369782,
52. https://doi.org/10.1038/s44185-024-00050-w,
53. https://doi.org/10.3389/fmicb.2022.1075274,
54. https://doi.org/10.1007/s00792-019-01150-3,
55. https://doi.org/10.1038/s41598-024-63581-z,
56. https://doi.org/10.3389/fmicb.2023.1192059,