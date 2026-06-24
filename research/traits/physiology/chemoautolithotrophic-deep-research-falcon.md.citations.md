# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautolithotrophic
- **METPO identifier:** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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
**Generated:** 2026-06-18T11:04:19.197134

1. deng2023strategiesofchemolithoautotrophs pages 1-2
2. yousavich2024effectsoftransient pages 21-25
3. cornell2024genomeencodedmetabolicpotential pages 15-18
4. ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2
5. wang2024characterizethegrowth pages 1-2
6. deng2023strategiesofchemolithoautotrophs pages 13-14
7. twible2024phandthiosulfate pages 1-2
8. han2024unveilinguniquemicrobial pages 1-2
9. deng2023strategiesofchemolithoautotrophs pages 10-13
10. twible2024phandthiosulfate pages 5-6
11. tonietti2024unveilingthebioleaching pages 1-2
12. wang2024characterizethegrowth pages 2-3
13. yousavich2024effectsoftransient pages 25-30
14. NiFe
15. Ni–Fe
16. but
17. S2O3 2−
18. https://doi.org/10.1186/s40168-023-01712-w
19. https://doi.org/10.3390/microorganisms12030590
20. https://doi.org/10.1128/aem.01698-23
21. https://doi.org/10.1038/s41467-024-47392-4
22. https://doi.org/10.3389/fmicb.2024.1426584
23. https://doi.org/10.3390/microorganisms12122407
24. https://doi.org/10.3390/molecules29102293
25. https://doi.org/10.1186/s40168-023-01712-w,
26. https://doi.org/10.3390/molecules29102293,
27. https://doi.org/10.1128/aem.01698-23,
28. https://doi.org/10.3390/microorganisms12030590,
29. https://doi.org/10.1038/s41467-024-47392-4,
30. https://doi.org/10.3389/fmicb.2024.1426584,
31. https://doi.org/10.3390/microorganisms12122407,