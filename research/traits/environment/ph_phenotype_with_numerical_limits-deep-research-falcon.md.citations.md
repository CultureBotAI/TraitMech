# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **pH phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_phenotype_with_numerical_limits.yaml`.

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
**Generated:** 2026-08-04T02:55:04.933942

1. sanchezclemente2020carbonsourceinfluence pages 1-3
2. barnum2024predictingmicrobialgrowth pages 14-16
3. krulwich2011molecularaspectsof pages 1-3
4. krulwich2011molecularaspectsof pages 5-6
5. krulwich2011molecularaspectsof pages 12-14
6. yao2023howmethanotrophsrespond pages 5-7
7. jiang2024exogenousputrescineplays pages 12-14
8. goto2022differencesinbioenergetic pages 1-2
9. atasoy2024exploitationofmicrobial pages 2-3
10. ramoneda2024leveraginggenomicinformation pages 1-2
11. krulwich2011molecularaspectsof pages 3-5
12. krulwich2011molecularaspectsof pages 22-23
13. yao2023howmethanotrophsrespond pages 1-2
14. 10.1038/nrmicro2549
15. 10.1186/s13068-018-1095-y
16. 10.3389/fmicb.2022.842785
17. 10.3389/fmicb.2022.1034164
18. 10.1093/ismejo/wrae195
19. 10.1128/aem.00569-24
20. 10.1093/femsre/fuad062
21. 10.1101/2024.03.22.586313
22. 10.3390/genes11111292
23. https://doi.org/10.1038/nrmicro2549
24. https://doi.org/10.1186/s13068-018-1095-y
25. https://doi.org/10.3389/fmicb.2022.842785
26. https://doi.org/10.3389/fmicb.2022.1034164
27. https://doi.org/10.1093/ismejo/wrae195
28. https://doi.org/10.1128/aem.00569-24
29. https://doi.org/10.1093/femsre/fuad062
30. https://doi.org/10.1101/2024.03.22.586313
31. https://doi.org/10.3390/genes11111292
32. https://doi.org/10.1038/nrmicro2549,
33. https://doi.org/10.3390/genes11111292,
34. https://doi.org/10.1101/2024.03.22.586313,
35. https://doi.org/10.1186/s13068-018-1095-y,
36. https://doi.org/10.3389/fmicb.2022.842785,
37. https://doi.org/10.3389/fmicb.2022.1034164,
38. https://doi.org/10.1128/aem.00569-24,
39. https://doi.org/10.1093/femsre/fuad062,
40. https://doi.org/10.1093/ismejo/wrae195,