# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** natural competence
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 12 nodes, 8 edges

## Research Objective

Research the microbial trait **natural competence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/natural_competence.yaml`.

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
**Generated:** 2026-08-04T11:37:51.075783

1. toussaint2024unveilingtheregulatory pages 1-6
2. zuke2024fromisotopicallylabeled pages 9-12
3. marli2024geneticmodificationof pages 1-2
4. prudhomme2024pneumococcalcompetenceis pages 7-8
5. niu2025molecularmechanismsand pages 1-2
6. hardy2024yranisa pages 1-4
7. marli2024geneticmodificationof pages 2-5
8. toussaint2024unveilingtheregulatory pages 6-9
9. zuke2024fromisotopicallylabeled pages 6-9
10. prudhomme2024pneumococcalcompetenceis pages 3-4
11. hardy2024yranisa pages 9-12
12. prudhomme2024pneumococcalcompetenceis pages 1-2
13. prudhomme2024pneumococcalcompetenceis pages 2-3
14. prudhomme2024pneumococcalcompetenceis pages 5-6
15. prudhomme2024pneumococcalcompetenceis pages 8-8
16. niu2025molecularmechanismsand pages 15-16
17. 10.1128/mmbr.00125-23
18. 10.1101/2024.02.06.579203
19. 10.1128/msphere.00214-24
20. 10.1038/s41467-024-49853-2
21. 10.1101/2024.02.08.579460
22. 10.1128/mbio.02631-21
23. 10.1038/s41467-022-28690-1
24. https://doi.org/10.1128/mmbr.00125-23
25. https://doi.org/10.1101/2024.02.06.579203
26. https://doi.org/10.1128/msphere.00214-24
27. https://doi.org/10.1038/s41467-024-49853-2
28. https://doi.org/10.1101/2024.02.08.579460
29. https://doi.org/10.1128/mbio.02631-21
30. https://doi.org/10.1038/s41467-022-28690-1
31. https://doi.org/10.1128/mmbr.00125-23,
32. https://doi.org/10.3389/fmicb.2025.1578813,
33. https://doi.org/10.1101/2024.02.06.579203,
34. https://doi.org/10.1101/2024.02.08.579460,
35. https://doi.org/10.1128/msphere.00214-24,
36. https://doi.org/10.1038/s41467-024-49853-2,