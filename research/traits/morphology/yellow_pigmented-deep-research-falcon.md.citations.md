# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** yellow pigmented
- **METPO identifier:** METPO:1003030
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear yellow due to production of yellow pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_yellow
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated bacterial color phenotype.)
- **Existing causal graph summary:** yellow_pigmented_carotenoid_color: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **yellow pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/yellow_pigmented.yaml`.

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
**Generated:** 2026-06-18T10:47:04.222281

1. gottl2024enhancingastaxanthinbiosynthesis pages 1-3
2. huang2024bacterialpigmentsas pages 6-8
3. liu2024multiomicsdissectionof pages 11-12
4. anshi2024unveilingtheintricacies pages 2-4
5. dey2024aninsightinto pages 1-2
6. anshi2024unveilingtheintricacies pages 4-5
7. jimenez2024estudoinvitroa pages 96-99
8. zhan2024expandingthecrispr pages 1-2
9. gottl2024enhancingastaxanthinbiosynthesis pages 3-3
10. gottl2024enhancingastaxanthinbiosynthesis pages 5-6
11. jimenez2024estudoinvitro pages 114-118
12. dey2024aninsightinto pages 11-12
13. jimenez2024estudoinvitroa pages 87-92
14. jimenez2024estudoinvitroa pages 114-118
15. shende2024theshikimatepathway pages 3-4
16. jimenez2024estudoinvitro pages 54-60
17. jimenez2024estudoinvitroa pages 54-60
18. jimenez2024estudoinvitro pages 92-96
19. gottl2024enhancingastaxanthinbiosynthesis pages 8-9
20. zhan2024expandingthecrispr pages 12-14
21. jimenez2024estudoinvitro pages 96-99
22. gottl2024enhancingastaxanthinbiosynthesis pages 6-8
23. https://doi.org/10.1038/s41598-024-58700-9
24. https://doi.org/10.1038/s41598-024-58700-9;
25. https://doi.org/10.3390/microorganisms12040803
26. https://doi.org/10.4014/jmb.2404.04018;
27. https://doi.org/10.11606/d.97.2024.tde-12122024-113132
28. https://doi.org/10.1016/j.heliyon.2024.e34275
29. https://doi.org/10.1038/s41467-024-54112-5
30. https://doi.org/10.3390/micro4040038
31. https://doi.org/10.4014/jmb.2404.04018
32. https://doi.org/10.1039/d3np00037k
33. https://doi.org/10.1038/s41467-024-54112-5,
34. https://doi.org/10.3390/micro4040038,
35. https://doi.org/10.1038/s41598-024-58700-9,
36. https://doi.org/10.4014/jmb.2404.04018,
37. https://doi.org/10.1016/j.heliyon.2024.e34275,
38. https://doi.org/10.3390/microorganisms12040803,
39. https://doi.org/10.11606/d.97.2024.tde-12122024-113132,
40. https://doi.org/10.1039/d3np00037k,