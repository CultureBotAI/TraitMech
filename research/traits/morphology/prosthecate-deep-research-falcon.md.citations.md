# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prosthecate
- **METPO identifier:** traitmech:000065
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell bears one or more prosthecae — tubular extensions of the cell envelope (stalks) — that increase nutrient-uptake surface area or mediate attachment, as in Caulobacter.
- **Parent traits:** METPO:1000059
- **Synonyms:** stalked, prostheca
- **Existing evidence:** DOI:10.1111/j.1365-2958.2007.05633.x:  (Wagner & Brun describe the Caulobacter stalk (prostheca) as a cell-envelope extension and a specialized form of cell elongation aiding nutrient uptake.) | DOI:10.1128/MMBR.00040-09:  (Curtis & Brun's review of Caulobacter development supports the stalk as a regulated developmental appendage.)
- **Existing causal graph summary:** prosthecate_stalk_nutrient_uptake: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **prosthecate** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/prosthecate.yaml`.

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
**Generated:** 2026-06-18T09:22:26.837775

1. hallgren2023phosphatestarvationdecouples pages 1-2
2. richter2023interactingbactofilinsimpact pages 13-15
3. barrows2023synchronizedswarmersand pages 11-13
4. billini2024thecytoplasmicphosphate pages 4-5
5. north2023thecaulobacterntrbntrc pages 16-18
6. richter2023interactingbactofilinsimpact pages 15-16
7. barrows2023synchronizedswarmersand pages 9-11
8. https://doi.org/10.1371/journal.pgen.1010882
9. https://doi.org/10.1038/s42003-024-06469-y
10. https://doi.org/10.1128/jb.00181-23
11. https://doi.org/10.1128/jb.00384-22
12. https://doi.org/10.1371/journal.pgen.1010788
13. https://doi.org/10.1371/journal.pgen.1010882,
14. https://doi.org/10.1371/journal.pgen.1010788,
15. https://doi.org/10.1128/jb.00384-22,
16. https://doi.org/10.1038/s42003-024-06469-y,
17. https://doi.org/10.1128/jb.00181-23,