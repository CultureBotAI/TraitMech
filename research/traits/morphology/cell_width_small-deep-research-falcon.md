---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:51:10.853468'
end_time: '2026-08-04T07:58:53.031557'
duration_seconds: 462.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width small
  trait_identifier: METPO:1000888
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension lies approximately
    between 0.5 and 0.65 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_0.5_0.65
  evidence_summary: "DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan\
    \ synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths\
    \ in the 0.5\u20130.65 \u03BCm range.)"
  causal_graph_summary: 'cell_width_small_mreb_setpoint: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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
- **Trait label:** cell width small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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


# Curation report: **cell width small**

## 1. Scope and interpretation

**Target:** `METPO:1000888`  
**Label:** cell width small  
**Definition supplied for curation:** the shorter cell dimension is approximately **0.5–0.65 µm**.  
**Parent:** `METPO:1000882`; synonym: `W_0.5_0.65`.

This is a **quantitative, assay-observed morphology class**, not a molecular function or an intrinsic statement that a species is “small.” For a straight rod, width is usually the diameter of the cylindrical sidewall measured perpendicular to the long axis. For curved rods, it should be estimated locally along the centerline. For cocci, irregular cells, branched cells, L-forms, or strongly tapered organisms, “shorter dimension” may not be biologically equivalent to Rod-system-controlled sidewall diameter.

The class should be assigned only when a calibrated measurement or an explicitly reported range places the relevant population statistic in approximately 0.5–0.65 µm. It should not be inferred merely from “thin,” “narrow,” “small,” an electron micrograph, filtration through a nominal pore size, or membership in a taxon normally having narrow cells.

### Boundary cases

* **Below ~0.5 µm:** belongs to a narrower-width class, not this class.
* **Above ~0.65 µm:** belongs to an adjacent larger-width class.
* **Rod shape versus width:** a cell can remain rod-shaped while becoming wider or narrower; conversely, loss of rod shape can make width ill-defined.
* **Length, volume, and surface-to-volume ratio:** these are related but distinct traits. A mutation can change length or volume without producing width in this interval.
* **Cell-wall thickness:** nanometre-scale wall thickness is not cell width.
* **Population heterogeneity:** report whether the value is a mean, median, fitted cylindrical diameter, single-cell range, or subpopulation. A mean in the interval does not establish that every cell satisfies it.
* **Preparation artifacts:** fixation, dehydration, sectioning, osmolarity, growth phase, medium, temperature, and segmentation method can shift apparent width.

## 2. Current mechanistic model

The best-supported mechanism is not a simple “MreB set-point.” In rod-shaped bacteria using dispersed lateral growth, width emerges from the relative activities and spatial organization of two peptidoglycan-synthetic systems. The circumferential Rod system tends to reduce diameter by depositing oriented material, whereas spatially less organized class-A PBPs can promote diameter expansion. In *Bacillus subtilis*, increasing `mreBCD` expression narrowed cells by approximately **33 nm**, or **58 nm** in a merodiploid context; reducing PBP1/PonA to 0.25 of wild-type caused about **23% thinning**, while PBP1 overexpression produced cells nearly twice wild-type diameter. Wild-type diameter was retained over a PBP1:MreB abundance ratio of roughly **0.8–1.5**. Directionally moving MreB-filament density correlated with width across *E. coli* backgrounds with reported R² values of **0.84–0.99**. These data support a balance-and-organization model rather than MreB alone acting as a molecular ruler. (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10)

