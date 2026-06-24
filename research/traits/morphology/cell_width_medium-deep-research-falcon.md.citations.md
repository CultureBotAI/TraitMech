# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width medium
- **METPO identifier:** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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
**Generated:** 2026-06-18T07:21:59.987634

1. ago2023relationshipbetweenthe pages 1-3
2. micelli2023aconservedzincbinding pages 1-2
3. shlosman2023allostericactivationof pages 1-2
4. gilman2024mrecmredstructurereveals pages 1-2
5. zhang2023coordinatedpeptidoglycansynthases pages 1-2
6. dersch2024adaptationofbacillus pages 1-2
7. middlemiss2023moleculartugofwarregulatesa pages 92-96
8. middlemiss2023moleculartugofwarregulates pages 92-96
9. middlemiss2023moleculartugofwarregulates pages 19-23
10. blank
11. https://doi.org/10.1038/s41467-023-39037-9
12. https://doi.org/10.1002/mbo3.1385
13. https://doi.org/10.1101/2024.10.08.617240
14. https://doi.org/10.1038/s41467-023-41082-3
15. https://doi.org/10.1101/2024.11.22.624946
16. https://doi.org/10.3390/microorganisms12071309
17. https://doi.org/10.1073/pnas.2215237120
18. https://doi.org/10.1101/2024.11.22.624946,
19. https://doi.org/10.1038/s41467-023-39037-9,
20. https://doi.org/10.1038/s41467-023-41082-3,
21. https://doi.org/10.1002/mbo3.1385,
22. https://doi.org/10.1073/pnas.2215237120,
23. https://doi.org/10.1101/2024.10.08.617240,
24. https://doi.org/10.3390/microorganisms12071309,