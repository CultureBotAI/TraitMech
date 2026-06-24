---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:06:23.050535'
end_time: '2026-06-18T01:28:41.324926'
duration_seconds: 1338.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: psychrophilic
  trait_identifier: METPO:1000614
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: psychrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at low temperatures,\
    \ typically near or below ~15 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Supports psychrophilic growth at low temperatures.)
    | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism
    example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)'
  causal_graph_summary: 'psychrophilic_cold_adaptation: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrophilic
- **METPO identifier:** METPO:1000614
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at low temperatures, typically near or below ~15 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Supports psychrophilic growth at low temperatures.) | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)
- **Existing causal graph summary:** psychrophilic_cold_adaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrophilic.yaml`.

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
- **Trait label:** psychrophilic
- **METPO identifier:** METPO:1000614
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at low temperatures, typically near or below ~15 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Supports psychrophilic growth at low temperatures.) | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)
- **Existing causal graph summary:** psychrophilic_cold_adaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrophilic.yaml`.

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


## Psychrophilic (METPO:1000614) — curation-focused research report

### Scope summary (trait meaning, boundaries, and assays)

**Trait definition (operational):** “Psychrophilic” refers to microorganisms whose growth is favored at low temperatures; a widely used operational definition (Morita, 1975) defines psychrophiles as having **Topt ≲ 15 °C**, **Tmax ≲ 20 °C**, and **Tmin ≤ 0 °C**. Psychrotrophs/psychrotolerant organisms can grow at low temperature but have **Topt and Tmax above 15 °C and 20 °C**, respectively. This 20 °C cutoff is partly pragmatic (near typical laboratory room temperatures) and there is a continuum of cardinal temperatures rather than discrete bins. (moyer2017psychrophilesandpsychrotrophs pages 1-2)

**Boundary cases:** Growth at very low temperature is not sufficient to call an organism psychrophilic if its optimum/maximum are high. For example, **Planococcus halocryophilus** has authenticated growth at **−15 °C** but has **Topt 25 °C** and **Tmax 37 °C**, and is classified as psychrotolerant. This illustrates that subzero growth can occur in non-psychrophiles and that classification requires cardinal temperature measurement. (moyer2017psychrophilesandpsychrotrophs pages 1-2)

**Assay/interpretation caveats (important for TraitMech curation):**
- **Topt/Tmax can misrepresent ecological cold adaptation.** Cavicchioli argues that using lab growth-rate optima or Tmax alone is misleading because growth rate increases with temperature until thermal damage, and many cold isolates grow well above in situ temperatures. Empirically, a methanogen with higher lab Topt/Tmax can still outcompete another at lake temperatures, so ecological fitness at low temperature is not captured by Topt/Tmax alone. (cavicchioli2016ontheconcept pages 1-2)
- **Authentication requires careful growth curves at low/subzero temperatures** (generation times can be many days to weeks). Sampling and handling should keep materials cold and use environments that do not exceed psychrophilic ranges to avoid bias toward psychrotolerants. (moyer2017psychrophilesandpsychrotrophs pages 1-2)

**Distinguish from nearby traits:**
- *Psychrotolerant/psychrotrophic*: low-temperature growth-capable but not low-temperature optimum (often Topt 20–25 °C). (maayer2014somelikeit pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 1-2)
- *Eurypsychrophile*: taxa that grow down to ~4 °C but have optimum above ~15 °C (used in low-temperature acidophile literature; likely a separate trait label). (dopson2023eurypsychrophilicacidophilesfrom pages 11-12)

### Current understanding (key mechanistic concepts)

Psychrophilic growth requires overcoming multiple cold-imposed constraints: reduced membrane fluidity, slowed transcription/translation and folding, ice formation/freezing-point effects, and oxidative stress due to increased gas solubility at low temperature. (damico2006psychrophilicmicroorganismschallenges pages 2-3, maayer2014somelikeit pages 5-6)

Core mechanistic themes supported by authoritative sources include:

1. **Homeoviscous adaptation (membrane remodeling):** Low temperature reduces membrane fluidity; psychrophiles compensate by increasing unsaturated/polyunsaturated and methyl-branched fatty acids and adjusting chain length/headgroups to maintain fluidity. (damico2006psychrophilicmicroorganismschallenges pages 2-3, maayer2014somelikeit pages 5-6)
2. **Nucleic-acid and translation support:** Cold stabilizes DNA/RNA secondary structures and slows translation. Cold-shock proteins (CSPs/CAPs) and **RNA helicases** help restore transcription/translation under cold conditions. (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9, maayer2014somelikeit pages 5-6)
3. **Protein quality control:** Molecular chaperones and (in some taxa) heat-shock proteins support protein homeostasis under cold stress. (maayer2014somelikeit pages 5-6, li2024mechanismsunderlyingthe pages 9-10)
4. **Cryoprotection and ice control:** Compatible solutes (e.g., trehalose, glycine betaine, glycerol) depress freezing points and stabilize macromolecules; antifreeze/ice-binding proteins bind ice crystals and can lower the temperature at which organisms can grow. EPS can act as cryoprotectant and protect extracellular enzymes. (purwar2024adaptationsofpsychrophilic pages 10-11, damico2006psychrophilicmicroorganismschallenges pages 2-3)
5. **Oxidative stress defense:** Low temperature increases ROS burden; catalases, superoxide dismutases, peroxidases, glutathione-related systems, and pigments (e.g., carotenoids) are implicated, though some pigment roles are postulated rather than universally established. (maayer2014somelikeit pages 5-6, bao2023miningofkey pages 7-9, li2024mechanismsunderlyingthe pages 9-10)

