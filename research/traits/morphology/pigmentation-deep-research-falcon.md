---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:30:24.609504'
end_time: '2026-08-04T09:37:16.897977'
duration_seconds: 412.29
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pigmentation
  trait_identifier: METPO:1003021
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pigmentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the color of pigments produced by a microorganism.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food,
    pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically
    produced microbial color phenotypes.)'
  causal_graph_summary: 'pigmentation_biosynthetic_colorants: 16 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 64
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pigmentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003021
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the color of pigments produced by a microorganism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food, pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically produced microbial color phenotypes.)
- **Existing causal graph summary:** pigmentation_biosynthetic_colorants: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pigmentation.yaml`.

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
- **Trait label:** pigmentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003021
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the color of pigments produced by a microorganism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food, pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically produced microbial color phenotypes.)
- **Existing causal graph summary:** pigmentation_biosynthetic_colorants: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pigmentation.yaml`.

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


# Curation report: microbial pigmentation

## Executive summary

**Target trait:** `METPO:1003021` (quoted verbatim)  
**Label:** pigmentation  
**Category:** morphology  
**Definition supplied:** “A phenotype characterized by the color of pigments produced by a microorganism.”  
**Parent:** `METPO:1000059`

For TraitMech, pigmentation should be modeled as an **observable cell, colony, biomass, or culture color resulting from production, accumulation, localization, or secretion of one or more microbial pigments**. Pigment biosynthesis is the causal process; the pigment molecule is the proximate color-bearing entity; and `METPO:1003021` is the phenotype endpoint. Pigments absorb and reflect visible wavelengths, whereas dyes are generally distinguished by solubility and mode of dispersion. A recent review places the relevant visible range at approximately 400–800 nm. (barreto2023microbialpigmentsmajor pages 1-2)

The best-supported initial graph consists of taxon-specific modules rather than a single universal linear pathway. Priority modules are: (1) prodigiosin in *Serratia*, (2) violacein in *Chromobacterium* or a heterologous host, and (3) pyomelanin through homogentisate. Broader carotenoid, bacteriochlorophyll, DOPA-melanin, and DHN-melanin branches should be separate modules sharing only the terminal relation “pigment accumulation causes pigmentation.”

| module | strongest direct causal chain | exemplar taxon | evidence strength | curation recommendation |
|---|---|---|---|---|
| prodigiosin | cpxR ⟶ represses pig gene cluster transcription ⟶ decreased prodigiosin production/red pigmentation; parallel direct support for metR ⟶ represses PigP ⟶ represses pig operon, and χ phage infection ⟶ increases pig operon transcription ⟶ increased prodigiosin | *Serratia marcescens* JNB 5-1 / ATCC 274 | high | Curate as a priority core bacterial pigmentation module with regulator-to-operon-to-pigment edges; annotate regulator and phage effects as strain-specific where applicable. |
| violacein | L-tryptophan ⟶ VioA/VioB/VioE/VioD/VioC pathway ⟶ violacein; CviIR quorum sensing at high cell density ⟶ activates violacein production | *Chromobacterium violaceum* | high | Curate as a priority pathway module with precursor-to-enzyme-set-to-pigment edges; add quorum-sensing activation as a separate regulatory branch. |
| pyomelanin/melanin | tyrosine degradation ⟶ homogentisate ⟶ pyomelanin; 4-hydroxyphenylpyruvate dioxygenase supports homogentisate production and homogentisate 1,2-dioxygenase supports homogentisate oxidation | *Shewanella oneidensis* MR-1 | high for pyomelanin, moderate/review-only for broader melanin classes | Curate pyomelanin first using direct enzyme/metabolite evidence; defer broader DOPA-, DHN-, tyrosinase-, laccase-, and PKS-based melanin graph expansion until primary species-specific causal papers are added. |
| carotenoids/photopigments | light/oxygen regulatory context ⟶ photosynthesis gene expression and pigment synthesis; excess membrane-bound carotenoids ⟶ scavenging capacity that safeguards bacteriochlorophyll synthesis/photosystem assembly | *Sediminicoccus* sp. KRV36 | moderate | Curate a limited photopigment submodule for light/oxygen-linked pigment maintenance and membrane localization; defer generic carotenoid biosynthesis edges unless supported by direct primary pathway papers in target taxa. |


*Table: This matrix ranks the main microbial pigmentation modules by directness of causal evidence and immediate suitability for TraitMech curation. It helps prioritize robust pathway/regulatory branches before adding broader review-derived pigment biology.*

## 1. Scope and boundary cases

### Included

* Visible color of microbial cells, colonies, aggregates, spores, biomass, or culture supernatant caused by endogenous pigment production.
* Intracellular, membrane-associated, cell-wall-associated, or extracellular pigments. For example, *Rhodotorula* carotenoids accumulate intracellularly and yield orange, salmon, pink, or red colonies; fungal melanin may be localized in the cell wall or secreted. (qin2024melanininfungi pages 1-2, ochoavinals2024currentadvancesin pages 1-2)
* Loss, gain, or quantitative change in color following mutation, pathway transfer, altered gene expression, precursor supply, environmental treatment, or infection.
* Pigment mixtures where the assay measures a composite color, provided the chemical ambiguity is recorded. “Crude violacein,” for example, includes violacein and deoxyviolacein. (fang2015highcrudeviolacein pages 1-2)

### Excluded or separately modeled

