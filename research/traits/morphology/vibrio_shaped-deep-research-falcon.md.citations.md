# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** vibrio shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 10 nodes, 11 edges

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
**Generated:** 2026-08-04T15:09:41.623927

1. pohl2024anoutermembrane pages 2-3
2. banks2022asymmetricpeptidoglycanediting pages 1-2
3. fernandez2020vibriocholeraeadapts pages 1-1
4. fernandez2020vibriocholeraeadapts pages 2-3
5. herzog2020smallregulatoryrnas pages 37-43
6. banks2022asymmetricpeptidoglycanediting pages 2-4
7. fernandez2020vibriocholeraeadapts pages 5-6
8. martin2020theevolutionof pages 5-9
9. nikolai2020rnamediatedcontrolof pages 1-2
10. fernandez2020vibriocholeraeadapts pages 1-2
11. pohl2024anoutermembrane pages 4-5
12. pohl2024anoutermembrane pages 9-10
13. martin2020theevolutionof pages 1-5
14. pohl2024anoutermembrane pages 1-2
15. banks2022asymmetricpeptidoglycanediting pages 10-11
16. pohl2024anoutermembrane pages 12-13
17. martin2020theevolutionof pages 11-18
18. pohl2024anoutermembrane pages 13-14
19. pohl2024anoutermembrane pages 10-11
20. banks2022asymmetricpeptidoglycanediting pages 12-12
21. pohl2024anoutermembrane pages 7-7
22. 5.5%, 5.9%
23. https://doi.org/10.1038/s41467-020-19890-8
24. https://doi.org/10.1073/pnas.2010199117
25. https://doi.org/10.1101/2020.02.20.954503
26. https://doi.org/10.5282/edoc.27302
27. https://doi.org/10.1038/s41467-022-29007-y
28. https://doi.org/10.1038/s41467-024-51790-z
29. https://doi.org/10.1016/j.cell.2016.12.019.
30. https://doi.org/10.3389/fmicb.2023.1162806.
31. https://doi.org/10.1038/s41467-024-52325-2.
32. https://doi.org/10.1093/femsre/fuad010.
33. https://doi.org/10.1073/pnas.2010199117,
34. https://doi.org/10.1038/s41467-020-19890-8,
35. https://doi.org/10.1038/s41467-022-29007-y,
36. https://doi.org/10.1038/s41467-024-51790-z,
37. https://doi.org/10.1101/2020.02.20.954503,
38. https://doi.org/10.5282/edoc.27302,