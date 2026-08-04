# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 4
- **METPO identifier:** METPO:1001105
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses extreme risk of life-threatening disease through aerosol transmission with no available treatment.
- **Parent traits:** METPO:1001101
- **Synonyms:** 4
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the extreme virulence and absence of countermeasures characteristic of BSL-4 agents.)
- **Existing causal graph summary:** biosafety_level_4_extreme_hazard: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **biosafety level 4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_4.yaml`.

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
**Generated:** 2026-08-03T23:21:51.065515

1. gao2024frombiosafetyto pages 5-6
2. gao2024frombiosafetyto pages 10-12
3. nunez2024treatmentofhighly pages 26-28
4. ndayambaje2024molecularcharacterizationof pages 4-6
5. vogel2023viraltargetingof pages 4-6
6. ndayambaje2024molecularcharacterizationof pages 14-15
7. https://doi.org/10.3390/laboratories1030013
8. https://doi.org/10.1080/22221751.2024.2356149
9. https://doi.org/10.1007/s40121-023-00913-y
10. https://doi.org/10.3390/cells13010071
11. https://doi.org/10.1186/s43042-024-00600-8
12. https://doi.org/10.1038/s41390-023-02873-y
13. https://doi.org/10.1080/17460441.2024.2340494
14. https://doi.org/10.3390/laboratories1030013,
15. https://doi.org/10.1080/17460441.2024.2340494,
16. https://doi.org/10.1186/s43042-024-00600-8,
17. https://doi.org/10.3390/cells13010071,