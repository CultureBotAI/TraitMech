# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anoxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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
**Generated:** 2026-08-04T05:39:29.297384

1. martin2018aphysiologicalperspective pages 2-3
2. kushkevych2021anoxygenicphotosynthesisin pages 3-5
3. niederman2024whatweare pages 1-2
4. alarcon2024evidenceforautotrophic pages 1-2
5. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
6. kushkevych2021anoxygenicphotosynthesisin pages 2-3
7. kushkevych2021anoxygenicphotosynthesisin pages 1-2
8. niederman2024whatweare pages 5-7
9. niederman2024whatweare pages 7-9
10. 4Fe–4S
11. 4Fe-4S
12. 10.3390/antiox10060829
13. 10.3389/fmicb.2024.1417714
14. 10.3390/biom14030311
15. 10.1128/aem.00863-24
16. 10.3390/microorganisms7110576
17. 10.1093/femsre/fux056
18. https://doi.org/10.3390/antiox10060829
19. https://doi.org/10.3389/fmicb.2024.1417714
20. https://doi.org/10.3390/biom14030311
21. https://doi.org/10.1128/aem.00863-24
22. https://doi.org/10.3390/microorganisms7110576
23. https://doi.org/10.1093/femsre/fux056
24. https://doi.org/10.3390/antiox10060829,
25. https://doi.org/10.1093/femsre/fux056,
26. https://doi.org/10.3390/biom14030311,
27. https://doi.org/10.1128/aem.00863-24,
28. https://doi.org/10.3389/fmicb.2024.1417714,