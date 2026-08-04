# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mercury tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000016
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of toxic inorganic or organic mercury compounds, typically via the mer operon, whose mercuric reductase (MerA) reduces reactive Hg(II) to volatile Hg(0).
- **Parent traits:** traitmech:000012
- **Synonyms:** mercury resistant
- **Existing evidence:** DOI:10.1016/S0168-6445(03)00046-9: Bacterial resistance to inorganic and organic mercury compounds (HgR) is one of the most widely observed phenotypes in eubacteria (Review supports mercury resistance as a widespread bacterial phenotype mediated by MerA, "that reduces reactive ionic Hg(II) to volatile, relatively inert, monoatomic Hg(0) vapor".) | PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Heavy-metal resistance review situates mercury detoxification within the broader prokaryotic metal-resistance machinery.)
- **Existing causal graph summary:** mercury_tolerance_mer_reduction: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **mercury tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mercury_tolerant.yaml`.

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
**Generated:** 2026-08-04T01:08:02.724456

1. barkay2003bacterialmercuryresistance pages 8-10
2. barkay2003bacterialmercuryresistance pages 1-2
3. tiodar2024plantcolonizersof pages 1-2
4. barkay2003bacterialmercuryresistance pages 21-22
5. tiodar2024plantcolonizersof pages 16-17
6. barkay2003bacterialmercuryresistance pages 5-7
7. barkay2003bacterialmercuryresistance pages 2-4
8. tiodar2024plantcolonizersof pages 11-13
9. tiodar2024plantcolonizersof pages 2-4
10. 10.1016/S0168-6445(03)00046-9
11. 10.1016/S0168-6445(03)00051-2
12. 10.1128/msystems.00736-22
13. 10.1007/s11104-024-06552-7
14. 10.3390/applmicrobiol4040111
15. 10.3390/microorganisms12101945
16. https://doi.org/10.1016/S0168-6445(03
17. https://doi.org/10.1128/msystems.00736-22
18. https://doi.org/10.1007/s11104-024-06552-7
19. https://doi.org/10.3390/applmicrobiol4040111
20. https://doi.org/10.3390/microorganisms12101945
21. https://doi.org/10.1016/s0168-6445(03
22. https://doi.org/10.1128/msystems.00736-22,
23. https://doi.org/10.1007/s11104-024-06552-7,