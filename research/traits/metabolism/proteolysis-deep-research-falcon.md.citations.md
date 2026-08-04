# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteolysis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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
**Generated:** 2026-08-04T06:59:27.402878

1. hughes2022peptidetransportin pages 1-3
2. kieliszek2021characteristicsofthe pages 2-4
3. harwood2022theinsand pages 14-15
4. harwood2022theinsand pages 13-14
5. tinta2023jellyfishdetritussupports pages 7-10
6. song2023microbialproteasesand pages 2-3
7. tinta2023jellyfishdetritussupports pages 1-2
8. ter2024areviewon pages 3-4
9. rao1998molecularandbiotechnological pages 1-2
10. harwood2022theinsand pages 15-16
11. kieliszek2021characteristicsofthe pages 11-13
12. 10.3389/fmicb.2023.1236368
13. 10.3390/molecules26071858
14. 10.1099/mic.0.001274
15. s
16. 10.1093/femsre/fuab046
17. is
18. 10.1186/s40168-023-01598-8
19. and
20. 10.1111/ijfs.16888
21. 10.1128/MMBR.62.3.597-635.1998
22. https://doi.org/10.3389/fmicb.2023.1236368
23. https://doi.org/10.3390/molecules26071858
24. https://doi.org/10.1099/mic.0.001274
25. https://doi.org/10.1093/femsre/fuab046
26. https://doi.org/10.1186/s40168-023-01598-8
27. https://doi.org/10.1111/ijfs.16888
28. https://doi.org/10.1128/MMBR.62.3.597-635.1998
29. https://doi.org/10.1093/femsre/fuab046,
30. https://doi.org/10.1128/mmbr.62.3.597-635.1998,
31. https://doi.org/10.1186/s40168-023-01598-8,
32. https://doi.org/10.3390/molecules26071858,
33. https://doi.org/10.3389/fmicb.2023.1236368,
34. https://doi.org/10.1099/mic.0.001274,
35. https://doi.org/10.1111/ijfs.16888,