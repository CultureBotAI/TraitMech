---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:48:23.618611'
end_time: '2026-08-04T07:56:59.964278'
duration_seconds: 516.35
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width medium
  trait_identifier: METPO:1000889
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_medium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension lies approximately
    between 0.65 and 0.9 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_0.65_0.9
  evidence_summary: "DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan\
    \ synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths\
    \ in the 0.65\u20130.9 \u03BCm range.)"
  causal_graph_summary: 'cell_width_medium_typical_rod: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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
- **Trait label:** cell width medium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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


# Curation report: cell width medium

## Executive assessment

**Target trait:** `METPO:1000889`  
**Label:** cell width medium  
**Definition:** the shorter cellular dimension is approximately **0.65–0.9 µm**.  
**Category:** morphology; **term kind:** class; **mapping:** reviewed; **parent:** `METPO:1000882`; **synonym:** `W_0.65_0.9`.

The most defensible TraitMech graph is a **typical-rod width-maintenance graph**, centered on geometry-sensitive MreB and the Rod complex/elongasome. MreB orientation guides circumferential insertion of peptidoglycan (PG); RodA polymerizes glycan strands, PBP2 crosslinks them, and MreC, MreD, and RodZ organize or activate the machinery. Nutrient/cAMP signaling and the balance between elongasome, class-A PBP, membrane, and PG synthesis modify the resulting width. However, the literature generally explains **continuous width control or rod-versus-sphere transitions**, not why a cell falls specifically within 0.65–0.9 µm. Accordingly, the final edge into `METPO:1000889` should normally be conditioned on an actual calibrated width measurement.

## 1. Trait scope and boundaries

### What the trait represents

`METPO:1000889` is an **assay-observed morphological class**, not a pathway, physiological capacity, or taxonomic property. For a straight rod, width is ordinarily the diameter perpendicular to the long axis; operationally, it is the shorter cell dimension after segmentation. The class should be asserted when a representative statistic—preferably the population median or mean under a stated condition—lies approximately between **0.65 and 0.9 µm**.

The phenotype is compatible with a typical rod, curved rod, or short ovoid if the shorter dimension meets the threshold. It does **not** by itself assert rod shape, a particular aspect ratio, growth rate, cell-wall composition, or the presence of MreB.

### Boundary cases

1. **Near-threshold measurements:** Values close to 0.65 or 0.9 µm require uncertainty, pixel-size, point-spread-function, and segmentation-error reporting. Avoid assigning the bin from a rounded literature value such as “~0.9 µm.”
2. **Spheres and ovoids:** For a sphere, “shorter dimension” becomes indistinguishable from diameter. Such observations can technically satisfy a numerical width bin but should not be used as evidence for the typical-rod mechanism without an explicit shape qualifier.
3. **Length and volume:** Increased length, area, or volume does not imply increased width. In *E. coli*, nutrient enrichment increased length about twofold and width about 1.5-fold, whereas *B. subtilis* length increased about threefold while width remained approximately constant—demonstrating taxon dependence (westfall2018comprehensiveanalysisof pages 1-2).
4. **Transient morphology:** Width during division, recovery from spherical growth, antibiotic exposure, stationary-phase exit, osmotic shock, or microfluidic confinement should be represented with condition and time annotations.
5. **Population heterogeneity:** A population spanning several bins should not be reduced to `METPO:1000889` unless the curation convention explicitly uses a central statistic.
6. **Wall-less and non-MreB rods:** MreB/Rod-complex causality cannot be generalized to wall-less organisms, tip-growing Actinobacteria/Rhizobiales, or taxa using alternative morphogenetic systems.

## 2. Current mechanistic model

MreB filaments associate with the inner membrane and orient along the greatest principal membrane curvature. In rod-shaped cells this produces circumferential motion and directs wall insertion perpendicular to the long axis. In experimentally rounded *B. subtilis*, MreB motion became isotropic; externally imposed rod geometry restored orientation. During sphere-to-rod recovery, oriented MreB motion appeared in emerging rods while adjoining spherical regions retained unaligned motion, supporting a local self-reinforcing geometry–synthesis loop (hussain2018mrebfilamentsalign pages 1-2, hussain2018mrebfilamentsalign pages 13-15).

The Rod complex then converts spatial information into wall architecture. RodA is the SEDS-family glycosyltransferase; PBP2 is its cognate class-B transpeptidase. RodA polymerizes lipid-II-derived glycan strands and PBP2 crosslinks their peptide stems. MreBCD and RodZ connect or regulate this synthase pair. Disruption of elongasome components produces spherical, enlarged cells and can culminate in lysis; A22/MP265 disrupt MreB polymerization, while mecillinam specifically inhibits PBP2 and produces ovoid cells (garde2021peptidoglycanstructuresynthesis pages 13-15).

