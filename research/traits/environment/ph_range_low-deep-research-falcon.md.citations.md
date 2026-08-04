# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **pH range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_low.yaml`.

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
**Generated:** 2026-08-04T03:01:36.402669

1. krulwich2011molecularaspectsof pages 1-3
2. johnson2020acidophilemicrobiologyin pages 1-2
3. ianutsevich2023theroleof pages 1-2
4. sionek2024theimpactof pages 5-6
5. krulwich2011molecularaspectsof pages 11-12
6. terradot2024escherichiacolimaintains pages 8-9
7. atasoy2024exploitationofmicrobial pages 10-11
8. tonietti2024unveilingthebioleaching pages 1-2
9. dopson2023eurypsychrophilicacidophilesfrom pages 9-11
10. krulwich2011molecularaspectsof pages 5-6
11. ianutsevich2023theroleof pages 2-4
12. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
13. dopson2023eurypsychrophilicacidophilesfrom pages 7-8
14. s
15. https://doi.org/10.1038/nrmicro2549.
16. https://doi.org/10.3389/fmicb.2023.1149903.
17. https://doi.org/10.3390/microorganisms11071733.
18. https://doi.org/10.1103/prxlife.2.043015.
19. https://doi.org/10.1111/1758-2229.70019.
20. https://doi.org/10.1093/femsre/fuad062.
21. https://doi.org/10.3390/fermentation10060298.
22. https://doi.org/10.3390/microorganisms12122407.
23. https://doi.org/10.21775/cimb.039.063.
24. https://doi.org/10.1038/nrmicro2549,
25. https://doi.org/10.21775/cimb.039.063,
26. https://doi.org/10.1111/1758-2229.70019,
27. https://doi.org/10.3390/microorganisms11071733,
28. https://doi.org/10.3390/fermentation10060298,
29. https://doi.org/10.3389/fmicb.2023.1149903,
30. https://doi.org/10.1103/prxlife.2.043015,
31. https://doi.org/10.1093/femsre/fuad062,
32. https://doi.org/10.3390/microorganisms12122407,