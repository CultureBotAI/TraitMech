---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:58:08.759218'
end_time: '2026-08-04T09:05:42.502214'
duration_seconds: 453.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: magnetosome
  trait_identifier: traitmech:000071
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: magnetosome
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A membrane-bounded intracellular organelle containing a magnetic iron-mineral
    crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria
    to align with and navigate along geomagnetic field lines.
  parent_traits: traitmech:000066
  synonyms: magnetotactic
  evidence_summary: "DOI:10.1038/nrmicro.2016.99:  (Uebe & Sch\xFCler review magnetosome\
    \ biogenesis as the formation of membrane-bounded magnetic-mineral organelles\
    \ in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel,\
    \ \"Magnetosome formation in prokaryotes\", describe magnetosomes and the magnetotactic\
    \ lifestyle they enable.)"
  causal_graph_summary: 'magnetosome_magnetotaxis: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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


# Magnetosome TraitMech Curation Report

**Target:** `traitmech:000071`  
**Label:** magnetosome  
**Category:** MORPHOLOGY | **Term kind:** CLASS | **Status:** REVIEWED  
**Parent:** `traitmech:000066`

## 1. Scope and current definition

A **magnetosome** is the combined membrane-plus-mineral bacterial organelle: a cytoplasmic-membrane-derived lipid-bilayer compartment containing a biomineralized magnetic crystal, usually magnetite (Fe₃O₄) or greigite (Fe₃S₄). Chains of these organelles generate a cellular magnetic dipole. **Magnetotaxis** or **magnetoaerotaxis** is the resulting behavior—not the organelle itself—where magnetic alignment assists swimming toward favorable oxygen/redox zones. This distinction should be explicit in the graph: `magnetosome chain enables magnetotaxis`, rather than treating “magnetosome” and “magnetotactic” as exact biological equivalents. (ferrara2024bacterialorganellesin pages 2-4, awal2023experimentalanalysisof pages 1-2, mccausland2022globalanalysisof pages 1-2)

### Boundary cases

- **Include:** mature magnetite- or greigite-containing membrane compartments; chains and alternative intracellular arrangements; and empty or immature magnetosome vesicles when discussing the organelle-biogenesis process.
- **Do not equate with:** free intracellular iron particles, synthetic magnetic nanoparticles, ferrosomes, ferritin-like storage compartments, sulfur globules, or generic iron biomineralization. Ferrosomes and encapsulated ferritin-like structures are separate iron-related organelles. (ferrara2024bacterialorganellesin pages 2-4)
- **Do not require magnetotactic behavior as the defining assay:** defective chain organization or undersized/superparamagnetic crystals can yield structurally recognizable magnetosomes but weak or absent magnetic alignment. The Δ`mamP` phenotype is an example. (amor2024magnetochromecatalyzedoxidationof pages 7-8, amor2024magnetochromecatalyzedoxidationof pages 1-2)
- **Mineral identity is variable:** magnetite is associated mainly with oxygen-poor, low-sulfide settings; greigite predominates in sulfide-rich habitats; some organisms can produce both depending on conditions. This ecological association is not a universal deterministic rule. (ferrara2024bacterialorganellesin pages 2-4)
- **Taxonomic caution:** most causal mechanisms were established in *Magnetospirillum magneticum* AMB-1 and *M. gryphiswaldense* MSR-1. Deep-branching MTB can use additional lineage-specific proteins and architectures. (ferrara2024bacterialorganellesin pages 2-4, awal2023experimentalanalysisof pages 1-2)

## 2. Candidate graph nodes and ontology grounding

Only identifiers that can be stated confidently are supplied. Protein accessions and exact GO terms should be added after organism-specific validation; gene symbols alone are preferable to invented or cross-species UniProt identifiers.

### Trait, structures, and locations

| Candidate node | Type | Grounding recommendation |
|---|---|---|
| magnetosome | morphology/organelle | `traitmech:000071` |
| magnetosome membrane | cellular structure | Label-only pending exact ontology review |
| magnetosome lumen | cellular location | Label-only |
| magnetosome vesicle | cellular structure/developmental state | Label-only |
| magnetosome chain | supramolecular cellular structure | Label-only |
| cytoplasmic membrane | cellular component | Ground to an appropriate GO cellular-component term after validation |
| MamK filament / magnetoskeleton | cytoskeletal structure | Label-only; do not equate automatically with generic actin cytoskeleton |
| magnetic single-domain crystal | material state | Label-only |