Physical wall architecture links this machinery to shape. AFM showed that normal rod-shaped *E. coli* has long, circumferentially oriented glycans, including chains up to approximately 200 nm, whereas chemically or genetically induced spheroids have shorter, disordered glycans (turner2018molecularimagingof pages 1-2). This supports circumferential glycan organization as a rod- and width-stabilizing mechanical output, although it does not establish a unique 0.65–0.9 µm set-point.

## 3. Recent developments, 2023–2024

### RodA concentration and elongasome processivity

A 2024 peer-reviewed single-molecule study tracked *B. subtilis* elongasomes around the full cell circumference. RodA abundance directly regulated processivity, reversal, and pausing. The authors inferred competition between likely two oppositely oriented synthesis complexes on an antiparallel MreB filament (“molecular motor tug-of-war”). Earlier processivity estimates were 400–600 nm; the newer trajectories averaged roughly half a cell circumference (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 8-9).

The paper proposes a non-monotonic width model: low synthase abundance yields too few long strands and a wider, weaker wall; excessive abundance yields frequent tug-of-war, short strands, and again a wider wall; intermediate activity yields a narrower, stronger wall. This is an expert mechanistic model, explicitly presented as speculative for cell-width determination, and should not be curated as established causality (middlemiss2024molecularmotortugofwar pages 8-9).

### MreC–MreD as a Rod-complex activation module

A 2024 preprint reported a 3.6 Å cryo-EM structure of the *Thermus thermophilus* MreC–MreD complex. Single-molecule FRET indicated that MreD stabilizes a lower MreC conformation compatible with PBP2 engagement; disrupting the relevant interfaces abolished Rod-complex activity in *E. coli*. The reported conformational displacement was approximately 20 Å. Mutations such as MreC I38D and T44D showed dominant-negative activity, while V63Q abolished growth in the complementation assay (gilman2024mrecmredstructurereveals pages 1-2, gilman2024mrecmredstructurereveals pages 5-6). This is mechanistically compelling but remains **preprint evidence** and should be flagged uncertain pending peer review.

### RodZ/MreB perturbations and envelope integrity

In 2024, *E. coli* ΔrodZ cells were shown to be spherical, to contain PG-layer holes, and to have increased volume. CRISPRi reduced `mreB` expression to **20% of wild type**, also producing morphological and envelope defects. ΔrodZ generated **>50-fold** more outer-membrane vesicles than wild type; MreB-repressed cells generated **eightfold** more, and approximately **7%** of ΔrodZ cells displayed budding, dents, or curved surface patterns (ojima2024buddingandexplosive pages 1-2). These data strengthen the link from the RodZ–MreB system to wall integrity but do not prove a direct transition into or out of the target numerical width bin.

### Coordination of membrane and PG synthesis

A 2023 *B. subtilis* study found that reducing fatty-acid synthesis genetically through FapR* or chemically with cerulenin rescued strains with limited PG-synthesis capacity. The authors interpret this as evidence that balanced membrane and PG synthesis is necessary to maintain cell shape and resist turgor and envelope stress (willdigg2023adecreasein pages 1-3). This is a valuable envelope-homeostasis branch but is only indirectly related to exact width.

## 4. Candidate nodes

Identifiers below are limited to high-confidence grounding. Where a stable entity-specific CURIE was not verified, the recommended representation is **label-only**, rather than inventing an identifier.

### Trait and measurable outputs

- `METPO:1000889` — cell width medium.
- `METPO:1000882` — supplied parent trait.
- Cell width, cell diameter, rod shape, ovoid shape, spherical morphology — label-only candidates.
- Peptidoglycan glycan-strand length, glycan circumferential orientation, wall anisotropy, elongasome processivity, surface-area-to-volume ratio — label-only quantitative/process nodes.

### Genes and proteins

- **MreB** — bacterial actin homolog; curvature-sensitive cytoskeletal filament.
- **MreC, MreD** — Rod-complex accessory/regulatory proteins.
- **RodZ** — transmembrane organizer coupling MreB and PG synthesis.
- **RodA / mrdB** — SEDS glycosyltransferase.
- **PBP2 / mrdA** — class-B penicillin-binding transpeptidase.
- **Class-A PBPs**, including PonA/PBP1 — autonomous PG polymerases acting alongside the elongasome.
- *B. subtilis* **Mbl, MreBH**, and **LytE** — taxon-specific MreB paralogs/hydrolase branch.
- **CyaA, Crp, Crr/EIIAᵍˡᶜ** — *E. coli* glucose–cAMP width-regulatory branch.
- **FapR** and fatty-acid-synthesis enzymes — membrane/PG-balance branch.

