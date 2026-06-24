---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:46:57.646428'
end_time: '2026-06-17T23:04:29.358160'
duration_seconds: 1051.71
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: microaerotolerant
  trait_identifier: METPO:1000610
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: microaerotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that tolerates low levels of molecular oxygen\
    \ (O\u2082) without requiring it."
  parent_traits: METPO:1000601
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.biortech.2011.02.011: microaerotolerant or aerotolerant
    anaerobes can survive (Supports microaerotolerance as survival under limited oxygen
    exposure.) | PMID:30113300: The novel strain stains Gram-negative and Congo-red-negative
    and is characterized mesophilic, neutrophilic, chemoheterotrophic and microaerotolerant
    (Organism example: Simulacricoccus ruber strain MCy10636 is described as microaerotolerant.)'
  causal_graph_summary: 'microaerotolerant_low_oxygen_defense: 5 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** microaerotolerant
- **METPO identifier:** METPO:1000610
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that tolerates low levels of molecular oxygen (O₂) without requiring it.
- **Parent traits:** METPO:1000601
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.biortech.2011.02.011: microaerotolerant or aerotolerant anaerobes can survive (Supports microaerotolerance as survival under limited oxygen exposure.) | PMID:30113300: The novel strain stains Gram-negative and Congo-red-negative and is characterized mesophilic, neutrophilic, chemoheterotrophic and microaerotolerant (Organism example: Simulacricoccus ruber strain MCy10636 is described as microaerotolerant.)
- **Existing causal graph summary:** microaerotolerant_low_oxygen_defense: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **microaerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerotolerant.yaml`.

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
- **Trait label:** microaerotolerant
- **METPO identifier:** METPO:1000610
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that tolerates low levels of molecular oxygen (O₂) without requiring it.
- **Parent traits:** METPO:1000601
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.biortech.2011.02.011: microaerotolerant or aerotolerant anaerobes can survive (Supports microaerotolerance as survival under limited oxygen exposure.) | PMID:30113300: The novel strain stains Gram-negative and Congo-red-negative and is characterized mesophilic, neutrophilic, chemoheterotrophic and microaerotolerant (Organism example: Simulacricoccus ruber strain MCy10636 is described as microaerotolerant.)
- **Existing causal graph summary:** microaerotolerant_low_oxygen_defense: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **microaerotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerotolerant.yaml`.

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


## Research report: Microbial trait “microaerotolerant” (METPO:1000610)

### Scope summary (TraitMech curation focus)
**Microaerotolerant** (METPO:1000610) denotes an oxygen preference/physiological capacity where an organism **tolerates low levels of molecular oxygen (O₂) without requiring O₂**, and may grow both with and without O₂, often with maximal growth at intermediate O₂. In a cultivation-focused oxygen-sensitivity scheme cited in clinical microbiology, **“microaerotolerant”** is defined as: *“growth occurs in the presence or absence of oxygen in the medium; however, maximal growth occurs at intermediate oxygen levels.”* (lagier2015currentandpast pages 3-4). In contrast, **microaerophiles** require low O₂ for growth; e.g., Campylobacter spp. often require an atmosphere of **5% O₂, 10% CO₂, 85% N₂** for optimal recovery (lagier2015currentandpast pages 3-4). A clinical anaerobe methods review further states that **“micro aerotolerant anaerobes”** can exist in environments containing **0–5% O₂**, while obligate anaerobes grow only at very low oxygen (<0.05% O₂), and facultative anaerobes grow with or without oxygen (nwaokorie2021applicationofanaerobic pages 1-2). 

**Boundary cases / nearby traits**:
- **Microaerophile (requires low O₂)** vs **microaerotolerant (does not require O₂; tolerates it)** (lagier2015currentandpast pages 3-4).
- **Aerotolerant anaerobe** is often used in microbiology for organisms that do not respire with O₂ but tolerate it; some sources and datasets may blur “aerotolerant” with “microaerotolerant.” Curate with explicit assay conditions when possible (lagier2015currentandpast pages 3-4, nwaokorie2021applicationofanaerobic pages 1-2).
- **Facultative anaerobe** is distinct mechanistically/energetically (can use O₂ when present), and should not be merged with microaerotolerant unless explicitly defined in the source (nwaokorie2021applicationofanaerobic pages 1-2).

### Key concepts and definitions (current understanding)
Microaerotolerance is best operationalized as an **assay-observed capacity for survival and/or growth under microoxic conditions** (trace-to-low percent O₂), typically explained by:
1) **oxygen consumption/scavenging** (enzymatic O₂ reduction),
2) **reactive oxygen species (ROS) detoxification** (superoxide → H₂O₂ → H₂O),
3) **repair of oxidatively damaged proteins**, and
4) **regulatory control** that tunes defenses to O₂ tension.

Recent mechanistic work in strict anaerobes emphasizes that O₂ exposure often causes endogenous ROS (notably H₂O₂), requiring peroxidases and superoxide detoxification systems (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 10-12).

### Recent developments and latest research (prioritize 2023–2024)
#### 1) O₂-reducing enzyme “coverage” across distinct O₂ tensions (2024)
A major 2024 advance is the resolution, in an obligate anaerobe (*Clostridioides difficile*), of **multiple O₂-reducing enzymes with complementary ranges of action**, effectively “tiling” physiologically relevant microoxic-to-oxic exposures:
- **revRbr2**: active at **<0.4% O₂**
- **FdpA**: **0.4–1% O₂**
- **revRbr1**: **0.1–4% O₂**
- **FdpF**: **>4% O₂ and air**
with differential regulation by σ factors, Spx-family regulator(s), and Rex (caulat2024physiologicalroleand pages 1-2).

The same study provides phenotype-level evidence: an **fdpA mutant shows reduced growth at 0.4% O₂**, supporting a direct genotype→microoxic growth edge (caulat2024physiologicalroleand pages 1-2). 

A key curated visual summary of these O₂ ranges and regulatory relationships is provided in **Figure 8** of Caulat et al. 2024 (caulat2024physiologicalroleand media fefcabd0).

