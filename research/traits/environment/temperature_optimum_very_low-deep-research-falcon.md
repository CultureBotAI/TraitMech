---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:04:33.512508'
end_time: '2026-08-04T04:10:37.773506'
duration_seconds: 364.26
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum very low
  trait_identifier: METPO:1000441
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ at or below approximately 10 \xB0C, characteristic of psychrophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Psychrophile, TO_<=10
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports growth at very low temperatures
    as the psychrophilic optimum.)'
  causal_graph_summary: 'temperature_optimum_very_low_psychrophile_setpoint: 17 nodes,
    11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_very_low.yaml`.

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
- **Trait label:** temperature optimum very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000441
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature at or below approximately 10 °C, characteristic of psychrophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, TO_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic optimum.)
- **Existing causal graph summary:** temperature_optimum_very_low_psychrophile_setpoint: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_very_low.yaml`.

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


# Curation report: microbial “temperature optimum very low”

**Target trait:** `METPO:1000441`  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** `METPO:1000304`  
**Synonyms:** Psychrophile; TO_<=10

## 1. Scope and current interpretation

`METPO:1000441` should represent an **assay-observed temperature optimum**, namely that maximal or near-maximal microbial growth occurs at an ambient temperature **at or below approximately 10 °C**. The preferred evidence is a growth-rate or biomass-versus-temperature curve under otherwise controlled conditions, not merely isolation from a cold habitat, survival after freezing, transcriptional response to cold, or detectable growth at 4–10 °C.

This ontology class is **narrower than the conventional microbiological definition of a psychrophile**. Recent reviews commonly define psychrophiles as organisms growing at 0 °C, with optimum around or below 15 °C and maximum around or below 20 °C; psychrotrophs/psychrotolerants can grow in the cold but have optima or maxima above those thresholds. Thus an organism with optimum 13–15 °C may be a conventional psychrophile but does not necessarily satisfy the supplied `TO_<=10` threshold. Conversely, growth at −10 °C does not establish an optimum ≤10 °C unless temperatures above −10 °C were compared. (ramon2023ageneraloverview pages 1-2, bao2023miningofkey pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 1-2)

**Boundary exclusions** should include:

- **Cold tolerance/psychrotolerance:** capacity to grow or persist at low temperature while having a warmer optimum.
- **Minimum growth temperature:** the lowest temperature permitting detectable growth.
- **Maximum growth temperature:** useful for conventional psychrophile classification but not equivalent to the optimum.
- **Freeze survival or metabolic activity without growth:** relevant to cryoprotection, not sufficient for this trait.
- **Transient cold-shock response:** an acclimation program that also occurs in mesophiles.
- **Cold-active purified enzyme:** a molecular property that may contribute to cold growth but does not establish the organism-level optimum.

Examples illustrate the distinction: *Planococcus halocryophilus*, *Psychromonas ingrahamii*, and *Psychrobacter arcticus* can grow at −15, −12, and −10 °C, respectively, with reported generation times of approximately 50, 10, and 39 days, but these minima alone do not specify their optimum. *Psychrobacter cryopegella* can thrive at −10 °C and remain metabolically active at −20 °C, again demonstrating extreme cold activity rather than necessarily proving `TO_<=10`. (purwar2024adaptationsofpsychrophilic pages 3-4, moyer2017psychrophilesandpsychrotrophs pages 1-2)

## 2. Mechanistic model

Current expert understanding is that very-low-temperature growth is a **multifactorial systems phenotype**, not a single-gene trait. Low temperature reduces membrane fluidity, molecular diffusion and catalytic rates; increases viscosity; stabilizes inhibitory RNA secondary structures; perturbs protein folding and ribosome assembly; promotes extracellular and intracellular ice formation; and can increase reactive-oxygen burden. Psychrophilic physiology compensates through coordinated membrane remodeling, cold-efficient catalysis, macromolecular homeostasis, cryoprotection, antioxidant defense, transport, and energy-management mechanisms. (moyer2017psychrophilesandpsychrotrophs pages 2-3, ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10)

