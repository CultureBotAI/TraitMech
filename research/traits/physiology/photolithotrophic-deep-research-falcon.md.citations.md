# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithotrophic
- **METPO identifier:** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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
**Generated:** 2026-06-18T12:29:36.788196

1. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
2. zhuang2024electrontransferin pages 6-8
3. nikeleit2024inhibitionofphototrophic pages 11-17
4. nishihara2024illuminatingthecoevolution pages 1-2
5. nikeleit2024inhibitionofphototrophic pages 9-11
6. zhuang2024electrontransferin pages 14-15
7. kushkevych2024anoxygenicphotosynthesiswith pages 16-17
8. kushkevych2024anoxygenicphotosynthesiswith pages 4-6
9. nishihara2024illuminatingthecoevolution pages 9-9
10. nikeleit2024inhibitionofphototrophic pages 17-17
11. CHEBI:25212, candidate
12. GO:0009773
13. label-only candidate
14. GO:0009765, candidate
15. ENVO:low light, candidate
16. CHEBI:16136
17. GO:0015979
18. NCBITaxon:label-only candidate
19. CHEBI:26806
20. CHEBI:label-only candidate
21. GO:0015977, candidate
22. CHEBI:16526
23. KEGG: M00173 candidate / label-only
24. KEGG:M00173 candidate / label-only
25. GO:0000103 candidate / EC:1.8.99.5 related
26. GO:0009522
27. GO:0009523
28. CHEBI:29033, candidate ferrous iron
29. METPO:label-only candidate
30. CHEBI:16480
31. GO:0019646 candidate / label-only
32. CHEBI:18420, CHEBI:17632 / label-only
33. ENVO:label-only candidate
34. https://doi.org/10.3389/fmicb.2024.1417714
35. https://doi.org/10.3390/life14050591
36. https://doi.org/10.1038/s41561-024-01560-9
37. https://doi.org/10.1038/s41579-024-01044-y
38. https://doi.org/10.1073/pnas.2322120121
39. https://doi.org/10.3389/fmicb.2024.1417714,
40. https://doi.org/10.3390/life14050591,
41. https://doi.org/10.1038/s41561-024-01560-9,
42. https://doi.org/10.1073/pnas.2322120121,