# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Homoacetogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 21 nodes, 20 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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
**Generated:** 2026-08-04T06:24:16.374296

1. ragsdale2008enzymologyofthe pages 1-2
2. gencic2020diverseenergyconservingpathways pages 1-4
3. jiao2024cultivationofnovel pages 1-2
4. karekar2022homoacetogenstheirmetabolism pages 1-3
5. basen2023editorialacetogens pages 1-2
6. baum2024theenergyconvertinghydrogenase pages 1-2
7. westphal2018thernfcomplex pages 1-2
8. wiechmann2021energyconservationin pages 8-11
9. bourgade2024progressesandchallenges pages 1-2
10. serves
11. 10.1128/spectrum.03380-23
12. 10.3389/fmicb.2024.1476253
13. 10.1186/s40168-024-01836-7
14. 10.3389/fmicb.2023.1186930
15. 10.3390/microorganisms10020397
16. 10.3390/microorganisms9020258
17. 10.1128/JB.00233-20
18. 10.1128/JB.00357-18
19. 10.1196/annals.1419.015
20. 10.1016/j.tibtech.2019.05.008
21. 10.1016/j.bbapap.2008.08.012
22. https://doi.org/10.1128/spectrum.03380-23
23. https://doi.org/10.3389/fmicb.2024.1476253
24. https://doi.org/10.1186/s40168-024-01836-7
25. https://doi.org/10.3389/fmicb.2023.1186930
26. https://doi.org/10.3390/microorganisms10020397
27. https://doi.org/10.3390/microorganisms9020258
28. https://doi.org/10.1128/JB.00233-20
29. https://doi.org/10.1128/JB.00357-18
30. https://doi.org/10.1196/annals.1419.015
31. https://doi.org/10.1016/j.tibtech.2019.05.008
32. https://doi.org/10.1016/j.bbapap.2008.08.012
33. https://doi.org/10.3390/microorganisms10020397,
34. https://doi.org/10.1128/spectrum.03380-23,
35. https://doi.org/10.1196/annals.1419.015,
36. https://doi.org/10.1128/jb.00233-20,
37. https://doi.org/10.1186/s40168-024-01836-7,
38. https://doi.org/10.3389/fmicb.2023.1186930,
39. https://doi.org/10.1128/jb.00357-18,
40. https://doi.org/10.3390/microorganisms9020258,
41. https://doi.org/10.3389/fmicb.2024.1476253,