#### 2) Regulatory networks and enzyme cooperation for survival under air/4% O₂ (2025, but mechanistically central and tightly linked to 2024)
While 2025, Lotoux et al. provide high-resolution causal support for how strict anaerobes survive oxygen exposure, including: 
- **Rubrerythrin (Rbr)** and **peroxiredoxin (Bcp)** as central H₂O₂ detoxifiers that **promote survival in H₂O₂, air, or 4% O₂** (lotoux2025defensearsenalof pages 1-2).
- Induction of defense genes upon **H₂O₂ or air exposure** (lotoux2025defensearsenalof pages 1-2).
- O₂-dependent thresholds: **1% O₂** exposure produced no H₂O₂/survival phenotype, while **4% O₂** triggered H₂O₂ production and survival defects in detoxification mutants (lotoux2025defensearsenalof pages 10-12).
- Explicit regulator edges: **PerR** (H₂O₂-sensing repressor) and **OseR** (O₂-responsive regulator) for the rbr operon, and **σB control of bcp** (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 12-15).

These results strengthen TraitMech edges linking microoxic/low-percent O₂ to ROS intermediates and defense modules.

#### 3) Quantitative oxygen tolerance metrics in anaerobic ammonium oxidizers (anammox; 2023)
Okabe et al. quantify oxygen inhibition kinetics for multiple anammox taxa, using IC50 and DOmax:
- Freshwater taxa: **IC50 = 2.7–4.2 µM DO** and **DOmax = 10.9–26.6 µM DO**, with complete inhibition around ~25 µM DO (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand pages 6-7).
- Marine “Ca. Scalindua sp.”: markedly higher tolerance (**IC50 = 18.0 µM**, **DOmax = 51.6 µM**), and recovery after prolonged exposure to low-percent and even air exposures (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand pages 6-7).
This work also reports that O₂ reduction rates were **~10,000-fold lower than N₂ production rates**, supporting detoxification rather than aerobic respiration as the role of O₂ handling (okabe2023oxygentoleranceand pages 5-6).

#### 4) Strain-dependent oxygen resilience in gut obligate anaerobes (2023)
In *Faecalibacterium* (candidate next-generation probiotic genus), Botin et al. show strain-dependent survival and rapid induction of detoxification genes:
- Air exposure upregulated the two **SOR** genes by **>150-fold** after 10 min and **rbr** by **~30-fold** after 15 min (botin2023thetoleranceof pages 5-7).
- Under agitation/aeration, cysteine strongly modulated survival: with cysteine, strain L2-6 survived to ~10 min; without cysteine, a **3-log CFU decrease after 5 min** occurred; cysteine also reduced extracellular superoxide accumulation (botin2023thetoleranceof pages 5-7).
These provide strong edges for “environment/media metabolite → ROS level → survival under O₂”.

### Current applications and real-world implementations
1) **Culturing and diagnostics**: Clinical microbiology workflows explicitly manipulate microaerobic or low-O₂ atmospheres; distinguishing microaerophilic vs microaerotolerant growth supports recovery of fastidious taxa (e.g., using defined gas mixtures such as 5% O₂ for microaerophiles) (lagier2015currentandpast pages 3-4).

2) **Next-generation probiotics / anaerobe bioprocessing**: Oxygen sensitivity is a major barrier to cultivating and exploiting beneficial gut anaerobes. Mechanistic identification of detoxification systems (flavodiiron proteins, rubrerythrins, SORs) and protective media components (e.g., cysteine) supports more robust manufacturing and formulation strategies (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 5-7).

3) **Industrial and laboratory-scale anaerobe growth under trace O₂**: For *Phocaeicola vulgatus* (formerly *Bacteroides vulgatus*), a RAMOS-based gassed cultivation showed **unrestricted growth up to 0.7 vol% O₂**, with rapid viability loss at **≥1.3 vol% O₂**, indicating a practical tolerance window relevant to scale-up and gas control (keitel2023carbondioxideand pages 1-2).

4) **Environmental microbiology: oxic–anoxic transition zones**: Sulfate-reducing bacteria (SRB) can persist in fluctuating redox regimes. In a long-term bioreactor mimicking peatland conditions, SRB established populations despite weekly oxic phases at **133 µM O₂ (50% air saturation)**, with transcriptomic evidence for oxygen consumption, ROS detoxification, and repair systems (dyksma2024growthofsulfatereducing pages 1-2).

5) **Wastewater nitrogen removal and marine nitrogen loss modeling**: Quantitative IC50/DOmax values for anammox oxygen sensitivity inform both **engineered reactor design** and **marine nitrogen loss models** by constraining how microoxia inhibits anammox activity (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand pages 6-7).

### Expert opinions and analysis (authoritative synthesis)
A 2025 Infection and Immunity review frames oxygen tension as a central ecological control shaping gut microbiota resilience: inflammation-associated increases in luminal oxygen favor facultative anaerobes and deplete strict anaerobes, motivating mechanistic attention to anaerobe O₂/ROS defenses (rose2025commensalresilienceancient pages 7-9). The review also highlights canonical anaerobe detoxification logic: **SOR reduces superoxide using reduced electron donors (e.g., NADH)** and peroxidases (including rubrerythrins) reduce **H₂O₂ to water**, with success constrained by electron donor availability (rose2025commensalresilienceancient pages 9-11). 

Mechanistically, the strongest recent “expert-level” inference suitable for TraitMech is that **microaerotolerance is frequently an emergent property of (i) O₂-reducing enzymes with tension-specific ranges, (ii) ROS detoxification modules, and (iii) redox-sensing regulation (e.g., Rex, σB, Spx-family factors) that couples defense deployment to NADH/NAD⁺ balance and oxidative challenge** (caulat2024physiologicalroleand pages 1-2, lotoux2025defensearsenalof pages 1-2).

