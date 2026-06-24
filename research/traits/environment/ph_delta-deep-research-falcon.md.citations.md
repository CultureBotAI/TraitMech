# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta
- **METPO identifier:** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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
**Generated:** 2026-06-18T00:18:40.722342

1. qin2024characterizationofmild pages 1-2
2. ianutsevich2023theroleof pages 1-2
3. poolman2023physicochemicalhomeostasisin pages 1-2
4. ianutsevich2023theroleof pages 4-5
5. li2024responseofescherichia pages 10-12
6. jong2024quantitativeproteomicsreveals pages 6-8
7. ramoneda2023buildingagenomebased pages 3-5
8. li2024responseofescherichia pages 5-7
9. jiang2024exogenousputrescineplays pages 9-12
10. zheng2024heterologousexpressionof pages 1-2
11. li2024responseofescherichia pages 1-2
12. yao2023howmethanotrophsrespond pages 5-7
13. jiang2024exogenousputrescineplays pages 1-2
14. qin2024characterizationofmild pages 13-14
15. kim2024lineagespecificevolutionof pages 2-4
16. qin2024characterizationofmild pages 2-3
17. palmer2024dynamicevolutionof pages 1-5
18. zhang2023transcriptomeanalysisreveals pages 7-10
19. zhang2023transcriptomeanalysisreveals pages 13-14
20. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2
21. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7
22. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 2-4
23. https://doi.org/10.1093/femsre/fuad033
24. https://doi.org/10.1128/AEM.00569-24
25. https://doi.org/10.1126/sciadv.adf8998
26. https://doi.org/10.3389/fmicb.2024.1468929
27. https://doi.org/10.3389/fmicb.2022.1034164
28. https://doi.org/10.3390/microorganisms11071733
29. https://doi.org/10.3390/microorganisms12091774
30. https://doi.org/10.3390/microorganisms12081565
31. https://doi.org/10.3390/jof9060652
32. https://doi.org/10.1128/AEM.02091-23
33. https://doi.org/10.1128/mbio.03535-22
34. https://doi.org/10.1128/aem.00569-24
35. https://doi.org/10.21203/rs.3.rs-4032669/v1
36. https://doi.org/10.3389/fmicb.2022.1034164,
37. https://doi.org/10.3390/microorganisms12081565,
38. https://doi.org/10.3390/microorganisms11071733,
39. https://doi.org/10.1093/femsre/fuad033,
40. https://doi.org/10.1128/aem.00569-24,
41. https://doi.org/10.3389/fmicb.2024.1468929,
42. https://doi.org/10.3390/microorganisms12091774,
43. https://doi.org/10.3390/ijms242216103,
44. https://doi.org/10.1128/aem.02091-23,
45. https://doi.org/10.1126/sciadv.adf8998,
46. https://doi.org/10.3390/jof9060652,
47. https://doi.org/10.1186/s12866-024-03498-9,
48. https://doi.org/10.21203/rs.3.rs-4032669/v1,