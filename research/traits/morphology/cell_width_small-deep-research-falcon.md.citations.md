# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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
**Generated:** 2026-08-04T07:58:53.031557

1. ago2023relationshipbetweenthe pages 1-3
2. middlemiss2024molecularmotortugofwar pages 1-2
3. ojima2024buddingandexplosive pages 1-2
4. zhang2023coordinatedpeptidoglycansynthases pages 1-2
5. dion2018celldiameterin pages 3-6
6. dion2018celldiameterin pages 18-19
7. dion2018celldiameterin pages 1-3
8. dion2018celldiameterin pages 8-10
9. https://doi.org/10.1038/s41467-024-49785-x
10. https://doi.org/10.3389/fmicb.2024.1400434
11. https://doi.org/10.1002/mbo3.1385
12. https://doi.org/10.1038/s41467-023-41082-3
13. https://doi.org/10.7554/eLife.50629
14. https://doi.org/10.7554/eLife.32471
15. https://doi.org/10.1101/392837
16. https://doi.org/10.1016/j.bpj.2016.07.017
17. https://doi.org/10.1073/pnas.1509610112
18. https://doi.org/10.1016/j.cub.2017.09.065
19. https://doi.org/10.1101/392837,
20. https://doi.org/10.1038/s41467-024-49785-x,
21. https://doi.org/10.1002/mbo3.1385,
22. https://doi.org/10.3389/fmicb.2024.1400434,
23. https://doi.org/10.1038/s41467-023-41082-3,