### Relevant statistics and data (recent studies)
- **C. difficile O₂-defense enzyme action ranges**: revRbr2 <0.4% O₂; FdpA 0.4–1% O₂; revRbr1 0.1–4% O₂; FdpF >4% O₂/air (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0).
- **O₂ threshold for mutant phenotypes (C. difficile)**: 1% O₂ produced no H₂O₂/survival phenotype, while 4% O₂ triggered H₂O₂ production and survival defects in detoxification mutants (lotoux2025defensearsenalof pages 10-12).
- **Faecalibacterium gene induction under air**: SORs >150-fold at 10 min; rbr ~30-fold at 15 min (botin2023thetoleranceof pages 5-7).
- **Faecalibacterium survival modulation by cysteine**: without cysteine, ~3-log CFU decrease after 5 min aeration; with cysteine, survival up to 10 min under aeration with agitation (botin2023thetoleranceof pages 5-7).
- **Anammox oxygen inhibition kinetics**: freshwater IC50 2.7–4.2 µM DO and DOmax 10.9–26.6 µM DO; marine Scalindua IC50 18.0 µM and DOmax 51.6 µM DO (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand pages 6-7).
- **SRB periodic oxygen stress**: populations persisted with weekly oxic phases at 133 µM O₂ (50% air saturation) over >200 days (dyksma2024growthofsulfatereducing pages 1-2).
- **Phocaeicola vulgatus gas-supply thresholds**: unrestricted growth up to 0.7 vol% O₂; viability decreases rapidly at ≥1.3 vol% O₂ (keitel2023carbondioxideand pages 1-2).

---

