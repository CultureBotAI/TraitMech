# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC content
- **METPO identifier:** METPO:1000127
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that is describing the percentage of guanine and cytosine nucleotides in genomic DNA, calculated as the ratio of GC base pairs to total base pairs.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports GC content as a fundamental genome-composition descriptor varying widely across prokaryotic lineages.) | DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion and mutation bias as the mechanistic drivers of genomic GC composition.)
- **Existing causal graph summary:** gc_content_composition_drivers: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC content** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_content.yaml`.

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
**Generated:** 2026-06-18T03:11:32.970808

1. hu2022apositivecorrelation pages 1-2
2. hu2022apositivecorrelation pages 13-15
3. teng2023genomiclegaciesof pages 12-13
4. aliperti2023rkselectionof pages 1-3
5. teng2023genomiclegaciesof pages 10-12
6. aliperti2023rkselectionof pages 3-6
7. chuckran2023edaphiccontrolson pages 1-6
8. wang2023bacterialgenomesize pages 2-3
9. teng2023genomiclegaciesof pages 1-2
10. teng2023genomiclegaciesof pages 2-5
11. teng2023genomiclegaciesof pages 8-10
12. chuckran2023edaphiccontrolson pages 6-10
13. chuckran2023edaphiccontrolson pages 16-23
14. aliperti2023rkselectionof pages 6-9
15. https://doi.org/10.1128/spectrum.02145-22
16. https://doi.org/10.1186/s12864-022-08353-7
17. https://doi.org/10.1101/2021.11.17.469016;
18. https://doi.org/10.1038/s41467-023-43297-w
19. https://doi.org/10.1101/2021.11.17.469016
20. https://doi.org/10.1111/1462-2920.16511
21. https://doi.org/10.1111/1462-2920.16511,
22. https://doi.org/10.1128/spectrum.02145-22,
23. https://doi.org/10.1186/s12864-022-08353-7,
24. https://doi.org/10.1101/2021.11.17.469016,
25. https://doi.org/10.1038/s41467-023-43297-w,