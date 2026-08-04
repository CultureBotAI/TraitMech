# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotaxis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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
**Generated:** 2026-08-04T11:10:35.854481

1. muok2024unpackingalternativefeatures pages 1-2
2. xu2023systematicmappingof pages 2-4
3. cassidy2023structureofthe pages 1-2
4. muok2024unpackingalternativefeatures pages 4-6
5. ugolini2024microfluidicapproachesin pages 1-2
6. armitage2024twistsandturns pages 6-8
7. xu2023systematicmappingof pages 1-2
8. uchida2022thechemoreceptorsensory pages 1-3
9. muok2024unpackingalternativefeatures pages 2-4
10. 10.1128/mbio.00793-23
11. 10.1146/annurev-micro-032421-110850
12. 10.1002/prot.26430
13. 10.1128/mbio.02099-23
14. 10.3389/fmicb.2024.1473099
15. 10.1039/D3LC00784G
16. 10.1099/mic.0.001432
17. 10.1128/jb.00278-22
18. 10.1038/nrm1524
19. 10.1038/nrmicro2505
20. https://doi.org/10.1128/mbio.00793-23
21. https://doi.org/10.1146/annurev-micro-032421-110850
22. https://doi.org/10.1002/prot.26430
23. https://doi.org/10.1128/mbio.02099-23
24. https://doi.org/10.3389/fmicb.2024.1473099
25. https://doi.org/10.1039/D3LC00784G
26. https://doi.org/10.1099/mic.0.001432
27. https://doi.org/10.1128/jb.00278-22
28. https://doi.org/10.1038/nrm1524
29. https://doi.org/10.1038/nrmicro2505
30. https://doi.org/10.1146/annurev-micro-032421-110850,
31. https://doi.org/10.1002/prot.26430,
32. https://doi.org/10.1128/mbio.02099-23,
33. https://doi.org/10.3389/fmicb.2024.1473099,
34. https://doi.org/10.1128/jb.00278-22,
35. https://doi.org/10.1128/mbio.00793-23,
36. https://doi.org/10.1039/d3lc00784g,
37. https://doi.org/10.1099/mic.0.001432,