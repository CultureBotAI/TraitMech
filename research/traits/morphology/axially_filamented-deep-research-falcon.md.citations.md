# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** axially filamented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000705
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility where the flagellum filament of an organism is located in the periplasm and does not extend past the cell envelope.
- **Parent traits:** METPO:1000702
- **Synonyms:** axial filament
- **Existing evidence:** DOI:10.3390/biom10040550: flagella are hidden within the periplasmic space (Supports axial/periplasmic flagella as the defining motility structure.)
- **Existing causal graph summary:** axially_filamented_periplasmic_flagella: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **axially filamented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/axially_filamented.yaml`.

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
**Generated:** 2026-08-04T07:23:53.100901

1. nakamura2020spirocheteflagellaand pages 1-3
2. ribardo2024viscositydependentdeterminantsof pages 1-2
3. nakamura2020spirocheteflagellaand pages 3-5
4. chang2019structuralinsightsinto pages 10-12
5. nakamura2020spirocheteflagellaand pages 9-11
6. 10.3390/biom10040550
7. 10.7554/eLife.48979
8. 10.1016/j.tim.2022.09.010
9. 10.1128/jb.00463-22
10. 10.1128/mbio.02544-23
11. https://doi.org/10.3390/biom10040550
12. https://doi.org/10.7554/eLife.48979
13. https://doi.org/10.1016/j.tim.2022.09.010
14. https://doi.org/10.1128/jb.00463-22
15. https://doi.org/10.1128/mbio.02544-23
16. https://doi.org/10.3390/biom10040550,
17. https://doi.org/10.7554/elife.48979,
18. https://doi.org/10.1128/mbio.02544-23,