Gene/protein names should be connected to organism-specific UniProt or NCBI Gene records during YAML implementation; a bare protein name is not universally equivalent across taxa.

### Complexes, pathways, and biological processes

- Rod complex / elongasome.
- RodA–PBP2 synthase pair.
- MreC–MreD complex.
- MreB filament-associated PG synthesis complexes.
- Peptidoglycan biosynthesis — `GO:0009252`.
- Cell-wall organization or biogenesis — `GO:0071555`.
- Fatty-acid biosynthetic process — `GO:0006633`.
- cAMP-mediated catabolite-repression signaling — label-only pathway candidate.
- Class-A-PBP/elongasome balance and membrane/PG synthesis balance — label-only regulatory modules.

### Chemicals and environmental/experimental factors

- **Peptidoglycan** — `CHEBI:8005`.
- **Cyclic AMP** — `CHEBI:17489`.
- **Glucose** — `CHEBI:17234`.
- **A22**, **MP265**, **mecillinam**, **cerulenin**, **lipid II**, and magnesium supplementation — retain label-only until the project validates exact chemical CURIEs.
- Nutrient-rich versus nutrient-poor medium, osmotic support, growth phase, temperature, and physical confinement — condition nodes; preserve medium composition and time.

### Cellular locations

- Cytoplasmic membrane / inner membrane.
- Cytoplasm.
- Periplasm in diderm bacteria.
- Peptidoglycan sacculus and cylindrical sidewall.
- Cell poles and division septum.

## 5. Candidate causal edges

The following table is intended as the evidence ledger for YAML curation. “Direct” indicates perturbational, structural, or biochemical support in the stated model; it does not mean that the edge establishes the exact numerical target bin.