### Recent developments and latest research (priority 2023–2024)

#### (A) Multi-omics identification of cold-adaptation genes (2023)
A 2023 genome+transcriptome study of **Pseudomonas fragi D12** mined **124 potential cold adaptation genes**, explicitly linking cold adaptation to membrane remodeling genes (including fatty-acid enzymes), compatible-solute systems, EPS/motility elements, helicases, and antioxidant enzymes. The authors state that fatty-acid degradation modes can increase unsaturated fatty acids and reduce average chain length, “thereby changing the composition of lipids… and improving… fluidity” at low temperature; they also report annotated cold-shock genes and helicases that “assist the entangled RNA to unwind… thereby restoring normal transcription and translation.” (bao2023miningofkey pages 7-9)

#### (B) Physiology+transcriptomics in a low-temperature pollutant degrader (2024)
A 2024 study on **Rhodococcus sp. RCBS9** (a 17β-estradiol degrader) reports low-temperature adaptation involving **antioxidant synthesis**, **DNA repair upregulation**, **membrane/cell-wall remodeling** (including peptidoglycan-related genes), and stress-regulated protein expression. Notably, it emphasizes universal stress proteins and heat shock proteins (DnaK/htpG/sHsp/DnaJ/GrpE) upregulated at 10 °C and interprets DAP-type peptidoglycan as enhancing elasticity for survival at low temperature. (li2024mechanismsunderlyingthe pages 9-10)

#### (C) Updated 2024 synthesis of compatible-solute and PUFA roles
A 2024 review consolidates that compatible solutes (glycine betaine, trehalose, glycerol, sucrose, polyols) can accumulate to molar levels and stabilize proteins/membranes while depressing freezing point, and highlights long-chain PUFA roles (EPA/DHA) in membrane fluidity maintenance and ROS shielding (not universal across taxa). (purwar2024adaptationsofpsychrophilic pages 10-11)

### Candidate causal-graph nodes (entities) grouped by type

