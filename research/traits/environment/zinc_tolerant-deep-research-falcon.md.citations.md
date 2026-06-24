# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** zinc tolerant
- **METPO identifier:** traitmech:000014
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc to a MIC of 20 mM.)
- **Existing causal graph summary:** zinc_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **zinc tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/zinc_tolerant.yaml`.

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
**Generated:** 2026-06-18T03:05:44.515005

1. nies2024aflowequilibrium pages 1-3
2. pagnucco2023metaltoleranceand pages 2-3
3. schulz2024theeffluxsystem pages 9-12
4. nies2024aflowequilibrium pages 20-22
5. pagnucco2023metaltoleranceand pages 9-10
6. schulz2024theeffluxsystem pages 1-3
7. schulz2024theeffluxsystem pages 12-14
8. pagnucco2023metaltoleranceand pages 3-4
9. dong2024bacterialmetalion pages 12-14
10. schulz2024theeffluxsystem pages 14-15
11. pagnucco2023metaltoleranceand pages 1-2
12. https://doi.org/10.1128/jb.00080-24;
13. https://doi.org/10.1128/jb.00299-24;
14. https://doi.org/10.3389/fmicb.2023.1278886
15. https://doi.org/10.1128/jb.00080-24
16. https://doi.org/10.1128/jb.00299-24
17. https://doi.org/10.13343/j.cnki.wsxb.20230561
18. https://doi.org/10.1128/jb.00395-23;
19. https://doi.org/10.1093/mtomcs/mfae058
20. https://doi.org/10.1128/jb.00395-23
21. https://doi.org/10.1128/jb.00080-24,
22. https://doi.org/10.1128/jb.00299-24,
23. https://doi.org/10.3389/fmicb.2023.1278886,
24. https://doi.org/10.13343/j.cnki.wsxb.20230561,