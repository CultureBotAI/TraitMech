# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gas vesicle
- **METPO identifier:** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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
**Generated:** 2026-06-18T08:03:47.583739

1. hurt2024directedevolutionof pages 1-3
2. feng2024advancesinthe pages 4-5
3. yang2024rapidflotationof pages 1-2
4. feng2024advancesinthe pages 2-4
5. iburg2024elucidatingtheassembly pages 1-2
6. feng2024advancesinthe pages 9-10
7. liu2024characterizationandcomparison pages 1-2
8. jazbec2024proteingasvesicles pages 5-6
9. jazbec2024proteingasvesicles pages 1-3
10. iburg2024elucidatingtheassembly pages 2-4
11. chen2013thebacterialcarbonfixing pages 1-2
12. https://doi.org/10.1038/s44318-024-00178-2
13. https://doi.org/10.1186/s13036-024-00426-3
14. https://doi.org/10.1021/acsnano.4c01498
15. https://doi.org/10.1021/acssynbio.4c00283
16. https://doi.org/10.1002/btm2.10584
17. https://doi.org/10.3390/ph17060755
18. https://doi.org/10.1371/journal.pone.0076127
19. https://doi.org/10.1159/000351625
20. https://doi.org/10.1038/s44318-024-00178-2,
21. https://doi.org/10.1186/s13036-024-00426-3,
22. https://doi.org/10.1021/acssynbio.4c00283,
23. https://doi.org/10.1021/acsnano.4c01498,
24. https://doi.org/10.3389/fpls.2024.1367680,
25. https://doi.org/10.1371/journal.pone.0076127,
26. https://doi.org/10.1159/000351625,
27. https://doi.org/10.1002/btm2.10584,
28. https://doi.org/10.3390/ph17060755,