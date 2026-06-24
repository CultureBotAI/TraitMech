# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** bioluminescence
- **METPO identifier:** traitmech:000085
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capability to emit visible light through a luciferase-catalyzed reaction, frequently regulated by quorum sensing in marine bacteria such as Aliivibrio and Photobacterium.
- **Parent traits:** METPO:1000059
- **Synonyms:** luminescent
- **Existing evidence:** DOI:10.1016/j.csbj.2018.11.003:  (Brodl, Winkler & Macheroux review the molecular mechanisms of bacterial bioluminescence and the luciferase reaction.) | DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler support quorum-sensing regulation of light production in luminous bacteria.)
- **Existing causal graph summary:** bioluminescence_luciferase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **bioluminescence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/bioluminescence.yaml`.

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
**Generated:** 2026-06-18T11:01:16.106495

1. tinikul2020bacterialluciferasemolecular pages 1-4
2. brodl2018molecularmechanismsof pages 5-8
3. septer2024lightingtheway pages 3-5
4. waters2005quorumsensingcelltocell pages 9-11
5. farkas2024bioluminescentpseudomonasaeruginosa pages 7-9
6. kim2024bioluminescentsystemsfor pages 3-4
7. brodl2018molecularmechanismsof pages 1-5
8. farkas2024bioluminescentpseudomonasaeruginosa pages 1-2
9. https://doi.org/10.1016/j.csbj.2018.11.003
10. https://doi.org/10.1128/jb.00035-24
11. https://doi.org/10.1038/s41598-024-83190-0
12. https://doi.org/10.1038/s41598-024-81926-6
13. https://doi.org/10.3390/ijms25147563
14. https://doi.org/10.1016/bs.enz.2020.06.001
15. https://doi.org/10.1146/annurev.cellbio.21.012704.131001
16. https://doi.org/10.1016/j.csbj.2018.11.003,
17. https://doi.org/10.1016/bs.enz.2020.06.001,
18. https://doi.org/10.1038/s41598-024-81926-6,
19. https://doi.org/10.1038/s41598-024-83190-0,
20. https://doi.org/10.3390/ijms25147563,
21. https://doi.org/10.1128/jb.00035-24,
22. https://doi.org/10.1146/annurev.cellbio.21.012704.131001,