The strongest recent functional result in the retrieved literature is Li et al. (November 2024). Six *Rhodococcus* sp. RCBS9 proteins—small heat-shock protein, DPS, GroEL, USP-1, Cu/Zn-SOD, and USP-2—were heterologously expressed in *E. coli* BL21. At 10 °C, strains expressing DPS, GroEL, or USP-2 reached approximately OD600 1.4 after four hours, versus approximately 1.0–1.1 for vector control. This supports gene-to-low-temperature-growth edges, but only in a short-duration heterologous assay; it does not prove that any gene changes the thermal optimum or is necessary in the native strain. The authors also reported declining counts after eight hours and called for deeper validation. (li2024mechanismsunderlyingthe pages 10-12, li2024mechanismsunderlyingthe pages 12-13)

Bao et al. (July 2023) identified 124 candidate cold-adaptation genes in psychrotrophic *Pseudomonas fragi* D12, including 46 associated with membrane fluidity—four in unsaturated-fatty-acid synthesis and 42 in fatty-acid degradation—and 233 stress-response genes. Responses differed by temperature interval: 30→15 °C was associated with membrane-fluidity maintenance, extracellular polymer and compatible-solute production, and reduced ROS, whereas 15→4 °C preferentially induced chaperones and transcription factors. This is valuable mechanistic evidence but is primarily comparative-genomic/transcriptomic and comes from a psychrotroph, so it should not be asserted as a direct cause of `METPO:1000441`. (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7)

## 3. Candidate graph nodes

### Trait and assay nodes

- **temperature optimum very low** — `METPO:1000441`
- **parent temperature-optimum phenotype** — `METPO:1000304`
- Growth rate, generation time, biomass yield, OD600, colony formation
- Controlled ambient temperature; temperature series; incubation duration
- **Cold response** — `GO:0009409`

### Environmental and physical nodes

- Low ambient temperature; subzero temperature; freeze–thaw cycle
- Extracellular ice; intracellular ice; ice recrystallization
- Increased solvent viscosity; reduced molecular kinetic energy
- Membrane liquid-crystalline state; membrane fluidity
- Cold habitats such as sea ice, permafrost, glaciers, polar soils, and deep ocean—prefer ENVO grounding only after term lookup

### Cellular structures and processes

- Membrane / membrane component — `GO:0016020`
- Transport — `GO:0006810`
- Electron-transport chain — `GO:0022900`
- Ribosome biogenesis — `GO:0042254`
- Translation — `GO:0006412`
- Protein folding — `GO:0006457`
- Chaperone-mediated protein folding — `GO:0061077`
- Catalytic activity — `GO:0003824`
- RNA chaperone activity, membrane homeoviscous adaptation, cryoprotection, cellular redox homeostasis—retain as label-only pending exact ontology review

### Genes, proteins, enzymes, and complexes

- Fatty-acid desaturases and unsaturated-fatty-acid synthesis enzymes
- Cold-shock proteins/Csp-family RNA chaperones
- GroEL, GroES, DnaK, Clp proteins
- DPS/Dps-family DNA protection proteins
- Universal stress proteins USP-1 and USP-2
- Catalase — `EC:1.11.1.6`
- Superoxide dismutase — `EC:1.15.1.1`; Cu/Zn-SOD
- Antifreeze proteins and ice-binding proteins
- Ribosomal proteins and ribosome-assembly factors
- Two-component cold-sensing machinery, including DesK-like sensors—gene/protein grounding must be strain-specific
- Pili proteins identified in *P. fragi* D12—uncertain and taxon-specific

### Chemicals and extracellular products

- Unsaturated and polyunsaturated fatty acids; shorter-chain and branched fatty acids
- Palmitoleate (16:1), oleate (18:1), myristate (14:0)
- Compatible solutes: glycine betaine, trehalose, mannitol, sorbitol
- Exopolysaccharide — candidate `CHEBI:26220`, to be verified before release
- Reactive oxygen species — `CHEBI:26523`
- Extracellular polymeric substances and biofilm matrix

