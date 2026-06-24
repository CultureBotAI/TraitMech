# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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
**Generated:** 2026-06-18T10:24:31.921188

1. warrell2024interspeciessurfactantsserve pages 1-2
2. pastora2024multiplepathwaysimpact pages 1-3
3. pastora2024multiplepathwaysimpact pages 5-7
4. pozo2024optimizedswarmingmotility pages 2-4
5. lin2023glabridinfunctionsas pages 1-2
6. lin2023glabridinfunctionsas pages 4-8
7. shi2023vibriosplendidusfur pages 7-9
8. shi2023vibriosplendidusfur pages 1-2
9. panich2024swashingmotilitya pages 13-15
10. panich2024swashingmotilitya pages 11-13
11. shi2023vibriosplendidusfur pages 5-7
12. shi2023vibriosplendidusfur pages 9-10
13. lin2023glabridinfunctionsas pages 2-4
14. biosurfactant
15. https://doi.org/10.1128/spectrum.00166-24
16. https://doi.org/10.1128/mbio.03322-23
17. https://doi.org/10.1063/5.0128140
18. https://doi.org/10.1128/jb.00281-24
19. https://doi.org/10.1016/j.mex.2024.102622
20. https://doi.org/10.3389/fvets.2023.1207831
21. https://doi.org/10.2147/idr.s417751
22. https://doi.org/10.3390/ijms24021707
23. https://doi.org/10.1101/2024.08.21.609010
24. https://doi.org/10.1063/5.0128140,
25. https://doi.org/10.1128/jb.00281-24,
26. https://doi.org/10.3390/ijms24021707,
27. https://doi.org/10.1101/2024.08.21.609010,
28. https://doi.org/10.1128/mbio.03322-23,
29. https://doi.org/10.1128/spectrum.00166-24,
30. https://doi.org/10.1016/j.mex.2024.102622,
31. https://doi.org/10.2147/idr.s417751,
32. https://doi.org/10.3389/fvets.2023.1207831,