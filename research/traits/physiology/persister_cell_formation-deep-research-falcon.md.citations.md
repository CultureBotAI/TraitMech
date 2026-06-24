# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** persister cell formation
- **METPO identifier:** traitmech:000082
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** Formation of dormant phenotypic variants (persister cells) that are transiently tolerant to antibiotics and other lethal stresses without carrying genetic resistance, arising stochastically in a population.
- **Parent traits:** traitmech:000080
- **Synonyms:** persistence
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134306:  (Lewis reviews persister cells as dormant variants highly tolerant to antibiotics.) | DOI:10.1038/nrmicro1557:  (Lewis links persister-cell dormancy to the recalcitrance of chronic infections.)
- **Existing causal graph summary:** persister_dormancy_tolerance: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **persister cell formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/persister_cell_formation.yaml`.

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
**Generated:** 2026-06-18T12:25:48.963810

1. shore2024typeitoxinantitoxin pages 18-20
2. yuan2024molecularmechanismand pages 3-6
3. santi2024toxinmediateddepletionof pages 3-4
4. wan2024protonmotiveforce pages 6-7
5. fernandezgarcia2024toxinantitoxinsystemsinduce pages 1-3
6. blattman2024identificationandgenetic pages 4-5
7. https://doi.org/10.3389/fmicb.2024.1395504
8. https://doi.org/10.1038/s44318-024-00248-5
9. https://doi.org/10.1128/spectrum.03388-23
10. https://doi.org/10.1111/1751-7915.70042
11. https://doi.org/10.1186/s12866-024-03628-3
12. https://doi.org/10.1128/ecosalplus.esp-0025-2022
13. https://doi.org/10.1038/s41586-024-08124-2
14. https://doi.org/10.3390/microorganisms12061158
15. https://doi.org/10.1128/ecosalplus.esp-0025-2022,
16. https://doi.org/10.1186/s12866-024-03628-3,
17. https://doi.org/10.3389/fmicb.2024.1395504,
18. https://doi.org/10.1128/spectrum.03388-23,
19. https://doi.org/10.1038/s44318-024-00248-5,
20. https://doi.org/10.1111/1751-7915.70042,
21. https://doi.org/10.1038/s41586-024-08124-2,
22. https://doi.org/10.3390/microorganisms12061158,