## 4. Candidate causal edges

The following artifact gives a compact graph-level overview. The expanded evidence notes below preserve the distinction between direct functional tests and broad adaptive inference.

| subject | predicate | object | candidate grounding | evidence type/strength | taxon or scope | DOI |
|---|---|---|---|---|---|---|
| low temperature / cold environment | activates or is sensed by | membrane state change and two-component cold response | low temperature [label-only]; membrane [GO:0016020]; two-component system [label-only]; cold response [GO:0009409] | Review-level, moderate; mechanistically plausible but mostly generalized, not trait-exclusive (ramon2023ageneraloverview pages 1-2) | Broad bacteria/archaea psychrophile literature | 10.1007/s42770-023-01057-4 |
| fatty-acid desaturase activity | increases | unsaturated membrane lipids | fatty acid desaturase [label-only]; unsaturated fatty acid [CHEBI label-only]; membrane lipid [label-only] | Review-level to comparative evidence, moderate; direct enzyme-to-lipid direction established, psychrophile generalization still broad (moyer2017psychrophilesandpsychrotrophs pages 3-5, purwar2024adaptationsofpsychrophilic pages 8-10) | Broad bacteria; stronger in membrane adaptation literature than in one taxon | 10.1016/B978-0-12-809633-8.02282-2; 10.37256/amtt.5220244537 |
| unsaturated membrane lipids | increases | membrane fluidity | unsaturated fatty acid [label-only]; membrane fluidity [label-only] | Strong review consensus (moyer2017psychrophilesandpsychrotrophs pages 3-5, moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 8-10) | Broad bacteria | 10.1016/B978-0-12-809633-8.02282-2; 10.37256/amtt.5220244537 |
| membrane fluidity | enables | membrane transport and electron transport | membrane fluidity [label-only]; transport [GO:0006810]; electron transport chain [GO:0022900] | Strong review-level physiological claim (moyer2017psychrophilesandpsychrotrophs pages 1-2) | Broad microbes | 10.1016/B978-0-12-809633-8.02282-2 |
| cold-adapted enzyme structural flexibility | increases | catalytic activity at low temperature | enzyme flexibility [label-only]; catalytic activity [GO:0003824] | Strong review consensus with explicit caveat that flexibility is not universal (moyer2017psychrophilesandpsychrotrophs pages 2-3, ramon2023ageneraloverview pages 1-2) | Broad psychrophiles | 10.1016/B978-0-12-809633-8.02282-2; 10.1007/s42770-023-01057-4 |
| antifreeze protein / ice-binding protein | inhibits | ice recrystallization / ice crystal growth | antifreeze protein [label-only]; ice-binding protein [label-only]; ice recrystallization inhibition [label-only] | Moderate review-level evidence; strong for subzero survival, less direct for optimum-growth phenotype (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10) | Psychrophiles across taxa | 10.37256/amtt.5220244537 |
| exopolysaccharide (EPS) | provides | freeze-thaw cryoprotection | exopolysaccharide [CHEBI:26220] | Moderate review-level evidence; often taxon- and habitat-specific (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 8-10, bao2023miningofkey pages 1-2) | Broad, including Pseudomonas and sea-ice microbes | 10.1016/B978-0-12-809633-8.02282-2; 10.37256/amtt.5220244537; 10.3389/fmicb.2023.1215837 |
| compatible solutes | protects | macromolecules and cellular homeostasis under cold stress | compatible solute [label-only]; cellular homeostasis [label-only] | Moderate review + transcriptomic support; direct molecule-specific causality often limited (bao2023miningofkey pages 1-2) | Broad; explicitly noted in Pseudomonas fragi D12 | 10.3389/fmicb.2023.1215837 |
| molecular chaperones / RNA chaperones | maintains | protein and RNA homeostasis | chaperone-mediated protein folding [GO:0061077]; RNA chaperone activity [label-only]; RNA metabolic process [GO:0016070] | Strong review consensus, moderate direct trait specificity (purwar2024adaptationsofpsychrophilic pages 6-7, bao2023miningofkey pages 1-2) | Broad psychrophiles; transcriptomic support in P. fragi D12 | 10.37256/amtt.5220244537; 10.3389/fmicb.2023.1215837 |
| catalase / superoxide dismutase | reduces | reactive oxygen species burden | catalase [EC 1.11.1.6]; superoxide dismutase [EC 1.15.1.1]; reactive oxygen species [CHEBI:26523] | Moderate support from review and transcriptomic/physiological studies (bao2023miningofkey pages 1-2) | Broad; explicit in Pseudomonas fragi D12 and low-temperature adaptation studies | 10.3389/fmicb.2023.1215837 |
| DPS heterologous expression | increases | E. coli growth at 10 °C | DPS family protein [label-only]; growth at 10 C [label-only] | Direct functional evidence, stronger than correlative omics; still assay-specific and heterologous (li2024mechanismsunderlyingthe pages 12-13) | Recombinant E. coli expressing Rhodococcus sp. RCBS9 gene | 10.3389/fmicb.2024.1465627 |
| GroEL heterologous expression | increases | E. coli growth at 10 °C | GroEL [UniProt family label-only]; protein folding [GO:0006457] | Direct functional evidence, stronger than correlative omics; assay-specific and heterologous (li2024mechanismsunderlyingthe pages 12-13) | Recombinant E. coli expressing Rhodococcus sp. RCBS9 gene | 10.3389/fmicb.2024.1465627 |
| USP-2 heterologous expression | increases | E. coli growth at 10 °C | universal stress protein [label-only] | Direct functional evidence, stronger than correlative omics; assay-specific and heterologous (li2024mechanismsunderlyingthe pages 12-13) | Recombinant E. coli expressing Rhodococcus sp. RCBS9 gene | 10.3389/fmicb.2024.1465627 |
| increased ribosomal protein production / ribosome-associated proteins | supports | translation under cold conditions | ribosome biogenesis [GO:0042254]; translation [GO:0006412] | Moderate primary-study support plus review background; may reflect cold acclimation more than trait-defining mechanism (moyer2017psychrophilesandpsychrotrophs pages 2-3) | Broad psychrophiles | 10.1016/B978-0-12-809633-8.02282-2 |
| membrane adaptation + enzyme cold activity + cryoprotectants + chaperones + ROS defenses | collectively supports | growth at very low temperature (METPO:1000441) | METPO:1000441; cold response [GO:0009409] | Integrative inference only; should be curated cautiously because sources support cold growth/adaptation, not by themselves proof of optimum <=10 C (ramon2023ageneraloverview pages 1-2, bao2023miningofkey pages 1-2, li2024mechanismsunderlyingthe pages 12-13) | Trait-level synthesis across taxa | 10.1007/s42770-023-01057-4; 10.3389/fmicb.2023.1215837; 10.3389/fmicb.2024.1465627 |