### Genes, proteins, transporters, and complexes

- **Conserved/core MAPs:** `mamA`, `mamB`, `mamE`, `mamK`, `mamM`, `mamO`, `mamP`, `mamQ`, `mamI`. A 2024 synthesis reports nine core genes, `mamABEKMOPQI`, conserved across known MTB, while noting that not all functions are fully resolved. (ferrara2024bacterialorganellesin pages 2-4)
- **Membrane formation:** MamI, MamL, MamQ, MamB; MamA scaffold.
- **Iron acquisition/transport:** FeoB1, FeoB2, MamB, MamM, MamH, MamZ.
- **Biomineralization/redox and crystal control:** MamE, MamO, MamP, MamT, MamX, Mms6, MamC, MamD, MamF.
- **Chain organization:** MamK, MamJ, LimJ, MamY, McaA, McaB; lineage-specific Mad28 and other MamK interactors.
- **Environment-linked metabolism:** CysC; nitrate/denitrification modules and `nap` operon as condition-dependent candidates.

MamB and MamM are CDF-family transporters; MamK is an actin-like ATP-dependent filament protein; MamJ is an adaptor connecting magnetosome membranes to MamK; and MamP contains c-type-cytochrome-like magnetochrome domains. These molecular-function descriptions can guide later GO/InterPro grounding but should not be converted into unverified CURIEs. (amor2024magnetochromecatalyzedoxidationof pages 1-2, ferrara2024bacterialorganellesin pages 4-6, awal2023experimentalanalysisof pages 1-2)

### Chemicals and minerals

| Node | Suggested grounding |
|---|---|
| iron atom | `CHEBI:18248` |
| ferrous iron / Fe(II) | `CHEBI:29033` |
| ferric iron / Fe(III) | `CHEBI:29034` |
| magnetite | `CHEBI:46726` |
| oxygen | `CHEBI:15379` |
| reactive oxygen species | `CHEBI:26523` |
| greigite | Label-only pending ChEBI verification |
| sulfide, sulfate, nitrate, nitrite | Use exact ChEBI species only after protonation-state and assay context are checked |

### Processes and factors

- Membrane invagination, MAP sorting, vesicle growth, iron uptake, magnetosome iron transport, iron nucleation, magnetite biomineralization, Fe(II) oxidation, crystal maturation, chain assembly, chain positioning/partitioning, magnetotaxis, and magnetoaerotaxis.
- Environmental or experimental nodes: extracellular iron concentration, oxygen limitation, oxic–anoxic transition zone, sulfide-rich habitat, redox condition, anaerobic growth, high-iron growth, geomagnetic field, and 1.5-mT static magnetic field.

## 3. Candidate causal graph

The following table prioritizes experimentally supported edges and distinguishes direct evidence from review-level synthesis.

