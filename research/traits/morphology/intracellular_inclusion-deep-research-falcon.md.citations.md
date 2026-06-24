# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** intracellular inclusion
- **METPO identifier:** traitmech:000066
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing a discrete intracellular body — a storage granule, gas-filled structure, or protein-bounded microcompartment/organelle — that compartmentalizes material or function within a prokaryotic cell.
- **Parent traits:** METPO:1000059
- **Synonyms:** cytoplasmic inclusion
- **Existing evidence:** DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow, "Formation and function of bacterial organelles", establish that bacteria contain diverse inclusions/organelles (storage granules, gas vesicles, microcompartments, magnetosomes); parent of the inclusion sub-variants.) | DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments as a major class of protein-bounded intracellular organelles.)
- **Existing causal graph summary:** inclusion_compartmentalization: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **intracellular inclusion** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/intracellular_inclusion.yaml`.

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
**Generated:** 2026-06-18T08:48:41.110037

1. doron2024bacterialmicrocompartmentsas pages 1-3
2. but2024newsolutionsin pages 1-2
3. corrales2025polyphosphatefromlactic pages 1-2
4. nezio2024synergisticphenotypicadaptations pages 1-2
5. doron2024bacterialmicrocompartmentsas pages 3-5
6. trettel2024modelingbacterialmicrocompartment pages 1-2
7. paulus2024mamflikeproteinsare pages 1-2
8. woo2024isolationandcharacterization pages 1-2
9. woo2024isolationandcharacterization pages 2-6
10. iburg2024elucidatingtheassembly pages 1-2
11. feng2024advancesinthe pages 1-2
12. feng2024advancesinthe pages 2-4
13. paulus2024mamflikeproteinsare pages 2-3
14. kushkevych2024anoxygenicphotosynthesiswith pages 18-18
15. nezio2024synergisticphenotypicadaptations pages 2-3
16. martinez2024enhancingmagnetosomebiomanufacturing pages 29-32
17. paulus2024mamflikeproteinsare pages 3-5
18. saito2024regulatoryroleof pages 1-2
19. corrales2025polyphosphatefromlactic pages 13-15
20. yadav2025therapeuticinnovationsin pages 7-9
21. altamiraalgarra2024bioplasticproductionby pages 20-22
22. iburg2024elucidatingtheassembly pages 2-4
23. iburg2024elucidatingtheassembly pages 4-5
24. feng2024advancesinthe pages 9-10
25. yadav2025therapeuticinnovationsin pages 9-11
26. corrales2025polyphosphatefromlactic pages 2-4
27. https://doi.org/10.3390/molecules29102293
28. https://doi.org/10.1128/aem.00603-24
29. https://doi.org/10.3390/fermentation10050265
30. https://doi.org/10.3390/microorganisms12010115
31. https://doi.org/10.3390/foods14132211
32. https://doi.org/10.1186/s13036-024-00426-3
33. https://doi.org/10.1038/s44318-024-00178-2
34. https://doi.org/10.1042/bst20230229
35. https://doi.org/10.3389/fpls.2024.1346759
36. https://doi.org/10.1038/s41467-024-55121-0
37. https://doi.org/10.2147/IJN.S462031
38. https://doi.org/10.1371/journal.pone.0310265
39. https://doi.org/10.3389/fmicb.2024.1417714
40. https://doi.org/10.1042/bst20230229,
41. https://doi.org/10.1186/s13036-024-00426-3,
42. https://doi.org/10.3390/molecules29102293,
43. https://doi.org/10.3390/fermentation10050265,
44. https://doi.org/10.3390/foods14132211,
45. https://doi.org/10.1038/s41467-024-55121-0,
46. https://doi.org/10.1371/journal.pone.0310265,
47. https://doi.org/10.3389/fpls.2024.1346759,
48. https://doi.org/10.1038/s44318-024-00178-2,
49. https://doi.org/10.1128/aem.00603-24,
50. https://doi.org/10.2147/ijn.s462031,
51. https://doi.org/10.3390/microorganisms12010115,
52. https://doi.org/10.3389/fmicb.2024.1417714,
53. https://doi.org/10.1101/2023.11.06.565755,