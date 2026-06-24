# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organoheterotrophic
- **METPO identifier:** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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
**Generated:** 2026-06-18T12:12:27.772206

1. slowinski2019bioenergeticsofmixotrophic pages 11-15
2. slowinski2019bioenergeticsofmixotrophic pages 32-37
3. mujakic2023multienvironmentecogenomicsanalysis pages 1-2
4. slowinski2019bioenergeticsofmixotrophic pages 15-21
5. liu2023isolationandgenomics pages 13-15
6. tothero2024leptothrixochraceagenomes pages 9-13
7. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
8. liu2023isolationandgenomics pages 8-10
9. tothero2024leptothrixochraceagenomes pages 1-2
10. gutierrezpreciado2024extremelyacidicproteomes pages 7-9
11. tothero2024leptothrixochraceagenomes pages 15-16
12. liu2023isolationandgenomics pages 7-8
13. tothero2024leptothrixochraceagenomes pages 13-15
14. liu2023isolationandgenomics pages 10-13
15. liu2023isolationandgenomics pages 15-17
16. slowinski2019bioenergeticsofmixotrophic pages 27-32
17. slowinski2019bioenergeticsofmixotrophic pages 21-27
18. slowinski2019bioenergeticsofmixotrophic pages 1-7
19. are
20. https://doi.org/10.1128/spectrum.04110-22
21. https://doi.org/10.1128/aem.00599-24
22. https://doi.org/10.1038/s41559-024-02505-6
23. https://doi.org/10.1128/spectrum.01112-23
24. https://doi.org/10.1128/spectrum.01112-23,
25. https://doi.org/10.1128/aem.00599-24,
26. https://doi.org/10.1128/spectrum.04110-22,
27. https://doi.org/10.1038/s41559-024-02505-6,