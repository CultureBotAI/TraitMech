# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plasmid carriage
- **METPO identifier:** traitmech:000090
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of one or more plasmids — extrachromosomal, typically circular DNA replicons that carry accessory genes such as resistance, virulence, or metabolic functions and can transfer by conjugation.
- **Parent traits:** traitmech:000089
- **Synonyms:** plasmid-bearing
- **Existing evidence:** DOI:10.1128/MMBR.00020-10:  (Smillie et al. review plasmid mobility, classifying conjugative and mobilizable plasmids as key vectors of horizontal gene transfer.) | DOI:10.1038/nrmicro1235:  (Frost et al. include plasmids among the principal mobile genetic elements.)
- **Existing causal graph summary:** plasmid_conjugation_hgt: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **plasmid carriage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/plasmid_carriage.yaml`.

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
**Generated:** 2026-06-18T03:47:45.318923

1. tokuda2024microbialevolutionthrough pages 6-8
2. orlek2023factorsassociatedwith pages 1-2
3. xue2024theevolutionarylandscape pages 6-6
4. dimitriu2024variousplasmidstrategies pages 1-2
5. fraikin2024singlecellevidencefor pages 3-5
6. xiang2024porindeficiencyor pages 1-2
7. cheng2024evolutionandmaintenance pages 1-2
8. liu2024compensatoryevolutionof pages 6-6
9. wright2024achromosomalmutation pages 21-22
10. wright2024achromosomalmutation pages 22-23
11. fraikin2024singlecellevidencefor pages 2-3
12. broad class
13. https://doi.org/10.1093/nar/gkae018
14. https://doi.org/10.1093/nar/gkae896
15. https://doi.org/10.1080/22221751.2024.2352432
16. https://doi.org/10.1128/msystems.01197-24
17. https://doi.org/10.1002/ece3.70121
18. https://doi.org/10.1371/journal.pbio.3002926
19. https://doi.org/10.1038/s42003-024-07167-5
20. https://doi.org/10.1111/1751-7915.14408
21. https://doi.org/10.1038/s41598-023-29530-y
22. https://doi.org/10.1038/s41598-023-29530-y,
23. https://doi.org/10.1111/1751-7915.14408,
24. https://doi.org/10.1038/s42003-024-07167-5,
25. https://doi.org/10.1080/22221751.2024.2352432,
26. https://doi.org/10.1371/journal.pbio.3002926,
27. https://doi.org/10.1093/nar/gkae018,
28. https://doi.org/10.1002/ece3.70121,
29. https://doi.org/10.1093/nar/gkae896,
30. https://doi.org/10.1128/msystems.01197-24,