# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccobacillus shaped
- **METPO identifier:** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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
**Generated:** 2026-06-18T07:18:29.549087

1. pereira2016ftszdependentelongationof pages 1-2
2. cantlay2024phenotypicandtranscriptional pages 5-6
3. micelli2023aconservedzincbinding pages 1-2
4. castanheira2023evidenceoftwo pages 2-3
5. costa2024theroleof pages 1-2
6. cantlay2024phenotypicandtranscriptional pages 6-8
7. barry2024longtermsurvivalphasecells pages 1-2
8. slovak2005localizationofmreb pages 3-3
9. pereira2016ftszdependentelongationof pages 2-3
10. slovak2005localizationofmreb pages 7-10
11. costa2024theroleof pages 2-4
12. https://doi.org/10.1128/JB.187.1.54-64.2005
13. https://doi.org/10.1073/pnas.2215237120
14. https://doi.org/10.1038/s42003-023-05308-w
15. https://doi.org/10.1128/mbio.03235-23
16. https://doi.org/10.3389/fmicb.2024.1347488
17. https://doi.org/10.3389/frfst.2024.1442761
18. https://doi.org/10.1128/mbio.00908-16
19. https://doi.org/10.1128/jb.187.1.54-64.2005,
20. https://doi.org/10.1128/mbio.00908-16,
21. https://doi.org/10.3389/fmicb.2024.1347488,
22. https://doi.org/10.3389/frfst.2024.1442761,
23. https://doi.org/10.1073/pnas.2215237120,
24. https://doi.org/10.1038/s42003-023-05308-w,
25. https://doi.org/10.1128/mbio.03235-23,