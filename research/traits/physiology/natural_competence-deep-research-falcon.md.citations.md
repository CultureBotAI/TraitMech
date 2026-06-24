# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** natural competence
- **METPO identifier:** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T11:59:57.108495

1. mazzamurro2024intragenomicconflictswith pages 1-2
2. zuke2024fromisotopicallylabeled pages 9-12
3. hardy2024yranisa pages 22-24
4. prudhomme2024pneumococcalcompetenceis pages 1-2
5. toussaint2024unveilingtheregulatory pages 16-19
6. marli2024geneticmodificationof pages 1-2
7. stukenberg2024establishingthefastgrowing pages 38-39
8. toussaint2024unveilingtheregulatory pages 6-9
9. zuke2024productiondynamicsand pages 23-28
10. zuke2024productiondynamicsand pages 56-60
11. prudhomme2024pneumococcalcompetenceis pages 13-14
12. zuke2024productiondynamicsand pages 158-161
13. zuke2024productiondynamicsand pages 34-38
14. prudhomme2024pneumococcalcompetenceis pages 8-8
15. prudhomme2024pneumococcalcompetenceis pages 5-6
16. toussaint2024unveilingtheregulatory pages 9-13
17. toussaint2024unveilingtheregulatory pages 39-41
18. toussaint2024unveilingtheregulatory pages 1-6
19. prudhomme2024pneumococcalcompetenceis pages 2-3
20. prudhomme2024pneumococcalcompetenceis pages 7-8
21. prudhomme2024pneumococcalcompetenceis pages 9-10
22. marli2024geneticmodificationof pages 2-5
23. zuke2024productiondynamicsand pages 161-163
24. prudhomme2024pneumococcalcompetenceis pages 12-13
25. toussaint2024unveilingtheregulatory pages 13-16
26. toussaint2024unveilingtheregulatory pages 32-39
27. https://doi.org/10.1128/mmbr.00125-23
28. https://doi.org/10.1101/2024.02.06.579203
29. https://doi.org/10.1371/journal.pbio.3002814
30. https://doi.org/10.1038/s41467-024-49853-2
31. https://doi.org/10.1101/2024.02.08.579460
32. https://doi.org/10.1128/msphere.00214-24
33. https://doi.org/10.1371/journal.pbio.3002814;
34. https://doi.org/10.17192/z2024.0096
35. https://doi.org/10.1371/journal.pbio.3002814,
36. https://doi.org/10.1038/s41467-024-49853-2,
37. https://doi.org/10.1101/2024.02.08.579460,
38. https://doi.org/10.1128/mmbr.00125-23,
39. https://doi.org/10.1101/2024.02.06.579203,
40. https://doi.org/10.1128/msphere.00214-24,
41. https://doi.org/10.17192/z2024.0096,