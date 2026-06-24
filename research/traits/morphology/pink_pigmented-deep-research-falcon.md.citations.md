# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pink pigmented
- **METPO identifier:** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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
**Generated:** 2026-06-18T09:19:49.532464

1. sandmann2023genesandpathway pages 1-3
2. ma2024thebiosynthesismechanism pages 2-6
3. ma2024thebiosynthesismechanism pages 6-8
4. strakova2024unveilingthegenomic pages 11-13
5. sandmann2023genesandpathway pages 3-5
6. wang2024hostsmanipulatelifestyle pages 1-5
7. sandmann2023genesandpathway pages 12-14
8. ma2024thebiosynthesismechanism pages 1-2
9. godoy2023asingularppaaaerrlike pages 5-9
10. zhang2023geneticdiversityinto pages 9-10
11. guryanov2024bacterialpigmentprodigiosin pages 1-2
12. barreto2023microbialpigmentsmajor pages 4-6
13. zhang2023geneticdiversityinto pages 7-8
14. nagar2024genomicinsightson pages 5-6
15. guryanov2024bacterialpigmentprodigiosin pages 14-15
16. zhang2023geneticdiversityinto pages 8-9
17. nagar2024genomicinsightson pages 6-8
18. kumar2024isolationandcharacterization pages 18-22
19. nery2023quantummechanicaleffects pages 46-49
20. ma2024thebiosynthesismechanism pages 13-15
21. barreto2023microbialpigmentsmajor pages 6-8
22. label-only
23. Serratia marcescens
24. https://doi.org/10.1128/aem.00540-24;
25. https://doi.org/10.3389/fmars.2024.1421769;
26. https://doi.org/10.3390/biology12101346;
27. https://doi.org/10.3389/fmicb.2023.1295854;
28. https://doi.org/10.1101/2024.02.14.580325;
29. https://doi.org/10.3390/applmicrobiol4040115;
30. https://doi.org/10.1128/aem.00540-24
31. https://doi.org/10.3389/fmars.2024.1421769
32. https://doi.org/10.3390/md22040167
33. https://doi.org/10.3390/biology12101346
34. https://doi.org/10.3389/fmicb.2023.1295854
35. https://doi.org/10.1101/2024.02.14.580325
36. https://doi.org/10.3390/applmicrobiol4040115
37. https://doi.org/10.3390/microorganisms11122920
38. https://doi.org/10.1128/aem.00540-24,
39. https://doi.org/10.3389/fmars.2024.1421769,
40. https://doi.org/10.3390/biology12101346,
41. https://doi.org/10.1101/2024.02.14.580325,
42. https://doi.org/10.3390/applmicrobiol4040115,
43. https://doi.org/10.1128/msystems.00702-23,
44. https://doi.org/10.3390/microorganisms11122920,
45. https://doi.org/10.3389/fmicb.2023.1295854,