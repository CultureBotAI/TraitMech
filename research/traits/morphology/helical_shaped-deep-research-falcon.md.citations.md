# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** helical shaped
- **METPO identifier:** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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
**Generated:** 2026-06-18T08:29:57.410943

1. sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2
2. frirdich2023multiplecampylobacterjejuni pages 1-2
3. salama2020cellmorphologyas pages 1-2
4. sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5
5. pohl2024adynamicbactofilin pages 12-13
6. sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10
7. pohl2024adynamicbactofilin pages 3-4
8. pohl2024adynamicbactofilin pages 1-2
9. pohl2024adynamicbactofilin pages 21-22
10. label
11. GO:0048870
12. GO:0042710
13. GO:0009253-like label
14. GO:0009252
15. https://doi.org/10.3389/fmicb.2023.1162806
16. https://doi.org/10.7554/eLife.86577.2
17. https://doi.org/10.1016/j.mib.2019.12.002
18. https://doi.org/10.1016/j.cell.2010.03.046
19. https://doi.org/10.1371/journal.ppat.1002602
20. https://doi.org/10.1016/j.cell.2010.03.046,
21. https://doi.org/10.3389/fmicb.2023.1162806,
22. https://doi.org/10.1016/j.mib.2019.12.002,
23. https://doi.org/10.7554/elife.86577.2,
24. https://doi.org/10.1371/journal.ppat.1002602,