| Node type | Node label | Suggested ontology grounding | Evidence/supporting source(s) | Notes |
|---|---|---|---|---|
| Environmental factor | cold environment / low temperature habitat | ENVO:01000230 | Moyer 2017, DOI:10.1016/B978-0-12-809633-8.02282-2; D’Amico 2006, DOI:10.1038/sj.embor.7400662 (moyer2017psychrophilesandpsychrotrophs pages 1-2, damico2006psychrophilicmicroorganismschallenges pages 2-3) | Core external condition defining the trait; should likely be an upstream driver node. |
| Environmental factor | permanently cold marine environment | ENVO:cold_marine_habitat candidate | Moyer 2017, DOI:10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2) | Relevant ecological context because true psychrophiles are concentrated in permanently cold environments. |
| Environmental factor | subzero temperature |  | Moyer 2017, DOI:10.1016/B978-0-12-809633-8.02282-2; Purwar 2024, DOI:10.37256/amtt.5220244537 (moyer2017psychrophilesandpsychrotrophs pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) | Important boundary condition for growth and survival; useful for assay interpretation. |
| Environmental factor | oxidative stress at low temperature | GO:0006979 | De Maayer 2014, DOI:10.1002/embr.201338170; Purwar 2024, DOI:10.37256/amtt.5220244537 (maayer2014somelikeit pages 5-6, purwar2024adaptationsofpsychrophilic pages 10-11) | Cold increases gas solubility and ROS burden; likely a secondary stress node. |
| Environmental factor | freezing / ice crystal exposure |  | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Purwar 2024, DOI:10.37256/amtt.5220244537 (damico2006psychrophilicmicroorganismschallenges pages 2-3, purwar2024adaptationsofpsychrophilic pages 10-11) | Relevant for AFP/IBP and compatible-solute mechanisms. |
| Assay/experimental factor | Tmin/Topt/Tmax growth temperature measurement |  | Moyer 2017, DOI:10.1016/B978-0-12-809633-8.02282-2; Cavicchioli 2016, DOI:10.1038/ismej.2015.160 (moyer2017psychrophilesandpsychrotrophs pages 1-2, cavicchioli2016ontheconcept pages 1-2) | Essential for phenotype assignment, but not itself a mechanistic node. |
| Assay/experimental factor | critical temperature (Tcritical) |  | Cavicchioli 2016, DOI:10.1038/ismej.2015.160 (cavicchioli2016ontheconcept pages 1-2) | Useful boundary/assay concept; may be better captured in curation notes than in core graph. |
| Assay/experimental factor | growth curve authentication at low/subzero temperature |  | Moyer 2017, DOI:10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2) | Important to distinguish true psychrophily from mere survival or transient activity. |
| Pathway/module | unsaturated fatty acid biosynthesis | KEGG:map01040 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; D’Amico 2006, DOI:10.1038/sj.embor.7400662 (bao2023miningofkey pages 7-9, damico2006psychrophilicmicroorganismschallenges pages 2-3) | Canonical homeoviscous-adaptation module; strong candidate core node. |
| Pathway/module | fatty acid degradation / β-oxidation | GO:0006635 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; Li 2024, DOI:10.3389/fmicb.2024.1465627 (bao2023miningofkey pages 7-9, li2024mechanismsunderlyingthe pages 9-10) | Supports membrane remodeling and energy generation; taxon-specific details vary. |
| Pathway/module | exopolysaccharide biosynthetic process | GO:0045226 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; D’Amico 2006, DOI:10.1038/sj.embor.7400662 (bao2023miningofkey pages 7-9, damico2006psychrophilicmicroorganismschallenges pages 2-3) | Strong candidate for extracellular cryoprotection/biofilm node. |
| Pathway/module | trehalose / compatible-solute transport and accumulation | GO:0015840 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; Purwar 2024, DOI:10.37256/amtt.5220244537 (bao2023miningofkey pages 7-9, purwar2024adaptationsofpsychrophilic pages 10-11) | Broad cryoprotection/osmoprotection module; multiple compounds may need separate chemical nodes. |
| Pathway/module | reactive oxygen species detoxification | GO:0072593 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; Li 2024, DOI:10.3389/fmicb.2024.1465627 (bao2023miningofkey pages 7-9, li2024mechanismsunderlyingthe pages 9-10) | Supported by catalase/SOD/peroxidase data; likely a conserved adaptation module. |
| Pathway/module | peptidoglycan biosynthetic process | GO:0009252 | Li 2024, DOI:10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10) | Cell-wall adaptation mechanism; strong in RCBS9 but may be more taxon-specific than membrane adaptation. |
| Gene/protein family | fatty acid desaturase | EC:1.14.19.- | Bao 2023, DOI:10.3389/fmicb.2023.1215837; Li 2024, DOI:10.3389/fmicb.2024.1465627 (bao2023miningofkey pages 7-9, li2024mechanismsunderlyingthe pages 9-10) | Directly implicated in unsaturated fatty acid production and membrane fluidity; strong mechanistic node. |
| Gene/protein family | fatty acid cis/trans isomerase | EC:5.2.1.5 | Bao 2023, DOI:10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9) | Specific membrane-remodeling enzyme; good candidate but less universally documented than desaturase. |
| Gene/protein family | ketoacyl-ACP synthase II/III (KAS-II/III) | EC:2.3.1.179 / EC:2.3.1.180 | Bao 2023, DOI:10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9) | Supports fatty-acid chain remodeling; candidate enzymatic node. |
| Gene/protein family | cold-shock proteins (Csp/CAP family) | GO:0061844 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; De Maayer 2014, DOI:10.1002/embr.201338170 (damico2006psychrophilicmicroorganismschallenges pages 2-3, maayer2014somelikeit pages 5-6) | Canonical cold-response family; central node for transcription/translation adaptation. |
| Gene/protein family | RNA helicases | GO:0003724 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; D’Amico 2006, DOI:10.1038/sj.embor.7400662 (bao2023miningofkey pages 7-9, damico2006psychrophilicmicroorganismschallenges pages 2-3) | Strong evidence for unwinding stabilized RNA structures at low temperature. |
| Gene/protein family | DNA helicases | GO:0003678 | Bao 2023, DOI:10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9) | Supports nucleic-acid processing under cold stress; likely secondary to RNA helicase node. |
| Gene/protein family | molecular chaperones (GroEL/GroES, DnaK/DnaJ/GrpE) | GO:0005524; GO:0061077 | De Maayer 2014, DOI:10.1002/embr.201338170; Li 2024, DOI:10.3389/fmicb.2024.1465627 (maayer2014somelikeit pages 5-6, li2024mechanismsunderlyingthe pages 9-10) | Protein-folding homeostasis under cold stress; strong candidate family node. |
| Gene/protein family | heat-shock proteins upregulated in cold adaptation | GO:0034605 | Li 2024, DOI:10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10) | RCBS9 uses HSPs/USPs rather than typical CSPs; likely taxon-specific or stress-context dependent. |
| Gene/protein family | universal stress proteins (USP family) |  | Li 2024, DOI:10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10) | Recent primary evidence; promising but not yet broadly established as a psychrophily-defining node. |
| Gene/protein family | catalase | EC:1.11.1.6 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; De Maayer 2014, DOI:10.1002/embr.201338170 (bao2023miningofkey pages 7-9, maayer2014somelikeit pages 5-6) | Standard antioxidant defense node. |
| Gene/protein family | superoxide dismutase | EC:1.15.1.1 | Bao 2023, DOI:10.3389/fmicb.2023.1215837; De Maayer 2014, DOI:10.1002/embr.201338170 (bao2023miningofkey pages 7-9, maayer2014somelikeit pages 5-6) | Standard ROS-detoxification node. |
| Gene/protein family | peroxidases (PX/GPX/Prx) | EC:1.11.1.- | Li 2024, DOI:10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10) | Strong in RCBS9; may be preferable as an uncertain/taxon-specific antioxidant node. |
| Gene/protein family | antifreeze proteins / ice-binding proteins |  | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Purwar 2024, DOI:10.37256/amtt.5220244537 (damico2006psychrophilicmicroorganismschallenges pages 2-3, purwar2024adaptationsofpsychrophilic pages 10-11) | Canonical cryoprotection proteins; important but not universally present. |
| Gene/protein family | exopolysaccharide production protein ExoZ |  | Bao 2023, DOI:10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9) | Specific EPS-associated gene from Pseudomonas fragi D12; taxon-specific node. |
| Gene/protein family | PilT / pilin / fimbrin family |  | Bao 2023, DOI:10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9) | Linked to extracellular polymer/motility adaptations; likely not a general psychrophily marker. |
| Cellular process/structure | membrane fluidity / homeoviscous adaptation | GO:0016042 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; De Maayer 2014, DOI:10.1002/embr.201338170 (damico2006psychrophilicmicroorganismschallenges pages 2-3, maayer2014somelikeit pages 5-6) | One of the most central mechanistic nodes for psychrophily. |
| Cellular process/structure | transcription and translation at low temperature | GO:0006351; GO:0006412 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Bao 2023, DOI:10.3389/fmicb.2023.1215837 (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9) | Core process impaired by cold and rescued by CSPs/helicases/chaperones. |
| Cellular process/structure | cell wall remodeling / elastic peptidoglycan | GO:0005618; GO:0009252 | Li 2024, DOI:10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10) | Mechanistically relevant, especially in Gram-positive taxa; uncertain as universal node. |
| Cellular process/structure | biofilm / extracellular matrix stabilization | GO:0042710 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Bao 2023, DOI:10.3389/fmicb.2023.1215837 (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9) | EPS-rich extracellular protection may be important in freezing and nutrient retention. |
| Chemical/metabolite | unsaturated fatty acids | CHEBI:35579 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Bao 2023, DOI:10.3389/fmicb.2023.1215837 (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9) | Strong chemical node mediating membrane-fluidity adaptation. |
| Chemical/metabolite | polyunsaturated fatty acids (PUFAs; EPA/DHA) | CHEBI:26208; CHEBI:28364; CHEBI:28125 | Purwar 2024, DOI:10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11) | Important membrane and application node; more prominent in some marine psychrophiles. |
| Chemical/metabolite | methyl-branched fatty acids | CHEBI:62499 | D’Amico 2006, DOI:10.1038/sj.embor.7400662 (damico2006psychrophilicmicroorganismschallenges pages 2-3) | Candidate membrane-adaptation chemical class. |
| Chemical/metabolite | trehalose | CHEBI:16566 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Bao 2023, DOI:10.3389/fmicb.2023.1215837 (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9) | Strong cryoprotectant/compatible-solute node. |
| Chemical/metabolite | glycine betaine | CHEBI:17750 | Purwar 2024, DOI:10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11) | Well-known compatible solute; good node even if not universal. |
| Chemical/metabolite | glycerol | CHEBI:17522 | Purwar 2024, DOI:10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11) | Common cryoprotectant/compatible-solute node. |
| Chemical/metabolite | exopolysaccharides (EPS) | CHEBI:62968 | D’Amico 2006, DOI:10.1038/sj.embor.7400662; Bao 2023, DOI:10.3389/fmicb.2023.1215837 (damico2006psychrophilicmicroorganismschallenges pages 2-3, bao2023miningofkey pages 7-9) | Major extracellular protective material; strong candidate node. |
| Chemical/metabolite | reactive oxygen species | CHEBI:26523 | De Maayer 2014, DOI:10.1002/embr.201338170; Purwar 2024, DOI:10.37256/amtt.5220244537 (maayer2014somelikeit pages 5-6, purwar2024adaptationsofpsychrophilic pages 10-11) | Useful stress-intermediate node connecting cold to antioxidant defenses. |
| Chemical/metabolite | carotenoids | CHEBI:23044 | De Maayer 2014, DOI:10.1002/embr.201338170; Purwar 2024, DOI:10.37256/amtt.5220244537 (maayer2014somelikeit pages 5-6, purwar2024adaptationsofpsychrophilic pages 10-11) | Membrane-fluidity and stress-protection role is plausible but partly review/postulated. |
| Application/product | cold-active enzymes / extremozymes |  | Kuddus 2024, DOI:10.1111/1751-7915.14467; Yang 2023, DOI:10.3390/ijms24108532 (kuddus2024cold‐activemicrobialenzymes pages 1-2, yang2023coldadaptedproteasesan pages 1-2) | Major real-world output of psychrophily; useful downstream application node. |
| Application/product | cold-active protease | EC:3.4.-.- | Yang 2023, DOI:10.3390/ijms24108532 (yang2023coldadaptedproteasesan pages 12-14, yang2023coldadaptedproteasesan pages 1-2) | Strong application product in detergents, food, waste treatment. |
| Application/product | cold-active β-galactosidase (lactase) | EC:3.2.1.23 | Kuddus 2024, DOI:10.1111/1751-7915.14467 (kuddus2024cold‐activemicrobialenzymes pages 2-4) | Refrigerated lactose hydrolysis; useful concrete implementation node. |
| Application/product | cold-active alkaline phosphatase / molecular biology enzyme | EC:3.1.3.1 | Kuddus 2024, DOI:10.1111/1751-7915.14467 (kuddus2024cold‐activemicrobialenzymes pages 10-12, kuddus2024cold‐activemicrobialenzymes pages 12-13) | Commercialized psychrophile-derived product; downstream application rather than trait mechanism. |
| Application/product | low-temperature biomining / bioleaching |  | Dopson 2023, DOI:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 11-12) | Important real-world use of eurypsychrophilic acidophiles; not a core causal node for general psychrophily. |
| Application/product | cold-environment bioremediation |  | Kuddus 2024, DOI:10.1111/1751-7915.14467; Dopson 2023, DOI:10.3389/fmicb.2023.1149903 (kuddus2024cold‐activemicrobialenzymes pages 10-12, dopson2023eurypsychrophilicacidophilesfrom pages 11-12) | Relevant implementation class; keep separate from core mechanistic graph unless modeling outputs. |


