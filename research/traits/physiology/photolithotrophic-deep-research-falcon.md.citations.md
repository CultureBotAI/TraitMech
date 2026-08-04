# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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
**Generated:** 2026-08-04T12:01:37.850679

1. kushkevych2024anoxygenicphotosynthesiswith pages 16-17
2. kushkevych2024anoxygenicphotosynthesiswith pages 13-14
3. kushkevych2021anoxygenicphotosynthesisin pages 3-5
4. kushkevych2024anoxygenicphotosynthesiswith pages 4-6
5. kushkevych2024anoxygenicphotosynthesiswith pages 9-10
6. gupta2020extracellularelectronuptake pages 8-9
7. gupta2020extracellularelectronuptake pages 7-8
8. gupta2020extracellularelectronuptake pages 11-12
9. kushkevych2024anoxygenicphotosynthesiswith pages 15-16
10. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
11. kushkevych2024anoxygenicphotosynthesiswith pages 18-18
12. gupta2020extracellularelectronuptake pages 4-5
13. 10.3389/fmicb.2024.1417714
14. 10.3390/antiox10060829
15. 10.1007/s10295-020-02309-0
16. 10.3389/fmicb.2017.00323
17. https://doi.org/10.3389/fmicb.2024.1417714
18. https://doi.org/10.3390/antiox10060829
19. https://doi.org/10.1007/s10295-020-02309-0
20. https://doi.org/10.3389/fmicb.2017.00323
21. https://doi.org/10.3389/fmicb.2024.1417714,
22. https://doi.org/10.1007/s10295-020-02309-0,
23. https://doi.org/10.3390/antiox10060829,