| ID | subject | predicate | object | taxon/context | evidence tier | DOI and publication date | short verbatim supporting snippet | curation note |
|---|---|---|---|---|---|---|---|---|
| E1 | MreB filament alignment | orients | circumferential peptidoglycan synthesis supporting rod-width maintenance | *Bacillus subtilis*; shape perturbation and recovery experiments | direct | 10.7554/eLife.32471 — 2018-02-22 | “MreB filaments align along greatest principal membrane curvature to orient cell wall synthesis” and “emerging rods displayed oriented MreB motion even at the initial points of their formation” (hussain2018mrebfilamentsalign pages 1-2, hussain2018mrebfilamentsalign pages 13-15) | Strong foundational edge for rod-width maintenance; supports typical rod width set-point indirectly, not the exact 0.65–0.9 µm bin. |
| E2 | Rod complex glycan synthase RodA + transpeptidase PBP2 | performs | glycan polymerization and peptide crosslinking during elongation | Mainly *Escherichia coli* review synthesis; rod-shaped bacteria generally | supportive | 10.1128/ecosalplus.esp-0010-2020 — 2021-12 | “RodA is a major glycosyltransferase” and “Glycan polymerization by RodA is followed by cross-linking of peptide stems by the cognate TPase PBP2” (garde2021peptidoglycanstructuresynthesis pages 13-15) | Good mechanistic edge for elongasome chemistry. Review-based rather than one primary experiment in this excerpt. |
| E3 | MreC-MreD interaction | stabilizes | activation-primed MreC conformation | *Thermus thermophilus* structure; *E. coli* in vivo validation | uncertain/preprint | 10.1101/2024.10.08.617240 — 2024-10 | “MreD controls the conformation of MreC through these contacts, inducing a state primed for Rod complex activation” (gilman2024mrecmredstructurereveals pages 1-2) | Preprint; mechanistically strong but not yet peer reviewed. Curate with uncertainty flag. |
| E4 | Disruption of MreC-MreD contacts | abolishes | Rod complex activity | *E. coli* model in vivo | uncertain/preprint | 10.1101/2024.10.08.617240 — 2024-10 | “Using E. coli as a model, we demonstrate that disrupting these interactions abolishes Rod complex activity in vivo” (gilman2024mrecmredstructurereveals pages 1-2) | Preprint; useful causal edge upstream of width control. Avoid overgeneralizing beyond rod-complex activity. |
| E5 | RodA abundance | regulates | elongasome processivity, reversal, and pausing | *Bacillus subtilis*; single-molecule VerCINI tracking | direct | 10.1038/s41467-024-49785-x — 2024-06 | “We found that cellular levels of RodA regulate elongasome processivity, reversal and pausing” (middlemiss2024molecularmotortugofwar pages 1-2) | Strong recent direct edge. Good candidate upstream regulator node for width-related graph. |
| E6 | intermediate concentration of active elongasome synthases | results in | “narrow, optimally strong cell wall” | *Bacillus subtilis*; model in Fig. 5 | uncertain/preprint? no, speculative within peer-reviewed paper | 10.1038/s41467-024-49785-x — 2024-06 | “At intermediate concentrations of active elongasome synthases… resulting in a narrow, optimally strong cell wall” (middlemiss2024molecularmotortugofwar pages 8-9) | Mark uncertain/speculative because authors explicitly present a model; informative for width mechanism, not direct proof. |
| E7 | low or high active elongasome synthase concentration | results in | “weaker, wider cell wall” | *Bacillus subtilis*; model in Fig. 5 | uncertain/speculative | 10.1038/s41467-024-49785-x — 2024-06 | “At low concentrations… resulting in a weaker, wider cell wall” and “At high concentrations… again resulting in a weaker, wider cell wall” (middlemiss2024molecularmotortugofwar pages 8-9) | Useful bidirectional width-control hypothesis; curate only with explicit uncertainty. |
| E8 | rodZ deletion | causes | spherical morphology with incomplete PG structure / increased cell volume | *Escherichia coli* ΔrodZ | direct | 10.3389/fmicb.2024.1400434 — 2024-06-20 | “ΔrodZ cells were spherical (WT cells are rod-shaped)” and “Holes in the PG layer and an increased cell volume were observed for ΔrodZ” (ojima2024buddingandexplosive pages 1-2) | Direct morphology edge; supports loss of normal rod width maintenance, not specific medium-width assignment. |
| E9 | mreB repression | causes | spherical morphology and increased cell volume | *Escherichia coli* CRISPRi mreBR3 | direct | 10.3389/fmicb.2024.1400434 — 2024-06-20 | “CRISPRi-mediated repression of mreB expression also induced morphological change of cells to spherical” and “Holes in the PG layer and an increased cell volume were observed for ΔrodZ and mreBR3 cells” (ojima2024buddingandexplosive pages 1-2) | Strong perturbation edge for graph; outcome is outside the target width class. |
| E10 | A22 / MP265 inhibition of MreB polymerization | causes | diffuse MreB distribution and loss of cell shape / rounding | Rod-shaped bacteria generally; *E. coli* and review evidence | supportive | 10.1128/ecosalplus.esp-0010-2020 — 2021-12 | “Small molecules A22 and MP265 reversibly inhibit MreB polymerization, resulting in diffuse distribution of MreB in the cytoplasm and loss of cell shape” (garde2021peptidoglycanstructuresynthesis pages 13-15) | Strong chemistry-to-phenotype edge from review. Useful as assay perturbation node. |
| E11 | mecillinam (PBP2 inhibitor) | inhibits | PBP2 transpeptidase activity, causing ovoid/rounded cells | *E. coli* elongation system | supportive | 10.1128/ecosalplus.esp-0010-2020 — 2021-12 | “TPase activity of PBP2 is specifically inhibited by the beta-lactam mecillinam, leading to ovoid cells” (garde2021peptidoglycanstructuresynthesis pages 13-15) | Good assay perturbation edge; supports role of PBP2 in maintaining rod width. |
| E12 | MP265/A22 analogue or mecillinam treatment | induces | rod-to-sphere transition | *Escherichia coli*; rapid drug treatment imaging | uncertain/preprint | 10.1101/2023.10.16.562172 — 2023-10 | “MreB disruption (via MP265/A22 analogue) and PBP2 inhibition (via Mecillinam) both induce rod-to-sphere morphological transitions in E. coli” (spahn2023transertionandcell pages 5-7) | Preprint; useful corroboration of perturbation phenotypes. |
| E13 | glucose/cAMP signaling | regulates | *E. coli* cell width | *Escherichia coli* central carbon metabolism mutants | direct | 10.1371/journal.pgen.1007205 — 2018-02-12 | “we identify a genetic pathway linking glucose levels to cell width through the signaling molecule cyclic-AMP” (westfall2018comprehensiveanalysisof pages 1-2) | Direct statement from primary paper; taxon-specific and environmentally contingent. |
| E14 | defects in crr, cyaA, or crp (low cAMP signaling) | reduce / stabilize | narrower width across media relative to WT response | *Escherichia coli* in LB-glu and AB-glu | supportive | 10.1371/journal.pgen.1007205 — 2018-02-12 | “The width of cyaA::kan and crp::kan was nearly identical in LB-glu and AB-glu, further supporting a key role for cAMP in regulating cell width” (westfall2018comprehensiveanalysisof pages 8-10) | Supports specific pathway nodes crr/cyaA/crp upstream of width. Quantitative values not present in excerpt. |
| E15 | nutrient-rich medium | increases | *E. coli* cell width | *Escherichia coli* growth-law context | supportive | 10.1371/journal.pgen.1007205 — 2018-02-12 | “E. coli increases length (2-fold) and width (1.5-fold) for a ~3-fold increase in the 2D micrography square area between nutrient poor and nutrient rich conditions” (westfall2018comprehensiveanalysisof pages 1-2) | Broad environment-to-width edge; relevant for assay context and boundary cases. |
| E16 | balanced fatty-acid synthesis and peptidoglycan synthesis | maintains | cell envelope capacity / shape integrity | *Bacillus subtilis* and bacteria generally | supportive | 10.1128/mbio.00475-23 — 2023-04-05 | “Balanced synthesis of the peptidoglycan cell wall and the cell membrane is critical for cells to maintain shape” (willdigg2023adecreasein pages 1-3) | Important systems-level edge for envelope homeostasis; do not curate as direct determinant of the medium-width bin. |
| E17 | decreased fatty-acid synthesis (cerulenin or FapR*) | rescues | growth of PG-limited cells | *Bacillus subtilis* PG-limited backgrounds | direct | 10.1128/mbio.00475-23 — 2023-04-05 | “inhibition of FAS by cerulenin also restored growth of PG-limited cells” (willdigg2023adecreasein pages 1-3) | Direct compensation edge relevant to envelope-balance subgraph; width consequence is indirect. |
| E18 | aPBP activity + elongasome activity balance | maintains | normal cell length and width | *Bacillus subtilis* | supportive | 10.1128/mbio.00475-23 — 2023-04-05 | “both aPBPs and the elongasome are necessary to maintain normal cell length and width” (willdigg2023adecreasein pages 1-3) | Taxon-specific but valuable. Supports inclusion of aPBP node(s) opposite Rod complex in width-control graph. |
| E19 | MreB localization pattern | correlates with | cell width | *Escherichia coli* MreB mutant library | direct | 10.1016/j.cub.2017.09.065 — 2017-11 | “wider cells exhibited flatter profiles (smaller slopes) that shifted to the left” and “MreB subcellular localization pattern correlates with cell width” (shi2017deepphenotypicmapping pages 8-9, shi2017deepphenotypicmapping pages 1-3) | Correlative rather than perturbational mechanism, but highly relevant for width-state readout. |
| E20 | spheroid-inducing perturbation (chemical or genetic) | causes | short, disordered glycan architecture instead of long circumferential glycans | *Escherichia coli* AFM of sacculi | supportive | 10.1038/s41467-018-03551-y — 2018-03 | “Glycans from E. coli in its normal rod shape are long and circumferentially oriented, but when a spheroid shape is induced… glycans become short and disordered” (turner2018molecularimagingof pages 1-2) | Supports edge from glycan architecture to rod-width-supporting wall mechanics; phenotype is rounded rather than exact width class. |


