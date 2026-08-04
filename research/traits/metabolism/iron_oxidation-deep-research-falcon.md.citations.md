# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** iron oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **iron oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/iron_oxidation.yaml`.

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
**Generated:** 2026-08-04T06:27:12.608854

1. wang2024characterizethegrowth pages 1-2
2. hoover2023gallionellaceaepangenomicanalysis pages 4-8
3. li2023sequencesimilaritynetwork pages 2-4
4. li2023sequencesimilaritynetwork pages 1-2
5. hoover2023gallionellaceaepangenomicanalysis pages 15-17
6. tonietti2024unveilingthebioleaching pages 1-2
7. hoover2023gallionellaceaepangenomicanalysis pages 1-2
8. li2023sequencesimilaritynetwork pages 16-17
9. tonietti2024unveilingthebioleaching pages 12-13
10. tonietti2024unveilingthebioleaching pages 27-28
11. tonietti2024unveilingthebioleaching pages 21-23
12. wang2024characterizethegrowth pages 26-26
13. https://doi.org/10.1128/msystems.00720-23.
14. https://doi.org/10.1128/msystems.00038-23.
15. https://doi.org/10.3390/microorganisms12030590.
16. https://doi.org/10.3390/microorganisms12122407.
17. https://doi.org/10.1128/AEM.00496-21.
18. https://doi.org/10.1146/annurev.micro.112408.134208.
19. https://doi.org/10.1099/mic.0.045344-0.
20. https://doi.org/10.1128/msystems.00720-23,
21. https://doi.org/10.3390/microorganisms12030590,
22. https://doi.org/10.1128/msystems.00038-23,
23. https://doi.org/10.3390/microorganisms12122407,