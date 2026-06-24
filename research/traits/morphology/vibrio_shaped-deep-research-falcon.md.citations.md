# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** vibrio shaped
- **METPO identifier:** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **vibrio shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/vibrio_shaped.yaml`.

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
**Generated:** 2026-06-18T10:34:56.153160

1. nikolai2020rnamediatedcontrolof pages 1-2
2. fernandez2020vibriocholeraeadapts pages 5-6
3. goudin2023recoveryofvibrio pages 1-2
4. goudin2023recoveryofvibrio pages 6-8
5. fernandez2020vibriocholeraeadapts pages 1-2
6. pohl2024anoutermembrane pages 1-2
7. nikolai2020rnamediatedcontrolof pages 4-6
8. martin2020theevolutionof pages 5-9
9. fernandez2020vibriocholeraeadapts pages 4-5
10. pohl2024anoutermembrane pages 10-11
11. schiller2024identificationofstructural pages 1-2
12. 5.5%, 5.9%
13. −0.87%, 2.8%
14. −0.40, 0.22
15. −0.91, −0.28
16. https://doi.org/10.1038/s41467-020-19890-8
17. https://doi.org/10.1038/s41598-023-40897-w
18. https://doi.org/10.1101/2020.02.20.954503
19. https://doi.org/10.1073/pnas.2010199117
20. https://doi.org/10.1038/s41467-024-51790-z
21. https://doi.org/10.1371/journal.pone.0293276
22. https://doi.org/10.1038/s41467-024-45196-0
23. https://doi.org/10.1038/s41467-020-19890-8,
24. https://doi.org/10.1073/pnas.2010199117,
25. https://doi.org/10.1038/s41467-024-51790-z,
26. https://doi.org/10.1371/journal.pone.0293276,
27. https://doi.org/10.1038/s41467-024-45196-0,
28. https://doi.org/10.1101/2020.02.20.954503,