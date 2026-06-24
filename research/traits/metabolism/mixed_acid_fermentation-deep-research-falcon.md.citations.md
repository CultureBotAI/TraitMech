# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixed-acid fermentation
- **METPO identifier:** traitmech:000027
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which sugars are converted via the glycolytic pathway to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and H2. Characteristic of enteric bacteria such as Escherichia coli.
- **Parent traits:** METPO:1002005
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation lists acetate, ethanol, lactate, succinate and formate as products of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation pathways describes mixed-acid fermentation by enterobacteria and its characteristic acid product spectrum.)
- **Existing causal graph summary:** mixed_acid_fermentation_enterobacterial: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mixed-acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/mixed_acid_fermentation.yaml`.

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
**Generated:** 2026-06-18T05:30:17.401598

1. brothwell2023formateproductionis pages 1-2
2. taggar2024hydrogenproductionvia pages 5-7
3. zhu2024acetateproductionfrom pages 4-7
4. li2024agrowthbasedscreening pages 2-4
5. ikeda2023supplementationwithamino pages 7-9
6. FocA
7. s
8. to
9. H2
10. https://doi.org/10.35812/cellulosechemtechnol.2024.58.90
11. https://doi.org/10.1128/iai.00176-23
12. https://doi.org/10.1128/aem.01472-24
13. https://doi.org/10.1186/s12934-024-02575-y
14. https://doi.org/10.1128/aem.00868-23
15. https://doi.org/10.1128/iai.00176-23,
16. https://doi.org/10.35812/cellulosechemtechnol.2024.58.90,
17. https://doi.org/10.1128/aem.01472-24,
18. https://doi.org/10.1186/s12934-024-02575-y,
19. https://doi.org/10.1128/aem.00868-23,