* Color imparted only by medium pH indicators, exogenous dyes, blood products, host pigments, or stained substrates.
* Fluorescence or bioluminescence without corresponding visible pigment coloration.
* Structural color or iridescence not caused by a pigment molecule.
* Biological functions such as antioxidant activity, virulence, UV protection, or electron transfer unless linked through a distinct causal edge to pigment production or accumulation.
* Pigment-production capacity inferred only from genomic annotation. A biosynthetic gene cluster is not sufficient evidence that a strain is visibly pigmented.
* Taxonomic identification based on colony color alone. Pigmentation can vary with strain, growth phase, medium, temperature, light, oxygen, and spontaneous regulatory state.

## 2. Candidate graph nodes

Identifiers below are deliberately conservative. Label-only nodes are preferable to unverified CURIEs.

### Trait and phenotype nodes

| Node | Grounding | Comment |
|---|---|---|
| microbial pigmentation | `METPO:1003021` | Required phenotype endpoint. |
| morphology parent | `METPO:1000059` | Supplied parent. |
| red pigmentation | label only | Prodigiosin-associated assay phenotype. |
| violet/purple pigmentation | label only | Violacein-associated phenotype. |
| brown/black pigmentation | label only | Melanin-associated phenotype. |
| orange/pink/red yeast pigmentation | label only | Carotenoid-associated phenotype. |

### Pigments, precursors, and metabolites

* Prodigiosin; 2-methyl-3-*n*-amyl-pyrrole (MAP); 4-methoxy-2,2′-bipyrrole-5-carbaldehyde (MBC); trans-2-octenal; L-proline; pyruvate; malonyl-CoA; S-adenosyl-L-methionine.
* Violacein; deoxyviolacein; prodeoxyviolacein; proviolacein; chromopyrrolic acid; L-tryptophan; molecular oxygen; NADPH.
* Melanin; DOPA-melanin/eumelanin; DHN-melanin; pyomelanin; L-tyrosine; L-DOPA; dopaquinone; homogentisate/homogentisic acid; 4-hydroxyphenylpyruvate; malonyl-CoA; 1,3,6,8-tetrahydroxynaphthalene.
* Carotenoids; β-carotene; γ-carotene; lycopene; torulene; torularhodin; bacteriochlorophyll.

Before YAML insertion, chemical nodes should be resolved against ChEBI by exact structure and protonation state. “Melanin,” “crude violacein,” and carotenoid mixtures are material classes rather than single defined compounds and should not be assigned a narrow chemical identifier without validation.

### Genes, proteins, operons, and regulatory systems

* `pigA–pigN` operon; optional `pigO` in strains that possess it; PigB, PigD, PigE, PigF; PigP.
* CpxR, MetR, RcsB, FlhDC, SlyA; CviI, CviR, VitR, VioS.
* `vioABCDE`; VioA, VioB, VioC, VioD, VioE.
* 4-hydroxyphenylpyruvate dioxygenase; homogentisate 1,2-dioxygenase/HmgA.
* Tyrosinase, laccase/multicopper oxidase, polyketide synthase.
* PpsR and photopigment-biosynthesis genes for aerobic anoxygenic phototrophs.

These should generally remain strain-qualified gene/protein nodes until mapped to a specific genome accession or UniProt record. The same regulator can have different phenotypic effects in different *Serratia* backgrounds.

### Pathways and biological processes

* Prodigiosin biosynthesis: MAP and MBC branches followed by condensation.
* Violacein biosynthesis from two L-tryptophan molecules.
* Quorum sensing through CviIR and AHL.
* Tyrosine degradation to homogentisate and pyomelanin.
* DOPA-melanin biosynthesis.
* DHN-melanin/polyketide biosynthesis.
* Carotenoid biosynthesis and intracellular or membrane accumulation.
* Photopigment biosynthesis and photosystem assembly.
* Oxidative polymerization and auto-oxidation.

### Environmental and experimental nodes

* Temperature, light intensity, light/dark regime, oxygen concentration, pH, salinity, nutrient composition, phosphate availability, precursor supplementation, cell density, oxidative or envelope stress.
* χ bacteriophage infection and χ-induced cell lysate.
* Gene deletion, insertion mutation, operon transfer, promoter replacement, precursor-pathway overexpression, fermentation optimization.
* Readouts: colony/culture color, absorbance at 535 nm, pigment titer, reporter activity, spectroscopy, chromatography.

### Cellular localization nodes

* Cytoplasm/intracellular accumulation.
* Cytoplasmic membrane or other membrane-associated pigment.
* Fungal cell wall.
* Extracellular space/culture supernatant.
* Chromatophore and photosynthetic complex.

## 3. Candidate causal edges

“High” denotes direct genetic, biochemical-reconstitution, or controlled intervention evidence. “Moderate” denotes direct observations with incomplete molecular mediation. “Review-only” should not normally enter the graph until a primary taxon-specific source is obtained.

