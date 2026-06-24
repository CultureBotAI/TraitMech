# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately alkaphilic
- **METPO identifier:** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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
**Generated:** 2026-06-17T23:56:08.350874

1. khomyakova2023phenotypicandgenomic pages 1-2
2. khomyakova2023phenotypicandgenomic pages 2-3
3. xing2024thepolyextremophilenatranaerobius pages 19-21
4. yao2023howmethanotrophsrespond pages 5-7
5. jong2023membraneproteomeof pages 9-10
6. jong2023membraneproteomeof pages 8-9
7. https://doi.org/10.1128/AEM.00145-24
8. https://doi.org/10.3389/fmicb.2022.1034164
9. https://doi.org/10.3389/fmicb.2023.1228266
10. https://doi.org/10.3389/fmicb.2023.1233691
11. https://doi.org/10.1128/aem.00145-24
12. https://doi.org/10.3389/fmicb.2023.1233691,
13. https://doi.org/10.1128/aem.00145-24,
14. https://doi.org/10.3389/fmicb.2022.1034164,
15. https://doi.org/10.3389/fmicb.2023.1228266,