# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC high
- **METPO identifier:** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:19:32.812590

1. yasuda2024highlyreducedcomplementary pages 1-2
2. moncadas2026deepbranchingchloroflexotalineages pages 9-10
3. mccutcheon2024howdobacterial pages 4-5
4. mccutcheon2024howdobacterial pages 5-7
5. moncadas2026deepbranchingchloroflexotalineages pages 8-9
6. deka2025basesubstitutionsin pages 3-5
7. hale2025elevatedratesand pages 14-17
8. moncadas2026deepbranchingchloroflexotalineages pages 6-7
9. mccutcheon2024howdobacterial pages 1-3
10. mccutcheon2024howdobacterial pages 3-4
11. deka2025basesubstitutionsin pages 13-15
12. https://doi.org/10.1038/s41467-026-71228-y
13. https://doi.org/10.1264/jsme2.me24041
14. https://doi.org/10.1371/journal.pbio.3002577
15. https://doi.org/10.1128/mbio.03054-25
16. https://doi.org/10.63635/mrj.v1i4.188
17. https://doi.org/10.1264/jsme2.me24041,
18. https://doi.org/10.1038/s41467-026-71228-y,
19. https://doi.org/10.1371/journal.pbio.3002577,
20. https://doi.org/10.63635/mrj.v1i4.188,
21. https://doi.org/10.1128/mbio.03054-25,