*Table: This table lists candidate causal-graph nodes for the psychrophilic trait, grouped by biological and curation-relevant type. It is useful for selecting core mechanistic nodes versus assay or downstream application nodes when drafting a TraitMech YAML.*

### Evidence-backed candidate causal edges (triples)

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference (DOI/URL, year) | Notes for curation |
|---|---|---|---|---|---|
| low temperature exposure (ENVO:01000230 cold environment; label-level) | decreases | membrane fluidity (GO:0006869 membrane lipid homeostasis, label-level membrane fluidity) | “Decreasing temperatures have an adverse effect… typically leading to a reduction in membrane fluidity” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Foundational review; strong generic edge linking cold to membrane stress. Curate as environmental driver. |
| unsaturated/polyunsaturated/methyl-branched fatty acids (CHEBI class labels) | increases | membrane fluidity (label-level) | “lower growth temperatures produce a higher content of unsaturated, polyunsaturated and methyl-branched fatty acids… This altered composition is thought to have a key role in increasing membrane fluidity” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Review-derived but canonical mechanism; good generic edge for homeoviscous adaptation. |
| fatty acid desaturase activity (EC class label; gene/protein label) | increases | unsaturated fatty acid content (CHEBI class label) | “fatty acid synthase, fatty acid desaturase… play a role in maintaining membrane fluidity at low temperatures” and “can increase the content of unsaturated fatty acids” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary genome/transcriptome study in *Pseudomonas fragi* D12; taxon-specific direct mechanistic support. |
| unsaturated fatty acid synthesis pathway (KEGG/map01040 candidate) | improves | cell membrane fluidity at low temperatures (label-level) | “four genes involved in the unsaturated fatty acid synthesis pathway… can increase the content of unsaturated fatty acids… improving the fluidity of cell membranes at low temperatures” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary omics; pathway-level edge. Good candidate if pathway node preferred over single enzyme. |
| cold-shock proteins / CAPs (GO:0061844 cold shock response; protein family label) | regulate | transcription and translation (GO:0006351, GO:0006412) | “cold-shock proteins (CSPs)… regulate a variety of cellular processes, including transcription, translation” (maayer2014somelikeit pages 5-6) | De Maayer et al. 2014, https://doi.org/10.1002/embr.201338170, 2014 | Review; broad, authoritative. Consider node as CSP family rather than single gene. |
| RNA helicases (GO:0003724 RNA helicase activity) | restores | normal transcription and translation (GO:0006351, GO:0006412) | “five RNA helicases, and ten DNA helicases were annotated; these genes assist the entangled RNA to unwind at low temperatures, thereby restoring normal transcription and translation” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary omics; direct causal wording. Strong candidate edge. |
| molecular chaperones / heat-shock proteins (GO:1903644 regulation of chaperone-mediated protein folding; DnaK/DnaJ/GrpE labels) | maintains | protein homeostasis (GO:0035966 response to topologically incorrect protein) | “Genes encoding heat shock proteins (Hsps), including DnaK, htpG sHsp, DNAJ, and GRPE, were also upregulated… maintain cytoplasmic protein homeostasis” (li2024mechanismsunderlyingthe pages 9-10) | Li et al. 2024, https://doi.org/10.3389/fmicb.2024.1465627, 2024 | Primary transcriptomics in *Rhodococcus* RCBS9; cold adaptation context explicit. Taxon-specific but mechanistically useful. |
| trehalose (CHEBI:16566) | prevents | protein denaturation and aggregation (GO:0061077 chaperone-mediated protein folding, label-level aggregation) | “Trehalose is thought to have a colligative effect, but probably also helps in preventing protein denaturation and aggregation” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Review-derived; direct quote supports cryoprotectant mechanism. |
| compatible solutes (e.g., glycine betaine CHEBI:17750; trehalose CHEBI:16566; glycerol CHEBI:17522) | lower | freezing point of intracellular environment (label-level) | “The production of active and compatible solutes can lower the freezing point of the intracellular environment and provide a stable internal environment” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary omics/interpretive statement; strong candidate generic edge. |
| compatible solutes (glycine betaine/trehalose/glycerol/sucrose/sorbitol etc.) | stabilize | proteins and membranes (GO:0042221 response to chemical, label-level stabilization) | “Compatible solutes depress the freezing point… stabilize proteins and membranes” (purwar2024adaptationsofpsychrophilic pages 10-11) | Purwar & Srivastava 2024, https://doi.org/10.37256/amtt.5220244537, 2024 | Recent review; broad but directly phrased. Good generic edge. |
| antifreeze proteins / ice-binding proteins (GO:0050821 protein stabilization; label-level AFP/IBP) | bind | ice crystals (CHEBI:24866 ice) | “Antifreeze proteins (AFPs) have the ability to bind to ice crystals” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Canonical cryoprotection edge; direct and curatable. |
| antifreeze proteins / ice-binding proteins (label-level) | lowers | temperature at which an organism can grow (label-level minimum growth temperature) | “bind to ice crystals… and thereby create thermal hysteresis and lower the temperature at which an organism can grow” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Strong mechanistic edge but phenotype phrasing is broader; curate cautiously as trait-enabling rather than universal requirement. |
| exopolysaccharides / EPS (CHEBI:62968 polysaccharide; GO:0045226 extracellular matrix structural constituent candidate) | acts as | cryoprotectant (label-level) | “retain and protect extracellular enzymes against cold denaturation and also act as cyoprotectants” (damico2006psychrophilicmicroorganismschallenges pages 2-3) | D'Amico et al. 2006, https://doi.org/10.1038/sj.embor.7400662, 2006 | Review; “cyoprotectants” clearly intended as cryoprotectants in source context. Curate with note on wording normalization. |
| extracellular polymer synthesis genes / EPS production (exoZ, pil/fim-associated labels) | provides | stable extracellular environment at low temperatures (label-level) | “Twenty-six genes associated with extracellular polymer synthesis were annotated… and provide a stable extracellular environment at low temperatures” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary genome study; somewhat inferential from annotation. Mark uncertain/taxon-specific. |
| low temperature / increased O2 solubility (label-level) | increases | reactive oxygen species (CHEBI:26523 reactive oxygen species) | “The solubility of gases increases at lower temperatures, resulting in increased concentrations of reactive oxygen species” (maayer2014somelikeit pages 5-6) | De Maayer et al. 2014, https://doi.org/10.1002/embr.201338170, 2014 | Review-derived environmental stress edge; useful upstream driver in graph. |
| catalase and superoxide dismutase (EC 1.11.1.6; EC 1.15.1.1) | maintains | ROS balance at low temperatures (label-level) | “Five genes associated with the ROS balance were annotated, comprising three catalases and two superoxide dismutases, which would maintain the ROS balance at low temperatures” (bao2023miningofkey pages 7-9) | Bao et al. 2023, https://doi.org/10.3389/fmicb.2023.1215837, 2023 | Primary genome analysis; phrased as inferred function from annotation. Mark uncertain/taxon-specific. |
| carotenoids / pigment production (CHEBI:23044 carotenoid) | buffers | membrane fluidity / homeoviscosity (label-level) | “Carotenoid pigments… have been postulated to buffer membrane fluidity and assist in maintaining homeoviscosity” (maayer2014somelikeit pages 5-6) | De Maayer et al. 2014, https://doi.org/10.1002/embr.201338170, 2014 | Review; explicitly postulated, so uncertainty should be flagged. |
| DAP-type peptidoglycan synthesis (label-level; GO:0009252 peptidoglycan biosynthetic process) | strengthens / increases elasticity of | cell wall (GO:0005618 cell wall) | “DAP-type peptidoglycans strengthen the cell wall and make it more elastic, which helps bacteria to survive at low temperatures” (li2024mechanismsunderlyingthe pages 9-10) | Li et al. 2024, https://doi.org/10.3389/fmicb.2024.1465627, 2024 | Primary transcriptomic/interpretive evidence in *Rhodococcus* RCBS9; strong but taxon-specific. |
| low temperature acidophile activity / exothermic iron and sulfur oxidation (label-level) | creates | warm niche (label-level) | “their ability to raise the temperature of their surroundings by catalyzing exothermic iron and sulfur oxidation reactions” (dopson2023eurypsychrophilicacidophilesfrom pages 11-12) | Dopson et al. 2023, https://doi.org/10.3389/fmicb.2023.1149903, 2023 | Ecologically interesting but indirect for psychrophily itself; likely too context-specific for core TraitMech. Mark uncertain/not core. |


