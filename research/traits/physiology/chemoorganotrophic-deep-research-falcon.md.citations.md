# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 17 nodes, 15 edges

## Research Objective

Research the microbial trait **chemoorganotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganotrophic.yaml`.

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
**Generated:** 2026-08-04T11:05:22.669003

1. azevedo2024microbialcontributionto pages 1-2
2. simon2008theorganisationof pages 1-3
3. spero2015phylogenomicanalysisand pages 1-2
4. freches2024thebiotechnologicalpotential pages 1-4
5. briski2017environmentalmicrobiology pages 1-3
6. hackmann2024thevastlandscape pages 2-3
7. hackmann2024thevastlandscape pages 4-5
8. hackmann2024thevastlandscape pages 3-4
9. freches2024thebiotechnologicalpotential pages 12-14
10. freches2024thebiotechnologicalpotential pages 6-9
11. hackmann2024thevastlandscape pages 1-2
12. freches2024thebiotechnologicalpotential pages 14-15
13. 10.1093/femsre/fuae016
14. 10.1128/aem.01756-23
15. 10.36783/18069657rbcs20230065
16. 10.1128/mbio.00389-15
17. 10.1016/j.bbabio.2008.09.008
18. 10.1515/psr-2016-0118
19. https://doi.org/10.1093/femsre/fuae016
20. https://doi.org/10.1128/aem.01756-23
21. https://doi.org/10.36783/18069657rbcs20230065
22. https://doi.org/10.1128/mbio.00389-15
23. https://doi.org/10.1016/j.bbabio.2008.09.008
24. https://doi.org/10.1515/psr-2016-0118
25. https://doi.org/10.36783/18069657rbcs20230065,
26. https://doi.org/10.1128/aem.01756-23,
27. https://doi.org/10.1093/femsre/fuae016,
28. https://doi.org/10.1016/j.bbabio.2008.09.008,
29. https://doi.org/10.1128/mbio.00389-15,
30. https://doi.org/10.1515/psr-2016-0118,