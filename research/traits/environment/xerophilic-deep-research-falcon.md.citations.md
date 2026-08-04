# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 8 nodes, 6 edges

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
**Generated:** 2026-08-04T04:41:17.795510

1. hamill2020microbiallagphase pages 3-4
2. pocsi2024biotechnologicalpotentialof pages 2-5
3. zajc2014osmoadaptationstrategyof pages 1-2
4. perezllano2020stressreshapesthe pages 15-17
5. perezllano2020stressreshapesthe pages 8-11
6. pocsi2024biotechnologicalpotentialof pages 5-7
7. pocsi2024biotechnologicalpotentialof pages 7-8
8. pocsi2024biotechnologicalpotentialof pages 1-2
9. perezllano2020stressreshapesthe pages 11-13
10. zajc2014osmoadaptationstrategyof pages 9-9
11. pocsi2024biotechnologicalpotentialof pages 12-13
12. pocsi2024biotechnologicalpotentialof pages 11-12
13. pocsi2024biotechnologicalpotentialof pages 10-11
14. perezllano2020stressreshapesthe pages 4-8
15. 10.1007/s00253-024-13338-5
16. 10.1128/AEM.02702-13
17. 10.3390/cells9030525
18. 10.1038/s41598-020-62552-4
19. https://doi.org/10.1007/s00253-024-13338-5
20. https://doi.org/10.1128/AEM.02702-13
21. https://doi.org/10.3390/cells9030525
22. https://doi.org/10.1038/s41598-020-62552-4
23. https://doi.org/10.1007/s00253-024-13338-5,
24. https://doi.org/10.1038/s41598-020-62552-4,
25. https://doi.org/10.1128/aem.02702-13,
26. https://doi.org/10.3390/cells9030525,