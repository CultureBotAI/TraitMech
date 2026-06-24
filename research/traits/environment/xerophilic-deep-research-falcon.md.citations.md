# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xerophilic
- **METPO identifier:** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/xerophilic.yaml`.

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
**Generated:** 2026-06-18T03:10:51.886638

1. pocsi2024biotechnologicalpotentialof pages 1-2
2. grzyb2022introductiontobacterial pages 2-3
3. pocsi2024biotechnologicalpotentialof pages 2-5
4. preetha2020factorsinfluencingthe pages 6-7
5. pocsi2024biotechnologicalpotentialof pages 5-7
6. loukou2024dampbuildingsassociated pages 4-5
7. pocsi2024biotechnologicalpotentialof pages 11-12
8. raghavendra2026growthofmicroorganisms pages 13-14
9. dijksterhuis2025fungalspoilageof pages 16-17
10. agrawal2024hiddentreasurehalophilic pages 1-2
11. raghavendra2026growthofmicroorganisms pages 1-2
12. https://doi.org/10.1007/s00253-024-13338-5
13. https://doi.org/10.34293/sijash.v7i3.473
14. https://doi.org/10.3390/jof10040290
15. https://doi.org/10.1007/978-3-031-81904-9_3
16. https://doi.org/10.5281/zenodo.10001628
17. https://doi.org/10.3390/jof10020108
18. https://doi.org/10.3390/microorganisms10020432
19. https://doi.org/10.1007/s00253-024-13338-5,
20. https://doi.org/10.3390/jof10020108,
21. https://doi.org/10.3390/microorganisms10020432,
22. https://doi.org/10.34293/sijash.v7i3.473,
23. https://doi.org/10.3390/jof10040290,
24. https://doi.org/10.1038/s41598-026-35595-2,
25. https://doi.org/10.1007/978-3-031-81904-9\_3,