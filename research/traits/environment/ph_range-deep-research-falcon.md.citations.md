# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range
- **METPO identifier:** METPO:1000332
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005: highly impermeable cell membranes (pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.)
- **Existing causal graph summary:** ph_range_bounded_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range.yaml`.

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
**Generated:** 2026-06-18T00:48:19.144669

1. krulwich2011molecularaspectsof pages 1-3
2. krulwich2011molecularaspectsof pages 3-5
3. carere2021growthonformic pages 1-2
4. ramoneda2023buildingagenomebased pages 6-7
5. yao2023howmethanotrophsrespond pages 4-5
6. yao2023howmethanotrophsrespond pages 5-7
7. yao2023howmethanotrophsrespond pages 7-8
8. atasoy2024exploitationofmicrobial pages 7-8
9. atasoy2024exploitationofmicrobial pages 5-6
10. jiang2024exogenousputrescineplays pages 1-2
11. atasoy2024exploitationofmicrobial pages 17-18
12. krulwich2011molecularaspectsof pages 5-6
13. krulwich2011molecularaspectsof pages 12-14
14. ito2017mrpantiportershave pages 1-2
15. lund2020understandinghowmicroorganisms pages 3-5
16. lund2020understandinghowmicroorganisms pages 2-3
17. ito2017mrpantiportershave pages 5-8
18. krulwich2011molecularaspectsof pages 15-17
19. krulwich2011molecularaspectsof pages 27-28
20. ramoneda2023buildingagenomebased pages 1-2
21. atasoy2024exploitationofmicrobial pages 2-3
22. atasoy2024exploitationofmicrobial pages 1-2
23. atasoy2024exploitationofmicrobial pages 3-4
24. ito2017mrpantiportershave pages 2-4
25. ito2017mrpantiportershave pages 9-10
26. ito2017mrpantiportershave pages 4-5
27. https://doi.org/10.1038/nrmicro2549
28. https://doi.org/10.3389/fmicb.2020.556140
29. https://doi.org/10.3389/fmicb.2022.1034164
30. https://doi.org/10.3389/fmicb.2017.02325
31. https://doi.org/10.1128/aem.00569-24
32. https://doi.org/10.3389/fmicb.2017.00206
33. https://doi.org/10.3389/fmicb.2021.651744
34. https://doi.org/10.1126/sciadv.adf8998
35. https://doi.org/10.1093/femsre/fuad062
36. https://doi.org/10.1038/nrmicro2549,
37. https://doi.org/10.1126/sciadv.adf8998,
38. https://doi.org/10.3389/fmicb.2021.651744,
39. https://doi.org/10.3389/fmicb.2022.1034164,
40. https://doi.org/10.1093/femsre/fuad062,
41. https://doi.org/10.1128/aem.00569-24,
42. https://doi.org/10.3389/fmicb.2017.02325,
43. https://doi.org/10.3389/fmicb.2020.556140,