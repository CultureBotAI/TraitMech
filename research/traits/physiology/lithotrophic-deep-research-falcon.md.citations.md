# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithotrophic
- **METPO identifier:** METPO:1000649
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses inorganic compounds as electron donors for energy generation.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_lithotroph, lithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Encyclopedia review supports inorganic compounds as growth-supporting reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation of an electrochemical ion gradient (Review supports respiratory energy conservation through ion gradients and ATP synthesis.)
- **Existing causal graph summary:** lithotrophic_inorganic_donor_energy: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithotrophic.yaml`.

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
**Generated:** 2026-06-18T12:01:25.731806

1. wang2024characterizethegrowth pages 1-2
2. hoover2025anorganotrophicsideroxydans pages 1-2
3. grinter2023structuralbasisfor pages 1-2
4. zhou2025diversityandecology pages 32-34
5. lasoperez2025nitrogencyclingduring pages 1-2
6. zhao2024anabundantbacterial pages 1-3
7. kong2026overlookedsiderophoreproducers pages 1-2
8. soom2025hydrogenasedrivenatpsynthesis pages 1-4
9. soom2025hydrogenasedrivenatpsynthesis pages 11-13
10. soom2025hydrogenasedrivenatpsynthesis pages 4-7
11. zhou2025diversityandecology pages 5-7
12. burton2025studiesonthe pages 22-26
13. hoover2025anorganotrophicsideroxydans pages 9-10
14. ibanez2023fromgenesto pages 1-2
15. soom2025hydrogenasedrivenatpsynthesis pages 7-11
16. NiFe
17. https://doi.org/10.1038/s41586-023-05781-7
18. https://doi.org/10.1101/2025.03.14.643271
19. https://doi.org/10.3390/microorganisms11061436
20. https://doi.org/10.1038/s41579-024-01104-3
21. https://doi.org/10.3390/microorganisms12030590
22. https://doi.org/10.1128/aem.00395-25
23. https://doi.org/10.1186/s40168-025-02290-9
24. https://doi.org/10.1128/mbio.00749-25
25. https://doi.org/10.3390/genes14091772
26. https://doi.org/10.1038/s42003-024-06136-2
27. https://doi.org/10.3390/microorganisms12030590,
28. https://doi.org/10.1128/aem.00395-25,
29. https://doi.org/10.1101/2025.03.14.643271,
30. https://doi.org/10.1038/s41586-023-05781-7,
31. https://doi.org/10.3390/microorganisms11061436,
32. https://doi.org/10.1038/s41579-024-01104-3,
33. https://doi.org/10.1128/mbio.00749-25,
34. https://doi.org/10.1038/s42003-024-06136-2,
35. https://doi.org/10.1186/s40168-025-02290-9,
36. https://doi.org/10.3390/genes14091772,