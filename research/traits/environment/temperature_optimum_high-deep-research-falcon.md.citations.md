# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum high
- **METPO identifier:** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_high.yaml`.

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
**Generated:** 2026-06-18T02:10:08.474972

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. arfah2024systematicreviewon pages 3-5
3. baes2023transcriptionalandtranslational pages 1-2
4. takemata2024howdothermophiles pages 2-3
5. takemata2024howdothermophiles pages 4-5
6. grunberger2023uncoveringthetemporal pages 1-2
7. lehmann2023adaptivelaboratoryevolution pages 6-7
8. mondal2024aquificaeovercomescompetition pages 1-2
9. takemata2024howdothermophiles pages 1-2
10. gallo2024theundeniablepotential pages 4-5
11. baes2023transcriptionalandtranslational pages 21-21
12. arfah2024systematicreviewon pages 1-3
13. gallo2024theundeniablepotential pages 8-9
14. gallo2024theundeniablepotential pages 11-12
15. ACP
16. label
17. broad label not exact
18. family-level
19. acyl-carrier-protein
20. https://doi.org/10.1264/jsme2.me23087
21. https://doi.org/10.1264/jsme2.me23087;
22. https://doi.org/10.1128/mbio.03593-22
23. https://doi.org/10.3389/fmicb.2023.1265216
24. https://doi.org/10.1128/mbio.02174-23;
25. https://doi.org/10.1371/journal.pone.0310595
26. https://doi.org/10.1128/mbio.03593-22;
27. https://doi.org/10.1128/mbio.02174-23
28. https://doi.org/10.1007/s00253-024-13082-w
29. https://doi.org/10.33640/2405-609x.3367
30. https://doi.org/10.3390/ijms25147685
31. https://doi.org/10.3389/fmicb.2023.1265216,
32. https://doi.org/10.33640/2405-609x.3367,
33. https://doi.org/10.1128/mbio.02174-23,
34. https://doi.org/10.1128/mbio.03593-22,
35. https://doi.org/10.1264/jsme2.me23087,
36. https://doi.org/10.1371/journal.pone.0310595,
37. https://doi.org/10.1007/s00253-024-13082-w,
38. https://doi.org/10.3390/ijms25147685,