*Table: This table compiles source-backed candidate causal edges relevant to curating a TraitMech graph for METPO:1000889 cell width medium. It prioritizes direct mechanistic evidence, flags speculative or preprint claims, and avoids asserting that any mechanism alone guarantees the exact 0.65–0.9 µm width bin.*

## 6. Recommended minimal TraitMech graph

A conservative expansion of the existing 10-node/9-edge graph would use this core:

1. **Membrane curvature/rod geometry → orients → MreB filaments**.
2. **Oriented MreB filaments → spatially guide → circumferential Rod-complex motion**.
3. **MreC–MreD interaction → promotes → activation-compatible Rod complex** — uncertain/preprint.
4. **RodZ → organizes/couples → MreB and PG synthase machinery**.
5. **RodA → polymerizes → glycan strands**.
6. **PBP2 → crosslinks → nascent glycan strands into existing PG**.
7. **Circumferential PG insertion → produces → anisotropic rod-reinforcing wall**.
8. **Anisotropic wall reinforcement → maintains → stable rod diameter**.
9. **Stable measured diameter of 0.65–0.9 µm → realizes → `METPO:1000889`**.

The last edge must include an observation node or evidence annotation containing the numerical measurement. Mechanistic evidence alone should terminate at “stable rod diameter/width maintenance,” not directly at `METPO:1000889`.