*Table: This table compiles candidate subject-predicate-object edges for a psychrophilic TraitMech causal graph, with short evidence snippets, references, and curation notes. It prioritizes direct mechanistic support while flagging taxon-specific, review-derived, or uncertain claims.*

### Current applications and real-world implementations (with recent quantitative data)

#### 1) Cold-active enzymes across industrial sectors (2024)
A 2024 review summarizes broad deployment of cold-active enzymes (amylases, cellulases, proteases, lipases, etc.) in **food processing, detergents, textile processing, wastewater treatment, biopulping, bioremediation in cold climates, biotransformation, and molecular biology**, emphasizing energy savings and preservation of heat-labile compounds. (kuddus2024cold‐activemicrobialenzymes pages 1-2, kuddus2024cold‐activemicrobialenzymes pages 12-13)

#### 2) Quantitative/market and performance statistics (2023–2024)
- **Detergents as a major market:** Detergents account for **~25–30% of the enzyme market**, and cold-adapted proteases are positioned as enabling low-temperature cleaning (reducing heating costs and color damage). (yang2023coldadaptedproteasesan pages 12-14, yang2023coldadaptedproteasesan pages 1-2)
- **Example performance data:** a *Bacillus subtilis* protease removed blood stains after **20 min at 15 °C**; a *Saccharomyces*-derived protease degraded **90% of casein at 5 °C** after 24 h. (yang2023coldadaptedproteasesan pages 12-14)
- **Enzyme market shares & projections (as reported in review):** Kuddus et al. report an enzyme-sector projection of **US$6.3 billion**, and note **pectinolytic enzymes ~10%** of the enzyme market and **amylases ~25%** of total enzyme sales (as compiled in their figures/tables). (kuddus2024cold‐activemicrobialenzymes pages 1-2, kuddus2024cold‐activemicrobialenzymes media 306aa950)
- **Bioremediation statistic:** the same review cites a “pre-optimized biostimulation” achieving **75% pollutant removal in 40 days**. (kuddus2024cold‐activemicrobialenzymes pages 10-12, kuddus2024cold‐activemicrobialenzymes media 306aa950)
- **Cold dairy processing example:** cold-adapted β-galactosidase (optimal 15–18 °C) is used for lactose hydrolysis at low temperature; a cited marine psychrophilic β-galactosidase digested **>80% of lactose in raw milk at 20 °C (pH 6.5)**. (kuddus2024cold‐activemicrobialenzymes pages 2-4)

