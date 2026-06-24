# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** red pigmented
- **METPO identifier:** METPO:1003028
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear red due to production of red pigments such as prodiginines or carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_red
- **Existing evidence:** DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports red microbial pigmentation as a prodiginine-associated color phenotype in representative bacteria.)
- **Existing causal graph summary:** red_pigmented_prodiginine_pathway: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **red pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/red_pigmented.yaml`.

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
**Generated:** 2026-06-18T09:47:15.833451

1. barreto2023microbialpigmentsmajor pages 10-12
2. lu2024prodigiosinunveilingthe pages 8-9
3. barreto2023microbialpigmentsmajor pages 4-6
4. ochoavinals2024currentadvancesin pages 2-5
5. pereira2024improvingbioprocessconditions pages 1-2
6. ochoavinals2024currentadvancesin pages 7-8
7. ochoavinals2024currentadvancesin pages 5-6
8. mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9
9. barreto2023biotechnologicalapplicationsof pages 7-9
10. sakaikawada2020characterizationofprodiginine pages 23-29
11. esteves2024serratiamarcescensatcc pages 1-2
12. barreto2023biotechnologicalapplicationsof pages 11-14
13. esteves2024serratiamarcescensatcc pages 2-3
14. lu2024prodigiosinunveilingthe pages 9-10
15. pereira2024improvingbioprocessconditions pages 19-20
16. pereira2024improvingbioprocessconditions pages 9-11
17. ochoavinals2024currentadvancesin pages 1-2
18. mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2
19. esteves2024serratiamarcescensatcc pages 3-5
20. pereira2024improvingbioprocessconditions pages 14-16
21. pereira2024improvingbioprocessconditions pages 16-17
22. pan2021regulatorrcsbcontrols pages 10-12
23. https://doi.org/10.3390/microorganisms11122920
24. https://doi.org/10.20944/preprints202310.0121.v1
25. https://doi.org/10.3389/fmicb.2024.1412776
26. https://doi.org/10.33043/ff.3.1.33-51
27. https://doi.org/10.1038/s41598-024-68747-3
28. https://doi.org/10.3390/md22040142
29. https://doi.org/10.3390/fermentation10040190
30. https://doi.org/10.3389/ffunb.2024.1378590
31. https://doi.org/10.3390/molecules29030589
32. https://doi.org/10.3390/microorganisms11122920,
33. https://doi.org/10.3389/fmicb.2024.1412776,
34. https://doi.org/10.3390/fermentation10040190,
35. https://doi.org/10.3390/molecules29030589,
36. https://doi.org/10.20944/preprints202310.0121.v1,
37. https://doi.org/10.1038/s41598-024-68747-3,
38. https://doi.org/10.3390/md22040142,
39. https://doi.org/10.3389/ffunb.2024.1378590,
40. https://doi.org/10.1128/aem.02052-20,