Optional context branches include **glucose → cAMP–Crp signaling → increased *E. coli* width**, **RodA abundance → elongasome processivity**, **aPBP/elongasome balance → normal width**, and **fatty-acid/PG synthesis balance → envelope integrity**. These should be taxon- and condition-scoped.

## 7. Applications and real-world implementations

1. **Antibacterial target discovery.** PBP2 is directly inhibited by mecillinam, and A22/MP265 are experimental MreB inhibitors. The MreC–MreD interface has been proposed as a new regulatory target because disrupting it abolishes Rod-complex activity, although that result currently rests on a preprint (gilman2024mrecmredstructurereveals pages 1-2, garde2021peptidoglycanstructuresynthesis pages 13-15).
2. **Morphological antibiotic assays.** Rod-to-ovoid/sphere transitions provide rapid phenotypic readouts of PBP2 or MreB disruption. A 2023 preprint observed rounding within about **30 minutes** after MP265 or mecillinam treatment in *E. coli* (spahn2023transertionandcell pages 5-7).
3. **Single-cell phenotyping.** FACS-generated *E. coli* MreB mutant libraries spanned a **fivefold range in mean volume** while preserving growth rate; MreB A53 variants tuned width by as much as **60% above wild type**. Such libraries provide practical calibration strains for width bins (shi2017deepphenotypicmapping pages 1-3).
4. **Bioprocess engineering.** RodZ deletion or MreB repression can increase vesicle release dramatically, suggesting morphology engineering for extracellular-vesicle production. The associated PG defects, osmotic sensitivity, and slower growth are major process liabilities (ojima2024buddingandexplosive pages 1-2).
5. **High-resolution wall mechanics.** AFM measurement of glycan length and orientation and full-circumference single-molecule tracking now connect molecular synthase behavior to material architecture, enabling quantitative testing of width-control models (middlemiss2024molecularmotortugofwar pages 1-2, turner2018molecularimagingof pages 1-2).

## 8. Warnings: claims not yet ready for TraitMech curation

- **Do not assert that MreB or the Rod complex specifically causes 0.65–0.9 µm width.** The sources support rod formation, continuous width regulation, or rounding after perturbation, not this ontology threshold.
- **Do not curate “intermediate RodA concentration causes medium width” as established.** The narrow-at-intermediate-level relationship is a speculative model in the 2024 study (middlemiss2024molecularmotortugofwar pages 8-9).
- **Flag MreC–MreD activation edges as preprint-derived.** Structural and in vivo evidence is strong but was not peer reviewed in the retrieved 2024 version (gilman2024mrecmredstructurereveals pages 1-2, gilman2024mrecmredstructurereveals pages 5-6).
- **Do not treat MreB enrichment as a simple one-way cause.** MreB localization correlates strongly with width and responds to geometry; the relationship is feedback-driven. In one mutant series, mean curvature and width had **R = −0.95, p < 10⁻⁵** (shi2017deepphenotypicmapping pages 9-9).
- **Do not generalize *E. coli* glucose/cAMP width regulation to all bacteria.** The cyaA/crp/crr evidence is species- and medium-specific; each condition included at least **200 cells in each of three biological replicates** (westfall2018comprehensiveanalysisof pages 8-10).
- **Do not infer width from volume or vesiculation.** ΔrodZ and MreB-repressed cells had increased volume and spherical morphology, but no retrieved evidence assigns their shorter dimension to a particular METPO bin (ojima2024buddingandexplosive pages 1-2).
- **Do not use antibiotic exposure as evidence of a native trait.** A22/MP265 and mecillinam are perturbation nodes and usually produce abnormal, time-dependent states.
- **Do not conflate rod shape with medium width.** Rods can be substantially narrower or wider than the target interval.
- **Do not add unverified CURIEs.** Species-specific genes/proteins and chemicals should remain label-only until identifiers are checked against the project’s ontology-release versions.

## 9. DOI-first bibliography