*Table: This table compiles the strongest candidate causal edges for curating METPO:1000441, emphasizing mechanisms with the best available support and clearly separating direct functional evidence from broader review-level inferences.*

| Proposed subject–predicate–object | Supporting snippet or result | Interpretation and curation status |
|---|---|---|
| low temperature → alters → membrane physical state | The 2023 review describes cold sensing through modification of the membrane liquid-crystalline state and activation of two-component responses. (ramon2023ageneraloverview pages 1-2) | **Moderate, review-level.** Curate as a cold-response mechanism, not as sufficient proof of the optimum phenotype. |
| fatty-acid desaturase activity → increases → unsaturated membrane lipids | “Lipid desaturation via desaturase enzymes” is described as the primary response maintaining fluidity as temperature decreases; 2024 synthesis likewise reports desaturase and lipid-synthesis upregulation. (moyer2017psychrophilesandpsychrotrophs pages 3-5, purwar2024adaptationsofpsychrophilic pages 8-10) | **Moderate-to-strong consensus.** Direction is mechanistically credible, but the exact desaturase must be grounded by species/sequence. |
| unsaturated membrane lipids → increase → membrane fluidity | Psychrophiles have higher 16:1/18:1 and PUFA proportions, and decreasing culture temperature increases unsaturated phospholipids. In *Moritella* ANT-300, palmitoleate rose from 46% to 62.5% while myristate fell from 26% to 13% during the reported condition. (moyer2017psychrophilesandpsychrotrophs pages 3-5) | **Strong physiological support**, but the cited quantitative change involved starvation as well as lipid remodeling and should not be represented as a pure temperature intervention. |
| membrane fluidity → enables → transport/electron transport/ion pumping | The membrane must remain fluid for electron transport, ion pumping, and nutrient uptake across the temperature range. (moyer2017psychrophilesandpsychrotrophs pages 1-2) | **Strong physiological rationale; review-level.** Suitable as intermediate edges. |
| cold-adapted enzyme architecture → increases → low-temperature catalytic rate | Cold-adapted enzymes may show up to an order-of-magnitude greater low-temperature specific activity than mesophilic counterparts, often with heat lability above 30 °C. (moyer2017psychrophilesandpsychrotrophs pages 2-3) | **Strong but generalized.** Do not encode “greater flexibility” as universal; stable or unchanged-flexibility cold-active enzymes are known exceptions. |
| AFP/IBP → inhibits → ice growth or recrystallization | IBPs bind ice surfaces and prevent recrystallization; some antifreeze proteins depress freezing point by ≥2 °C. (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 6-7) | **Good for subzero survival**, but only indirectly linked to optimum ≤10 °C. Mark uncertain for the target trait unless tested in growth curves. |
| EPS → protects against → freeze–thaw injury | Reviews and *P. fragi* D12 data associate extracellular polymers with cryoprotection and cold response. (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 8-10, bao2023miningofkey pages 1-2) | **Moderate; habitat/taxon dependent.** Often correlational. |
| compatible-solute accumulation → stabilizes → macromolecules/cellular homeostasis | *P. fragi* D12 accumulated glycine/betaine, trehalose, mannitol, and sorbitol-associated compatible-solute functions during cold adaptation. (bao2023miningofkey pages 1-2) | **Moderate, psychrotroph-specific.** Molecule-specific perturbation evidence is needed before asserting necessity. |
| cold exposure → induces → chaperones and transcription factors | In *P. fragi* D12, shifting 15→4 °C mainly increased expression of molecular chaperones and transcription factors. (bao2023miningofkey pages 1-2) | **Primary but transcriptomic.** Curate as regulation, not gene necessity. |
| GroEL → supports → growth at 10 °C | Recombinant BL21-GroEL reached approximately OD600 1.4 at four hours versus ~1.0–1.1 for vector control. (li2024mechanismsunderlyingthe pages 12-13) | **Direct gain-of-function, assay-specific.** Strong candidate edge to low-temperature growth; not to thermal-optimum setpoint. |
| DPS → supports → growth at 10 °C | Recombinant BL21-DPS showed the same approximate four-hour improvement at 10 °C. (li2024mechanismsunderlyingthe pages 12-13) | **Direct gain-of-function, assay-specific.** Native function and necessity remain untested. |
| USP-2 → supports → growth at 10 °C | Recombinant BL21-USP-2 reached approximately OD600 1.4 at four hours. (li2024mechanismsunderlyingthe pages 12-13) | **Direct gain-of-function, assay-specific.** Do not generalize to all universal stress proteins. |
| catalase/SOD → decreases → ROS burden | *P. fragi* D12 cold adaptation included ROS reduction through catalase and superoxide dismutase; RCBS9 also implicated Cu/Zn-SOD. (bao2023miningofkey pages 1-2, li2024mechanismsunderlyingthe pages 10-12) | **Moderate.** RCBS9 SOD expression was tested, but the retrieved evidence does not show the same quantified benefit as DPS/GroEL/USP-2. |
| increased ribosomal protein production → supports → translation in cold | Psychrophiles increase rRNA and ribosomal-protein production at suboptimal temperatures; cold perturbs ribosomal and protein synthesis. (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 3-4) | **Moderate, broad.** Could be acclimation rather than a trait-setting mechanism. |
| combined membrane, catalytic, chaperone, cryoprotective, and antioxidant adaptations → supports → growth at ≤10 °C | Recent syntheses explicitly frame cold adaptation as multifactorial. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) | **Integrative inference only.** No retrieved study proves this suite determines an optimum ≤10 °C across taxa. |