## Candidate nodes grouped by type (curation-ready)
| Category | Node label | Node type | Suggested ontology grounding | Brief role in microaerotolerance | Key supporting citations |
|---|---|---|---|---|---|
| Environmental/assay conditions | low oxygen tension | environmental condition | ENVO:environmental oxygen level (unresolved exact term) | Core environmental state defining the trait; supports survival/growth under limited O2 rather than strict anoxia or full aerobiosis. | (lagier2015currentandpast pages 3-4, nwaokorie2021applicationofanaerobic pages 1-2, caulat2024physiologicalroleand pages 1-2) |
| Environmental/assay conditions | intermediate oxygen level | assay/environmental condition | unresolved | Operational culture condition for microaerotolerant behavior; maximal growth may occur at intermediate O2. | (lagier2015currentandpast pages 3-4) |
| Environmental/assay conditions | microaerobic atmosphere (e.g., 5% O2, 10% CO2, 85% N2) | assay condition | unresolved | Useful boundary comparator distinguishing microaerophily from microaerotolerance in cultivation assays. | (lagier2015currentandpast pages 3-4) |
| Environmental/assay conditions | air exposure | assay perturbation | ENVO:atmospheric air (unresolved exact term) | Strong oxidative challenge used experimentally to test whether defense systems preserve viability outside strict anoxia. | (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 1-2) |
| Environmental/assay conditions | gut lumen oxygen gradient (0.1-0.4% colon lumen; ~4-5% small intestine) | host-associated environmental context | ENVO:gut lumen (unresolved exact term) | Physiologically relevant low-O2 context explaining why anaerobes encounter and must tolerate limited O2 in vivo. | (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| Environmental/assay conditions | periodic oxygen stress at 133 uM O2 (50% air saturation) | experimental factor | unresolved | Demonstrates that some sulfate-reducing anaerobes persist through repeated oxic phases, motivating defense-node inclusion. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Reactive oxygen species | molecular oxygen | chemical | CHEBI:15379 | Primary stressor; low levels can be scavenged or reduced by specialized enzymes enabling microaerotolerance. | (caulat2024physiologicalroleand pages 1-2, okabe2023oxygentoleranceand pages 12-12) |
| Reactive oxygen species | superoxide | chemical | CHEBI:18421 | Toxic ROS generated during O2 exposure; detoxification is a major mechanism of limited O2 tolerance. | (lotoux2025defensearsenalof pages 1-2, rose2025commensalresilienceancient pages 9-11, rose2025commensalresilienceancient pages 7-9) |
| Reactive oxygen species | hydrogen peroxide | chemical | CHEBI:16240 | Central ROS intermediate/product detoxified by rubrerythrin, peroxiredoxin, catalase/peroxidases, and related systems. | (lotoux2025defensearsenalof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2, rose2025commensalresilienceancient pages 9-11) |
| Reactive oxygen species | hydroxyl radical | chemical | CHEBI:16243 | Highly damaging downstream ROS; motivates peroxide-removal and repair systems though often not directly scavenged. | (dyksma2024growthofsulfatereducing pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| Detoxification enzymes/proteins | flavodiiron protein FdpA | protein | GO:0018699 oxygen reductase activity (candidate), EC unresolved | O2-reducing enzyme active at low/intermediate O2 (0.4-1%) in C. difficile; candidate direct microaerotolerance effector. | (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0) |
| Detoxification enzymes/proteins | flavodiiron protein FdpF | protein | GO:0018699 oxygen reductase activity (candidate), EC unresolved | O2-reducing enzyme functioning mainly at >4% O2 and air; expands tolerance range toward higher oxidative exposure. | (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0) |
| Detoxification enzymes/proteins | reverse rubrerythrin 1 (revRbr1) | protein | GO:0055114 oxidation-reduction process (broad), EC unresolved | Broad-range O2-reducing/peroxidase-like defense enzyme active from ~0.1-4% O2 in C. difficile. | (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0) |
| Detoxification enzymes/proteins | reverse rubrerythrin 2 (revRbr2) | protein | GO:0055114 oxidation-reduction process (broad), EC unresolved | Low-O2-specialized defense enzyme active below 0.4% O2, matching microoxic survival conditions. | (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0) |
| Detoxification enzymes/proteins | rubrerythrin (Rbr) | protein | GO:0055114 oxidation-reduction process (broad), EC unresolved | Peroxidase/O2-defense enzyme detoxifying H2O2 and promoting survival in H2O2, air, or 4% O2; recurring anaerobe defense node. | (lotoux2025defensearsenalof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2, rose2025commensalresilienceancient pages 9-11, botin2023thetoleranceof pages 1-2) |
| Detoxification enzymes/proteins | superoxide reductase (Sor/SOR) | protein | EC 1.15.1.2 | Reduces superoxide to H2O2 in many anaerobes; key alternative to SOD in low-O2-tolerant strict anaerobes. | (lotoux2025defensearsenalof pages 1-2, rose2025commensalresilienceancient pages 9-11, okabe2023oxygentoleranceand pages 12-12, botin2023thetoleranceof pages 1-2) |
| Detoxification enzymes/proteins | peroxiredoxin Bcp | protein | GO:0051920 peroxiredoxin activity | Detoxifies H2O2 and contributes to survival during air or 4% O2 exposure in C. difficile. | (lotoux2025defensearsenalof pages 1-2) |
| Detoxification enzymes/proteins | superoxide dismutase (Sod/SodA) | protein | EC 1.15.1.1 | Converts superoxide to H2O2; present in some microaerotolerant anaerobes and associated with higher O2 tolerance in anammox and gut taxa. | (lotoux2025defensearsenalof pages 1-2, okabe2023oxygentoleranceand pages 12-12, rose2025commensalresilienceancient pages 7-9) |
| Detoxification enzymes/proteins | catalase / catalase-peroxidase (KatG) | protein | EC 1.11.1.6 / EC 1.11.1.21 | Removes H2O2; not universal in strict anaerobes but contributes to oxygen defense where present, including SRB and Scalindua-like anammox. | (dyksma2024growthofsulfatereducing pages 1-2, okabe2023oxygentoleranceand pages 12-12) |
| Detoxification enzymes/proteins | alkyl hydroperoxide reductase (Ahp) | protein complex/enzyme | EC 1.11.1.26 | Detoxifies organic peroxides/H2O2; part of sulfate-reducer and gut anaerobe oxidative defense repertoires. | (dyksma2024growthofsulfatereducing pages 1-2, rose2025commensalresilienceancient pages 9-11, botin2023thetoleranceof pages 1-2) |
| Detoxification enzymes/proteins | rubredoxin:oxygen oxidoreductase (Roo/NorV) | enzyme | EC unresolved | Direct O2-consuming enzyme in sulfate-reducing anaerobes; candidate oxygen-scavenging effector supporting survival under transient O2. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Detoxification enzymes/proteins | bd-type quinol oxidase (CydAB) | membrane protein complex | GO:0004129 cytochrome-c oxidase activity (approximate family-level only), EC unresolved | Terminal oxidase implicated in oxygen consumption/scavenging under low-O2 stress in anaerobe communities. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Detoxification enzymes/proteins | heme-copper oxygen reductase | membrane protein complex | EC unresolved | Membrane O2 reductase supporting oxygen consumption in some sulfate-reducing taxa under periodic oxic stress. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Detoxification enzymes/proteins | neelaredoxin / desulfoferrodoxin | protein | unresolved | Superoxide-scavenging proteins cited as anaerobe alternatives to classical aerobic ROS enzymes. | (okabe2023oxygentoleranceand pages 12-12) |
| Regulatory factors | PerR | transcriptional regulator | GO:0006979 response to oxidative stress (process), UniProt unresolved | H2O2-sensing repressor linked to rbr-sor operon control; activates appropriate ROS defense upon oxidative challenge. | (lotoux2025defensearsenalof pages 1-2) |
| Regulatory factors | sigma B (σB) | sigma factor | GO:0006970 response to osmotic stress / stress-response regulator (broad), UniProt unresolved | Global stress sigma factor controlling oxidative-stress genes such as bcp and influencing rbr operon induction. | (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 1-2) |
| Regulatory factors | OseR | transcriptional regulator | unresolved | O2-responsive regulator contributing to induction of the rbr operon in C. difficile during oxygen exposure. | (lotoux2025defensearsenalof pages 1-2) |
| Regulatory factors | Spx-family regulator | transcriptional regulator | unresolved | Induces fdp and revrbr genes upon O2 exposure, providing layered regulation of O2-reducing defenses. | (caulat2024physiologicalroleand pages 1-2) |
| Regulatory factors | Rex | redox-sensing transcriptional regulator | unresolved | Senses NADH/NAD+ ratio and regulates fdpF, linking redox state to O2-defense deployment. | (caulat2024physiologicalroleand pages 1-2) |
| Regulatory factors | OxyR | transcriptional regulator | GO:0006979 response to oxidative stress (process), UniProt unresolved | Canonical oxidative-stress regulator highlighted for gut anaerobes such as Bacteroides; useful comparator node across taxa. | (rose2025commensalresilienceancient pages 9-11) |
| Electron donors/redox partners | NADH | metabolite | CHEBI:57945 | Electron donor for O2/ROS detoxification enzymes including FdpF and SOR-linked systems; donor availability constrains tolerance. | (rose2025commensalresilienceancient pages 9-11, caulat2024physiologicalroleand pages 1-2) |
| Electron donors/redox partners | NADPH | metabolite | CHEBI:57783 | Reducing equivalent for peroxide detoxification in several anaerobe antioxidant systems. | (lotoux2025defensearsenalof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| Electron donors/redox partners | rubredoxin | electron carrier protein | UniProt unresolved | Transfers electrons to SOR/rubrerythrin-class defenses and oxygen-reducing pathways in anaerobes. | (lotoux2025defensearsenalof pages 1-2, okabe2023oxygentoleranceand pages 12-12) |
| Electron donors/redox partners | NADH:rubredoxin oxidoreductase (NROR) | enzyme | EC unresolved | Reduces rubredoxin using NADH, supplying electrons to SOR/rubrerythrin-like ROS detoxification systems. | (lotoux2025defensearsenalof pages 1-2, okabe2023oxygentoleranceand pages 12-12) |
| Electron donors/redox partners | thioredoxin (TrxA) | protein | GO:0004791 thioredoxin-disulfide reductase activity (pathway partner unresolved) | Redox carrier supporting peroxide defense and repair of oxidized proteins under O2 stress. | (dyksma2024growthofsulfatereducing pages 1-2, thomashoff2024survivalofoxidative pages 46-48) |
| Electron donors/redox partners | thioredoxin reductase (TrxB/TrxR) | enzyme | EC 1.8.1.9 | Regenerates reduced thioredoxin, sustaining peroxide detoxification and repair circuits during oxidative stress. | (dyksma2024growthofsulfatereducing pages 1-2, thomashoff2024survivalofoxidative pages 46-48) |
| Electron donors/redox partners | cysteine | metabolite | CHEBI:17561 | Lowers extracellular superoxide production and improves survival of some Faecalibacterium strains under high O2 tension. | (botin2023thetoleranceof pages 1-2) |
| Electron donors/redox partners | flavins / extracellular electron shuttle | metabolite/process node | CHEBI:30527 flavin | Enables extracellular electron transfer to O2 in some gut anaerobes, providing an alternate oxygen-handling route. | (rose2025commensalresilienceancient pages 9-11, botin2023thetoleranceof pages 1-2) |
| Repair systems | ClpB-DnaK chaperone system | protein complex/system | GO:0061077 chaperone-mediated protein folding | Repairs/protects proteins damaged during periodic oxygen stress in sulfate-reducing anaerobes. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Repair systems | GroEL/GroES (GroLS) chaperonin system | protein complex | GO:0006457 protein folding | Supports refolding/protection of oxidatively damaged proteins during oxic-anoxic transitions. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Repair systems | methionine sulfoxide reductase (MsrA) | enzyme | EC 1.8.4.11 | Repairs oxidized methionine residues in proteins, mitigating oxidative damage associated with O2 exposure. | (dyksma2024growthofsulfatereducing pages 1-2) |
| Repair systems | oxidized protein repair | biological process | GO:0030091 protein repair | Higher-level process node capturing recovery of damaged enzymes/proteins needed for persistence under low O2. | (dyksma2024growthofsulfatereducing pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| Repair systems | iron-sulfur enzyme protection / metabolic rerouting | biological process | GO:0006091 generation of precursor metabolites and energy (broad), unresolved specific term | Anaerobes may reroute metabolism away from O2-sensitive iron-sulfur and glycyl-radical enzymes to preserve viability under microoxic conditions. | (rose2025commensalresilienceancient pages 7-9) |


*Table: This table lists curation-ready candidate nodes for a microaerotolerant trait causal graph, organized by mechanistic category and grounded where possible to stable ontologies. It emphasizes recent evidence on O2-reducing enzymes, ROS detoxification, regulation, redox partners, and repair systems relevant to low-oxygen survival.*

---

## Candidate causal edges (evidence-backed triples)
| Edge (S–P–O) | Edge type | Taxon scope | Evidence strength | Supporting snippet | Reference (DOI + URL + publication month/year) | Citations (pqac IDs) | Notes for curation |
|---|---|---|---|---|---|---|---|
| low oxygen tension → enables survival/growth of → microaerotolerant cells | environmental | broad | medium | Microaerotolerant organisms can exist at low O2 and are defined by growth in presence or absence of O2, often with better growth at intermediate O2 | Lagier et al. DOI:10.1128/CMR.00110-14 https://doi.org/10.1128/cmr.00110-14 Jan 2015; Nwaokorie et al. DOI:10.52968/23689336 https://doi.org/10.52968/23689336 Jan 2021 | (lagier2015currentandpast pages 3-4, nwaokorie2021applicationofanaerobic pages 1-2) | Good scope edge for trait definition; phenotype-level, not mechanism-specific |
| intermediate oxygen level → maximizes growth of → microaerotolerant cells | environmental | broad | medium | “growth occurs in the presence or absence of oxygen… however, maximal growth occurs at intermediate oxygen levels” | Lagier et al. DOI:10.1128/CMR.00110-14 https://doi.org/10.1128/cmr.00110-14 Jan 2015 | (lagier2015currentandpast pages 3-4) | Useful definitional edge; curate carefully because wording derives from cultivation classification rather than a molecular mechanism |
| microaerotolerant anaerobes → tolerate → 0–5% O2 environments | environmental | broad | weak | Review states microaerotolerant anaerobes “do not use oxygen to live” but can exist in “0–5% oxygen” | Nwaokorie et al. DOI:10.52968/23689336 https://doi.org/10.52968/23689336 Jan 2021 | (nwaokorie2021applicationofanaerobic pages 1-2) | Review-only and terminology may mix “microaerotolerant anaerobe” with related classes; mark uncertain |
| microaerophilic atmosphere (5% O2, 10% CO2, 85% N2) → supports optimal recovery of → microaerophiles | environmental | broad comparator | strong | Campylobacter require “5% O2, 10% CO2, and 85% N2 for optimal recovery” | Lagier et al. DOI:10.1128/CMR.00110-14 https://doi.org/10.1128/cmr.00110-14 Jan 2015 | (lagier2015currentandpast pages 3-4) | Comparator edge to distinguish microaerophily from microaerotolerance; not direct trait mechanism |
| O2 exposure → induces expression of → fdp and revrbr genes | regulatory | taxon-specific: *Clostridioides difficile* | strong | “a member of the Spx family contributes to induction of fdp and revrbr genes upon O2 exposure” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Strong recent regulatory evidence; taxon-specific but mechanistically valuable |
| revRbr2 → protects against → O2 tensions <0.4% | mechanistic | taxon-specific: *C. difficile* | strong | revRbr2 is “specific to low O2 tensions (<0.4%)” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Excellent quantitative edge for low-O2 tolerance range |
| FdpA → protects against → O2 tensions 0.4–1% | mechanistic | taxon-specific: *C. difficile* | strong | FdpA acts at “low and intermediate O2 tensions (0.4%–1%)” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Strong quantitative edge; maps well to microoxic range |
| revRbr1 → protects against → O2 tensions 0.1–4% | mechanistic | taxon-specific: *C. difficile* | strong | revRbr1 “has a wider spectrum of activity (0.1%–4%)” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Broadest low/intermediate O2 range among the four enzymes |
| FdpF → protects against → O2 tensions >4% and air | mechanistic | taxon-specific: *C. difficile* | strong | FdpF is “more specific to tensions >4% and air” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | More relevant to upper boundary of tolerance than core microaerotolerance |
| fdpA loss-of-function → reduces growth at → 0.4% O2 | mechanistic | taxon-specific: *C. difficile* | strong | “an fdpA mutant shows reduced growth at 0.4% O2” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Direct genotype–phenotype evidence; high curation value |
| FdpF → receives electrons directly from → NADH | mechanistic | taxon-specific: *C. difficile* | strong | “FdpF receives electrons directly from NADH” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Good biochemical edge connecting redox metabolism to tolerance |
| Spx-family regulator → induces on O2 exposure → fdp/revrbr genes | regulatory | taxon-specific: *C. difficile* | strong | “a regulator of the Spx family… plays a role in the induction of fdp and revrbr genes upon O2 exposure” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Strong but regulator identity may need exact gene/protein grounding before YAML curation |
| Rex → regulates → fdpF expression | regulatory | taxon-specific: *C. difficile* | strong | “fdpF is regulated by Rex, a regulator sensing the NADH/NAD+ ratio” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Valuable link between redox state and O2 defense |
| σB → controls expression of → revRbr2 | regulatory | taxon-specific: *C. difficile* | strong | “revrbr2 is under the dual control of σA and σB” | Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024 | (caulat2024physiologicalroleand pages 1-2) | Specific, curation-ready regulatory edge |
| Sor → detoxifies → superoxide | mechanistic | taxon-specific: *C. difficile*; broad analogs in anaerobes | strong | Sor has “superoxide reductase activity in vitro” and “protects the bacterium from exposure to menadione” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | Strong direct enzymology plus phenotype |
| Rbr → detoxifies → H2O2 | mechanistic | taxon-specific: *C. difficile*; broad analogs in anaerobes | strong | “Rbr… plays a central role in the detoxification of H2O2” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | Strong; broadly plausible across anaerobes but direct proof here is taxon-specific |
| Bcp → detoxifies → H2O2 | mechanistic | taxon-specific: *C. difficile* | strong | Bcp together with Rbr “plays a central role in the detoxification of H2O2” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | Strong direct evidence |
| Rbr + Bcp → promote survival in → air or 4% O2 | mechanistic | taxon-specific: *C. difficile* | strong | Rbr and Bcp “promotes the survival of C. difficile in the presence of not only H2O2 but also air or 4% O2” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | One of the strongest direct microaerotolerance edges in the set |
| high O2 exposure → generates endogenous → H2O2 | mechanistic | taxon-specific: *C. difficile*; broad concept | strong | “Under high O2 concentrations… the bacterium generated endogenous H2O2” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | Important causal intermediate linking O2 to peroxide detoxification modules |
| H2O2 or air exposure → induces expression of → ROS reductase genes and CD0828 | regulatory | taxon-specific: *C. difficile* | strong | “The expression of the genes encoding the ROS reductases and the CD0828 protein was induced upon exposure to either H2O2 or air” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2) | Strong induction edge for stress-response graph |
| PerR → represses/controls → rbr operon | regulatory | taxon-specific: *C. difficile* | strong | “The induction of the rbr operon is mediated… by PerR” and PerR is a “H2O2-sensing repressor” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 10-12) | Good regulatory edge; predicate may be ‘negatively regulates’ depending YAML schema |
| OseR → regulates → rbr operon | regulatory | taxon-specific: *C. difficile* | strong | “OseR, a recently identified O2-responsive regulator… mediates” induction of the rbr operon | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 12-15) | Strong O2-responsive regulatory edge |
| σB → controls expression of → bcp | regulatory | taxon-specific: *C. difficile* | strong | “the expression of bcp is only controlled by σB” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 12-15) | Very curation-ready |
| 4% O2 exposure → causes survival defects in → detoxification mutants | environmental | taxon-specific: *C. difficile* | strong | At 1% O2 no phenotype was detected, whereas “4% O2 triggers H2O2 production and survival defects in detoxification mutants” | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025 | (lotoux2025defensearsenalof pages 10-12) | Helpful quantitative threshold edge; mutant-dependent phenotype |
| air exposure → upregulates >150-fold → SOR genes | regulatory | taxon-specific: *Faecalibacterium longum* L2-6 | strong | “Exposure to air upregulated the genes encoding the two SORs >150-fold after 10 min” | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 5-7) | Strong induction evidence but strain-specific |
| air exposure → upregulates 30-fold → rbr gene | regulatory | taxon-specific: *Faecalibacterium longum* L2-6 | strong | Air induced “the Rbr-encoding gene 30-fold after 15 min” | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 5-7) | Strong induction evidence but strain-specific |
| SORs → protect against → air exposure | mechanistic | taxon-specific: *Faecalibacterium longum* L2-6 | medium | SORs are “crucial for protection against air likely through the detoxification of endogenous” superoxide | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 5-7) | Mechanistic inference from induction and survival; slightly less direct than knockout evidence |
| cysteine → limits extracellular superoxide and improves survival under → high O2 tension | mechanistic | taxon-specific: *Faecalibacterium longum* L2-6 | strong | Cysteine “limited the production of extracellular O2− and improved the survival… under high O2 tension” | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 5-7) | Useful metabolite edge; likely assay/media-dependent |
| extracellular flavin/thiol electron shuttle → transfers electrons to → O2 | mechanistic | taxon-specific: *Faecalibacterium duncaniae* A2-165 | medium | Growth at low O2 uses “an extracellular flavin/thiol electron shuttle to transfer electrons to O2” | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 1-2) | Valuable but taxon-specific and somewhat inferential |
| periodic oxygen stress (133 µM O2; 50% air saturation) → permits persistence/growth of → sulfate-reducing bacteria populations | environmental | taxon-specific community: peatland SRB | strong | SRB “established growing populations despite weekly oxygen exposures at 133 µM (50% air saturation)” | Dyksma & Pester DOI:10.1186/s40168-024-01909-7 https://doi.org/10.1186/s40168-024-01909-7 Oct 2024 | (dyksma2024growthofsulfatereducing pages 1-2) | Strong ecological evidence for oxygen tolerance under fluctuating conditions |
| Roo/NorV, heme-copper oxidase, bd oxidase → consume O2 and defend against → oxygen stress | mechanistic | taxon-specific community: SRB | medium | SRB possess “oxygen-reducing enzymes… that function as defenses by consuming O2” | Dyksma & Pester DOI:10.1186/s40168-024-01909-7 https://doi.org/10.1186/s40168-024-01909-7 Oct 2024 | (dyksma2024growthofsulfatereducing pages 1-2) | Good mechanism class edge; taxa and exact enzyme usage vary |
| KatG/Ahp/Rbr-revRbr → detoxify → ROS during oxygen exposure | mechanistic | taxon-specific community: SRB; broad analogs | medium | “Classic ROS-detoxifying enzymes are listed (KatG, Ahp, Rbr/revRbr)” | Dyksma & Pester DOI:10.1186/s40168-024-01909-7 https://doi.org/10.1186/s40168-024-01909-7 Oct 2024 | (dyksma2024growthofsulfatereducing pages 1-2) | Community transcriptomic support; enzyme-specific causality less direct |
| sustained transcription of oxygen defense genes → supports persistence during → oxic phases | regulatory | taxon-specific community: SRB | medium | Some SRB “maintained high transcript levels of genes encoding oxygen defense proteins even under anoxic conditions” and persisted under redox switching | Dyksma & Pester DOI:10.1186/s40168-024-01909-7 https://doi.org/10.1186/s40168-024-01909-7 Oct 2024 | (dyksma2024growthofsulfatereducing pages 1-2) | Strong ecological association, but individual gene-to-phenotype causality is diffuse |
| superoxide reductase → reduces → superoxide to H2O2 | mechanistic | broad | medium | Review notes SOR reduces superoxide using electrons from donors like NADH | Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (rose2025commensalresilienceancient pages 9-11) | Broad conceptual edge; good for generic graph backbone |
| rubrerythrin/peroxidases → reduce → H2O2 to water | mechanistic | broad | medium | Review states Rbr/peroxidases reduce H2O2 to water | Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (rose2025commensalresilienceancient pages 9-11) | Broad mechanism edge consistent with primary studies |
| available NADH/reduced electron donors → enables function of → SOR/Rbr defenses | mechanistic | broad | medium | “The protection conferred by SOR/Rbr depends on available reduced electron donors” | Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (rose2025commensalresilienceancient pages 9-11) | Important systems-level edge; review synthesis rather than direct experiment |
| high oxidative stress with donor depletion → limits protection by → SOR/Rbr systems | mechanistic | broad | weak | Review notes SOR/Rbr protection “can fail under high oxidative stress when donors are depleted” | Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (rose2025commensalresilienceancient pages 9-11) | Useful cautionary edge; broad inference, not curation-priority |
| many Bacteroidetes cannot grow above → ~0.5% O2 | environmental | broad within Bacteroidetes | medium | Review states many Bacteroidetes “cannot grow above micromolar O2 levels (>~0.5% O2)” | Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (rose2025commensalresilienceancient pages 9-11) | Helpful boundary statistic; not directly microaerotolerant unless mapped to specific taxa |
| gut lumen oxygen gradient (colon lumen ~0.1–0.4%, mucus 1–2%, tissues up to ~5%) → creates selection for → low-O2 defense systems | environmental | broad host-associated anaerobes | medium | Gut O2 gradients range from colon lumen 0.1–0.4% to ~5% in tissues, exposing anaerobes to low O2 during colonization/inflammation | Lotoux et al. DOI:10.1128/mbio.03753-24 https://doi.org/10.1128/mbio.03753-24 Apr 2025; Caulat et al. DOI:10.1128/mbio.01591-24 https://doi.org/10.1128/mbio.01591-24 Oct 2024; Rose et al. DOI:10.1128/IAI.00502-24 https://doi.org/10.1128/iai.00502-24 Jun 2025 | (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 1-2, rose2025commensalresilienceancient pages 7-9) | Strong contextual edge for environment→mechanism; indirect but biologically important |
| strict anaerobes → differ from → facultative anaerobes by inability to use O2 for growth | environmental | broad comparator | medium | Facultative anaerobes “grow and survive with or without free oxygen”; strict anaerobes require very low O2 | Nwaokorie et al. DOI:10.52968/23689336 https://doi.org/10.52968/23689336 Jan 2021 | (nwaokorie2021applicationofanaerobic pages 1-2) | Comparator edge for scope clarification, not mechanism |
| oxidative-stress detoxifying enzyme repertoire → underlies strain-dependent O2 tolerance in → Faecalibacterium | mechanistic | taxon-specific genus-level | medium | Genomes vary in detoxifying enzymes, and “strains differed widely in their sensitivity” | Botin et al. DOI:10.1128/AEM.00606-23 https://doi.org/10.1128/aem.00606-23 Jul 2023 | (botin2023thetoleranceof pages 1-2) | Good gene-content-to-phenotype edge; association stronger than direct causation |


