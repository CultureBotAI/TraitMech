# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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
**Generated:** 2026-08-04T06:34:58.082235

1. pacheco2023resolvingmetabolicinteraction pages 3-4
2. nicholls2023onthepotential pages 1-2
3. mock2015energyconservationassociated pages 1-5
4. go2024integrationofmetabolomics pages 3-4
5. zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3
6. lockyer2024secondaryionmass pages 22-24
7. seto2020howthermodynamicsilluminates pages 4-6
8. pacheco2023resolvingmetabolicinteraction pages 1-3
9. go2024integrationofmetabolomics pages 1-3
10. taha2023optimalevaluationof pages 24-28
11. taha2023optimalevaluationof pages 1-4
12. zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 3-4
13. lockyer2024secondaryionmass pages 1-5
14. FeFe
15. 10.3390/ijms252413421
16. 10.3389/fevo.2020.602809
17. 10.3389/fmicb.2023.1239189
18. 10.1101/2023.02.13.528271
19. 10.1128/JB.00399-15
20. 10.1016/j.mib.2023.102317
21. d
22. 10.1007/s00253-024-13384-z
23. 10.1016/j.crmeth.2022.100383
24. s
25. 10.1038/s43586-024-00311-9
26. https://doi.org/10.3390/ijms252413421
27. https://doi.org/10.3389/fevo.2020.602809
28. https://doi.org/10.3389/fmicb.2023.1239189
29. https://doi.org/10.1101/2023.02.13.528271
30. https://doi.org/10.1128/JB.00399-15
31. https://doi.org/10.1016/j.mib.2023.102317
32. https://doi.org/10.1007/s00253-024-13384-z
33. https://doi.org/10.1016/j.crmeth.2022.100383
34. https://doi.org/10.1038/s43586-024-00311-9
35. https://doi.org/10.3389/fevo.2020.602809,
36. https://doi.org/10.3389/fmicb.2023.1239189,
37. https://doi.org/10.1007/s00253-024-13384-z,
38. https://doi.org/10.1016/j.mib.2023.102317,
39. https://doi.org/10.3390/ijms252413421,
40. https://doi.org/10.1101/2023.02.13.528271,
41. https://doi.org/10.1128/jb.00399-15,
42. https://doi.org/10.1016/j.crmeth.2022.100383,
43. https://doi.org/10.1038/s43586-024-00311-9,