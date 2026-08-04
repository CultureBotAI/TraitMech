# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **GC high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_high.yaml`.

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
**Generated:** 2026-08-04T04:51:35.794980

1. teng2023genomiclegaciesof pages 2-5
2. lassalle2015gccontentevolutionin pages 11-14
3. lind2008wholegenomemutationalbiases pages 1-1
4. teng2023genomiclegaciesof pages 8-10
5. akashi2013relevanceofgc pages 2-3
6. long2018specificityofthe pages 2-3
7. wu2012onthemolecular pages 1-2
8. long2018specificityofthe pages 5-6
9. long2018specificityofthe pages 3-3
10. GC\% = 100\times\frac{G+C}{A+T+G+C}
\
11. 10.1128/spectrum.02145-22
12. 10.1073/pnas.0804445105
13. 10.1093/molbev/msy134
14. 10.3389/fmicb.2013.00266
15. 10.1186/1745-6150-7-2
16. 10.1101/011023
17. 10.1093/nar/gkae132
18. 10.1099/mic.0.001404
19. https://doi.org/10.1128/spectrum.02145-22
20. https://doi.org/10.1073/pnas.0804445105
21. https://doi.org/10.1093/molbev/msy134
22. https://doi.org/10.3389/fmicb.2013.00266
23. https://doi.org/10.1186/1745-6150-7-2
24. https://doi.org/10.1101/011023
25. https://doi.org/10.1093/nar/gkae132
26. https://doi.org/10.1099/mic.0.001404
27. https://doi.org/10.1128/spectrum.02145-22,
28. https://doi.org/10.1101/011023,
29. https://doi.org/10.1073/pnas.0804445105,
30. https://doi.org/10.3389/fmicb.2013.00266,
31. https://doi.org/10.1093/molbev/msy134,
32. https://doi.org/10.1186/1745-6150-7-2,