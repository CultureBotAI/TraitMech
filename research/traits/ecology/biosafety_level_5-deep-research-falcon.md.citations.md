# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 5
- **METPO identifier:** METPO:1001106
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that is proposed as a classification beyond BSL-4 for hypothetical biological agents requiring enhanced containment.
- **Parent traits:** METPO:1001101
- **Synonyms:** 5
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the framing of pathogen hazard above existing BSL-4 thresholds (the rationale underlying the proposed BSL-5 classification).)
- **Existing causal graph summary:** biosafety_level_5_proposed_enhanced_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 5** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_5.yaml`.

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
**Generated:** 2026-08-03T22:59:29.037621

1. cohen2002missionarchitectureconsiderations pages 1-4
2. gao2024frombiosafetyto pages 6-7
3. yeh2021significanceofhighcontainment pages 7-8
4. pavone2024biologicalcontainmentfor pages 1-2
5. pavone2024biologicalcontainmentfor pages 2-3
6. warmflash2007assessingthebiohazard pages 1-5
7. kurth2022maintainingdifferentialpressure pages 1-2
8. gao2024frombiosafetyto pages 3-5
9. cohen2002missionarchitectureconsiderations pages 4-5
10. warmflash2007assessingthebiohazard pages 8-11
11. warmflash2007assessingthebiohazard pages 11-16
12. gao2024frombiosafetyto pages 9-10
13. https://doi.org/10.3390/laboratories1030013
14. https://doi.org/10.3390/ani14030454
15. https://doi.org/10.3389/fbioe.2022.953675
16. https://doi.org/10.26686/nzjhsp.v1i2.9540
17. https://doi.org/10.3389/fbioe.2021.720315
18. https://doi.org/10.3390/laboratories1030013,
19. https://doi.org/10.3389/fbioe.2021.720315,
20. https://doi.org/10.3390/ani14030454,
21. https://doi.org/10.3389/fbioe.2022.953675,
22. https://doi.org/10.26686/nzjhsp.v1i2.9540,