# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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
**Generated:** 2026-08-04T09:22:28.315695

1. haiko2013theroleof pages 5-7
2. warrell2024interspeciessurfactantsservea pages 5-7
3. wu2020reciprocalcdigmpsignaling pages 11-13
4. laganenka2020flagellummediatedmechanosensingand pages 4-5
5. wu2020reciprocalcdigmpsignaling pages 6-8
6. han2023flagellarbrakeprotein pages 1-2
7. ribardo2024viscositydependentdeterminantsof pages 4-6
8. ribardo2024viscositydependentdeterminantsof pages 1-2
9. warrell2024interspeciessurfactantsservea pages 1-2
10. guan2024flhfaffectsthe pages 1-2
11. guan2024flhfaffectsthe pages 2-6
12. laganenka2020flagellummediatedmechanosensingand pages 2-4
13. kato2024molecularmechanismof pages 5-6
14. kato2024molecularmechanismof pages 1-2
15. kato2024molecularmechanismof pages 3-4
16. croze2011migrationofchemotactic pages 5-8
17. croze2011migrationofchemotactic pages 1-5
18. laganenka2020flagellummediatedmechanosensingand pages 5-6
19. …
20. https://doi.org/10.1128/aem.01548-23.
21. https://doi.org/10.1038/s42003-024-07104-6.
22. https://doi.org/10.1128/jb.00281-24.
23. https://doi.org/10.1128/mbio.02544-23.
24. https://doi.org/10.3389/fmicb.2023.1159974.
25. https://doi.org/10.1128/mbio.02269-19.
26. https://doi.org/10.1371/journal.pgen.1008703.
27. https://doi.org/10.1111/j.1365-2958.2010.07179.x.
28. https://doi.org/10.3390/biology2041242.
29. https://doi.org/10.1016/j.bpj.2011.06.023.
30. https://doi.org/10.1128/aem.01548-23,
31. https://doi.org/10.1128/jb.00281-24,
32. https://doi.org/10.3390/biology2041242,
33. https://doi.org/10.1371/journal.pgen.1008703,
34. https://doi.org/10.3389/fmicb.2023.1159974,
35. https://doi.org/10.1111/j.1365-2958.2010.07179.x,
36. https://doi.org/10.1128/mbio.02544-23,
37. https://doi.org/10.1128/mbio.02269-19,
38. https://doi.org/10.1038/s42003-024-07104-6,
39. https://doi.org/10.1016/j.bpj.2011.06.023,