| subject | predicate | object | evidence strength | taxon/assay qualifier | DOI |
|---|---|---|---|---|---|
| MamI/MamL/MamQ/MamB | required_for | magnetosome membrane formation | strong primary + review | *Magnetospirillum magneticum* AMB-1 inducible/complementation genetics for MamQ and prior required-gene set; general MTB review summary (cornejo2016dynamicremodelingof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | 10.1128/mbio.01898-15; 10.1111/mmi.15330 |
| MamB | promotes | magnetosome membrane invagination | moderate, review-supported/likely | Review synthesis: MamB likely recruits MAP complexes and generates lateral pressure for membrane bending; mechanism not fully resolved (ferrara2024bacterialorganellesin pages 4-6) | 10.1111/mmi.15330 |
| FeoB1/FeoB2 | imports | cytoplasmic Fe(II) | moderate review-supported | *M. gryphiswaldense* MSR-1; species-specific iron transporters supplying iron for biomineralization (ferrara2024bacterialorganellesin pages 4-6) | 10.1111/mmi.15330 |
| MamB/MamM | transports | Fe(II) into magnetosome compartment | moderate review-supported | *M. gryphiswaldense* MSR-1; CDF transporters managing Fe(II) import into magnetosome compartments (ferrara2024bacterialorganellesin pages 4-6) | 10.1111/mmi.15330 |
| MamH/MamZ | facilitates_import_of | Fe(III) into magnetosome compartment | moderate review-supported | *M. gryphiswaldense* MSR-1; review summary of Fe(III) import (ferrara2024bacterialorganellesin pages 4-6) | 10.1111/mmi.15330 |
| MamP-catalyzed Fe(II) oxidation | enables | magnetite crystal growth | strong primary | AMB-1/Δ*mamP*; in vitro + TEM + magnetic measurements + XAS/XMCD; Δ*mamP* crystals ~21 nm vs WT ~39 nm, coercivity 8.1 vs 17.8 mT (amor2024magnetochromecatalyzedoxidationof pages 7-8, amor2024magnetochromecatalyzedoxidationof pages 1-2, amor2024magnetochromecatalyzedoxidationof pages 6-7) | 10.1073/pnas.2410245121 |
| MamK | organizes | magnetosome chain | strong primary + recent comparative support | Magnetospirillum genetics/cell biology; deletion causes off-centered, fragmented chains; 2023 ortholog complementation supports conserved chain-organizing role (awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | 10.1128/mbio.01649-23; 10.1111/mmi.15330 |
| MamJ | tethers | magnetosomes to MamK filaments | strong primary/review | Magnetospirillum; MamJ acts as connector/adaptor, deletion causes chain collapse/clustered magnetosomes (awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | 10.1128/mbio.01649-23; 10.1111/mmi.15330 |
| MamY | aligns | magnetosome chain along positive cell curvature / motility axis | strong primary/review | Especially AMB-1/helical cells; Δ*mamY* keeps chain intact but mislocalized, impairing magnetotaxis (awal2023experimentalanalysisof pages 1-2, ferrara2024bacterialorganellesin pages 4-6) | 10.1128/mbio.01649-23; 10.1111/mmi.15330 |
| biomineralization initiation | permits | magnetosome membrane growth beyond ~50 nm | strong primary | AMB-1 inducible de novo formation with electron cryotomography; without biomineralization membranes stall at ~50 nm (cornejo2016dynamicremodelingof pages 1-2) | 10.1128/mbio.01898-15 |
| mamT | supports | biomineralization under high-iron and anaerobic conditions | strong primary | AMB-1 RB-TnSeq magnetic selection; defect exacerbated under high-iron and anaerobic conditions relative to standard conditions (mccausland2022globalanalysisof pages 1-2) | 10.1128/msystems.01037-21 |
| 1.5 mT static magnetic field | reduces | magnetosome formation | strong primary | AMB-1 microbiology/transcriptomics/genetics; compared with geomagnetic field, with decreased sulfate-reduction gene expression (chen2023effectsofstatic pages 1-6) | 10.1093/jambio/lxad302 |
| 1.5 mT static magnetic field | may_act_via | CysC / sulfur metabolism / ROS to reduce magnetosome formation | moderate primary, mediation uncertain | AMB-1; Δ*cysC* lost SMF response and ROS increased in SMF-treated WT, but causal mediation remains partly inferred (chen2023effectsofstatic pages 1-6) | 10.1093/jambio/lxad302 |
| magnetosome chain | enables | magnetotaxis / magnetoaerotaxis | strong review + primary background | MTB generally; chains form a magnetic dipole/cellular compass for navigation to suitable oxygen zones (ferrara2024bacterialorganellesin pages 2-4, mccausland2022globalanalysisof pages 1-2, awal2023experimentalanalysisof pages 1-2) | 10.1111/mmi.15330; 10.1128/msystems.01037-21; 10.1128/mbio.01649-23 |


*Table: This table summarizes the strongest candidate causal edges for curating a magnetosome TraitMech graph, prioritizing direct experimental evidence and clearly marking review-supported or uncertain links. It is useful as a compact starting point for YAML graph curation and evidence ranking.*

### Additional graph-ready triples with supporting snippets

| Subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|
| `MamI/MamL/MamQ/MamB required_for magnetosome membrane formation` | Cornejo et al.: “four genes appear to be necessary, but not sufficient, to make the magnetosome membrane compartment: mamI, mamL, mamQ, and mamB.” DOI: [10.1128/mbio.01898-15](https://doi.org/10.1128/mbio.01898-15), published February 2016. (cornejo2016dynamicremodelingof pages 1-2) | **Strong, AMB-1.** “Necessary but not sufficient” must be retained.
| `biomineralization initiation enables magnetosome-membrane expansion` | “A nascent magnetosome membrane…does not grow beyond ~50 nm” and can continue growth “if, and only if, it has initiated biomineralization.” DOI: [10.1128/mbio.01898-15](https://doi.org/10.1128/mbio.01898-15). (cornejo2016dynamicremodelingof pages 1-2) | **Strong, inducible AMB-1/cryo-ET.** This is a checkpoint-like causal relation, not merely correlation.
| `MamB promotes membrane invagination` | The 2024 review states that MamB “likely recruits and assembles other MAPs into larger complexes, generating lateral pressure to promote membrane bending and invagination.” DOI: [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330), published November 2024. (ferrara2024bacterialorganellesin pages 4-6) | **Uncertain mechanism.** Curate with `likely`/review-supported evidence, because the same review says the responsible remodeling mechanism remains unresolved.
| `FeoB1/FeoB2 supply cytoplasmic Fe(II) for biomineralization` | In MSR-1, the two Fe(II) transporters “supply iron for biomineralization processes.” DOI: [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330). (ferrara2024bacterialorganellesin pages 4-6) | **Moderate, species-specific.** Do not infer universal FeoB paralogue usage.
| `MamB/MamM transport Fe(II) into magnetosome` | “MamM and MamB manage Fe(II) transport” into magnetosome compartments in MSR-1. DOI: [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330). (ferrara2024bacterialorganellesin pages 4-6) | **Moderate review evidence.** Directionality is into the compartment; iron chaperones remain unknown.
| `MamH/MamZ facilitate Fe(III) import into magnetosome` | “MamH and MamZ facilitate the import of Fe(III).” DOI: [10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330). (ferrara2024bacterialorganellesin pages 4-6) | **Moderate, MSR-1.** Avoid generalizing to greigite-forming MTB.
| `MamP-catalyzed Fe(II) oxidation enables magnetite crystal growth` | Amor et al. show MamP magnetochromes catalyze Fe(II) oxidation; Δ`mamP` crystals averaged about 21 nm versus 39 nm in WT, with coercivity 8.1 versus 17.8 mT. DOI: [10.1073/pnas.2410245121](https://doi.org/10.1073/pnas.2410245121), published December 2024. (amor2024magnetochromecatalyzedoxidationof pages 1-2, amor2024magnetochromecatalyzedoxidationof pages 6-7) | **Strong, recent primary evidence.** Prefer “promotes crystal growth” over a broad claim that MamP globally sets the lumenal Fe(II):Fe(III) ratio; in vivo iron-speciation control was not apparent.
| `MamK organizes and partitions magnetosome chains` | MamK forms filaments; deletion caused “off-centered shorter, fragmented, and ectopic” chains, while MamK treadmilling supports repositioning and equal partitioning. DOI: [10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23), published October 12, 2023. (awal2023experimentalanalysisof pages 1-2) | **Strong in Magnetospirillum.** Chain architectures and partners vary by lineage.
| `MamJ tethers magnetosomes to MamK` | MamJ acts as “a connector that attaches magnetosomes to MamK filaments,” and deletion caused chain collapse and clustered magnetosomes in MSR-1. DOI: [10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23). (awal2023experimentalanalysisof pages 1-2) | **Strong, taxon-qualified.** In AMB-1, LimJ provides partial/redundant functionality.
| `MamY aligns chain with positive curvature and motility axis` | Δ`mamY` retained an intact MamK-bound chain, but it was mislocalized to negative curvature and magnetotaxis was impaired. DOI: [10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23). (awal2023experimentalanalysisof pages 1-2) | **Strong in helical Magnetospirillum.** Best represented as spatial alignment, not crystal synthesis.
| `Mad28 can substitute for MamK-like chain function` | Mad28 orthologues from Thermodesulfobacteriota and Nitrospirota formed filaments and functionally complemented *M. gryphiswaldense* `mamK` mutants. DOI: [10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23). (awal2023experimentalanalysisof pages 1-2) | **Assay-specific/heterologous.** Do not curate as universal native equivalence.
| `mamT supports biomineralization under high-iron and anaerobic conditions` | RB-TnSeq used 184,710 AMB-1 strains, about 34 mutants per gene; `mamT` insertions showed an exacerbated defect under high-iron and anaerobic conditions, validated with markerless deletion and TEM. DOI: [10.1128/msystems.01037-21](https://doi.org/10.1128/msystems.01037-21), published January 25, 2022. (mccausland2022globalanalysisof pages 1-2) | **Strong condition-dependent evidence.** Do not simplify to an unconditional essential-gene edge.
| `1.5-mT static field decreases magnetosome formation` | Chen et al.: “a 1.5 mT SMF significantly promoted cell growth but reduced magnetosome formation” versus the geomagnetic field. DOI: [10.1093/jambio/lxad302](https://doi.org/10.1093/jambio/lxad302), published December 2023. (chen2023effectsofstatic pages 1-6) | **Strong experimental factor, AMB-1.** Field magnitude and exposure protocol are essential qualifiers.
| `static field acts through CysC/sulfur metabolism/ROS` | Sulfate-reduction transcripts decreased; Δ`cysC` no longer responded to the field; ROS increased in field-treated WT. DOI: [10.1093/jambio/lxad302](https://doi.org/10.1093/jambio/lxad302). (chen2023effectsofstatic pages 1-6) | **Uncertain mediation.** The authors “proposed” this pathway; curate as a model or multi-edge hypothesis rather than a settled linear mechanism.
| `magnetosome chain enables magnetotaxis/magnetoaerotaxis` | Chains form a magnetic dipole/cellular compass that aligns cells with geomagnetic fields and assists navigation toward suitable oxygen levels. (ferrara2024bacterialorganellesin pages 2-4, awal2023experimentalanalysisof pages 1-2, mccausland2022globalanalysisof pages 1-2) | **Strong functional edge.** Magnetic alignment reduces a three-dimensional search to movement along field lines, but swimming still requires motility machinery.

## 4. Recent developments, expert interpretation, and quantitative findings

### 2023–2024 advances

1. **MamP mechanism resolved.** The December 2024 PNAS study substantially sharpens the redox module: MamP-mediated Fe(II) oxidation promotes growth of pre-existing magnetite rather than simply determining bulk intracellular iron speciation. Δ`mamP` reduced mean crystal length from approximately 39 to 21 nm, increased the superparamagnetic fraction from about 6% to 11%, and lowered coercivity from 17.8 to 8.1 mT; only about 10% of mutant crystals reached wild-type stable-single-domain size. (amor2024magnetochromecatalyzedoxidationof pages 7-8, amor2024magnetochromecatalyzedoxidationof pages 1-2, amor2024magnetochromecatalyzedoxidationof pages 6-7)

2. **The magnetoskeleton is conserved but evolutionarily flexible.** In 2023, MamK orthologues from several bacterial lineages restored chain assembly to different degrees in *M. gryphiswaldense*. Mad28 proteins from deep-branching MTB also formed filaments and complemented `mamK` mutants. The authors nevertheless found evidence for species-specific interactors, arguing against a universal single-protein chain model. (awal2023experimentalanalysisof pages 1-2)

3. **External magnetic fields can affect biogenesis indirectly.** The 2023 AMB-1 study linked a weak 1.5-mT static field to reduced magnetosome formation, altered sulfate-pathway expression, increased ROS, and CysC-dependent responsiveness. This is important for experimental metadata but is not yet a canonical endogenous magnetosome-biogenesis pathway. (chen2023effectsofstatic pages 1-6)

4. **Current expert synthesis emphasizes four interdependent stages:** MAP sorting/membrane invagination, chain formation, iron transport, and nucleation/biomineralization. These stages can overlap rather than forming a strictly linear pipeline. Major unresolved areas include MAP sorting signals, the exact membrane-remodeling machinery, iron chaperones, and regulation of iron allocation. (ferrara2024bacterialorganellesin pages 4-6)

### Relevant statistics

- Magnetosome islands commonly span **80–100 kb**, approximately **2% of a bacterial genome**; MSR-1 contains more than 30 MAPs across five polycistronic operons. (ferrara2024bacterialorganellesin pages 2-4)
- In MSR-1, more than **99.5% of intracellular iron** can reside in magnetosomes. Biomineralization is detectable below **1 μM** extracellular iron; uptake/mineralization saturates around **20–50 μM**, while **200 μM** iron inhibits growth. (ferrara2024bacterialorganellesin pages 4-6)
- The AMB-1 RB-TnSeq study generated **184,710 unique strains**, averaging about **34 mutants per gene**. (mccausland2022globalanalysisof pages 1-2)
- MTB can comprise up to **30% of microbial biomass** in some habitats; one estimate places their capture at **1–50% of dissolved iron inputs** to the ocean. These are habitat/model-dependent ecological estimates, not global constants. (mccausland2022globalanalysisof pages 1-2)

## 5. Applications and real-world relevance

- **Ecology and biogeochemistry:** magnetosome production sequesters substantial iron, and MTB occur near oxic–anoxic transitions. Magnetite/greigite mineralization intersects iron and sulfur cycling. (ferrara2024bacterialorganellesin pages 2-4, mccausland2022globalanalysisof pages 1-2)
- **Paleoenvironmental reconstruction:** preserved magnetosome crystals, or magnetofossils, are used as candidate indicators of ancient environments and geomagnetic history. The strength of any specific paleoenvironmental interpretation depends on distinguishing biogenic crystals from abiotic look-alikes.
- **Biotechnology:** magnetosomes offer genetically encoded, membrane-coated magnetic nanoparticles with controlled size, morphology, and surface chemistry. Proposed and preclinical uses include magnetic separation, biosensing, MRI contrast, drug delivery, magnetic hyperthermia, and magnetically guided bacterial microrobots. These remain primarily research or preclinical applications; they should not be represented as established clinical implementations.
- **Synthetic biology:** transferring a minimal magnetosome gene set into tractable hosts is a route toward programmable magnetic cells, but faithful membrane formation, iron homeostasis, crystal maturation, and chain assembly remain coupled engineering challenges.

## 6. Recommended minimal graph architecture

A defensible first revision of the existing 14-node/10-edge graph would use the following modules:

1. `extracellular Fe(II) -> FeoB1/FeoB2 -> cytoplasmic Fe(II)`
2. `MamI + MamL + MamQ + MamB -> magnetosome membrane formation`
3. `MamB/MamM -> Fe(II) transport into magnetosome`
4. `MamH/MamZ -> Fe(III) transport into magnetosome`
5. `MamP-catalyzed Fe(II) oxidation -> magnetite crystal growth -> stable-single-domain crystal`
6. `biomineralization initiation -> membrane expansion beyond ~50 nm`
7. `MamK filament + MamJ/LimJ adaptor + MamY -> chain assembly/alignment/partitioning`
8. `magnetosome chain -> cellular magnetic dipole -> magnetotaxis -> access to preferred oxygen/redox zone`

Add condition-specific branches for `mamT`, anaerobiosis/high iron, sulfide-rich habitat, and static-field/CysC/ROS only when the YAML evidence model can preserve organism, assay, and uncertainty qualifiers.

## 7. Warnings: claims not ready for unconditional curation

- **MamB-driven membrane bending** remains a plausible mechanistic model, not a fully resolved direct molecular mechanism. (ferrara2024bacterialorganellesin pages 4-6)
- **MamP as the global controller of the Fe(II):Fe(III) ratio** is too broad; recent in-vivo measurements did not show apparent bulk iron-speciation control. Curate its demonstrated Fe(II)-oxidizing/crystal-growth role instead. (amor2024magnetochromecatalyzedoxidationof pages 1-2)
- **Greigite synthesis should not inherit the magnetite pathway automatically.** Its genetic and biochemical mechanism is much less resolved.
- **Mms6 “determines uniform crystal size/shape”** is widely reported, but a graph edge should await a directly examined primary source and organism-specific evidence in this curation pass.
- **MamE, MamO, MamX, and MamZ functions should not be collapsed into one generic redox edge.** Their protease, localization, transport, or condition-dependent roles require separate primary evidence.
- **Environmental associations are not universal causes:** low sulfide versus sulfide-rich conditions predict mineral occurrence at population/ecosystem level but do not by themselves establish a direct within-cell switch.
- **Static-field → CysC → ROS → reduced magnetosome formation** is a proposed mediation chain from one AMB-1 exposure study; preserve it as uncertain and assay-specific. (chen2023effectsofstatic pages 1-6)
- **Heterologous complementation is evidence of functional capacity, not proof of the protein’s native role** in every donor lineage. This applies particularly to Mad28 and diverse MamK orthologues. (awal2023experimentalanalysisof pages 1-2)
- **Taxon-specific paralogues matter:** MamJ/LimJ redundancy and AMB-1 versus MSR-1 differences mean deletion phenotypes cannot be generalized without strain qualifiers.

## DOI-first bibliography

1. Amor M. et al. “Magnetochrome-catalyzed oxidation of ferrous iron by MamP enables magnetite crystal growth in the magnetotactic bacterium AMB-1.” *PNAS* 121, December 2024. [https://doi.org/10.1073/pnas.2410245121](https://doi.org/10.1073/pnas.2410245121). (amor2024magnetochromecatalyzedoxidationof pages 7-8, amor2024magnetochromecatalyzedoxidationof pages 1-2)
2. Ferrara K.M., Gupta K.R., Pi H. “Bacterial Organelles in Iron Physiology.” *Molecular Microbiology* 122:914–928, November 2024. [https://doi.org/10.1111/mmi.15330](https://doi.org/10.1111/mmi.15330). (ferrara2024bacterialorganellesin pages 2-4, ferrara2024bacterialorganellesin pages 4-6)
3. Awal R.P. et al. “Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in *Magnetospirillum gryphiswaldense*.” *mBio* 14, October 12, 2023. [https://doi.org/10.1128/mbio.01649-23](https://doi.org/10.1128/mbio.01649-23). (awal2023experimentalanalysisof pages 1-2)
4. Chen H. et al. “Effects of static magnetic field on the sulfate metabolic pathway involved in *Magnetospirillum magneticum* AMB-1 cell growth and magnetosome formation.” *Journal of Applied Microbiology* 134, December 2023. [https://doi.org/10.1093/jambio/lxad302](https://doi.org/10.1093/jambio/lxad302). (chen2023effectsofstatic pages 1-6)
5. McCausland H.C. et al. “Global Analysis of Biomineralization Genes in *Magnetospirillum magneticum* AMB-1.” *mSystems* 7, January 25, 2022. [https://doi.org/10.1128/msystems.01037-21](https://doi.org/10.1128/msystems.01037-21). (mccausland2022globalanalysisof pages 1-2)
6. Amor M. et al. “Iron-biomineralizing organelle in magnetotactic bacteria: function, synthesis and preservation in ancient rock samples.” *Environmental Microbiology* 22:3611–3632, June 2020. [https://doi.org/10.1111/1462-2920.15098](https://doi.org/10.1111/1462-2920.15098). (amor2020iron‐biomineralizingorganellein pages 15-19)
7. Cornejo E. et al. “Dynamic Remodeling of the Magnetosome Membrane Is Triggered by the Initiation of Biomineralization.” *mBio* 7, February 2016. [https://doi.org/10.1128/mbio.01898-15](https://doi.org/10.1128/mbio.01898-15). (cornejo2016dynamicremodelingof pages 1-2)
8. Uebe R., Schüler D. “Magnetosome biogenesis in magnetotactic bacteria.” *Nature Reviews Microbiology* 14:621–637, September 2016. [https://doi.org/10.1038/nrmicro.2016.99](https://doi.org/10.1038/nrmicro.2016.99).
9. Faivre D., Schüler D. “Magnetotactic bacteria and magnetosomes.” *Chemical Reviews* 108:4875–4898, October 2008. [https://doi.org/10.1021/cr078258w](https://doi.org/10.1021/cr078258w).
10. Schüler D. “Genetics and cell biology of magnetosome formation in magnetotactic bacteria.” *FEMS Microbiology Reviews* 32:654–672, July 2008. [https://doi.org/10.1111/j.1574-6976.2008.00116.x](https://doi.org/10.1111/j.1574-6976.2008.00116.x).

References

1. (ferrara2024bacterialorganellesin pages 2-4): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (awal2023experimentalanalysisof pages 1-2): Ram Prasad Awal, Frank D. Müller, Daniel Pfeiffer, Caroline L. Monteil, Guy Perrière, Christopher T. Lefèvre, and Dirk Schüler. Experimental analysis of diverse actin-like proteins from various magnetotactic bacteria by functional expression in <i>magnetospirillum gryphiswaldense</i>. mBio, Oct 2023. URL: https://doi.org/10.1128/mbio.01649-23, doi:10.1128/mbio.01649-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

3. (mccausland2022globalanalysisof pages 1-2): Hayley C. McCausland, Kelly M. Wetmore, Adam P. Arkin, and Arash Komeili. Global analysis of biomineralization genes in <i>magnetospirillum magneticum</i> amb-1. Feb 2022. URL: https://doi.org/10.1128/msystems.01037-21, doi:10.1128/msystems.01037-21. This article has 6 citations and is from a peer-reviewed journal.

4. (amor2024magnetochromecatalyzedoxidationof pages 7-8): Matthieu Amor, Daniel M. Chevrier, Marina I. Siponen, Ramon Egli, Ernesto Scoppola, Lourdes Marcano, Chenghao Li, Fadi Choueikani, and Damien Faivre. Magnetochrome-catalyzed oxidation of ferrous iron by mamp enables magnetite crystal growth in the magnetotactic bacterium amb-1. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2410245121, doi:10.1073/pnas.2410245121. This article has 3 citations and is from a highest quality peer-reviewed journal.

5. (amor2024magnetochromecatalyzedoxidationof pages 1-2): Matthieu Amor, Daniel M. Chevrier, Marina I. Siponen, Ramon Egli, Ernesto Scoppola, Lourdes Marcano, Chenghao Li, Fadi Choueikani, and Damien Faivre. Magnetochrome-catalyzed oxidation of ferrous iron by mamp enables magnetite crystal growth in the magnetotactic bacterium amb-1. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2410245121, doi:10.1073/pnas.2410245121. This article has 3 citations and is from a highest quality peer-reviewed journal.

6. (ferrara2024bacterialorganellesin pages 4-6): Kristina M. Ferrara, Kuldeepkumar R. Gupta, and Hualiang Pi. Bacterial organelles in iron physiology. Molecular Microbiology, 122:914-928, Nov 2024. URL: https://doi.org/10.1111/mmi.15330, doi:10.1111/mmi.15330. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (cornejo2016dynamicremodelingof pages 1-2): Elias Cornejo, Poorna Subramanian, Zhuo Li, Grant J. Jensen, and Arash Komeili. Dynamic remodeling of the magnetosome membrane is triggered by the initiation of biomineralization. Mar 2016. URL: https://doi.org/10.1128/mbio.01898-15, doi:10.1128/mbio.01898-15. This article has 56 citations and is from a domain leading peer-reviewed journal.

8. (amor2024magnetochromecatalyzedoxidationof pages 6-7): Matthieu Amor, Daniel M. Chevrier, Marina I. Siponen, Ramon Egli, Ernesto Scoppola, Lourdes Marcano, Chenghao Li, Fadi Choueikani, and Damien Faivre. Magnetochrome-catalyzed oxidation of ferrous iron by mamp enables magnetite crystal growth in the magnetotactic bacterium amb-1. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2410245121, doi:10.1073/pnas.2410245121. This article has 3 citations and is from a highest quality peer-reviewed journal.

9. (chen2023effectsofstatic pages 1-6): Haitao Chen, Hongkai Shi, Changyou Chen, Yangkun Jiao, Pingping Wang, Chuanfang Chen, Jinhua Li, Long-Fei Wu, and Tao Song. Effects of static magnetic field on the sulfate metabolic pathway involved in magnetospirillum magneticum amb-1 cell growth and magnetosome formation. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxad302, doi:10.1093/jambio/lxad302. This article has 6 citations and is from a peer-reviewed journal.

10. (amor2020iron‐biomineralizingorganellein pages 15-19): Matthieu Amor, François P. Mathon, Caroline L. Monteil, Vincent Busigny, and Christopher T. Lefevre. Iron‐biomineralizing organelle in magnetotactic bacteria: function, synthesis and preservation in ancient rock samples. Jun 2020. URL: https://doi.org/10.1111/1462-2920.15098, doi:10.1111/1462-2920.15098. This article has 109 citations and is from a domain leading peer-reviewed journal.