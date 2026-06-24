# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC low
- **METPO identifier:** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:19:38.081537

1. tomasch2024ontheevolution pages 1-2
2. ruis2023mutationalspectraare pages 1-2
3. ruis2023mutationalspectraare pages 2-3
4. delgado2024impactofthe pages 1-2
5. ngugi2023abioticselectionof pages 1-2
6. barnum2024predictingmicrobialgrowth pages 1-3
7. chen2024globalmarinemicrobial pages 1-2
8. https://doi.org/10.1038/s41467-023-42916-w
9. https://doi.org/10.3389/fmicb.2024.1412318
10. https://doi.org/10.1101/2024.03.22.586313
11. https://doi.org/10.1038/s41467-023-36988-x
12. https://doi.org/10.1128/mbio.00602-24
13. https://doi.org/10.1038/s41586-024-07891-2
14. https://doi.org/10.1128/mbio.00602-24,
15. https://doi.org/10.17863/cam.102279,
16. https://doi.org/10.3389/fmicb.2024.1412318,
17. https://doi.org/10.1038/s41467-023-36988-x,
18. https://doi.org/10.1101/2024.03.22.586313,
19. https://doi.org/10.1038/s41586-024-07891-2,