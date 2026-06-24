# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plant pathogen
- **METPO identifier:** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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
**Generated:** 2026-06-17T20:59:40.204280

1. kvitko2023discoveryofthe pages 1-2
2. carezzano2023biofilmformingabilityof pages 5-6
3. carezzano2023biofilmformingabilityof pages 9-11
4. carezzano2023biofilmformingabilityof pages 6-8
5. carter2024lectinsandpolysaccharide pages 1-2
6. hajjihedfi2024plantdiseasespathogenicity pages 2-4
7. dulal2024pathsofleast pages 1-2
8. liu2024aneffectoressential pages 1-2
9. fontana2023effectsofflavonoids pages 1-2
10. mulungu2024unmaskingthehidden pages 1-2
11. mulungu2024unmaskingthehidden pages 7-9
12. carezzano2023biofilmformingabilityof pages 8-9
13. wojtasik2024endophyticnonpathogenicfusarium pages 1-2
14. wojtasik2024endophyticnonpathogenicfusarium pages 2-3
15. liu2023crucialrolesof pages 15-17
16. santosbriones2024algorithmsforeffector pages 18-19
17. and
18. https://doi.org/10.1094/phyto-08-22-0292-kd
19. https://doi.org/10.3390/plants12112207
20. https://doi.org/10.21608/mb.2024.307263.1134
21. https://doi.org/10.1111/mpp.13322
22. https://doi.org/10.3389/fpls.2024.1342714
23. https://doi.org/10.1038/s41467-024-53725-0
24. https://doi.org/10.1094/mpmi-12-23-0212-cr
25. https://doi.org/10.3389/fpls.2024.1352105
26. https://doi.org/10.1371/journal.ppat.1012358
27. https://doi.org/10.3390/plants12071508
28. https://doi.org/10.62773/jcocs.v5i4.277
29. https://doi.org/10.21608/mb.2024.307263.1134,
30. https://doi.org/10.1094/phyto-08-22-0292-kd,
31. https://doi.org/10.3389/fpls.2024.1352105,
32. https://doi.org/10.3390/plants12112207,
33. https://doi.org/10.1371/journal.ppat.1012358,
34. https://doi.org/10.3389/fpls.2024.1342714,
35. https://doi.org/10.1094/mpmi-12-23-0212-cr,
36. https://doi.org/10.1038/s41467-024-53725-0,
37. https://doi.org/10.3390/plants12071508,
38. https://doi.org/10.3390/horticulturae9020250,
39. https://doi.org/10.3390/microbiolres15040145,
40. https://doi.org/10.62773/jcocs.v5i4.277,