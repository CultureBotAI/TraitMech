# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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
**Generated:** 2026-08-04T00:54:01.787366

1. andre2021theselectiveadvantage pages 2-4
2. mrnjavac2024theradicalimpact pages 15-17
3. gunsalus1994aerobicanaerobicgeneregulation pages 3-5
4. brown2022thearcabtwocomponent pages 3-4
5. brown2023conservedmetabolicregulator pages 1-3
6. brown2023conservedmetabolicregulator pages 12-14
7. brown2023conservedmetabolicregulator pages 8-10
8. price2021bacterialapproachesto pages 11-12
9. mrnjavac2024theradicalimpact pages 7-9
10. brown2022thearcabtwocomponent pages 20-23
11. andre2021theselectiveadvantage pages 7-8
12. 4Fe–4S
13. 2Fe–2S
14. 4Fe-4S
15. 2Fe-2S
16. https://doi.org/10.1002/1873-3468.14906
17. https://doi.org/10.1038/s41467-024-51029-x
18. https://doi.org/10.3390/ijms25021277
19. https://doi.org/10.3389/fbioe.2024.1339054
20. https://doi.org/10.1128/mbio.01448-23
21. https://doi.org/10.3390/inorganics11120450
22. https://doi.org/10.3390/ijms24065417
23. https://doi.org/10.1128/mmbr.00110-21
24. https://doi.org/10.1111/cmi.13338
25. https://doi.org/10.1111/mmi.14795
26. https://doi.org/10.1371/journal.pgen.1003839
27. https://doi.org/10.1016/0923-2508(94
28. https://doi.org/10.1073/pnas.94.12.6087
29. https://doi.org/10.1046/j.1365-2958.1997.4731841.x
30. https://doi.org/10.1016/S0005-2728(97
31. https://doi.org/10.1007/s00792-005-0479-7
32. https://doi.org/10.1111/cmi.13338,
33. https://doi.org/10.1002/1873-3468.14906,
34. https://doi.org/10.1128/mmbr.00110-21,
35. https://doi.org/10.1128/mbio.01448-23,
36. https://doi.org/10.1111/mmi.14795,