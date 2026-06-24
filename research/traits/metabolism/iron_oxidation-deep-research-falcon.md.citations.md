# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** iron oxidation
- **METPO identifier:** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T05:27:32.138321

1. li2023sequencesimilaritynetwork pages 2-4
2. nikeleit2024inhibitionofphototrophic pages 1-2
3. hoover2023gallionellaceaepangenomicanalysis pages 4-8
4. tothero2024leptothrixochraceagenomes pages 9-13
5. wang2024characterizethegrowth pages 1-2
6. hou2024biologicalandchemical pages 11-13
7. hoover2023gallionellaceaepangenomicanalysis pages 10-14
8. hoover2023gallionellaceaepangenomicanalysis pages 1-2
9. jones2023mechanismsofbioleaching pages 6-11
10. https://doi.org/10.1128/msystems.00720-23
11. https://doi.org/10.1128/aem.00599-24
12. https://doi.org/10.1128/msystems.00038-23
13. https://doi.org/10.3390/microorganisms12122454
14. https://doi.org/10.1042/EBC20220257
15. https://doi.org/10.1038/s41561-024-01560-9
16. https://doi.org/10.3390/microorganisms12030590
17. https://doi.org/10.1128/msystems.00720-23,
18. https://doi.org/10.1128/msystems.00038-23,
19. https://doi.org/10.3390/microorganisms12122454,
20. https://doi.org/10.1038/s41561-024-01560-9,
21. https://doi.org/10.1128/aem.00599-24,
22. https://doi.org/10.1042/ebc20220257,
23. https://doi.org/10.3390/microorganisms12030590,