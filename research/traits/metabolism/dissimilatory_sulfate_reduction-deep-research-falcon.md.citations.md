# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory sulfate reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **dissimilatory sulfate reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_sulfate_reduction.yaml`.

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
**Generated:** 2026-08-04T06:16:15.850902

1. neukirchen2023stepwisepathwayfor pages 8-9
2. diao2023globaldiversityand pages 1-2
3. neukirchen2023stepwisepathwayfor pages 2-3
4. sim2023whatcontrolsthe pages 1-2
5. klier2024evolutionaryhistoryand pages 1-2
6. diao2023globaldiversityand pages 3-4
7. klier2024evolutionaryhistoryand pages 12-13
8. liu2024enrichmentofacidtolerant pages 1-2
9. sim2023whatcontrolsthe pages 3-5
10. sim2023whatcontrolsthe pages 6-7
11. neukirchen2023stepwisepathwayfor pages 11-12
12. liu2024enrichmentofacidtolerant pages 2-3
13. 10.1021/acsenvironau.2c00059
14. 10.1093/ismejo/wrae167
15. 10.1038/s41396-023-01477-y
16. 10.1093/femsre/fuad058
17. 10.1073/pnas.2313650121
18. 10.3389/fmicb.2024.1475137
19. 10.1073/pnas.2220725120
20. 10.1038/s41467-023-42074-z
21. 10.1186/s40168-024-01909-7
22. 10.3389/fmicb.2018.00309
23. 10.1038/s41396-018-0077-1
24. 10.1038/nrmicro1892
25. 10.3389/fmicb.2011.00081
26. https://doi.org/10.1021/acsenvironau.2c00059
27. https://doi.org/10.1093/ismejo/wrae167
28. https://doi.org/10.1038/s41396-023-01477-y
29. https://doi.org/10.1093/femsre/fuad058
30. https://doi.org/10.1073/pnas.2313650121
31. https://doi.org/10.3389/fmicb.2024.1475137
32. https://doi.org/10.1073/pnas.2220725120
33. https://doi.org/10.1038/s41467-023-42074-z
34. https://doi.org/10.1186/s40168-024-01909-7
35. https://doi.org/10.3389/fmicb.2018.00309
36. https://doi.org/10.1038/s41396-018-0077-1
37. https://doi.org/10.1038/nrmicro1892
38. https://doi.org/10.3389/fmicb.2011.00081
39. https://doi.org/10.1021/acsenvironau.2c00059,
40. https://doi.org/10.1093/femsre/fuad058,
41. https://doi.org/10.1093/ismejo/wrae167,
42. https://doi.org/10.1038/s41396-023-01477-y,
43. https://doi.org/10.3389/fmicb.2024.1475137,