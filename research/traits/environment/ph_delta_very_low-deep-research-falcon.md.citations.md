# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta very low
- **METPO identifier:** METPO:1000473
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a very narrow growth-supporting pH breadth of at most approximately 1 pH unit, characteristic of stenotopic pH-sensitive physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_<=1
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very narrow pH-tolerance breadths as the stenotopic / pH-sensitive phenotype.)
- **Existing causal graph summary:** ph_delta_very_low_stenotopic: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_very_low.yaml`.

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
**Generated:** 2026-06-18T00:30:28.988099

1. gubryrangin2024nichebreadthspecialization pages 1-2
2. krulwich2011molecularaspectsof pages 3-5
3. ramoneda2023buildingagenomebased pages 6-7
4. hernandez2023multidimensionalspecializationand pages 1-2
5. ramoneda2024leveraginggenomicinformation pages 1-2
6. krulwich2011molecularaspectsof pages 11-12
7. krulwich2011molecularaspectsof pages 27-28
8. ramoneda2023buildingagenomebased pages 3-5
9. krulwich2011molecularaspectsof pages 12-14
10. krulwich2011molecularaspectsof pages 5-6
11. ramoneda2023buildingagenomebased pages 1-1
12. ianutsevich2023theroleof pages 1-2
13. ianutsevich2023theroleof pages 4-5
14. ianutsevich2023theroleof pages 10-12
15. hernandez2023multidimensionalspecializationand pages 2-3
16. krulwich2011molecularaspectsof pages 15-17
17. ianutsevich2023theroleof pages 8-10
18. ramoneda2024leveraginggenomicinformation pages 4-6
19. ramoneda2024leveraginggenomicinformation pages 2-4
20. ramoneda2024leveraginggenomicinformation pages 6-7
21. label-only; ENVO term candidate
22. label-only
23. label-only; noted as context that pH effects can be habitat-dependent
24. label-only/TCDB family
25. label-only/UniProt taxon-specific
26. label-only; UniProt taxon-specific
27. label-only if no stable ID handy
28. label-only/CHEBI candidate
29. https://doi.org/10.1038/nrmicro2549
30. https://doi.org/10.1126/sciadv.adf8998
31. https://doi.org/10.3390/microorganisms11071733
32. https://doi.org/10.1093/ismejo/wrae195
33. https://doi.org/10.1038/s41559-023-02149-y
34. https://doi.org/10.1093/ismejo/wrae183
35. https://doi.org/10.1093/ismejo/wrae183,
36. https://doi.org/10.3390/microorganisms11071733,
37. https://doi.org/10.1126/sciadv.adf8998,
38. https://doi.org/10.1038/s41559-023-02149-y,
39. https://doi.org/10.1038/nrmicro2549,
40. https://doi.org/10.1093/ismejo/wrae195,