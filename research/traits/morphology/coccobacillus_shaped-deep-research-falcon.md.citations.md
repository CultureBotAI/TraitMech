# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccobacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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
**Generated:** 2026-08-04T08:03:34.562834

1. micelli2023aconservedzincbinding pages 4-6
2. slovak2005localizationofmreb pages 1-2
3. slovak2005localizationofmreb pages 7-10
4. micelli2023aconservedzincbinding pages 7-8
5. caccamo2018themolecularbasis pages 7-9
6. micelli2023aconservedzincbinding pages 1-2
7. micelli2023aconservedzincbinding pages 6-7
8. mechanistic synthesis; uncertain as a universal edge
9. 10.1073/pnas.2215237120
10. 10.1128/JB.187.1.54-64.2005
11. 10.1016/j.tim.2017.09.012
12. https://doi.org/10.1073/pnas.2215237120
13. https://doi.org/10.1128/JB.187.1.54-64.2005
14. https://doi.org/10.1016/j.tim.2017.09.012
15. https://doi.org/10.1128/jb.187.1.54-64.2005,
16. https://doi.org/10.1073/pnas.2215237120,
17. https://doi.org/10.1016/j.tim.2017.09.012,