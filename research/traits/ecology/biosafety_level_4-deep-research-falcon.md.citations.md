# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 4
- **METPO identifier:** METPO:1001105
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses extreme risk of life-threatening disease through aerosol transmission with no available treatment.
- **Parent traits:** METPO:1001101
- **Synonyms:** 4
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the extreme virulence and absence of countermeasures characteristic of BSL-4 agents.)
- **Existing causal graph summary:** biosafety_level_4_extreme_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_4.yaml`.

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
**Generated:** 2026-06-17T20:16:29.762567

1. kaufer2020laboratorybiosafetymeasures pages 4-5
2. kaufer2020laboratorybiosafetymeasures pages 3-4
3. fauscotino2024nipahvirusa pages 1-3
4. fauscotino2024nipahvirusa pages 5-7
5. resnik2024biosafetybiosecurityand pages 13-16
6. resnik2024biosafetybiosecurityand pages 23-25
7. resnik2024biosafetybiosecurityand pages 1-3
8. gao2024frombiosafetyto pages 12-15
9. hassan2024nipahvirusdisease pages 1-4
10. gao2024frombiosafetyto pages 5-6
11. saha2024recentadvancesof pages 1-2
12. mendonca2024comparisonofbrazilian pages 7-8
13. gao2024frombiosafetyto pages 6-7
14. gao2024frombiosafetyto pages 3-5
15. mehnaz2024thecurrentpathogenicity pages 2-3
16. anish2024pandemicpotentialof pages 2-3
17. mehnaz2024thecurrentpathogenicity pages 1-2
18. fauscotino2024nipahvirusa pages 7-9
19. https://doi.org/10.3390/laboratories1030013
20. https://doi.org/10.1007/s40592-024-00204-3
21. https://doi.org/10.3390/v16020179
22. https://doi.org/10.1016/S1473-3099(23
23. https://doi.org/10.1101/2024.03.11.24304091
24. https://doi.org/10.1007/s12275-024-00168-3
25. https://doi.org/10.1089/apb.2023.0005
26. https://doi.org/10.1016/j.pathol.2020.09.006
27. https://doi.org/10.1016/j.pathol.2020.09.006,
28. https://doi.org/10.3390/laboratories1030013,
29. https://doi.org/10.3390/v16020179,
30. https://doi.org/10.1002/hsr2.70241,
31. https://doi.org/10.1371/journal.pgph.0003926,
32. https://doi.org/10.1016/s1473-3099(23
33. https://doi.org/10.1007/s40592-024-00204-3,
34. https://doi.org/10.1007/s12275-024-00168-3,
35. https://doi.org/10.1089/apb.2023.0005,