#### 3) Commercial molecular biology enzymes derived from cold-adapted systems
The 2024 review describes commercial cold-adapted alkaline phosphatases and nucleases, including product examples (e.g., heat-labile nucleases and alkaline phosphatases) and emphasizes the practical advantage of **heat inactivation** after reactions. (kuddus2024cold‐activemicrobialenzymes pages 10-12, kuddus2024cold‐activemicrobialenzymes pages 12-13)

#### 4) Low-temperature biomining/bioleaching implementations (2023)
A 2023 review of eurypsychrophilic acidophiles reports long-running industrial-scale biomining: bioheaps for Ni/Zn/Co/Cu recovery at the Terrafame mine (Finland) have operated since 2008, with winter ambient temperatures between **0 and −20 °C**, though exergonic reactions can create much warmer inner heap regions, implying a role for cold-active acidophiles during initiation and cold-surface niches. (dopson2023eurypsychrophilicacidophilesfrom pages 11-12)

### Expert opinions and analysis (authoritative perspectives)

- **On definitions:** Cavicchioli (ISME J) argues the field should not define psychrophiles purely by Topt/Tmax; these are “arbitrary limits” and can be ecologically misleading, and classification should incorporate ecological context and physiology beyond growth rate. This perspective is central for TraitMech curation because it cautions against inferring mechanisms from simplistic growth categories. (cavicchioli2016ontheconcept pages 1-2)
- **On core constraints and solutions:** D’Amico et al. (EMBO Reports) and De Maayer et al. (EMBO Reports) emphasize that **membrane fluidity**, **macromolecular synthesis/translation constraints**, and **cryoprotection/ice interactions** are principal low-temperature pressures, with convergent solutions across diverse taxa (fatty-acid remodeling, helicases/chaperones, compatible solutes, AFP/IBP, EPS). (damico2006psychrophilicmicroorganismschallenges pages 2-3, maayer2014somelikeit pages 5-6)