*Table: This table compiles candidate subject–predicate–object edges for a TraitMech causal graph of microaerotolerance, emphasizing direct mechanistic and regulatory evidence from recent anaerobe oxygen-stress literature. It is useful for selecting curation-ready edges, separating broad definitional/context edges from stronger taxon-specific molecular mechanisms.*

---

## Warnings / curation risks (do not curate without qualifiers)
1) **Terminology drift (“microaerotolerant” vs “aerotolerant anaerobe”)**: Some reviews and datasets may conflate oxygen tolerance classes; prioritize sources that specify gas composition, O₂ %, DO (µM), or explicit assay methodology (lagier2015currentandpast pages 3-4, nwaokorie2021applicationofanaerobic pages 1-2).
2) **Taxon- and strain-specificity**: Many strong edges are proven in particular taxa (e.g., *C. difficile*, *Faecalibacterium longum* L2-6, specific SRB communities). Curate such edges with explicit taxon scope (NCBITaxon) and avoid overgeneralizing to “microaerotolerant bacteria” broadly (caulat2024physiologicalroleand pages 1-2, botin2023thetoleranceof pages 5-7, dyksma2024growthofsulfatereducing pages 1-2).
3) **Assay/media dependence**: Metabolite effects (e.g., cysteine) and agitation/aeration strongly change outcomes; treat as experimental-factor nodes and annotate context (botin2023thetoleranceof pages 5-7).
4) **Community-level inference**: Metatranscriptomic association in SRB communities supports mechanism classes but does not always prove necessity/sufficiency of individual genes; mark such edges as medium evidence unless coupled to isolate genetics (dyksma2024growthofsulfatereducing pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates)
- Caulat LC et al. **Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.** *mBio* (Oct 2024). DOI:10.1128/mbio.01591-24. https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand media fefcabd0)
- Dyksma S, Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O2 saturation.** *Microbiome* (Oct 2024). DOI:10.1186/s40168-024-01909-7. https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 1-2)
- Keitel L et al. **Carbon dioxide and trace oxygen concentrations impact growth and product formation of the gut bacterium *Phocaeicola vulgatus*.** *BMC Microbiology* (Dec 2023). DOI:10.1186/s12866-023-03127-x. https://doi.org/10.1186/s12866-023-03127-x (keitel2023carbondioxideand pages 1-2)
- Botin T et al. **The tolerance of gut commensal *Faecalibacterium* to oxidative stress is strain dependent and relies on detoxifying enzymes.** *Applied and Environmental Microbiology* (Jul 2023). DOI:10.1128/aem.00606-23. https://doi.org/10.1128/aem.00606-23 (botin2023thetoleranceof pages 1-2, botin2023thetoleranceof pages 5-7)
- Okabe S et al. **Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria.** *ISME Communications* (May 2023). DOI:10.1038/s43705-023-00251-7. https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand pages 6-7)
- Lotoux A et al. **Defense arsenal of the strict anaerobe *Clostridioides difficile* against reactive oxygen species encountered during its infection cycle.** *mBio* (Apr 2025). DOI:10.1128/mbio.03753-24. https://doi.org/10.1128/mbio.03753-24 (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 10-12, lotoux2025defensearsenalof pages 12-15)
- Rose AE et al. **Commensal resilience: ancient ecological lessons for the modern microbiota.** *Infection and Immunity* (Jun 2025). DOI:10.1128/iai.00502-24. https://doi.org/10.1128/iai.00502-24 (rose2025commensalresilienceancient pages 9-11, rose2025commensalresilienceancient pages 7-9)
- Lagier J-C et al. **Current and past strategies for bacterial culture in clinical microbiology.** *Clinical Microbiology Reviews* (Jan 2015). DOI:10.1128/cmr.00110-14. https://doi.org/10.1128/cmr.00110-14 (lagier2015currentandpast pages 3-4)
- Nwaokorie FO et al. **Application of Anaerobic Techniques in Laboratory Diagnosis of Otitis Media in Nigeria: A Review.** (Jan 2021). DOI:10.52968/23689336. https://doi.org/10.52968/23689336 (nwaokorie2021applicationofanaerobic pages 1-2)


