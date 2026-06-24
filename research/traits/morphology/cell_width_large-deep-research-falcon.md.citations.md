# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width large
- **METPO identifier:** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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
**Generated:** 2026-06-18T07:20:42.480783

1. micelli2023aconservedzincbinding pages 1-2
2. cameron2024insightsintothe pages 1-3
3. kals2024antibioticschangethe pages 5-7
4. costa2024theroleof pages 1-2
5. shlosman2023allostericactivationof pages 1-2
6. ago2023relationshipbetweenthe pages 1-3
7. middlemiss2024molecularmotortugofwar pages 1-2
8. micelli2023aconservedzincbinding pages 6-7
9. fivenson2023arolefor pages 1-2
10. castanheira2023evidenceoftwo pages 1-2
11. castanheira2023evidenceoftwo pages 2-3
12. galinier2023recentadvancesin pages 1-3
13. middlemiss2024molecularmotortugofwar pages 6-7
14. lakey2023theroleof pages 1-2
15. shlosman2023allostericactivationof pages 7-8
16. fivenson2024coordinatedassemblyof pages 1-2
17. middlemiss2023moleculartugofwarregulatesa pages 100-103
18. middlemiss2023moleculartugofwarregulates pages 100-103
19. https://doi.org/10.1038/s41467-024-49785-x
20. https://doi.org/10.1038/s41467-023-39037-9
21. https://doi.org/10.1073/pnas.2215237120
22. https://doi.org/10.1073/pnas.2301987120
23. https://doi.org/10.1002/mbo3.1385
24. https://doi.org/10.1128/mbio.03235-23
25. https://doi.org/10.1038/s42003-023-05308-w
26. https://doi.org/10.3390/biom13050720
27. https://doi.org/10.1038/s41579-023-00942-x
28. https://doi.org/10.1016/j.mib.2024.102479
29. https://doi.org/10.1073/pnas.2215237120,
30. https://doi.org/10.1038/s41579-023-00942-x,
31. https://doi.org/10.1101/2024.08.27.609914,
32. https://doi.org/10.1128/mbio.03235-23,
33. https://doi.org/10.1038/s41467-023-39037-9,
34. https://doi.org/10.3390/biom13050720,
35. https://doi.org/10.1073/pnas.2301987120,
36. https://doi.org/10.1002/mbo3.1385,
37. https://doi.org/10.1038/s41467-024-49785-x,
38. https://doi.org/10.1038/s42003-023-05308-w,
39. https://doi.org/10.1128/mbio.00631-23,
40. https://doi.org/10.1016/j.mib.2024.102479,