Mechanistically, MreB-associated complexes move around the circumference. RodA polymerizes glycan strands, while its cognate class-B PBP crosslinks them. Circumferentially oriented glycans provide barrel-hoop-like reinforcement and increase sacculus mechanical anisotropy, thereby opposing radial expansion under turgor. (dion2018celldiameterin pages 1-3, middlemiss2024molecularmotortugofwar pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and morphology

* `METPO:1000888` — cell width small; terminal phenotype.
* `METPO:1000882` — supplied parent trait.
* Cell diameter/cell width — quantitative measurement node; label-only unless the project has a preferred quality ontology.
* Rod-shaped cell morphology — contextual phenotype, not synonymous with `METPO:1000888`.

### Complexes and pathways

* **Rod complex / elongasome** — MreB, MreC, MreD, RodZ, RodA, and a class-B PBP such as PBP2/PBP2A.
* **Class-A PBP system** — bifunctional glycosyltransferase/transpeptidases such as PBP1/PonA.
* **Peptidoglycan biosynthesis and remodeling** — candidate grounding: `GO:0009252` for peptidoglycan biosynthetic process.
* **Circumferential lateral-wall peptidoglycan synthesis** — label-only specialized process.
* **Peptidoglycan hydrolysis/remodeling** — label-only unless a more specific verified GO term is selected.

### Genes and proteins

* **MreB/MreB-family proteins** — cytoskeletal organizer; use taxon-specific UniProt accessions during organism-level curation.
* **MreC and MreD** — regulatory components coupling MreB organization to synthase activity.
* **RodZ** — transmembrane organizer interacting with major Rod-complex components.
* **RodA/MrdB** — SEDS-family glycosyltransferase.
* **PBP2/MrdA**, or *B. subtilis* PBP2A/PBPH — cognate class-B transpeptidases.
* **PBP1/PonA and other aPBPs** — bifunctional synthases with width-expanding or wall-repair effects that are species- and dosage-dependent.
* **DacB** — PBP4-family endo/carboxypeptidase in the *Myxococcus xanthus* synthase–hydrolase mechanism.

### Structures, localizations, and physical properties

* Peptidoglycan cell wall/sacculus — candidate grounding: `GO:0030288` for the Gram-negative peptidoglycan-based cell wall where appropriate; verify taxon-specific applicability.
* Cytoplasmic membrane — `GO:0005886`.
* Cell sidewall/peripheral wall — label-only unless a project-approved ontology term is available.
* Circumferentially oriented glycan strands.
* Directionally moving MreB filaments.
* Sacculus mechanical anisotropy.
* Turgor pressure — physical input; label-only unless the project has an approved biophysical ontology.
* Dense versus porous peptidoglycan architecture.

### Chemicals and experimental factors

* **Mecillinam/amdinocillin** — inhibits PBP2 and is useful as a Rod-system perturbation; verify the current ChEBI record before insertion.
* **A22** — MreB antagonist; keep label-only until the intended chemical record is verified.
* **Moenomycin** — inhibits aPBP glycosyltransferase activity; verify the specific compound/mixture identifier.
* Osmotic support, including sucrose — experimental modifier; sucrose is `CHEBI:17992`.
* Inducer-controlled expression of `mreBCD`, `rodA`, or `ponA` — experimental factor, not an endogenous causal node.

### Taxa for evidence qualifiers

* *Bacillus subtilis* — `NCBITaxon:1423`.
* *Escherichia coli* — `NCBITaxon:562`.
* *Myxococcus xanthus* — `NCBITaxon:34`.

Protein identifiers should be added as species-specific UniProt CURIEs only after strain and isoform verification; using one generic accession across these taxa would be misleading.

## 4. Candidate causal edges

The compact graph below summarizes the highest-priority relations. The detailed evidence and curation qualifications follow it.

| subject | predicate | object | taxon/context | evidence strength |
|---|---|---|---|---|
| Rod-system activity | decreases | cell diameter / cell width | *Bacillus subtilis*; balance with aPBP activity determines width (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10) | strong |
| class A PBPs (aPBPs; e.g., PBP1/PonA) activity | increases | cell diameter / cell width | *Bacillus subtilis*; opposing system to Rod complex (dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10) | strong |
| directional MreB filament density | promotes | narrow cell width | *Bacillus subtilis* and generalized to *Escherichia coli* in comparative analysis (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10) | strong |
| circumferential peptidoglycan synthesis | increases | mechanical anisotropy of the sacculus / sidewall reinforcement | rod-shaped bacteria, especially *Bacillus subtilis* (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 1-3, middlemiss2024molecularmotortugofwar pages 1-2) | strong |
| RodZ | organizes / activates | Rod complex / elongasome function | *Escherichia coli*; interacts with MreB, MreC, MreD, PBP2, RodA (ago2023relationshipbetweenthe pages 1-3) | strong |
| RodA cellular level | regulates | elongasome processivity, reversal, and pausing | *Bacillus subtilis* single-molecule imaging (middlemiss2024molecularmotortugofwar pages 1-2) | strong |
| RodA-PBP2 complex | synthesizes / crosslinks | lateral peptidoglycan during elongation | rod-shaped bacteria; explicit in *B. subtilis* and *E. coli* Rod system descriptions (middlemiss2024molecularmotortugofwar pages 1-2, ago2023relationshipbetweenthe pages 1-3) | strong |
| rodZ disruption | causes | spherical/wider cells with defective or porous peptidoglycan | *Escherichia coli* ΔrodZ; increased cell volume and PG holes (ago2023relationshipbetweenthe pages 1-3, ojima2024buddingandexplosive pages 1-2) | strong |
| mreB repression | causes | spherical/wider cells with defective or porous peptidoglycan | *Escherichia coli* CRISPRi mreB-repressed strain; increased cell volume and PG holes (ojima2024buddingandexplosive pages 1-2) | strong |
| inhibited PBP1a2 | promotes | DacB-mediated polar peptidoglycan degradation and rod-shape collapse | *Myxococcus xanthus* under moenomycin/aPBP inhibition context (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | strong |


*Table: This table summarizes compact, curation-ready candidate causal edges for the microbial trait METPO:1000888. It highlights the main mechanistic modules and perturbations most directly supported by the retrieved evidence.*

| # | Subject–predicate–object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | Increased Rod-system/MreBCD activity **decreases** cell diameter | Dion et al.: increasing `mreBCD` “progressively narrows cells”; the Rod system “reduces diameter.” (dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6) | **High priority.** Direct perturbation evidence in *B. subtilis*. Do not encode the exact 0.5–0.65 µm endpoint unless the curated strain/condition was actually measured in that interval. |
| 2 | Increased aPBP/PBP1 activity **increases** cell diameter | Reducing PBP1 to 0.25 WT caused ~23% thinning, whereas overexpression produced cells “nearly twice WT diameter.” (dion2018celldiameterin pages 3-6) | **High priority, taxon-specific.** Best supported for *B. subtilis*; aPBPs also repair defects, and their effects are not universally width-expanding. |
| 3 | Rod-system:aPBP activity balance **determines** cell width | WT diameter was maintained only over a PBP1/MreB abundance ratio of about 0.8–1.5; Rod and aPBP systems have opposing actions. (dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6) | **High priority.** Prefer a balance/intermediate node over two absolute deterministic edges. |
| 4 | Increased directional MreB-filament density **promotes** decreased width | “As MreBCD expression increases and rods thin,” oriented material and directional filaments increase; *E. coli* correlations had R² 0.84–0.99. (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10) | **Strong association with perturbational support**, but filament density is not necessarily the sole proximal cause. |
| 5 | Directional MreB organization **orients** circumferential PG synthesis | The Rod complex moves around the circumference; MreB-associated structures guide insertion perpendicular to the long axis. (dion2018celldiameterin pages 1-3, middlemiss2024molecularmotortugofwar pages 1-2) | **High priority** for rod-shaped, MreB-dependent taxa. |
| 6 | Circumferential PG synthesis **increases** sacculus mechanical anisotropy | Increased Rod activity generated more oriented wall material and stronger anisotropy; circumferential glycans reinforce the sidewall. (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 1-3, middlemiss2024molecularmotortugofwar pages 1-2) | **High priority mechanistic bridge** between synthesis geometry and width restraint. |
| 7 | Sacculus mechanical anisotropy **opposes** radial expansion / promotes narrow rod width | The wall stretched preferentially along length rather than width as Rod activity increased, linking oriented material to radial reinforcement. (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10) | **Mechanistically supported but partly model-based.** Encode as “contributes to” rather than sufficient causation. |
| 8 | RodA **polymerizes** glycan strands | The elongasome uses “the glycosyltransferase RodA, which polymerizes glycan strands.” (middlemiss2024molecularmotortugofwar pages 1-2) | **High confidence molecular-function edge.** |
| 9 | PBP2/PBP2A **crosslinks** newly synthesized glycan strands | The cognate class-B transpeptidase “attaches new strands to the existing cell wall.” (middlemiss2024molecularmotortugofwar pages 1-2) | **High confidence.** Use species-specific PBP names/accessions. |
| 10 | MreC–PBP2 interaction **stimulates** PG polymerization/crosslinking | Ago et al.: MreC interacts with PBP2; this is thought to cause a PBP2 structural change and “stimulate peptidoglycan polymerization and crosslinking.” (ago2023relationshipbetweenthe pages 1-3) | **Moderate confidence.** The phrase “thought to” warrants an uncertain qualifier unless primary structural/biochemical evidence is separately cited. |
| 11 | RodZ **organizes** the Rod complex | RodZ physically/genetically interacts with MreB, MreC, MreD, PBP2, and RodA and “plays a key role in this complex.” (ago2023relationshipbetweenthe pages 1-3) | **High priority.** “Organizes” is safer than a universal claim that RodZ nucleates MreB. |
| 12 | RodZ loss **disrupts** MreB organization and rod morphology | *E. coli* Δ`rodZ` cells were spherical; RodZ loss produces MreB misassembly and loss of shape. (ojima2024buddingandexplosive pages 1-2) | **Strong, taxon-specific.** This supports failure of width homeostasis, not specifically the small-width endpoint. |
| 13 | RodZ mutation **causes** porous/abnormal PG architecture | The 2023 RMR RodZ mutant had abnormal growth/morphology, and purified PG had “many large holes”; Rod-complex suppressors restored morphology. (ago2023relationshipbetweenthe pages 1-3) | **Strong recent evidence** linking complex integrity to wall architecture. RMR is a chimeric experimental allele, so qualify as assay-specific. |
| 14 | MreB repression **causes** spherical morphology, increased volume, and PG holes | CRISPRi reduced `mreB` expression to **20% of WT**; cells became spherical, with increased volume and PG holes. (ojima2024buddingandexplosive pages 1-2) | **Strong perturbation edge** in *E. coli*. It is evidence against curating low MreB activity as a cause of small width. |
| 15 | RodA abundance **regulates** elongasome processivity, pausing, and reversal | 2024 single-molecule work found that “cellular levels of RodA regulate elongasome processivity, reversal and pausing.” (middlemiss2024molecularmotortugofwar pages 1-2) | **Strong recent edge.** The downstream effect on final width was described as likely, so do not yet make RodA level → `METPO:1000888` a direct edge. |
| 16 | Multiple oppositely oriented synthesis complexes **regulate** elongasome dynamics through motor competition | Single-molecule data and simulations support competition between “likely two” oppositely oriented PG-synthesis complexes on an MreB filament. (middlemiss2024molecularmotortugofwar pages 1-2) | **Uncertain/model-supported.** Useful as an explanatory subgraph, not yet a trait-terminal edge. |
| 17 | aPBP inhibition by moenomycin **promotes** DacB-mediated polar PG degradation | In *M. xanthus*, inhibited PBP1a2 accelerated DacB degradation of poles; moenomycin promoted DacB–PG binding and reduced DacB mobility. (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | **Strong but highly taxon- and drug-state-specific.** Inhibition and genetic absence are not equivalent. |
| 18 | Unbalanced synthase–hydrolase activity **causes** rod-shape collapse | PG insertion requires hydrolase-generated openings; inhibited PBP1a2 plus DacB activity caused rapid rod collapse, whereas all-aPBP deletion mutants remained rods but were moderately shorter and wider. (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | **High-value warning edge.** Do not generalize to “all aPBP loss causes collapse.” |
| 19 | Osmotic support **reduces** consequences of Δ`rodZ` envelope failure | Sucrose significantly increased Δ`rodZ` culture OD and drastically reduced vesicle production. (ojima2024buddingandexplosive pages 1-2) | **Assay-specific modifier**, useful for modeling environmental rescue, not endogenous width determination. |

## 5. Recent developments, 2023–2024

1. **Rod-complex integrity was connected directly to PG ultrastructure.** Ago et al. showed that an *E. coli* RodZ transmembrane-domain chimera produced abnormal morphology and PG containing many large holes, while suppressors mapped mainly to Rod-complex components. This advances the field from correlations between shape proteins and whole-cell outline to a direct link between complex integrity, PG density, and mechanical support. Published **25 September 2023**. (ago2023relationshipbetweenthe pages 1-3)

2. **Synthase–hydrolase coordination emerged as a state-dependent mechanism.** Zhang et al. found that pharmacologically inhibited PBP1a2 recruits or immobilizes DacB on PG and accelerates polar degradation in *M. xanthus*. In contrast, deleting all three aPBPs did not abolish rods, although cells became moderately shorter and wider. The expert implication is that a trapped, inhibited enzyme can be more damaging than enzyme absence; graph predicates must therefore distinguish inhibition from loss of function. Published **2023**, DOI 10.1038/s41467-023-41082-3. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

3. **Elongasome dynamics were measured around the full circumference.** Middlemiss et al. used vertical-cell single-molecule imaging to show that the *B. subtilis* elongasome is highly processive but frequently pauses or reverses, that RodA abundance controls these dynamics, and that competing synthesis motors probably terminate runs. Earlier estimates of processivity were only **400–600 nm** and likely limited by shallow illumination. MreB double filaments were described as approximately **170 nm** long, with about **68 subunits** on average. Published **18 June 2024**. (middlemiss2024molecularmotortugofwar pages 1-2)

4. **Envelope consequences of width-control failure were quantified.** In *E. coli*, Δ`rodZ` produced **>50-fold** more outer-membrane vesicles, while `mreB` repression to 20% of WT produced an **eightfold** increase. About **7%** of Δ`rodZ` cells displayed budding, dents, or curved surface patterns, and both perturbations generated PG holes and increased cell volume. Published **20 June 2024**. These results show that width-control components also preserve envelope integrity and osmotic robustness. (ojima2024buddingandexplosive pages 1-2)

## 6. Applications and implementation relevance

* **Antibiotic discovery:** MreB, PBP2, RodA, and synthase–hydrolase coordination are druggable morphogenesis modules. However, the desired graph should represent drug-state effects precisely: PBP2 inhibition, MreB antagonism, and aPBP inhibition produce different failures, and an inhibited synthase can create a deleterious enzyme–hydrolase complex rather than simple loss of synthesis. (zhang2023coordinatedpeptidoglycansynthases pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2)
* **Morphology engineering:** Changing the Rod:aPBP balance can tune diameter while retaining viability over part of the dosage range. This is potentially useful for controlling surface-to-volume ratio, intracellular capacity, bioprocessing, or product release, but extreme widening or loss of Rod-system integrity produces porous walls, osmotic sensitivity, or lysis. (dion2018celldiameterin pages 3-6, ojima2024buddingandexplosive pages 1-2)
* **Phenotyping and quality control:** Width should be measured under standardized medium, growth rate, osmolarity, temperature, and cell-cycle conditions. Segmentation-based light microscopy is suitable near 0.5–0.65 µm only with calibrated optics and a width-estimation method that accounts for the point-spread function; electron microscopy requires explicit preparation controls.
* **TraitMech implementation:** The most defensible terminal route is: increased organized Rod-system activity → increased directional/circumferential PG synthesis → increased wall anisotropy/radial reinforcement → decreased cell width → `METPO:1000888`, with an opposing aPBP branch. The terminal edge should be conditioned on an actual measured 0.5–0.65 µm phenotype.

## 7. Recommended minimal graph extension

A conservative extension to the existing 10-node/9-edge MreB-set-point graph would add:

1. class-A PBP activity;
2. Rod-system:aPBP activity balance;
3. directional MreB-filament density;
4. circumferential glycan insertion;
5. sacculus mechanical anisotropy;
6. radial expansion restraint;
7. RodA–PBP2 synthesis activity;
8. RodZ-mediated Rod-complex organization.

The preferred terminal chain is:

**RodZ/MreBCD organization → increased directionally active Rod complexes → circumferential RodA–PBP2 PG synthesis → oriented glycan material → increased sacculus anisotropy → reduced radial expansion → cell width 0.5–0.65 µm.**

Add the countervailing branch:

**increased spatially unorganized aPBP activity → isotropic wall expansion → increased diameter**, with final width determined by the balance of the two systems. (dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10)

## 8. Claims not yet ready for TraitMech curation

* Do **not** curate “MreB alone sets width to 0.5–0.65 µm.” Current evidence favors a balance between Rod and aPBP systems and wall mechanics.
* Do **not** infer `METPO:1000888` from rod shape, the presence of `mreB`, or “narrow” prose without calibrated measurements.
* Do **not** generalize the *B. subtilis* PBP1 widening relationship to all bacteria. Species lacking canonical MreB-based elongation can use polar, septal, or other growth modes.
* Do **not** equate aPBP inhibition with aPBP deletion. In *M. xanthus*, inhibition caused rapid DacB-dependent collapse, whereas deletion mutants retained rods. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
* Do **not** use Δ`rodZ`, severe `mreB` repression, A22 treatment, or PBP2 inhibition as positive causes of small width; these commonly cause widening, rounding, porous PG, or lysis. (ojima2024buddingandexplosive pages 1-2)
* Do **not** curate RodA abundance → small width directly from the 2024 processivity paper. RodA levels clearly altered processivity, reversal, and pausing, but the final width effect was presented as likely rather than directly established. (middlemiss2024molecularmotortugofwar pages 1-2)
* Treat “two opposing elongasome motors” as model-supported and uncertain because the study states “likely two.” (middlemiss2024molecularmotortugofwar pages 1-2)
* Do not add generic UniProt identifiers without strain-level verification, and do not invent ChEBI identifiers for A22, mecillinam, or moenomycin.
* The quantitative Rod:aPBP study retrieved here is a **2018 bioRxiv preprint**. Its mechanistic edges are compelling and quantitative, but curators should locate and cite the peer-reviewed version, if available, before production release. (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 3-6)

## 9. DOI-first bibliography

1. Middlemiss S, et al. “Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in *Bacillus subtilis*.” *Nature Communications* 15, 5411. Published 18 June 2024. DOI: **10.1038/s41467-024-49785-x**. https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2)
2. Ojima Y, et al. “Budding and explosive membrane vesicle production by hypervesiculating *Escherichia coli* strain ΔrodZ.” *Frontiers in Microbiology* 15, 1400434. Published 20 June 2024. DOI: **10.3389/fmicb.2024.1400434**. https://doi.org/10.3389/fmicb.2024.1400434 (ojima2024buddingandexplosive pages 1-2)
3. Ago R, et al. “Relationship between the Rod complex and peptidoglycan structure in *Escherichia coli*.” *MicrobiologyOpen* 12, e1385. Accepted 25 September 2023. DOI: **10.1002/mbo3.1385**. https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3)
4. Zhang H, Venkatesan S, Ng E, Nan B. “Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall.” *Nature Communications* 14, 5357. Accepted 21 August 2023. DOI: **10.1038/s41467-023-41082-3**. https://doi.org/10.1038/s41467-023-41082-3 (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
5. Özbaykal G, et al. “The transpeptidase PBP2 governs initial localization and activity of the major cell-wall synthesis machinery in *E. coli*.” *eLife* 9. Published February 2020. DOI: **10.7554/eLife.50629**. https://doi.org/10.7554/eLife.50629
6. Hussain S, et al. “MreB filaments align along greatest principal membrane curvature to orient cell wall synthesis.” *eLife* 7. Published February 2018. DOI: **10.7554/eLife.32471**. https://doi.org/10.7554/eLife.32471
7. Dion MF, et al. “Cell Diameter in *Bacillus subtilis* is Determined by the Opposing Actions of Two Distinct Cell Wall Synthetic Systems.” bioRxiv preprint, posted August 2018. DOI: **10.1101/392837**. https://doi.org/10.1101/392837 (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 3-6)
8. Ouzounov N, et al. “MreB Orientation Correlates with Cell Diameter in *Escherichia coli*.” *Biophysical Journal* 111:1035–1043. Published September 2016. DOI: **10.1016/j.bpj.2016.07.017**. https://doi.org/10.1016/j.bpj.2016.07.017
9. Morgenstein RM, et al. “RodZ links MreB to cell wall synthesis to mediate MreB rotation and robust morphogenesis.” *PNAS* 112:12510–12515. Published September 2015. DOI: **10.1073/pnas.1509610112**. https://doi.org/10.1073/pnas.1509610112
10. Shi H, et al. “Deep Phenotypic Mapping of Bacterial Cytoskeletal Mutants Reveals Physiological Robustness to Cell Size.” *Current Biology* 27:3419–3429.e4. Published November 2017. DOI: **10.1016/j.cub.2017.09.065**. https://doi.org/10.1016/j.cub.2017.09.065

## Curation conclusion

`METPO:1000888` is suitable for a causal graph, but its terminal phenotype must remain measurement-dependent. The most defensible mechanism is **organized circumferential Rod-system synthesis producing anisotropic, radially reinforcing peptidoglycan, opposed by width-expanding aPBP activity**. RodZ, MreBCD, RodA–PBP2, oriented glycan insertion, and wall mechanics are strong candidate nodes. Severe Rod-system disruption, drug inhibition, hydrolase imbalance, and taxon-specific alternative growth modes should be represented as qualified perturbation branches rather than universal causes of the small-width trait.

References

1. (dion2018celldiameterin pages 18-19): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

2. (dion2018celldiameterin pages 1-3): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

3. (dion2018celldiameterin pages 3-6): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

4. (dion2018celldiameterin pages 8-10): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

5. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 22 citations and is from a highest quality peer-reviewed journal.

6. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 17 citations and is from a peer-reviewed journal.

7. (ojima2024buddingandexplosive pages 1-2): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 9 citations and is from a peer-reviewed journal.

8. (zhang2023coordinatedpeptidoglycansynthases pages 1-2): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 31 citations and is from a highest quality peer-reviewed journal.