References

1. (lagier2015currentandpast pages 3-4): Jean-Christophe Lagier, Sophie Edouard, Isabelle Pagnier, Oleg Mediannikov, Michel Drancourt, and Didier Raoult. Current and past strategies for bacterial culture in clinical microbiology. Clinical Microbiology Reviews, 28:208-236, Jan 2015. URL: https://doi.org/10.1128/cmr.00110-14, doi:10.1128/cmr.00110-14. This article has 867 citations and is from a highest quality peer-reviewed journal.

2. (nwaokorie2021applicationofanaerobic pages 1-2): F.O. Nwaokorie, N.N. Nwokoye, and E.E. Chukwu. Application of anaerobic techniques in laboratory diagnosis of otitis media in nigeria: a review. University of Lagos Journal of Basic Medical Sciences, 5:21-31, Jan 2021. URL: https://doi.org/10.52968/23689336, doi:10.52968/23689336. This article has 3 citations.

3. (lotoux2025defensearsenalof pages 1-2): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. mBio, Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (lotoux2025defensearsenalof pages 10-12): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. mBio, Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (caulat2024physiologicalroleand media fefcabd0): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

7. (lotoux2025defensearsenalof pages 12-15): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. mBio, Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (okabe2023oxygentoleranceand pages 5-6): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

9. (okabe2023oxygentoleranceand pages 6-7): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

