# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotrophic
- **METPO identifier:** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotrophic.yaml`.

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
**Generated:** 2026-06-18T11:44:07.670069

1. yousavich2024effectsoftransient pages 21-25
2. yousavich2024effectsoftransient pages 25-30
3. simon2008theorganisationof pages 1-3
4. laufermeiser2024oxidationofsulfur pages 4-6
5. wang2024characterizethegrowth pages 1-2
6. tonietti2024unveilingthebioleaching pages 2-4
7. enriquez2024phenotypicandgenomic pages 1-2
8. simon2008theorganisationof pages 3-5
9. tonietti2024unveilingthebioleaching pages 21-23
10. laufermeiser2024oxidationofsulfur pages 1-2
11. NiFe
12. https://doi.org/10.1093/ismejo/wrae173
13. https://doi.org/10.3390/microorganisms12030590
14. https://doi.org/10.3390/microorganisms12122407
15. https://doi.org/10.1128/aem.00268-24
16. https://doi.org/10.1016/j.bbabio.2008.09.008.
17. https://doi.org/10.3390/microorganisms12030590.
18. https://doi.org/10.3390/microorganisms12122407.
19. https://doi.org/10.1093/ismejo/wrae173.
20. https://doi.org/10.1128/aem.00268-24.
21. https://doi.org/10.1016/j.bbabio.2008.09.008
22. https://doi.org/10.1016/j.bbabio.2008.09.008,
23. https://doi.org/10.1093/ismejo/wrae173,
24. https://doi.org/10.3390/microorganisms12030590,
25. https://doi.org/10.3390/microorganisms12122407,
26. https://doi.org/10.1128/aem.00268-24,