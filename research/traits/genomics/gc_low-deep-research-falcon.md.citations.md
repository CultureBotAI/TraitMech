# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **GC low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_low.yaml`.

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
**Generated:** 2026-08-04T04:56:17.820511

1. teng2023genomiclegaciesof pages 1-2
2. lind2008wholegenomemutationalbiases pages 1-2
3. lind2008wholegenomemutationalbiases pages 3-4
4. lind2008wholegenomemutationalbiases pages 1-1
5. wu2012onthemolecular pages 2-4
6. teng2023genomiclegaciesof pages 10-12
7. teng2023genomiclegaciesof pages 8-10
8. lassalle2015gccontentevolutionin pages 1-4
9. lassalle2015gccontentevolutionin pages 4-6
10. wu2012onthemolecular pages 1-2
11. lind2008wholegenomemutationalbiases pages 5-6
12. lind2008wholegenomemutationalbiases pages 4-5
13. 10.1128/spectrum.02145-22
14. 10.1073/pnas.0804445105
15. 10.1186/1745-6150-7-2
16. 10.1101/cshperspect.a018077
17. 10.1101/011023
18. https://doi.org/10.1073/pnas.0804445105
19. https://doi.org/10.1101/cshperspect.a018077
20. https://doi.org/10.1101/011023
21. https://doi.org/10.1128/spectrum.02145-22
22. https://doi.org/10.1186/1745-6150-7-2
23. https://doi.org/10.1128/spectrum.02145-22,
24. https://doi.org/10.1101/cshperspect.a018077,
25. https://doi.org/10.1073/pnas.0804445105,
26. https://doi.org/10.1101/011023,
27. https://doi.org/10.1186/1745-6150-7-2,