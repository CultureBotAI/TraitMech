# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** euryhaline
- **METPO identifier:** METPO:1000627
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate a wide range of salinity conditions.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.5928/kaiyou.14.337: growing over a salinity range of 15% (Supports euryhaline halophiles as organisms growing across a wide salinity range.) | PMID:22675587: due to its strong euryhaline phenotype (Organism example: Chromohalobacter salexigens is described as having a strong euryhaline phenotype.)
- **Existing causal graph summary:** euryhaline_wide_salinity_tolerance: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **euryhaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/euryhaline.yaml`.

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
**Generated:** 2026-06-17T21:59:45.718007

1. wu2024metagenomicinsightsinto pages 1-2
2. bonnaud2024haloarchaeaaspromising pages 2-4
3. wu2024metagenomicinsightsinto pages 13-14
4. jurdzinski2023largescalephylogenomicsof pages 11-12
5. wu2024metagenomicinsightsinto pages 11-13
6. galisteo2023astepinto pages 13-14
7. jurdzinski2023largescalephylogenomicsof pages 1-1
8. galisteo2023astepinto pages 14-17
9. was
10. https://doi.org/10.1186/s40168-024-01817-w
11. https://doi.org/10.3389/fmicb.2023.1192059
12. https://doi.org/10.3390/microorganisms12081738
13. https://doi.org/10.1126/sciadv.adg2059
14. https://doi.org/10.1186/s40168-024-01817-w,
15. https://doi.org/10.3390/microorganisms12081738,
16. https://doi.org/10.3389/fmicb.2023.1192059,
17. https://doi.org/10.1126/sciadv.adg2059,