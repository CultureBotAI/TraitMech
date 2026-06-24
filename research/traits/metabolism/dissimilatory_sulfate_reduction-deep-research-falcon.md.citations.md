# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory sulfate reduction
- **METPO identifier:** traitmech:000105
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism uses sulfate as the terminal electron acceptor, reducing it to hydrogen sulfide while oxidizing organic matter or hydrogen for energy.
- **Parent traits:** METPO:1000802
- **Synonyms:** sulfate respiration
- **Existing evidence:** DOI:10.1038/nrmicro1892:  (Muyzer & Stams review sulfate-reducing bacteria, which respire sulfate to sulfide in anoxic habitats.) | DOI:10.3389/fmicb.2011.00081:  (Plugge et al. review the metabolic flexibility of sulfate-reducing bacteria.)
- **Existing causal graph summary:** sulfate_reduction_to_sulfide: 4 nodes, 2 edges

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
**Generated:** 2026-06-18T05:12:30.801236

1. fan2023recentadvancesin pages 5-6
2. diao2023globaldiversityand pages 2-3
3. ferreira2023unravelingthemetabolic pages 20-24
4. neukirchen2023stepwisepathwayfor pages 2-3
5. bernardino2023elucidatingthephysiological pages 32-33
6. yan2023insightsintoremediation pages 1-2
7. sun2023biomineralizationtoprevent pages 1-2
8. diao2023globaldiversityand pages 1-2
9. neukirchen2023stepwisepathwayfor pages 1-2
10. demin2024sulfatereducingbacteriaunearthed pages 8-10
11. yang2023harnessingsulfatereducingbacteria pages 1-2
12. klier2024evolutionaryhistoryand pages 1-2
13. diao2023globaldiversityand pages 3-4
14. 4Fe-4S
15. https://doi.org/10.3390/antiox12030767.
16. https://doi.org/10.1038/s41396-023-01477-y.
17. https://doi.org/10.1093/femsre/fuad058.
18. https://doi.org/10.1021/acs.est.3c04680.
19. https://doi.org/10.3389/fmicb.2023.1050635.
20. https://doi.org/10.1093/femsre/fuad058
21. https://doi.org/10.1038/s41396-023-01477-y
22. https://doi.org/10.3390/antiox12030767
23. https://doi.org/10.3389/fmicb.2023.1050635
24. https://doi.org/10.1021/acs.est.3c04680
25. https://doi.org/10.3389/fmicb.2023.1306573
26. https://doi.org/10.1128/aem.01390-23
27. https://doi.org/10.1093/ismejo/wrae167
28. https://doi.org/10.1038/s41396-023-01477-y,
29. https://doi.org/10.1093/femsre/fuad058,
30. https://doi.org/10.3390/antiox12030767,
31. https://doi.org/10.3389/fmicb.2023.1050635,
32. https://doi.org/10.1021/acs.est.3c04680,
33. https://doi.org/10.1128/aem.01390-23,
34. https://doi.org/10.3389/fmicb.2023.1306573,
35. https://doi.org/10.1093/ismejo/wrae167,