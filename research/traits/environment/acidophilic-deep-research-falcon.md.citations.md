# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidophilic
- **METPO identifier:** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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
**Generated:** 2026-06-17T21:22:39.772401

1. dopson2023eurypsychrophilicacidophilesfrom pages 1-2
2. krulwich2011molecularaspectsof pages 3-5
3. xu2023transcriptomicandmetabolomic pages 1-2
4. krulwich2011molecularaspectsof pages 11-12
5. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
6. chong2024archaeamembranesin pages 1-2
7. li2023comammoxnitrospiraand pages 1-2
8. luo2024rolesandregulation pages 1-2
9. jia2024multiscaleandtransdisciplinary pages 1-2
10. tonietti2024unveilingthebioleaching pages 1-2
11. funari2023urbanminingof pages 20-22
12. cozma2024biorecoveryofmetals pages 10-11
13. cozma2024biorecoveryofmetals pages 19-20
14. https://doi.org/10.1038/nrmicro2549
15. https://doi.org/10.3389/fmicb.2023.1149903
16. https://doi.org/10.3389/fmicb.2023.1149903;
17. https://doi.org/10.1111/1758-2229.70019
18. https://doi.org/10.3389/frbis.2023.1338019
19. https://doi.org/10.1128/spectrum.00022-23
20. https://doi.org/10.1128/aem.00047-23
21. https://doi.org/10.3390/microorganisms12030422
22. https://doi.org/10.3390/microorganisms12122407
23. https://doi.org/10.3390/min14080808
24. https://doi.org/10.1007/s11356-023-26790-z
25. https://doi.org/10.3390/pr12091793
26. https://doi.org/10.3389/fmicb.2023.1149903,
27. https://doi.org/10.1038/nrmicro2549,
28. https://doi.org/10.1128/spectrum.00022-23,
29. https://doi.org/10.1111/1758-2229.70019,
30. https://doi.org/10.3389/frbis.2023.1338019,
31. https://doi.org/10.1128/aem.00047-23,
32. https://doi.org/10.3390/microorganisms12122407,
33. https://doi.org/10.3390/microorganisms12030422,
34. https://doi.org/10.3390/min14080808,
35. https://doi.org/10.1007/s11356-023-26790-z,
36. https://doi.org/10.3390/pr12091793,