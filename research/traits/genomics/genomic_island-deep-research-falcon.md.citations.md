# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genomic island
- **METPO identifier:** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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
**Generated:** 2026-06-18T03:33:59.769254

1. audrey2023asystematicapproach pages 2-3
2. audrey2023asystematicapproach pages 1-2
3. lyu2024theintricaterelationship pages 1-2
4. audrey2023asystematicapproach pages 3-5
5. pons2023conjugativeinccplasmid pages 2-4
6. vizzarro2024vibriocholeraepathogenicity pages 1-2
7. vizzarro2024vibriocholeraepathogenicity pages 2-5
8. picorodriguez2024effectofsalmonella pages 1-2
9. picorodriguez2024effectofsalmonella pages 2-4
10. botelho2023defensesystemsare pages 1-2
11. kushwaha2024comprehensiveblueprintof pages 1-2
12. lyu2024theintricaterelationship pages 4-6
13. lyu2024theintricaterelationship pages 6-7
14. https://doi.org/10.1093/nar/gkad644
15. https://doi.org/10.1128/spectrum.02201-22
16. https://doi.org/10.1128/jb.00145-24
17. https://doi.org/10.1007/s11259-023-10185-z
18. https://doi.org/10.3389/fvets.2024.1401392
19. https://doi.org/10.1093/nar/gkad282
20. https://doi.org/10.7554/elife.91985.3
21. https://doi.org/10.1371/journal.pbio.3002746
22. https://doi.org/10.1093/nar/gkad644,
23. https://doi.org/10.7554/elife.91985.3,
24. https://doi.org/10.1128/spectrum.02201-22,
25. https://doi.org/10.1007/s11259-023-10185-z,
26. https://doi.org/10.3389/fvets.2024.1401392,
27. https://doi.org/10.1128/jb.00145-24,
28. https://doi.org/10.1093/nar/gkad282,
29. https://doi.org/10.1371/journal.pbio.3002746,