10. (botin2023thetoleranceof pages 5-7): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 19 citations and is from a peer-reviewed journal.

11. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 19 citations and is from a peer-reviewed journal.

12. (keitel2023carbondioxideand pages 1-2): Laura Keitel, Kristina Braun, Maurice Finger, Udo Kosfeld, Stanislav Yordanov, and Jochen Büchs. Carbon dioxide and trace oxygen concentrations impact growth and product formation of the gut bacterium phocaeicola vulgatus. BMC Microbiology, Dec 2023. URL: https://doi.org/10.1186/s12866-023-03127-x, doi:10.1186/s12866-023-03127-x. This article has 10 citations and is from a peer-reviewed journal.

13. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 52 citations and is from a highest quality peer-reviewed journal.

14. (rose2025commensalresilienceancient pages 7-9): Abigail E. Rose, Ryan T. Fansler, and Wenhan Zhu. Commensal resilience: ancient ecological lessons for the modern microbiota. Jun 2025. URL: https://doi.org/10.1128/iai.00502-24, doi:10.1128/iai.00502-24. This article has 9 citations and is from a peer-reviewed journal.

15. (rose2025commensalresilienceancient pages 9-11): Abigail E. Rose, Ryan T. Fansler, and Wenhan Zhu. Commensal resilience: ancient ecological lessons for the modern microbiota. Jun 2025. URL: https://doi.org/10.1128/iai.00502-24, doi:10.1128/iai.00502-24. This article has 9 citations and is from a peer-reviewed journal.

16. (okabe2023oxygentoleranceand pages 12-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

17. (thomashoff2024survivalofoxidative pages 46-48): UL Thomashoff. Survival of oxidative stress-adapted bifidobacterium spp. in yoghurt. Unknown journal, 2024.