## 5. Recent developments and applications

### Recent research directions

1. **Multi-omics is replacing single-mechanism explanations.** The 2023 *P. fragi* study combined whole-genome comparison and transcriptomics and reported 124 candidate genes, 19 strain-unique cold-adaptive genes, and temperature-interval-specific responses. These data support modular rather than uniform cold adaptation. (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7)
2. **Functional transfer is beginning to test omics candidates.** The 2024 RCBS9 work moved beyond differential expression by expressing six proteins in *E. coli*, with DPS, GroEL, and USP-2 producing measurable growth gains at 10 °C. This is stronger causal evidence than enrichment or expression alone, although still not a thermal-optimum experiment. (li2024mechanismsunderlyingthe pages 10-12, li2024mechanismsunderlyingthe pages 12-13)
3. **Enzyme adaptation is now treated as mechanistically diverse.** The common flexibility–activity–instability model remains useful, but authoritative 2023 analysis emphasizes that some cold-active enzymes retain high stability, high substrate affinity, or unchanged flexibility. Graphs should therefore represent enzyme-specific mechanisms rather than a universal “flexibility causes psychrophily” rule.
4. **Ecotype-aware comparative genomics is increasingly important.** Broad pangenome studies seek to distinguish psychrophilic from mesophilic ecotypes, but enrichment and amino-acid-composition signals remain evolutionary associations until validated experimentally.

