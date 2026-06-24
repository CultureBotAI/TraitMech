# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** branched shaped
- **METPO identifier:** METPO:1000687
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms lateral branches from filamentous or hyphal cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** branced, branched
- **Existing evidence:** DOI:10.1016/j.mib.2012.10.012: Streptomyces grow by tip extension and through the initiation of new branches (Supports branched morphology as a Streptomyces hyphal growth phenotype.)
- **Existing causal graph summary:** branched_shaped_streptomyces_branching: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **branched shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/branched_shaped.yaml`.

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
**Generated:** 2026-06-18T06:38:50.122744

1. bhowmick2023osmoticstressresponses pages 1-2
2. schyck2024harnessingfungisignaling pages 2-3
3. cuesta2024discoveryandcharacterization pages 148-152
4. bhowmick2024cellshapeand pages 1-2
5. li2024contrastingeffectsof pages 9-10
6. zhong2025thestomatinlikeprotein pages 2-4
7. zhong2025thestomatinlikeprotein pages 1-2
8. yuan2024fgpfnparticipatesin pages 9-11
9. claessen2024thestomatinlikeprotein pages 7-9
10. zuriegat2024emergingrolesof pages 6-7
11. zuriegat2024emergingrolesof pages 23-24
12. cuesta2024discoveryandcharacterization pages 29-34
13. zhong2025thestomatinlikeprotein pages 4-5
14. zuriegat2024emergingrolesof pages 9-10
15. claessen2024thestomatinlikeprotein pages 20-27
16. DivIVA
17. https://doi.org/10.1128/mbio.01492-24
18. https://doi.org/10.1093/femsml/uqad020
19. https://doi.org/10.3390/jof10090614
20. https://doi.org/10.3389/fmicb.2024.1387643
21. https://doi.org/10.1002/gch2.202400104
22. https://doi.org/10.1371/journal.ppat.1012215
23. https://doi.org/10.1038/s41467-025-58093-x
24. https://doi.org/10.21203/rs.3.rs-3811693/v1
25. https://doi.org/10.1093/femsml/uqad020,
26. https://doi.org/10.1038/s41467-025-58093-x,
27. https://doi.org/10.1128/mbio.01492-24,
28. https://doi.org/10.21203/rs.3.rs-3811693/v1,
29. https://doi.org/10.1002/gch2.202400104,
30. https://doi.org/10.3390/jof10090614,
31. https://doi.org/10.3389/fmicb.2024.1387643,
32. https://doi.org/10.1371/journal.ppat.1012215,