1. Middlemiss S, et al. “Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in *Bacillus subtilis*.” *Nature Communications* 15, 5411. Accepted **18 June 2024**. DOI: [10.1038/s41467-024-49785-x](https://doi.org/10.1038/s41467-024-49785-x). (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 8-9)
2. Ojima Y, et al. “Budding and explosive membrane vesicle production by hypervesiculating *Escherichia coli* strain ΔrodZ.” *Frontiers in Microbiology* 15. Published **20 June 2024**. DOI: [10.3389/fmicb.2024.1400434](https://doi.org/10.3389/fmicb.2024.1400434). (ojima2024buddingandexplosive pages 1-2)
3. Gilman MSA, et al. “MreC–MreD structure reveals a multifaceted interface that controls MreC conformation.” bioRxiv preprint, **October 2024**. DOI: [10.1101/2024.10.08.617240](https://doi.org/10.1101/2024.10.08.617240). (gilman2024mrecmredstructurereveals pages 1-2, gilman2024mrecmredstructurereveals pages 5-6)
4. Willdigg JR, Patel Y, Helmann JD. “A Decrease in Fatty Acid Synthesis Rescues Cells with Limited Peptidoglycan Synthesis Capacity.” *mBio* 14. Published **5 April 2023**. DOI: [10.1128/mbio.00475-23](https://doi.org/10.1128/mbio.00475-23). (willdigg2023adecreasein pages 1-3)
5. Spahn C, et al. “Transertion and cell geometry organize the *Escherichia coli* nucleoid during rapid growth.” bioRxiv preprint, **October 2023**. DOI: [10.1101/2023.10.16.562172](https://doi.org/10.1101/2023.10.16.562172). (spahn2023transertionandcell pages 5-7)
6. Garde S, Chodisetti PK, Reddy M. “Peptidoglycan: Structure, Synthesis, and Regulation.” *EcoSal Plus* 9. Published **December 2021**. DOI: [10.1128/ecosalplus.esp-0010-2020](https://doi.org/10.1128/ecosalplus.esp-0010-2020). (garde2021peptidoglycanstructuresynthesis pages 13-15)
7. Hussain S, et al. “MreB filaments align along greatest principal membrane curvature to orient cell wall synthesis.” *eLife* 7:e32471. Published **22 February 2018**. DOI: [10.7554/eLife.32471](https://doi.org/10.7554/eLife.32471). (hussain2018mrebfilamentsalign pages 1-2, hussain2018mrebfilamentsalign pages 13-15)
8. Turner RD, et al. “Molecular imaging of glycan chains couples cell-wall polysaccharide architecture to bacterial cell morphology.” *Nature Communications* 9:1263. Published **March 2018**. DOI: [10.1038/s41467-018-03551-y](https://doi.org/10.1038/s41467-018-03551-y). (turner2018molecularimagingof pages 1-2)
9. Westfall CS, Levin PA. “Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in *Escherichia coli*.” *PLOS Genetics* 14:e1007205. Published **12 February 2018**. DOI: [10.1371/journal.pgen.1007205](https://doi.org/10.1371/journal.pgen.1007205). (westfall2018comprehensiveanalysisof pages 1-2, westfall2018comprehensiveanalysisof pages 8-10)
10. Shi H, et al. “Deep Phenotypic Mapping of Bacterial Cytoskeletal Mutants Reveals Physiological Robustness to Cell Size.” *Current Biology* 27:3419–3429.e4. Published **November 2017**. DOI: [10.1016/j.cub.2017.09.065](https://doi.org/10.1016/j.cub.2017.09.065). (shi2017deepphenotypicmapping pages 9-9, shi2017deepphenotypicmapping pages 8-9, shi2017deepphenotypicmapping pages 1-3)

## Curation conclusion

The evidence supports expanding `cell_width_medium_typical_rod` around a **geometry-sensitive MreB → activated Rod complex → circumferential glycan synthesis/crosslinking → anisotropic wall → stable rod diameter** chain. The best recent additions are RodA-dependent control of elongasome processivity, MreC–MreD-mediated activation, and envelope-synthesis balance. Nevertheless, assignment of `METPO:1000889` should remain dependent on an explicit **0.65–0.9 µm measurement**, with taxon, medium, growth phase, imaging method, and uncertainty recorded.

References

1. (westfall2018comprehensiveanalysisof pages 1-2): Corey S. Westfall and Petra Anne Levin. Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in escherichia coli. PLOS Genetics, 14:e1007205, Feb 2018. URL: https://doi.org/10.1371/journal.pgen.1007205, doi:10.1371/journal.pgen.1007205. This article has 79 citations and is from a domain leading peer-reviewed journal.

2. (hussain2018mrebfilamentsalign pages 1-2): Saman Hussain, Carl N Wivagg, Piotr Szwedziak, Felix Wong, Kaitlin Schaefer, Thierry Izoré, Lars D Renner, Matthew J Holmes, Yingjie Sun, Alexandre W Bisson-Filho, Suzanne Walker, Ariel Amir, Jan Löwe, and Ethan C Garner. Mreb filaments align along greatest principal membrane curvature to orient cell wall synthesis. eLife, Feb 2018. URL: https://doi.org/10.7554/elife.32471, doi:10.7554/elife.32471. This article has 212 citations and is from a domain leading peer-reviewed journal.

3. (hussain2018mrebfilamentsalign pages 13-15): Saman Hussain, Carl N Wivagg, Piotr Szwedziak, Felix Wong, Kaitlin Schaefer, Thierry Izoré, Lars D Renner, Matthew J Holmes, Yingjie Sun, Alexandre W Bisson-Filho, Suzanne Walker, Ariel Amir, Jan Löwe, and Ethan C Garner. Mreb filaments align along greatest principal membrane curvature to orient cell wall synthesis. eLife, Feb 2018. URL: https://doi.org/10.7554/elife.32471, doi:10.7554/elife.32471. This article has 212 citations and is from a domain leading peer-reviewed journal.

4. (garde2021peptidoglycanstructuresynthesis pages 13-15): Shambhavi Garde, Pavan Kumar Chodisetti, and Manjula Reddy. Peptidoglycan: structure, synthesis, and regulation. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0010-2020, doi:10.1128/ecosalplus.esp-0010-2020. This article has 338 citations.

5. (turner2018molecularimagingof pages 1-2): Robert D. Turner, Stéphane Mesnage, Jamie K. Hobbs, and Simon J. Foster. Molecular imaging of glycan chains couples cell-wall polysaccharide architecture to bacterial cell morphology. Nature Communications, Mar 2018. URL: https://doi.org/10.1038/s41467-018-03551-y, doi:10.1038/s41467-018-03551-y. This article has 128 citations and is from a highest quality peer-reviewed journal.

6. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (middlemiss2024molecularmotortugofwar pages 8-9): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 22 citations and is from a highest quality peer-reviewed journal.

8. (gilman2024mrecmredstructurereveals pages 1-2): Morgan S.A. Gilman, Irina Shlosman, Daniel D. Samé Guerra, Masy Domecillo, Elayne M. Fivenson, Claire Bourett, Thomas G. Bernhardt, Nicholas F. Polizzi, Joseph J. Loparo, and Andrew C. Kruse. Mrec-mred structure reveals a multifaceted interface that controls mrec conformation. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.08.617240, doi:10.1101/2024.10.08.617240. This article has 2 citations.

9. (gilman2024mrecmredstructurereveals pages 5-6): Morgan S.A. Gilman, Irina Shlosman, Daniel D. Samé Guerra, Masy Domecillo, Elayne M. Fivenson, Claire Bourett, Thomas G. Bernhardt, Nicholas F. Polizzi, Joseph J. Loparo, and Andrew C. Kruse. Mrec-mred structure reveals a multifaceted interface that controls mrec conformation. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.08.617240, doi:10.1101/2024.10.08.617240. This article has 2 citations.

10. (ojima2024buddingandexplosive pages 1-2): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 9 citations and is from a peer-reviewed journal.

11. (willdigg2023adecreasein pages 1-3): Jessica R. Willdigg, Yesha Patel, and John D. Helmann. A decrease in fatty acid synthesis rescues cells with limited peptidoglycan synthesis capacity. mBio, Apr 2023. URL: https://doi.org/10.1128/mbio.00475-23, doi:10.1128/mbio.00475-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (spahn2023transertionandcell pages 5-7): Christoph Spahn, Stuart Middlemiss, Estibaliz Gómez-de-Mariscal, Ricardo Henriques, Helge B. Bode, Séamus Holden, and Mike Heilemann. Transertion and cell geometry organize the escherichia coli nucleoid during rapid growth. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.10.16.562172, doi:10.1101/2023.10.16.562172. This article has 10 citations.

13. (westfall2018comprehensiveanalysisof pages 8-10): Corey S. Westfall and Petra Anne Levin. Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in escherichia coli. PLOS Genetics, 14:e1007205, Feb 2018. URL: https://doi.org/10.1371/journal.pgen.1007205, doi:10.1371/journal.pgen.1007205. This article has 79 citations and is from a domain leading peer-reviewed journal.

14. (shi2017deepphenotypicmapping pages 8-9): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

15. (shi2017deepphenotypicmapping pages 1-3): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

16. (shi2017deepphenotypicmapping pages 9-9): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.