| # | Subject — predicate → object | Scope and strength | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|---|
| 1 | `pigA–pigN` operon — enables biosynthesis of → prodigiosin | *S. marcescens*; high | 10.1038/s41598-024-68747-3 | “pig operon, containing genes essential for pigment biosynthesis” | Curate as an operon-to-process edge; individual Pig enzyme functions can be child edges. (esteves2024serratiamarcescensatcc pages 1-2) |
| 2 | prodigiosin — causes → red pigmentation | *S. marcescens*; high | 10.1038/s41598-024-68747-3 | “vibrant red pigment called prodigiosin” | Strong proximate pigment-to-trait edge. (esteves2024serratiamarcescensatcc pages 1-2) |
| 3 | PigB/PigD/PigE — contribute to production of → MAP | *Serratia*; moderate | 10.3389/fbioe.2020.00344 | “pigD, pigE, and pigB encode proteins that are involved in the production of MAP” | Source summarizes prior assignments; obtain original enzyme papers before fine-grained reaction curation. (sun2020improvedprodigiosinproduction pages 1-2) |
| 4 | PigA and PigF–PigN — contribute to production of → MBC | *Serratia*; moderate | 10.3389/fbioe.2020.00344 | “pigA and pigF–pigN encode proteins responsible for the synthesis of MBC” | Curate initially as a module-level edge. (sun2020improvedprodigiosinproduction pages 1-2) |
| 5 | MAP + MBC — condense to form → prodigiosin | *Serratia*; high/moderate | 10.1038/s41598-024-68747-3 | “These two molecules are joined by a condensation reaction to form the tripyrrole prodigiosin” | Suitable chemical-process edge; enzyme identity should be separately sourced. (esteves2024serratiamarcescensatcc pages 1-2) |
| 6 | CpxR — represses transcription of → `pig` gene cluster | *S. marcescens* JNB 5-1; high | 10.3389/fbioe.2020.00344 | “CpxR could bind to the promoter of the pig gene cluster and repress the transcription levels” | Direct EMSA plus mutant evidence. (sun2020improvedprodigiosinproduction pages 1-2) |
| 7 | `cpxR` disruption — increases → prodigiosin production | JNB 5-1; high | 10.3389/fbioe.2020.00344 | “insertion mutation of cpxR … increased the production of PG” | Curate as a perturbation edge, not as the normal physiological direction. (sun2020improvedprodigiosinproduction pages 1-2) |
| 8 | increased proline/serine/methionine precursor supply — increases → prodigiosin production | Engineered JNB 5-1; high but engineering-specific | 10.3389/fbioe.2020.00344 | Engineered strain reached “5.83 g/L” and “increased by 41.9%” | Strong application evidence; the intervention combined precursor genes with the `cpxR` locus and should not be generalized to all strains. (sun2020improvedprodigiosinproduction pages 1-2) |
| 9 | MetR — represses → PigP expression | JNB 5-1; high | 10.1128/AEM.02241-19 | “MetR directly binding to the promoter region of … PigP and hence negatively regulated” | Direct promoter-binding mechanism. (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| 10 | PigP — positively regulates → prodigiosin synthesis/`pig` operon | Certain *Serratia* strains; moderate | 10.1128/AEM.02241-19 | “prodigiosin-synthesis positive regulator PigP” | Mark strain-specific; PigP's role is not established in every *S. marcescens* isolate. (pan2020lysrtypetranscriptionalregulator pages 1-2) |
| 11 | RcsB — represses → FlhDC | JNB5-1; high | 10.1128/AEM.02052-20 | RcsB bound the `flhDC` promoter; `flhC` and `flhD` rose 3.42- and 6.29-fold in the mutant | Supports an indirect branch to prodigiosin rather than direct RcsB–`pig` binding. (pan2021regulatorrcsbcontrols pages 10-12) |
| 12 | FlhDC — activates → prodigiosin synthesis | JNB5-1; moderate/high | 10.1128/AEM.02052-20 | Evidence identifies FlhDC as an activator linking RcsB to pigment synthesis | Curate with the RcsB paper’s strain context. (pan2021regulatorrcsbcontrols pages 10-12) |
| 13 | SlyA — positively regulates → prodigiosin production | One *S. marcescens* background; high phenotype, incomplete direct mechanism | 10.3389/fmicb.2021.793202 | “delete … slyA to generate a non-pigmented mutant. The ΔslyA strain loses prodigiosin synthesis capacity” | Do not assert direct promoter binding from this evidence. (xiang2022transcriptomicanalysisreveals pages 1-2) |
| 14 | downregulation of `pig` genes — decreases → red pigmentation | Spontaneous *S. marcescens* color morphotypes; moderate | 10.3389/fmicb.2021.793202 | “Most of the pig genes are significantly downregulated … which directly lead to prodigiosin dyssynthesis” | Demonstrates that an intact cluster does not guarantee pigmentation. (xiang2022transcriptomicanalysisreveals pages 1-2) |
| 15 | χ phage infection — increases → prodigiosin production | *S. marcescens* ATCC 274; high | 10.1038/s41598-024-68747-3 | “greater than fivefold overproduction of prodigiosin” | Recent, strong, strain- and phage-specific edge. (esteves2024serratiamarcescensatcc pages 1-2) |
| 16 | χ-induced cell lysate — increases transcription of → `pig` operon | ATCC 274; high | 10.1038/s41598-024-68747-3 | “threefold increase in transcription of the pig operon” | Response appears promoter-mediated; causal lysate molecule remains unknown. (esteves2024serratiamarcescensatcc pages 1-2) |
| 17 | native `Ppig` regulatory region — mediates → χ-induced pigmentation increase | ATCC 274; high | 10.1038/s41598-024-68747-3 | “Replacement … with a constitutive promoter abolished the pigmentation increase” | Strong promoter-dependence evidence. (esteves2024serratiamarcescensatcc pages 1-2) |
| 18 | L-tryptophan — precursor of → violacein | *C. violaceum* enzymes; high | 10.1021/bi061998z | “violacein arises by enzymatic oxidation and coupling of two molecules of L-tryptophan” | Core chemical precursor edge. (balibar2006invitrobiosynthesis pages 1-2) |
| 19 | VioA + VioB — oxidize and dimerize → L-tryptophan-derived intermediate | In-vitro reconstitution; high | 10.1021/bi061998z | “VioA and … VioB work in conjunction to oxidize and dimerize L-tryptophan” | Suitable direct enzyme-module edge. (balibar2006invitrobiosynthesis pages 1-2) |
| 20 | VioE — directs/rearranges intermediate to → prodeoxyviolacein | In vitro; high | 10.1021/bi061998z | “In the presence of VioE, the intermediate … undergoes … indole rearrangement to prodeoxyviolacein” | High-confidence pathway edge. (balibar2006invitrobiosynthesis pages 1-2) |
| 21 | VioD — hydroxylates → prodeoxyviolacein/proviolacein branch | In vitro; high | 10.1021/bi061998z | “VioD hydroxylates one indole ring at the 5-position to yield proviolacein” | Curate reaction after checking exact substrate naming in the full pathway. (balibar2006invitrobiosynthesis pages 1-2) |
| 22 | VioC — completes oxidation to → violacein | In vitro; high | 10.1021/bi061998z | “VioC then acts … to create the oxindole and complete violacein formation” | High-confidence terminal biosynthetic edge. (balibar2006invitrobiosynthesis pages 1-2) |
| 23 | violacein — causes → violet/purple pigmentation | *C. violaceum*; high | 10.1021/bi061998z | “purple chromobacterial pigment violacein” | Strong pigment-to-phenotype edge. (balibar2006invitrobiosynthesis pages 1-2) |
| 24 | high cell density/AHL–CviIR quorum sensing — activates → violacein production | *C. violaceum*; high | 10.1128/msystems.01397-23 | “At high cell density, CviIR activated … violacein” | Recent primary evidence; can be decomposed into CviI→AHL→CviR→`vio` operon after sourcing exact direct-binding assays. (batista2024aquorumsensingregulatory pages 1-3) |
| 25 | VitR — represses → `vioS` | *C. violaceum*; high | 10.1128/msystems.01397-23 | “VitR … acts as a dedicated repressor of vioS” | Upstream regulatory branch. (batista2024aquorumsensingregulatory pages 1-3) |
| 26 | VioS — inhibits → CviR | *C. violaceum*; high | 10.1128/msystems.01397-23 | “Increased VioS leads to direct inhibition of the CviR regulator by protein-protein interaction” | Direct protein-interaction mechanism. (batista2024aquorumsensingregulatory pages 1-3) |
| 27 | increased tryptophan supply + `vioABCDE` — increases → crude violacein production | Engineered *E. coli*; high | 10.1186/s12934-015-0192-x | 0.60 ± 0.01 g/L, fourfold above control; 1.75 g/L and 36 mg/L/h in a 5-L reactor | Engineering implementation; crude product contains deoxyviolacein. (fang2015highcrudeviolacein pages 1-2) |
| 28 | 4-hydroxyphenylpyruvate dioxygenase — produces/supports production of → homogentisate | *S. oneidensis* MR-1; high | 10.1111/j.1574-6941.2009.00670.x | Enzymes were “responsible for homogentisate production and oxidation, respectively” | Map enzyme/gene precisely before assigning an EC or UniProt CURIE. (turick2009theroleof pages 1-2) |
| 29 | HmgA/homogentisate 1,2-dioxygenase — consumes/oxidizes → homogentisate | MR-1; high | 10.1111/j.1574-6941.2009.00670.x | “homogentisate 1,2-dioxygenase [is responsible for] … oxidation” | Loss of this sink can favor extracellular homogentisate and pyomelanin; add deletion edge only from explicit mutant results. (turick2009theroleof pages 1-2) |
| 30 | homogentisate auto-oxidation and polymerization — produces → pyomelanin | Bacterial pyomelanin pathway; high/moderate | 10.1111/j.1574-6941.2009.00670.x | “Subsequent auto-oxidation and self-polymerization of homogentisate yields pyomelanin” | Oxygen/redox conditions should be represented because polymerization is nonenzymatic. (turick2009theroleof pages 1-2) |
| 31 | tyrosine availability — increases/supports → pyomelanin production | MR-1; high, medium-specific | 10.1111/j.1574-6941.2009.00670.x | Study demonstrates the role of “organic precursors and their concentrations in pyomelanin production” | Use concentration-qualified experimental context. (turick2009theroleof pages 1-2) |
| 32 | tyrosine → L-DOPA → dopaquinone — contributes to → DOPA-melanin | Broad microbial claim; review-supported | 10.1186/s12934-023-02276-y | “tyrosine into L-Dopa … transformed into dopaquinone by … tyrosinase and laccase” | Do not curate as universal; obtain organism-specific primary evidence. (elzawawy2024bioproductionandoptimization pages 1-2) |
| 33 | malonyl-CoA + polyketide synthase — produces → THN/DHN-melanin precursor | Broad microbial claim; review-supported | 10.1186/s12934-023-02276-y | “step-by-step … condensation of five molecules of malonyl-coenzyme A … formation of … THN” | Keep separate from DOPA- and pyomelanin branches. (elzawawy2024bioproductionandoptimization pages 1-2) |
| 34 | pigment accumulation in fungal cell wall or extracellular space — causes → fungal melanization | Fungi; review-supported | 10.1186/s12934-024-02614-8 | “localization … in the cell wall or secreted into extracellular space” | Localization edge is plausible but requires species-specific primary evidence for curation. (qin2024melanininfungi pages 1-2) |
| 35 | carotenoid identity and concentration — determine → orange/salmon/pink/red colony color | *Rhodotorula* spp.; review-supported | 10.3390/fermentation10040190 | “Colonies can have an orange, salmon, pink, or red color depending on the type and concentration of pigments” | Good phenotype model, but add direct strain-level measurements before causal curation. (ochoavinals2024currentadvancesin pages 1-2) |
| 36 | continuous light — transiently decreases → photosynthesis-gene expression | *Sediminicoccus* sp. KRV36; moderate/high | 10.1128/msystems.01311-23 | Expression was “transiently downregulated in the first 2 hours … but recovered … within 24 hours” | Time-dependent edge; not a permanent repression. (tomasch2024aphotoheterotrophicbacterium pages 1-2) |
| 37 | membrane-bound carotenoid excess — protects → bacteriochlorophyll synthesis/photosystem assembly | KRV36; moderate | 10.1128/msystems.01311-23 | Carotenoids and oxidative-stress genes provided ROS-scavenging potential “safeguarding bacteriochlorophyll synthesis” | Mechanistic interpretation is strong but not a simple pigmentation edge. Curate only in a photopigment subgraph. (tomasch2024aphotoheterotrophicbacterium pages 1-2) |
| 38 | bacteriochlorophyll/carotenoid-containing chromatophores — contribute to → coral-red pigmentation | KRV36; uncertain | 10.1128/msystems.01311-23 | Cells contained 100–180 chromatophores and cultures formed coral-red aggregates | Association is not sufficient to assign which pigment causes the visible red color; defer. (tomasch2024aphotoheterotrophicbacterium pages 1-2) |

## 4. Recommended graph architecture

A compact, defensible initial YAML should use a shared terminal pattern:

1. **Environmental or experimental input** regulates a transcription factor, promoter, precursor supply, or enzyme.
2. **Regulatory factor** alters expression of a pigment biosynthetic module.
3. **Biosynthetic module** converts defined precursor(s) to a pigment.
4. **Pigment accumulation/localization** causes `METPO:1003021`.

Recommended first-pass modules are:

* **Prodigiosin:** CpxR/MetR/RcsB/SlyA/phage stress → `pigA–pigN` expression → MAP + MBC → prodigiosin → red pigmentation.
* **Violacein:** cell density/AHL/CviIR and VitR–VioS regulation → `vioABCDE`; L-tryptophan → violacein → violet pigmentation.
* **Pyomelanin:** tyrosine → 4-hydroxyphenylpyruvate → homogentisate; competition between HmgA-mediated degradation and extracellular auto-oxidation/polymerization → pyomelanin → brown/black pigmentation.

DOPA-melanin, DHN-melanin, carotenoids, and photopigments should be additional modules, not merged into the pyomelanin chain.

## 5. Recent developments, applications, and statistics

### Recent mechanistic advances

The strongest 2024 addition is the demonstration that χ phage infection of *S. marcescens* ATCC 274 produces more than a fivefold increase in prodigiosin. The response required active infection/flagellar susceptibility, became statistically detectable three hours after phage addition, and depended on the native `pig` promoter. χ-induced lysate raised reporter output to 22 Miller units after two hours—3.3-fold over the fresh-medium control—and later reached 204 Miller units. (esteves2024serratiamarcescensatcc pages 3-5, esteves2024serratiamarcescensatcc pages 1-2)

A 2024 *C. violaceum* study placed pigmentation in a regulatory cascade: VitR represses `vioS`; VioS directly inhibits CviR; and high-cell-density CviIR signaling activates violacein production. This supports graphing cell-density sensing upstream of pigment biosynthesis rather than treating violacein production as constitutive. (batista2024aquorumsensingregulatory pages 1-3)

A 2024 study of Arctic *Sediminicoccus* KRV36 showed that continuous illumination does not always suppress photopigment synthesis. The strain retained bacteriochlorophyll, contained approximately 100–180 chromatophores per cell, and restored initially reduced photosynthesis-gene expression within 24 hours. This is an important warning against universalizing light-response edges across phototrophic bacteria. (tomasch2024aphotoheterotrophicbacterium pages 1-2)

### Production and real-world applications

Recent reviews identify food, cosmetics, textiles, pharmaceuticals, medicine, and electronics among current or proposed sectors. Regulatory approval is pigment- and jurisdiction-specific; one 2024 review lists indigo, riboflavin, β-carotene, lycopene, astaxanthin, and Monascus pigments among a limited set receiving FDA or EFSA approval, but each product’s organism, purity, intended use, and current regulatory status must be verified independently. The same review estimates a broad pigment-market value of US$33.2–49.1 billion by 2027; this is not the microbial-pigment market alone. (huang2024bacterialpigmentsas pages 1-2)

Microbial pigments have practical production advantages—short microbial life cycles, reduced seasonality, fermentability, and possible use of molasses, corncobs, bagasse, straw, peels, glycerol, wastewater, or lignocellulosic hydrolysates. Nevertheless, downstream extraction, purification, safety, stability, and cost remain major commercialization constraints. (huang2024bacterialpigmentsas pages 1-2, barreto2023microbialpigmentsmajor pages 1-2, ochoavinals2024currentadvancesin pages 1-2)

Illustrative quantitative implementations include:

* Engineered *S. marcescens* produced 5.83 g/L prodigiosin, 41.9% above its parent, after relieving CpxR repression and augmenting precursor pathways. (sun2020improvedprodigiosinproduction pages 1-2)
* Engineered *E. coli* produced 0.60 ± 0.01 g/L crude violacein in flasks, fourfold above a non-upregulated control, and 1.75 g/L at 36 mg/L/h in a 5-L batch reactor from glucose without added tryptophan. (fang2015highcrudeviolacein pages 1-2)
* Optimized *Streptomyces djakartensis* NSS-3 yielded 118.73 mg pyomelanin per 10 mL, a 4.19-fold increase. The purified material had an in-vitro SPF of 18.5 and antioxidant IC50 of 18.03 µg/mL; these are laboratory properties, not evidence of an approved sunscreen or therapeutic. (elzawawy2024bioproductionandoptimization pages 1-2)
* A 2024 carotenoid review reports a market increase from US$1.5 billion in 2019 to a projected US$2.0 billion in 2026, approximately 4.2% annually. In *Rhodotorula*, β-carotene can account for up to 70% of total carotenoids, although values are strain- and condition-dependent. (ochoavinals2024currentadvancesin pages 1-2)
* A 2023 review gives an illustrative price comparison of approximately US$700–800 per 100 g for tartrazine versus US$1,000 per 100 g for microbial carotenoid, emphasizing that extraction and upstream/downstream processing strongly affect cost. These figures should not be treated as stable market quotations. (barreto2023microbialpigmentsmajor pages 1-2)

The expert consensus across recent reviews is that metabolic engineering, inexpensive waste-derived feedstocks, and optimized fermentation can improve production, but generalized claims that microbial pigments are inherently non-toxic or environmentally benign are too broad. Safety depends on pigment identity, impurities, production organism, extraction solvent, dose, and application. (huang2024bacterialpigmentsas pages 1-2, barreto2023microbialpigmentsmajor pages 1-2)

## 6. Warnings: claims not yet ready for TraitMech curation

1. **Do not make “pigment biosynthetic gene cluster → pigmentation” universal.** Spontaneous non-pigmented *S. marcescens* morphotypes retained the complete `pigA–N` cluster but downregulated it; a cluster can be present yet silent. (xiang2022transcriptomicanalysisreveals pages 1-2)
2. **Do not merge all melanins.** Pyomelanin from homogentisate, DOPA-melanin from tyrosine/L-DOPA, and DHN-melanin from polyketide metabolism have different precursors and enzymes. (turick2009theroleof pages 1-2, elzawawy2024bioproductionandoptimization pages 1-2)
3. **Do not assert that HmgA directly produces pigment.** HmgA consumes homogentisate; reduced HmgA activity may indirectly favor pyomelanin by preserving the precursor.
4. **Do not generalize regulator polarity across taxa or strains.** PigP, RpoS, quorum-sensing systems, and promoter architectures vary among *Serratia* strains. The χ response is specifically established for ATCC 274. (esteves2024serratiamarcescensatcc pages 1-2, xiang2022transcriptomicanalysisreveals pages 1-2)
5. **Do not curate the identity of the χ-lysate signal.** The lysate is causal, but its active molecular component is unresolved. (esteves2024serratiamarcescensatcc pages 3-5)
6. **Do not infer visible pigmentation from fluorescence screening or absorption alone.** These assays may detect photopigments without proving which molecule causes colony color.
7. **Treat light, temperature, oxygen, pH, salts, and nutrients as context-qualified variables.** Effects can be nonlinear, time-dependent, and taxon-specific. For example, prodigiosin is efficiently produced near 28°C and sharply reduced at ≥37°C in the cited *Serratia* context, while Arctic KRV36 maintains pigments under continuous light. (tomasch2024aphotoheterotrophicbacterium pages 1-2, sun2020improvedprodigiosinproduction pages 1-2)
8. **Review-derived tyrosinase, laccase, PKS, carotenoid, and industrial claims need primary evidence** before being represented as species-level causal edges.
9. **Avoid unverified ontology assignments.** Exact ChEBI, GO, EC, Rhea, KEGG, MetaCyc, UniProt, and NCBITaxon CURIEs should be added only after database lookup against the exact molecule, reaction, protein, strain, and release.
10. **Applications are not phenotype mechanisms.** Antimicrobial, anticancer, antioxidant, radioprotective, textile-dyeing, and food-coloring effects belong in downstream application graphs, not in the core causal chain ending in pigmentation.

## 7. DOI-first bibliography

### Recent sources, 2023–2024

1. Esteves NC, Scharf BE. “*Serratia marcescens* ATCC 274 increases production of the red pigment prodigiosin in response to Chi phage infection.” *Scientific Reports* 14, 17750. **Published July 2024.** DOI: [10.1038/s41598-024-68747-3](https://doi.org/10.1038/s41598-024-68747-3). (esteves2024serratiamarcescensatcc pages 1-2)
2. Batista BB et al. “A quorum-sensing regulatory cascade for siderophore-mediated iron homeostasis in *Chromobacterium violaceum*.” *mSystems* 9. **Published March 19, 2024.** DOI: [10.1128/msystems.01397-23](https://doi.org/10.1128/msystems.01397-23). (batista2024aquorumsensingregulatory pages 1-3)
3. Tomasch J et al. “A photoheterotrophic bacterium from Iceland has adapted its photosynthetic machinery to the long days of polar summer.” *mSystems* 9. **Published February 20, 2024.** DOI: [10.1128/msystems.01311-23](https://doi.org/10.1128/msystems.01311-23). (tomasch2024aphotoheterotrophicbacterium pages 1-2)
4. Huang X et al. “Bacterial Pigments as a Promising Alternative to Synthetic Colorants: From Fundamentals to Applications.” *Journal of Microbiology and Biotechnology* 34:2153–2165. **First published online September 11, 2024.** DOI: [10.4014/jmb.2404.04018](https://doi.org/10.4014/jmb.2404.04018). (huang2024bacterialpigmentsas pages 1-2)
5. Qin Y, Xia Y. “Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering.” *Microbial Cell Factories* 23:334. **2024.** DOI: [10.1186/s12934-024-02614-8](https://doi.org/10.1186/s12934-024-02614-8). (qin2024melanininfungi pages 1-2)
6. Ochoa-Viñals N et al. “Current Advances in Carotenoid Production by *Rhodotorula* sp.” *Fermentation* 10:190. **Published March 30, 2024.** DOI: [10.3390/fermentation10040190](https://doi.org/10.3390/fermentation10040190). (ochoavinals2024currentadvancesin pages 1-2)
7. El-Zawawy NA et al. “Bioproduction and optimization of newly characterized melanin pigment from *Streptomyces djakartensis* NSS-3…” *Microbial Cell Factories* 23:23. **2024.** DOI: [10.1186/s12934-023-02276-y](https://doi.org/10.1186/s12934-023-02276-y). (elzawawy2024bioproductionandoptimization pages 1-2)
8. Barreto JVO et al. “Microbial Pigments: Major Groups and Industrial Applications.” *Microorganisms* 11:2920. **Published December 4, 2023.** DOI: [10.3390/microorganisms11122920](https://doi.org/10.3390/microorganisms11122920). (barreto2023microbialpigmentsmajor pages 1-2)

### Foundational mechanistic sources

9. Balibar CJ, Walsh CT. “In Vitro Biosynthesis of Violacein from L-Tryptophan by the Enzymes VioA–E from *Chromobacterium violaceum*.” *Biochemistry* 45:15444–15457. **Published online December 19, 2006.** DOI: [10.1021/bi061998z](https://doi.org/10.1021/bi061998z). (balibar2006invitrobiosynthesis pages 1-2)
10. Turick CE et al. “The role of 4-hydroxyphenylpyruvate dioxygenase in enhancement of solid-phase electron transfer by *Shewanella oneidensis* MR-1.” *FEMS Microbiology Ecology* 68:223–235. **First published March 18, 2009.** DOI: [10.1111/j.1574-6941.2009.00670.x](https://doi.org/10.1111/j.1574-6941.2009.00670.x). (turick2009theroleof pages 1-2)
11. Fang M-Y et al. “High crude violacein production from glucose by *Escherichia coli* engineered with interactive control of tryptophan pathway and violacein biosynthetic pathway.” *Microbial Cell Factories* 14:8. **2015.** DOI: [10.1186/s12934-015-0192-x](https://doi.org/10.1186/s12934-015-0192-x). (fang2015highcrudeviolacein pages 1-2)
12. Pan X et al. “LysR-Type Transcriptional Regulator MetR Controls Prodigiosin Production…” *Applied and Environmental Microbiology* 86:e02241-19. **Published February 3, 2020.** DOI: [10.1128/AEM.02241-19](https://doi.org/10.1128/AEM.02241-19). (pan2020lysrtypetranscriptionalregulator pages 1-2)
13. Sun Y et al. “Improved Prodigiosin Production by Relieving CpxR Temperature-Sensitive Inhibition.” *Frontiers in Bioengineering and Biotechnology* 8:344. **Published June 3, 2020.** DOI: [10.3389/fbioe.2020.00344](https://doi.org/10.3389/fbioe.2020.00344). (sun2020improvedprodigiosinproduction pages 1-2)
14. Pan X et al. “Regulator RcsB Controls Prodigiosin Synthesis and Various Cellular Processes in *Serratia marcescens* JNB5-1.” *Applied and Environmental Microbiology* 87. **2021.** DOI: [10.1128/AEM.02052-20](https://doi.org/10.1128/AEM.02052-20). (pan2021regulatorrcsbcontrols pages 10-12)
15. Xiang T et al. “Transcriptomic Analysis Reveals Competitive Growth Advantage of Non-pigmented *Serratia marcescens* Mutants.” *Frontiers in Microbiology* 12:793202. **Published January 4, 2022.** DOI: [10.3389/fmicb.2021.793202](https://doi.org/10.3389/fmicb.2021.793202). (xiang2022transcriptomicanalysisreveals pages 1-2)
16. Venil CK, Zakaria ZA, Ahmad WA. “Bacterial pigments and their applications.” *Process Biochemistry* 48:1065–1079. **Published July 2013.** DOI: [10.1016/j.procbio.2013.06.006](https://doi.org/10.1016/j.procbio.2013.06.006). This is the supplied existing evidence and supports the broad pigment/application context, but the inaccessible full text was not used for new fine-grained causal edges.

References

1. (barreto2023microbialpigmentsmajor pages 1-2): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 102 citations.

2. (qin2024melanininfungi pages 1-2): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

3. (ochoavinals2024currentadvancesin pages 1-2): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 57 citations.

4. (fang2015highcrudeviolacein pages 1-2): Ming-Yue Fang, Chong Zhang, Song Yang, Jin-Yu Cui, Pei-Xia Jiang, Kai Lou, Masaaki Wachi, and Xin-Hui Xing. High crude violacein production from glucose by escherichia coli engineered with interactive control of tryptophan pathway and violacein biosynthetic pathway. Microbial Cell Factories, Jan 2015. URL: https://doi.org/10.1186/s12934-015-0192-x, doi:10.1186/s12934-015-0192-x. This article has 122 citations and is from a peer-reviewed journal.

5. (esteves2024serratiamarcescensatcc pages 1-2): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 7 citations and is from a peer-reviewed journal.

6. (sun2020improvedprodigiosinproduction pages 1-2): Yang Sun, Lijun Wang, Xuewei Pan, Tolbert Osire, Haitian Fang, Huiling Zhang, Shang-Tian Yang, Taowei Yang, and Zhiming Rao. Improved prodigiosin production by relieving cpxr temperature-sensitive inhibition. Frontiers in Bioengineering and Biotechnology, Jun 2020. URL: https://doi.org/10.3389/fbioe.2020.00344, doi:10.3389/fbioe.2020.00344. This article has 41 citations.

7. (pan2020lysrtypetranscriptionalregulator pages 1-2): Xuewei Pan, Changhao Sun, Mi Tang, Jiajia You, Tolbert Osire, Youxi Zhao, Meijuan Xu, Xian Zhang, Minglong Shao, Shangtian Yang, Taowei Yang, and Zhiming Rao. Lysr-type transcriptional regulator metr controls prodigiosin production, methionine biosynthesis, cell motility, h <sub>2</sub> o <sub>2</sub> tolerance, heat tolerance, and exopolysaccharide synthesis in serratia marcescens. Feb 2020. URL: https://doi.org/10.1128/aem.02241-19, doi:10.1128/aem.02241-19. This article has 49 citations and is from a peer-reviewed journal.

8. (pan2021regulatorrcsbcontrols pages 10-12): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 30 citations and is from a peer-reviewed journal.

9. (xiang2022transcriptomicanalysisreveals pages 1-2): Tingting Xiang, Wei Zhou, Cailing Xu, Jing Xu, Rui Liu, Nuo Wang, Liang Xu, Yu Zhao, Minhui Luo, Xiaoxin Mo, Zeyang Mao, and Yongji Wan. Transcriptomic analysis reveals competitive growth advantage of non-pigmented serratia marcescens mutants. Frontiers in Microbiology, Jan 2022. URL: https://doi.org/10.3389/fmicb.2021.793202, doi:10.3389/fmicb.2021.793202. This article has 12 citations and is from a peer-reviewed journal.

10. (balibar2006invitrobiosynthesis pages 1-2): Carl J. Balibar and Christopher T. Walsh. In vitro biosynthesis of violacein from l-tryptophan by the enzymes vioa-e from chromobacterium violaceum. Biochemistry, 45 51:15444-57, Dec 2006. URL: https://doi.org/10.1021/bi061998z, doi:10.1021/bi061998z. This article has 248 citations and is from a peer-reviewed journal.

11. (batista2024aquorumsensingregulatory pages 1-3): Bianca B. Batista, Vinicius M. de Lima, Beatriz A. Picinato, Tie Koide, and José F. da Silva Neto. A quorum-sensing regulatory cascade for siderophore-mediated iron homeostasis in <i>chromobacterium violaceum</i>. Apr 2024. URL: https://doi.org/10.1128/msystems.01397-23, doi:10.1128/msystems.01397-23. This article has 13 citations and is from a peer-reviewed journal.

12. (turick2009theroleof pages 1-2): Charles E. Turick, Alex S. Beliaev, Brian A. Zakrajsek, Catherine L. Reardon, Daniel A. Lowy, Tara E. Poppy, Andrea Maloney, and Amy A. Ekechukwu. The role of 4-hydroxyphenylpyruvate dioxygenase in enhancement of solid-phase electron transfer by shewanella oneidensis mr-1. FEMS Microbiology Ecology, 68:223-225, May 2009. URL: https://doi.org/10.1111/j.1574-6941.2009.00670.x, doi:10.1111/j.1574-6941.2009.00670.x. This article has 66 citations and is from a peer-reviewed journal.

13. (elzawawy2024bioproductionandoptimization pages 1-2): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 50 citations and is from a peer-reviewed journal.

14. (tomasch2024aphotoheterotrophicbacterium pages 1-2): Jürgen Tomasch, Karel Kopejtka, Tomáš Bílý, Alastair T. Gardiner, Zdenko Gardian, Sahana Shivaramu, Michal Koblížek, and David Kaftan. A photoheterotrophic bacterium from iceland has adapted its photosynthetic machinery to the long days of polar summer. Mar 2024. URL: https://doi.org/10.1128/msystems.01311-23, doi:10.1128/msystems.01311-23. This article has 5 citations and is from a peer-reviewed journal.

15. (esteves2024serratiamarcescensatcc pages 3-5): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 7 citations and is from a peer-reviewed journal.

16. (huang2024bacterialpigmentsas pages 1-2): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 40 citations and is from a peer-reviewed journal.