### Real-world implementations

Cold-adapted microorganisms and their products are used or investigated for:

- **Low-temperature bioremediation and wastewater treatment**, where active metabolism avoids costly heating.
- **Food and detergent processing**, using cold-active lipases, proteases, amylases, and cellulases to reduce energy requirements and heat damage.
- **Molecular biology**, especially cold-active DNA-processing enzymes.
- **Agriculture**, including cold-region plant-growth promotion and biocontrol by *Pseudomonas* formulations.
- **Cryopreservation and frozen foods**, using ice-binding proteins, antifreeze proteins, EPS, or compatible solutes to control ice crystals.
- **Biodegradation**, including pollutant transformation in cold soils and waters.

The recent review literature explicitly highlights bioremediation, plant-growth promotion, sewage treatment, composting, and food/drug processing. These are applications of cold-active cells or biomolecules; commercial use should not be interpreted as evidence that the source organism has optimum ≤10 °C. (ramon2023ageneraloverview pages 1-2, bao2023miningofkey pages 1-2)

## 6. Recommended TraitMech curation strategy

### High-confidence intermediate edges

Curate first:

1. fatty-acid desaturation → increased membrane unsaturation;
2. increased membrane unsaturation → increased membrane fluidity;
3. membrane fluidity → supports membrane transport/respiration;
4. AFP/IBP → inhibits ice growth/recrystallization;
5. chaperone activity → supports protein folding under cold stress;
6. catalase/SOD activity → decreases ROS burden;
7. DPS, GroEL, or USP-2 expression → increased short-term *E. coli* growth at 10 °C, with explicit assay and taxon qualifiers.

### Trait-level linkage

Use a conservative final edge such as:

**integrated cold-adaptation program — contributes_to — `METPO:1000441`**

Mark it **inferred/multifactorial**, because most sources demonstrate low-temperature growth, survival, or acclimation rather than a shift in the temperature optimum itself. A stronger trait-level assertion requires knockout/knockdown or allele-swap experiments combined with a full growth curve showing that the perturbation moves the optimum across the approximately 10 °C boundary.

