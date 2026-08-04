# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 20 nodes, 19 edges

## Research Objective

Research the microbial trait **motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motile.yaml`.

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
**Generated:** 2026-08-04T09:14:28.428741

1. charlesorszag2024adhesionpilusretraction pages 1-2
2. rosko2025cellularcoordinationunderpins pages 16-17
3. jin2024microbesinporous pages 14-18
4. wu2024torquespeedrelationshipof pages 1-2
5. botting2023flgvformsa pages 1-2
6. ribardo2024viscositydependentdeterminantsof pages 1-2
7. geiger2024abacterialsense pages 1-3
8. ohara2024surfacehydrophilicitypromotes pages 1-2
9. charlesorszag2023sulfolobusacidocaldariusadhesion pages 2-3
10. 10.1128/mbio.00745-24
11. 10.1371/journal.pone.0287514
12. 10.1128/mbio.02544-23
13. 10.1128/jb.00442-23
14. 10.1128/msphere.00390-24
15. 10.1111/mpp.70001
16. 10.1038/s41467-024-49101-7
17. 10.7554/eLife.99273.1
18. 10.1007/s12551-024-01185-7
19. 10.1038/s41579-021-00626-4
20. https://doi.org/10.1128/mbio.00745-24
21. https://doi.org/10.1371/journal.pone.0287514
22. https://doi.org/10.1128/mbio.02544-23
23. https://doi.org/10.1128/jb.00442-23
24. https://doi.org/10.1128/msphere.00390-24
25. https://doi.org/10.1111/mpp.70001
26. https://doi.org/10.1038/s41467-024-49101-7
27. https://doi.org/10.7554/eLife.99273.1
28. https://doi.org/10.1007/s12551-024-01185-7
29. https://doi.org/10.1038/s41579-021-00626-4
30. https://doi.org/10.1128/mbio.00745-24,
31. https://doi.org/10.1371/journal.pone.0287514,
32. https://doi.org/10.1128/msphere.00390-24,
33. https://doi.org/10.1128/jb.00442-23,
34. https://doi.org/10.1038/s41467-024-49101-7,
35. https://doi.org/10.1101/2024.02.06.579126,
36. https://doi.org/10.1007/s12551-024-01185-7,
37. https://doi.org/10.1128/mbio.02544-23,
38. https://doi.org/10.1111/mpp.70001,
39. https://doi.org/10.1101/2023.08.04.552066,