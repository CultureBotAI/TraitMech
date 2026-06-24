# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motile
- **METPO identifier:** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 6 nodes, 5 edges

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
**Generated:** 2026-06-18T08:43:47.255362

1. nakamura2024structureanddynamics pages 1-3
2. jin2024microbesinporous pages 14-18
3. johnson2024structuralbasisof pages 1-5
4. ribardo2024viscositydependentdeterminantsof pages 1-2
5. wu2024torquespeedrelationshipof pages 13-15
6. ohara2024surfacehydrophilicitypromotes pages 1-2
7. thunes2024glidingmotilityproteins pages 1-2
8. charlesorszag2024adhesionpilusretraction pages 1-2
9. sofer2024perturbednglycosylationof pages 1-2
10. ramoneda2024ecologicalrelevanceof pages 5-6
11. armitage2024microbialprimerthe pages 3-5
12. ramoneda2024ecologicalrelevanceof pages 1-2
13. armitage2024microbialprimerthe pages 5-6
14. liu2024counterclockwiserotationof pages 1-2
15. berry2024diversedomainarchitectures pages 3-6
16. berry2024diversedomainarchitectures pages 8-10
17. berry2024diversedomainarchitectures pages 6-8
18. yarrington2024thetypeiv pages 31-32
19. https://doi.org/10.3390/biom14121488
20. https://doi.org/10.1099/mic.0.001406
21. https://doi.org/10.1038/s41564-024-01630-z
22. https://doi.org/10.1128/mbio.00745-24
23. https://doi.org/10.1128/mbio.02544-23
24. https://doi.org/10.1128/mbio.00440-24
25. https://doi.org/10.1128/jb.00068-24
26. https://doi.org/10.1128/msphere.00390-24
27. https://doi.org/10.1038/s41467-024-49101-7
28. https://doi.org/10.1038/s41467-024-50277-1
29. https://doi.org/10.1093/ismejo/wrae067
30. https://doi.org/10.1128/spectrum.03464-23
31. https://doi.org/10.1007/s12551-024-01185-7
32. https://doi.org/10.1093/ismejo/wrae067,
33. https://doi.org/10.1128/jb.00068-24,
34. https://doi.org/10.1128/msphere.00390-24,
35. https://doi.org/10.1038/s41467-024-49101-7,
36. https://doi.org/10.3390/biom14121488,
37. https://doi.org/10.1038/s41564-024-01630-z,
38. https://doi.org/10.1007/s12551-024-01185-7,
39. https://doi.org/10.1128/mbio.02544-23,
40. https://doi.org/10.1128/mbio.00745-24,
41. https://doi.org/10.1128/spectrum.03464-23,
42. https://doi.org/10.1038/s41467-024-50277-1,
43. https://doi.org/10.1099/mic.0.001406,
44. https://doi.org/10.1371/journal.pbio.3002488,
45. https://doi.org/10.1128/mbio.00440-24,