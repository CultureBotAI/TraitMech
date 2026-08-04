# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **chemotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotrophic.yaml`.

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
**Generated:** 2026-08-04T11:11:25.717333

1. gupta2020extracellularelectronuptake pages 5-6
2. gupta2020extracellularelectronuptake pages 8-9
3. wang2024characterizethegrowth pages 1-2
4. laufermeiser2024oxidationofsulfur pages 6-8
5. laufermeiser2024oxidationofsulfur pages 1-2
6. llorente2024novelelectrochemicalstrategies pages 1-2
7. wang2024characterizethegrowth pages 22-23
8. NiFe
9. 10.3390/microorganisms12030590
10. 10.1093/ismejo/wrae173
11. 10.1111/1751-7915.14383
12. 10.1007/s10295-020-02309-0
13. https://doi.org/10.3390/microorganisms12030590
14. https://doi.org/10.1093/ismejo/wrae173
15. https://doi.org/10.1111/1751-7915.14383
16. https://doi.org/10.1007/s10295-020-02309-0
17. https://doi.org/10.1007/s10295-020-02309-0,
18. https://doi.org/10.3390/microorganisms12030590,
19. https://doi.org/10.1111/1751-7915.14383,
20. https://doi.org/10.1093/ismejo/wrae173,