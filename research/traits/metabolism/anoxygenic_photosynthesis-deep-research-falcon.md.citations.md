# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anoxygenic photosynthesis
- **METPO identifier:** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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
**Generated:** 2026-06-18T04:33:11.404370

1. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
2. yurkov2025phenomenaldiversityof pages 1-3
3. niederman2024whatweare pages 1-2
4. nikeleit2024inhibitionofphototrophic pages 1-2
5. lyratzakis2024thesynergybetween pages 1-2
6. li2023globallydistributedmyxococcota pages 7-8
7. ogola2025thiocapsalutimaribacterand pages 18-20
8. nishihara2024illuminatingthecoevolution pages 1-2
9. ye2024comparativestudyof pages 4-6
10. kushkevych2024anoxygenicphotosynthesiswith pages 15-16
11. ye2024comparativestudyof pages 1-2
12. ye2024comparativestudyof pages 9-12
13. tsuji2024anoxygenicphototrophof pages 2-3
14. tsuji2024anoxygenicphototrophof pages 1-2
15. yurkov2025phenomenaldiversityof pages 12-14
16. kushkevych2024anoxygenicphotosynthesiswith pages 16-17
17. 4Fe–4S
18. 4Fe-4S
19. https://doi.org/10.3389/fmicb.2024.1417714
20. https://doi.org/10.1038/s41586-024-07180-y
21. https://doi.org/10.3390/biom14030311
22. https://doi.org/10.1007/s11120-024-01093-7
23. https://doi.org/10.1073/pnas.2322120121
24. https://doi.org/10.1038/s41561-024-01560-9
25. https://doi.org/10.1007/s00449-024-03024-1
26. https://doi.org/10.1038/s41467-023-42193-7
27. https://doi.org/10.3390/biology14050503
28. https://doi.org/10.3389/fmicb.2024.1417714,
29. https://doi.org/10.1073/pnas.2322120121,
30. https://doi.org/10.3390/microorganisms13112446,
31. https://doi.org/10.1038/s41586-024-07180-y,
32. https://doi.org/10.3390/biom14030311,
33. https://doi.org/10.1038/s41561-024-01560-9,
34. https://doi.org/10.1038/s41467-023-42193-7,
35. https://doi.org/10.1007/s11120-024-01093-7,
36. https://doi.org/10.3390/biology14050503,
37. https://doi.org/10.1007/s00449-024-03024-1,