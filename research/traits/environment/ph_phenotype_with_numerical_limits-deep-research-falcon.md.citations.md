# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH phenotype with numerical limits
- **METPO identifier:** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 5 nodes, 4 edges

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
**Generated:** 2026-06-18T00:46:00.463795

1. poolman2023physicochemicalhomeostasisin pages 1-2
2. li2024responseofescherichia pages 1-2
3. rekadwad2023extremophilesthespecies pages 8-10
4. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7
5. poolman2023physicochemicalhomeostasisin pages 2-4
6. li2024responseofescherichia pages 2-4
7. ramoneda2023buildingagenomebased pages 3-5
8. qin2024characterizationofmild pages 1-2
9. jiang2024exogenousputrescineplays pages 1-2
10. atasoy2024exploitationofmicrobial pages 10-11
11. yao2023howmethanotrophsrespond pages 5-7
12. atasoy2024exploitationofmicrobial pages 5-6
13. atasoy2024exploitationofmicrobial pages 2-3
14. https://doi.org/10.1093/femsre/fuad033
15. https://doi.org/10.1111/1758-2229.70019
16. https://doi.org/10.3390/microorganisms12091774
17. https://doi.org/10.1126/sciadv.adf8998
18. https://doi.org/10.3389/fmicb.2022.1034164
19. https://doi.org/10.1128/aem.00569-24
20. https://doi.org/10.3390/jof9060652
21. https://doi.org/10.1007/s13205-023-03733-6
22. https://doi.org/10.3390/microorganisms12081565
23. https://doi.org/10.1093/femsre/fuad062
24. https://doi.org/10.1093/femsre/fuad033,
25. https://doi.org/10.3390/microorganisms12091774,
26. https://doi.org/10.1007/s13205-023-03733-6,
27. https://doi.org/10.3390/jof9060652,
28. https://doi.org/10.1111/1758-2229.70019,
29. https://doi.org/10.1126/sciadv.adf8998,
30. https://doi.org/10.3390/microorganisms12081565,
31. https://doi.org/10.1128/aem.00569-24,
32. https://doi.org/10.1093/femsre/fuad062,
33. https://doi.org/10.3389/fmicb.2022.1034164,