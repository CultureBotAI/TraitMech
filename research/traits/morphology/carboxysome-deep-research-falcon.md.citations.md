# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxysome
- **METPO identifier:** traitmech:000072
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A bacterial microcompartment — a polyhedral protein-shelled organelle that encapsulates RuBisCO and carbonic anhydrase to concentrate CO2 for carbon fixation in cyanobacteria and many chemoautotrophs.
- **Parent traits:** traitmech:000066
- **Synonyms:** bacterial microcompartment
- **Existing evidence:** DOI:10.1038/nrmicro.2018.10:  (Kerfeld et al. review bacterial microcompartments; the carboxysome is the archetypal protein-shelled CO2-fixing microcompartment.) | DOI:10.1038/nrmicro1913:  (Yeates et al. describe protein-based organelles in bacteria (carboxysomes and related microcompartments), including the carboxysome shell and its encapsulated enzymes.)
- **Existing causal graph summary:** carboxysome_co2_concentrating: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **carboxysome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carboxysome.yaml`.

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
**Generated:** 2026-06-18T06:42:17.169435

1. kerfeld2018bacterialmicrocompartments pages 1-2
2. trettel2024modelingbacterialmicrocompartment pages 2-3
3. wieschollek2024anewtype pages 1-2
4. trettel2024modelingbacterialmicrocompartment pages 5-6
5. li2024nanoengineeringcarboxysomeshells pages 1-3
6. doron2024bacterialmicrocompartmentsas pages 7-8
7. doron2024towardsusingbacterial pages 5-6
8. cheng2024molecularinteractionsof pages 3-5
9. doron2024bacterialmicrocompartmentsas pages 5-7
10. kerfeld2018bacterialmicrocompartments pages 4-5
11. kerfeld2018bacterialmicrocompartments pages 2-3
12. cheng2024molecularinteractionsof pages 1-2
13. cheng2024molecularinteractionsof pages 10-10
14. doron2024bacterialmicrocompartmentsas pages 1-3
15. doron2024bacterialmicrocompartmentsas pages 10-12
16. IV
17. label-only
18. CHEBI:16526
19. EC:4.2.1.1
20. CHEBI:17544
21. GO:0015701 candidate
22. METPO:traitmech:000072
23. CHEBI candidate label-only
24. CHEBI:15379
25. EC:4.1.1.39
26. GO:0016984 candidate
27. BMC-H/T/P label set
28. label-only; BMC-P family
29. GO candidate label-only
30. CsoS1A/CsoS4A label-only
31. CHEBI:25212
32. CHEBI:22563
33. CHEBI:17996
34. ENVO low CO2 label-only
35. ENVO elevated CO2 label-only
36. PR:000000001
37. CHEBI:16236
38. CHEBI:18276
39. https://doi.org/10.1038/nrmicro.2018.10
40. https://doi.org/10.1128/aem.01075-24
41. https://doi.org/10.3389/fpls.2024.1346759
42. https://doi.org/10.1093/plphys/kiae438
43. https://doi.org/10.1038/s41467-023-41211-y
44. https://doi.org/10.1042/bst20230229
45. https://doi.org/10.3389/fbioe.2024.1344260
46. https://doi.org/10.1021/acsnano.3c11559
47. https://doi.org/10.1038/nrmicro.2018.10,
48. https://doi.org/10.1128/aem.01075-24,
49. https://doi.org/10.1093/plphys/kiae438,
50. https://doi.org/10.3389/fpls.2024.1346759,
51. https://doi.org/10.1038/s41467-023-41211-y,
52. https://doi.org/10.1021/acsnano.3c11559,
53. https://doi.org/10.1042/bst20230229,
54. https://doi.org/10.3389/fbioe.2024.1344260,