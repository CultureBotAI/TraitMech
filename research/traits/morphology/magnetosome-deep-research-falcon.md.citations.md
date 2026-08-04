# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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
**Generated:** 2026-08-04T09:05:42.502214

1. ferrara2024bacterialorganellesin pages 2-4
2. ferrara2024bacterialorganellesin pages 4-6
3. cornejo2016dynamicremodelingof pages 1-2
4. mccausland2022globalanalysisof pages 1-2
5. chen2023effectsofstatic pages 1-6
6. awal2023experimentalanalysisof pages 1-2
7. amor2024magnetochromecatalyzedoxidationof pages 1-2
8. amor2024magnetochromecatalyzedoxidationof pages 7-8
9. amor2024magnetochromecatalyzedoxidationof pages 6-7
10. 10.1128/mbio.01898-15
11. 10.1111/mmi.15330
12. 10.1073/pnas.2410245121
13. 10.1128/mbio.01649-23
14. 10.1128/msystems.01037-21
15. 10.1093/jambio/lxad302
16. https://doi.org/10.1073/pnas.2410245121
17. https://doi.org/10.1111/mmi.15330
18. https://doi.org/10.1128/mbio.01649-23
19. https://doi.org/10.1093/jambio/lxad302
20. https://doi.org/10.1128/msystems.01037-21
21. https://doi.org/10.1111/1462-2920.15098
22. https://doi.org/10.1128/mbio.01898-15
23. https://doi.org/10.1038/nrmicro.2016.99
24. https://doi.org/10.1021/cr078258w
25. https://doi.org/10.1111/j.1574-6976.2008.00116.x
26. https://doi.org/10.1073/pnas.2410245121](https://doi.org/10.1073/pnas.2410245121
27. https://doi.org/10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330
28. https://doi.org/10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23
29. https://doi.org/10.1093/jambio/lxad302](https://doi.org/10.1093/jambio/lxad302
30. https://doi.org/10.1128/msystems.01037-21](https://doi.org/10.1128/msystems.01037-21
31. https://doi.org/10.1111/1462-2920.15098](https://doi.org/10.1111/1462-2920.15098
32. https://doi.org/10.1128/mbio.01898-15](https://doi.org/10.1128/mbio.01898-15
33. https://doi.org/10.1038/nrmicro.2016.99](https://doi.org/10.1038/nrmicro.2016.99
34. https://doi.org/10.1021/cr078258w](https://doi.org/10.1021/cr078258w
35. https://doi.org/10.1111/j.1574-6976.2008.00116.x](https://doi.org/10.1111/j.1574-6976.2008.00116.x
36. https://doi.org/10.1111/mmi.15330,
37. https://doi.org/10.1128/mbio.01649-23,
38. https://doi.org/10.1128/msystems.01037-21,
39. https://doi.org/10.1073/pnas.2410245121,
40. https://doi.org/10.1128/mbio.01898-15,
41. https://doi.org/10.1093/jambio/lxad302,
42. https://doi.org/10.1111/1462-2920.15098,