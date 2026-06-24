# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately acidophilic
- **METPO identifier:** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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
**Generated:** 2026-06-17T23:50:18.761179

1. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
2. gonzalez2024acidophilicheterotrophsbasic pages 1-2
3. tonietti2024unveilingthebioleaching pages 2-4
4. li2023comammoxnitrospiraand pages 1-2
5. yao2023howmethanotrophsrespond pages 5-7
6. jones2023mechanismsofbioleaching pages 2-5
7. liu2023molecularmechanismof pages 9-12
8. dopson2023eurypsychrophilicacidophilesfrom pages 1-2
9. dopson2023eurypsychrophilicacidophilesfrom pages 2-4
10. jones2023mechanismsofbioleaching pages 1-2
11. jones2023mechanismsofbioleaching pages 6-11
12. adetunji2024unravelingthepotentials pages 4-6
13. tonietti2024unveilingthebioleaching pages 1-2
14. gonzalez2024acidophilicheterotrophsbasic pages 3-4
15. higher pH
16. https://doi.org/10.3389/fmicb.2023.1149903
17. https://doi.org/10.1128/aem.00047-23
18. https://doi.org/10.1111/1758-2229.70019
19. https://doi.org/10.3389/fmicb.2022.1034164
20. https://doi.org/10.3390/microorganisms12122407
21. https://doi.org/10.1042/ebc20220257
22. https://doi.org/10.3390/microorganisms11071733
23. https://doi.org/10.3389/fmicb.2024.1374800
24. https://doi.org/10.1101/2023.07.13.548807
25. https://doi.org/10.3389/fmicb.2023.1149903,
26. https://doi.org/10.1111/1758-2229.70019,
27. https://doi.org/10.3390/microorganisms12122407,
28. https://doi.org/10.3389/fmicb.2024.1374800,
29. https://doi.org/10.1042/ebc20220257,
30. https://doi.org/10.1128/aem.00047-23,
31. https://doi.org/10.1101/2023.07.13.548807,
32. https://doi.org/10.3389/fmicb.2022.1034164,
33. https://doi.org/10.3390/min14090861,