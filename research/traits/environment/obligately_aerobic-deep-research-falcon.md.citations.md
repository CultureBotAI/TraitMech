# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately aerobic
- **METPO identifier:** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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
**Generated:** 2026-06-18T00:01:14.486581

1. ciemniecki2020thepotentialfor pages 1-2
2. andre2021theselectiveadvantage pages 2-4
3. khademian2021howmicrobesevolved pages 6-8
4. lu2021whenanaerobesencounter pages 3-4
5. mrnjavac2024theradicalimpact pages 33-36
6. khalfaouihassani2023theescherichiacoli pages 1-2
7. nastasi2024cyanideinsensitiveoxidase pages 2-3
8. nastasi2024cyanideinsensitiveoxidase pages 1-2
9. jones2023mechanismsofbioleaching pages 2-5
10. hu2024identificationofcomplex pages 1-3
11. khademian2021howmicrobesevolved pages 15-20
12. khalfaouihassani2023theescherichiacoli pages 21-22
13. nastasi2024cyanideinsensitiveoxidase pages 16-17
14. khalfaouihassani2023theescherichiacoli pages 2-3
15. mrnjavac2024theradicalimpact pages 10-12
16. mrnjavac2024theradicalimpact pages 7-9
17. lu2021whenanaerobesencounter pages 16-17
18. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
19. https://doi.org/10.1111/cmi.13338
20. https://doi.org/10.1128/JB.00797-19
21. https://doi.org/10.3390/antiox13030383
22. https://doi.org/10.1371/journal.pone.0293015
23. https://doi.org/10.1002/1873-3468.14906
24. https://doi.org/10.1016/j.tim.2020.10.001
25. https://doi.org/10.3389/fmicb.2024.1347466
26. https://doi.org/10.1042/ebc20220257
27. https://doi.org/10.1038/s41579-021-00583-y
28. https://doi.org/10.1128/jb.00797-19,
29. https://doi.org/10.1111/cmi.13338,
30. https://doi.org/10.1016/j.tim.2020.10.001,
31. https://doi.org/10.1038/s41579-021-00583-y,
32. https://doi.org/10.3390/antiox13030383,
33. https://doi.org/10.1002/1873-3468.14906,
34. https://doi.org/10.3389/fmicb.2024.1347466,
35. https://doi.org/10.1042/ebc20220257,
36. https://doi.org/10.1371/journal.pone.0293015,