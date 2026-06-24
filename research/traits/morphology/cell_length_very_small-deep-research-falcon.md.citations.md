# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length very small
- **METPO identifier:** METPO:1000883
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension is at most approximately 1.3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_<=1.3
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very small cell sizes to oligotrophic lifestyle and reduced cellular material requirements.)
- **Existing causal graph summary:** cell_length_very_small_streamlining: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_very_small.yaml`.

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
**Generated:** 2026-06-18T07:05:49.513321

1. props2019geneexpansionand pages 2-3
2. zhu2024shapingofmicrobial pages 7-8
3. grant2014phosphorusuptakekinetics pages 115-119
4. noell2023areductionof pages 8-10
5. page2022peptidoglycanhydrolasestheir pages 37-40
6. jackrel2023selectionforoligotrophy pages 6-9
7. zhang2024genomereductionoccurred pages 10-14
8. ranjit2020chlamydialmrebdirects pages 2-4
9. grant2014phosphorusuptakekinetics pages 111-115
10. ranjit2020chlamydialmrebdirects pages 7-10
11. ranjit2020chlamydialmrebdirects pages 1-2
12. zhao2017threedimensionalstructureof pages 7-9
13. ranjit2020chlamydialmrebdirects pages 4-7
14. ranjit2020chlamydialmrebdirects pages 11-12
15. zhu2024shapingofmicrobial pages 8-9
16. https://doi.org/10.1128/mSphereDirect.00011-19
17. https://doi.org/10.1038/s41467-024-48591-9
18. https://doi.org/10.1128/MMBR.00124-22
19. https://doi.org/10.1128/mBio.01415-23
20. https://doi.org/10.1128/mBio.03222-19
21. https://doi.org/10.1128/mmbr.00124-22
22. https://doi.org/10.1128/mbio.01415-23
23. https://doi.org/10.1101/2023.06.25.546417
24. https://doi.org/10.1128/aem.02807-16
25. https://doi.org/10.1128/mbio.03222-19
26. https://doi.org/10.1128/aem.02807-16,
27. https://doi.org/10.1128/mspheredirect.00011-19,
28. https://doi.org/10.1038/s41467-024-48591-9,
29. https://doi.org/10.1128/mmbr.00124-22,
30. https://doi.org/10.1128/mbio.03222-19,
31. https://doi.org/10.1128/mbio.01415-23,
32. https://doi.org/10.1101/2023.06.25.546417,