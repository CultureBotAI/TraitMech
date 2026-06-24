# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metabolism
- **METPO identifier:** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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
**Generated:** 2026-06-18T05:26:34.157165

1. marschmann2024predictionsofrhizosphere pages 1-2
2. he2024emergingmultiscaleinsights pages 1-2
3. williams2024mappingthemetabolic pages 17-22
4. williams2024mappingthemetabolic pages 22-26
5. althaher2023anoverviewof pages 1-2
6. jin2023syntrophicpropionateoxidation pages 1-2
7. williams2024mappingthemetabolic pages 40-43
8. robainaestevez2024applicationsofmarine pages 1-2
9. shiroma2024enteropathwaythemetabolic pages 1-2
10. ardalani2024pangenomereconstructionof pages 1-3
11. majzoub2024refiningmicrobialcommunity pages 1-2
12. carter2024applicationsofgenomescale pages 1-1
13. carter2024applicationsofgenomescale pages 1-2
14. carter2024applicationsofgenomescale pages 6-7
15. marschmann2024predictionsofrhizosphere pages 2-3
16. https://doi.org/10.1016/j.heliyon.2023.e22459
17. https://doi.org/10.1128/aem.00384-23
18. https://doi.org/10.1038/s41467-024-52160-5
19. https://doi.org/10.1038/s41564-023-01582-w
20. https://doi.org/10.1038/s41467-024-46374-w
21. https://doi.org/10.1371/journal.pstr.0000145
22. https://doi.org/10.1128/msystems.00746-24
23. https://doi.org/10.1093/bib/bbae419
24. https://doi.org/10.1128/msystems.00156-24
25. https://doi.org/10.1093/bib/bbad439
26. https://doi.org/10.1016/j.heliyon.2023.e22459,
27. https://doi.org/10.1038/s41564-023-01582-w,
28. https://doi.org/10.1038/s41467-024-52160-5,
29. https://doi.org/10.1128/aem.00384-23,
30. https://doi.org/10.1093/bib/bbad439,
31. https://doi.org/10.1371/journal.pstr.0000145,
32. https://doi.org/10.1093/bib/bbae419,
33. https://doi.org/10.1128/msystems.00156-24,
34. https://doi.org/10.1128/msystems.00746-24,
35. https://doi.org/10.1038/s41467-024-46374-w,