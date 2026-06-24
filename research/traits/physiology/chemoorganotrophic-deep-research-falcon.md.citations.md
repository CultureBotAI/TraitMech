# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganotrophic
- **METPO identifier:** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 8 nodes, 7 edges

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
**Generated:** 2026-06-18T11:31:08.914539

1. weissbrodt2023basicmicrobiologyand pages 16-18
2. hackmann2024thevastlandscape pages 2-3
3. weissbrodt2023basicmicrobiologyand pages 19-22
4. briski2017environmentalmicrobiology pages 3-4
5. hackmann2024thevastlandscape pages 1-2
6. hackmann2024thevastlandscape pages 5-6
7. garimella2024fromcellsto pages 4-6
8. hackmann2024thevastlandscape pages 10-11
9. sawers2025howfocafacilitates pages 7-8
10. sawers2025howfocafacilitates pages 1-3
11. briski2017environmentalmicrobiology pages 15-16
12. briski2017environmentalmicrobiology pages 13-15
13. weissbrodt2023basicmicrobiologyand pages 43-44
14. bettendorff2026electrontransferin pages 9-11
15. bettendorff2026electrontransferin pages 7-9
16. gupta2024exploringthebioenergetics pages 15-19
17. hackmann2024thevastlandscape pages 9-10
18. hackmann2024thevastlandscape pages 12-13
19. hackmann2024thevastlandscape pages 4-5
20. https://doi.org/10.2166/9781789062304_0009
21. https://doi.org/10.1093/femsre/fuae016
22. https://doi.org/10.3390/biophysica6020027
23. https://doi.org/10.1186/s13213-024-01761-y
24. https://doi.org/10.1128/jb.00502-24
25. https://doi.org/10.1515/psr-2016-0118
26. https://doi.org/10.2166/9781789062304\_0009,
27. https://doi.org/10.1186/s13213-024-01761-y,
28. https://doi.org/10.1093/femsre/fuae016,
29. https://doi.org/10.1515/psr-2016-0118,
30. https://doi.org/10.3390/biophysica6020027,
31. https://doi.org/10.1128/jb.00502-24,