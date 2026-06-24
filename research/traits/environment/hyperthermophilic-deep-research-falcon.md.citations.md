# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hyperthermophilic
- **METPO identifier:** METPO:1000617
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at very high temperatures, typically ≥80 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme thermophilic
- **Existing evidence:** DOI:10.1111/j.1574-6976.1996.tb00233.x: optimal growth temperatures between 80°C and 110°C (Supports hyperthermophile growth at very high temperatures.) | PMID:9348040: hyperthermophilic archaeon, Pyrococcus furiosus (Organism example: Pyrococcus furiosus is described as hyperthermophilic.)
- **Existing causal graph summary:** hyperthermophilic_thermostability: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/hyperthermophilic.yaml`.

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
**Generated:** 2026-06-17T22:42:41.670145

1. rekadwad2023extremophilesthespecies pages 2-4
2. baes2023transcriptionalandtranslational pages 1-2
3. grunberger2023uncoveringthetemporal pages 1-2
4. grunberger2023uncoveringthetemporal pages 10-12
5. taubner2023lipidomicsandcomparative pages 11-12
6. garcia2024identificationoftwo pages 6-7
7. garcia2024identificationoftwo pages 1-2
8. rose2023structuralcharacterizationof pages 1-2
9. li2024biosynthesisofgmgt pages 2-3
10. li2024biosynthesisofgmgt pages 1-2
11. rose2023structuralcharacterizationof pages 2-4
12. with
13. https://doi.org/10.1007/s13205-023-03733-6,
14. https://doi.org/10.1128/mbio.02174-23,
15. https://doi.org/10.1128/mbio.03593-22,
16. https://doi.org/10.3389/fmicb.2023.1267570,
17. https://doi.org/10.1038/s41467-024-49650-x,
18. https://doi.org/10.1073/pnas.2318761121,
19. https://doi.org/10.1128/msystems.01159-22,
20. https://doi.org/10.1007/s13205-023-03733-6
21. https://doi.org/10.1128/mbio.02174-23
22. https://doi.org/10.1128/mbio.03593-22
23. https://doi.org/10.3389/fmicb.2023.1267570
24. https://doi.org/10.1128/msystems.01159-22
25. https://doi.org/10.1038/s41467-024-49650-x
26. https://doi.org/10.1073/pnas.2318761121