### Warnings / curation cautions (do not curate as “core” without qualifiers)

1. **Do not equate “subzero growth” with “psychrophile”:** Planococcus halocryophilus demonstrates that subzero growth can occur in organisms with mesophilic optima; use Tmin/Topt/Tmax and context. (moyer2017psychrophilesandpsychrotrophs pages 1-2)
2. **Avoid using Topt/Tmax-only rules as mechanistic evidence:** they are classification metrics, not mechanisms, and can be misleading about fitness in situ. (cavicchioli2016ontheconcept pages 1-2)
3. **Mark several edges as uncertain where sources use inferential language:** e.g., pigment (carotenoid) buffering of membrane fluidity is “postulated,” and some genome-annotation-based claims (“would maintain ROS balance”) are plausible but not experimentally causal. (maayer2014somelikeit pages 5-6, bao2023miningofkey pages 7-9)
4. **Taxon-specific mechanisms should be flagged:** e.g., *Rhodococcus* RCBS9 relying on USPs/HSPs rather than canonical CSPs, or specific peptidoglycan modifications; curate as candidate edges with taxon/context qualifiers until broader support is added. (li2024mechanismsunderlyingthe pages 9-10)

---

## DOI-first bibliography (with publication dates and URLs)

**2024**
1. Li Q. et al. *Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain Rhodococcus sp. RCBS9.* Frontiers in Microbiology. **Nov 2024**. DOI: **10.3389/fmicb.2024.1465627**. https://doi.org/10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 9-10)
2. Kuddus M. et al. *Cold-active microbial enzymes and their biotechnological applications.* Microbial Biotechnology. **Apr 2024**. DOI: **10.1111/1751-7915.14467**. https://doi.org/10.1111/1751-7915.14467 (kuddus2024cold‐activemicrobialenzymes pages 1-2, kuddus2024cold‐activemicrobialenzymes media 306aa950)
3. Purwar S., Srivastava S. *Adaptations of psychrophilic microorganism to low-temperature environments.* Applied Microbiology: Theory ＆ Technology. **Oct 2024**. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11)

