# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000444
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 27 and 30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 27–30 °C optimum as a typical mesophile setpoint maintained by homoviscous membrane composition.)
- **Existing causal graph summary:** temperature_optimum_mid2_mesophile: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid2.yaml`.

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
**Generated:** 2026-08-04T04:05:08.836009

1. engqvist2018correlatingenzymeannotations pages 1-2
2. mendoza2014temperaturesensingby pages 2-4
3. sidarta2024lipidphaseseparation pages 1-2
4. mendoza2014temperaturesensingby pages 5-6
5. sidarta2024lipidphaseseparation pages 12-14
6. richter2024membranefluiditycontrol pages 16-18
7. zhou2021acoldshock pages 1-2
8. mendoza2014temperaturesensingby pages 1-2
9. mendoza2014temperaturesensingby pages 4-5
10. 10.1128/spectrum.03925-23
11. 10.1111/mmi.15323
12. 10.1371/journal.ppat.1012738
13. 10.1146/annurev-micro-091313-103612
14. 10.1038/s41421-021-00246-5
15. 10.1186/s12866-018-1320-7
16. 10.5281/zenodo.1175608
17. https://doi.org/10.1128/spectrum.03925-23
18. https://doi.org/10.1111/mmi.15323
19. https://doi.org/10.1371/journal.ppat.1012738
20. https://doi.org/10.1146/annurev-micro-091313-103612
21. https://doi.org/10.1038/s41421-021-00246-5
22. https://doi.org/10.1186/s12866-018-1320-7
23. https://doi.org/10.5281/zenodo.1175608
24. https://doi.org/10.1146/annurev-micro-091313-103612,
25. https://doi.org/10.1128/spectrum.03925-23,
26. https://doi.org/10.1111/mmi.15323,
27. https://doi.org/10.1186/s12866-018-1320-7,
28. https://doi.org/10.1371/journal.ppat.1012738,
29. https://doi.org/10.1038/s41421-021-00246-5,