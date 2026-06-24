# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid1
- **METPO identifier:** METPO:1000485
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 10–20 °C, characteristic of organisms with moderate thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_10_20
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity as common among generalist mesophiles.)
- **Existing causal graph summary:** temperature_delta_mid1_moderate_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid1.yaml`.

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
**Generated:** 2026-06-18T02:03:31.221194

1. noll2020modelingandexploiting pages 6-8
2. chaloner2020geometryandevolution pages 1-2
3. ramon2023ageneraloverview pages 1-2
4. lehmann2023adaptivelaboratoryevolution pages 1-2
5. son2023morphologicalandphysiological pages 1-2
6. sidarta2024lipidphaseseparation pages 1-2
7. ramon2023ageneraloverview pages 2-4
8. lehmann2023adaptivelaboratoryevolution pages 6-7
9. dessenne2024lipidomicanalysesreveal pages 1-2
10. purwar2024adaptationsofpsychrophilic pages 10-11
11. https://doi.org/10.1128/spectrum.03925-23
12. https://doi.org/10.1007/s42770-023-01057-4
13. https://doi.org/10.1128/spectrum.00757-24
14. https://doi.org/10.1111/mmi.15323
15. https://doi.org/10.1038/s41598-023-42179-x
16. https://doi.org/10.37256/amtt.5220244537
17. https://doi.org/10.3390/pr8010121
18. https://doi.org/10.1038/s41467-020-16778-5
19. https://doi.org/10.3390/pr8010121,
20. https://doi.org/10.1038/s41467-020-16778-5,
21. https://doi.org/10.1007/s42770-023-01057-4,
22. https://doi.org/10.3389/fmicb.2023.1265216,
23. https://doi.org/10.1038/s41598-023-42179-x,
24. https://doi.org/10.1128/spectrum.03925-23,
25. https://doi.org/10.1128/spectrum.00757-24,
26. https://doi.org/10.37256/amtt.5220244537,