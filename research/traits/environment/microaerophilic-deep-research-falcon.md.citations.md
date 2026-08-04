# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** microaerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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
**Generated:** 2026-08-04T01:15:26.069168

1. ledermann2021howrhizobiaadapt pages 4-6
2. borisov2021bacterialoxidasesof pages 18-19
3. price2021bacterialapproachesto pages 4-6
4. borisov2021bacterialoxidasesof pages 1-2
5. benoit2020molecularhydrogenmetabolism pages 16-18
6. casado2024noveldruglikehsra pages 1-2
7. hu2024dualrnasequencing pages 1-2
8. huang2024noveltherapeuticregimens pages 1-2
9. maity2024mergingmultiomicswith pages 1-4
10. feng2024proteinqualitycontrol pages 1-4
11. alleman2023mechanismsforgenerating pages 7-9
12. mele2023oxidoreductasesandmetal pages 16-17
13. 10.1128/aem.00378-23
14. 10.1042/EBC20230012
15. 10.1128/msystems.00206-24
16. 10.3389/fmicb.2024.1418129
17. 10.3390/ijms251810175
18. 10.1101/2024.07.15.603561
19. 10.1111/mmi.14795
20. 10.1128/JB.00539-20
21. 10.1089/ars.2020.8039
22. 10.1128/MMBR.00092-19
23. https://www.ncbi.nlm.nih.gov/books/NBK154539/:
24. https://doi.org/10.1128/aem.00378-23
25. https://doi.org/10.1042/EBC20230012
26. https://doi.org/10.1128/msystems.00206-24
27. https://doi.org/10.3389/fmicb.2024.1418129
28. https://doi.org/10.3390/ijms251810175
29. https://doi.org/10.1101/2024.07.15.603561
30. https://doi.org/10.1111/mmi.14795
31. https://doi.org/10.1128/JB.00539-20
32. https://doi.org/10.1089/ars.2020.8039
33. https://doi.org/10.1128/MMBR.00092-19
34. https://doi.org/10.1111/mmi.14795,
35. https://doi.org/10.1128/jb.00539-20,
36. https://doi.org/10.1089/ars.2020.8039,
37. https://doi.org/10.1128/aem.00378-23,
38. https://doi.org/10.1128/mmbr.00092-19,
39. https://doi.org/10.3390/ijms251810175,
40. https://doi.org/10.1128/msystems.00206-24,
41. https://doi.org/10.3389/fmicb.2024.1418129,
42. https://doi.org/10.1101/2023.09.07.556692,
43. https://doi.org/10.1101/2024.07.15.603561,
44. https://doi.org/10.1042/ebc20230012,