# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width very small
- **METPO identifier:** METPO:1000887
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension is at most approximately 0.5 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_<=0.5
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very narrow cell widths to oligotrophic and streamlined lineages.)
- **Existing causal graph summary:** cell_width_very_small_streamlining: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_very_small.yaml`.

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
**Generated:** 2026-06-18T07:25:27.586678

1. belykh2024ultramicrobacteriaandfilterable pages 1-2
2. belykh2024ultramicrobacteriaandfilterable pages 2-3
3. belykh2024ultramicrobacteriaandfilterable pages 3-5
4. giovannoni2014implicationsofstreamlining pages 3-4
5. giovannoni2014implicationsofstreamlining pages 1-2
6. noell2023areductionof pages 1-2
7. juillot2021ahighcontentmicroscopy pages 2-4
8. juillot2021ahighcontentmicroscopy pages 1-2
9. giovannoni2014implicationsofstreamlining pages 2-3
10. juillot2021ahighcontentmicroscopy pages 10-11
11. and
12. https://doi.org/10.1038/ismej.2014.60
13. https://doi.org/10.1128/mmbr.00124-22
14. https://doi.org/10.31951/2658-3518-2024-a-4-795
15. https://doi.org/10.1128/msystems.01017-21
16. https://doi.org/10.1101/2024.11.22.624946
17. https://doi.org/10.31951/2658-3518-2024-a-4-795,
18. https://doi.org/10.1038/ismej.2014.60,
19. https://doi.org/10.1128/mmbr.00124-22,
20. https://doi.org/10.1128/msystems.01017-21,
21. https://doi.org/10.1101/2024.11.22.624946,