**2023**
4. Bao C. et al. *Mining of key genes for cold adaptation from Pseudomonas fragi D12 and analysis of its cold-adaptation mechanism.* Frontiers in Microbiology. **Jul 2023**. DOI: **10.3389/fmicb.2023.1215837**. https://doi.org/10.3389/fmicb.2023.1215837 (bao2023miningofkey pages 7-9)
5. Yang Z. et al. *Cold-Adapted Proteases: An Efficient and Energy-Saving Biocatalyst.* International Journal of Molecular Sciences. **May 2023**. DOI: **10.3390/ijms24108532**. https://doi.org/10.3390/ijms24108532 (yang2023coldadaptedproteasesan pages 12-14, yang2023coldadaptedproteasesan pages 1-2)
6. Dopson M. et al. *Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.* Frontiers in Microbiology. **Mar 2023**. DOI: **10.3389/fmicb.2023.1149903**. https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 11-12)

**Foundational / high-citation context**
7. De Maayer P. et al. *Some like it cold: understanding the survival strategies of psychrophiles.* EMBO reports. **May 2014**. DOI: **10.1002/embr.201338170**. https://doi.org/10.1002/embr.201338170 (maayer2014somelikeit pages 5-6)
8. Cavicchioli R. *On the concept of a psychrophile.* The ISME Journal. Published online **15 Sep 2015** (issue 2016). DOI: **10.1038/ismej.2015.160**. https://doi.org/10.1038/ismej.2015.160 (cavicchioli2016ontheconcept pages 1-2)
9. D’Amico S. et al. *Psychrophilic microorganisms: challenges for life.* EMBO Reports. **Apr 2006**. DOI: **10.1038/sj.embor.7400662**. https://doi.org/10.1038/sj.embor.7400662 (damico2006psychrophilicmicroorganismschallenges pages 2-3)
10. Moyer C.L. et al. *Psychrophiles and Psychrotrophs.* Reference Module in Life Sciences. **Jan 2017**. DOI: **10.1016/B978-0-12-809633-8.02282-2**. https://doi.org/10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2)

### Citable visual evidence retrieved
Figures/tables summarizing application sectors and quantitative statistics for cold-active enzymes were retrieved from Kuddus et al. 2024. (kuddus2024cold‐activemicrobialenzymes media 306aa950, kuddus2024cold‐activemicrobialenzymes media 3ed86bdd, kuddus2024cold‐activemicrobialenzymes media b3e518d5, kuddus2024cold‐activemicrobialenzymes media 3a7e6893)


References

1. (moyer2017psychrophilesandpsychrotrophs pages 1-2): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

2. (cavicchioli2016ontheconcept pages 1-2): Ricardo Cavicchioli. On the concept of a psychrophile. The ISME Journal, 10:793-795, Sep 2016. URL: https://doi.org/10.1038/ismej.2015.160, doi:10.1038/ismej.2015.160. This article has 131 citations.

3. (maayer2014somelikeit pages 1-2): Pieter De Maayer, Dominique Anderson, Craig Cary, and Don A Cowan. Some like it cold: understanding the survival strategies of psychrophiles. EMBO reports, 15:508-517, May 2014. URL: https://doi.org/10.1002/embr.201338170, doi:10.1002/embr.201338170. This article has 710 citations and is from a highest quality peer-reviewed journal.

4. (dopson2023eurypsychrophilicacidophilesfrom pages 11-12): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

5. (damico2006psychrophilicmicroorganismschallenges pages 2-3): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. The EMBO Reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1134 citations.

6. (maayer2014somelikeit pages 5-6): Pieter De Maayer, Dominique Anderson, Craig Cary, and Don A Cowan. Some like it cold: understanding the survival strategies of psychrophiles. EMBO reports, 15:508-517, May 2014. URL: https://doi.org/10.1002/embr.201338170, doi:10.1002/embr.201338170. This article has 710 citations and is from a highest quality peer-reviewed journal.

7. (bao2023miningofkey pages 7-9): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 21 citations and is from a peer-reviewed journal.

8. (li2024mechanismsunderlyingthe pages 9-10): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

9. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

10. (kuddus2024cold‐activemicrobialenzymes pages 1-2): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

11. (yang2023coldadaptedproteasesan pages 1-2): Zhengfeng Yang, Zhendi Huang, Qian Wu, Xianghua Tang, and Zunxi Huang. Cold-adapted proteases: an efficient and energy-saving biocatalyst. International Journal of Molecular Sciences, 24:8532, May 2023. URL: https://doi.org/10.3390/ijms24108532, doi:10.3390/ijms24108532. This article has 22 citations.

12. (yang2023coldadaptedproteasesan pages 12-14): Zhengfeng Yang, Zhendi Huang, Qian Wu, Xianghua Tang, and Zunxi Huang. Cold-adapted proteases: an efficient and energy-saving biocatalyst. International Journal of Molecular Sciences, 24:8532, May 2023. URL: https://doi.org/10.3390/ijms24108532, doi:10.3390/ijms24108532. This article has 22 citations.

13. (kuddus2024cold‐activemicrobialenzymes pages 2-4): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

14. (kuddus2024cold‐activemicrobialenzymes pages 10-12): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

15. (kuddus2024cold‐activemicrobialenzymes pages 12-13): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

16. (kuddus2024cold‐activemicrobialenzymes media 306aa950): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

17. (kuddus2024cold‐activemicrobialenzymes media 3ed86bdd): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

18. (kuddus2024cold‐activemicrobialenzymes media b3e518d5): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

19. (kuddus2024cold‐activemicrobialenzymes media 3a7e6893): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.