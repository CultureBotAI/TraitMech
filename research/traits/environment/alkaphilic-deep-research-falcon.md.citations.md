# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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
**Generated:** 2026-08-04T00:08:59.745475

1. maksimova2024metabolicandmorphological pages 1-2
2. goto2022differencesinbioenergetic pages 1-2
3. matsuno2018formationofproton pages 1-2
4. jong2023membraneproteomeof pages 8-9
5. ito2017mrpantiportershave pages 10-11
6. goto2022differencesinbioenergetic pages 2-3
7. https://doi.org/10.1155/2024/3087296.
8. https://doi.org/10.3389/fmicb.2023.1228266.
9. https://doi.org/10.3389/fmicb.2022.842785.
10. https://doi.org/10.3390/ijms23169156.
11. https://doi.org/10.3389/fmicb.2018.02331.
12. https://doi.org/10.3389/fmicb.2017.02325.
13. https://doi.org/10.1074/jbc.M116.751016.
14. https://doi.org/10.1016/S0021-9258(17
15. https://doi.org/10.1155/2024/3087296,
16. https://doi.org/10.3389/fmicb.2018.02331,
17. https://doi.org/10.3389/fmicb.2022.842785,
18. https://doi.org/10.3389/fmicb.2025.1637315,
19. https://doi.org/10.3390/ijms23169156,
20. https://doi.org/10.1074/jbc.m116.751016,
21. https://doi.org/10.3389/fmicb.2017.02325,
22. https://doi.org/10.3389/fmicb.2023.1228266,