## 7. Claims not yet suitable for unqualified curation

- **“Psychrophile” equals `METPO:1000441`.** Conventional optimum cutoffs often extend to 15 °C; map only with organism-specific assay evidence.
- **Any cold-growth gene causes a very-low optimum.** It may improve growth at 10 °C without changing the optimum.
- **All psychrophiles remodel fatty acids identically.** Some evidence indicates psychrotrophs may show stronger inducible lipid remodeling than obligate psychrophiles. (moyer2017psychrophilesandpsychrotrophs pages 3-5)
- **Protein flexibility universally causes cold activity.** It is common, not universal.
- **AFPs/IBPs establish the optimum phenotype.** They primarily support freezing survival and ice management.
- **Transcriptomic upregulation proves causation.** Bao et al. provides candidate pathways, not loss-of-function validation.
- **Pili genes are general psychrophile determinants.** Their upregulation in *P. fragi* D12 is strain-specific and mechanistically unresolved. (bao2023miningofkey pages 1-2)
- **Metabolic activity at −20 to −40 °C equals growth.** Distinguish activity, survival, and cell division.
- **Unverified CURIEs.** Exact gene, protein, lipid, habitat, Rhea, KEGG, and MetaCyc identifiers should be added only after sequence-, reaction-, and species-specific lookup.

## 8. DOI-first bibliography

1. **Li Q. et al.** “Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain *Rhodococcus* sp. RCBS9.” *Frontiers in Microbiology* 15. **November 2024.** DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627). (li2024mechanismsunderlyingthe pages 10-12, li2024mechanismsunderlyingthe pages 12-13)
2. **Purwar S., Srivastava S.** “Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.” *Applied Microbiology: Theory & Technology*, 168–188. **October 2024.** DOI: [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537). (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 3-4)
3. **Bao C. et al.** “Mining of key genes for cold adaptation from *Pseudomonas fragi* D12 and analysis of its cold-adaptation mechanism.” *Frontiers in Microbiology* 14. **July 2023.** DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837). (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7)
4. **Ramón A. et al.** “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* 54:2259–2287. **July 2023.** DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 1-2)
5. **Moyer C.L., Collins R.E., Morita R.Y.** “Psychrophiles and Psychrotrophs.” *Reference Module in Life Sciences*. **January 2017.** DOI: [10.1016/B978-0-12-809633-8.02282-2](https://doi.org/10.1016/B978-0-12-809633-8.02282-2). (moyer2017psychrophilesandpsychrotrophs pages 3-5, moyer2017psychrophilesandpsychrotrophs pages 2-3, moyer2017psychrophilesandpsychrotrophs pages 1-2)
6. **D’Amico S. et al.** “Psychrophilic microorganisms: challenges for life.” *EMBO Reports* 7:385–389. **April 2006.** DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662). This is the supplied foundational evidence supporting growth near the freezing point.

**Bottom line:** the most defensible graph is a layered model in which low temperature triggers membrane and stress sensing; lipid remodeling preserves membrane functions; cold-efficient enzymes preserve metabolic flux; chaperones, ribosomal processes, and stress proteins maintain macromolecules; AFP/IBP, EPS, and compatible solutes limit freezing injury; and antioxidant systems constrain ROS. These mechanisms support very-low-temperature growth, but only organism-level temperature-response assays can assign `METPO:1000441`, and almost no retrieved perturbation study directly demonstrates movement of the optimum across the ≤10 °C threshold.

References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

2. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

3. (moyer2017psychrophilesandpsychrotrophs pages 1-2): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

4. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

5. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

6. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

7. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

8. (li2024mechanismsunderlyingthe pages 10-12): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

9. (li2024mechanismsunderlyingthe pages 12-13): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

10. (bao2023miningofkey pages 6-7): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

11. (moyer2017psychrophilesandpsychrotrophs pages 3-5): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.