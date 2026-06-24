# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range low
- **METPO identifier:** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T00:49:49.312731

1. dopson2023eurypsychrophilicacidophilesfrom pages 8-9
2. kim2023clcchloridechannels pages 2-4
3. deng2023strategiesofchemolithoautotrophs pages 14-16
4. sreenivas2024evaluationofpyrophosphatedriven pages 1-2
5. perezrodriguez2024methodsforstudying pages 36-37
6. the membrane potential
7. https://doi.org/10.3389/fmicb.2023.1149903
8. https://doi.org/10.4014/jmb.2303.03009;
9. https://doi.org/10.3389/fmicb.2022.1034164
10. https://doi.org/10.3390/microorganisms12030625;
11. https://doi.org/10.3390/microorganisms12030625
12. https://doi.org/10.4014/jmb.2303.03009
13. https://doi.org/10.1111/1758-2229.70019
14. https://doi.org/10.1186/s40168-023-01712-w
15. https://doi.org/10.3389/fmicb.2023.1149903;
16. https://doi.org/10.3389/fmicb.2023.1149903,
17. https://doi.org/10.4014/jmb.2303.03009,
18. https://doi.org/10.1111/1758-2229.70019,
19. https://doi.org/10.1186/s40168-023-01712-w,
20. https://doi.org/10.3390/microorganisms12030625,
21. https://doi.org/10.3389/fmicb.2022.1034164,